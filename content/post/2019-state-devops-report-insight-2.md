---
date: 2019-09-01T17:27:16+08:00
title: "怎样使用两个DevOps研究模型？"
subtitle: "死磕2019年加速度全球DevOps状态调查报告系列，深度解读第二篇。"
description: "死磕2019年加速度全球DevOps状态调查报告系列，深度解读第二篇。"
categories: ["DevOps"]
tags: ["DevOps","DORA","Google"]
keywords: ["DevOps","DORA", "Report","2019"]
slug: "2019-state-devops-report-insight-2"
image: "https://res.cloudinary.com/martinliu/image/upload/v1567000726/1-jafadjf.jpg"
---

本文要覆盖的章节是《 How to use the research models》 这一章。双模型在今年的报告中首次出现了，它们是效能模型和生产力模型。为什么会存在两个模型？有什么区别？有什么相似之处？最重要的问题是，你怎么用它们来指导你的DevOps工作？

本文的阅读建议：

* 下载我整理的最新版的《DevOps能力成长模型》，含双模型分解图。
* 阅读和参考前5年的DevOps状态调查报告，了解今年这份报告的历史和发展历程。以前的文章中有下载链接/二维码。
* 阅读2019年的调查问卷的中文版，感谢中国DevOps社区翻译团队对英文原版问卷的翻译工作，如果你都不知道这些调查结果是通过什么问卷调查得出的，那真的是很可惜。如果你想用这套问卷工具在企业内部做调研，请使用前文中的免费调查服务申请流程。样例问卷的访问地址：<https://www.wjx.cn/jq/43837840.aspx>
* 在Google的网站上做极简版DevOps行业基础测试，它是6年行业调查结果数据库的首次对外开放。

## 模型是怎么诞生的？

首先，我们需要了解一下这份持续了6年的报告是谁主导并开发的？这是一个怎样的团队？从DORA公司网站的这个页面上，可以看到团队人员介绍。<https://devops-research.com/about.html> 如下所示。

![](https://res.cloudinary.com/martinliu/image/upload/v1567336555/1sajldfkj.png)

不做其它任何解读和评论，只想请大家关注一下分析报告的主持者的title : Dr Nicole Forsgren, CEO and Chief Scientist ; 翻译一下 Nicole Forsgren 博士，CEO和首席科学家。她是一个长期的IT行业从业人员，最早专注于DevOps的行业调研员。她持有管理信息系统的博士学位和会计硕士学位。从社交媒体上可以看出她和行业大咖Jez Humber和Gene Kim都是好朋友。

其次，如果你也回顾了所有往届的DevOps状态调查报告，我们应该能体会到这场历时6年行业调研的基本逻辑和脉络。在第一年就已经提出了四大黄金度量指标，并且以此为主线；每年反复验证状态，以及其他相关影响因素。使用了**穷举**的逻辑，每年根据行业的发展动态，根据和其它业内大咖的讨论，适当的加入新的调查点。当然每个调查的能力点也是需要每年反复确认和验证，调查点之间的逻辑关系也越来越明显，经过二次研究之后就形成了DevOps能力成长模型。

最后，DevOps能力成长模型诞生于《Accelerate:The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations  》这本书。
<https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339>

![](https://res.cloudinary.com/martinliu/image/upload/v1530036828/Accelerate.jpg)

在这本书里分模块（局部）的介绍了DevOps能力模型的影响逻辑关系，从转型型领导力一直推导出模型的最右侧：组织效能和非商业效能。这个模型应该就是历届DevOps状态调查研究背后的理论基础，当然它也应该是慢慢发展和完善出来的，起码数字转型这个话题是2018年才出现的热点。模型的数值计算算法，见近两年报告的附录部分。这个模型在本书中是从各个不同的局部关系逐渐介绍的。如下图所示：

![](https://res.cloudinary.com/martinliu/image/upload/v1567337105/3-jsfjaksjf333.png)

Accelerate全书的逻辑不仅在于介绍各种DevOp实践、技术、文化、领导力等等相关因素有哪些，更重要的是揭示出这些影响因素（能力点）之间的关联关系。在书的最后展示了DevOps能力成长模型的全图，如下图所示：

![](https://res.cloudinary.com/martinliu/image/upload/v1567337168/4-ruwiur848.png)

Accelerate这本书也提供了这幅图的电子版下载链接：<https://devops-research.com/assets/transformation_practices.pdf>

这是一份非常棒的学习资料，如果你还没有买本书的话，也可以下载学习这份精华资料。这份文档的总标题是：”调研总体策划“，除了模型之外该文档还提供了一张全面复杂的表格，表格的名字：”高效能团队，管理、领导力行为和实践调查表，由Steve Bell，Karen Whitley Bell“；如果你想对自己的组织进行全面的调研的话，这也是一份优秀的调研方案。调研的矩阵如下：

* 纵向：文化、组织结构、直接学习和对齐价值、部署策略、通过分析提高流动性和训练有素的问题解决、工作方式节奏化&日常化
* 横向：团队实践、管理实践、领导力实践。

我很有幸2017年在北京DevOpsDays大会上参加Jez先生的培训，并获赠了Jez先生的签名版《Accelerate》纸版书，其实在这以前我已经购买了Kindle的电子版和Audible的有声书版。我反复研读了这本书的各种版本，再次强烈推荐所有DevOps相关的管理者一定要学习这本书。

以书中的模型为基础，2018年的DevOps状态报告里以又进一步做了各种扩展，如果你读过去年的报告，你可以看到如下的各种局部的扩展。

![](https://res.cloudinary.com/martinliu/image/upload/v1567337168/7asdfweruui238.png)

大家注意看2018年的这个局部模型图的标题”精益和敏捷实践“，这里也包含敏捷开发实践。我在反复琢磨这个模型之后，用Twitter私信问过Nicole博士。我问他为何没有专项调查过敏捷开发实践？模型上为何不给敏捷开发一个位置？她的回复是，我们之前已经调研过了，而且模型上也提到了。可能在全球的软件开发工程水平看，有可能Nicole博士团队认为敏捷开发应该是比较基础的软件开发实践，据我个人了解国外高水平公司要么都已经规范照做了，要么也有像Google这样的高水平公司确实也不显性的宣传自己是敏捷开发，甚至吐槽敏捷的。

![](https://res.cloudinary.com/martinliu/image/upload/v1567337168/8jfasjflsdf.png)

![](https://res.cloudinary.com/martinliu/image/upload/v1567337168/9ruwueriowur.png)

2018年对模型的扩展力度还是很大的，提出了很多新的调查项；为了能看到方便的看到一个DevOps能力模型的全景视图，我使用OmniGraffle软件基于《Accelerate》书中的模型，扩充绘制了如下的模型图：

![](https://res.cloudinary.com/martinliu/image/upload/v1567338260/12-23ru83.png)

这幅图向我们完整的揭示了到2018年以来的所有DevOps调研点，有些点是经过多年反复验证的，有些是2018年新引入的。这幅图花了我几天时间，在这个过程中也反复的推敲了其中的逻辑关系。这幅图仅代表我个人的观点，不代表DORA和《Accelerate》书籍的任何观点；需要声明的是：我绘制的DevOps能力成长模型并非我的个人著作，引用了DORA和《Accelerate》的著作，但我力求精确无误的表达整个模型。再次声明，这个模型图非官方出品，是我的个人研究。

研究模型的研究逻辑是穷举法，是从左到右的推导和影响关系。最新发布的2019年DevOps状态调查报告显示了新的变化，这触发了对以上模型的更新。本文将提供最新版高清大图的下载。

## 为何两个模型？

为何2019年会分化出两个模型，简单的讲：穷举的范围越来越大了，生产力作为一个新的全局共享目标进入了调查问卷的范围。我们之前社区的小伙伴已经将2019年的近100道调查题问题翻译成中文了，敬请参阅参考DevOps状态调研问卷。在翻译完那些题目后，我并没有意识到今年可能会新增出这样一个全局共享目标的调研对象，真的以为：这个效能模型（组织效能和非商业效能）会一条道走到最后。

### 效能模型

对效能模型的更新变化如下图所示：

![](https://res.cloudinary.com/martinliu/image/upload/v1567339754/2019-dora-perf.jpg)

### 生产力模型

新增的生产力模型令我感到相当意外，它的结构如下所示：

![](https://res.cloudinary.com/martinliu/image/upload/v1567339754/2019-dora-prod.jpg)

总之，还无法预测明年的调研范围会有怎样的更新。可以确认的是行业DevOps的能力模型是在动态变化的，想跟上世界级的水平还必须不断刷新自己的能力组合。否则你的同行的对手可能早就一骑绝尘而去了。DevOps能力发展不是一个有限游戏（例如刷黄金5级），是每年都和整个行业一起发展的无限游戏。

## 如何使用模型？

2019年的报告中给出了模型的使用和阅读方法的官方解释，见2019年报告英文原版的27页。本文对其的解读如下。

![](https://res.cloudinary.com/martinliu/image/upload/v1567379589/11-3kgsfdgjds.png)

### 使用模型指导转型

识别你将要改善的能力点。模型中的每个被箭头所指向的方块被称之为构造，构造有单级构造，也有二级构造（如精益产品开发、软件开发实践），历年来的报告中已经为你展示和所有DevOps能力点，你现在需要做的是从中选择出你需要改进的候选能力点。

开展加速度的组织转型需要一个前提条件，一个扎实的基础作为起点。报告中并没有解释这个条件，你需要自己理解。聚焦在转型所急需的那些候选能力点上，在多个候选能力点里选择出亟需改进的”约束点“「此处参考TOC限制理论，相关书籍《目标》」。想想：那些能力的不足造成了最大的延期？「记住这里说的是最大值，这需要一个量化的跨组织的分析调研」什么最让你头痛？什么是最大的问题？经过以上的引导问题的提示，从清单中选出3~5个候选优化发展的能力项，安排出专项人力和财力资源，先重拳出击改善第一波能力点。不要担心你还有其他的很多问题；现阶段不妨聚焦在那个最大的问题上；这样你才能将瓶颈（约束点）各个击破，发掘这个其他的协同功效，避免不必要的工作。这个部分基本上是经典TOC理论的应用，关于这个理论在DevOps实施中的详细使用方法描述，请参考《DevOps实践指南》的第二章 2.5 持续识别和改善约束点。

以上DevOps转型工作还有其他的产出。那些追求SDO组织效能的组织还会得到这些收益，降低职业透支（996icu）和部署的痛，提高安全水平。附加的好处还包括，它能提高生产力，提高了生产力就可以获得工作生活平衡且降低职业透支。

### 怎样阅读模型？

报告使用了结构方程模型 （Structural equation modeling <https://en.wikipedia.org/wiki/Structural_equation_modeling）> ，来作为一种预测模型，用它测试各个构造之间的关系。模型中的每个方块就是一个调研度量的点，就是一个构造。剪头表示了构造之间的关系。一个大的包含多个构造的方框称之为二级构造。淡蓝色的构造表示一个控制变量，它用点线连接。

在报告原文中，将第31页和57页的模型称之为全模型，见报告的27页的原文：”See pages 31 and 57 for full models.“；而在我的系列文章中，则将下图称之为全模型。

![](https://res.cloudinary.com/martinliu/image/upload/v1567339751/2019-dora-DevOps-all.jpg)

以上阅读方法同样的适用于上图。总之请仔细理解了左下角的图例，正确的阅读和理解模型。不管你是将DevOps实践的实施视为组织转型也好，把它当做项目做也罢；当你识别你的目标的时候，都可以参考这个模型。

### 两个研究模型的重叠

由于SDO效能和生产力在很多方面本来就是相关的。它们的产出都是使用各种优秀的方法创造和交付各种技术，从而为组织和个人交付价值。那些优化软件交付的支持工作也将使生产力受益，这也是理所当然的。虽然他们的某些诱因是相同的，它们看起来很相似，但是他们度量的产出确实不同的，报告团队也是组织了独立的分析调研。总之，SDO效能和生产力是两个不同的调研模型。

### 重叠模型的妙用

当你在应用SDO效能模型的时候，可以在消减职业透支方面做出聪明点的投资，更高的生产力也同样能降低职业透支。因此这个应该是向各种组织和技术团队大力提倡的做法，由于工作需求是持续增长的。工作是没完没了的，这个项目完了，还有下一个项目。而我们需要注意，我们也要关注生活和工作的平衡，而降低职业透支。

心理安全性文化也能对SDO效能、组织效能和生产力作出贡献。研究结果表明了创造和发展健康的文化对组织和个人都有好处。

投资在代码可维护性、松耦合架构和监控方面，也能同时帮助SDO效能、生产力（它们是通过消减技术债间接的影响到生产力的）。好的工具和系统也非常值得关注。

## 总结

通过本文我相信你已经可以正确的理解2019年状态报告中的模型了，模型包括SDO效能模型和生产力模型。包括我绘制的全模型。希望DORA官方能后续推出官方版模型全图。

> 模型的意义在于：DevOps能力点是整个软件开发和交付行业都应该关注的，在投资DevOps实践的时候，需要能聚焦到组织各自不同的急需改进的能力约束点组合上。通过模型最右侧的组织级统一共享目标来度量和验证DevOps的实践是否实际有效。

TOC是一个值得关注的问题解决套路，参考其它的相关文章和其它各种书籍。

请关注DevOps教练的公众号，在后台输入2019，下载本文中各种模型的高清大图。

![](https://res.cloudinary.com/martinliu/image/upload/v1566516259/DevOps-Coach-qrcode_for_gh_bce38ef330e5_430.jpg)

-------
