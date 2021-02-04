---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-05-24T02:15:27Z
slug: ganglia-install-and-configure
tags:
- cluster
- Ganglia
- grid
title: Ganglia install and configure
url: /2008/05/24/ganglia-install-and-configure/
wordpress_id: 49207
---

我准备安装的版本是ganglia-3.0.7 ， 参考的安装文档是[http://www.linuxsir.org/bbs/thread309837.html](http://www.linuxsir.org/bbs/thread309837.html)<br /><br />rpm的安装会比较省事。rpm安装都会很正常，不过在Suse下面需要注意一下两点：<br />

<br />	
  * gmond和gmated的启动脚本不是rpm包中默认装上的那个，那个脚本适用于redhat linux；下载源码编译之后在gmond/ gmated/的文件夹里有后缀为 .SuSE的哪两个文件才对。
<br />	
  * rpm吧gmated的web界面默认安装路径是/var/www/http/ ，SuSE下的apache的路径是 /srv/www/htdoc/；安装完后copy或者连接过来
<br /><br />配置：<br /><br />	
  * gmond.conf 更具我参考的安装文档产生这个文件的命令是 gmond -t > /etc/gmond.conf；rpm安装包中有这个文件，如果需要恢复到默认状态可以使用这个命令。
<br />	
  * gmated.conf 是服务器端的主要配置文件，详细阅读一下源码包中的那个html文件对这个文件的配置会有帮助
<br /><br />安装过程中出现的问题如下：在启动gmond的时候启动失败，debug一下可以看到下面的错误。<br /><br />sles:~ # gmond --debug=9<br />slurpfile() open() error on file /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq: No such file or directory<br />udp_recv_channel mcast_join=239.2.11.71 mcast_if=NULL port=8649 bind=239.2.11.71<br />Error creating multicast server mcast_join=239.2.11.71 port=8649 mcast_if=NULL family='inet4'. Exiting.<br /><br />在所有虚拟机（host-only 网络设置）上都遇到这个错误。一次一个NAT网络的虚机上正常<br /><br />至今觉得这是一个网络的问题，还没有想出正确的配置和解决方法。如果您有什么好建议请留言。
