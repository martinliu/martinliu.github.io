#!/usr/bin/env python3
"""GSC + GA4 拉数脚本 —— 6 个月内容计划的「数据复盘看板」数据源。

为什么要有它：计划的 5.1 看板要求每周一 30 分钟复盘，靠手工翻后台在第 3 周就会断掉。
这个脚本把「打开两个后台 → 抄数 → 填表」压成一条命令。

数据源
  - GSC：`sc-domain:martinliu.cn`（含子域），Search Console API v1
  - GA4：`properties/395618943`（Martin's Blog - GA4），Data API v1beta
  - 凭证：服务账号 JSON（默认 /Users/martinliu/secrets/clickhouse-cp-3be5ecbd401a.json，
          可用 --key 或环境变量 GSC_KEY_PATH 覆盖）。**凭证不进 git、不进输出。**

运行解释器（必须装了 google-api-python-client + google-analytics-data）：
  /Users/martinliu/.workbuddy/binaries/python/envs/default/bin/python scripts/pull_metrics.py

用法
  pull_metrics.py                       # 默认近 28 天，打印摘要
  pull_metrics.py --days 7              # 近 7 天
  pull_metrics.py --dashboard           # 追加一节到看板 markdown
  pull_metrics.py --dashboard-only      # 只刷看板，不打印长表
  pull_metrics.py --json out.json       # 存原始数据

退出码：0 成功；2 环境/凭证错误；3 两个数据源都拿不到数据。
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys

DEFAULT_KEY = "/Users/martinliu/secrets/clickhouse-cp-3be5ecbd401a.json"
GSC_PROPERTY = "sc-domain:martinliu.cn"
GA4_PROPERTY = "395618943"
GA4_PROPERTY_LABEL = "Martin's Blog - GA4"
SITE_LABEL = "martinliu.cn"
SITE_OUTBOUND_DOMAIN = "chinaready.co"      # 计划里的 B2B 目标

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")


# ------------------------------------------------------------------ 环境

def die(msg, code=2):
    print(f"✗ {msg}", file=sys.stderr)
    sys.exit(code)


def load_clients(key_path: str):
    if not os.path.exists(key_path):
        die(f"找不到服务账号密钥：{key_path}（用 --key 指定）")
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    scopes_gsc = ["https://www.googleapis.com/auth/webmasters.readonly"]
    creds_gsc = service_account.Credentials.from_service_account_file(key_path, scopes=scopes_gsc)
    gsc = build("searchconsole", "v1", credentials=creds_gsc, cache_discovery=False)

    ga4 = None
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        creds_ga4 = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/analytics.readonly"])
        ga4 = BetaAnalyticsDataClient(credentials=creds_ga4)
    except Exception as exc:                      # noqa: BLE001
        print(f"⚠ GA4 不可用（{type(exc).__name__}: {exc}）—— 只出 GSC 部分", file=sys.stderr)
    return gsc, ga4


# ------------------------------------------------------------------ GSC

def gsc_query(gsc, start, end, dims=None, row_limit=1000, filters=None):
    body = {"startDate": start.isoformat(), "endDate": end.isoformat(),
            "rowLimit": row_limit, "dataState": "all"}
    if dims:
        body["dimensions"] = dims
    if filters:
        body["dimensionFilterGroups"] = filters
    resp = gsc.searchanalytics().query(siteUrl=GSC_PROPERTY, body=body).execute()
    return resp.get("rows", [])


def gsc_totals(gsc, start, end):
    rows = gsc_query(gsc, start, end)
    if not rows:
        return {"clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0}
    r = rows[0]
    return {"clicks": r.get("clicks", 0), "impressions": r.get("impressions", 0),
            "ctr": r.get("ctr", 0.0), "position": r.get("position", 0.0)}


def gsc_rows_to_dicts(rows, dims):
    out = []
    for r in rows:
        d = dict(zip(dims, r.get("keys", [])))
        d.update(clicks=r.get("clicks", 0), impressions=r.get("impressions", 0),
                 ctr=r.get("ctr", 0.0), position=r.get("position", 0.0))
        out.append(d)
    return out


def is_english(q: str) -> bool:
    """不含 CJK 字符即视为英文查询词。"""
    return not CJK.search(q or "")


# 判定「疑似机器流量」：同一分辨率上会话量大、但会话时长≈0 且互动率≈0。
# 真人不会这样聚集 —— 正常人分布在几十种分辨率上，机器只需要两三种。
BOT_MIN_SESSIONS = 200        # 该分片至少这么多会话才值得怀疑
BOT_MAX_ENGAGEMENT = 0.05     # 互动率低于 5%
BOT_MAX_DURATION_S = 5.0      # 平均会话时长低于 5 秒


def split_human_bot(resolution_rows):
    """按分辨率切片，把 GA4 会话拆成「疑似机器」与「其余（真人近似）」。"""
    bot, human, details = 0, 0, []
    for r in resolution_rows or []:
        try:
            n = int(r.get("sessions") or 0)
            er = float(r.get("engagementRate") or 0)
            dur = float(r.get("averageSessionDuration") or 0)
        except (TypeError, ValueError):
            continue
        is_bot = n >= BOT_MIN_SESSIONS and er < BOT_MAX_ENGAGEMENT and dur < BOT_MAX_DURATION_S
        details.append({"resolution": r.get("screenResolution"), "sessions": n,
                        "engagement_rate": er, "avg_duration_s": dur,
                        "verdict": "疑似机器" if is_bot else "看真人"})
        if is_bot:
            bot += n
        else:
            human += n
    return bot, human, details


# ------------------------------------------------------------------ GA4

def ga4_report(ga4, metrics, start, end, dims=None, limit=25, order_by=None):
    from google.analytics.data_v1beta.types import (
        DateRange, Dimension, Metric, OrderBy, RunReportRequest,
    )
    req = RunReportRequest(
        property=f"properties/{GA4_PROPERTY}",
        date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
        metrics=[Metric(name=m) for m in metrics],
        dimensions=[Dimension(name=d) for d in (dims or [])],
        limit=limit,
    )
    if order_by:
        req.order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_by), desc=True)]
    resp = ga4.run_report(req)
    names = [d.name for d in resp.dimension_headers] + [m.name for m in resp.metric_headers]
    rows = []
    for row in resp.rows:
        vals = [dv.value for dv in row.dimension_values] + [mv.value for mv in row.metric_values]
        rows.append(dict(zip(names, vals)))
    return rows


# ------------------------------------------------------------------ 报告

def fmt_int(x):
    try:
        return f"{int(round(float(x))):,}"
    except (TypeError, ValueError):
        return "-"


def collect(gsc, ga4, days, months=4):
    today = dt.date.today()
    # GSC 数据有 2-3 天延迟，末端往前挪 3 天，避免末尾空档把均值拉低
    gsc_end = today - dt.timedelta(days=3)
    gsc_start = gsc_end - dt.timedelta(days=days - 1)

    out = {"generated_at": dt.datetime.now().isoformat(timespec="seconds"),
           "window": {"days": days, "gsc_start": gsc_start.isoformat(),
                      "gsc_end": gsc_end.isoformat(),
                      "ga4_start": (today - dt.timedelta(days=days - 1)).isoformat(),
                      "ga4_end": today.isoformat()},
           "gsc": {}, "ga4": {}}

    # --- GSC 汇总
    out["gsc"]["totals"] = gsc_totals(gsc, gsc_start, gsc_end)
    out["gsc"]["daily"] = gsc_rows_to_dicts(
        gsc_query(gsc, gsc_start, gsc_end, dims=["date"], row_limit=400), ["date"])
    out["gsc"]["daily"].sort(key=lambda r: r["date"])

    # --- 查询词
    q_rows = gsc_rows_to_dicts(
        gsc_query(gsc, gsc_start, gsc_end, dims=["query"], row_limit=5000), ["query"])
    q_rows.sort(key=lambda r: r["impressions"], reverse=True)
    out["gsc"]["queries_by_impressions"] = q_rows[:60]
    out["gsc"]["queries_by_clicks"] = sorted(q_rows, key=lambda r: r["clicks"], reverse=True)[:25]
    out["gsc"]["query_count"] = len(q_rows)
    out["gsc"]["english_query_count"] = sum(1 for r in q_rows if is_english(r["query"]))
    out["gsc"]["english_queries"] = [r for r in q_rows if is_english(r["query"])][:25]

    # --- 机会词：第 8-20 位、有展示、还没被点 —— 这是选题的富矿
    out["gsc"]["striking_distance"] = [
        r for r in q_rows if 7.5 <= r["position"] <= 20.5 and r["impressions"] >= 10
    ][:30]

    # --- 高展示零点击：标题/描述没接住的词
    out["gsc"]["high_impression_zero_click"] = [
        r for r in q_rows if r["clicks"] == 0 and r["impressions"] >= 20
    ][:20]

    # --- 落地页
    p_rows = gsc_rows_to_dicts(
        gsc_query(gsc, gsc_start, gsc_end, dims=["page"], row_limit=2000), ["page"])
    p_rows.sort(key=lambda r: r["impressions"], reverse=True)
    out["gsc"]["pages_by_impressions"] = p_rows[:30]
    out["gsc"]["page_count"] = len(p_rows)

    # --- 国家
    c_rows = gsc_rows_to_dicts(
        gsc_query(gsc, gsc_start, gsc_end, dims=["country"], row_limit=100), ["country"])
    c_rows.sort(key=lambda r: r["impressions"], reverse=True)
    out["gsc"]["countries"] = c_rows[:12]

    # --- GA4
    if ga4:
        ga4_end = today
        ga4_start = today - dt.timedelta(days=days - 1)
        try:
            out["ga4"]["totals"] = ga4_report(
                ga4, ["totalUsers", "sessions", "screenPageViews", "engagementRate"],
                ga4_start, ga4_end) or []
            out["ga4"]["channel_groups"] = ga4_report(
                ga4, ["sessions", "totalUsers"], ga4_start, ga4_end,
                dims=["sessionDefaultChannelGroup"], order_by="sessions")
            out["ga4"]["sources"] = ga4_report(
                ga4, ["sessions"], ga4_start, ga4_end,
                dims=["sessionSourceMedium"], order_by="sessions", limit=20)
            # ★ 流量质量：GA4 的总会话里混着大量非人类流量，
            #   单看「用户数」会得出完全错误的结论（本仓库 2026-10-10 实测踩过）。
            #   判据：同一分辨率上「会话很多 + 会话时长≈0 + 互动率≈0」即为机器。
            quality_metrics = ["sessions", "engagedSessions", "engagementRate",
                               "averageSessionDuration", "screenPageViews"]
            out["ga4"]["resolution_quality"] = ga4_report(
                ga4, quality_metrics, ga4_start, ga4_end,
                dims=["screenResolution"], order_by="sessions", limit=20)
            out["ga4"]["channel_quality"] = ga4_report(
                ga4, quality_metrics, ga4_start, ga4_end,
                dims=["sessionDefaultChannelGroup"], order_by="sessions", limit=10)
            out["ga4"]["language_quality"] = ga4_report(
                ga4, quality_metrics, ga4_start, ga4_end,
                dims=["language"], order_by="sessions", limit=10)
            # 出站到 chinaready.co 的点击（依赖 GA4 增强衡量里的「出站点击」）
            out["ga4"]["chinaready_outbound"] = ga4_report(
                ga4, ["eventCount"], ga4_start, ga4_end,
                dims=["linkDomain"], limit=50)
            # 近 N 个月
            monthly = []
            d0 = today.replace(day=1)
            for _ in range(months):
                m_end = (d0 - dt.timedelta(days=1))
                m_start = m_end.replace(day=1)
                rows_m = ga4_report(ga4, ["totalUsers", "sessions", "screenPageViews"],
                                    m_start, m_end)
                monthly.append({"month": m_start.strftime("%Y-%m"),
                                **(rows_m[0] if rows_m else {})})
                d0 = m_start
            out["ga4"]["monthly"] = list(reversed(monthly))
            # 本月进行中
            rows_m = ga4_report(ga4, ["totalUsers", "sessions", "screenPageViews"], today.replace(day=1), today)
            out["ga4"]["month_to_date"] = {"month": today.strftime("%Y-%m"),
                                           **(rows_m[0] if rows_m else {})}
        except Exception as exc:                  # noqa: BLE001
            out["ga4"]["error"] = f"{type(exc).__name__}: {exc}"
    return out


def render_markdown(d):
    L = []
    w = d["window"]
    L.append(f"## {w['gsc_end']} 数据快照（近 {w['days']} 天）\n")
    L.append(f"> 生成于 {d['generated_at']} ｜ 数据源：GSC `{GSC_PROPERTY}` + GA4 `{GA4_PROPERTY_LABEL}`\n")

    t = d["gsc"]["totals"]
    L.append("### GSC 搜索表现\n")
    L.append(f"- 窗口：{w['gsc_start']} ~ {w['gsc_end']}（GSC 有 2–3 天延迟，已自动前移）")
    L.append(f"- 点击 **{fmt_int(t['clicks'])}** ｜ 展示 **{fmt_int(t['impressions'])}** ｜ "
             f"CTR **{t['ctr']*100:.2f}%** ｜ 平均位次 **{t['position']:.1f}** ｜ "
             f"有展示的查询词 **{fmt_int(d['gsc']['query_count'])}** 个"
             f"（其中英文 **{fmt_int(d['gsc']['english_query_count'])}** 个）\n")

    sd = d["gsc"].get("striking_distance") or []
    if sd:
        L.append("### 机会词（位次 8–20、有展示、还没被点）—— 选题富矿\n")
        L.append("| 查询词 | 展示 | 点击 | 位次 | 类型 |")
        L.append("|---|---|---|---|---|")
        for r in sd[:15]:
            L.append(f"| {r['query']} | {fmt_int(r['impressions'])} | {fmt_int(r['clicks'])} | "
                     f"{r['position']:.1f} | {'EN' if is_english(r['query']) else '中文'} |")
        L.append("")

    zc = d["gsc"].get("high_impression_zero_click") or []
    if zc:
        L.append("### 高展示零点击（标题或描述没接住）\n")
        L.append("| 查询词 | 展示 | 位次 |")
        L.append("|---|---|---|")
        for r in zc[:12]:
            L.append(f"| {r['query']} | {fmt_int(r['impressions'])} | {r['position']:.1f} |")
        L.append("")

    pq = d["gsc"].get("queries_by_clicks") or []
    if pq and any(r["clicks"] for r in pq):
        L.append("### 真正带来点击的词\n")
        L.append("| 查询词 | 点击 | 展示 | CTR | 位次 |")
        L.append("|---|---|---|---|---|")
        for r in pq[:12]:
            if not r["clicks"]:
                continue
            L.append(f"| {r['query']} | {fmt_int(r['clicks'])} | {fmt_int(r['impressions'])} | "
                     f"{r['ctr']*100:.1f}% | {r['position']:.1f} |")
        L.append("")

    pp = d["gsc"].get("pages_by_impressions") or []
    if pp:
        L.append("### 落地页 Top（按展示）\n")
        L.append("| 页面 | 展示 | 点击 | 位次 |")
        L.append("|---|---|---|---|")
        for r in pp[:12]:
            page = r["page"].replace("https://martinliu.cn", "")[:70]
            L.append(f"| `{page}` | {fmt_int(r['impressions'])} | {fmt_int(r['clicks'])} | {r['position']:.1f} |")
        L.append("")

    cc = d["gsc"].get("countries") or []
    if cc:
        L.append("### 展示来源国家 Top\n")
        L.append("| 国家 | 展示 | 点击 | 位次 |")
        L.append("|---|---|---|---|")
        for r in cc[:8]:
            L.append(f"| {r['country']} | {fmt_int(r['impressions'])} | {fmt_int(r['clicks'])} | {r['position']:.1f} |")
        L.append("")

    g = d.get("ga4") or {}
    L.append("### GA4 流量\n")
    if g.get("error"):
        L.append(f"- ⚠ GA4 拉取失败：{g['error']}\n")
    else:
        tot = (g.get("totals") or [{}])[0]
        L.append(f"- 近 {w['days']} 天：用户 **{fmt_int(tot.get('totalUsers'))}** ｜ "
                 f"会话 **{fmt_int(tot.get('sessions'))}** ｜ "
                 f"浏览量 **{fmt_int(tot.get('screenPageViews'))}** ｜ "
                 f"互动率 **{float(tot.get('engagementRate') or 0)*100:.1f}%**")
        bot, human, details = split_human_bot(g.get("resolution_quality"))
        if bot:
            L.append(f"- 🚨 **流量质量告警**：{fmt_int(bot)} 个会话（{bot/(bot+human)*100:.0f}%）"
                     f"集中在少数分辨率上，且会话时长≈0、互动率≈0 → **疑似机器流量**。"
                     f"扣除后真人会话约 **{fmt_int(human)}**。")
            L.append(f"  - **不要用 GA4 的用户数当 KPI**，它会把机器算进去。")
        if details:
            L.append("")
            L.append("| 分辨率 | 会话 | 互动率 | 平均时长(s) | 判定 |")
            L.append("|---|---|---|---|---|")
            for r in details[:8]:
                L.append(f"| {r['resolution']} | {fmt_int(r['sessions'])} | "
                         f"{r['engagement_rate']*100:.1f}% | {r['avg_duration_s']:.1f} | {r['verdict']} |")
            L.append("")
        if g.get("channel_quality"):
            L.append("| 渠道 | 会话 | 互动率 | 平均时长(s) |")
            L.append("|---|---|---|---|")
            for r in g["channel_quality"][:8]:
                L.append(f"| {r.get('sessionDefaultChannelGroup')} | {fmt_int(r.get('sessions'))} | "
                         f"{float(r.get('engagementRate') or 0)*100:.1f}% | "
                         f"{float(r.get('averageSessionDuration') or 0):.1f} |")
            L.append("")
        mt = g.get("month_to_date") or {}
        if mt:
            L.append(f"- 本月（{mt.get('month')}）进行中：用户 {fmt_int(mt.get('totalUsers'))} ｜ "
                     f"会话 {fmt_int(mt.get('sessions'))}")
        if g.get("monthly"):
            L.append("")
            L.append("| 月份 | 用户 | 会话 | 浏览量 |")
            L.append("|---|---|---|---|")
            for m in g["monthly"]:
                L.append(f"| {m.get('month')} | {fmt_int(m.get('totalUsers'))} | "
                         f"{fmt_int(m.get('sessions'))} | {fmt_int(m.get('screenPageViews'))} |")
            L.append("")
        if g.get("channel_groups"):
            L.append("| 渠道 | 会话 |")
            L.append("|---|---|")
            for r in g["channel_groups"][:8]:
                L.append(f"| {r.get('sessionDefaultChannelGroup')} | {fmt_int(r.get('sessions'))} |")
            L.append("")
        ob = [r for r in (g.get("chinaready_outbound") or [])
              if SITE_OUTBOUND_DOMAIN in str(r.get("linkDomain", ""))]
        if ob:
            L.append(f"- 出站到 {SITE_OUTBOUND_DOMAIN} 的点击：**{fmt_int(ob[0].get('eventCount'))}** 次")
        else:
            L.append(f"- 出站到 {SITE_OUTBOUND_DOMAIN} 的点击：无数据"
                     f"（可能未启用「出站点击」增强衡量，或近 {w['days']} 天确实没有）")
        L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", default=os.environ.get("GSC_KEY_PATH", DEFAULT_KEY))
    ap.add_argument("--days", type=int, default=28, help="GSC 窗口天数（默认 28）")
    ap.add_argument("--months", type=int, default=4, help="GA4 回看的月数")
    ap.add_argument("--json", dest="json_out", help="把原始数据写到这个路径")
    ap.add_argument("--dashboard", action="store_true",
                    help="把渲染出的 Markdown 追加到看板文件")
    ap.add_argument("--dashboard-file",
                    default="/Users/martinliu/WorkBuddy/2026-10-04-10-18-55/outputs/analytics/dashboard.md")
    ap.add_argument("--dashboard-only", action="store_true", help="只刷看板，不打印长表")
    args = ap.parse_args()

    gsc, ga4 = load_clients(args.key)
    d = collect(gsc, ga4, args.days, args.months)

    if not d["gsc"]["totals"]["impressions"] and not d.get("ga4", {}).get("totals"):
        die("两个数据源都没拿到数据，检查服务账号权限。", code=3)

    md = render_markdown(d)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        print(f"✓ 原始数据 → {args.json_out}")

    if args.dashboard or args.dashboard_only:
        os.makedirs(os.path.dirname(args.dashboard_file), exist_ok=True)
        new = not os.path.exists(args.dashboard_file)
        with open(args.dashboard_file, "a", encoding="utf-8") as fh:
            if new:
                fh.write("# 数据复盘看板（martinliu.cn）\n\n"
                         "> 由 `scripts/pull_metrics.py --dashboard` 追加，每节一个数据快照。"
                         "**只增不改**，便于看趋势。\n\n---\n\n")
            fh.write(md + "\n---\n\n")
        print(f"✓ 看板已追加 → {args.dashboard_file}")

    if not args.dashboard_only:
        print(md)


if __name__ == "__main__":
    main()
