---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-05-08T04:35:00Z
slug: opennms-faqs
tags:
- faq
- OpenNMS
title: OpenNMS常问问题All-in-One
url: /2007/05/08/opennms-faqs/
wordpress_id: 49152
---

**问：OpenNMS是什么？<br />**答： OpenNMS是第一个开发在开源模式下的企业级网络管理平台应用。OpenNMS的目标是成为一个真真的分布式、可升级的网络管理平台，尽管它看似一个 FCAPS网络管理模型，使之可用于开放源码和商业领域。目前：OpenNMS专注与以下三个方面：服务轮询 － 检查应用服务的可用性，产生可用性报表。数据收集 － 收集、保存和报表网络信息数据，并设定和触发门限值。事件和提示管理 － 接受事件系统内部的和外部的事件，将源事件提供给强大的故障告警和故障升级系统。OpenNMS Group是开发和支持OpenNMS应用的一个商业性的实体。<br /><br />**问：为什么要开源？**<br />答： 我们坚信真真的创新不会来自规模巨大的企业。我们还相信网络管理软件领域比Linux操作系统更适合开源模式。不像Linux，网络管理要去监视和控制来 自不同厂商的很多的技术。考虑到每年都有很多新的网络设备面世。商业软件公司并不希望追赶这种更新产品的工作负荷，相反它们只能依赖与它们的通用管理技术 （最小化的通用性）。相反，对于一个开源项目中的每一个人－－厂商、用户或者技术顾问－－都能对项目做出自己的共享，从而保障了这个项目成功的几率。<br /><br />**问：OpenNMS是用什么语言写的？<br />**答： OpenNMS主要是用Java语言写的。OpenNMS2.0的目标是：让它成为一个以一堆.jar文件形式来安装的产品。还有一些非Java的部分： icmpd-Java1.4 API不能理解ICMP。因为ICMP回答请求（ping）是一个最简单的来测试基于Ip的网络设备是否可以服务的方法，没有那个网络管理应用程序不用的 它的。将ICMP功能分离为一个独立的守护进程的目标是，如果系统中有ICMP的功能那么OpenNMS就用，如果没有OpenNMS就率略它。 OpenNMS不需要ICMP来监控网络设备。数据库－OpenNMS现在使用PostgreSQL作为它的地层数据库，PostgreSQL 是用C写 的。OpenNMS2.0会使用几个能通过Hibernate适配器访问到的数据库。rrdtool－OpenNMS当前的版本实时的选择使用 RRDtool或jRobin（Java会使用RRDtool）。最终这个选项的默认使用jRobin，也可以选择使用RRDtool。<br /><br />**问：OpenNMS有图形的显示么？<br />**答： 这可能是一个对于OpenNMS新人来说最常问的问题：OpenNMS的图形监控界面在那？简单的问答是我们没有一个这样的地图，如果你想听听我们的解释 请继续往下看。OpenNMS是被一些经验丰富的网络管理技术顾问开发出来的。HP的Openvew NNM是一个很流行的商业软件，它能生产一个可定制化的网络监控图形。OpenNMS Screenshot<br /><br /><br /><br />

<br /><table style="width: 194px" ><br /><tr ><br />
<td style="height: 194px" align="center" >[![](http://lh4.google.com/image/liuzh66/Rl19YgD97vE/AAAAAAAAAE8/hFVbteNWiR0/s160-c/OpenNMS.jpg)](http://picasaweb.google.com/liuzh66/OpenNMS)
</td><br /></tr><br /><tr ><br />
<td style="text-align: center;font-family: arial,sans-serif;font-size: 11px" >[OpenNMS](http://picasaweb.google.com/liuzh66/OpenNMS)
</td><br /></tr><br /></table><br />**原文地址** [http://www.opennms.org/index.php/FAQ-About](http://www.opennms.org/index.php/FAQ-About)
