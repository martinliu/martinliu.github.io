---
title: "Google 白皮书 《事故管理剖析》第七章 总结与展望"
date: 2024-07-06T12:46:48+08:00
description:  Google 的生产服务事故管理方法，Google 编写这份报告（白皮书）是为了分享&总结一份：技术事故响应实践的指南。
slug: anatomy-of-an-incident-ch7
image: pexels-pixabay-69934.webp
categories:
    -  SRE
tags:
    - incident
    - 事故管理
    - Google
    - 白皮书
comments: true
toc: true
---

* [下载中文版 PDF 文件](/wp/anatomy-of-an-incident-cn.pdf)
* [下载英文版 PDF 文件](/wp/anatomy-of-an-incident.pdf)
* [从 Google 下载白皮书](https://sre.google/resources/practices-and-processes/anatomy-of-an-incident/)

我们探讨了事故的基础知识，并详细了解了事故管理生命周期的三个阶段：准备、响应和恢复。这涵盖了很多内容，但你现在可能会想，“接下来该怎么做？”

首先，要学会在适当的时候使用事故管理。事故响应需要大量人力资源。通常需要一个或多个人参与其中，从最初的告警，到问题解决的整个过程中。事故响应的目的是在问题发生时实施缓解措施，以争取时间来做出优先级决策。这意味着常规的产品修复可能会被推迟，长期计划和改进可能不会被优先考虑。事故响应可能导致服务质量目标 (SLO) 被违反或客户承诺无法履行，并且参与事故响应的员工都会感受到较大压力。

有研究表明，现实世界中的第一事故响应者更容易出现倦怠和疲劳；同样的趋势也适用于处理非现实事故的人——即那些工作与生活不平衡、活动极端或可能缺乏控制的员工。这些因素在技术事故管理工作中很常见，意味着员工可能会感受到倦怠的影响和职业后果。这里的风险包括，最好的情况下是工作表现不佳，最坏的情况下是员工流失。由于这种倦怠产生的相关风险，公司必须尽量做好事故管理，并尽可能减少事故管理的频率。

你的下一个行动是将**事故管理**视为一项关键运维学科，并努力在这方面取得出色的表现。那么，什么是“擅长”事故管理呢？这意味着你的团队（而不仅仅是个别人员）需要积极改进这一循环的所有部分。虽然这听起来不像是：有几个超级英雄消防员冲了进来，他们拯救世界的场景那么戏剧化，但英雄主义心态是有害的。缓慢而仔细地改进事故准备，开发响应事故的工具、技术和通信渠道，并优先考虑可持续和可扩展的工程工作，才是强大事故管理实践的核心。

通过将所有内容视为一个连续且相互关联的循环，每个人都变得重要，并且可以避免将责任归咎于任何一个人或系统组件。无责文化的实践营造了一个心理安全的工作环境，让员工能够在其中蓬勃发展，并创造出色的产品。这些方法帮助谷歌度过了最近全球历史上的巨大不确定时期，也可以帮助提高贵公司的韧性。

总体而言，不要将事故管理应用于每一个潜在问题或类型问题。谨慎而合理地使用事故管理，以避免让团队成员感到倦怠。当你完成事故管理时，停止管理事故，开始进行解决长期问题或风险所需的工程工作。识别并使用其他可能有用的工具。

## 进一步阅读

* 来自《Google SRE 工作手册》的监控 <https://sre.google/workbook/monitoring/>
* 来自《Google SRE 工作手册》的事故响应 <https://sre.google/workbook/incident-response/>
* 来自《Google SRE 工作手册》的事后分析文化：从失败中学习 <https://sre.google/workbook/postmortem-culture/>
* 事后分析行动项目：计划工作并执行计划 <https://research.google/pubs/postmortem-action-items-plan-the-work-and-work-the-plan/>
* 使用 SRE 原则减少生产事故影响——CRE 实战经验 <https://cloud.google.com/blog/products/devops-sre/shrinking-the-impact-of-production-incidents-using-sre-principles-cre-life-lessons>
* 缩短生产事故缓解时间——CRE 实战经验 <https://cloud.google.com/blog/products/management-tools/shrinking-the-time-to-mitigate-production-incidents>

## 参考书目

* “Google Data Center FAQ”。《Data Center Knowledge》，2017 年 3 月 19 日。<https://www.datacenterknowledge.com/hyperscalers/google-data-center-faq>
* Aleksandra. “63 Fascinating Google Search Statistics”。《SEOtribunal》，2018 年 9 月 26 日。<https://seotribunal.com/blog/google-stats-and-facts/>
* “Incident Command System Resources”。美国联邦紧急事务管理局，美国国土安全部，2018 年 6 月 26 日。
* Beyer, Betsy, Chris Jones, Niall Richard Murphy 和 Jennifer Petoff 编辑。 《Site Reliability Engineering: How Google Runs Production Systems》。O’Reilly Media，2016 年。
* “Data Access and Restrictions”。《Google Workspace Security Whitepaper》，2021 年 10 月。 <https://workspace.google.com/learn-more/security/security-whitepaper/page-7.html>
* Treynor Sloss, Benjamin. “An Update on Sunday’s Service Disruption”。《Inside Google Cloud (博客)》，Google Cloud，2019 年 6 月 3 日。 <https://cloud.google.com/blog/topics/inside-google-cloud/an-update-on-sundays-service-disruption>

## 致谢

作者感谢 Jennifer Mace, Hazael Sanchez, Alexander Perry, Cindy Quach 和 Myk Taylor 对本报告的贡献。

## 作者简介

**Ayelet Sachto** 是 GKE SRE 的站点可靠性工程师，曾在 Google UK 担任战略云工程师，并领导 EMEA 地区的 PSO-SRE 项目。在她 17 年的职业生涯中，她开发和设计了大规模应用程序和数据流，同时实施了 DevOps 和 SRE 方法。她是众多技术文章、演讲和培训的作者，包括 O’Reilly 课程 “SRE Fundamentals in 3 Weeks”，并在数十个会议上发言和领导了数百个工作坊。Ayelet 还是技术社区的积极成员和导师。在空闲时间，她喜欢创造各种东西，无论是厨房中的一道菜、一段代码，还是有影响力的内容。

**Adrienne Walcer** 是谷歌 SRE 的技术项目经理，专注于提高弹性，减少大规模事故对谷歌服务、基础设施和运营的影响。Adrienne 曾为谷歌的 O’Reilly 出版物 《A Practical Guide to Cloud Migration》作出贡献，并在最后一次 USENIX LISA 会议 (LISA21) 上就规模化事故管理发表演讲。在加入谷歌之前，Adrienne 曾在 IBM Watson Health (前身为 Explorys Inc.) 担任数据科学家，并在 Strong Memorial Hospital 和 Cleveland Clinic 从事生物统计工作。她拥有乔治华盛顿大学的系统工程硕士学位和罗切斯特大学的学士学位。在空闲时间，Adrienne 喜欢玩龙与地下城游戏，并在 Second Harvest 食品银行做志愿者。

> 来源： <https://sre.google> ；本白皮书一共有 7 章，后续章节将陆续发布。完整中文版白皮书即将发布，敬请期待。

![cover](/img/anatomy-of-an-incident.png)

❤️ Photo by Pixabay: <https://www.pexels.com/photo/photo-of-a-2-fireman-killing-a-huge-fire-69934/>
