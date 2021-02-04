---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-01-21T17:34:00Z
slug: trap-tools
tags:
- NSM
- Tools
- Trap
title: 网管系统的测试工具
url: /2008/01/21/trap-tools/
wordpress_id: 49181
---

很多网络系统管理软件都有Trap管理的功能，在系统的安装和配置过程中；验证系统是否能正常处理Trap是很麻烦的事情。原因有很多，发送trap的设备没有，设备上的snmp没有启用，或者设备都正常，到网管系统的网络可能有防火墙吧snmp给堵住了。<br /><br />为了方便的测试和配置网络管理监控系统，需要手工生产和验证trap的发送和接收。最近偶然在网上发现了这样几个免费（非OSS软件）软件工具，可以做这件事。<br /><br />下载的网站是：[http://www.ncomtech.com/](http://www.ncomtech.com/) 下面吧我所下载和测试的软件做一个小结，希望对您有所帮助：<br />

<br />	
  * **Trap Receiver** [http://www.trapreceiver.com/](http://www.trapreceiver.com/) 是一个Windows程序非常小，安装了之后会在windows安装一个服务。程序的启动目录是C:\Program Files\Trap Receiver\TrapRcvr.exe 程序界面非常简单，如下图所示：
<br /><br />[![image](http://lh5.google.com/liuzh66/R5TXj4CljQI/AAAAAAAAAdI/FPsG9LiZrXo/image%5B12%5D.png)](http://lh5.google.com/liuzh66/R5TXj4CljQI/AAAAAAAAAdI/FPsG9LiZrXo/image%5B12%5D.png)<br /><br />点击configure按钮后可以做一些配置：Action －－当收到某些特定的trap是出发邮件、声音等动作；logging－－把收到的trap信息按照某种格式记录在文件中；Mibs－－导入目标设备的trap文件，让这个接收器能认识到另外的trap格式。还有其他配置信息也非常简单。<br />

<br />	
  * **TrapGen **[http://www.ncomtech.com/trapgen.html](http://www.ncomtech.com/trapgen.html) 顾名思义－这就是一个手工生产和发送trap的工具，是一个命令行工具。example:  trapgen -d 192.168.2.3；上图中的第一条和第三条就是用这个命令发出的trap。欲知详细帮助信息，使用"trapgen -h"
<br />	
  * **I/F Spy** [http://www.ncomtech.com/ifspy.html](http://www.ncomtech.com/ifspy.html) 是一个网络接口枚举工具，它通过snmp协议去访问目标设备的IFMIB信息，显示所有IFMIB相关信息。
<br />	
  * **UDP Listen** [http://www.ncomtech.com/udplisten.html](http://www.ncomtech.com/udplisten.html) **UDP**协议的监听程序，是命令行工具，有linux和Solaris版，能用作一个debug工具。
<br />	
  * **Thingy** [http://www.ncomtech.com/thingy.html](http://www.ncomtech.com/thingy.html)是一个Windows下的GUI工具，能帮你监控三个SNMP指标，采集并做大于等于和小于的逻辑判断然后显示不同的信号灯。
<br /><br />这几个小工具都很小，都能在windows下安装和使用对网络系统监控软件的安装、配置和排错应该有一定的帮助。如果您有什好的小工具也请回复一下本文。
