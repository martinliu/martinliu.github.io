---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-01-28T13:31:00Z
slug: cisco-network-configure
tags:
  - cisco
  - configure
  - snmp
title: Cisco网络设备如何配置SNMP代理
url: /2007/01/28/cisco-network-configure/
wordpress_id: 49137
---

Cisco 是网络设备的老大，它的设备以稳定、成熟和高性能著称。很多用户都以自己的网络设备是 99％的 Cisco 设备而自豪。<br /><br />对于任何一个网络设备如果没有配置 SNMP 代理，就不能被任何管理工具管理。下面的这个连接就是关于如何配置 Cisco 的 SNMP 服务：[http://www.cisco.com/univercd/cc/td/doc/product/software/ios122/122cgcr/ffun_c/fcfprt3/fcf014.htm](http://www.cisco.com/univercd/cc/td/doc/product/software/ios122/122cgcr/ffun_c/fcfprt3/fcf014.htm)<br /><br />可网管网络设备都内置有 SNMP 代理，很多网管不喜欢配置、enable SNMP 服务的理由如下：不希望 SNMP 服务占用 CPU、内存等资源；不信任 SNMP 服务的安全性；不认确认 SNMP 管理协议的价值。我个人认为：通过 SNMP 协议对网络设备管理的价值将远远高于它对设备造成的消耗和带来的风险。如果你同时面对和管理 30 台以上的网络设备，试想把它们的运行状况做一遍检查，您需要花的时间是多长。<br /><br />网络管理系统和网络设备的互动如下：<br />

<br />	
  1. 网管系统主动定时读取MIB的值，存储和分析得到的数值，产生报表和报警事件。
<br />	
  2. 网管系统被动作为网络设备发送Trap的目的地，网管系统需要能翻译各种网络设备的Trap信息的意义。
<br />
