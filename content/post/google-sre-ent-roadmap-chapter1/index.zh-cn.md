---
title: "《企业 SRE 路线图》第一章：初探企业 SRE "
date: 2024-04-30T21:41:05+08:00
description:  Google SRE 整理了一些建议，希望能帮助到更多企业。通过评估企业现有的环境、设定合理的预期，并确保企业朝着正确的方向迈出正确的步伐，企业可以从评估 SRE的原则和实践，从评估SRE在组织中的运作方式开始。
slug: google-enterprise-roadmap-to-sre-chapter1
image: pexels-anete-lusina-4792380.jpg
categories:
    - SRE
tags:
    - Google
    - 白皮书
comments: true
toc: true

---

>译者：刘征

* [下载中文版 PDF 文件](/wp/enterprise-roadmap-to-sre-cn.pdf)
* [下载英文版 PDF 文件](/wp/enterprise-roadmap-to-sre.pdf)
* [从 Oreilly 阅读白皮书](https://www.oreilly.com/library/view/enterprise-roadmap-to/9781098117740/)
* [从 Google 下载白皮书](https://sre.google/resources/practices-and-processes/enterprise-roadmap-to-sre/)

将 SRE 导入当前的各种传统企业，是一项看似可能艰巨的工作，因此 Google SRE 整理了一些建议，希望能帮助到更多企业。通过评估企业现有的环境、设定合理的预期，并确保企业朝着正确的方向迈出正确的步伐，企业可以从评估 SRE的原则和实践，从评估SRE在组织中的运作方式开始。

## 演进优于革命

企业的一个显著特点是：会始终拥有以前的 IT/管理信息系统（MIS）方法和原则的历史，Google SRE将详细讨论一些常见的方法。无论当前状态如何，Google SRE发现在采用 SRE 时，选择通过演进和补充现有框架的方式，而不是直接与其对抗会取得最大成功。此外，SRE 与其他任何技术的采用过程类似，都会受到历史遗留的影响（参见维基百科关于路径依赖的页面）。简而言之，这意味着：在像企业这样的复杂系统中，在不同地方应用相同的改变，也将产生出不一致而非收敛的结果。Google SRE将从一些成功的采用了不同的流行框架的示例开始讨论。

## SRE 实践可与 ITSM 框架共存

信息技术基础架构库（ITIL）是一组详细的 IT 活动实践，如 IT 服务管理（ITSM）。并非每个企业都使用 ITIL，但如果企业的相关组织在一定程度上采用过 ITIL，则应准备好 SRE 和 ITIL 实践之间会存在着重叠。此外，由于 ITIL 是一个框架，企业的定制化实施可能与库中的内容有很大差异。

>关键点：ITIL 有五本核心书籍，用数千页的篇幅涵盖了：关于如何构建和运行 IT 服务的内容，其中的很多主题与可靠性无关，也有很多内容故意未被 SRE 涵盖。ITIL 是一个框架，而 SRE 是一组实践，因此它们肯定是兼容的，但是在翻译术语（例如，“warranty”，“utility” 等）时可能会遇到挑战。此外，SRE 在变更管理和服务的拥有权等领域有着明确的观点，因此即使结果是一致的，也要做好调整的准备。

对于调和现存的一些常见 SRE 的反模式，可能也会比较有挑战。变更咨询委员会（CAB）是变更控制的常见模式。SRE 所秉持的持续交付的方式，意味着要让这个机构简化和战略化：企业可以在 Google 的 DevOps 研究和评估（DORA）的文章中，了解到更多有关简化变更审批的内容。类似地，对于网络运维中心（NOC，或者中国的 ECC）而言，则应该将其从事件驱动模型转变为更具前瞻性的方式，重点是对其进行自动化和赋能。在这两种情况下，重点是演进当前的运作模式，而非立即替换它们。

## DevOps/敏捷/精益

DevOps 有多种定义。为了简单起见，Google SRE 假定它包括其他方法的相关部分，如敏捷（SAFe、DAD 和 LeSS）和精益（Six Sigma、看板）。Google 的 DORA 研究表明，SRE 和 DevOps 是互补的，因此如果企业的组织在一定程度上采用了 DevOps，则通常会有所裨益。与 ITIL 一样，我们要预见到 SRE 和 DevOps 实践存在着一些重叠，并且企业的定制化实施可能与《DevOps Handbook - DevOps 实践指南》存在着广泛的差异。Google SRE将在后面更详细地介绍特定的 SRE  实践，但 SRE 与 DevOps 相关最大的许多能力（例如版本控制、同行评审等）也通常被视为采用 SRE 的先决条件。无论企业选择通过 DevOps 还是 SRE 倡议来构建这些能力，这些都由企业来决定，但为了确保采用 SRE 的成功，那些重要的 DevOps 能力仍然需要提前准备继续。

>关键点：当企业在调和  DevOps  和  SRE  的差异时，倡议务实的原则；想要完成大规模演进变革的成功，还是要通过迭代和循序渐进的方式来实现。重要的是：需要把特定的工作活动拆解出来，并专注于对人员的赋能，而不是花费不必要的时间和精力来获取一个完美的“空架子”。

尽管 DevOps 和 SRE 是互补的，但它们在一些领域还可能会令人难以调和。例如，企业可能已经决定将开发和运维报告层次结构替换为跨职能的 DevOps 团队。在这种情况下，重新引入像 SRE 这样的专门职能则需要进行认真的考虑。

### 千里之行，始于足下

无论您的企业正在使用着什么方法和框架，了解并诚实地对待企业今天的现状都很重要。正如《Google SRE 运维解密》 一书所言，“希望不是一种策略！” 如果企业认为：当前的企业环境中即没有任何缺失，也不存在任何改进的机会，那么企业应该问自己：为什么要采用 SRE。同样，企业现有的一些技术或员工的想法，在刚开始的时候，看起来也可能与企业的 SRE 愿景并不一致。在做出任何改变以前，花时间来了解这些也很重要。

### 明确企业的期望和愿景

接下来，企业了解自己期望的结果很重要。SRE 会包含许多技术和文化的组成部分，但它们都指向一个相同的目标，即：实现可靠性的目标。企业应该提前预计到：企业需要花费大量的时间和精力，来定义SRE 的技术和文化与现有框架的交互方式。只是简单地说“提高可靠性”是行不通的。同样，如果企业期望的结果与可靠性无关（例如：成本、速度），那么就需要准备额外的工作成本，来让SRE 实践与企业的整体愿景进行适配。

### SRE 开始与人

随着时间的推移，流程和技术会潮起潮落，而人员和实践则能够接受和适应它们。如果，企业是从培训和招聘开始的，那么企业可以不断的添加或删除技术和流程。而建立 SRE 能力则是一个渐进的过程；所以，不要试图通过简单的招聘来取得成功。将招聘看做是培训方式的一种加强版，而不是取代培训。记住，SRE 需要一种 “生机文化”（与病态和官僚的企业文化并列） 才能取得成功，所以确保这一点至关重要。

### 拥抱自身的特殊性

在企业的某个特定组织内采用 SRE，其实并没有一个标准化的最佳实践的做法。企业能成功的方式才是它唯一正确的方式。Google SRE 现在已经对很多组织的工作成果进行了大量的研究，知道了一些行之有效的方式，还有一些无效的做法；然而，企业必然还是会犯一些新颖的错误。将这些组织的经验视为真正的学习工具，将各种有效的改进循环融入你当前的企业的组织中。

Feature picture ❤️ Anete Lusina: <https://www.pexels.com/photo/miniature-toy-car-on-top-of-monopoly-board-game-4792380/>
