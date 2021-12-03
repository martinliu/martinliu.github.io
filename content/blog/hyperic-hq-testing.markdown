---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-05-30T04:28:00Z
slug: hyperic-hq-testing
tags:
  - Hyperic HQ
title: Hyperic HQ小测手记
url: /2007/05/30/hyperic-hq-testing/
wordpress_id: 49157
---

[![](http://bp2.blogger.com/_KU0istEHv9w/Rlz-qwD97uI/AAAAAAAAADk/j3tVzwajvC4/s320/logo.JPG)](http://bp2.blogger.com/_KU0istEHv9w/Rlz-qwD97uI/AAAAAAAAADk/j3tVzwajvC4/s1600-h/logo.JPG)<br />HQ 的网站是一个显的非常商业化的网站；看上去制作的比较精良也比较专业。从 HQ 的官方文档（好像没找到 pdf 手册）中看出它能监控的东西还真的非常多，无论是商业的软件还是开源的都有一大串的 matrix；他们在被监控的及其上是需要安装和运行代理的。所以从这一点上讲和商业软件也没有什么区别，总之看的数据多应该比较好，不过数据收集的多有时候会给监控对象代理太重的 workload。<br /><br />如何安装<br />下载 HQ\hyperic-hq-installer-3.0.4-389-x86-linux 从 HQ 的网站。这个压缩文件包含：安装程序，服务器端程序（好像包括一个内嵌的 PostgreSQL 数据库），代理程序，服务期端 shell 程序，JRE。<br />BTW:服务器端和代理都是 Java 程序，如果自己配置好 JRE 的话可以下载不包含 JRE 的安装包。Windows 上的代理包是一个 zip 文件，为了方便我都下载的含有 JRE 的安装包。<br /><br />由于是纯 Java 的应用所以服务器端和代理端看似好像都没有任何依赖性要求，只是需要在服务器端安装 xorg-x11-libs 包，否则不能正常绘图，看不到图形。<br />在 Linux 下的安装过程大致如下。<br />mkdir /opt/hq<br />useradd hq -G root -d /opt/hq<br />su hq<br />tar zxvf hq.tgz<br />cd hyperic-hq-installer/<br />./setup.sh<br />/opt/hq/server-3.0.4/bin/hq-server.sh start<br />注意最好建立一个新的用户为 HQ，服务期端本身需要被非 root 用户安装和启动。另外代理和服务器端都需要特殊的两个端口通信，所以安装完之后必须停止或者配置防火墙；否则不能访问服务器，服务器也不能和代理通信。启动代理之前需要配置好防火墙。<br /><br />试用：<br />总体说 HQ 的安装和配置都是非常简单的，不过他的 Web 界面更是简洁。当代理启动了之后，会自动出现在 Auto-Discovery 下面，点击 Add Resource 按钮将它变成一个正式的监控对象。默认的情况下，代理会收集一定数量的监控指标；大概是可收集数量的 20%左右。当在某个监控对象上（例如 Memory Used）设置了收集间隔之后，服务器端就开始了定时的数据收集，所收集的数据默认情况下用折线图的形式展示。可以根据某个指标建立一个告警，告警的逻辑也相当的完整：逻辑判断，巅峰判断，升级处理；看似能想到的都有了。由于是第一次使用展示没有看的如何建立一个告警规则应用于所有监控对象的。我用 HQ 对我的一个服务器（iis,MS Sql,.net）做了监控，从数据收集和展现效果上来说，真的堪称可与商业软件媲美。<br /><br />使用结论：<br />安装简单方便，在 Linux 下代理端完全无需关照包依赖性。代理配置的安装配置需要一定量的工作，必须配置服务器地址，通信端口等。<br />代理程序对服务器的工作负担还是比较大的，特别是在启动的那几分钟内。代理进程对 CPU 的使用率可以达到 50 ～ 80%，之后就比较低了。对内存的利用一般是 30MB 左右，当然这应该是可以通过降低收集数的数量和频率来降低的。<br />用户界面的使用还真的是很方便，还支持告警信息的 RSS 访问。总之 HQ 是一个开源软件中的重量级选手：功能强，复杂性高，代理程序负担较重。其他使用小结，待续。
