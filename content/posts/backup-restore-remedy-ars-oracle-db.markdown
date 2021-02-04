---
author: liuadmin
categories:
- BMC
comments: true
date: 2011-02-14T15:05:27Z
slug: backup-restore-remedy-ars-oracle-db
tags:
- ARS
- backup
- BMC
- cmdb
- install
- ITSM
- remedy
- 备份
- 安装
- 恢复
- 部署
title: 在Oracle上备份和恢复 Remedy ARS数据库
url: /2011/02/14/backup-restore-remedy-ars-oracle-db/
wordpress_id: 50947
---

# Why ARS system need full backup and restore


众所周知_Remedy ARS_上运行的所有程序代码都是在数据库中存储的，几乎所有的程序代码和相关数据都是存储在后端的数据库里的。基于这种特性，我们可以很方便地从数据库层面实现对ARS系统的备份和恢复。所谓基于数据库的备份和恢复就是指数据库的全库导入和导出。在这方面_Oracle_做的很好，他所提供的imp和exp命令行工具能很好的完成此项任务。
![](http://img.en25.com/Web/BMCSoftwareInc/eloqua_webform_banner_868w_arch07.jpg)


# When you may backup BMC Remedy ARS system Database


_Remedy ARS_系统数据库全备份可能会发生在下面的几个时间点：



	
  1. 


## 在安装过程中，_Remedy ITSM_套件的安装都是从ARS开始一个模块一个模块增加安装的，可以在安装每个新模块之前，做一个数据库备份，用于安装失败情况下的现场恢复




	
  2. 


## 在系统上线前，当系统需要做升级/代码更新等等大规模操作之前可以考虑做一次数据库的导出备份




	
  3. 


## 在做系统迁移的情况下，我们甚至可以生产库迁移到开发机上进行问题的重现，或者代码的修改，或者测试，完成之后再导回生产系统（如果生产系统再次期间处于维护状态的话）







# How-to


下面是我总结的相关操作步骤参考。


## 备份_ARSystem_数据库


exp aradmin/ar#admin@itil file=c:\before-patch7.dmp log=c:\exp.log compress=n statistics=none

参数解释：
aradmin/ar#admin  是ARS系统默认的用户名和口令
@itil 是ARSystem数据库所在的数据库实例名
file=c:\before-patch7.dmp log=c:\exp.log  是导出的数据库文件和日志文件路径


## _删除ARAdmin用户数据_


drop user aradmin cascade;


## _创建和授权ARAdmin用户_


CREATE USER ARADMIN
IDENTIFIED BY ar#admin#
DEFAULT TABLESPACE ARSYSTEM
TEMPORARY TABLESPACE ARTMPSPC
PROFILE DEFAULT
ACCOUNT UNLOCK;

GRANT ARADMINROLE TO ARADMIN;
ALTER USER ARADMIN DEFAULT ROLE ALL;
ALTER USER ARADMIN QUOTA UNLIMITED ON ARSYSTEM;


## _导入备份的数据文件_


imp ARAdmin/AR#Admin@ars file=c:\CMDB2010-12-13_13.dmp log=c:\imp.log  fromuser=ARAdmin touser=ARAdmin ignore=y

Credit to：以上操作步骤由_神州太岳_工程师_李成旗_协助编写和测试.
