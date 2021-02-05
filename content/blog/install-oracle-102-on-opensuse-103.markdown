---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-05-08T01:51:16Z
slug: install-oracle-102-on-opensuse-103
tags:
- opensuse
- oracle
title: Install Oracle 10.2.01 on OpenSuSE 10.3
url: /2008/05/08/install-oracle-102-on-opensuse-103/
wordpress_id: 49203
---

![](http://www.railsonwave.com/assets/2007/9/5/oracle.jpg)<br /><br />A) Download 10201_database_linux32.zip from Oracle website.<br /><br />B) Download 10gR2_openSUSE102_introduction.pdf and ora.rpm from ftp ftp.novelŀcom<br /><br />C) Install Oracle, following quick steps:<br /><br />1. Install openSUSE 10.2 with "C/C++ Development" selection.<br />2. Download and Install orarun package.<br />3. Enable and set password for newly created user oracle by orarun.<br />4. Set updated kernel parameters by executing /etc/init.d/oracle start.<br />5. Download and unzip Oracle 10gR2 Database SW.<br />Edit file database/install/oraparam.ini to add "SuSE-10" to line #39.<br />6. login as user oracle and run Oracle Universal Installer "database/runInstaller".<br /><br />**Troubleshooting:**<br /><br />1) installer error:<br /><br />---------------------------------------------------------------------------------------------<br /><br />oracle@Martin:~/database> ./runInstaller<br />Starting Oracle Universal Installer...<br /><br />Checking installer requirements...<br /><br />Checking operating system version: must be redhat-3, SuSE-9, redhat-4, UnitedLinux-1.0, asianux-1, asianux-2 or SuSE-10<br />Passed<br /><br />All installer requirements met.<br /><br />Preparing to launch Oracle Universal Installer from /tmp/OraInstall2008-05-08_09-11-56AM. Please wait ...oracle@Martin:~/database> java: xcb_xlib.c:52: xcb_xlib_unlock: Assertion `c->xlib.lock' failed.<br /><br />---------------------------------------------------------------------------------------------<br /><br />Solution :<br />

<br />	
  * export LIBXCB_ALLOW_SLOPPY_LOCK=1
<br />	
  * run runInstaller again
<br /><br />2) 在安装完成末期,需要root用户运行两个脚本，完了之后，我遇到一个错误对话框，点击过去之后好像没有发现安装失败，安装目前正常<br /><br />More SQL scripts:<br /><br />[http://cs-netlab-01.lynchburg.edu/courses/Oracle/SQLPlus.htm](http://cs-netlab-01.lynchburg.edu/courses/Oracle/SQLPlus.htm)<br /><br />SQL> CREATE TABLESPACE AMP<br />2  DATAFILE '/opt/oracle/oradata/orcl/AMP.dbf' SIZE 200M;<br /><br />Tablespace created.<br /><br />SQL> CREATE USER        AMP     IDENTIFIED BY ca1234<br />2  DEFAULT TABLESPACE AMP<br />3  QUOTA UNLIMITED ON AMP;<br /><br />User created.<br /><br />SQL> GRANT CONNECT, RESOURCE TO AMP;<br /><br />Grant succeeded.<br /><br />SQL> GRANT CREATE SESSION, CREATE TABLE TO AMP;<br /><br />Grant succeeded.<br /><br />**How to start oracle em manully?**<br /><br />可能出现的错误如下，没有ORACLE_SID的 环境变量, 可能网络地址和环境发生变化,比如主机名修改等.<br /><br />oracle@Martin:~/product/10.2/db_1/bin> ./emctl start dbconsole<br />TZ set to PRC<br />EM Configuration issue. /opt/oracle/product/10.2/db_1/localhost_orcl not found.<br /><br />oracle@Martin:~/product/10.2/db_1/bin> ./emctl start dbconsole<br />TZ set to PRC<br />OC4J Configuration issue. /opt/oracle/product/10.2/db_1/oc4j/j2ee/OC4J_DBConsole_localhost_orcl not found.<br /><br />修正方式:<br /><br />oracle@Martin:~/product/10.2/db_1/oc4j/j2ee> cp -R  OC4J_DBConsole_Martin.bmc.com_orcl OC4J_DBConsole_localhost_orcl<br /><br />oracle@Martin:~/product/10.2/db_1> cp -R Martin.bmc.com_orcl/ localhost_orcl<br /><br />oracle@Martin:~/product/10.2/db_1> bin/emctl start dbconsole<br />TZ set to PRC<br />Oracle Enterprise Manager 10g Database Control Release 10.2.0.1.0<br />Copyright (c) 1996, 2005 Oracle Corporation.  All rights reserved.<br />http://Martin.bmc.com:1158/em/console/aboutApplication<br />Starting Oracle Enterprise Manager 10g Database Control ............................ started.<br />------------------------------------------------------------------<br />Logs are generated in directory /opt/oracle/product/10.2/db_1/localhost_orcl/sysman/log<br /><br />启动了后访问: http://localhost:1158/em/<br /><br />**手工启动Oracle实例的方法**<br /><br />1) sqlplus<br /><br />sqlplus /nolog<br /><br />connect sys/manager as sysdba<br /><br />startup<br /><br />2) rcoracle<br /><br />需要修改如下几个文件：/etc/oraInst.loc  /etc/oratab /  /etc/sysconfig/oracle /opt/oracle/product/10.2/db_1/bin/dbstart /usr/sbin/rcoracle 修改这些文件中的路径等信息知道 rcoracle start 命令不出错为止。
