---
date: 2018-02-26T11:08:53+08:00
title: "DevOps on Nutanix[Beta]"
subtitle: "如何使用超融合平台加速DevOps旅程"
description: "如何使用超融合平台加速DevOps旅程"
categories: "DevOps"
tags: ["DevOps"]
keywords: ["DevOps", "持续交付", "Nutanix", "HCI", "超融合"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/testdrive_background.jpg", desc: "DevOps"}]
---

Nutanix是什么？中文名字是路坦力，是我目前所在的公司；我负责运营商行业以及与云服务商的合作业务，解决客户在售前、架构和DevOps等方面的问题，我是Nutanix Calm产品的专家。

之前也发过一些介绍Nutanix和超融合技术的文章，本文会是一篇持续更新的文章，我会把在Nutanix上开展超融合的方法，持续的更新在这里。

本文上属于Beta版本，会持续更新，欢迎各种类型的反馈信息，发邮件到： martin.liu@nutanix.com

变更日志：

* 2018-2-26，发表了相关概况介绍性内容

## 什么是DevOps？


> 我的定义：DevOps是为了将软件开发、运维和质量保证等部门紧密地协作和集成在一起，而运用的一组成熟的、相互融合在一起的最佳实践。它使人们能准时/及时地生产软件产品或服务，从而满足企业的某个业务目标，开发与运维工作将在一个统一的目标之下协同工作，它是对IT组织内部各个角色之间的相互依存关系的一种新的理解。这个实践集合主要包含了四种最佳实践，如下图所示：

![DevOps 定义](http://res.cloudinary.com/martinliu/image/upload/q_auto:eco/devops-house.png)

注意：上图里Nutanix的定位在持续交付，超融合平台能高速平滑的交付IT服务。

来自网络的其它定义还有如下。

> 定义2：You cannot buy DevOps and install it. DevOps is not just automation or infrastructure as code. DevOps is people following a process enabled by products to deliver value to end users.   -- Donovan Brown, Microsoft DevOps Program Manager

以上出自：[Donovan's blog post on "What is DevOps".](http://www.donovanbrown.com/post/2015/09/01/what-is-devops)

> 定义3：DevOps（Development和Operations的组合词）是一种重视“软件开发人员（Dev）”和“IT运维技术人员（Ops）”之间沟通合作的文化、运动或惯例。透过自动化“软件交付”和“架构变更”的流程，来使得构建、测试、发布软件能够更加地快捷、频繁和可靠。

以上出自：[维基百科 Wikipedia - DevOps](http://zh.wikipedia.org/wiki/DevOps)


## 什么是HCI-超融合基础架构

我对超融合的定义：将计算、存储和网络这三种资源的至少两种融合在一起的技术就可以称之为超融合技术。Nutanix是将计算和存储融合在了一个系统只能，这里说的系统可以理解一个物理的机箱，并且在这个机箱里搭载了目前业内最通用的KVM虚拟化功能。Nutanix的超融合系统是开箱即用的IaaS平台，可以无节点数限制的水平扩展，能够支持服务器虚拟化、VDI、Oracle RAC等关键性数据库、企业核心业务系统、大数据和私有云等工作负载。在性能和功能上是专门为HCI而打造的。HCI技术正在颠覆着传统的三层架构技术堆栈（指的是：服务器-存储网络-集中存储）。

Nutanix在2018年Gartner融合基础架构分析报告中，Nutanix在领导象限里遥遥领先。

![Gartner 报告](http://res.cloudinary.com/martinliu/image/upload/Gartner-report-2018.png)


2018 年 2 月 9 日，北京 ——企业云计算领域的领先企业 Nutanix（纳斯达克：NTNX）今天宣布， Gartner 将 Nutanix 评为 2018 年 Gartner 超融合基础架构（HCI）魔力象限领导者。Nutanix 认为，此次跻身“领导者”象限有力印证了 Nutanix 在其率先开拓的市场上的领导地位，也充分彰显了公司致力于提供下一代企业云操作系统的愿景。

随着越来越多的企业机构认识到超融合基础架构（HCI）的优势，企业基础设施正在经历根本性的转变。这些企业机构采用了一种新的架构设计，将网络规模技术和消费级设计相融合，实现“隐形基础设施”，从而使 IT 团队能将更多的时间投入到业务应用中。同时，这些企业机构还纷纷采取了能够利用多云基础设施和云服务的 IT 战略。

<embed src='http://player.youku.com/player.php/sid/XMTUyODU1MzA5Ng==/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>

Nutanix 认为，利用其企业云操作系统软件，用户不但能实现公有云的精简性、敏捷性以及部分 IT 消费收益，还能保障企业数据中心的高可控性与安全性。在融合了私有云、公有云和分布式云的统一 IT 操作环境下，Nutanix 企业云操作系统软件提供单点控制来管理任何云的基础设施与应用，从而为云运营商和采用云交付式服务及应用的用户提供统一、高性能、无缝的使用体验。

关于Nutanix的更多视频，[请访问Youku的频道。](http://i.youku.com/i/UMzM5NzI4MDg1Mg==?spm=a2hzp.8244740.0.0)

### 学习Nutanix核心技术

关于Nutanix超融合系统的核心技术特性请访问：[Nutanix 圣经](http://nutanixbible.com/)，圣经网站上有中文版本pdf下载，最近会有一次中文版的修订请关注。

### 试用Nutanix产品

Nutanix提供免费的社区版本，对此感兴趣的人都可以下载和使用。使用这个版本，你能够在几个小时内，搭建起数量为1、3或者4个的物理服务器组成的Nutanix集群。

关于如何安装和试用Nutanix CE版本的技术文档，访问我的Nutanix实验室文档站点：[https://nutanix.martinliu.cn/](https://nutanix.martinliu.cn/)


## 使用Nutanix Calm实现DevOps持续交付

Nutanix是一种开箱即用的高性价比的虚拟化资源池，你可以用最小的时间成本完成大规模资源池的搭建和部署。而现实情况下：所有企业的虚拟化管理员的工作模式还是基于工单的手工VM模板克隆的方式。还没有人能将基于vm的业务系统做到自动化的持续交付。Nutanix Calm就是一项解决这个问题的技术。它是Nutanix超融合系统内置的一个功能，可以一键式的开启这项功能。


![Nutanix Calm](http://res.cloudinary.com/martinliu/image/upload/WechatIMG224.jpeg)


Nutanix Calm的主要功能如下所示：

* 应用生命周期管理：利用预定义的应用蓝图，全面地实现了传统型多层应用和流行的分布式服务的自动化运维，包括系统制备、扩缩容和资源释放等操作。应用蓝图将极大地简化了私有云和公有云的应用管理和运维。
* 应用蓝图管理：将应用系统的所有组成部分（包括相关的虚拟机、配置和可执行程序）融入到了一个可视化的、操作直观的蓝图里，从而简化了企业应用的配置管理和日常运维。应用蓝图提升了基础架构团队的管理效率。IT团队再也不用像以前那样，在应用管理的日常工作上花费大量时间。
* Nutanix应用市场：应用蓝图可以在Nutanix 应用市场（Marketplace）里把应用直接发布给最终用户，使产品经理和开发人员能够持续交付产品，快速地供给应用，及时地满足IT服务请求。
* 应用治理：Calm基于角色的访问控制机制可以限制用户的操作权限。此外，系统会集中地记录所有操作活动和变更，可以实现端到端的可追溯性，这些信息可以提供给安全团队，用来配合相关合规审核工作。
* 混合云管理：能在混合云的架构里，自动化地制备应用，包括AWS公有云环境，能实现多层应用和分布式应用的弹性扩缩容。Calm能全局统计资源用量，让您对公有云的实际消费成本一目了然，方便您按照业需求和预算做出合理的决策。

Nutanix Calm的蓝图编辑器如下所示。

![Nutanix Calm Blueprint](http://res.cloudinary.com/martinliu/image/upload/blueprint.png)

在我的[Nutanix实验室：](https://nutanix.martinliu.cn/)文档站点里已经写了一些操作使用的方法和产品截图。如果您已经是Nutanix用户了，请参考和使用这些文档。如果你还不是的话，可以联系Nutanix试用这个产品。


-------
后续会持续更新这一部分，会根据DevOps的逻辑将Nutanix Calm的能力全面的展示出来，敬请期待。

## 使用Nutanix实现完美的Docker Datacenter体验

CaaS on IaaS的简洁实现方式莫过于在Nutanix超融合平台上部署Docker Datacenter产品。其实Docker Datacenter还是一个很容易使用的Docker平台，易用性非常好，入门级Docker用户建议走这条路试试，毕竟K8s的学习曲线目前还比较陡峭。

这个组合的免费试用方法：

1. 安装部署Nutanix CE（文档见Nutanix实验室）
2. 申请和下载Docker Datacenter的安装包和许可证文件（10个节点免费试用，30天到期了还可以无限次延续）
3. 在Nutanix上创建10个虚拟机用于部署Docker Datacenter
4. 安装部署Docker Datacenter （[文档见Nutanix实验室](https://nutanix.martinliu.cn/04-nucalm-advance/02-owncloud-dvp/)）
5. Enjoy it forever!

如果你使用4台物理服务器安装Nutanix CE，建议的服务器配置：2路20核 Intel XeonCPU，内存256，SSD 512GB一块，SAS HDD 4TB两块；这样形成的群集的总资源量：

* 160个物理CPU核，一个物理核跑两个虚拟机的话，你可以跑320个虚拟机；当然内存够的情况下，你还可以尝试更高的整合比，如1个物理的核带5到10个虚拟机
* 总存储空间为18TB，使用两副本存数据，你有9TB可用空间，打开去重压缩等功能的话你可以拥有更多的存储空间。
* 2TB的SSD存储可以让你应付大量的热数据，所有热数据相当于使用了全闪存储一般。
* 建议这些服务器使用10GB或更高速的以太网，以保证更优雅的性能
* 不建议这个环境跑生产负载，记住不要把研发环境不算生产负载。
* 如果需要生产级别的保障，请考虑使用费CE版本的正式Nutanix产品。



## 使用Nutanix ACS2.0实现完美的K8s体验

此产品预计18年发布，敬请期待。

