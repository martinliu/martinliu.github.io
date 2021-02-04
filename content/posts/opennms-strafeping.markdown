---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-12-21T07:14:00Z
slug: opennms-strafeping
tags:
- OpenNMS
- StrafePing
title: 如何使用OpenNMS中的StrafePing功能
url: /2007/12/21/opennms-strafeping/
wordpress_id: 49175
---

自从1.3.7之后OpenNMS加入了Smokeping功能，取名为StrafePing。从此OpenNMS也成了Smokeping的银牌赞助商。

<br />

**_安装：_**

<br />

StafePing做为一个Poller默认被安装在1.3.7后的软件中，不需要单独安装和配置。

<br />

**_配置：_**

<br />

没有单独的配置文件，相关的配置信息需要修改文件： poller-configuration.xml中的相关部分。需要在 标记中加入需要使用的Ip地址范围。启用之后StrafePing做为一个被监控的服务显示在这个节点上。

<br />

默认安装OpenNMS并不使用这个服务，是为了减小网络流量；推荐根据OpenNMS硬件的能力只对部分节点做这种监控。

<br />

**_使用：_**

<br />

需要产品StrafePing的图形有两种方式。1）在OpenNMS首页上，点击右侧的Resources Graphs，选中产看的机器，在Response Time下面的列表中选中需要产看的Ip地址，点击Submit，即可产看到图形。2）在节点产看页面，选中Resources Graphs，在Response Time下面的列表中选中需要产看的Ip地址，点击Submit，即可产看到图形。

<br />

**如何想看懂StafePing****的图**

<br />

请参考我以前的blog [http://lzheng.blogspot.com/2007/02/smokeping-rttround-trip-time-tcp-tcp.html](http://lzheng.blogspot.com/2007/02/smokeping-rttround-trip-time-tcp-tcp.html)

<br />

参考Smokeping的网站[http://oss.oetiker.ch/smokeping/doc/reading.en.html](http://oss.oetiker.ch/smokeping/doc/reading.en.html)
