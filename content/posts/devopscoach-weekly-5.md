---
date: 2020-08-25T15:20:51+08:00
title: "DevOps Coach 周刊 #5"
subtitle: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
description: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
categories: "DevOps"
tags: ["周刊"]
keywords: ["DevOps", "DevOps教练", "周刊"]
bigimg: [{ src: "/images/abstract-3.jpg", desc: "周刊" }]
---

## 宕机

- 上一周新发的宕机事故。
- 近期全球重大宕机事故的分析总结、事后回顾。

> May your queries flow and your pagers stay silent.
> --Dave, Betsy, Niall, Stephen, and Ken

### Equinix 重大电力故障让数据中心客户大发雷霆

- 关于 Equinix ：Equinix 是全球领先的数据运营商，目前在美洲、亚太、欧洲及中东 14 个国家（地区）的 31 个市场运营着 94 个国际业务交换。
- 消息来源 CBR https://www.cbronline.com/news/equinix-outage

> 教练点评：数据中心 UPS 的单点故障并不稀奇，但是这次 Equinix 的事故堪称史诗级事故。

"经历如此严重的停电，显然是不可接受的"

北京时间 8 月 19 日 8 点 10 分更新：最后的电路似乎已经在 8 月 18 日晚间约 22 点 20 分恢复；在停电开始后约 18 小时。

数据中心巨头 Equinix 表示，在其位于伦敦码头区的 IBX LD8 数据中心遭遇长时间停电后，它已经为所有客户恢复了机架--该问题使数百名客户（包括几家 ISP）的服务从北京时间凌晨 4:30 开始离线；使许多人对缓慢的电力恢复深感沮丧。

"Equinix 工程师已将问题的根本原因诊断为 UPS（不间断电源）系统故障，我们正在与客户合作，以尽量减少影响。该公司在北京时间 8 月 18 日 12:04 的首次公开声明中表示："我们对由此造成的任何不便感到遗憾。(ISP Giganet 负责人 Matthew Skipsey 早些时候将 Equinix 缺乏沟通描述为 "糟糕透顶")。

多名客户指出，该问题是 Galaxy UPS 系统(由施耐德销售)中的输出静态开关出现故障。该开关将关键负载连接到 UPS 的条件电源或旁路电源的原始电源。停电时间的长短表明，LD8 的 A+B 交流电源是来自同一个 UPS。期望其直流供应商确保弹性和依赖单一数据中心的 ISP 正在吸取惨痛教训。

伦敦互联网交易所 LINX 同时表示，约有 150 名 LINX 会员直接受到此次事件的影响。(到 13:42，LINX 的所有设备都恢复了。该组织有 900 多个 ASN 从 80 多个不同的国家连接）。)

受影响的一个客户是 ISP Giganet。它告诉客户。"我们仍在等待我们的网络架恢复供电 继 Equinix 和他们的承包商在早期故障后将电源迁移到新的基础设施上之后。

"可悲的是，仍然没有估计的修复时间，这是最令人沮丧的。他们已向我们保证，他们将在可能的情况下提供这一信息。Equinix 不断被追问最新情况。正如您所了解的那样，这是一个 P1 问题，影响着许多 100 多家其他运营商/ISP--所以它被赋予了最大的优先级。"

据了解，英国电信也是受影响的公司之一。数据中心的访问控制系统已经被中断，一个客户，马修-斯基普西说，"所以一切[是]通过双向无线电手动运行，然后通过其他地方打电话。疯狂的时代。这是一个 MBORC 的地狱。"

Equinix 表示，它允许客户 "更灵活地访问 LD8"，因为它争分夺秒地解决这个问题，"在我们的 COVID-19 限制内工作"。

Giganet 补充道："我们已经在凌晨 4.23 时左右失去了我们 2 个 Equinix LD8 机架中的 1 个机架的两个 A+B 馈线。此前，根据 Equinix 的报告，UPS 出现故障，然后触发了数据中心的火警。我们失去电源的机架上安装着我们的核心 Juniper MX 路由器和 Cisco LNS。瞻博网络 MX 路由器是我们的核心设备，LD8 中的一切功能都需要它，包括终止一些专线连接以及为我们的 vDC 平台提供连接。我们所有的设备电源都是由数据中心提供的'多样化'A+B 电源双馈--但是经过这次事件，我们怀疑是缺乏弹性，在事件解决后一定会提出来，因为经历如此严重的断电显然是不可接受的。"

### Google 公司的云平台和 G Stuit 系列事故

- 来源官方 https://status.cloud.google.com/incident/zall/20008#20008005
- Google Cloud Infrastructure Components Incident #20008
- GCP 多个产品发生故障：App Engine, Cloud Storage 和 Cloud Logging
- G Suit 多个模块和功能：Gmail, Drive, Docs/Editor, Chat, Meet, Keep, Voice, Jamboard, Admin Console
- 事故时间：August 19, 2020, from 20:55 to 03:30
- 诊断：AppEngine 的部署会报错，访问 GCS 桶时的高延迟，以及 Cloud Logging 中的日志条目丢失。G Suit 多种产品报错和无法使用。
- 详细的事故总结报告https://static.googleusercontent.com/media/www.google.com/zh-CN//appsstatus/ir/bd9m3vkqwpvkk4j.pdf
- 根本原因
  - 许多 Google 服务使用一个通用的、内部的、分布式的系统来存储不可变的、非结构化的数据，也就是二进制大对象，或者说 blob。这个 blob 存储系统包含一个与 Google 内部客户端服务对接的前端，一个处理元数据操作的中层，以及一个用于存储数据的后端。blobs 本身。当客户端向前端提出请求时，元数据操作被转发到元数据服务，元数据服务与存储服务进行通信。
  - 来自另一个 Google 服务的流量增加开始使元数据服务超载，导致任务变得不健康，请求的延迟增加。这种延迟促使这些操作的过度重试，导致资源耗尽。自动化系统试图启动新的元数据任务。然而，其中许多任务立即被其收到的流量所淹没，而这些任务也被淹没。由于资源枯竭，分配到的资源不足。这一问题因以下原因而更加严重： 策略用于取消和重试失败的请求，这对流量造成了倍增效应。
  - 与其他产品相比，谷歌云存储受到的影响较小。虽然谷歌云存储是建立在 同一个 blob 存储系统，GCS 的元数据层大多与受影响的元数据层隔离。谷歌内部元数据服务。对于 "美国"，GCS 元数据隔离的迁移正在进行中。多区域，而所有其他迁移工作已经完成。因此，对全球通信系统客户的影响是 减少，这种影响仅限于 "美国 "多区域。

> 教练点评：从事发时刻到 Google 工程师收到告警的时刻（20：58）之间只有短短的 3 分钟，在一个小时内受影响的各个 GCP 服务就开始了并行的调查和补救措施。在 23：00 定位到 blob 存储是根因故障，并实施配置变更，消除了大多数的内部错误。这正是 SRE 中所讨论的重大事故应急流程的有效执行，能快速有效的恢复服务。可以看出 Google 团队在事故响应方面的训练有素。

### Spotify

- 来源官方 Twitter 账号： https://twitter.com/SpotifyStatus/status/1296064517504409600
- 这好像是由于 TLS 证书过期导致的。
- 其它媒体报道： https://www.teiss.co.uk/spotify-outage-expired-tls-cert/
- 据报道，周三发生了影响音乐流媒体服务 Spotify 的长达一小时的大规模中断，原因是该公司未能在 TLS 证书到期前更新。
- 不过，Cloudflare 的网络工程师 Louis Poinsignon 提供了 Spotify 系统内部到底发生了什么事情的线索。据他介绍，该公司显然没有及时更新 TLS 证书，证书过期导致中断。在 TLS 证书更新后，Spotify 的服务很快就恢复了在线。

> 教练点评：Spotify 的特有的团队工作开发模式一直是一种学习的榜样，很难想象他们的服务会在这样简单的问题上翻船。

## 新闻

### DevOps 大会/峰会

中国 DevOps 社区流水线大赛 -- Pipeline Craft Championship

- 8 月 18 日开始为期两个月，免费活动
- 报名：https://wj.qq.com/s2/6852880/c181
- 活动官网：https://Pipeline.devopsmeetup.com

GitLab 的大会 -- Commit: You belong here

- 8 月 26 日
- 线上免费峰会
- https://about.gitlab.com/events/commit/

推荐你感兴趣的大会和峰会，发邮件到：martin@devopscoach.org

### Grafana Labs 喜提 B 轮 5000 万美元融资

- 来源官方：https://grafana.com/about/press/2020-08-17-series-b-announcement/
- 8 月 27 日宣布
- Grafana Labs 还宣布了 Grafana 加速器计划（GAP），以培养在更广泛的 Grafana 生态系统中进行创新的早期公司和副业项目。GAP 将提供免费的 Grafana Cloud 和 Grafana Enterprise 订阅、现金补助、股权融资以及进入 Grafana Labs 核心开发者的内部通道。

> 教练点评：这个 CNCF 的热门项目终于迈向了商业化的第一步，随着企业订阅模式的形成，且看后续的创新开发和社区经营是否也能一浪高过一浪。

## 文章

- 《 Ops 工作的未来 》
- 一篇关于运维角色变化的好文章。对于那些想知道现代运维是什么样子的人来说，有一些很好的提示，包括供应商管理、外包基础设施和理解社会技术系统的重要性。
- https://acloudguru.com/blog/engineering/the-future-of-ops-jobs

- 《 NAT 是如何工作的 》
- 对于任何想要更好地了解这个网络领域的人来说，这是一本很好的 NAT 网络介绍。好的图和例子，还有很多细节。
- https://tailscale.com/blog/how-nat-traversal-works/

- 《 如何打造给董事会看的软件开发 KPI 报表 》
- 度量标准有很多不同的用途，包括向组织高层报告。这篇文章探讨了用于董事会对话的工程 KPI。
- https://codeclimate.com/blog/engineering-kpis-board-deck/

- 《 马丁富乐老师：单链接通道 》
- 有没有想过确保服务之间的消息保持有序，并为任何丢失的消息建立重试机制？这篇文章描述了一个具体的模式，但也是一组关于分布式计算模式的文章的一部分，值得探讨。
- https://martinfowler.com/articles/patterns-of-distributed-systems/single-socket-channel.html

- 《 提升事故回顾质量的套路 》
- 事故回顾越来越常见，但往往很难做好。这段视频和详细的文字记录有各种改进流程的技巧。
- https://www.blameless.com/blog/improving-postmortems-paul-osman

- 《 应用日志开发的最佳实践 》
- 即使你不是用 Java 编写应用程序，掌握一些关于日志工作的知识通常也是有用的，因为你可能最终会至少运行一些 Java 应用程序。这些帖子提供了一个坚实的基础。
- https://sematext.com/blog/java-logging/
- https://sematext.com/blog/java-logging-best-practices/

## 工具

- 标签对于大规模管理 AWS 资源至关重要。Awstaghelper 提供了一个命令行工具，可以轻松地在广泛的 AWS 资源中向 CSV 文件或从 CSV 文件中添加和管理标签。
- https://github.com/mpostument/awstaghelper

* GitOps 工具包是一套可组合的 API 和专门的工具，可用于在 Kubernetes 之上构建一个持续交付平台。它们应该可以为 Flux 的 v2 提供基础，但也可以用来构建其他有趣的高级工具，采用同样的控制循环方法。
* https://toolkit.fluxcd.io/

- Kip 是一个虚拟 Kubelet 提供商，它允许 Kubernetes 集群透明地将 pods 发射到自己的云实例上。如果你需要额外的工作负载隔离，这很方便。
- https://github.com/elotl/kip

## 学习资源

这里推荐一些值得关注和学习的免费视频学习资料。

> 教练点评：B 站里的相关视频是不可忽视的学习资源。善加利用，就可以加速获取知识的进度。

波波老师的系列课程

- https://space.bilibili.com/518029478/video
- 包括 k8s 和微服务等 DevOps 技术

【SpringBoot 项目实战】 2020 最新在线教育 spring boot 分布式项目实战

- 系统后端接口部分，使用目前流行的 SpringBoot+SpringCloud 进行微服务架构，使用 Feign、Gateway、Hystrix，以及阿里巴巴的 Nacos 等组件搭建了项目的基础环境。项目中还使用 MyBatisPlus 进行持久层的操作，使用了 OAuth2+JWT 实现了分布式的访问，项目中整合了 SpringSecurity 进行了权限控制。除此之外，项目中使用了阿里巴巴的 EasyExcel 实现对 Excel 的读写操作，使用了 Redis 进行首页数据的缓存，使用 Git 进行代码的版本控制
- https://www.bilibili.com/video/BV1y7411y7am
- 播放量： 10w+

2019 谷粒商城微服务 SpringBoot,Dubbo,MySql 高级,Redis 秒杀,ElasticSearch,ActiveMQ,SSO 单点登

- https://www.bilibili.com/video/BV1B4411V7cA
- 2019 谷粒商城微服务 SpringBoot, zookeep 注册中心, Dubbo, MySql 高级, ElasticSearch, ActiveMQ, 通用 mapper, 解决秒杀, SSO 单点登录, OAuth2 协议三方登录, 第三方支付接口对接, Redis lua 脚本, Redis 秒杀, Redis 分布式锁, 集群搭建, 分布式, sku,spu 表结构介绍, 等等技术结合使用~~~~~~~~~~~
- 播放量： 10w+

Git+GitHub 教程

- https://www.bilibili.com/video/BV1pW411A7a5
- Git 是先进的分布式版本控制系统，而 Github 是常用的 Git 代码托管中心。
  本套教程内容丰富、详实，囊括：Git 安装过程、本地库基本操作、远程基本操作、基于分支的 Gitflow 工作流、跨团队协作的 Forking 工作流、Eclipse 中的 Git 版本控制以及 Git 对 Eclipse 特定文件忽略的配置方法。还通过展示 Git 内部版本管理机制，让你了解 到 Git 高效操作的底层逻辑。教程的最后完整演示了 Gitlab 服务器的搭建过程。
- 播放量： 21w+

GitLab 与 GitFlow 的简单使用

- https://www.bilibili.com/video/BV1Wb411e7ec
- 播放量： 1w+
