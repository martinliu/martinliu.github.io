---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-12-13T10:14:00Z
slug: opennms-yum-install
tags:
- OpenNMS
- Yum
title: OpenNMS的Yum的安装方式，安装简单了很多
url: /2007/12/13/opennms-yum-install/
wordpress_id: 49172
---

OpenNMS网站的安装文档：<br />[http://www.opennms.org/index.php/Installation:Yum](http://www.opennms.org/index.php/Installation:Yum)<br />

下面是我在一个CentOS4的机器上按照上面文档安装的。

<br /><br />

<br />
  1. 先浏览一下这个页面      [http://yum.opennms.org/repofiles/](http://yum.opennms.org/repofiles/)      找到适合你的OS的那一行。
<br />
  2. 我选择安装的是1.3.10-0.8030.snapshot 这是当前开发的最新版本的OpenNMS； 运行命令： rpm -Uvh [http://yum.opennms.org/repofiles/opennms-repo-snapshot-rhel4.noarch.rpm](http://yum.opennms.org/repofiles/opennms-repo-snapshot-rhel4.noarch.rpm)
<br />
  3. 检查是否安装成功，      运行命令： yum list opennms ；我能看到如下输出结果
<br /><br />

[root@jng-hkg-48-dyn3328831 ~]# yum list opennms

<br />

Repository opennms-stable-common is listed more than once in the configuration

<br />

Repository opennms-stable-rhel4 is listed more than once in the configuration

<br />

Setting up repositories

<br />

Reading repository metadata in from local files

<br />

Available Packages

<br />

opennms.noarch                           1.3.10-0.8030.snapshot opennms-snapshot

<br />

<br /><br />

<br />
  4. 安装这个版本的OpenNMS，运行命令： yum install opennms      ; yum会处理包的依赖关系，把需要安装的包都从网络下载并安装上，所以我按y键开始安装，根据网络快慢的情况不同，您需要等待～～
<br /><br />

Dependencies Resolved

<br />

=============================================================================

<br />

Package                 Arch       Version          Repository        Size

<br />

=============================================================================

<br />

Installing:

<br />

opennms                 noarch     1.3.10-0.8030.snapshot  opennms-snapshot-common  5.0 k

<br />

Installing for dependencies:

<br />

iplike                  i386       1.0.6-1          opennms-snapshot-rhel4   10 k

<br />

jdk                     i586       2000:1.5.0_13-fcs  opennms-snapshot-common   46 M

<br />

jicmp                   i386       1.0.4-1          opennms-snapshot-rhel4   43 k

<br />

opennms-core            noarch     1.3.10-0.8030.snapshot  opennms-snapshot-common   47 M

<br />

opennms-webapp-jetty    noarch     1.3.10-0.8030.snapshot  opennms-snapshot-common   27 M

<br />

postgresql              i386       7.4.17-1.RHEL4.1  update            2.0 M

<br />

postgresql-server       i386       7.4.17-1.RHEL4.1  update            3.0 M

<br />

Transaction Summary

<br />

=============================================================================

<br />

Install      8 Package(s)

<br />

Update       0 Package(s)

<br />

Remove       0 Package(s)

<br />

Total download size: 125 M

<br />

Is this ok [y/N]: y

<br /><br />

<br />
  5. 建立/opt/opennms目录；导出到环境变量 export OPENNMS_HOME=/opt/opennms
<br />
  6. 配置数据库；启动数据库，第一次启动之后才能得到相关的配置文件； 运行命令： /sbin/service postgresql start
<br />
  7. 修改/var/lib/pgsql/data/pg_hba.conf      文件；内容如下。
<br /><br />

local   all         all                               trust

<br />

host    all         all         127.0.0.1/32          trust

<br />

host    all         all         ::1/128               trust

<br /><br />

<br />
  8. 修改 /var/lib/pgsql/data/postgresql.conf文件；内容如下
<br /><br />

tcpip_socket = true

<br />

isten_addresses = 'localhost' (这一行加入了好些数据库启动不了了，去掉就行了，不知原因)

<br /><br />

<br />
  9. 重新启动数据库服务；运行命令： /sbin/service postgresql restart
<br />
  10. 告诉OpenNMS JDK在那里； 运行命令：$OPENNMS_HOME/bin/runjava      -S /usr/java/jdk1.5.0_13/bin/java
<br />
  11. 初始化OpenNMS的数据库；运行命令：$OPENNMS_HOME/bin/install      -disU -l /usr/lib/jni:/usr/lib
<br />
  12. 启动OpenNMS；运行命令：/etc/init.d/opennms start
<br />
  13. 访问OpenNMS； [http://ip:8980/opennms](http://ip:8980/opennms) 用户名和密码都是admin
<br />
  14. 进入管理部门，配置自动发现的ip范围，配置提示邮件。
<br />
  15. Enjoy      open source software, have fun.
<br />
