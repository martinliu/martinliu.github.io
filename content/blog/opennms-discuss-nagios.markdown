---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-02-01T14:51:00Z
slug: opennms-discuss-nagios
tags:
  - Nagios
  - opensource
title: 翻译[opennms-discuss]邮件组里的一个讨论“Nagios转变”
url: /2007/02/01/opennms-discuss-nagios/
wordpress_id: 49138
---

全文在＝》[China OpenNMS](http://opennms.blogspot.com/2007/01/opennms.html)<br />[![](http://www.opennms.org/images/thumb/a/a3/Untitled.PNG/800px-Untitled.PNG)](http://www.opennms.org/images/thumb/a/a3/Untitled.PNG/800px-Untitled.PNG) --------------------------------------------<br />我们已经在一个中等规模的企业实施了 Nagios，用来监控一堆 Cisco 设备：交换机、路由器、防火墙，还有各种类型的服务器<br />（Windows,Linux 和 Unix）。对我们来说 Nagios 工作的非常好。我们现在看 OpenNMS，是由于她有好看的用户界面和集成的服务资源<br />图。我喜欢 Nagios 是由于它的模块化。我能很容易的写一个插件来完成任何相关的事情。<br />我看到 OpenNMS 有 NRPE 和 NSCLIENT 的能力，但是有一些邮件和资源图不能彻底的采集到。有人正打算用 OpenNMS 作为 Nagios 或者其他<br />软件的替代品？我的答案是非常确定的，可是我也非常想听到一些关于 OpenNMS 的成功或者不很成功的故事。我正在测试环境中使用<br />的是 OpenNMS1.3.2。<br /><br />Thanks!<br />Jon Christensen<br />--------------------------------------------<br />我们也有一个和你类似的环境（路由器、交换机、各种服务器），目前有大约 250 个节点。<br />使用一个 CentOS4 的服务器，我们已经在上面安装了 OpenNMS1.2.9，Syslog-NG，Swatch, Logtool([http://xjack.org/logtool/](http://xjack.org/logtool/))，<br />在 Windows 上用 Informant MIB，在几乎所有 Linux/Unix 上的是 NET-SNMP，和它们一起的还有很多在客户端的自定义脚本；它们中的<br />大多数都使用 send-event.pl 或者和它无关。<br />应为所有这些，我们已经能完全替代了 HP OpenView，虽然这是我的一面之词：这个架构是如此的模块化，以致于我们能做的比我们<br />使用 OpenView 的还要多，因种种理由。<br />Tim Selivanow<br />NOC Technician<br />EasyStreet Online Services, Inc.<br />******************\_\_******************<br />我的个人观点：<br />从 Nagios 转到 OpenNMS 上，其实不太容易。由于一下因素：<br />1）Nagios 非常模块化，架构让人决定非常稳定可靠；它没有用到 Java。<br />2）它的文档非常好，包括它官方的使用手册和用户上传的文档；从文档可以看出这个欧洲 Base 的项目非常踏实，风格严谨。开发 ONMS 的那帮老米显得比较自作聪明一点。<br />3）Nagios 的论坛很好，有很多人可以互相帮助。
