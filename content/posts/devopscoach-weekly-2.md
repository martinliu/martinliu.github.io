---
date: 2020-08-03T22:26:23+08:00
title: "DevOps Coach 周刊 #2"
subtitle: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
description: "推荐 DevOps 教练学习的全球新闻，文章，宕机事件和流行工具"
categories: "DevOps"
tags: ["周刊"]
keywords: ["DevOps","DevOps教练","周刊"]
bigimg: [{src: "/images/abstract-4.jpg", desc: "周刊"}]
---


![DevOps Coach weekly update](/images/weeklyupdate.jpg)

## 宕机

上周全球重大宕机事故清单。

### Facebook

* 具英媒体报道：7月 28 日 12：20pm， Facebook, Instagram 和 WhatsApp 这三款用户的一半以上的用户，无法加载出页面，无法正常使用服务。 Facebook 官方还没有关于这次事故的回应。实际上整个欧洲大陆，特别是葡萄牙和西班牙的故障更要严重一些。原因不明。
* 影响范围：London, Birmingham 和 Manchester.
* 来源： https://metro.co.uk/2020/07/28/facebook-instagram-whatsapp-13048914/



### fastly - 知名 CDN 服务商

* 官方声明：Fastly的网络具有内置冗余和自动故障转移路由，以确保最佳性能和正常运行时间。但当网络问题出现时，我们认为我们的客户应该得到清晰、透明的沟通，这样他们才能保持对我们的服务和团队的信任。当我们重新分配流量、升级硬件或在极少数情况下我们的网络不提供流量时，我们会在这里发布通知。如果您遇到问题而没有看到张贴的通知，请发送电子邮件至 support@fastly.com 寻求帮助。
* 影响范围：North America (Ashburn (BWI), Ashburn (DCA), Ashburn (IAD), Ashburn (WDC), Atlanta (FTY), Atlanta (PDK), Dallas (DAL), Dallas (DFW), Jacksonville (JAX)).
* 来源：https://status.fastly.com/history


### Heroku 

* 官方声明：JUL 28, 2020 09:15 UTC Heroku 平台的很大的部分都遭受到可用性故障。然后开始和他们的服务提供商一起解决问题。一个多小时后平台恢复了正常。
* 来源：https://status.heroku.com/incidents/2090


## 新闻

DevOps实践的采用与组织拥抱数字化转型齐头并进。这两个短语都有被过度使用的风险，但这些帖子讨论了一些有用的心理模型，以帮助聚焦对话。
* https://aws.amazon.com/blogs/enterprise-strategy/mental-models-for-digital-transformation/
* https://aws.amazon.com/blogs/enterprise-strategy/mental-models-to-clarify-the-goals-for-of-digital-transformation-part-2/


开发者平台的哪些属性会导致采用？下面的文章是专门关于大规模边缘平台的，但对于任何为开发者构建各种平台的人来说，包括在内部平台团队中这样做的人来说，都是很好的阅读。
* https://blog.cloudflare.com/cloudflare-workers-serverless-week/


当第一次接受DevOps实践和云服务时，在大型组织中通常会建立一个卓越中心。在采取这种方法时，需要避免一些陷阱，下面的文章将讨论这些陷阱。
* https://www.contino.io/insights/cloud-centre-of-excellence-2020


最近的DevSecCon在线会议的视频都可以看到，其中涵盖了一系列有趣的主题，包括基础设施作为代码安全、持续审计合规、供应链攻击等。
* https://www.mydevsecops.io/post/devseccon24


关于无服务器架构和单体应用之间的权衡，主要集中在较小规模的应用上，是一个不错的讨论。
* https://dev.to/iamcherta/my-monolith-doesn-t-fit-in-your-serverless-311o


一篇关于linux内核新特性的深度技术文章，这些特性应该会让非特权容器更受欢迎。对seccomp的细节也做了很好的介绍。
* https://people.kernel.org/brauner/the-seccomp-notifier-new-frontiers-in-unprivileged-container-development


基于角色的访问控制在保护Kubernetes的安全方面发挥着重要作用。这个方便的网站将文章、工具和官方文档收集在一起。
* https://rbac.dev/


对于任何使用Serverless技术的人来说，这是一项有趣的调查，来自该领域的众多公司。我期待着结果公布时的到来。
* https://codingsans.typeform.com/to/mPinnC

## 文章


LaunchDarkly从基于 Polling 的架构开始，最终迁移到向客户推送变化量（Streaming）。Dawn Parzych--LaunchDarkly。
* https://launchdarkly.com/blog/launchdarklys-evolution-from-polling-to-streaming/

一个更简单的分布式跟踪的替代方案，用于故障排除。
简要概述了分布式追踪的一些问题，以及涉及人工智能的另一种方式的建议。 Larry Lancaster - Zebrium
* https://www.zebrium.com/blog/virtual-tracing-a-simpler-alternative-to-distributed-tracing-for-troubleshooting


谷歌云 对 Classroom 的故障总结报告 2020-07-07
这是Google在7月7日对其Google Classroom 事件的事后报告。
* https://static.googleusercontent.com/media/www.google.com/en//appsstatus/ir/u5sinmib27yly4i.pdf

面向领域的微服务架构介绍
长期以来，Uber一直是微服务的倡导者。现在，凭借几年的经验，他们分享了他们所学到的经验，以及如何处理一些陷阱。Adam Gluck - Uber
* https://eng.uber.com/microservice-architecture/

通过远程事件响应使PagerDuty始终保持开启状态。
本文开篇就从PagerDuty的角度对Cloudflare中断的情况进行了有趣的描述。Dave Bresci - PagerDuty
* https://www.pagerduty.com/blog/remote-incident-response/

安全是设计出来的？
这篇文章反映了两种不同的安全理念。
* 工程设计应确保系统的安全。
* 单纯的设计不能保证系统的安全
Lorin Hochstein
* https://surfingcomplexity.blog/2020/07/28/safe-by-design/

我们能做的就是发现问题
你不能用可用性指标来告知你的系统是否足够可靠，因为它们只能在你出现问题时告诉你。
Lorin Hochstein
* https://surfingcomplexity.blog/2020/07/28/all-we-can-do-is-find-problems/

## 工具推荐

管理 K8s 命令行工具的工具，所有命令行工具一站式搞定，一键式安装很多 k8s 集群基础。
* https://github.com/alexellis/arkade/

一个在文件系统之上的文件系统。
* https://github.com/carlosgaldino/gotenksfs

一个 Cloud-Native API Gateway
* https://github.com/apache/apisix

一个简单而全面的容器漏洞扫描器，适用于CI。
* https://github.com/aquasecurity/trivy
