---
author: liuadmin
categories:
- Linux
comments: true
date: 2015-06-07T16:35:05Z
subtitle: Katello是红帽 Satellite 6 的开源社区项目，是最近我主推的标准化运维自动化运维的底层技术平台。希望使用本文，你可以快速的进入Katello的功能评估的过程中。
slug: '%e5%9c%a8centos-7%e4%b8%8a%e5%ae%89%e8%a3%85%e9%83%a8%e7%bd%b2katello2-2'
tags:
- Candlepin
- centos
- Foreman
- katello
- Pulp
- puppet
title: 在CentOS 7上安装部署Katello2.2
url: /2015/06/07/e59ca8centos-7e4b88ae5ae89e8a385e983a8e7bdb2katello2-2/
wordpress_id: 53753
---

Katello的系统架构如下图：

![katello-arch-diagram](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/06/katello-arch-diagram.png)

Katell系统是一个复合型开源项目，是Pulp, Candlepin 和 Foreman的组合。Foreman默认使用Puppet作配置管理。

它的安装文档见官方手册：[http://www.katello.org/docs/2.2/installation/index.html](http://www.katello.org/docs/2.2/installation/index.html)

为了简化安装，请下在本站提供的CentOS7完美安装模板。使用它来创建一个虚拟机，6GB内存，2VCPU；网络上为了方便，请在virt-manger中新建如下所示的网络。

![QEMU-KVM Connection Details_006](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/06/QEMU-KVM-Connection-Details_006.png)

虚拟机启动之后，确保host能正常联网。启动刚才创建的虚拟机，配置好IP，ping 外网网站，确保它能正常联网即可。其它安装命令如下：

[bash]

yum -y localinstall http://fedorapeople.org/groups/katello/releases/yum/2.2/katello/RHEL/7Server/x86_64/katello-repos-latest.rpm
yum -y localinstall http://yum.theforeman.org/releases/1.8/el7/x86_64/foreman-release.rpm
yum -y localinstall http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
yum -y localinstall http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y install foreman-release-scl

yum -y install katello

katello-installer -v \
--foreman-admin-username admin \
--foreman-admin-password smartvm \
--capsule-dns true \
--capsule-dns-interface eth0 \
--capsule-dns-zone xenlab.com \
--capsule-dns-forwarders 192.168.10.1 \
--capsule-dns-reverse 10.168.192.in-addr.arpa \
--capsule-dhcp true \
--capsule-dhcp-interface eth0 \
--capsule-dhcp-range "192.168.10.100 192.168.10.240" \
--capsule-dhcp-gateway 192.168.10.1 \
--capsule-dhcp-nameservers 192.168.10.10 \
--capsule-tftp true \
--capsule-tftp-servername $(hostname) \
--capsule-puppet true \
--capsule-puppetca true



[/bash]

以上的安装命令如果成功，katello服务器将具有一下功能：



	
  1. Foreman 服务器：用于自动化网络安装linux系统

	
  2. Puppet Master服务器

	
  3. Repos管理服务器

	
  4. DNS，DHCP，PXE服务器




安装成功之后，使用默认的用户名和密码就可以登陆了。
