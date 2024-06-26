+++
date = 2021-04-28T17:22:22+08:00
title = "2021 年 Gartner  AIops 平台市场指南报告"
description = "AIOps平台通过对大量的运维数据进行上下文分析，增强了I&O（基础架构和运维）角色的决策能力。I&O领导应该使用AIOps平台来改善整个应用生命周期的分析和洞察力，此外还可以增强IT服务的管理和自动化。"
author = "Martin Liu"
categories = ["DevOps"]
tags = ["AIops", "ITSM"]
image  = "img/2021/4/AIOps-an-Industrial-Benchmark-2048x719.jpg"
slug = "gartner-aiops-platform-market-guide-2021"
+++

本文是翻译整理的 Gartner 的行业调查报告，原文在：<https://www.gartner.com/doc/reprints?id=1-25RAD0H3&ct=210407&st=sb>

<!--more-->

## 概述

### 主要发现

- AIOps平台在企业中的应用正在迅速增长。I&O（基础设施和运维）领导人正在为COVID-19后的环境进行规划，主要参考当前的实际成果，而非理想的目标。
- AIOps平台的产品分为两类：领域无关的和以领域为中心的解决方案。然而，在处理高度多元化数据集的灵活性方面的需求正在逐渐提升，这正在对市场产生重大影响，并使AIOps平台向领域无关的功能性方向转变。
- 企业已经开始采用AIOps平台来对比和替换一些类别的传统监控工具。例如，监控 IaaS 和可观察性正在完全在 AIOps 平台内完成，特别是当企业的整个IT服务部署都在云里时。
- 企业正在增加将 AIOps 用于IT运维管理（ITOM）的各方面，并使其在DevOps 和 SRE 的实践中的使用应用场景更加成熟。

### 建议

专注于基础设施、运维和云管理的 I&O 领导人应该。

- 通过采用渐进式方法，从取代基于规则的事件分析开始，然后再扩展到以领域为中心的工作流程中，如应用程序和网络的诊断，优先考虑实际成果，而不是理想中的目标。
- 通过允许根据使用场景来选择的方法，在以领域为中心的AIOps或与领域无关的AIOps之间作出选择。在使用以领域为中心的AIOps功能点时，要将其内置于监控工具中，服务于一次性的特定用例，同时在路线图上规划部署能兼顾多种用例的，领域无关的独立解决方案。
- 通过选择一个支持与ITSM工具双向整合的AIOps平台，实现任务自动化、知识管理和变更分析。小心那些只提供基本搜索和显示功能的工具。
- 通过AIOps平台所支持的以上这三个方面，实现对整个ITOM的持续洞察：观测、干预和行动（observe, engage and act）。

## 市场定义

本报告于2021年4月19日修订。你正在查看的文件是更正后的版本。欲了解更多信息，请参见gartner.com上的 [更正](http://www.gartner.com/technology/about/policies/current_corrections.jsp)页面。

AIOps 平台通过结合数据存储和分析功能，满足I&O领导者对运维支持的需求，根据IT部门为应对数字化转型而产生的数据，向有关团队提供相关的洞见。该能力是数据流水线的一部分，包括数据的摄人和存储，然后是数据整形和分析，然后转向可视化层。分析能力包括统计技术和人工智能技术的混合，但考虑到用户的成熟度，与人工智能层的互动界面对I&O来说是最小化、甚至是不存在的。

## 市场描述

AIOps 平台广泛的强化了一些列 IT 实践，包括 I&O（基础架构/运维）、DevOps、SRE 和服务管理。然而，更集中的成果是在 I&O 领域，包括异常检测、诊断信息、事件关联和根本原因分析（RCA），以改善监控、服务管理和自动化任务。

AIOps平台的核心功能包括：

**摄入**

AIOps 平台可以从多个领域、信息提供源进行数据摄取、索引和规范化事件或监控数据，包括基础设施、网络、应用程序、云或现有监控工具（用于跨领域分析）（见注2）。该平台必须至少在两个方面，使用机器学习的使能（enable）数据分析，包括。

- 摄入点的实时分析（流分析）。
- 存储数据的历史分析

**拓扑**

AIOps 平台发现并建立IT资产的统一拓扑结构，包括应用程序，和其它相关领域。拓扑结构可以表达物理上的连接性、逻辑上的依赖性或捕捉到IT资产和服务之间其他维度的关系。

**关联**

AIOps 平台对多个监控领域或来源的事件进行关联和压缩（抑制），减少不必要的人工干预。关联功能结合了时间和拓扑结构来分组相关的事件。

**识别**

AIOps 平台处理事件和监控数据，从而检测或预测重要的事件或事故。该平台不断地从操作员的输入和优化的机制中学习和强化重要事件的独特模式。

**修复**

AIOps 平台通过操作员的调校或观察，不断的学习和改进每个重要事件和操作响应之间的关联性。AIOps 平台可能会提供一个建议，自动化响应或触发外部自动化系统。

AIOps 不仅仅是一个数据存储和检索系统。此外，该平台不限于趋势分析、预测和查询大量数据集的能力。

AIOps 的目标是通过策划和提高摄入数据的质量，以便 I&O 的领导者能够将多种用例推向相关的合适实践或角色。例如，模式发现可以有助于预测新出现的行为，IT 实体之间的关系，以及（IT工件、用户和代理）的基准行为，从而识别出异常情况，并给业务所有者提供相关背景。分析也促成了自动化的洞察力，简化了根本原因的定位，并使能了运用自动化解决所已发现问题的行动（见图1）。

图1: AIOps 跨多 IT 运维监控(ITOM)领域使能持续生成洞见 ![Figure 1: AIOps Platform Enabling Continuous Insights Across IT Operations Monitoring (ITOM)](img/cos/2021-04-28-Figure_1_AIOps_Platform_Enabling_Continuous_Insights_Across_IT_Operations_Monitoring_ITOM.png)

图片翻译如下：

Real-time and historical data : 实时和历史数据

Events Metrics, Traces, Topology : 事件 指标，追踪，拓扑

Incidents, dependencies and changes : 事故、依赖和变更

Observe （monitoring）：观测（监控）

- Historical analysis 历史分析
- Anomaly Detection 异常检测
- Performance analysis 性能分析
- Correlation and contextualization 关联和上下文化

Engage （ITSM）：干预（ITSM）

- Task Automation 任务自动化
- Change Risk analysis 变更风险分析
- Performance Analysis 性能分析
- Knowledge Management 知识管理

Act （automation） ： 行动 （自动化）

- Scripts 脚本
- Runbooks 运行手册
- ARA

## 市场方向

### 市场转向领域无关的 AIOps

领域无关的平台正在作为一个独立的市场出现，与以领域为中心的AIOps平台不同（见注3）。这是因为在三到五年渐进式的路线图中，可以灵活地摄取日益多样化的数据集。这种路线图上的用例不仅仅关注异常状态识别，还包括行为分析、客户参与和识别潜在机会。未来的市场指南报告将专注于领域无关的 AIOps。

随着企业在应用 AIOps 方面的成熟，他们需要一个跨越 I&O、DevOps、SRE的统一的领域无关平台，在某些情况下还需要包括安全实践。

Gartner 看到 I&O 领导人正在与高级管理层讨论相关的KPI（关键绩效指标）和仪表盘。在所有这些情况下，以领域为中心的工具则出现了明显的差异，它更聚焦在异常检测和减少错误告警方面。AIOps 已经成为许多以领域为中心的市场中的一个决定性特性。

### AIOps：以领域为中心的工具中的必备功能

以领域为中心的 AIOps 已经扩展到多个 ITOM 细分市场，包括可观测性和自动化工具市场。它是一些市场的决定性特性。比如说。

- AIOps 能力是 APM 工具的决定性特性之一（见[应用性能监控魔力象限]报告）。
- 在 ITIM 和 NPMD 市场，分析被认为是一种核心能力，但供应商已经开始提供AIOps能力，以支持各种产出，如提升洞察和诊断力。
- 许多ITSM供应商通过投资自开发平台或与 AIOps 平台供应商合作，将AIOps能力纳入其中（见[IT服务管理工具魔力象限]）。AITSM 的概念通过在 ITSM 工具上应用人工智能的上下文、建议、行动和界面，为 I&O 人员带来了有效性、效率和降低错误（见[利用 AITSM的4个领域来发展ITSM工具和实践]）。

以领域为中心的 AIOps 方法对那些数据种类有限（即只有少数点状解决方案）并优先考虑少数重点用例的组织有效。这类组织对同时查看多个孤岛数据的需求或能力都比较有限。随着组织内用例的增加，他们可能会转向领域无关的工具。

仅仅关注以领域为中心的方法的供应商将在那些还没有准备好利用领域诊断工具的优势的客户身上获得成功。然而，随着越来越多的企业希望转向领域无关的选项，只关注以领域为中心的技术的供应商将发现自己被排除在市场的讨论之外。

### 持续的关注和增长

AIOps 继续的增长和对整个 ITOM 市场的影响，估计2020年的市场规模在9亿至15亿美元之间，2020年至2025年的复合年增长率约为15%（见[市场机会图：全球IT运维管理]）。采用和方向正受到两个独立但最终相关的领域的严重影响。

- 数字化业务转型
- 从被动应对问题过渡到主动解决问题

数字化业务转型正在推动着 AIOps 市场的发展，因为更多的业务运维被数字化，分析不断增长的数据量变得更加关键和困难。随着数据量达到或超过每分钟千兆字节，跨越十几个不同的领域，人类已经不可能手动分析数据了。

随着企业继续进行数字化转型，他们不再奢望在问题发生后才作出响应。相反，他们必须变得积极主动，在影响到用户的体验之前就解决掉潜在的问题。

AIOps 市场继续朝着更广泛和更好的解决方案发展，在这两个目标下，依然同时仍然保持着以领域为中心的方法和领域无关的方法之间的区分（见注3）。未来的状态是一个统一的 AIOps 平台试图取代问题日益增多的领域为中心的工具。Gartner 预计会看到越来越多的专业层，获奖在嵌入设备中包含分析和训练有素的模型。最终，分析技术将被嵌入到构成以领域为中心的AIOps的不同监控技术中，以至于以领域为中心的AIOps被包含在多种监控市场的定义中。

此外，一些供应商正在尝试将领域无关和以领域为中心的方式混合起来，在其孤立的工具之上提供领域诊断的AIOps功能。在日益动态的IT架构中，由于必须更新相关规则的速度，基于规则的事件关联已经让位于基于人工智能的关联（见[使用AIOps的数据驱动方法来提高IT运维监控工具的洞察力]）。

### 低准入门槛

开源技术的商品化降低了该领域许多供应商的准入门槛，为数据采集、存储和可视化工具提供了许多选择。这些与领域无关的采集、存储和展示技术相对容易部署和整合，引发了许多以领域为中心的供应商，包括系统集成商和管理服务提供商的产品开发或改进。用于跨指标、追踪和日志领域的诊断数据采集的开源工具，包括 Prometheus、Elastic Beats、Jaeger 和 Fluentd。对于数据可视化，Gartner 遇到了许多利用 Grafana 实现的方案，无论数据存储在哪里。

尽管 AIOps 尚未成熟，但只要使用案例合适，AIOps 就会被认为是企业内部的一个有价值的工具，并能长期保持持有的状态（见图2）。

图 2: 组织计划持续使用 CMP 和 AIOps![Of the DevOps initiatives organizations began using in response to COVID-19, CMP and AIOps are the ones organizations most intend to continue using.](img/cos/2021-04-28-Figure_2_Organizations_Plans_to_Continue_Using_CMP_and_AIOps.png)

## 市场分析

尽管 AIOp s技术已经存在多年，但成功的部署还需要时间和努力，包括终端用户的结构化路线图。实施通常会遇到一些问题，包括数据摄取、提供上下文相关的分析和较长的价值实现时间。许多 AIOps 平台工具部署的价值实现时间是以月或年计算的，这导致了对该细分市场的不满和幻灭。然而，企业应该毫不怀疑。

> IT运维的未来不可能不包括 AIOps。这是由于数据量和变化速度的快速增长（以应用交付速度和事件驱动的商业模式为例），不能依靠人类从数据中挖掘出洞见。

人类根本不可能对其IT系统每秒产生的成千上万的事件进行理解。

为了更清楚地了解市场是如何发展的，以及供应商彼此之间的定位，请考虑以下属性。

- 数据摄取和处理
- 机器学习（ML）分析
- 补救措施

### 数据摄入和处理

AIOps  平台必须能够摄取静态（历史）数据和动态（实时、流）数据。这些平台可以摄取、索引和存储日志、事件数据、指标、追踪以及图表和文档数据（见注释2）。

这些用于IT运维的工具必须直接在摄取点上做实时数据分析，而不需要在分析前将数据保存到数据库。它们还必须提供跨越多个实时和历史数据流的关联分析。

### 机器学习分析

- AIOps 平台使用以下类型的分析方法。

  - **统计学、概率分析** 单变量和多变量分析的结合，包括使用相关、聚类、分类和跨IT实体捕获的指标进行推断。
  - **自动模式发现和预测** 发现隐含描述历史和/或流数据中的相关性的模式、集群或群体。然后，这些模式可用于预测具有不同程度概率的事件。
  - **异常检测** 使用前述组件发现的模式来确定正常行为，然后辨别与正常行为的偏差，包括单变量和多变量。超越了单纯的异常值检测，它们必须与业务影响和其他并发流程（如发布管理）相关联，才能充分发挥作用，而不是产生出更多的告警噪音（见[使用AI技术增强DevOps的决策能力]）。
  - **可能原因判定**  对通过自动模式发现和摄取图数据建立的关联网络进行修剪，以确定连接因果关系的因果关系链。
  - **拓扑分析**  AIOps平台可以使用应用程序、网络、基础设施或其他拓扑结构来提供上下文分析。从拓扑结构内的数据中得出的模式将建立相关性，并说明隐藏的依赖关系。将拓扑结构作为因果关系判断的一部分，可以大大增加其准确性和有效性。
  - **规范性建议**  建议解决一个问题的方案。这些建议可能是基于对重复出现的问题的历史解决方案（部落知识）的数据库，或通过众包确定。

### 补救措施

随着技术的成熟，用户将能够利用该平台的建议，实现行动阶段（见注4）。这方面的步骤如图3所示。

图3: AI 辅助自动化的未来 —问题的分类和补救![Graphic illustrates the problem-remediation process with AI-assisted automation.](img/cos/2021-04-28-Figure_3_The_Future_of_AI-Assisted_Automation__Triage_and_Remediation_of_Problems.png)

图片翻译：

1 开始于已知的

- 在一个部落知识库中记录成功的解决方案
- 将问题进行分类

2 当前和历史的对照

- 在数据库将一类问题与一组已知解决方案进行匹配
- 众包

3 建议

- 建议一组可能的解决方案

4 执行和评估

- 运行解决方案（提供）（ARA/运行手册）
- 跟踪解决方案效果
- 对效果投票

一个被称为 "自我驱动的ITOM "的自动化、闭环的流程是非常令人向往的，但这仍然是一种愿望。在商业工具中，除了那些简单的自动 "弹出服务器 "或 “创建工单 "类型的脚本外，很少看到规范性的解决方案。有可能从规范性工具中获得自动行动的候选者是那些低风险的。这些是那些如果失败或导致意外的副作用，造成的损失相对较小。根据环境的不同，手工的预定操作，如补丁更新，以及执行工作负载优化的行动，如启动一个额外的虚拟机（VM）或容器，可能是成功的。

#### 价值实现时间

Gartner 客户的一个共同抱怨是，部署、配置和从AIOps解决方案中获取价值所需的时间可能长达六个月，在极端情况下，可能长达两年。AIOps是一项新兴技术，这意味着该领域的最佳实践仍在不断发展。但是，当潜在的回报在时间跨度上如此遥远时，企业不愿意投资于一个产品。

为了应对这种情况，供应商正在采取举措，加快部署速度。这些措施包括。

- 转向基于SaaS的部署
- 改进通用接口的开箱即用的集成方式
- 基于现场测试的最佳实践，在系统中建立可重复的工作流
- 减少系统产生的误报数量

在为AIOps的投资回报建立商业案例时，I&O 领导人必须与供应商讨论其实施的预期价值时间。在许多情况下，预计会有一个有限的概念验证，以证明集成在现实环境中如何运作。

#### DevOps 中的 AIOps

作为IT运维工具与DevOps流水线整合的 "左移 "大趋势的一部分，早期采用者正在开发流水线的早期尝试AIOps。结合越来越多的自动化使用，开发人员正在使用人工智能来更快、更安全地交付软件，在生产中更容易管理。图4显示了AIOps 存在于 DevOps 流水线中的例子。
图4：在应用程序的生命周期中，在一系列的使用案例中应用AIOps平台

![Graphic illustrates how to apply AIOps throughout an application’s nonexistent, from development through IT service management.](img/cos/2021-04-28-Figure_4_Applying_AIOps_Platforms_Across_a_Spectrum_of_Use_Cases_Over_the_Life_Cycle_of_an_Application.png)

图片翻译：

1. 识别代码中的风险
2. 日志文件分析
3. 时间关联、异常分析，RCA
4. 数字化代理（智能客服）/自动化，变更

NLP 在 ITSM 工具中被大量采用，但一些APM供应商已经开始将NLP作为其AIOps能力的一部分。一个主要目标是为DevOps团队实现更灵活的ChatOps，并为APM数据和自动化提供更好的接口。

## 代表性厂商

### 市场介绍

AIOps平台供应商拥有广泛的功能，并在继续增长。供应商在其数据摄取和开箱即用的用例方面存在差异，只需最小的配置即可使用。在表1中，我们提供了一个有代表性的供应商样本列表，提供领域无关的AIOps平台功能。该表中的一些供应商也提供以领域为中心的产品。

表2包括以领域为中心的AIOps供应商，在某些情况下，他们专注于一个以上的领域。随着AIOps功能开始成为APM和ITSM等不同领域的决定性特性，Gartner将在本市场指南的未来版本中关注领域无关的AIOps供应商。

表1: 领域无关的AIOps平台市场的代表厂商

|                         **厂商**                         |       **产品,服务或者解决方案** **名称**        |
| :------------------------------------------------------: | :---------------------------------------------: |
|           [BigPanda](https://www.bigpanda.io/)           |                    BigPanda                     |
|               [BMC](https://www.bmc.com/)                | TrueSight Operations Management, Helix Platform |
|  [Broadcom-CA Technologies](https://www.broadcom.com/)   |           DX Operational Intelligence           |
|    [Devo](https://www.devo.com/) (formerly Logtrust)     |                      Devo                       |
|            [Digitate](https://digitate.com/)             |                      ignio                      |
|            [Elastic](https://www.elastic.co/)            |                  Elasticsearch                  |
|               [IBM](https://www.ibm.com/)                |         IBM Cloud Pak for Watson AIOps          |
| [Interlink Software](https://www.interlinksoftware.com/) |               Interlink Software                |
|               [Logz.io](https://logz.io/)                |                 Log Management                  |
|          [Moogsoft](https://www.moogsoft.com/)           |                    Moogsoft                     |
|         [PagerDuty](https://www.pagerduty.com/)          |                    PagerDuty                    |
|           [ServiceNow](http://servicenow.com/)           |         IT Operations Management (ITOM)         |
|            [Splunk](https://www.splunk.com/)             |         Splunk Enterprise, Splunk Cloud         |
|        [StackState](https://www.stackstate.com/)         |                   StackState                    |
|         [Sumo Logic](https://www.sumologic.com/)         |                   Sumo Logic                    |
|                                                          |                                                 |

Source: Gartner (April 2021)

表2: 以领域为中心的AIOps平台市场的代表厂商

|                     **厂商**                     |              **产品,服务或者解决方案** **名称**              | **供应商擅长的领域** |
| :----------------------------------------------: | :----------------------------------------------------------: | :------------------: |
|          [Aisera](https://aisera.com/)           |                            Aisera                            |         ITSM         |
|         [Cisco](https://www.cisco.com/)          |                         AppDynamics                          |         APM          |
|         [Datadog](http://datadoghq.com/)         |                         Datadog APM                          |         APM          |
|        [Digital.ai](https://digital.ai/)         |                           Numerify                           |         ITSM         |
|     [Dynatrace](https://www.dynatrace.com/)      |                          Dynatrace                           |      APM, ITIM       |
|    [Espressive](https://www.espressive.com/)     |                   Barista Case Management                    |         ITSM         |
|      [ExtraHop](https://www.extrahop.com/)       |             ExtraHop Reveal(x) for IT Operations             |         NPMD         |
|          [Harness](https://harness.io/)          | Continuous Integration, Continuous Delivery, Continuous Efficiency Platforms |        DevOps        |
|   [IPsoft (Amelia)](https://amelia.com/about/)   |                 DigitalWorkforce.ai Platform                 |         ITSM         |
|        [Kentik](https://www.kentik.com/)         |                            Kentik                            |         NPMD         |
|       [OverOps](https://www.overops.com/)        |                           OverOps                            |         Dev          |
|          [Pico](https://www.pico.net/)           |                            Corvil                            |         NPMD         |
|        [New Relic](https://newrelic.com/)        |                    New Relic One Platform                    |      APM, ITIM       |
|       [OpsRamp](https://www.opsramp.com/)        |                           OpsRamp                            |         ITIM         |
|    [ScienceLogic](https://sciencelogic.com/)     |                         SL1 Platform                         |         ITIM         |
|       [Virtana](https://www.virtana.com/)        |                       Virtana Platform                       |         ITIM         |
| [Zenoss](https://www.gartner.com/doc/zenoss.com) |                            Zenoss                            |         ITIM         |
|                                                  |                                                              |                      |

Source: Gartner (April 2021)

*本市场指南中所列的供应商并不意味着是一份详尽的清单。本节旨在提供对市场及其产品的更多了解。

## 市场建议

### 使用一个自上而下的 AIOps 框架

AIOps的使用案例跨越了从IT操作员到业务线所有者甚至CEO的各个层次。

在实践中，这些平台只具备开箱即用的异常检测和事件关联能力。这意味着对IT操作员来说，开箱即用的相关性相当高，而终端用户必须创造与人员相关的结果，如 I&O 领导、系统管理员、架构师和LOB所有者。

该平台的分析能力利用算法和模型来支持基于数据集的结果，这些数据集可能质量差、不完整且缺乏统一性。结果并不总是通用或相似的；因此，算法的价值是有限的。由于IT的复杂性和不断变化的性质，即使是AIOps平台所利用的模型，如果没有持续的反馈机制，也会失去相关性。

**例如，在监控策略中，确定AIOps如何将数据转化为与目标人物的相关性，以及如何帮助解决各自人物的目的（见注5）。随后，从IT运维中的可视化现状开始，描绘出通往目标的以下步骤（见[采用AIOps的解决方案路径]）。

- 以最终目标为起点的目标路线图
- 通向目标的中间步骤
- IT运维的现有状态（噪音事件、基于静态阈值的告警或利用动态阈值）

选择最适合为路线图上的第一步提供开箱即用功能的AIOps供应商，并提供符合组织路线图的平台（例如，帮助组织以最小的努力从事件关联推进到动态阈值到行为分析）。随着用例的成熟，请注意这些平台的可移植性挑战（见注6）。

### 基于洞见的自动化

一些企业有一个目标，导致对已发现的异常情况进行自动化补救。任何自动化举措都是基于一定程度的标准化。这是大规模部署自动化行动的一个主要抑制因素。成熟度高的IT组织更喜欢自动化的洞察力，而不是自动化的行动，这是一个切实的目标。I&O领导应该优先考虑那些能减少IT操作人员视觉负担的工具。例如，AIOps平台应该强调出需要人类关注的领域，而不是对多个图表进行可视化分析。

COVID-19疫情要求企业从根本上改变排查方式和采用AIOps用例的方式，因为向居家工作的转变暴露了现有做法的缺点。例如，在运维中心，有人会提出一个 "问题"，不同的小组会大声喊出他们对 "答案 "的看法。高管们看到了一个机会，在起草一个能够长期保持的战略时，重新审视综合运维工具、流程和人员的基本方面（见注5的图5）。

在2019年，Gartner的客户有一个理想的目标，即设计与LOB所有者相关的仪表盘。这个过程中，一些企业花了10个月到两年的时间。两个主要因素是透明度和用于使业务领导人推动决策的上下文信息，与旨在让业务领导人了解情况的报告相比。疫情大流行开始后，大多数企业关注基本面和减少风险，把自己限制在现有的开箱即用的用例上，如事件关联性。在COVID-19大流行之前，Gartner看到企业提出了理想的目标，而这些目标在今天的AIOps工具中可能还没有开箱即用。

### 与不同角色的关联性

AIOps平台被不同的团队采用，如DevOps、SRE、IT运维、网络安全（见[安全信息和事件管理魔力象限]），以及业务领导人。所需的用例和原始数据根据采用该平台的团队及其成熟度而不同。

DevOps团队主要专注于日志摄取和分析。随着DevOps实践的成熟，用例从对生产前的关注扩大到包括用户参与、质量和业务相关性等生产指标。这就产生了对新的KPI的需求，在多个版本之间进行比较，并关注产品和平台。考虑到这种情况，选择能够摄取埋点的数据（追踪、指标和日志）的平台，并减轻为DevOps提供平台和产品视图的工作。

IT运维团队通常需要指标和日志摄取的组合，然后是分析。这个过程从事件关联开始，随着团队的成熟，扩大到基于指标和日志分析的行为分析。这里的主要目标是异常检测和诊断信息，然后是根本原因分析。其他用例包括通过使用脚本的自动行动，其中AIOps识别与自动行动相关的触发器。选择那些能够灵活地摄取事件、日志和指标的平台，并为I&O的至少一个优先用例提供开箱即用的功能。

企业领导更关注用户参与度，而应用性能只是影响整体参与度的一个参数。在一些全球性的组织中，业务领导已经不再区分员工和客户，所以这里的 "用户 "既指员工也指客户。这个旅程通常从基于IT的用户影响的相关性开始，但扩大到包括技术、人员和现有流程的效率和生产力等定性的关键绩效指标。在成熟的组织中，更好的参与而不是减员是这种关键绩效指标背后的驱动力。对于这样的场景，选择专注于聚类和人口统计学的平台，并在不同的数据集上提供因果洞察力，包括情感和满意度。

SRE实践通常有与IT运维和DevOps用例重叠的目标。通常，这些都是跨越两个实践的成熟用例。例如，事件关联和日志摄取不是SRE团队的主要目标。他们的重点领域包括IT架构评估。对于SRE用例，选择为IT架构提供实时拓扑和依赖性洞见的平台作为主要用例之一。

## 首字母缩写词和词汇表术语

| **APM** | **Application performance monitoring** 应用性能监控          |
| ------- | ------------------------------------------------------------ |
| BAM     | Business activity monitoring 业务活动监控                    |
| DA      | Domain-agnostic 领域无关                                     |
| DC      | Domain-centric 领域为中心                                    |
| ITIM    | IT infrastructure monitoring IT 基础架构监控                 |
| ITOM    | IT operations management IT 运维管理                         |
| ITSM    | IT service monitoring IT 服务监控                            |
| NLP     | Natural language processing 自然语言处理                     |
| NPMD    | Network performance monitoring and diagnostics 网络性能监控和诊断 |
| SIEM    | Security information and event management 安全信息和事件管理 |

## 证据

**1** **Gartner的2020年通过自动化、持续质量和DevOps实现业务敏捷性研究**于2020年6月至8月在北美和西欧已部署或正在使用DevOps的服务提供商、云供应商和终端用户组织工作的205名受访者中进行了在线调查。符合条件的组织的年收入至少为5亿美元，并要求主要在银行和金融服务、政府、保险、医疗机构和零售业中运维。受访者必须在其组织的IT职能部门工作，其职称低于C-suite级别，并且与组织中的最高主管相差两层或更多。受访者的角色必须主要集中在应用开发、基础设施和运维，或商业智能和信息管理。在这些重点领域，他们还被要求执行相关的角色/活动。这项研究是由关注数字商业趋势的Gartner分析师和Gartner的研究数据和分析团队合作开发的。

这项研究的结果并不代表全球调查结果或整个市场，而是反映受访者和受访公司的情绪。

在过去的12个月里，AIOps构成了Gartner客户关于IT性能分析的所有咨询中的40%的谈话内容。这些咨询的主题包括。

- 技术和市场意识
- 平台选择
- 构建与购买决策
- 现有AIOps部署的优化
- 新部署情况下的部署策略
- 在DevOps、I&O、安全和SRE团队之间共享一个共同平台的利与弊
- IT内部和外部的多种AIOps使用案例，以帮助可视化、决策和诊断。

在大流行病中，大多数用例都与事件关联有关。

## 注1: 代表性供应商选择

- 本研究中列出的供应商是根据具有以下一个或两个特征而挑选出来的样本。

  - 领域无关的解决方案，能够从多个来源摄取数据，包括历史和实时流。
  - 以领域为中心的解决方案，能够从特定领域或特定框架或实践的数据中摄取数据（例如，网络、应用、IT基础设施、DevOps或ITSM领域）。
  - 不同的产品，包括专有的、开源的、免费的和商业化的版本，包括跨越企业内部和基于SaaS的部署方案。

## 注2:  AIOps 平台的数据源

AIOps 的数据源包括:

- API
- Application logs 应用日志
- CRM 数据
- 客户数据
- 事件
- 图
- ITSM
- 元数据
- 指标
- 社交媒体
- 追踪
- 布线

不幸的是，无论一个给定的数据集有多大，更新有多频繁，限制在一个单一的数据源往往会限制对系统行为的洞察力。现代IT系统--具有模块化和动态性--需要一个多视角的方法来理解它们在被观察时正在发生什么。

## 注 3: 领域无关和领域中心的AIOps

**领域无关的AIOps -**供应商以通用的AIOps平台进入市场。这些产品往往主要依靠监控工具来执行数据采集，并迎合最广泛的使用情况。

 **领域中心的AIOps -**供应商拥有核心组件，但是一组有限的使用场景。以他们基本上做着与以前相同的事情，但现在他们用数学（算法）代替了规则、启发式方法和指纹。这些供应商专注于一个领域（例如，网络、端点系统或APM）。然而，以领域为中心的解决方案供应商已经做出了一些努力，将这些类别混合起来，发展到从他们自己的埋点工具以外的来源摄取数据，并将这些数据纳入他们的分析。

## 注4: 基于规范性建议的自动化行动所面临的挑战

自动化执行行动分为多个类别。

- 可以提前计划的预定性质的任务（例如，补丁管理或新构建的部署）。
- 不能提前计划好的任务，但有已知的触发器，可能会或不可能经常出现。在这种情况下，程序是有据可查的（例如，虚拟化环境中的工作负载优化）。
- 具有不可预测的触发器的任务，其行动是众所周知的，但没有很好的文件记录（例如，已知的异常情况）。

I&O领导通常不希望将行动完全交给机器，并要求在触发自动化之前至少有一个验证步骤。这种缺乏信任是阻碍自动化行动普遍使用的主要障碍之一。

在这三种自动化行动中，我们看到对第三类行动的兴趣最大；然而，处理这类行动的技术困难是具有挑战性的，因此，到目前为止，它的采用是最小的。

## 注5: AIOps 作为 IT 监控策略的一部分

Figure 5: AIOps as Part of an IT Monitoring Strategy![Where AIOps Contributes to a Sample IT Monitoring Strategy](img/cos/2021-04-28-Figure_5_AIOps_as_Part_of_an_IT_Monitoring_Strategy.png)

## 注 6: 可移植性

随着企业采用AIOps的功能模型和质量成果的成熟，供应商转换变得困难。切换到不同的供应商来复制现有的高质量仪表盘将需要时间，这就消除了通过直接成本节约获得的任何价值。Gartner观察到，在部署比较成熟的企业中，正是因为这个原因，才不愿意在续约时更换供应商。

需要可行的选择来挑战现有的供应商，这就产生了关于跨供应商的算法的可移植性问题。这种需求来自于一些成熟的企业，在这些企业中，AIOps的采用已经很成熟。市场仍处于高速增长阶段，我们至少要在几年后才能看到企业对可移植性的压力增加，以及供应商作为差异化的回应。

一些供应商正在提出转移学习，这仍然处于初级阶段。在其较简单的形式中，终端用户可以选择通过使用历史数据训练一个选定的模型。该算法的结果与实时结果进行比较。一旦结果显示出相当的准确性和可接受的误差范围，终端用户就可以使用相同的算法来分析实时数据。这种能力在生产前和生产环境之间或在边缘和数据中心环境之间效果最好。更复杂的用例的演变将需要供应商和最终用户方面的成熟和高级技能。
