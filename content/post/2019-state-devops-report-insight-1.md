---
date: 2019-08-28T07:27:16+08:00
title: "如何做横向行业的DevOps表现基准测试？"
subtitle: "死磕2019年加速度全球DevOps状态调查报告系列，深度解读第一篇。"
description: "死磕2019年加速度全球DevOps状态调查报告系列，深度解读第一篇。"
categories: ["DevOps"]
tags: ["DevOps","DORA","Google"]
keywords: ["DevOps","DORA", "Report","2019"]
slug: "2019-state-devops-report-insight-1"
image: "https://res.cloudinary.com/martinliu/image/upload/v1567000726/1-jafadjf.jpg"
---

长期关注我的blog和微信公众号（DevOps教练）的朋友可以发现，我今年从这个调查问卷开始，陆续发布了一些列文章。如果给这些文章一个文集标题的话，那么应该是：死磕2019年加速度全球DevOps状态调查报告系列。 为了帮助大家充分利用这份优秀的行业报告，我会用一些列文章，分章节的解读这份长达80多页的报告。上一篇文章如果你已经解读了该报告的核心重要发现和看点。本文要覆盖的章节是 How do we compare 这一章。

本文的阅读建议：

* 先阅读和参考前5年的DevOps状态调查报告，了解今年这份报告的历史和发展历程。以前的文章中有下载链接/二维码。
* 阅读2019年的调查问卷的中文版，感谢中国DevOps社区翻译团队对英文原版问卷的翻译工作，如果你都不知道这些调查结果是通过什么问卷调查得出的，那真的是很可惜。如果你想用这套问卷工具在企业内部做调研，请使用前文中的免费调查服务申请流程。样例问卷的访问地址：<https://www.wjx.cn/jq/43837840.aspx>
* 在Google的网站上做极简版DevOps行业基础测试，它是6年行业调查结果数据库的首次对外开放。

## WHY DEVOPS？

这是一个可以持续反复问自己的问题，首先让我们澄清一件事情：为什么要做DevOps？

是否是为了提高研发效能？是否是为了提高生产力？是否是为了提高效率？这些答案可能都对，也可都不对。对于一个组织而言：如果IT对它的使命和目标至关重要的情况下，组织对IT会产生强依赖关系，DevOps才对该组织才有意义。历年来的DevOps状态调查告诉我们：DevOps对于那些以IT为命脉的组织而言直观重要，对所有从事软件交付的组织广泛有效。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/12-23ru83.png)

从DevOps能力成长模型中可以看出，图中的诸多能力项都正向贡献/预测到最右侧的两个组织级别目标，他们是：组织效能和非商业效能（商业和非商业目标），它们是：

* 盈利能力 （商业）
* 生产力
* 市场份额 （商业）
* 客户数量 （商业）
* 产品或服务的数量 （商业）
* 运营效率
* 客户满意度 （商业）
* 提供的产品或服务的质量  （商业）
* 实现组织或使命目标

如果你的某项/某几项DevOps实践能够直接贡献到以上的商业目标，或者说能持续的创造客户价值，即商业价值；那么你的DevOps就是成功的。反之，如果你仅仅期望研发效能、生产力、效率能够就等同于创造出了很多的客户价值，那是一种幻觉；这就像是：你经过了很多预赛和体能的准备，而在冠军争夺赛中，你依然名落孙山，当你的组织的绩效远远低于预期的商业目标的时候，你的各种XXX效率都是无用的。

## 四大黄金度量指标

6年来的DevOps状态调查报告（我只关注DORA主导和执行的这个）已经在用量化的方式，帮助我们作出了精英表现者的画像，当然还有其它的落后者。可以明确的一点是：强者从四个维度上同时都表现强劲。（去年已经打破了常见的一个误区：过度的保守主义导致在组织四个指标之中做折中选择，常见的是牺牲吞吐量指标，确保稳定性，可是后果往往是相反的。）

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/10-2373.png)

先来回顾和梳理所谓的四大黄金度量指标的分类：

* **吞吐量--部署频率**：对于您工作的主要应用程序或服务，您的组织在生产环境进行代码部署或向最终用户做发布的频率。调查这个指标的问题见2019年加速度DevOps状态调查问卷中的第二部分的第二题。
* **吞吐量--前置时间**：对于您工作的主要应用程序或服务，从代码提交到在生产中成功运行的过程需要的时间。调查这个指标的问题见2019年加速度DevOps状态调查问卷中的第二部分的第一题。
* **稳定性--服务恢复时间**：对于您工作的主要应用程序或服务，当服务中断或出现影响用户Bug时（如：计划外中断、服务受损），恢复服务通常需要的时间。调查这个指标的问题见2019年加速度DevOps状态调查问卷中的第二部分的第四题。
* **稳定性--变更失败率**：对于您所工作的主要应用程序或服务，对于生产变更，或向最终用户发版的变更，百分之多少会导致服务质量下降（如：服务受损或服务中断），并需要进行后续的修复工作（需要热补丁、回滚，前向修复，打补丁修复）。调查这个指标的问题见2019年加速度DevOps状态调查问卷中的第二部分的第五题。

上面的四个指标是DevOps状态调查报告使用cluster算法做受众分类的主要依据，这个类聚分析的结果就是那张四大DevOps等级的泡泡图。

![](https://res.cloudinary.com/martinliu/image/upload/v1567001372/11-w97459438isuuf.png)

在这个泡泡图中，我们可以看到有多少比例的受访者处于精英、高效、中等和低效的阵营。复述一下今年的一个重大发现：精英表现者已经从去年的高效能表现者集团中脱颖而出，他们在指标的绝对值和总体数量上都增长迅敏，增长率高达将近3倍。*【DevOps教练点评：回顾一下这份报告的标题中加入的加速度的关键字，一旦某个组织的实施方法得当，一个持续优化的组织的整体效能就可能做上火箭，加速度的飞离地球。而加速度不足的企业则处于持续跌回地面的窘境。】*

这四大黄金度量指标的采集方法就是调查问卷中那些四个问题。对所有实践DevOps的组织而言，我们需要的是持续实施和优化追踪这些度量指标的方法和系统，确保能实时查看这四个指标的状态是最完美的。可是目前几乎还没有什么企业能够做到，手工分别统计上报，定期公布到全体IT部门也是非常可取的做法。总之，没有度量就不存在管理，就无从系统性的改进。

## 我在行业里的表现如何？

这是我写作本文想要回答的核心问题。如果你能够度量自己的四个黄金指标了，也能够随时拿出一组确切的数据，我们就能做行业基准测试比较了。

这可能是Google收编DORA团队所买到的最有价值的一部分资产，历年来的DevOps调查问卷参与者的问卷答案数据库。Google今年将这个数据库向公众开放了，网址在 <https://beta.devops-research.com/performance.html> (这个网址应该不用科学上网，会出现证书错误提示，请忽略继续访问该页面)。在你回答了下面的五个问题后，就可以获得一份自己的行业基准测试报告。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/2-faldjfald.png)

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/3-adfjafdasldf.png)

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/4-9578921374.png)

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/5-faljdfl2e44.png)

最后一个问题是，从13个行业中选择出一个最合适的所在行业。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/6-ajflasjfd22.png)

下图是你在整个所有行业里的横向对比。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/7-fjlasf.png)

下图是你在所在行业里的横向对比。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/8-ajflasjf2.png)

下图是四个黄金指标在四个表现级别/集团上的度量；表明你每个指标处于哪个等级。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/9-asjfl23uu.png)

经过以上的最简版DevOps表现状态基准测试以后，你就看到了你在所有行业中和所在行业中的横向比较。当然，我们也能预测一下自己处于那个阵营和等级。然而，这并不是你的DevOps旅程的剧终情节。

所有DevOps的实践者一旦上路以后，都是一条不归路的感觉，我们可以定期的关注我们的基准测试结果，并观察自己在动态变化的行业基线中的位置，而更重要的是：找到每个现阶段的改进空间，并且持续突破自己DevOps的能力瓶颈和极限。持续的无限制的加速度发展所有DevOps能力点才是这个DevOps旅程的终极意义。

## 关于服务运维效能

服务效能指标是在去年的效能报告中新引进的，而在去年和今年的调查问卷和结果报告中并没有直接的关于这项指标的采集数据和结果。

![](https://res.cloudinary.com/martinliu/image/upload/v1567000726/10-2373.png)

从上图中我们可以直接的理解一下，左侧的四大黄金指标都关乎于软件开发部门，而这个指标关乎于服务运维部门。去年并没有给出关于可用性指标的度量方法，今年也没有在调查问卷中做直接/显性的问题设置。只是在今年2019年的报告中做了进一步的解释，说这个可用性指标的实施方法论是SRE套路。我正在翻译SRE Workbook，这本书比起之前翻译的DevOps Handbook，更具有实操性。我们拭目以待，明年的状态调查问卷是如何对可用性设问和调查分析的。关于SRE的基础概念和实施方法，心急的朋友不妨参加中国DevOps社区今年10月在杭州举办的年度大会，我有一个关于SRE的主题分享，让我们一起讨论SRE的落地套路，让用SRE套路使我们的DevOps故事闭环。

总之我们实践DevOps的时候要全局的关注“软件交付和运维效能”，简称SDO效能（software delivery and operational performance）；有O了才完整的闭环了。

## 总结

本文写道这里，我认为你可以无障碍的阅读2019年加速度全球DevOps状态调查报告到第25页了。我们总结一下，你应该能理解吞吐量和稳定性的四大黄金度量指标的定义；持续度量和关注这些指标的正确方法；使用Google所提供的极简版度量工具，找到自己在行业中的定位和所处的效能级别。关注SDO效能的完整性，尝试了解和实践SRE实践，让你的DevOps体验闭环和完整起来。下一期死磕2019年加速度全球DevOps状态调查报告系列将为你呈现更新版本的DevOps能力成长模型，进一步讲解如何应用今年分化出来的两个研究模型：SDO和组织效能模型与生产力模型。

-------
