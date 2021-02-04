---
author: liuadmin
categories:
- BMC
comments: true
date: 2011-05-04T15:59:42Z
slug: remedy-itsm-7-6-04-quick-install-guide
tags:
- ARS
- ITSM
- remedy
- 安装
title: Remedy ITSM 7.6.04 套件快速安装
url: /2011/05/04/remedy-itsm-7-6-04-quick-install-guide/
wordpress_id: 51038
---

![](http://media.cms.bmc.com/images/box_services_trio_compass.png)自从Remedy ITSM 7.6.03版本发布以后，Remedy ITSM套件有了一种全新的安装方式“预配置堆栈式安装”，这种安装方法简化了以前从ARS开始一个部件罗一个部件的安装方法，它将ITSM套件中的所有组件一次性的安装上去。下面讲具体该如何操作。


## 什么情况下使用这个安装方式？


A）POC的情况下
B）客户的生产环境满足下面的需求：
• Microsoft Windows Server 2008 (64-bit) (Standard, Enterprise, or Datacenter) with Microsoft SQL Server 2008 (64-bit) (Standard or Enterprise)
• Oracle Solaris 10 with Oracle 11g (64-bit) (Standard, Enterprise, or RAC)
• Red Hat Enterprise Linux 5 (Update 5) (64-bit) with Oracle 11g (64-bit) (Standard, Enterprise, or RAC)
• Microsoft Windows Server 2008 (64-bit) (Standard, Enterprise, or Datacenter) with Oracle 11g (64-bit) (Standard or Enterprise)
Note: The BMC Remedy ITSM Suite Precon gured Stack installer supports only Unicode database servers


## 这种方式安装了什么组件？


 BMC Remedy AR System server version 7.6.04
 AREA LDAP Directory Service Authentication
 ARDBC LDAP Directory Service Data Access
 Web Services Plugin
 Simple Network Management Protocol (SNMP) Configuration
 Full Text Search (FTS) Configuration
 Approval Server
 Assignment Engine
 Email Engine
 Flashboards
 Mid-Tier
 BMC Remedy AR System clients
 BMC Remedy User
 BMC Remedy Alert
 BMC Remedy Developer Studio
 BMC Remedy Data Import
 BMC Remedy Migrator
 Crystal Reports
 ODBC
 BMC Atrium Core
 BMC Atrium CMDB version 7.6.04
 Product Catalog version 7.6.04
 Atrium Impact Simulator version 7.6.04
 BMC Remedy ITSM Suite
 BMC Remedy Asset Management version 7.6.04
 BMC Remedy Change Management version 7.6.04
 BMC Remedy Incident Management version 7.6.04
 BMC Remedy Problem Management version 7.6.04
 BMC Remedy Service Desk 7.6.04
 BMC Service Level Management version 7.6.04
 BMC Remedy Knowledge Management version 7.6.0
如果你真的不需要安装以上所有组件，请不要使用此安装方法。


## 需要什么硬件？


System requirements for Microsoft Windows and UNIX®:
• Minimum 12 GB free disk space for the installation directory
• Minimum 8 GB free space for local database and remote database
• (For Red Hat Enterprise Linux® only) Minimum of 2.5 GB free space in the /tmp directory or /tmp file system.
• (For Oracle® Solaris only) Minimum of 2.5 GB free space in the /var/tmp directory or the file system.
• 3 GHz dual processor
• Minimum 3 GB RAM during installation; 8 GB RAM during runtime; 8 GB main memory for optimal performance
• (When 6 GB UNIX systems are used) Make sure that a minimum of 6 GB Swap Space is configured within the system.
如果您的硬件真的低于以上需要，请不要使用此安装方法，否则安装完之后系统可能不能正常运行。


## 需要什么人参与？


需要操作系统管理员和数据库管理员参与
以Linux+Oracle为例，可能需要如下环境变量
[bash]
export ORACLE_BASE=/u01/app/oracle
export ORACLE_SID=remedy
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
export NLS_LANG=en_US.UTF8
export LANG=en_US.utf8
export PATH=$PATH:$ORACLE_HOME/bin
[/bash]


## 需要什么安装文件？


以Linux+Oracle的安装为例，需要如下文件：


linux.x64_11gR2_database_1of2.zip
linux.x64_11gR2_database_2of2.zip
jdk-6u25-ea-bin-b03-linux-amd64-27_feb_2011.bin
BMCRemedyITSMSuitePreconfiguredStack7.6.04.Linux.tar.gz


## 需要安装多长时间？


大约1.5个小时左右，是的没有夸张，这个时间是在一个DELL E6400（64位，8GB内存）的笔记本上测得的，如果你有更好的硬件，相信可以更快，这应该是史上最快的Remedy ITSM套件安装速度，如果你也成功通过此方式安装，请留下评论留下下你的安装时间和系统配置情况。


## 参考以下操作步骤


安装之前需要根据网卡的MAC地址先申请一个Lic，接着基本上都是点Next，即可完成安装
[imagebrowser id=8]
