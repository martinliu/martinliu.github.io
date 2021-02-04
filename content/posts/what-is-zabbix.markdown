---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-05-22T13:51:00Z
slug: what-is-zabbix
tags:
- zabbix
title: What is ZABBIX?
url: /2007/05/22/what-is-zabbix/
wordpress_id: 49155
---

[![](http://www.zabbix.com/img/zabbix1.png)](http://www.zabbix.com/img/zabbix1.png)<br />第一次看到这个软件是在OpenNMS的邮件讨论组中，他们计划做一个vmware的image放到[VMTN上](http://www.vmware.com/vmtn/appliances/index.html) 。我在VMTN里哪里点击了一下监控管理这一类，一个叫[OpenESM的项目](http://www.vmware.com/vmtn/appliances/directory/124)进入了我的视线。它能引起我的注意是因为，它在项目的描述中说:我们理解ITSM、、、、[Check it out](http://www.openesm.com/s1/)! 大致浏览了一下他们的网站，发现他们的目的是在Zabbix的基础上作一下优化和开发，加入若干特色：GSM modem发短信、新报表、SLA监控等。<br /><br />现在很多项目都有迅速实施的解决方案。对于很多开源项目来说，它们对于新手的相同门槛就是安装。安装上了，不会配置；配置好了，不会用；用上了解决不了问题。<br /><br />我先下载了[OpenESM](http://www.vmware.com/vmtn/appliances/directory/124) ，一个不算太大的文件1.3GB。解压缩之后用VMWare打开运行，猜出root的用户名是openesm，登陆之后发现它是一个Fedora的虚拟机。登陆OpenESM的控制台， http://ip/ 接下来就需要去www.openesm.com上下载手册了，否则无法继续下去。照着手册安装代理，在我的两个Windows的机器上。安装需要先下子代理安装包，允许安装命令的时候需要制定自己的主机名和服务器的主机名。在控制台中加入这两个安装了代理的机器，由于是初次使用没用玩自动发现之类的功能。收集了一阵子数据之后，很快发现了很多有趣的数据。<br /><br />最终总结如下<br />

<br />	
  * 这是我安装的第一个有代理程序的开源监控软件，感觉在Windows下代理的安装还是比较方便的。比我想象的简单，安装文件只有一个exe文件，装完之后形成一个服务。我记得在查阅文档的时候看到了一文档，上面列出了所有代理程序能收集的数据的表格，说明了什么数据在什么操作系统中支持，那些不支持。它能在多种操作系统上安装，他的安装时说从代码编译安装，windows上不需要，在非windows上就以为这需要安装编译器什么的。这好像并不是特别好。
<br />	
  * 可用性和性能的数据都能收集。
<br />	
  * 事件管理功能，能触发action，还没有试过，能触发邮件和GSM短信等。没有试过。
<br />	
  * 没有试的还挺多，还需要进一步研究。
<br />
