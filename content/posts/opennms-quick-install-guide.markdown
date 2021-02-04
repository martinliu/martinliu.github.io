---
author: liuadmin
categories:
- OpenNMS
comments: true
date: 2009-01-11T02:33:12Z
slug: 161-1-opennms-quick-install-guide
tags:
- OpenNMS
- Yum
title: opennms 1.6.1-1 quick start guide
url: /2009/01/11/161-1-opennms-quick-install-guide/
wordpress_id: 49246
---

![](http://www.etproductions.com/images/start.jpg)<br /><br />本安装手册为纯命令版，如果有什么疑问清参考官方安装手册，或给本贴留言。<br /><br />[install yum on your Linux box]<br />选择任意Linux系统，安装上yum工具，在命令行测试 yum -v<br /><br />[testing internet connection with those two URL]<br />测试是否能上网，用浏览器分别打开这两个网址<br />

<br />	
  1. [http://www.martinliu.cn/2007/12/13/opennms-yum-install/](http://www.martinliu.cn/2007/12/13/opennms-yum-install/)
<br />	
  2. [http://yum.opennms.org/repofiles/](http://http://yum.opennms.org/repofiles/)
<br /><br />先别关闭这两个网页。<br /><br />[Install opennms   开始安装:<br /><br />	
  1. yum install yum-fastestmirror
<br />	
  2. rpm -Uvh http://yum.opennms.org/repofiles/opennms-repo-snapshot-rhel4.noarch.rpm
<br />	
  3. yum list opennms
<br />	
  4. yum install opennms
<br /><br />[ post-install and config]  开始配置：<br /><br />	
  1. export OPENNMS_HOME=/opt/opennms
<br />	
  2. vi /var/lib/pgsql/data/pg_hba.conf<br /><br />	
    1. 注释掉其中所有可用的行，加入下面三行<br />local   all     all     trust<br />host    all     all     127.0.0.1/32 trust<br />host    all     all     ::1/128 trust
<br /><br />
<br />	
  3. /sbin/service postgresql restart
<br />	
  4. /usr/java/jdk1.5.0_15/bin/java -version
<br />	
  5. $OPENNMS_HOME/bin/runjava -S  /usr/java/jdk1.5.0_15/bin/java
<br />	
  6. $OPENNMS_HOME/bin/install      -disU -l /usr/lib/jni:/usr/lib
<br /><br />[ startup opennms and login ]启动登录：<br /><br />	
  1. /etc/init.d/opennms start
<br />	
  2. http://localhost:8980/opennms
<br />	
  3. username and password are admin/admin
<br />	
  4. click Admin  / Add Interface, input a ipaddress and press Add button
<br /><br />OK， I have get oepnnms 1.6.1-1 installed on my home pc, I hope you good luck and have fun.
