---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-12-23T12:20:00Z
slug: opennms-path-outage
tags:
- OpenNMS
- Path Outage
title: 如何配置OpenNMS中的 Path outage －路径失效
url: /2007/12/23/opennms-path-outage/
wordpress_id: 49176
---

这个功能是是1.3.2之后加入的。它解决的问题是：当OpenNMS系统和被监控节点之间的网络路径失效了，或者网络链路down了，那么OpenNMS就需要抑制发送这个节点的告警。例如，如果一个广域网链路down了，所有由这个链路连接的远程站点的所有节点就都看起来down了。因为你将会得到一个路由器上远端链路无响应的告警，而不需要得到在这个路由器后所有节点Down的告警。如果当一个远程节点不响应了，OpenNMS会测试一下那个远程路由器广域网接口的ip，通过对这个ip的测试OpenNMS觉得是否该发出此节点Down的告警。OpenNMS测试的这个节点叫做此节点的Critical Path IP Address（关键路径Ip地址）。<br /><br />给一个节点配置Path Outage<br />在OpenNMS的节点配置上，点击Admin, 点击 Configure Path Outage，输入对于这个节点来说关键的ip地址。点击Submit按钮。<br /><br />配置基于规则的Path outage<br />可以为一组节点配置一个规则。在总导航条上选中Admin，Configure Notifications，点击Configure Path Outages，在Define the Critical Path下面输入一个Ip地址，例如：192.168.0.1（这种格式）；在Current Rule下面输入地址范围，例如：IPADDR IPLIKE 192.168.0.*；可以选中Show matching node list后的box，点击Validate Rule Results连接；在下面的页面可以查询到受那个关键Ip地址所影响的所有节点；最后点击Finish按钮完成配置。<br /><br />查看Path Outage<br />在总导航条上选中Path Outages，在页面中你可以看到你配置的所有Path Outages的规则。<br />这个文章基本上翻译的是[http://www.opennms.org/index.php/Path_Outage_How-To](http://www.opennms.org/index.php/Path_Outage_How-To) 只是觉得这是个不错的功能，所以就大概翻译了一下，希望对感兴趣的朋友们有帮助。由于手头硬件环境的限制，我还没有真实测试过这个功能，如果您对此功能做了什么测试的话，也欢迎和我交流，请留言或者或发邮件给我。
