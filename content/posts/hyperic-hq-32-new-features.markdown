---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-02-02T06:02:00Z
slug: hyperic-hq-32-new-features
tags:
- Hyperic HQ
- new features
- NSM
title: Hyperic HQ 3.2 new features
url: /2008/02/02/hyperic-hq-32-new-features/
wordpress_id: 49183
---

If you'd like to check out release note, please click here. [http://support.hyperic.com/confluence/display/DOC/HQ+3.2+Release+Notes](http://support.hyperic.com/confluence/display/DOC/HQ+3.2+Release+Notes)<br /><br />I had a quick install on RHEL 5. For some features what I saw, I took some screenshots as bellowing. I hope this helps you to understand what's new in 3.2 and save a little bit time for you if you do not wants to install it. I will describe in Chinese.<br />

## New Nav menu 新导航菜单

<br />![](http://lh5.google.com/liuzh66/R6QKZn2WokI/AAAAAAAAAeo/ZYObo0rO5Dc/image%5B15%5D.png)导航菜单的名称变成了：Dashboard -- Resources -- Analyze -- Administration 菜单的风格稍微有一点变化。Analyze下面可以进入Alert Center去查看报警信息。我觉得3.2毕竟是一个小的功能增进板，添加了支持MY SQL的支持。增强了对Nagios的集成。对Nagios的集成对它还是很有好处的，由于它自己是Agent Based的监控方法，而Nagios是Agentless的监控方法；集成之后通过它的web界面能统一管理，还是挺好的。不过和Nagios具体能集成到什么程度，我还没有试过。<br />

## Currently Down Resources当前宕机资源

<br />![](http://lh4.google.com/liuzh66/R6QK9X2WomI/AAAAAAAAAe4/iGNp8zHxnok/image%5B19%5D.png)<br />如果所示：各种有问题的资源安装各种分类都显示出来，同实现时什么时间出的问题，持续了多久，点击放大镜后查看相关的报警信息。上图显示的是：HQ Agent在w2k3vm这一Windows服务器上没有启动的情况，它报告了包括hq agent自身以及所有相关资源的都宕机的情形。同时作为一个监控系统来说，管理员最需要看到的信息可能主要包括两种：1）有那些资源出了问题；2）当前有什么样的告警事件。这里对这两类信息提供了一个非常不错的访问入口。<br />

## Live Exec Data实时数据获取

<br />![](http://lh6.google.com/liuzh66/R6QLY32WooI/AAAAAAAAAfI/JDuTMobC7IE/image%5B24%5D.png)<br />HQ-agent本身只能周期性的采集matrix，在汇报给管理服务器。实时的数据采集对排错还是非常有帮助的。此功能我觉得是3.2版中的最好的增强。它应该是远程的让agent去执行一下命令在把最终结果返回到页面上：<br />

<br />	
  * Cpuinfo  CPU信息
<br />	
  * Cpuperc  CPU利用率
<br />	
  * Df            磁盘利用率
<br />	
  * Ifconfig   网卡ip信息
<br />	
  * Netstat   网络端口信息
<br />	
  * Top
<br />	
  * Who
<br /><br />这些信息的获取通过agent完成所以和平台无关，即使是Window平台也能收到相同的信息。<br />

## HQ Health Check 管理服务器自身检查

<br />![](http://lh4.google.com/liuzh66/R6QLxX2WoqI/AAAAAAAAAfY/_qW9Xr0ni6w/image%5B28%5D.png)<br />一个真正的自监控功能最好能做到对相关指标的报警处理。能设置一些条件，在不正常情况发生的时候报告管理员说出管理服务器那里有问题了。上图可以看出，hq已经做出了第一步，能采集并且显示很多HQ服务器运行的状态信息。<br />

## Summary：

<br />在3.2的发布说明中还提到它自身的扩展性也很大的增强，这一点对hq来说尤为重要。由于它的结构是基于代理的，当监控的设备和资源都非常多时，hq管理服务器自身的处理能理将会成为瓶颈，如果它的处理，存储和网络上的任何一个环节出现了问题，整个监控系统就失效了。由于事件有限，目前还留下了一些问题：<br />

<br />	
  * Global Alert Disable是在那里设置的？
<br />	
  * 报警阀值的设置是否有全局设置的地方？（例如：对所有windows机器都设置一个CPU>80％的阀值）
<br /><br />如果您对以上两个问题有些答案请回复告诉我。关于HQ的其它文章，清在本blog中搜索。
