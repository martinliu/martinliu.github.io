---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-12-21T07:14:00Z
slug: opennms-strafeping
tags:
  - opensource
  - StrafePing
title: 如何使用OpenNMS中的StrafePing功能
url: /2007/12/21/opennms-strafeping/
wordpress_id: 49175
---

自从 1.3.7 之后 OpenNMS 加入了 Smokeping 功能，取名为 StrafePing。从此 OpenNMS 也成了 Smokeping 的银牌赞助商。

<br />

**_安装：_**

<br />

StafePing 做为一个 Poller 默认被安装在 1.3.7 后的软件中，不需要单独安装和配置。

<br />

**_配置：_**

<br />

没有单独的配置文件，相关的配置信息需要修改文件： poller-configuration.xml 中的相关部分。需要在 标记中加入需要使用的 Ip 地址范围。启用之后 StrafePing 做为一个被监控的服务显示在这个节点上。

<br />

默认安装 OpenNMS 并不使用这个服务，是为了减小网络流量；推荐根据 OpenNMS 硬件的能力只对部分节点做这种监控。

<br />

**_使用：_**

<br />

需要产品 StrafePing 的图形有两种方式。1）在 OpenNMS 首页上，点击右侧的 Resources Graphs，选中产看的机器，在 Response Time 下面的列表中选中需要产看的 Ip 地址，点击 Submit，即可产看到图形。2）在节点产看页面，选中 Resources Graphs，在 Response Time 下面的列表中选中需要产看的 Ip 地址，点击 Submit，即可产看到图形。

<br />

**如何想看懂 StafePing\*\***的图\*\*

<br />

请参考我以前的 blog [http://lzheng.blogspot.com/2007/02/smokeping-rttround-trip-time-tcp-tcp.html](http://lzheng.blogspot.com/2007/02/smokeping-rttround-trip-time-tcp-tcp.html)

<br />

参考 Smokeping 的网站[http://oss.oetiker.ch/smokeping/doc/reading.en.html](http://oss.oetiker.ch/smokeping/doc/reading.en.html)
