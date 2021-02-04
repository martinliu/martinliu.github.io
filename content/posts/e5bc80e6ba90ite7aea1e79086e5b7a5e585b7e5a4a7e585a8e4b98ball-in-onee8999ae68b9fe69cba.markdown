---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-06-15T07:24:00Z
slug: '%e5%bc%80%e6%ba%90it%e7%ae%a1%e7%90%86%e5%b7%a5%e5%85%b7%e5%a4%a7%e5%85%a8%e4%b9%8ball-in-one%e8%99%9a%e6%8b%9f%e6%9c%ba'
title: 开源IT管理工具大全之All in one虚拟机
url: /2007/06/15/e5bc80e6ba90ite7aea1e79086e5b7a5e585b7e5a4a7e585a8e4b98ball-in-onee8999ae68b9fe69cba/
wordpress_id: 49164
---

我做开源工具测试时,90%以上是在VMWare虚拟机中实现的,本人比较懒一直没有学习Xen虚拟机的用法,等下次吧,一等要彻底开源是我的一个梦想呵呵!<br /><br />说说这个All in One虚拟机的想法,我只是想把所有的我熟悉的工具都安装和配置在一个虚拟机里,这样当有人需要给做Demo的时候,我可以很快的做一个分享.如果有朋友感兴趣的话,我可以刻盘他.总的来讲希望能分享一下我的学习成果给大家.<br /><br />第一步:安装虚拟机<br />这个虚拟机我不像使用很多的Snapshoot,我以前是这么做的,从一个基础的OS发出许多分支到不同的工具;这样做的缺点有二:1)特别占磁盘空间;2)不能同时访问多个系统.<br /><br />我选择的Linux是Open Suse Linux 10.2;Suse的包管理对我来说真的很方便,从安装DVD上用Yast可以方便安装各种软件,无须考虑包之间的依赖性问题.<br />我选择的是最小图形化系统安装,安装完之后,vmdk文件的大小好像是2GB多.<br /><br />接下来安装的是所有的必须的包,大致如下:Apache,Perl,MySQL,PostgreSQL,rddtool,net-snmp,php,gcc,Kernel-source(for vmware tools)...等安装完之后用chkconfig on 命令设置需要自动启动的服务;然后把apache等服务逐个启动一下验证是否工作正常.<br /><br />然后安装的是VMWare tools,这个好像也不是必须,不过还是装上比较好,方便虚拟机和host机共享文件.我的虚拟机的版本是5.5.3workstation版本.<br /><br />第二步:安装各种开源软件<br />下面可能会是一个很长的change log<br /><br />1. 安装OpenNMS 1.3.2 [安装方法](http://lzheng.blogspot.com/2007/05/install-opennms-132-on-opensuse-102.html) 设置了opennms的自动启动,还没有设置tomcat5.5.23的自动启动.<br /><br />2.安装Cacti **0.8.6j **[安装方法](http://lzheng.blogspot.com/2007/06/how-to-install-cacti-on-opensuse-102.html), 使用的poller.php,尝试安装cactid,安装失败,原因可能是OpenSuse10.2好像没有net-snmp lib包. 暂时不安装cactid<br /><br />3.安装OCSNG 1.0.1 [安装方法](http://lzheng.blogspot.com/2007/06/how-to-install-ocsng-101-on-opensuse.html)<br /><br />4.安装 hyperic-hq 3.0.4-389 [安装方法](http://lzheng.blogspot.com/2007/06/how-to-install-hyperic-hq-on-opensuse.html), 2007-6-21th<br /><br />5.安装 OTRS 2.2.1-1 安装方法很简单，执行rpm安装既可, 2007-7-28th<br /><br />
