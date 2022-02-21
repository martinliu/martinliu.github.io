---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-12-23T12:20:00Z
slug: opennms-path-outage
tags:
  - opensource
  - Path Outage
title: 如何配置OpenNMS中的 Path outage －路径失效
url: /2007/12/23/opennms-path-outage/
wordpress_id: 49176
---

这个功能是是 1.3.2 之后加入的。它解决的问题是：当 OpenNMS 系统和被监控节点之间的网络路径失效了，或者网络链路 down 了，那么 OpenNMS 就需要抑制发送这个节点的告警。例如，如果一个广域网链路 down 了，所有由这个链路连接的远程站点的所有节点就都看起来 down 了。因为你将会得到一个路由器上远端链路无响应的告警，而不需要得到在这个路由器后所有节点 Down 的告警。如果当一个远程节点不响应了，OpenNMS 会测试一下那个远程路由器广域网接口的 ip，通过对这个 ip 的测试 OpenNMS 觉得是否该发出此节点 Down 的告警。OpenNMS 测试的这个节点叫做此节点的 Critical Path IP Address（关键路径 Ip 地址）。<br /><br />给一个节点配置 Path Outage<br />在 OpenNMS 的节点配置上，点击 Admin, 点击 Configure Path Outage，输入对于这个节点来说关键的 ip 地址。点击 Submit 按钮。<br /><br />配置基于规则的 Path outage<br />可以为一组节点配置一个规则。在总导航条上选中 Admin，Configure Notifications，点击 Configure Path Outages，在 Define the Critical Path 下面输入一个 Ip 地址，例如：192.168.0.1（这种格式）；在 Current Rule 下面输入地址范围，例如：IPADDR IPLIKE 192.168.0.\*；可以选中 Show matching node list 后的 box，点击 Validate Rule Results 连接；在下面的页面可以查询到受那个关键 Ip 地址所影响的所有节点；最后点击 Finish 按钮完成配置。<br /><br />查看 Path Outage<br />在总导航条上选中 Path Outages，在页面中你可以看到你配置的所有 Path Outages 的规则。<br />这个文章基本上翻译的是[http://www.opennms.org/index.php/Path_Outage_How-To](http://www.opennms.org/index.php/Path_Outage_How-To) 只是觉得这是个不错的功能，所以就大概翻译了一下，希望对感兴趣的朋友们有帮助。由于手头硬件环境的限制，我还没有真实测试过这个功能，如果您对此功能做了什么测试的话，也欢迎和我交流，请留言或者或发邮件给我。
