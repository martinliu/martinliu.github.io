---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-06-15T15:50:31Z
slug: monitoring-temperature-and-fan-speed-using-ganglia
tags:
- Ganglia
title: 盛夏严防服务器中暑
url: /2008/06/15/monitoring-temperature-and-fan-speed-using-ganglia/
wordpress_id: 49213
---

![](http://www.hlj.xinhuanet.com/xw/2007-03/24/xin_190304241641921962117.jpg)哦不是中暑:-)而是发烧；夏天就要到了，监控服务器的主板温度和风扇是否工作正常有变的比较重要起来了。<br /><br />今天发现一个文档 [Monitoring Temperature and Fan Speed Using Ganglia and Winbond Chips](http://www.slac.stanford.edu/gen/edu/suli2006/finaltalks_thurs/caitie.ppt) 这个是一个不错的文档，值得参考一下。<br /><br />文章是写如何在Ganglia中实现对主板温度和风扇的监控。以前也有人问过我这个问题“Ganglia的监控图上为什么没有温度也风扇的图”；相信您看后就知道怎么回事了。<br /><br />下面是我对关于温度和风扇监控的一点想法：<br />

<br />	
  * 主板的芯片能提供这些数据的访问给操作系统
<br />	
  * 操作系统上有sensors这个命令工具用来采集这些数据
<br />	
  * 有合适的脚本分析上面命令的输出数据转换成能被监控工具（ganglia， cacti，nagios， opennms）采集的格式等
<br />	
  * 往往这两个参数并不是监控工具的默认采集数据，所以需要扩展采集工具的采集集合，收集并保存这些数据。
<br />	
  * 在监控工具如Ganglia中显示这些数据，当然如果有自动报警功能就好了，可以及时通知管理员给服务器消暑：）
<br /><br />Ganglia是最好的网格或者群集的监控软件，不过当你用它的使用也要注意到下面这个问题：<br /><br />What does Ganglia not provide?<br />Ganglia does not attempt to address service monitoring or reporting (unlike Nagios). So far, we have not come across a single monitoring solution that addresses all of our needs effectively.<br /><br />上面所说的服务监控是说，它的特点不是想Nagios和OpenNMS那样对服务器系统做非常全面细致的监控，它默认的监控指标比较少不过对于监控网格或者群集这种数量巨大的对象来说这些比较经典的指标也够用了，特别是对服务器的可用性，CUP、RAM，网络资源利用率和工作负载等数据的采集也比较够用了。如果你使用它来监控数量不是很多服务器的话，你可以使用它的可扩展性加入任何想监控的KPI。我最喜欢的还是它能把服务做分组，而且垂直的方向上可以加N层的嵌套；这种组织方式能比较好的适用于业务系统众多而复杂的数据中心。
