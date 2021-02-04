---
date: 2020-07-28T10:35:19+08:00
title: "DevOps Coach 周刊 #1"
subtitle: "DevOps 教练需要学习的全球新闻，文章，宕机事件和流行工具"
description: "DevOps 教练需要学习的全球新闻，文章，宕机事件和流行工具"
categories: "DevOps"
tags: ["周刊"]
keywords: ["DevOps","DevOps教练","周刊"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/abstract-1.jpg", desc: "DevOps"}]
---

![DevOps Coach weekly update](/images/weeklyupdate.jpg)

## 新闻

又到了一年一度的时间。定期的Puppet Devops状态调查已经开始。今年的重点是变革管理、持续交付和自服务平台之间的关系。
https://polls.onresearch.net/xsurvey/20JT028/20JT028T1/Survey.aspx?ckie=true

文档和设计在构建强大的系统中起着至关重要的作用。这篇文章探讨了为什么设计文档是有用的，以及它们应该包含什么样的内容。
https://www.industrialempathy.com/posts/design-docs-at-google/

一份关于公共Terraform代码安全状况的新报告。对于任何使用Terraform配置服务的人来说，一些有用的数据和一些好的提示。
https://bridgecrew.io/blog/state-of-open-source-terraform-security-report-2020/

看看如何使用 Azure Pipelines 自动验证 sysmon 配置。
https://medium.com/falconforce/using-azure-pipelines-to-validate-my-sysmon-configuration-48315dba7571

这是一个很好的大规模迁移低级组件的故事，在这个案例中是一个应用服务器。金丝雀的推出、上游贡献、性能和其他有趣的话题。
https://about.gitlab.com/blog/2020/07/08/migrating-to-puma-on-gitlab/

拥抱云原生技术和工作方式会带来挑战，本帖记录了其中一些挑战，包括安全、缺乏专业知识、发布周期缓慢等。
https://www.cloudops.com/2020/07/top-7-challenges-to-becoming-cloud-native/

## 文章

“How could they be so stupid?” 上周知名Twitter 账号入侵事件出现了更多细节，导致一些人说出了上面这句话。这里有一个看法，如何看待这不是 "愚蠢 "的问题。Lorin Hochstein
https://surfingcomplexity.blog/2020/07/20/how-could-they-be-so-stupid/

Data Consistency Checks 你的数据库中的数据应该是一致的......但话说回来，事故不应该发生，对吗？Slack接受在他们的规模下，数据经常会出问题，他们有框架和一套工具来处理它。Paul Hammond and Samantha Stoller — Slack
https://slack.engineering/data-consistency-checks-e73261318f96

Obstacles to Learning from Incidents 我从这篇文章中学到了很多东西。我最喜欢的障碍是 "通过差异化来拉开距离"，比如 "我们绝对不会以这种方式应对事件"。Thai Wood — Learning from Incidents
https://www.learningfromincidents.io/blog/obstacles-to-learning-from-incidents

You don’t need SRE. What you need is SRE. […] SRE，也就是谷歌定义的SRE，对于大多数组织来说并不适用。Sanjeev Sharma
https://sdarchitect.blog/2020/02/20/you-dont-need-sre-what-you-need-is-sre/

Questionable Advice: “What’s the critical path?” 专家建议，当你试图弄清楚你的关键路径是什么（以及为什么你想知道它是什么）时，应该问什么问题。Charity Majors
https://charity.wtf/2020/07/24/questionable-advice-whats-the-critical-path/

Thinking About Your Humans With J. Paul Reed 这个播客集有点像J.Paul Reed和Tim Heckman在https://srefromhome.com/的联合演讲的预览。我喜欢他们把这场传染病大流行称为长达数月的事件，并指出如果你总是在事件中，那么你永远不会在事件中。Julie Gunderson and Mandi Walls — Page it to the Limit
https://www.pageittothelimit.com/thinking-about-your-humans/

Rebuilding messaging: How we bootstrapped our platform 我喜欢一个好的双写故事。以下是LinkedIn如何过渡到新的消息存储机制。 Pradhan Cadabam and Jingxuan (Rex) Zhang — LinkedIn
https://engineering.linkedin.com/blog/2020/bootstrapping-our-new-messaging-platform

Using Automation and SLOs to Create Margin in your Systems 在系统中留有余地，使其具有适应能力，并利用SLO(同情地)来推动优先事项的确定。
https://thechief.io/c/blameless/using-automation-and-slos-create-margin-your-systems/

How to Classify Incidents  如何对事件进行分类 什么是事件分类？为什么要对事件进行分类？事件严重性与优先级，以及如何创建事件类别？
https://thechief.io/c/blameless/how-classify-incidents/

## 宕机

上周全球重大宕机事故清单。

*  Garmin 作为佳明手表和 app 的用户，我体验到了这场 24+小时的服务中断
	*  https://spectrumlocalnews.com/nys/rochester/ap-online/2020/07/24/garmin-fitness-tracking-service-goes-down-frustrating-users
*  Snapchat 打不开 app，黑屏，无法使用摄像头相关功能
	*  https://screenrant.com/snapchat-down-app-slow-response-messages-not-sent-issues/
*  Tweetdeck  Twitter 客户的工具服务发生故障。
	*  https://www.independent.co.uk/life-style/gadgets-and-tech/news/tweetdeck-down-twitter-not-working-loading-a9633636.html
*  GGPoker  在 World Series of Poker (WSOP) 世界扑克大赛赛事期间发生一些列问题.
	*  https://portswigger.net/daily-swig/online-poker-operator-hit-by-ddos-attack-on-opening-day-of-wsop-event
*  Fastly (control plane) Full disclosure: Fastly is my employer.
	*  https://status.fastly.com/incidents/7q2psqf255wl
*  Squarespace  这一周非常痛苦，在July 21 事故后发生的相关事件：
		* July 21  https://status.squarespace.com/incidents/hh3p432jcq03
		* July 22 (包含事件详细分析) https://status.squarespace.com/incidents/3cgg1171wyvz
		* July 24 https://status.squarespace.com/incidents/x63nssl9kzvm
		* July 24 https://status.squarespace.com/incidents/v6ql728f1f4d
*  Google Cloud Platform 几个谷歌云平台组件受到影响，包括 7 层负载均衡器。
	*  https://status.cloud.google.com/incident/zall/20006

## 工具

https://github.com/flant/shell-operator
Shell-operator是一个在Kubernetes集群中运行事件驱动脚本的工具。

https://github.com/Fizzadar/pyinfra
pyinfra在大规模的基础架构中实现了超快的自动化。它可以用于临时命令执行、服务部署、配置管理等。
#python #配置管理

https://github.com/alerta/alerta
Alerta 监测系统

https://github.com/GoogleCloudPlatform/terraformer
CLI工具可以从现有的基础设施中生成terraform文件（反向Terraform）。
#基础设施即代码

https://github.com/visenger/awesome-mlops
MLOps的精选参考资料清单。
#github

https://github.com/cycloidio/inframap
读取你的tfstate或HCL，为每个提供者生成一个特定的图表，只显示最重要/相关的资源。
#terraform

https://github.com/Hack-with-Github/Awesome-Hacking
一个为黑客、Pentesters和安全研究人员提供的各种令人敬畏的列表的集合。
#github #安全

https://github.com/box/kube-iptables-tailer
kube-iptables-tailer做的正是你所期望的。它将底层的iptables数据暴露给kubectl，方便发现服务在Kubernetes中互相通信的尝试和失败。

https://github.com/Stono/kconmon
Kconmon是一个Kubernetes连通性监控工具，它可以运行频繁的测试（tcp、udp和dns），并公开Prometheus指标，这些指标富含节点名称，以及位置信息（如区域），使您能够关联可用性区域或节点之间的问题。



