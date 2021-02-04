---
author: liuadmin
categories:
- Linux
comments: true
date: 2015-06-05T15:44:52Z
subtitle: CentOS7是最近似于 RHEL7的企业板Linux好处是不用多说的。在它上面做一些开原软件的测试是非常方便和稳定的。我可能会用它做后续的一些系列文档，先打个基础。希望它也能广泛地用于其它的KVM，OVirt和OpenStack的场景中。
slug: '%e5%ae%89%e8%a3%85%e5%ae%8c%e7%be%8e-centos7-%e8%99%9a%e6%8b%9f%e6%9c%ba%e6%a8%a1%e6%9d%bf'
tags:
- centos
- linux
- RHEL
title: 安装完美 CentOS7 虚拟机模板
url: /2015/06/05/e5ae89e8a385e5ae8ce7be8e-centos7-e8999ae68b9fe69cbae6a8a1e69dbf/
wordpress_id: 53738
---

## 初始化安装


下载最新版CentOS7 DVD 选择mini安装。


## 网络配置


安装过程中设置了静态网络地址，如下：

[bash]

[root@centos7-tmp ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth0
TYPE=Ethernet
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
NAME=eth0
DEVICE=eth0
ONBOOT=yes
DNS1=192.168.10.1
DOMAIN=xenlab.com
IPADDR=192.168.10.8
PREFIX=24
GATEWAY=192.168.10.1
UUID=5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03

[/bash]


## 软件包


Change log:



	
  1.  yum install wget [telnet](http://itgeeker.net/tag/telnet/) perl perl-devel net-tools kernel-devel 

	
  2. yum install vim-enhanced.x86_64

	
  3. yum -y install git

	
  4. yum install acpid

	
  5. yum install tree

	
  6. yum install ntp

	
  7. yum install unzip




## Repo 软件更新源


Change log:



	
  1. 初始化安装，添加了个几个国内的源

	
  2. 


rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm


	
  3. /etc/yum.repo/bk/dvd.repo ；这个是在用KVM虚拟机挂ISO文件光驱的时候用的，到时候 mount /dev/cdrom /media/dvd , 把该文件方的夫目录中即可使用iso文件中的repos

	
  4. 

当前的软件源如下：

[bash]

[root@centos7-tmp ~]# yum repolist
Loaded plugins: fastestmirror
Repository base is listed more than once in the configuration
Repository updates is listed more than once in the configuration
Repository extras is listed more than once in the configuration
Repository centosplus is listed more than once in the configuration
Loading mirror speeds from cached hostfile
* base: mirrors.163.com
* epel: mirrors.neusoft.edu.cn
* extras: mirrors.btte.net
* remi-safe: remi.kazukioishi.net
* updates: mirrors.btte.net
repo id                                 repo name                                                                          status
base/7/x86_64                           CentOS-7 - Base                                                                    8,652
epel/x86_64                             Extra Packages for Enterprise Linux 7 - x86_64                                     8,022
extras/7/x86_64                         CentOS-7 - Extras                                                                    128
remi-safe                               Safe Remi's RPM repository for Enterprise Linux 7 - x86_64                           123
updates/7/x86_64                        CentOS-7 - Updates                                                                   609
repolist: 17,534
[root@centos7-tmp ~]#

[/bash]




## 系统服务配置


Change log:



	
  1. 关闭SELinux

	
  2. 关闭 NetworkManager

	
  3. 关闭 FirewallD

	
  4. systemctl enable acpid.service

	
  5. 开启 truned-adm virtual-guest 服务模式

	
  6. systemctl enable ntpd


[bash]

[root@centos7-tmp tuned]# tuned-adm  list
Cannot talk to Tuned daemon via DBus.
Available profiles:
- balanced
- desktop
- latency-performance
- network-latency
- network-throughput
- powersave
- throughput-performance
- virtual-guest
- virtual-host
Cannot talk to Tuned daemon via DBus.
It seems that tuned daemon is not running, preset profile is not activated.
Preset profile: virtual-guest

[/bash]


## 模板文件封装


用sys-unconfig 关机。用 virt-sysprep,  virt-sparsify 去除不必要信息，压缩。

[bash]

[root@martin-fedora vm]# ll -h
total 12G
-rw-r--r--  1 qemu qemu  81G Jun  5 22:36 centos7-tmp.qcow2
-rw-r--r--  1 root root  81G Jun  5 22:34 centos7-tmp.qcow2.bk
-rw-r--r--  1 root root 2.9G Jun  5 07:56 rhel66-clone-1.qcow2
-rw-r--r--  1 root root 1.6G Jun  3 15:01 rhel66-clone.qcow2
-rw-r--r--  1 root root  81G Jun  3 13:03 rhel66.qcow2
-rw-r--r--. 1 root root  81G Jun  1 00:59 rhel71.qcow2
[root@martin-fedora vm]# export TMPDIR=/home/martin
[root@martin-fedora vm]# virt-sparsify --compress centos7-tmp.qcow2 centos7-tmp-v1.qcow2
Input disk virtual size = 85899345920 bytes (80.0G)
Create overlay file in /home/martin to protect source disk ...
Examine source disk ...
Fill free space in /dev/centos/root with zero ...
100% ⟦▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒⟧ 00:00
Clearing Linux swap on /dev/centos/swap ...
100% ⟦▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒⟧ 00:00
Fill free space in /dev/sda1 with zero ...
Fill free space in volgroup centos with zero ...
Copy to destination and make sparse ...

Sparsify operation completed with no errors.  Before deleting the old disk,
carefully check that the target disk boots and works correctly.
[root@martin-fedora vm]# ll -h
total 12G
-rw-r--r--  1 qemu qemu  81G Jun  5 22:36 centos7-tmp.qcow2
-rw-r--r--  1 root root  81G Jun  5 22:34 centos7-tmp.qcow2.bk
-rw-r--r--  1 root root 520M Jun  5 23:11 centos7-tmp-v1.qcow2
-rw-r--r--  1 root root 2.9G Jun  5 07:56 rhel66-clone-1.qcow2
-rw-r--r--  1 root root 1.6G Jun  3 15:01 rhel66-clone.qcow2
-rw-r--r--  1 root root  81G Jun  3 13:03 rhel66.qcow2
-rw-r--r--. 1 root root  81G Jun  1 00:59 rhel71.qcow2

[/bash]




## yum update -y





	
  * 2015-07-10 : Done yum updated. 删除了不需要的Kernel，安装了unzip, 修改启动过程为直接文字启动。

	
  * 2015-11.15: update kernel to 7.1, set old kernel 1: package-cleanup --oldkernels --count=1





## 使用方法


root 密码 martinliu.cn 开机后记得一定要先修改。

百度网盘下载地址 [su_button url="http://pan.baidu.com/s/1pJurap9" target="blank" style="stroked" size="6" icon="icon: codepen"]centos7-tmp-v7[/su_button]
