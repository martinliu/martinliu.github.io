---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-04-26T10:47:00Z
slug: opennms-install-sample
tags:
- OpenNMS
title: OpenNMS 安装说明－精简版
url: /2007/04/26/opennms-install-sample/
wordpress_id: 49148
---

**Per-install Checklist:**<br />

<br />	
  1. SuSE 10.1 Linux install CD
<br />	
  2. OpenNMS rpm packages for SuSE Linux
<br />	
  3. JDK 1.5 package
<br />	
  4. Tomcat 5.5.20 package
<br /><br />**Here we go:**<br />

<br />	
  * Insert install CD into Cd/Dvd rom
<br />	
  * Do SuSE Linux mini install
<br />	
  * Logon in OS, run 'yast firewall' to open 8080 tcp port on firewall
<br />	
  * upload all packages to /opt
<br />	
  * untar JDK
<br />	
  * untar Tomcat
<br />	
  * install postgresql through yast; run 'rcpostgresql start'
<br />	
  * Export some variables
<br /><br />_export JAVA_HOME=/opt/jdk1.5.0_09<br />export OPENNMS_HOME=/opt/opennms<br />export CATALINA_HOME=/opt/apache-tomcat-5.5.20<br />export PATH=$PATH:$JAVA_HOME/bin_<br />

<br />	
  * Test Java and Tomcat
<br /><br />_java -version<br />$CATALINA_HOME/bin/startup.sh_<br />

<br />	
  * Modify this file, vi /var/lib/pgsql/data/pg_hba.conf , then run 'rcpostgresql restart'
<br /><br />_#local  all    all             ident   sameuser<br />local all all trus<br />thost all all 127.0.0.1 255.255.255.255 trust<br />host all all ::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff trust_<br />

<br />	
  * install OpenNMS rpm packages; rpm -ivh xxx.rpm
<br />	
  * $OPENNMS_HOME/bin/runjava -s
<br />	
  * $OPENNMS_HOME/bin/install -dis
<br />	
  * $OPENNMS_HOME/bin/install -y -w $CATALINA_HOME/conf/Catalina/localhost
<br />	
  * restart Tomcat
<br />	
  * start OpenNMS; $OPENNMS_HOME/bin/opennms start
<br />	
  * Check opennms status; $OPENNMS_HOME/bin/opennms -v status
<br />	
  * login web console
<br /><br />以上仅仅是我一个偷懒的方法，可以比较快的部署运行OpenNMS。这种方式的好处如下：<br /><br />	
  1. Mini安装可以是最快的安装，总共只有几百MB就得到一个Linux操作系统
<br />	
  2. SuSE的包管理比较好用，配合一张安装DVD，几乎所有软件招之即来，不需要下载任何东西
<br />	
  3. Java和Tomcat的安装包是从以前的机器上直接把安装目录tar出来的，这也直接解压来用速度比较快。
<br /><br />这个安装方式的缺点：<br /><br />	
  1. 并不是最优的安装，没用设置服务的自动重启
<br />	
  2. 没用优化PostgreSQL
<br />	
  3. 没用优化Java和Tomcat；ONMS是java应用，性能可能会是个问题
<br />	
  4. 没用对ONMS做任何配置
<br /><br /><br />	
  * **Post-install Checklist:**<br />_Change Admin password for ONMS<br />customize ONMS per your requirements<br />optimize Tomcat/Postgresql/ONMS configuration_
<br />
