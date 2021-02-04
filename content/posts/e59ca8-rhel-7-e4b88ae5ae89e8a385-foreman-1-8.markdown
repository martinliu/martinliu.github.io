---
author: liuadmin
categories:
- opensource
- RHEL
comments: true
date: 2015-06-16T16:25:34Z
subtitle: Foreman 是一个发展的越来越好的开源项目，具备很多成功开源项目的相同特质：简单强大的核心装机和自动化配置功能、开放的插件架构下已经开发出足够丰富的周边功能，资源池集成插件涵盖各种服务器虚拟化和云主机，配置自动化控制方面集成了puppet和salt等。本文简述了如何在RHEL7上安装最新版本的Foremen
  1.8.2
slug: '%e5%9c%a8-rhel-7-%e4%b8%8a%e5%ae%89%e8%a3%85-foreman-1-8'
tags:
- Foreman
- puppet
- RHEL
- Yum
title: 在 RHEL 7 上安装 Foreman 1.8
url: /2015/06/16/e59ca8-rhel-7-e4b88ae5ae89e8a385-foreman-1-8/
wordpress_id: 53779
---

首先安装RHEL7使用光盘安装最小化系统，安装完成之后，关闭防火墙和SELinux（为了测试方便），配置主机名为FQDN格式，如 fm1.8.xenlab.com； 加本机的主机名解析到/etc/hosts 文集中。之后注册到RHN。

[bash]

[root@fm18 ~]# subscription-manager register
[root@fm18 ~]# subscription-manager attach  --auto
[root@fm18 ~]# subscription-manager repos --disable="*"
[root@fm18 ~]# subscription-manager repos --enable=rhel-7-server-optional-rpms
[root@fm18 ~]# subscription-manager repos --enable=rhel-server-rhscl-7-rpms
[root@fm18 ~]# subscription-manager repos --enable=rhel-7-server-rpms
[root@fm18 ~]# rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
[root@fm18 ~]# yum -y install http://yum.theforeman.org/releases/1.8/el7/x86_64/foreman-release.rpm
[root@fm18 ~]# yum -y install http://ftp.sjtu.edu.cn/fedora/epel/epel-release-latest-7.noarch.rpm
[root@fm18 ~]# yum clean all
[root@fm18 ~]# yum makecache
[root@fm18 ~]# yum update -y
[root@fm18 ~]# reboot
[root@fm18 ~]# yum install foreman-installer

[/bash]

安装foreman-installer可能会出现的错误是ruby包依赖的问题，导致这个问题的原因可能有：网速太满导致的yum meta-data 失效，国外的epel源下载失败等。解决方法是：使用国内较快的epel源，在安装foreman-installer前，清除yum 缓存，重新建立yum原数据缓存。

我的测试机的yum 源配置如下：

[bash]

[root@fm18 yum.repos.d]# yum repolist
Loaded plugins: fastestmirror, product-id, subscription-manager
Loading mirror speeds from cached hostfile
* epel: mirrors.neusoft.edu.cn
repo id repo name status
epel/x86_64 Extra Packages for Enterprise Linux 7 - x86_64 8,076
foreman/x86_64 Foreman 1.8 379
foreman-plugins/x86_64 Foreman plugins 1.8 199
puppetlabs-deps/x86_64 Puppet Labs Dependencies El 7 - x86_64 17
puppetlabs-products/x86_64 Puppet Labs Products El 7 - x86_64 175
rhel-7-server-optional-rpms/7Server/x86_64 Red Hat Enterprise Linux 7 Server - Optional (RPMs) 5,832
rhel-7-server-rpms/7Server/x86_64 Red Hat Enterprise Linux 7 Server (RPMs) 7,036
rhel-server-rhscl-7-rpms/7Server/x86_64 Red Hat Software Collections RPMs for Red Hat Enterprise Linux 7 Server 3,596
repolist: 25,310
[root@fm18 yum.repos.d]# cat /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=https://fedoraproject.org/static/352C64E5.txt

mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
baseurl=http://ftp.sjtu.edu.cn/fedora/epel/7/$basearch/debug
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
baseurl=http://ftp.sjtu.edu.cn/fedora/epel/7/SRPMS
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1
[root@fm18 yum.repos.d]#

[/bash]

以上应该是安装foreman-installer宝过的攻略了。接下来该安装foreman的各个组建和插件了。使用 foreman-installer -i 发现是个不错的方法。还可以顺便了解一下当前foreman版本的各个主要功能项，如下所示：

[bash]

[root@fm18 yum.repos.d]# foreman-installer -i
Welcome to the Foreman installer!
---------------------------------

This wizard will gather all required information. You can change any parameter
to your needs.

Ready to start? (y/n) y

Main Config Menu
1. [✓] Configure foreman
2. [✓] Configure foreman_cli
3. [✗] Configure foreman_compute_ec2
4. [✗] Configure foreman_compute_gce
5. [✓] Configure foreman_compute_libvirt
6. [✗] Configure foreman_compute_openstack
7. [✓] Configure foreman_compute_ovirt
8. [✗] Configure foreman_compute_rackspace
9. [✗] Configure foreman_compute_vmware
10. [✓] Configure foreman_plugin_bootdisk
11. [✗] Configure foreman_plugin_chef
12. [✓] Configure foreman_plugin_default_hostgroup
13. [✗] Configure foreman_plugin_digitalocean
14. [✓] Configure foreman_plugin_discovery
15. [✗] Configure foreman_plugin_docker
16. [✗] Configure foreman_plugin_hooks
17. [✗] Configure foreman_plugin_openscap
18. [✗] Configure foreman_plugin_ovirt_provision
19. [✗] Configure foreman_plugin_puppetdb
20. [✗] Configure foreman_plugin_salt
21. [✓] Configure foreman_plugin_setup
22. [✓] Configure foreman_plugin_tasks
23. [✗] Configure foreman_plugin_templates
24. [✓] Configure foreman_proxy
25. [✗] Configure foreman_proxy_plugin_abrt
26. [✗] Configure foreman_proxy_plugin_chef
27. [✗] Configure foreman_proxy_plugin_openscap
28. [✗] Configure foreman_proxy_plugin_pulp
29. [✗] Configure foreman_proxy_plugin_salt
30. [✓] Configure puppet
31. Display current config
32. Save and run
33. Cancel run without Saving
Choose an option from the menu...

[root@fm18 yum.repos.d]# puppet agent --test
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Caching catalog for fm18.xenlab.com
Info: Applying configuration version '1434466089'
Notice: Finished catalog run in 0.21 seconds
[root@fm18 yum.repos.d]#

[/bash]

输入数字即可进入每个选项打开和关闭这个功能和服务，这个是对foreman的功能配置管理，不光是首次安装可以使用，以后的服务器功能变更也可以这么作，这个对我这样不感冒answerfile的人来说甚好。如果是首次安装，可以什么都不选择，来一个说装就装的默认安装也不错。安装完全成功之后，就会显示登陆网址和 管理与密码等信息。用初始的admin密码登陆后，修改密码，你的全新的foreman就安装成功了。注意在，运行foreman-installer过程中是需要联网的，安装过程会按照需求，下载所需要的组建包，例如数据库和web服务器等等其它必须的包。登陆后界面如下：

[gallery size="medium" link="file" ids="53781,53782,53783"]

接下来需要作配置自动化的测试了，我做了一个录像，通过一个简单的示例来说明，如何在foreman中测试pupput module。过程中我使用一个最简单的 /etc/motd 文件的配置的类。演示的内容涉及：

[su_list icon="icon: check-square"]



	
  * 安装puppet module 到生产环境中

	
  * 导入并且定制puppet 类的功能

	
  * 测试和验证puppet 类是否工作正常


[/su_list]

视频下载：[su_button url="http://pan.baidu.com/s/1ntpBXfN" target="blank" style="stroked" background="#cccccc" size="6" icon="icon: cloud-download"]下载在这里[/su_button]

本文参考文档：

	
  * [http://theforeman.org/manuals/1.8/index.htm](http://theforeman.org/manuals/1.8/index.htm)

	
  * [http://itgeeker.net/centos-7-epel-china-mirror-repository/](http://itgeeker.net/centos-7-epel-china-mirror-repository/)


