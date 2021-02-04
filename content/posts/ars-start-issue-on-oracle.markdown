---
author: liuadmin
categories:
- BMC
comments: true
date: 2011-04-02T13:43:21Z
slug: ars-start-issue-on-oracle
tags:
- ARS
- oracle
- remedy
- 启动
- 排错
title: ARS启动故障修复案例
url: /2011/04/02/ars-start-issue-on-oracle/
wordpress_id: 51017
---

ARS版本 7.6.04
数据库 Oracle11G 和ARS在同一台服务器上

错误现象：
ARS服务不能正常启动
arerror.log报 390600 : SQL 数据库不可用 -- 将重试连接 (ARNOTE 590)
Sat Apr 02 20:27:41 2011 : Action Request System(R) 服务器 x64 版本 7.6.04 Build 002 201101141059
(c) Copyright 1991-2010 BMC Software, Inc.
Sat Apr 02 20:29:51 2011  390600 : SQL 数据库不可用 -- 将重试连接 (ARNOTE 590)
Sat Apr 02 20:29:51 2011     ORA-12170: TNS:Connect timeout occurred

排错步骤：
使用sqlplus测试登录，返回TNS超时错误
[powershell]
 C:\Users\martin>sqlplus ARAdmin/AR#Admin#@ars
SQL*Plus: Release 11.2.0.1.0 Production on Sat Apr 2 20:48:35 2011
Copyright (c) 1982, 2010, Oracle.  All rights reserved.
ERROR:
ORA-12170: TNS:Connect timeout occurred   
[/powershell]
使用tnsping ars 测试也不成功
ping本机主机名
[powershell]
ping arsserver
Pinging arsserver [fe80::c123:5921:b71b:64fd%13] with 32 bytes of data:
Reply from fe80::c123:5921:b71b:64fd%13: time<1ms
Reply from fe80::c123:5921:b71b:64fd%13: time<1ms
Reply from fe80::c123:5921:b71b:64fd%13: time<1ms
Reply from fe80::c123:5921:b71b:64fd%13: time<1ms
Ping statistics for fe80::c123:5921:b71b:64fd%13:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 0ms, Maximum = 0ms, Average = 0ms 
[/powershell]
貌似找到原因，修改host文件，加入主机名到127.0.0.1 后面，在测试ping主机名成功。
重启Oracle监听器服务，再次测试tnsping 和sqlplus ，测试都获得成功。
重新启动ARS服务，服务被正常启动
