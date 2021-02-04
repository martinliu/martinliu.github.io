---
author: liuadmin
categories:
- Tools
comments: true
date: 2007-04-28T11:43:00Z
slug: nmap-network-mappe
tags:
- Nmap
title: Nmap — Network Mapper(网络映射器)
url: /2007/04/28/nmap-network-mappe/
wordpress_id: 49149
---

[![](http://images.insecure.org/nmap/images/nmap_bnr_euroboy.jpg)](http://images.insecure.org/nmap/images/nmap_bnr_euroboy.jpg)<br /><br />Nmap (“Network Mapper(网络映射器)”) 是一款开放源代码的 网络探测和安全审核的工具。它的设计目标是快速地扫描大型网络，当然用它扫描单个 主机也没有问题。Nmap以新颖的方式使用原始IP报文来发现网络上有哪些主机，那些 主机提供什么服务(应用程序名和版本)，那些服务运行在什么操作系统(包括版本信息)， 它们使用什么类型的报文过滤器/防火墙，以及一堆其它功能。虽然Nmap通常用于安全审核， 许多系统管理员和网络管理员也用它来做一些日常的工作，比如查看整个网络的信息， 管理服务升级计划，以及监视主机和服务的运行。<br />Nmap输出的是扫描目标的列表，以及每个目标的补充信息，至于是哪些信息则依赖于所使用的选项。 “所感兴趣的端口表格”是其中的关键。那张表列出端口号，协议，服务名称和状态。状态可能是 open(开放的)，filtered(被过滤的)， closed(关闭的)，或者unfiltered(未被过滤的)。 Open(开放的)意味着目标机器上的应用程序正在该端口监听连接/报文。 filtered(被过滤的) 意味着防火墙，过滤器或者其它网络障碍阻止了该端口被访问，Nmap无法得知 它是 open(开放的) 还是 closed(关闭的)。 closed(关闭的) 端口没有应用程序在它上面监听，但是他们随时可能开放。 当端口对Nmap的探测做出响应，但是Nmap无法确定它们是关闭还是开放时，这些端口就被认为是 unfiltered(未被过滤的) 如果Nmap报告状态组合 openfiltered 和 closedfiltered时，那说明Nmap无法确定该端口处于两个状态中的哪一个状态。 当要求进行版本探测时，端口表也可以包含软件的版本信息。当要求进行IP协议扫描时 (-sO)，Nmap提供关于所支持的IP协议而不是正在监听的端口的信息。<br />除了所感兴趣的端口表，Nmap还能提供关于目标机的进一步信息，包括反向域名，操作系统猜测，设备类型，和MAC地址。<br /><br />摘自：[nmap中文文档](http://insecure.org/nmap/man/zh/) [nmap首页](http://insecure.org/nmap/index.html)
