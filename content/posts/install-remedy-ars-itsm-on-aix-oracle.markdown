---
author: liuadmin
categories:
- ITIL/ITSM
comments: true
date: 2010-09-22T13:51:14Z
slug: install-remedy-ars-itsm-on-aix-oracle
tags:
- "7.6"
- ar
- ARS
- cmdb
- ITSM
- remedy
title: 八月十五月儿圆，我和兄弟们装AR
url: /2010/09/22/install-remedy-ars-itsm-on-aix-oracle/
wordpress_id: 50811
---

![](http://ww.61bay.com/pic/upload/10ph1/20095272001540.jpg)经过几天的奋战，我们终于在中秋月圆之夜，在黑山扈的百望山脚下为客户成功地安装了Remedy ITSM 7.6.03 每当安装程序一次次挂死、安装程序界面不正常显示、安装不完全、安装失败，都让在场的人达到抓狂的后期，无语~~ 这里总结一下这几天的失败安装的血泪史，供后来人参考学习。

版本的确认：所有操作系统，JVM，JDK，数据库，数据库客户端，和以上软件的位数都需要查明，都需要在Remedy的兼容文档中一一确认。

AIX操作系统的字符集：需要同时安装中英文的UTF8字符集。安装方法smitty，需要有操作系统的安装盘，安装完成之后，locale -a ，需要能看到 ZH_CN, ZH_CN.UTF-8,EN_US, EN_US.UTF-8 这四种字符集缺一不可。否则无法以中文方式安装成功，也无法让操作系统已中文utf8来启动AR服务。

XManager需要安装在于AR同一网段的Windows服务器上，例如Mid-tier可能安装在Windows上，并与AR在同以网段，那么安装程序最好在该服务器的Xmanager的客户端中安装，从哪里连接AIX服务器并运行安装程序。如果不在同一个网段，安装程序很有可能安装了一半或者无名的消失，安装进程会立刻中断，需要把系统推到重来。

AIX系统上font server的安装：使用netstat -na|grep 7100， 如果没有结果则需要从AIX的光盘中在AIX的服务器上安装font server和相关的包，并且启动它。如果不装的话，remedy安装程序可能界面显示不正常，或者不显示。

Oracle上众多僵尸进程：如果在安装CMDB或者ITSM套件的时候，安装界面挂死或者消失，这会是Oracle服务器上产生上百个僵尸进程，这些进程会吃光Oracle服务器的所有物理内存。我们的oracle服务器的16GB内存被吃光之后，ITSM安装界面几乎停止，20~30分钟才能安装完一个定义文件。解决方法是：随时监控Oracle服务器的内存使用情况，当出现内存被僵尸进程吃光的情况，可以考虑使用IT行里无人不知的无敌重启方案，重启Oracle服务器的操作系统，从启动Oracle数据库实例，重启ARS服务，然后再次安装Remedy ITSM。

Remedy安装之备份：如果是在AIX+Oracle的数据库上安装。Remedy还是非常绿色的软件，需要在安装完AR，CMDB，ITSM套件后各做一个Remedy安装文件目录的备份，在AIX上可以把这个文件夹tar起来备用。Oracle数据库还是非常容易备份的，使用imp和exp命了就可以搞定，具体语句咨询DBA。切忌在安装CMDB和ITSM之前一定要对Remedy系统的安装文件和数据库做备份，一旦安装失败，可以恢复文件，恢复数据库，排错后重新再来。
