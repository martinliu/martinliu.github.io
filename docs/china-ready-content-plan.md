# Chinaready 内容排期（C 阶段）

2026-09-30 与 Martin 确认的执行方案。上游背景见 `martinliu-cn-mvp-commercial-todo.md`。

## 统一追踪入口（已定）

```
https://chinaready.co/diagnose/?utm_source=martinliu.cn&utm_medium=blog&utm_campaign=china-ready
```

- 域名：chinaready.co（现有 MVP，已验证 `/diagnose/` 返回 200）
- 全站唯一出口：已封装为 `layouts/shortcodes/china-ready.html`，改文案/URL 只动这一个文件
- 专题页：`/china-ready/`（中）与 `/en/china-ready/`（英），导航已加 Chinaready 入口

## 三篇文章（并行排期）

| # | 选题 | 核心论据（已有） | 目标读者 | 单一转化动作 |
|---|------|------------------|----------|--------------|
| 1 | 为什么海外站在中国大陆慢/不稳定 | 9 月站内 CN 侧 5xx/时延数据、跨境链路分层模型 | 出海产品/平台团队 | 免费诊断 |
| 2 | 进中国市场技术就绪清单 | chinaready.co 服务结构（评估/加速/托管/分发）；`static/img/china-android-app-stores/` 应用商店素材并入本篇 | 准备进中国的 SaaS/B2B | 清单下载或诊断 |
| 3 | 进中国前的 CDN/DNS/ICP/可观测性踩坑 | 本站自身优化案例（缓存规则前后 TTFB 0.7s→0.26s、504 治理） | DevOps/SRE 从业者 | 免费诊断 |

写作顺序与发布节奏由 Martin 定；每篇结构遵循：问题 → 分层原因/清单 → 可验证的改进路径 → 单一 CTA。

## 10 篇旧文加 CTA（文末统一模块）

选择标准：主题相关（DevOps/SRE/Cloudflare/CDN/DNS/性能/中国可访问性）× 流量。9 月请求量参考（来自 CF 边缘数据）：

- /blog/magic-quadrant-observability-platforms-2025/（97）
- /blog/incident-metrics-in-sre/（67）
- /blog/sre-best-practices-for-capacity-management/（64）
- /blog/ai-reliability-engineering-welcome-to-the-third-age-of-sre/（60）
- /blog/anatomy-of-an-incident-ch5/（58）
- /blog/stop-using-jenkins-in-2025/（54）
- /blog/devopscoach-weekly-2/（54）
- /blog/macmini-m4-homelab-redesign/（58）

> 以上仅为热点参考，最终 10 篇按"主题相关性优先"复核；每篇文末只加 `{{< china-ready >}}` 一个 CTA。

## 转化漏斗（以 Cloudflare Web Analytics 为基线）

文章浏览 → CTA 点击（UTM 到达 chinaready.co）→ /diagnose/ 页 → 提交诊断请求

成功信号（沿用商业待办文档）：相关文章 1% 点击率；月独立访客 0.1% 成为合格线索。
