---
author: liuadmin
categories:
- ITSM
comments: true
date: 2008-04-21T02:16:20Z
slug: open-source-ticket-request-system-otrs-226
tags:
- ITIL
- ITSM
- OTRS
- Request Tracer
title: Open Source Ticket Request System - OTRS 2.2.6
url: /2008/04/21/open-source-ticket-request-system-otrs-226/
wordpress_id: 49200
---

I made a OTRS 2.2.6 virtual machine for anyone who wants to test both OTRS and OTRS::ITSM. It was built on OpenSUSE 10.2, including OTRS 2.2.6 and OTRS::ITSM 1.0.94. OTRS::ITSM implements ITIL (R) focused IT service management. OTRS::ITSM 1.0.94 is still on Beta, you might have some bugs when using this virtual machine. Please download from my box.net, if you have an comment please just let me know. I'd like to invite you to improve this virtual machine if you have any good ideal.

[Download it from here](http://demo.wholog.net/OSS.rar) [点此下载。 ](http://demo.wholog.net/OSS.rar)[This source is not available any longer. I will offer it by DVD.  这个地址已经无法下载，请关注我即将推出的DVD版虚机。](http://demo.wholog.net/OSS.rar)

**Thanks [BigYue.com](http://www.bigyue.com) for donated upload space.  感谢****[BigYue.com](http://www.bigyue.com)****的空间捐助。**

**Credentials 登录密码如下**



	
  * OpenSuSE 10.2 : username / password is "root/ca1234"

	
  * MySQL : username / password is "root/ "

	
  * OTRS : admin username and password is [root@localhost/root](mailto:root@localhost/root)


**Run 运行压缩文件中的虚拟机**



	
  1. Download and install VM Player, the machine should have 1GB RAM at least.

	
  2. Un-zip OSS.rar in a partition, freespace must be 2.5+ GB.

	
  3. Double MartinLiu.cn.vmx and power on this machine.

	
  4. Click "keep" and OK button when you get a popup box。

	
  5. The network connection of virtual machine is 'bridged'. You will see the ip address of this virtual machine at 5th line one the top of boot screen. NOTE: you should have DHCP server on your network.


**Access 访问虚拟机**



	
  * SSH to it.

	
  * Agent login page: [http://ip_address/otrs/index.pl](http://ip_address/otrs/index.pl)

	
  * Customer login page: [http://ip_address/otrs/customer.pl](http://ip_address/otrs/customer.pl)


**Tips of OTRS installation 安装经验**



	
  * Apache should have perl mod, configure perl for apache before you install OTRS. 这是一个Perl写的程序，所以在安装之前最好吧apache上的perl配置好，确认apache能运行perl的东西

	
  * Make sure your database accepts packages over 5 MB in size. Increase max_allowed_packet in my.cnf to 20MB. 修改my.cnf中的max_allowed_packet 参数到20MB，否则ITSM的包安装有问题。

	
  * OTRS需要一写附件的perl包的支持，手头最好有操作系统的安装dvd或者直接从网上安装。


**Usage 用途**



	
  * You can use it for any purpose, if you need any support you will contact OTRS。你可以用于任何用途，本博客不提供技术支持，请联系OTRS的邮件列表。

	
  * ITIL training, OTRS::ITSM implements ITIL (R) focused IT service management. 可以用于ITIL的培训，它能演示：incident management, problem management, configuration management 等。

	
  * This virtual machine comes with ABSOLUTELY NO WARRANTY. DO NOT USE it for production. 仅供测试使用，切勿用于生产环境。


If you like OTRS, you may try [Request Tracer](http://www.bestpractical.com/rt/)

今天一个网友告诉我另外一个开源的类似系统[Request Tracer](http://www.bestpractical.com/rt/) ，有空的话回头也试试。
