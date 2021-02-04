---
author: liuadmin
categories:
- Blog
- ITIL/ITSM
comments: true
date: 2009-11-28T09:29:04Z
slug: remedy-itsm-76-installation-tips
tags:
- "7.6"
- BMC
- linux
- oracle
- remedy
- SUSE Linux Enterprise Server
- 安装
- 技巧
title: Remedy ITSM 7.6 installation Tips
url: /2009/11/28/remedy-itsm-76-installation-tips/
wordpress_id: 50186
---

自从7.6发布和以后一直没有时间安装，通过最近的几次安装，积累了一些经验，供大家参考。在安装开始之前请一定查看[ARS_7500_Comp_Matrixv1001.pdf](http://www.bmc.com/support/product-availability-compatibility)文档，保证操作系统、数据库、中间件和JDK的版本都符合要求。如果是安装生产系统的话，建议把数据库和应用服务器分开，硬件配置也一定参考Remedy ITSM安装手册中的建议硬件配置要求。


![](http://www.beareyes.com.cn/2/lib/200701/19/452/image002.jpg)![](http://www.my-softwareteacher.com/images/oracle_logo.gif)


最近在Linux的虚拟机上做了一次安装，相关细节如下:



	
  * Suse Linux Enterprise server 10 sp2 64 bit

	
  * Oracle 10G 64bit (10201_database_linux_x86_64.cpio.gz)

	
  * JDK 1.6(jdk-6u6-linux-i586.bin)


在Suse Linux上安装Oracle还是比较容易的，可以参考这个安装手册进行，[下载](ftp.novell.com/partners/oracle/docs/10gR2_sles10_install.pdf )。数据库安最好按照成utf8字符集，如下图所示：

[](http://martinliu.cn/?attachment_id=50187)[![](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2009/11/snap00142-300x234.jpg)](http://martinliu.cn/http:/martinliu.cn/2009/11/remedy-itsm-76-installation-tips.html/snap00142/)

Remedy ITSM套件的安装分为三个步骤：1）ARS 7.5 SP3 的安装；2）Atrium CMDB7.6安装；3）ITSM 7.6安装；其中第一步是最重要的，第二步骤如果安装产品目录数据的话时间花费比正常多一点。Remedy ARS 7.5是最新的补丁包，它修复了sp2的很多bug；是Remedy ITSM 7.6安装的必须版本。在安装ARS的时候需要准确的导出相关的环境变量，如果环境变量没有或者不够的话，安装程序则无法正确地连接数据库，下面的例子可以参考一下。

[![](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2009/11/snap00143-300x59.jpg)](http://martinliu.cn/http:/martinliu.cn/2009/11/remedy-itsm-76-installation-tips.html/snap00143/)

每一步安装完成之后都需要详细查看相关的日志，确保每一步都安装完全正确。在安装完ARS之后一定要为服务器添加所有相关License。
