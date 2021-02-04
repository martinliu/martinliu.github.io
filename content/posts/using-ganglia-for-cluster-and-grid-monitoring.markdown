---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-04-16T09:41:06Z
slug: using-ganglia-for-cluster-and-grid-monitoring
tags:
- cluster
- Ganglia
- grid
title: Using Ganglia for cluster and grid monitoring
url: /2008/04/16/using-ganglia-for-cluster-and-grid-monitoring/
wordpress_id: 49198
---

[![](http://www.nowmicro.com/NM_Images/hpc-ganglia-logo.jpg)](http://ganglia.info/) Ganglia是一个用来监控群集和网格计算环境的软件。它是可以扩展的分布式监控系统，它基于多播协议，数据存储和传输的格式都是基于开源的标准：XML/XDR/RRDTool/APR/Apache/php等。

应用Ganglia的几个理由：

  * 在一个点上监控包含很多服务器的群集，单个cluster内服务器的数量比较多，需要从整体看某个cluster的可用性和性能，也要能看到单独某个机器的运行情况。
  * 监控分布式的cluster环境，例如跨网段和地域的灾备的环境。
  * 需要监控系统能分N级的查看方式，以银行为例：北数据中心-->网络银行业务-->个人网银系统-->web server 群集--> WebSvr001；可以按业务逻辑和系统架构逻辑。
  * 需要7*24*365的监控整个系统，能得到可用性、性能和容量等方面的报表。

应用Ganglia的几个好处：

  * 监控能力的无限扩展，被管理服务器数量达数千个甚至根多。
  * 纯web前端，apache和php的应用页面方便定制
  * 强壮的系统结构，并且具备可以任意扩展采集数据KPI的特点
  * 适合高性能计算或者网格计算环境。

Ganglia应用需要注意的方面：

  * 在每一个节点上需要部署一个代理程序，考虑到对代理配置的变更的工作量，在部署代理之前，需要彻底的分析需求，尽量减少部署过程中配置变更带来的多于调试的工作量。
  * 部署后期的变更工作，如果比较频繁的话将导致后台维护工作量增大，可以考虑使用一些开源的软件分发和自动化配置管理的工具。这些配置的初始化工作可以与OS的安装部署工作一起考虑。

它被很多大学和专业机构研究并使用，所以有非常多的专业文档可以参考，哪行文档多分析了Ganglia的系统架构和特点，多系统的原理介绍的非常细致。下面是我收集的几个关于这个软件的文档请参考。并且在它们的网站上也可以看到很多相关的资源连接，都是非常好的实施方面的详细文档。

If you need more detail please take look those documents below.
