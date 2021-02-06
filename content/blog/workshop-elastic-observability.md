+++
date = 2021-02-06T10:36:12+08:00
title = "Elastic 可观测性工作坊"
description = "从 Elastic Stack 搭建开始直至云原生应用的运维和管理"
author = "Martin Liu"
categories = ["SRE"]
tags = ["elastic", "elk", "elasticsearch", "kibana"]
[[images]]
  src = "img/2019/03/pic01.jpg"
  alt = "Valley"
  stretch = "horizontal"
draft = true
+++

本工作坊包括本地虚拟机版本、AWS 和腾讯云共三个版本，目标是用实践的方式理解 Elastic 可观测性解决方案。可观测性是管理云原生以应用复杂且分布式运维难点的关键所在。

<!--more-->


## 简介

Elastic 可观测性解决方案是基于 Elastic Stack的一站式解决方案。该解决方案具有完备的日志、指标、APM 和可用性采集能力，可以在大规模和云原生的环境下完成基于服务质量目标的管理。本实战工作坊基于多层架构的宠物商店为示例应用，手把手的引导参与者搭建可观测性管理平台，体验分层次的收集整合、分析、关联和搜索运维数据的全过程。

![可观测性解决方案](/images/elastic-obv-solution.png)


## 为什么要做这个工作坊？

* 关于可观测性的各种一小时方案/产品分享，无法让听众理解相关概念
* 而实操的上机动手实验才能让新手迅速入门，熟手快速提高
* 大量 ELK 用户只使用到了日志部分，还不了解可观测性方案全貌
* 社区里存在着大量误解，如“APM 工具等于可观测性” 等等，急需系统的普及正确的观念



## 动手实验

本工作坊的最佳实践方式是在老师的引导下，在线下进行。其次是在视频的指导下自学。所有动手实验的目标是理解可观测性解决方案的各个组成部分，以及为什么要使用这些工具？而且这个整个方案的实施过程和顺序也是经过精心设计的，目标是让理论和实际彻底融会贯通。

您将会学到：

1. 搭建单节点 Elasticsearch 服务，并且配置好 Kibana 管理图形管理界面。
2. 学习可观测性的基本感念和实施步骤
3. 搭建和配置服务健康检查的探针
4. 部署采集操作系统性能监控指标的流程
5. 配置操作系统日志的采集和分析工具
6. 搭建用于 APM 追踪分析的后台服务
7. 运行一个多层架构的宠物商店应用，对各个子服务进行 APM 监控埋点
8. 配置常用的服务质量监控大屏

本工作坊课程基于如下的应用系统。

![](/images/16042852442364.png)

应用基本概况：

* 多层宠物商店应用系统
* 所有组件都部署在一个虚拟机上
* 包括前端、后端和内置的数据库
* 使用到的而技术有 JavaScript、NodeJs 和 Java Spring 等。
* 本应用系统是被监控的对象


Elastic Stack 的基本状况：

* 版本 7.9.3
* 组件 Elasticsearch、Kibana、APM、Filebeat、Metricbeat 和 Heatbeat。

实验环境：

* 本地虚拟机环境，打包好的虚拟机里包含了所有必要的软件包和演示应用。
* AWS 云环境，本课程所使用的公共 AMI 操作系统镜像：宁夏区 `ami-0e5a0e294902966af` 北京区 `ami-0e1382088b62cb38d`
* 腾讯云环境，基于腾讯云提供的 Elasticsearch 服务，演示用的虚拟机在制作中，稍后会发布到云市场。
* 阿里云环境，基于阿里云提供的 Elasticsearch 服务，课件正在开发中。


## 可观测性构建四步法

可观测性依赖于应用系统自身和监控工具平台的配合实现。

![可观测性](/images/e2e85893b5dd8014.jpeg)

分层次的构建可观测性的推荐过程如下：

1. STEP0：使用 Heatbeat 构建轻量灵活的服务健康检查能力
2. STEP1：使用 Metricbeat 构建全面细致的指标采集能力
3. STEP2：使用 Filebeat 构建高维度的日志采集能力
4. STEP3：使用 APM 构建分布式应用系统的全堆栈追踪能力


通过以上的四个构建步骤，使用 Elastic Stack 实施四大服务质量监控能力的构建，搭建了持续统一运维管理的工具平台。

使用 SRE 基于‘用户旅程’或‘系统边界’的 SLO 分析设定方法，从 Elastic Stack 的已有数据采集能力中，选取第批直接可用的 SLI 采集点。在基于 SLO 的监控过程中，不断的优选 SLI，调整告警的数量和质量，为开发团队提供持续有效的反馈。

使用 Canvas 的画布功能，定制如下的 SLO 监控大屏。

![2020-11-05_00-13-06](/images/2020-11-05_00-13-06.jpeg)

## 工作坊课件

讲师 PPT 下载： https://docs.qq.com/slide/DUGRzYVVTU3ZxblBP


#### 本地虚拟机环境

可以使用本地的 VirtualBox 或者 VMWare 的虚拟机环境，配合以下课件完成所有练习。

1. [‘Elastic Stack 单节点搭建’ 课件](https://elk-workshop.github.io/codelabs/one-nodes-es-server/#0)
2. [‘Elastic 可观测性方案’ 课件](https://elk-workshop.github.io/codelabs/elastic-observability-foundation/#0)


#### AWS 云计算环境

可以使用 AWS 云计算（中国区北京或宁夏区）环境，配合以下的课件完成所有练习。

1. [‘Elastic Stack 单节点搭建’ 课件](https://elk-workshop.github.io/codelabs/one-nodes-es-server/#0)
2. [‘Elastic 可观测性方案’ 课件](https://elk-workshop.github.io/codelabs/elastic-observability-foundation/#0)


#### 腾讯云计算环境

可以使用腾讯云计环境，配合以下的课件完成所有练习。

1. 在本环境下，不需要搭建 Elastic Stack 的服务器，参展下面课件的第二步骤，创建 Elasticsearch 服务集群。
2. [‘Elastic 可观测性方案’ 课件](https://elk-workshop.github.io/codelabs/elastic-observability-foundation-qq/#0)

#### 阿里云计算环境

可以使用腾讯云计环境，配合以下的课件完成所有练习。
> 课件开发中。


