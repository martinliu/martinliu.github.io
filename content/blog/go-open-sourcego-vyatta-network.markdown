---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2007-06-09T08:56:00Z
slug: go-open-sourcego-vyatta-network
tags:
- Network
- swithch
title: Go Open Source,GO! Vyatta开源软件挺进网络硬件领域
url: /2007/06/09/go-open-sourcego-vyatta-network/
wordpress_id: 49161
---

[![](http://www.vyatta.com/images/masthead.jpg)](http://www.vyatta.com/images/masthead.jpg)<br />这是一个比较新的产品，提供开源的软件路由的解决方案；他们的目标直指Cisco这些大牌网络硬件厂商。它能简单的安装和运行在32bit的普通计算机硬件上，实现路由器的几乎所有功能；能支持的硬件平台和路由协议还真不少，请查看 [Datasheet](http://www.vyatta.com/products/vyatta_software_datasheet.pdf)；下载[ 网址](http://www.vyatta.com/download/)<br /><br />在VMWare中安装了一下发现它可以完全满足我需求：<br />1）在公司中办公网络建立一个隔离的测试网。<br />2）测试网中提供DHCP,DNS服务<br />3）提供NAT,Firewall<br />4）安装简单，硬件需求低<br /><br />准备在公司实际环境中安装测试，安装和配置信息待续。<br /><br />现在我正在Vyatta Router后面的小网内更新这个Blog。<br />上午的安装过程如下：<br />（硬件准备）<br />测试机一台 Dell Gx620，主板上带Intel的内置网卡一块TP-LINK TG-3269C，网线若干<br />（网络环境）<br />在一台办公网的机器上，寻找一个未使用的IP地址，这个地址会分配给Router的Internet网卡上；然后运行 ipconfig /all 记录下默认网关、默认DNS和子网掩码，这些信息会配置到Router上。<br />（安装过程）<br />

<br />	
  1. 下载Vyatta的试用手册 [Quick Eval Guide - Boot, Configure & Test the Vyatta software](http://www.vyatta.com/documentation/vyatta_evalguide.pdf)翻到手册的第三页，重新标准出你的网络信息，注意后面的配置跟这里的信息有关。为了简单起见，我就改了对外链接的哪个网卡的IP地址，至于内网么，有什么ip地址范围都无所谓了呵呵
<br />	
  2. 下载刻录Vyatta软件 [Vyatta Community Edition 2 - CD-ROM Image](http://www.vyatta.com/download/ofr.php) 刻录到一张空白CD上
<br />	
  3. 把可好的CD放入机器中，从CDROM启动，这其实是一个livecd。启动过程可以无需关心，看似是一个Linux PE的CD，启动之后用root进入操作系统，root的密码是vyatta。进入后可以查看一下 vi /var/log/dmesg 主要看看你的两个网卡它是否能真确识别。我的测试机是Intel CPU的，不知道AMD的机器是否呢个装，没试过。
<br />	
  4. 其它的配置过程文档中说的非常详细，不用我在多说。
<br /><br />安装之后的小节：<br />Router有两个网卡，在对外的网卡上做了，NAT，firewall，在对内的网卡上做了DHCP,DNS，现在我的笔记本在Router后的小网里，运行ipconfig /all的结果如下<br />Ethernet adapter Local Area Connection:<br /><br />Connection-specific DNS Suffix  . : mycompany.com<br />Description . . . . . . . . . . . : Broadcom 570x Gigabit Integrated Con<br />troller<br />Physical Address. . . . . . . . . : 00-0F-1F-BB-B2-92<br />Dhcp Enabled. . . . . . . . . . . : Yes<br />Autoconfiguration Enabled . . . . : Yes<br />IP Address. . . . . . . . . . . . : 10.0.0.150<br />Subnet Mask . . . . . . . . . . . : 255.255.255.0<br />Default Gateway . . . . . . . . . : 10.0.0.1<br />DHCP Server . . . . . . . . . . . : 10.0.0.1<br />DNS Servers . . . . . . . . . . . : 192.168.172.200<br />10.100.112.27<br />Lease Obtained. . . . . . . . . . : 2007年6月12日 11:57:30<br />Lease Expires . . . . . . . . . . : 2007年6月13日 11:57:30<br /><br />总之这是一个非常成功的测试，这个产品真的非常Coooooool！！！！！它让我看到了OpenSource的东西不仅可以在纯软件领域和商业产品有所比较，它还能在硬件领域有所作为。<br /><br />
