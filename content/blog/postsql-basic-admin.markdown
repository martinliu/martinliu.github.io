---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-04-03T08:25:44Z
slug: postsql-basic-admin
tags:
- PostgreSQL
title: PostgreSQL基本操作指南
url: /2008/04/03/postsql-basic-admin/
wordpress_id: 49195
---

**安装**<br /><br />我的安装环境是虚拟机下面安装的CentOS4.4；在安装的时候需要注意的是：在安装选择的时候PostgreSQL一共有十几个可选的包，把可能会用到的包都尽量选中，否则就要手工去安装了，手工解决包之间的依赖关系烦啊。从光盘上装的好处就是它自己帮你把用户和启动脚本建好了，安装后需要检查如下两个文件：1）/etc/init.d/postgresql是否存在；2）/etc/passwd里面有没有postgres用户。<br /><br />**启动数据库**<br /><br />第一次启动，用root用户登录，运行命令：[root@RBA init.d]# service postgresql start ；如果需要数据库在系统启动是就启动的话需要运行：<br />

<blockquote>[root@RBA init.d]# chkconfig postgresql on ；</blockquote>

<br />检查结果<br />

<blockquote>[root@RBA ~]# chkconfig --list postgresql<br />postgresql      0:off   1:off   2:on    3:on    4:on    5:on    6:off</blockquote>

<br />**数据库管理**<br /><br />先切到postgres用户  su postgres<br /><br />新建一个数据库 createdb amp<br /><br />新建一个超级用户，需要在shell下运行：<br />

<blockquote>bash-3.00$ createuser amp<br />Shall the new user be allowed to create databases? (y/n) y<br />Shall the new user be allowed to create more new users? (y/n) y</blockquote>

<br />链接到数据库之后，确认以下：<br />

<blockquote>amp=# \du<br />List of database users<br />User name | User ID |         Attributes<br />-----------+---------+----------------------------<br />amp       |     100 | superuser, create database<br />postgres  |       1 | superuser, create database<br />(2 rows)</blockquote>

<br />给用户加一个密码：<br />

<blockquote>amp=# ALTER USER amp with password 'amp';<br />ALTER USER</blockquote>

<br />**其他参考信息**<br />

<blockquote># Put your actual configuration here<br /># ----------------------------------<br />#<br /># CAUTION: The default configuration allows any local user to connect<br /># using any PostgreSQL user name, including the superuser, over either<br /># Unix-domain sockets or TCP/IP.  If you are on a multiple-user<br /># machine, the default configuration is probably too liberal for you.<br /># Change it to use something other than "trust" authentication.<br />#<br /># If you want to allow non-local connections, you need to add more<br /># "host" records.  Also, remember TCP/IP connections are only enabled<br /># if you enable "tcpip_socket" in postgresql.conf.<br /># TYPE  DATABASE    USER        IP-ADDRESS        IP-MASK           METHOD<br />#访问来源 数据库    用户        IP-地址           子网掩码          认证方式<br />local   typhoon     typhoon                                         md5<br />#对于来自本地的访问，数据库“typhoon”对用户“typhoon”采用“md5”加密口令认证<br />local   typhoon     all                                             reject<br />#对于来自本地的访问，数据库“typhoon”对上面没提到的所有用户无条件拒绝认证<br />host    typhoon     typhoon     255.255.255.255   127.0.0.1         md5<br />#对于来网络的访问，数据库“typhoon”对用户“typhoon”，如果提出访问的是本机，采用“md5”加密口令认证<br />host    typhoon     all         0.0.0.0           0.0.0.0           reject<br />#对于来网络的访问，数据库“typhoon”对上面没提到的所有用户，不管提出访问的哪台机器，也不管它来自哪个子网，无条件拒绝认证<br />local   all         all                                             md5<br />#对于来自本地的访问，上面没提到的数据库对上面没提到的所有用户采用“md5”加密口令认证<br />host    all         all         0.0.0.0           0.0.0.0           md5<br />#对于来网络的访问，数上面没提到的数据库对上面没提到的所有用户，不管提出访问的哪台机器，也不管它来自哪个子网，采用“md5”加密口令认证<br />########################################<br />#   Others are all denied   其他访问一概无条件拒绝<br />local   all         all                                             reject<br />host    all         all         0.0.0.0           0.0.0.0           teject<br />########################################<br />########################################<br />#   All denied permissed, not safe<br />#   对所有访问都信任，太不安全，被我禁止掉了，只作为参考<br />#local   all         all                                             trust<br />#host    all         all         0.0.0.0           0.0.0.0           trust<br />########################################<br />这些认证的规则是从上到下一条一条加载的，要注意的是，里面的“all”并不是真正意义上的“所有”，只是前面的规定中没有提到的那部分。个人感觉用“other”也许更恰当。<br />这样，最终的结果是：<br />所有用户都能通过加密口令访问“typhoon”以外的数据库，但是只有用户“typhoon”能以加密口令访问数据库“typhoon”。<br />操作篇<br />[客户端基本连接操作]====================<br />*查看PostgreSQL的系统表：<br />(摸索/查找中)<br />*终端登录：<br />psql -l[主机名/IP] -d[数据库名] -U[用户名]<br />*连接到另外一个数据库：<br />\c [数据库名]<br />*断开终端：<br />\q<br />========================================<br />[基本用户管理]==========================<br />*添加用户：<br />create user [用户名];<br />*修改用户密码：<br />alter user [用户名] with password [口令];<br />*删除用户：<br />drop user [用户名];<br />*查看用户信息：<br />(摸索/查找中)<br />========================================<br />[基本数据库操作]========================<br />*创建数据库：<br />create database [数据库名];<br />*查看数据库列表：<br />\d<br />*删除数据库：<br />drop database [数据库名];<br />*修改数据库的所有者：<br />(摸索/查找中)<br />========================================<br />[数据库内基本操作]======================<br />*给予某用户在某数据库创建表的授权：<br />(摸索/查找中)<br />*收回某用户在某数据库创建表的授权：<br />(摸索/查找中)<br />创建表：<br />create table ([字段名1] [类型1] <references 关联表名(关联的字段名)>,[字段名2] [类型2],......<,primary key (字段名m,字段名n,...)>);<br />*查看表名列表：<br />\d<br />*查看某个表的状况：<br />\d [表名]<br />*重命名一个表：<br />alter table [表名A] rename to [表名B];<br />*修改表的所有者：<br />(摸索/查找中)<br />*删除一个表：<br />drop table [表名];<br />========================================<br />[表内基本操作]==========================<br />*在已有的表里添加字段：<br />alter table [表名] add column [字段名] [类型];<br />*删除表中的字段：<br />alter table [表名] drop column [字段名];<br />*重命名一个字段：<br />alter table [表名] rename column [字段名A] to [字段名B];</blockquote>
