+++
date = 2021-03-16T19:23:15+08:00
title = "DevOps 教练周刊 #7 | 全球 DevOps + SRE 精选资讯"
description = "为 DevOps 教练 之成长，提供必备的滋养，定期为你整理最值得了解的新闻、文章、工具和宕机事故分析"
author = "Martin Liu - 刘征"
categories = ["DevOps"]
tags = ["周刊"]
image = "images/weeklyupdate.jpg"
+++

本期有 6 个公司的服务出现了宕机事故，一如既往的为你精选了十几篇值得学习的内容。

<!--more--> 

> [EN] May your queries flow and your pagers stay silent. 
> --Dave, Betsy, Niall, Stephen, and Ken

【译】：愿你的咨询队列和传呼机都保持静默。

## 宕机



## Fastly 3 月事故一览

Fastly是一家 CDN 服务提供商，每个月的事故披露条数大约是 20 到 30 条。本月（三月）已经可以在 https://status.fastly.com/history 看到 23 条事故披露通告。主要内容有三种：事故时间线记录，事故回顾和计划内活动（扩容等）。



回顾三月份的事故历史，事故类型组要是：

* 区域性和全球性的性能事故。
* 网络路由和 DNS 故障
* 数据中心计划内的维护、扩容和新上线（新加坡）。



目前一共有 8 个事故回顾。浏览一下大致内容主要是对过去发生过的事故的确认。每一条事故回顾中精确的描述了事故影响起始时间点和影响范围。



> 教练观点：看起来他们三月份的日子过的不咋样，不知道这个月的错误预算是否快烧完了。



## OVH Cloud 数据中心发生火灾

这是一家服务器托管/云服务器提供商，数据中心主要在欧洲中西部和美国东岸。

3 月 10 日这次发生火灾的是位于法国Strasbourg的一个数据中心，该数据中心园区里有 4 栋大楼。从新闻图片上看到有一栋大楼几乎彻底烧毁。



![2021-03-21_23-05-14](https://elasticstack-1300734579.cos.ap-nanjing.myqcloud.com/2021-03-21-151636.png)



该公司的创始人/CEO 第一时间在 Twitter 上发布和更新着火灾的状态。

![2021-03-21_23-06-03](https://elasticstack-1300734579.cos.ap-nanjing.myqcloud.com/2021-03-21-151729.png)

从这可以看到，数据中心园区中的 SBG2 大楼发生火灾，因此直接关闭里其它的大楼。他每天在 Twitter 上更新一次，在公司官网上 https://www.ovh.com/world/news/press/cpl1787.fire-our-strasbourg-site?124 也可以看到每天一次的更新。

至今火灾的原因还没有说明，从每日的更新里还可以看到，火灾的影响目前没有完全消除，其它数据中心的电池还有冒烟的情况出现。

火灾恢复的过程包括：

* 对每个大楼的可用状态更新，SBG-3 大楼已经恢复到了 40%可用的状态，团队工作在重启服务器的过程中。
* 其它三个大楼在逐一恢复抢修中，主要包括这些工作：重启电源供应，重启网络服务，重启服务器。

可以看到他们的救灾工作的三个优先级：

1. 恢复各个大楼的服务。
2. 在其他数据中心为客户制备新的服务器（承诺了1.5 万台新服务器）
3. 与所有受到影响的客户一起实施 DRP 计划。（灾难恢复计划）

以上三项救灾工作的数据都是日更在以上的网页中。



> 教练观点：这个数据中心可谓是非常罕见的大规模灾难，救灾速度和进展还是比较缓慢的，但愿受影响的公司都有自己的扩域高可用容灾方案，希望 DRP 计划执行的顺利有效。



## 俄罗斯发生大规模域名解析故障

在 3 月10日，由于俄罗斯的网监局（[roscomnadzor](https://twitter.com/roscomnadzor) 联邦通信、信息技术和大众媒体监督局）对Twitter 的短域名服务 t[.]co 不当屏蔽，导致了全境所有包含了 t.co 的子域名都无法访问，包括例如：Microsoft[.]com 和 Reddit[.]com 的域名，还有很多其它躺枪的域名。

参考Twitter 上的信息如下：

![2021-03-21_23-38-50](https://elasticstack-1300734579.cos.ap-nanjing.myqcloud.com/2021-03-21-153938.png)

>教练观点：感觉这个错误犯的有点低级了。



## Dyn DNS 服务器故障

这是 Oracle 云的提供的 DNS 服务，本次故障导致大部分客户的 DNS 服务解析失败或者降级，影响范围是所有相关客户。

调查得到的主要根因：Oracle Public DNS 基础设施实施配置变更是发生了问题。



## Chef 服务发生大量 5xx 错误

Chef 的服务不经常发生故障，这次 api.chef.io 服务发生了大量 5xx 错误增多的事故，错误的对象是索引集群。目前故障已经排除，服务恢复了正常。



## GitHub 3 月事故

https://www.githubstatus.com/history 在这个页面上可以看到本月已经发生了 7 次事故。在 3 个严重事故中，有 2 个的事故影响时间接近 2 小时。3-15 日的事故影响了 GitHub Actions 服务。12 日的事故中影响到了绝大多数服务的可用性，但是恢复的还比较快。



> 教练观点：我本月体验到了一次 GitHub Actions 构建报错挂住僵死的问题，后来继续提交，GitHub Actions 的 pipeline 又恢复正常工作了。持续时间不太长。

# 新闻

* [Take the 2021 State of DevOps Survey, be part of our 10-year history](https://puppet.com/blog/take-the-2021-state-of-devops-survey-be-part-of-our-10-year-history/) 这是我跟踪最长时间的 DevOps 状态调查报告，以前是和 DORA 合作的，在 DORA 被 Google Cloud 收编了以后，Puppet 有开始找的其它大拿继续这个调查。对于计划做行业调查的朋友，还是可以学习一下，这套问卷的设问。

* [CD Foundation Announces Industry Initiative to Standardize Events from CI/CD Systems](https://kubernetes.us10.list-manage.com/track/click?u=3885586f8f1175194017967d6&id=5a32cff75d&e=7098f23071) 持续交付基金会发生了，宣布行业级 CI/CD 系统的标准化事件的号召。他们搞了一个  [Events SIG](https://github.com/cdfoundation/sig-events) 厂商中立的兴趣讨论小组，这个计划对以后所有 CI/CD 流水线系统间的互操作性比较重要。

  

## 软件发布

* Java 16 发布
* AWS EC2 发布了新的 X2gd 实例，这是一块 ARM-based Graviton2-powered 高内存实例。可达 1TB 内存和 3.8TB 的SSD 存储。
* Git 2.31 发布
* Ghost 4.0 开源 CMS 系统
* Audacity 3.0.0 开源音频编辑软件
* SQLite 3.35 发布



# 文章

本周推荐如下经常文章。

* [战斗机飞行员和事故管理有什么共同点？](https://www.transposit.com/blog/fighter-pilots-and-incident-management/)
  我觉得战斗机飞行员对每一次任务，无论成功与否，都会有一个回顾，这真的很新鲜。总有一些东西需要学习。杰西卡-阿贝尔森--Transposit

* [Heroku的事故响应](https://blog.heroku.com/incident-response-at-heroku-2020)
  Heroku应用事故管理系统，指定一名事故指挥官，负责保持事故的正常进行，并监督外部和内部的沟通。Guillaume Winter - Heroku

* [可汗学院如何在一周内成功处理2.5倍的流量？](https://blog.khanacademy.org/how-khan-academy-successfully-handled-2-5x-traffic-in-a-week/)
  这个故事正在变得很常见：当大范围居家办公开始时，可汗学员的流量突然暴增。他们的策略包括使用云和CDN。Marta Kosarchyn - 可汗学院

* [根基：确保站点可靠性](https://engineering.squarespace.com/blog/2017/under-the-hood-ensuring-site-reliability)
  下面是对Squarespace如何做SRE的精彩总结。Franklin Angulo - Squarespace

* [[增量：可靠性] 大规模的可靠性。](https://increment.com/reliability/reliability-at-scale/)
  Deliveroo、DigitalOcean、Fastly和Headspace的领导们分享了他们的组织是如何看待可靠性和弹性的，以及他们对开始可靠性之旅的工程机构的建议。每位领导都回答了一系列关于他们的组织如何处理可靠性的问题，给出了一个有趣的比较和对比的概述。

* [「增量：可靠性案例分析」弹性作为Freshworks的适应性](https://increment.com/reliability/resilience-as-adaptability-freshworks/)
  利用在一场毁灭性的飓风之后制定的灾难计划，Freshworks在这场大流行中幸存下来，并在大流行前的最后期限前交付了一个重要的新产品。伊普西塔-阿加瓦尔--增量公司

* [什么是金丝雀部署？](https://launchdarkly.com/blog/what-is-a-canary-deployment/)
  本篇解释了什么是金丝雀部署，它如何帮助您，以及金丝雀部署与蓝/绿部署的区别。LaunchDarkly

* [如何以成长的心态打造SRE团队？](https://www.blameless.com/blog/how-to-build-an-sre-team-with-a-growth-mindset)
  这篇文章解释了成长型思维方式的含义，并展示了它如何应用于SRE。艾米丽-阿诺特--Blameless





