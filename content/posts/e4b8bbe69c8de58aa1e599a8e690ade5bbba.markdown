---
author: liuadmin
categories:
- opensource
- RHEL
comments: true
date: 2015-03-08T15:42:01Z
subtitle: 经过半年多的思考，终于看清了红帽整体的产品架构；经过无数的测试，经过了一个痛苦学习过程，终于可以讲讲红帽的技术架构了。下面将用一些列文章整理一下，我目前所消化吸收的部分。顺便也对这一段的工作做一个小节。先看看红帽的整体技术架构。
slug: '%e4%b8%bb%e6%9c%8d%e5%8a%a1%e5%99%a8%e6%90%ad%e5%bb%ba'
tags:
- KVM
- lab
- nfs
- ntp
- opensouce
- redhat
- satellite 6
- 订阅
title: Martin's lab 主服务器搭建
url: /2015/03/08/e4b8bbe69c8de58aa1e599a8e690ade5bbba/
wordpress_id: 53505
---

![Red-Hat-open-hybrid-cloud-1000x563_0](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/05/Red-Hat-open-hybrid-cloud-1000x563_0.png)

上图是红帽产品和技术架构的全貌。来源是：[http://www.redhat.com/en/technologies/cloud-computing](http://www.redhat.com/en/technologies/cloud-computing) 这张图我用在了我的首次给公司内部的全体销售培训上。由于我是IT管理背景的，因此我很习惯从云管理层往下看云引擎的各个层面。但是管理层产品，其实是后来整合纳入的。红帽起家的旗舰产品还是在底层的RHEL。总之，我想在一个Lab里面实现以上所有的部分，所谓实现是让其每个部分都能在运行在假象的一个有意义的业务场景里。还好，红帽的产品全都是基于x86平台的，因此我用几个笔记本，再加上我家里的这台HP MicroServer G8服务器应该能够全部部署出来。

做这样的一个lab还是要一定的规划和设计的，这些初步的规划和设计都在我的本子里手写的，就不在这里敲字了，随后我会抽空上几张图。


## 主服务器基本配置


硬件：Lenovo W540 CPU Intel i7, RAM 32 GB, SSD 512GB, HD 1TB

OS : RHEL 7.1

订阅是红帽公司的业务模式，也是红帽认为最自豪的部分，红帽相信可以成为开源技术和用户之间的催化剂，它不断参与最优秀的开源技术创新，并为其用户提供最强有利的技术服务和支持。红帽技术员工可以申请一个红帽雇员订阅。我的订阅可以在网上查到如下图所示：

[![employee-sub](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/employee-sub-520x295.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/employee-sub.png)

红帽的服务必须是基于订阅的每一个节点（物理、虚拟）都需要有有效的订阅，否则红帽的支持服务不能生效。对于一个已经成功注册到红帽官网，并且状态正常的服务器，应该显示如下的注册状态：

[bash]
[root@w540 ~]# subscription-manager list

+-------------------------------------------+
安装的产品状态
+-------------------------------------------+
产品名称： Red Hat Enterprise Linux Server
产品 ID： 69
版本： 7.0
构架： x86_64
状态： 已订阅
状态详情：
开始： 2014年09月09日
结束： 2015年12月08日
[/bash]

红帽员工订阅意味着所有红帽产品。


## 基本服务配置




### KVM


KVM的上手还真比我想象的速度要慢一些，起码比我用XenServer的经历更加纠结一些。总之现在可以彻底的忘记其它任何的选项，KVM可以满足我的所有需求了。由于主服务器有512SSD + 32GB RAM + 8 vCPU，所以我打算把产品里的所有管理控制节点VM都部署在这个机器上。预计有10个左右的虚拟机。
安装配置方面这里就不赘述了。只把困扰我许久的几个网络配置贴出来，供参考。

网桥0的功能是为所有虚拟机提供外网链接，使他们和主机一样直通主机所物理链接的局域网。
[bash]
[root@w540 ~]# cat /etc/sysconfig/network-scripts/ifcfg-br0
DEVICE=br0
ONBOOT=yes
TYPE=Bridge
BOOTPROTO=none
STP=on
DELAY=0
DNS1=192.168.0.1
DEFROUTE=yes
IPV4_FAILURE_FATAL=yes
IPV6INIT=no
DNS2=4.4.4.4
IPADDR=192.168.0.5
PREFIX=24
GATEWAY=192.168.0.1
NM_CONTROLLED=no
[/bash]

主机原本的一块物理网卡的配置，由于增加了这个网桥，需求更新如下：
[bash]
[root@w540 ~]# cat /etc/sysconfig/network-scripts/ifcfg-enp0s25
DEVICE=enp0s25
ONBOOT=yes
BRIDGE=br0
NM_CONTROLLED=no
BOOTPROTO=none
[/bash]

kvm这块处理这个折腾我很久的br0之外，其它的功能看起来还不错，运行在SSD上的虚拟机也启动和运行速度飞快。


### Repo 服务器


Repos是红帽软件仓库的简称。它具体指每个订阅内所有软件频道里面下载出来的软件包目录。下载到的某个软件包频道的repos目录中是一堆的rpm包文件，这样的目录可以制作成本地Repos服务器，能够提供给所有LAN里RHEL OS用来做软件的安装和升级用。
用主服务器上1TB的慢速普通盘来保存这些下载的repos，安装http服务器，把它共享给本lab的lan中。具体的几个参考脚本如下。

在把本服务器注册到红帽网站之后，他会默认attach一堆可能不需要的repos，因此我的做法是先关闭掉所有的默认开启，然后再开启我所需要并且关注的东西。
[bash]
[root@w540 repos]# subscription-manager repos --disable="*"
[/bash]
以上命令的结果会反问，所有的被关闭的repos。下面许开启我当前需求的repos。
[bash]
[root@w540 repos]# cat rhel7-enable.sh
subscription-manager repos --enable=rhel-7-server-extras-rpms
subscription-manager repos --enable=rhel-7-server-satellite-capsule-optional-6.0-rpms
subscription-manager repos --enable=rhel-ha-for-rhel-7-server-rpms
subscription-manager repos --enable=jb-eap-6-for-rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-satellite-capsule-6.1-rpms
subscription-manager repos --enable=rhel-7-server-rt-rpms
subscription-manager repos --enable=rhel-7-server-openstack-6.0-rpms
subscription-manager repos --enable=rhel-server-rhscl-7-rpms
subscription-manager repos --enable=rhel-7-server-rhn-tools-rpms
subscription-manager repos --enable=rhel-7-server-satellite-capsule-6.0-rpms
subscription-manager repos --enable=rhel-7-server-openstack-5.0-rpms
subscription-manager repos --enable=rhel-7-server-rhevh-rpms
subscription-manager repos --enable=rhel-atomic-host-rpms
subscription-manager repos --enable=rhel-rs-for-rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-satellite-capsule-optional-6.1-rpms
subscription-manager repos --enable=rhel-7-server-rhev-mgmt-agent-rpms
subscription-manager repos --enable=rhel-7-server-openstack-6.0-installer-rpms
subscription-manager repos --enable=rhel-7-server-rh-common-rpms
subscription-manager repos --enable=jb-eap-6.3-for-rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-satellite-optional-6.0-rpms
subscription-manager repos --enable=rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-satellite-6.1-rpms
subscription-manager repos --enable=rhel-7-server-supplementary-rpms
subscription-manager repos --enable=rhel-7-server-satellite-optional-6.1-rpms
subscription-manager repos --enable=rhel-7-server-optional-rpms
subscription-manager repos --enable=rhel-7-server-satellite-6.0-rpms
subscription-manager repos --enable=jb-ews-2-for-rhel-7-server-rpms
[/bash]

接下来可以用命令来从红帽CDN同步下载每个Repos里面的软件包。
[bash]
[root@w540 rhel70]# cat sync.sh
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-satellite-6.0-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-extras-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-rhevh-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-satellite-capsule-6.0-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-openstack-5.0-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-rhev-mgmt-agent-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-atomic-host-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-optional-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-rs-for-rhel-7-server-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-rh-common-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-server-rhscl-7-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-openstack-6.0-installer-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-openstack-6.0-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=jb-eap-6.3-for-rhel-7-server-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-ha-for-rhel-7-server-rpms --download_path=/data/Repos/rhel70/
reposync --gpgcheck --newest-only --plugins --downloadcomps --repoid=rhel-7-server-supplementary-rpms --download_path=/data/Repos/rhel70/
[/bash]

安装httpd的过程就不叙述了，下面就贴一个本机的配置文件。
[bash]
Alias /repos "/data/repos"
<Directory "/data/repos">
Options None
AllowOverride None
Order allow,deny
Allow from all
Require all granted

[/bash]

最后，在任何需要的机器上本地repos源的配置文件可以类似如下：
[bash]
[root@sat6-leb yum.repos.d]# ls
rhel70.repo
[root@sat6-leb yum.repos.d]# cat rhel70.repo
[rhel-7-server-rpms]
name=rhel-7-server-rpms
baseurl=http://192.168.0.5/repos/rhel70/rhel-7-server-rpms/
gpgcheck=0
enable=1

[/bash]

当然，我的目标是以后这个lab网内所有的机器都需要受到satellite 6 服务器的管理和控制，并不需要在每个服务器上手动的去安装和管理repos内容和订阅。下面分阶段安装各种控制器节点的时候，在详细说明如何使用satellite 6做种子服务器生出所有的其他节点。这里的repo服务器还是作为最初的种子服务器，它使安装satellite 6 服务器的源。也是作为lab中对于satellite6的一个备份选项。


### NFS服务器


本机的存储空间比较大，可以作为慢速NFS共享存储和ISO镜像文件服务器使用，因此，安装nfs服务器之后，就可以把本地的满速普通硬盘使用nfs的方式共享到lab内网了。配置文件参考如下：
[bash]
[root@w540 ~]# cat /etc/exports
/data/nfs 192.168.0.*(rw,async)
/data/iso 192.168.0.*(rw,async)
/home/test 192.168.0.*(rw,async)
[root@w540 ~]# showmount -e localhost
Export list for localhost:
/home/test 192.168.0.*
/data/iso 192.168.0.*
/data/nfs 192.168.0.*
[root@w540 ~]#
[/bash]


### NTP服务器


根据红帽知识库文档，选择本机这个物理服务器作为lab内网的时钟服务器，所有的虚拟机和其他物理机都和他同步时钟。最终的配置还没有确定。随后更新靠谱的可以供参考的配置
