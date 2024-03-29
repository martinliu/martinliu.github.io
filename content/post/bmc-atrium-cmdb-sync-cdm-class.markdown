---
author: Martin Liu
categories:
  - CMDB
comments: true
date: 2011-01-12T04:22:44Z
slug: bmc-atrium-cmdb-sync-cdm-class
tags:
  - Atrium
  - itsm
  - class
  - cmdb
title: BMC Atrium CMDB 类定义迁移
url: /2011/01/12/bmc-atrium-cmdb-sync-cdm-class/
wordpress_id: 50854
---

当对 CDM 做了定制，并且要在不同的服务器直接做类的迁移的时候，需要把定制过的类都导出，然后在目标机上导入。可以使用的 CMDB 自带的命令行 cmdbdriver 工具。

_**cmdbdriver.exe 能支持的参数**_

Options:
-u<USER>
-a<AUTHORSTRING>
-p<PASSWORD>
-l<LOCALE>
-s<SERVER>
-x<INPUTFILE_FULLPATH>
-t<PORT_NUMBER>
-q<QUIET_MODE_NUMBER>

登录 CMDBdriver 实例：   cmdbdriver -u Demo -p bmc@XXX -s atriumcmdb -t 9988

登录之后在运行另外用于初始化的两个命令 init 和 log

Command: init
INITIALIZATION

CMDBInitialization  results
ReturnCode:  OK
Status List : 0 items

Command: log
Control record:
Authentication string () :
User name () : Demo
Password () : ****\*\*****
Locale[.charSet] () :
TimeZone () :
Server () : atriumcmdb

_**导出类定义的方法实例**_
Command: xexpdf
XEXPORT DEFINITION
Export all classes? (F):
Classes to export:
Class and its subclasses, From namespace (1,2) (1):
Namespace (): BMC.CORE
Class name (): BMC_ComputerSystem
Export all attributes with classes? (T):
Filename for exported data: c:\demo\BMC_ComputerSystem.xml

CMDBXExportDef  results
ReturnCode:  OK
Status List : 0 items

使用文本编辑器查看 c:\demo\BMC_ComputerSystem.xml 的导出结果

_**导入类定义的方法：**_
Command: impdf
DEFINITION IMPORT
Import Item List:
Number of import items (0):
Import option : Create/Overwrite (1-2) (1): 2
Filename containing import data: c:\demo\cs.xml

CMDBImportDef  results
ReturnCode:  OK
Status List : 0 items

使用 Remedy User，用 Demo 登录，把语言切换到英文，然后在查 BMC_ComputerSystem 表达，在 custom 2 ～ n 的 tab 页面里面查看哪些导入的属性。或者使用 class manager 查看确认导入是否成功。
