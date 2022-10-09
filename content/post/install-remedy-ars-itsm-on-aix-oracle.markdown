---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2010-09-22T13:51:14Z
slug: install-remedy-ars-itsm-on-aix-oracle
tags:
  - cmdb
  - ITSM
  - remedy
title: 八月十五月儿圆，我和兄弟们装AR
url: /2010/09/22/install-remedy-ars-itsm-on-aix-oracle/
wordpress_id: 50811
---

![](http://ww.61bay.com/pic/upload/10ph1/20095272001540.jpg)经过几天的奋战，我们终于在中秋月圆之夜，在黑山扈的百望山脚下为客户成功地安装了 Remedy ITSM 7.6.03 每当安装程序一次次挂死、安装程序界面不正常显示、安装不完全、安装失败，都让在场的人达到抓狂的后期，无语~~ 这里总结一下这几天的失败安装的血泪史，供后来人参考学习。

版本的确认：所有操作系统，JVM，JDK，数据库，数据库客户端，和以上软件的位数都需要查明，都需要在 Remedy 的兼容文档中一一确认。

AIX 操作系统的字符集：需要同时安装中英文的 UTF8 字符集。安装方法 smitty，需要有操作系统的安装盘，安装完成之后，locale -a ，需要能看到 ZH_CN, ZH_CN.UTF-8,EN_US, EN_US.UTF-8 这四种字符集缺一不可。否则无法以中文方式安装成功，也无法让操作系统已中文 utf8 来启动 AR 服务。

XManager 需要安装在于 AR 同一网段的 Windows 服务器上，例如 Mid-tier 可能安装在 Windows 上，并与 AR 在同以网段，那么安装程序最好在该服务器的 Xmanager 的客户端中安装，从哪里连接 AIX 服务器并运行安装程序。如果不在同一个网段，安装程序很有可能安装了一半或者无名的消失，安装进程会立刻中断，需要把系统推到重来。

AIX 系统上 font server 的安装：使用 netstat -na|grep 7100， 如果没有结果则需要从 AIX 的光盘中在 AIX 的服务器上安装 font server 和相关的包，并且启动它。如果不装的话，remedy 安装程序可能界面显示不正常，或者不显示。

Oracle 上众多僵尸进程：如果在安装 CMDB 或者 ITSM 套件的时候，安装界面挂死或者消失，这会是 Oracle 服务器上产生上百个僵尸进程，这些进程会吃光 Oracle 服务器的所有物理内存。我们的 oracle 服务器的 16GB 内存被吃光之后，ITSM 安装界面几乎停止，20~30 分钟才能安装完一个定义文件。解决方法是：随时监控 Oracle 服务器的内存使用情况，当出现内存被僵尸进程吃光的情况，可以考虑使用 IT 行里无人不知的无敌重启方案，重启 Oracle 服务器的操作系统，从启动 Oracle 数据库实例，重启 ARS 服务，然后再次安装 Remedy ITSM。

Remedy 安装之备份：如果是在 AIX+Oracle 的数据库上安装。Remedy 还是非常绿色的软件，需要在安装完 AR，CMDB，ITSM 套件后各做一个 Remedy 安装文件目录的备份，在 AIX 上可以把这个文件夹 tar 起来备用。Oracle 数据库还是非常容易备份的，使用 imp 和 exp 命了就可以搞定，具体语句咨询 DBA。切忌在安装 CMDB 和 ITSM 之前一定要对 Remedy 系统的安装文件和数据库做备份，一旦安装失败，可以恢复文件，恢复数据库，排错后重新再来。
