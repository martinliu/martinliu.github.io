---
date: 2020-08-31T00:11:01+08:00
title: "DevOps Coach 周刊 #6"
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

### 上周新发事故

* Zoom 无法开始和加入会议， 官方报道 https://status.zoom.us/incidents/1z2lrf4nrv8p
* Slack 多个功能模块服务降级，甚至无法使用，官方：https://status.slack.com//2020-08/960bbb3c9d49a3cc 
* Let's Encrypt 数据中心硬件方式故障导致 API 报错，官方：https://status.io/pages/incident/55957a99e800baa4470002da/5f45330250878c04bf3fb6eb 
* NZX 新西兰证券交易所遭受重大DDoS攻击导致NZX停电，交易停止。媒体：https://www.stuff.co.nz/business/122562006/major-ddos-attack-causes-nzx-power-outage-trading-halt 
* eBay宕机。服务器状态最新，DNS故障和服务不可用的错误错误，媒体：https://www.express.co.uk/life-style/science-technology/1329281/eBay-down-server-status-DNS-failure-service-unavailable-error
* Heroku 发生大量的 H100 报错，官方：https://status.heroku.com/incidents/2101
* Fastly CDN 服务商的服务发生多区域性能故障，官方：https://status.fastly.com/incidents/p1lwmmv2j2gq
* Cloudflare 上周发生的这个问题，我的个人 blog 也遇到了，Google 的搜索索引服务记录了那些 500 错误，我也感到非常诧异；第三方传输供应商问题导致HTTP 5xx错误增加； 官方：https://www.cloudflarestatus.com/incidents/hptvkprkvp23



### 鳄鱼杯：2020年第二季度最大宕机颁

来源：https://statusgator.com/blog/2020/08/21/5-biggest-outages-of-q2-2020/

![](/images/crocodile-cup-3-1.jpg)

任何可能发生的坏事都会发生。这句古老的谚语100%适用于技术行业，在这个行业中，崩溃和中断远比销售和营销团队希望我们想象的要常见得多。然而，与基础设施打交道的DevOps工程师知道，要确保所有东西都能一直按预期工作是多么困难--并配置监控，实际跟踪系统的健康状况，帮助防止崩溃和停机。

在StatusGator，我们监控800多个基于云的服务的状态页面，并向用户提供即时通知。我们拥有堆积如山的宕机和中断数据，并能看到全貌，因此我们决定每季度制定一份最高宕机时间列表。我们希望我们的发现能够激励DevOps工程师去看看其他人是如何处理服务中断的，以便他们能够提高自己的可靠性。

请继续阅读，了解2020年第二季度的五大故障，以及Slack、Zoom、GitHub、IBM Cloud和T-Mobile在这些危机中如何行动。我们还对这些故障的结果进行了评级，并很乐意听到您对我们评级的看法。

#### 第一名 Slack 全球范围的服务中断, May 12, 2020

Slack是全球数千家公司的主要沟通方式，因此其稳定的正常运行时间是最重要的问题。因此，当用户在美国东部时间晚上7:30左右停止发送和接收Slack消息时，情况迅速升级为一个全面的问题。与之前的故障期间不同，这影响到了整个Slack生态系统：没有人能够登录Slack，也没有人能够收到任何通知。"Slack宕机了吗？"，用户们自问自答，答案是毋庸置疑的 "是！"

美国东部时间晚上10:26，Slack报告全面恢复了服务，并再次为造成的不便道歉。更重要的是，他们在Medium上发表了一份详细的事后报告，解释了问题背后的原因，他们为克服这个问题所采取的行动，得出的结论，以及他们正在采取的措施，以消除类似情况再次发生的机会。

欢迎阅读这篇事后总结，它的技术性很强，但即使是普通人也很容易理解。Slack在这里展示了他们对用户群成员--包括开发者和大众用户群--的关心，这篇文章所投射出的信心令人钦佩。

这里需要注意的是，虽然问题本身是在美国东部时间上午8:30开始的，但直到美国东部时间晚上7:30左右，多名用户报告了Slack的问题，这个问题才完全被人察觉。在Slack团队意识到这一情况之前，他们在应用内部（当时大部分已经宕机）、Twitter上、Downdetector上、Slack网站（很快就宕机了）以及其他许多渠道进行了报告。

#### 第二名 Zoom 宕机, May 17, 2020

自冠状病毒大流行以来，随着越来越多的人远程工作和学习，Zoom的使用率急剧上升。Zoom状态页面的订阅量也是如此，自4月份以来，StatusGator中的订阅量急剧上升。

除了企业被迫开始远程办公外，许多教会和其他公共组织也开始使用Zoom来举行周日弥撒、会议以及举办公共活动。因此，虽然周日不是工作日，但英国的许多付费账户很快就发现他们无法主持或加入Zoom会议（免费账户似乎没有受到影响）。这个问题通过多种渠道被报告，包括Twitter和监控Zoom状态的StatusGator。

Zoom发言人回应称，承认意识到了这一情况，并提到这只影响了一个子集的用户。然而，我们都知道子集可能是1%或99%，Zoom没有提供任何关于受影响用户量的说明。提供更透明的受影响用户的比例是一个高质量状态页面的标志，这是Zoom应该改进的地方。

#### 第三名 GitHub 又无法访问了. June 29, 2020

自从GitHub被微软以75亿美元收购后，GitHub似乎又下降了很多。原因尚未披露，我们只能猜测原因。也许是与GitHub基础设施与微软系统的整合有关。也许是因为GitHub的发展速度更快，增加了更多的功能。无论如何，从收购到现在已经快两年了，用户发现GitHub的持续宕机时间越来越长。我们对GitHub状态页面的独立分析证实，在过去的两年里，宕机变得更加频繁。

微软正在努力将GitHub变成一个比以前更好的开发者场所。这家雷德蒙德巨头在今年早些时候让所有的付费计划变得更加实惠，并免费提供一些关键功能，将更多的工具放在IT专业人士的手中。微软、苹果、AWS、谷歌、Facebook和其他数千家公司使用GitHub来存储和运行他们的代码仓库，因此它的正常运行时间是最重要的。

然而，GitHub在2020年6月29日出现了两个小时的故障。整个网站及其服务都无法访问，因此许多开发人员甚至无法推送代码或部署他们的应用程序，因为GitHub集成的数量没有响应。自然，这引起了很大的反响，并导致GitHub除了状态页面外，还推出了每月的可用性报告，对每次中断的原因和结果进行了详细的解释。 

#### 第四名 IBM Cloud 挂了，服务状态页面有更新, June 10, 2020

任何基于云的服务都会犯的最大错误之一就是将其状态页面托管在自己的基础设施上。看来IBM云就是这么做的，所以当它的整个基础设施在6月份有几个小时无法访问的时候，它的状态页面也随之而来。我们本可以期待IBM在今年3月的达拉斯宕机事件后得出一些结论，但是，显然，他们并没有理会，或者说没有做出足够的努力。

于是，在2020年6月10日，IBM云基础设施在全球范围内宕机。这次宕机使得Watson AI、IBM Cloud Foundry、Kubernetes Service、云对象存储、身份访问和管理、VPS的VPN、App Connect等功能完全无法访问。幸运的是，IBM Cloud状态页面只在中断初期无法使用，后来才断断续续地可用。这也是为什么StatusGator还能向订阅了IBM Cloud状态页面的用户发送提醒的原因。

该公司完全没有告知中断的原因，以及为缓解影响所采取的措施。后来从一个独立的监控服务机构了解到，一个第三方网络提供商广泛使用了流量路线，导致IBM云配置带宽严重受限。IBM专家对系统进行了重新配置，并恢复了运行，但随后并没有官方的解释或公告--这让用户非常失望。

这不是IBM第一次在公共关系上失败，我们认为，也不会是最后一次。这可能是他们尽管提供了多样化的有竞争力的云服务，却远远落后于AWS、谷歌云平台、微软Azure和其他云服务商的原因之一。

但IBM能做什么呢？自然是有一个独立的状态页面! 下面只是他们可以使用的一些变种。

#### 第五名 T-Mobile冲洗其网络下水道，2020年6月15日。

作为美国、欧盟和英国最大的移动网络运营商之一，T-Mobile最近发现自己正处于一场完美的风暴之中，它在美国各地连续13个小时无法提供语音和短信服务。外界观察家马修-普林斯（Matthew Prince，CEO@Cloudflare）认为，"T-Mobile对他们的网络进行了一些改变，但这些改变出了问题，导致他们的用户出现了一连串的故障"。他还表示，"这场灾难几乎可以肯定完全是T-Mobile团队自己造成的"。

相反，T-Mobile技术总裁Neville Ray在推特上表示，虽然这确实是一个 "影响全国用户语音和文字服务的重大问题"，但它源于第三方供应商的系统故障，T-Mobile的工程师正在努力修复。随后，他在博客中详细阐述了这一话题，并对故障原因进行了解释。

引用雷先生的话说："据悉，触发事件是东南部的第三方供应商的租用光纤电路故障。这是每一个移动网络都会发生的事情，所以我们与我们的供应商合作，建立冗余和弹性，以确保这种类型的电路故障不会影响客户。这种冗余让我们失败了，导致了过载的情况，然后又因为其他因素而变得更加复杂'。这导致IP池过载，美国所有地区都发生了崩溃。

由于无法接触到大多数服务，T-Mobile的客户开始报告Facebook、Instagram和其他平台无法使用，而实际上离线的是他们的移动运营商网络。Business Insider报道称，虽然T-mobile客户将故障归咎于AT&T和Verizon，但这两家运营商都是在正常的负载水平下运营的。不过，前述Neville Ray的帖子表示，T-Mobile正在采取一切必要措施，通过为所有核心系统建立双重弹性和冗余措施，确保未来不可能发生此类事件。

可以看到，公司无法明确表达自己的立场，从一开始就不愿意承担失败的责任，以及在故障发生后缺乏透明度，都没能让T-mobile毫无污点地走出困境。这甚至导致了他们面临大规模DDoS攻击却未能击退的传闻。


### StatusGator为第二季参赛者颁奖

让我们根据这些宕机事件的发现、相关公司的沟通以及每个事件的结果来评定。

![](/images/gator-q2.png)

![](/images/Group-20-2048x1474.png)

## 新闻

## 软件发布

* Kubernetes 1.19 发布了， 它由34项增强功能组成。10个增强版转为稳定版，15个增强版在测试版，9个增强版在alpha版。
* AWS 发布新的 EBS 卷类型 (io2) 提高 100x 持久性，和 10x 倍的 IOPS/GiB
* Tekton Hub 预览版上线，随着该项目对底层流水线和构建的定义的日臻成熟，开放出一个相关的自由市场也是必然的，开源生态催生出来的上下游技术提供和消费的模式正在普及中，无周边生态的很难获利和发展，https://hub-preview.tekton.dev/

### DevOps 大会/峰会

#### 中国 DevOps 社区流水线大赛 -- Pipeline Craft Championship

- 8 月 18 日开始为期两个月，免费活动
- 报名：https://wj.qq.com/s2/6852880/c181
- 活动官网：https://Pipeline.devopsmeetup.com

#### SnykCon

* 将在10月21日/22日举行一个关于所有应用安全和 DevOps 的在线活动。免费注册，CFP现在开放。
* https://snyk.io/snykcon/


推荐和分享你感兴趣的大会和峰会给我和其它人吧？发邮件到：martin@devopscoach.org



## 文章

![](/images/WhyAvoidAutomation.gif)

* 这是一篇很好的文章，讲述了在整个组织中获得变革的支持时，自动化这个词所带来的问题，以及为什么观念很重要。
* https://blogs.starcio.com/2020/08/avoid-calling-it-automation.html

* 什么是Kubernetes Operators，为什么它对SRE很重要？
* 在Kubernetes Operators: 自动化容器编排平台》中，作者Jason Dobies和Joshua Wood将Operators描述为 "其应用的自动化站点可靠性工程师"。鉴于SRE的多方面经验和多样化的工作量，这是一个大胆的说法。那么，Operators到底能做什么呢？
* https://www.blameless.com/blog/what-is-a-kubernetes-operators-and-how-to-automate-sre


* 探讨遗留IT系统的隐秘世界。探讨了一些值得注意的事件，以及我们需要更多地了解如何建立可长期运行的系统。
* https://spectrum.ieee.org/computing/it/inside-hidden-world-legacy-it-systems


* 一篇文章，讲述了随着组织的发展，增加一个总括性的平台团队的风险，以及为什么向平台组件和重用发展可以更具扩展性。
* https://kislayverma.com/organizations/a-case-against-platform-teams/


* NoOps Go on Cloud Run 
* https://medium.com/@peter.malina/noops-go-on-cloud-run-689d92215c5c




## 工具

* werf/werf : GitOps 交付工具 
* ovh/cds : 企业级持续交付和 DevOps 自动化开源平台，
* markphelps/flipt 一个现代的功能开关方案
* fluxcd/toolkit ： 用 GitOps 的方式组装 CD 流水线的体验版工具包。
* 

## 学习资源

本周推荐如下 B 站学习资源。


Jenkins+Ansible+Gitlab自动化部署（CI/CD）

* https://www.bilibili.com/video/BV1Dp411Z7Lf
* 持续集成在工作中的应用。

通俗易懂ElasticSearch 项目实践课程

* https://www.bilibili.com/video/BV1wA411n7LY
* 搜房网实例项目讲解


【Python趣味教学】99%相似度！手把手教你用Python制作超级玛丽游戏

* https://www.bilibili.com/video/BV1G54y197C2
* 前26集都在这了，爱编程的小伙伴们，一起来重现童年经典吧！


Kubernetes教程 k8s企业级DevOps实践

* https://www.bilibili.com/video/BV1c64y1F7wP
* k8s是一个开源的，用于管理云平台中多个主机上的容器化的应用，Kubernetes的目标是让部署容器化的应用简单并且高效（powerful）,Kubernetes提供了应用部署，规划，更新，维护的一种机制。

