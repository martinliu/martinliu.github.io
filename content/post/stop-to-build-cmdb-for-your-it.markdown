---
author: Martin Liu
categories:
  - ITSM
comments: true
date: 2009-03-01T13:40:16Z
slug: stop-to-build-cmdb-for-your-it
tags:
  - cmdb
title: Stop to build CMDB for your IT - CMS是怎样炼成的？
url: /2009/03/01/stop-to-build-cmdb-for-your-it/
wordpress_id: 49256
---

ITIL 在国内的实施也有 8 年之久，就我看过和做过的项目中：service desk 是最多实施的工具，它包括 IM/PM；还有 Change Management；用户们还可能会常常认为，Release Management 可以和变更流程可以混在一起搞。服务台一般先上，有的变更流程先上，服务台的共同特点还有 PM 一般形同虚设。就我所见所闻的项目和用户来说，CMDB 没有那家能建的好用的好；CMDB 的建设的缺失似乎成了所有 ITIL 用户的通病，应该也是想重点突破的瓶颈。<br /><br />ITIL v3 发布后，CMDB 成了 CMS 中的一个数据库；而且，CMS 中包括不止像 CMDB 这样的配置信息数据库，其实任何保存配置信息的数据库都算在 CMS 系统内。既然是一个系统，所以它就不光包含数据还包含一套配套工具集合，通过这套工具，维护和使用配置信息。CMS 为其他所有 ITIL 流程提供基础的配置信息。它的结构如下图所示：<br /><br />[caption id="attachment_435" align="alignnone" width="658" caption="配置管理系统"]![配置管理系统](http://www.martinliu.cn/wp-content/uploads/2009/03/cms.jpg)[/caption]<br /><br />如果说上面这幅图比较还是比较抽象的话，那么请见下图：<br /><br />[caption id="attachment_436" align="alignnone" width="714" caption="CMS is a set of tools based on all configuration data"]![bmc-atrium1](http://www.martinliu.cn/wp-content/uploads/2009/03/bmc-atrium1.jpg)<br />[/caption]<br /><br />从上图中我们看到，CMS 系统一共可以分为四层。上三层是核心 CMDB 数据库和相关配套工具，最低层 Data 层则是是所有配置信息的基础来源。从 ITIL v3 的角度来说，只建设一个集中的 CMDB 数据库来存储所有的 CI 信息是不够的，CMS 系统中必须能够包含和处理所有企业已有的各个系统中的配置数据。换言之，CMDB 建设的局限性在于，它只是配置信息数据化，或者说电子化的第一步。<br /><br />当前依然有很多企业雄心勃勃的上马 CMDB 项目，不过切记在规划时，一定先好好阅读一下 ITIL v3 中和 CMS 相关的内容，适当调整项目的目标和预期总是好的，也可以规避一些项目风险。<br />

<blockquote>CMDB不只是一个数据库那么简单，更不可能在服务台的数据库中建立几张表就可以搞定。从企业IT管理的全局出发，按照ITIL v3的规范，建设CMS应该是所有ITIL项目的当务之急。CMS系统决不能遗忘过去，必须有效整个现有的各个配置信息数据源，无论其以何种形式存在。它必须是一个开放的平台，能过最大限度的和其他任何配置信息的消费者（ITIL流程，以及任何需要获取配置信息的任何应用）整合，</blockquote>

<br />以上的一些是我对 CMS 建设的一些认识。如果要落地到项目上还不许经过一个痛苦的过程，那就是产品选型。选项的过程中可以注重一下几点：<br />

<br />	
  * 可视化：配置项和之间的关系按拓扑形式展现
<br />	
  * 标准化：软件、硬件配置项都有完整标准的CTI信息
<br />	
  * 归一化：与现有各种配置管理系统核心共存同时CMS保持一份完整的户口记录，任何CI都有ID
<br />	
  * 集成化：CMS中的数据以图形或者裸数据等形式供其他相关消费者流程或者人员使用
<br />	
  * 联邦化：CMS核心数据库中不保存动态变化的配置信息（DB的最大连接数，网络设备所使用的syslog服务器地址），这些信息通过联邦管理让用户从其他相关的工具系统中查看到最新的数据。
<br /><br />最近可能还会接触一下CMDB的项目，其他经验总结待续。
