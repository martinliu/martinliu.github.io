---
date: 2020-08-11T15:03:54+08:00
title: "DevOps Coach 周刊 #3"
subtitle: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
description: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
categories: "DevOps"
tags: ["周刊"]
keywords: ["DevOps","DevOps教练","周刊"]
bigimg: [{src: "/images/abstract-4.jpg", desc: "周刊"}]
---


![DevOps Coach weekly update](/images/weeklyupdate.jpg)

## 宕机


* 上一周新发的宕机事故。
* 近期全球重大宕机事故的分析总结、事后回顾。

### 上周新发宕机事故

* **Discord** 这个值得注意的是，它涉及到谷歌云平台中所谓的 "吵闹邻居 "情况。https://discord.statuspage.io/incidents/bnv0wbddzz2x
* **Slack** 更新缓存基础架构的坑。从2020年7月23日晚上9:00 PDT到2020年8月1日下午5:17 PDT，客户在使用各种API端点时可能会出现滞后或故障。我们于7月29日开始调查这一问题，并将这些问题追溯到最近对我们的缓存基础设施进行的一项变更，旨在增加该基础设施的容量。一个不可预见的副作用导致一小部分API请求需要更长的时间来处理并最终超时。我们在8月1日恢复了这一更改，所有受影响的客户的问题都得到了解决。8月6日, 6:49 AM GMT+8 https://status.slack.com//2020-07/7d32ad54b0703c47
* **佳能 ** 遭遇勒索软件攻击，Maze宣称对此事负责 来源： https://www.zdnet.com/article/canon-suffers-ransomware-attack-maze-claims-responsibility/
* **Steam** 服务器目前已经瘫痪  https://gamerant.com/steam-servers-down-8-05/
* **Fastly** 著名 CDN 服务器最近又出性能事故了， 影响范围，Edge Cloud Services (Fastly API, 快速配置应用, TLS 制备)  https://status.fastly.com/incidents/d6ljy97shb0p

### 关于 Quay.io 宕机事故回顾

* 来源官网： https://www.openshift.com/blog/about-the-quay.io-outage-post-mortem
* 时间线：5 月 19 日第一次宕机，28 日第二次宕机，这些事故影响了大多数 quay.io 服务的用户。
* Red Hat SRE 团队对本次事件的经验总结：
    * **关于谁和什么人在使用你的服务，你永远都不可能有足够的参考数据。** 由于Quay "一直是正常工作"，我们从来不需要花太多时间分析我们的流量模式，处理负载的行为。这创造了一种虚假的安全感，即服务将无限期地扩展。
    * **当服务出现故障时，恢复是你的首要任务。** 由于Quay在第一次中断期间不断出现数据库死锁的情况，我们的标准流程并没有明确的实现服务恢复的预期目标。这就导致我们花了更多的时间进行分析和收集数据，希望找到根本原因，而不是把所有的精力都放在让客户恢复运行上。
    * **要了解你的每一个服务功能的影响。** App Registry很少被我们的客户使用，所以它不是我们团队的主要优先事项。当你的产品中有很少使用的功能时，bug就不会被提交，开发人员也不会再看代码。我们很容易认为这不会给团队带来任何负担--直到它突然成为重大事件的一部分。  

## 关于 Heroku 事故 #2090 的后续分析

* 概述：此次事件涉及Heroku的基础设施提供商（大概是AWS）的DNS故障。这次事故的坑是 DNS。
* 来源官网：https://status.heroku.com/incidents/2090
* 重要看点：为了给DNS查询提供内部IP地址，我们的服务提供商运行自己的内部DNS服务。这些DNS服务是确保在同一地区运行的基础设施之间建立最快连接的根本。当这些 DNS 服务不可用时，服务之间无法建立新的内部连接。与应用程序或数据服务的外部连接不会受到影响。在此次事件中，我们在一个地区的基础设施子集上经历了这些DNS服务的间歇性故障，包括我们运维的Heroku大部分内部服务的地方。
* 经验总结：我们正在审查我们如何应对服务提供商的DNS故障或降级，以确保我们能够尽快发现并解决任何未来的问题。

## LinkedIn 最近的 Hadoop 事故总结：理论 vs. 实战

* 概述：LinkedIn的这起事件影响了多个内部客户，他们对耐用性和延迟的要求各不相同，使得恢复变得复杂。
* 来源官网：https://engineering.linkedin.com/blog/2020/learnings-from-a-recent-hadoop-incident
* 学习制度化：一场大型事件结束后，总会有一些心得体会。以下是我们正在跟进的几条。
    * 为Hadoop基础设施建立一个强大和更全面的主机生命周期管理。
    * 建立更好地理解我们在负载下各数据中心的网络行为，并确保按需修改网络路由的自动化方式。
    * 目前，我们正在Azure上构建下一代基础设施，包括Hadoop协议栈。就中期而言，我们将有一个额外的集群，该集群建立在一个完全不同的技术栈上，这应该会进一步帮助我们实现冗余。
    * 调查其他架构的可行性，作为我们Azure迁移的一部分。例如，我们可以将数据摄取一次，然后将相同的数据复制到 D/R Cluster中，并通过数据布局和查询规划优化来吃掉延迟成本。我们正在采用Apache Iceberg作为我们的表格式。有了Iceberg，我们应该可以更好地对受影响的文件进行针对性的恢复。在我们当前架构的临时，我们已经建立了几个工具，让我们能够辅助恢复（例如，恢复除损坏数据以外的所有数据，更容易从另一个集群恢复大文件等），并围绕它建立了运行本，以便于访问。
    * 努力审计我们的流程，以确保它们有定义良好的灾难恢复协议。
    * 增加我们的灾难演练的频率，此外，还要审查灾难演练中流程的表现与他们所述的恢复策略的评分卡。
    * 继续研究我们的工具，围绕着理解世系，因为事实证明它在识别流和数据的依赖性方面非常有用。这也将提供理解生态系统端到端的连接图的能力--这在灾难恢复等大型协调事件中是非常宝贵的。
    * 一些流量所有者在他们的应用工作流本身中增强了弹性。例如，对延迟敏感的应用，产生关键业务小时和每日指标的应用，正在应用逻辑本身中进行明确的数据呆滞性与弹性的权衡。
    * 专注于提高我们预测数据恢复的数据可用性SLA的能力，以便在这种性质的事件再次发生时有能力快速发布。我们的内部数据消费者可以使用这些SLA，并在恢复协议的决策选择方面做出明智的决定。

### GitHub可用性报告 -- 2020年7月

* 概述：相信很多人都经历了 GitHub 7 月13 日的事故。该事故持续了4 小时 25 分钟。以下报告包括对涉及Kubernetes pods和DNS服务受损的事件的描述。
* 来源官网：https://github.blog/2020-08-05-github-availability-report-july-2020/ 
* 要点回顾：
    * 事件的起因是我们的生产型 Kubernetes Pods 开始被标记为不可用。这在我们的集群中层出不穷，导致容量减少，最终导致我们的服务瘫痪。对Pods的调查显示，Pod中的一个容器超过了其定义的内存限制并被终止。尽管该容器不需要处理生产流量，但Kubernetes的性质要求所有容器都是健康的，Pod才能被标记为可用。
    * 一般情况下，当一个Pod运行到这种故障模式时，集群会在一分钟左右恢复。在这种情况下，Pod中的容器被配置为ImagePullPolicy为Always，它指示Kubernetes每次都要获取新的容器镜像。然而，由于之前完成了一次例行的DNS维护操作，我们的集群无法成功到达我们的注册表，导致Pods无法启动。当为了缓解而触发了重新部署时，这个问题的影响就增加了，我们看到这个故障开始在我们的生产集群中传播。直到我们使用缓存的DNS记录重新启动进程，我们才得以成功获取容器镜像，重新部署，并恢复我们的服务。
* 后续事项：展望未来，我们已经确定了本季度要解决的一些领域。
    * 加强监控，确保Pod重启不会再基于这种相同的模式而失败
    * 尽量减少我们对镜像仓库的依赖。
    * 在DNS变更期间扩大验证范围
    * 重新评估所有现有的Kubernetes部署策略






## 新闻

### 项目发布速递

* Nano 5.0 — The popular simple Unix text editor.
* Julia 1.5 — High performance, dynamically typed language.
* Mastodon 3.2 — Federated social app.
* Django 3.1 — Python-based Web application framework.
* Alacritty 0.5 — Simplicity-focused terminal emulator.
* Terraform 0.13 General Availability


### DevOps 大会/峰会

KubeCon + CloudNativeCon 欧洲 2020

* 8 月 17 – 20，   免费
* 报名： https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/

Commit 峰会

* 8 月 26 ~ 27， GitLab 免费
* 报名：https://about.gitlab.com/events/commit/

DevOps Fusion

* 8 月 26 日， 免费
* 报名：https://swisstestingday.ch/en/

DevOpsCon 伦敦 2020

* 8 月 31 日 ~ 9 月 3 日，收费
* 报名： https://devopscon.io/

提交大议信息发邮件到：martin@devopscoach.org


## 文章

 麦肯锡：《十种 "反模式"，让技术转型脱轨。》

* 大型组织转型项目的反模式清单。在选择技术、技术管理、路线图等方面都有很好的建议。
* https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/ten-antipatterns-that-are-derailing-technology-transformations


 AWS：《为运维可视化构建仪表板》

* 一篇关于仪表盘设计的好文章，有很多道理、提示、技巧和例子。
* https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/

LearnK8s：《验证Kubernetes YAML的最佳实践和策略》

* 看看对验证和测试Kubernetes配置文件有用的几个工具。有用的对比表和每个不同工具的例子。
* https://learnk8s.io/validating-kubernetes-yaml

推荐 Arrested DevOps 这个网站，它是帮助你实现理解、开发良好实践、运营你的团队和组织的播客，以获得最大的DevOps妙用。

* 关于Service Mesh和SMI规范的所有事情的讨论。
* https://www.arresteddevops.com/service-mesh/

Dev.to：《使用Conftest、Regula和OPA保护你的Terraform管道安全》

* 关于使用Conftest和Regula帮助编写安全的Terraform代码和测试作为CI流程的一部分的帖子。
* https://dev.to/prince_of_pasta/securing-your-terraform-pipelines-with-conftest-regula-and-opa-4hkh

 
 无罪网：《事件回顾从小白到大师》

* Under Armour（！）的首席SRE对他们如何进行SRE有很多有趣的事情可以分享。我喜欢他们对事件回顾的方法，即从1:1采访相关人员开始。保罗-奥斯曼--Under Armour（无罪峰会）。
* https://www.blameless.com/blog/improving-postmortems-paul-osman

 medium.com 《主要的DevOps挑战以及如何应对这些挑战？》

* DevOps通过提供高效的解决方案，帮助加快交付速度，鼓励团队之间的协作，并促进敏捷环境，推动组织走向更美好的未来。
* https://medium.com/faun/major-devops-challenges-and-how-to-address-them-3b4d7b6ee50b



## 工具

* Open Service Mesh是一个新的轻量级、可扩展的、用于动态微服务环境的服务网状结构。它提供了开箱即用的可观察性功能，并使用SMI进行配置。
* https://openservicemesh.io/
* https://github.com/openservicemesh/osm


* Sysbox是一个新的容器运行时，它可以让你更容易地在容器中运行低级软件，比如Systemd、Docker和Kubernetes。由于可插拔的运行时功能，你也可以用Docker运行它。
* https://github.com/nestybox/sysbox


* 我们开始看到应用框架和开发者工具为在Kubernetes等平台上运行提供高级抽象。Tye是一个有趣的.NET工具，它可以简化在云原生平台上运行.NET应用程序。
* https://github.com/dotnet/tye


* Turandot允许在Kubernetes中使用TOSCA。TOSCA提供了一种高级服务描述，旨在实现底层基础设施之间的可移植性和互操作性。
* https://turandot.puccini.cloud/


* Copper是一个Kubernetes的配置文件验证器。它支持使用内置的Javascript DSL编写定制测试。
* https://github.com/cloud66-oss/copper






