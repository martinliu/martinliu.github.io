---
author: liuadmin
categories:
- Desktop
comments: true
date: 2013-05-24T01:32:28Z
subtitle: 刚刚入手了一台 Lenovo ThinkCenter M92/M92p Tiny测试机，虽然配置不高但是出于geek习惯，还是要动动螺丝刀的。下面是拆机过程，供参考。
slug: microserver-lenovo-thinkcenter-m92m92p-tiny
tags:
- cloudstack
- hadoop
- Lenovo
- M92
- M92p
- ThinkCenter
- Tiny
- xenclient
- XenDesktop
- xenserver
title: Microserver Lenovo ThinkCenter M92/M92p Tiny
url: /2013/05/24/microserver-lenovo-thinkcenter-m92m92p-tiny/
wordpress_id: 52436
---

刚刚入手了一台 Lenovo ThinkCenter M92/M92p Tiny测试机，虽然配置不高但是出于geek习惯，还是要动动螺丝刀的。下面是拆机过程，供参考。
[gallery columns="2" link="file" ids="52429,52430,52431,52432,52433,52434,52435"]

这款机器目前在国内好像还没有正式买，起码联想中国官网上连技术指标也查不到。美国网站上是有这个机器的介绍。

[caption id="" align="alignnone" width="960"][![](http://www.lenovo.com/images/products/desktops/m-series/m92p-hero-ribbon.jpg)](http://www.lenovo.com/products/us/desktop/thinkcentre/desktops-towers-us-only/m92-m92p/) ThinkCenter M92P[/caption]


## At a Glance





	
  * Up to 3rd generation Intel® Core™ i7

	
  * Up to Windows 8 Pro

	
  * Up to 1TB HDD, Up to 128GB SSD

	
  * Up to 32GB memory (4x8GB)

	
  * [M92/M92p Tower Tech Specs](http://www.lenovo.com/products/us/tech-specs/desktop/thinkcentre/m-series-towers/m92-m92p/)

	
  * [M92/M92p Tiny Tech Specs](http://www.lenovo.com/products/us/tech-specs/desktop/thinkcentre/m-series-towers/m92-tiny/)


我所测试的是M92 Tiny型。改机默认安装的Win8操作系统。如果把它改装为跑Hypervisor的服务器的话，它应该属于 Microserver的范畴。


<blockquote>微服务器定义：A micro server (may also be written as microserver or MicroServer) is a small server appliance that works like a server. Micro servers are off-the-shelf appliances that are designed for ease of installation and maintenance. A micro server will come with the operating system, hardware and software preinstalled and configured by the manufacturer. Some configuration functions of the micro server may be performed by the end-user through a touch panel and access to the server appliance is through a Web browser.
A micro server is a popular choice for small- to medium-sized businesses that need a server but do not need a full-scale rack or tower server. Micro servers are also used by corporations that operate with minimal IT staff at local or branch offices.
A micro server may also be called a server appliance.</blockquote>


接下来，我准备在这个机器上做些改动和测试。



	
  1. 如果有可能的话，更换硬盘为SSD硬盘，升级内存到最大两条8GB，共16GB

	
  2. 安装和测试XenClient：使用集中管理器，来更新本地硬盘的Widnows虚拟机操作系统

	
  3. 安装和测试XenServer：在上面跑XenDesktop的虚拟机，看看做多能达到多少个用户的密度，分别测试共享桌面和VDI桌面，看看共享桌面的密度会在这个机器上比VDI高几倍？

	
  4. 测试跑CloudStack的计算节点，试想如果实验室里面有一摞16个机器，都做在一个群集上，跑跑大数据Hadoop 应用，应该也是很好的使用场景


