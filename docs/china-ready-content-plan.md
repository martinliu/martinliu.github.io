# Chinaready 内容排期（C 阶段）

2026-09-30 与 Martin 确认的执行方案。上游背景见 `martinliu-cn-mvp-commercial-todo.md`。

## 统一追踪入口（已定）

```
https://chinaready.co/diagnose/?utm_source=martinliu.cn&utm_medium=blog&utm_campaign=china-ready
```

- 域名：chinaready.co（现有 MVP，已验证 `/diagnose/` 返回 200）
- 全站唯一出口：已封装为 `layouts/shortcodes/china-ready.html`，改文案/URL 只动这一个文件
- 专题页：`/chinaready/`（中）与 `/en/chinaready/`（英），导航已加 Chinaready 入口

## 三篇文章（并行排期，大纲已定）

通用规范：每篇为 `content/post/<slug>/index.zh-cn.md` 页面包；封面用 front matter `image:`；文末唯一 CTA 用 `{{< china-ready >}}`；英文版 `index.en.md` 同步。封面素材均来自 chinaready.co 官方图库（已核实内容与尺寸），写作时复制进各自 page bundle 即可。

### 文章一：为什么你的海外站在中国大陆很慢、还不稳定？

- **Header 配图**：`insight-aws-china.webp`（数据中心机房 + 网络光束，1536×1024，142KB）；备选 `insight-azure-china.webp`。源：`https://chinaready.co/images/home/insight-aws-china.webp`
- **目标读者**：出海 SaaS/产品团队的技术决策人
- **大纲**：
  1. 开篇钩子：同一个站点、两份体检报告——海外与大陆的数据反差（用本站真实测量开场）
  2. 先分清两类问题：不可用（部分地区/运营商解析或连接失败）vs 性能差（能开但慢）；两者的排查路径完全不同
  3. 分层拆解"慢"的来源：DNS 调度 → 跨境链路质量 → CDN 大陆覆盖与预热 → 源站位置 → 前端资源体积（高延迟放大器）
  4. "时好时坏"的机理：链路波动叠加"无边缘缓存、每个请求裸奔回源"（引用本站案例：9 月 5xx 5.8%、504 集中在首页；加缓存规则后 TTFB 0.7s→0.26s）
  5. 一份可自检清单：dig/nslookup 看解析落地、多地拨测、分地区 TTFB（Core Web Vitals）、资源瀑布图
  6. 结尾 CTA：`{{< china-ready >}}`
- **数据论据**：CF GraphQL 9 月数据、优化前后对比、Web Analytics CWV（中国访客）

### 文章二：进中国市场技术就绪清单（SaaS/B2B 版）

- **Header 配图**：`insight-android-stores.webp`（智能手机 + 应用图标网格，1536×1024，66KB）。源：`https://chinaready.co/images/home/insight-android-stores.webp`
- **目标读者**：准备进中国的 SaaS/B2B 产品与平台团队
- **大纲**：
  1. 清单的使用方式：按五阶段自查（评估→加速→托管→分发→运营），每项给出"怎么验证已就绪"
  2. 网络与分发：DNS/CDN 策略、静态资源分发、第三方依赖在大陆的可达性（字体/分析/支付）
  3. 合规与备案：ICP 备案路径、域名策略（.cn vs 海外域名）、数据与隐私要点
  4. 应用分发：安卓渠道生态——主流应用商店清单与上架要求（正文用 `static/img/china-android-app-stores/` 的 logo 素材做视觉化清单）
  5. 可观测性：分地区真实用户监控、告警阈值、上线后的持续验证
  6. 结尾 CTA
- **备注**：安卓商店部分素材充足，若篇幅超限可拆为系列第二篇《中国安卓应用商店上架实务》

### 文章三：进中国前，CDN/DNS/ICP 与可观测性的常见踩坑

- **Header 配图**：`insight-icp.webp`（发光盾牌 + 中国地图，合规主题，1536×1024，28KB）。源：`https://chinaready.co/images/home/insight-icp.webp`
- **目标读者**：DevOps/SRE/平台工程师
- **大纲**：
  1. 踩坑合集形式，每坑三段式：现象 → 根因 → 修复
  2. CDN 坑：以为开了 CDN 就快（大陆无节点/未预热）、HTML 从不缓存导致每个请求回源、404 被边缘缓存卡住新页面上线、忽略 stale-if-error 类兜底
  3. DNS 坑：地理调度把大陆用户送到远端节点、TTL 过长无法快速切换、只测权威不测递归
  4. ICP 坑：备案与域名策略误区、被忽略的合规依赖（第三方脚本/字体也算内容）
  5. 可观测性坑：只有海外拨测、没有真实用户数据（RUM）、告警覆盖不到"慢"只有"挂"
  6. 案例主线：本站 2026-09 真实优化记录（504 治理、缓存规则、WAF 拦截、TTFB 对比）——第一手案例，最贴近 SRE 读者
  7. 结尾 CTA

> 写作顺序与发布节奏由 Martin 定；已核实的封面素材缓存在 chinaready.co 图库，无需另行设计。

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
