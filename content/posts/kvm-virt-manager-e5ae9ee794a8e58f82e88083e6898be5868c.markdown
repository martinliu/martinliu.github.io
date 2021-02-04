---
author: liuadmin
categories:
- opensource
comments: true
date: 2015-01-06T15:55:02Z
subtitle: Virt Manager 是一个不错的kvm虚拟机管理工具，能够方便地管理虚拟机。我的测试机目前已经完全转向RHEL7上跑KVM虚拟机，通过virt-manager去管理的方案。命令行常用操作指南（持续更新中）virt-manager主要操作还是在命令行比较高效，特别是下面的这些操作，在使用过程中，比较多用，用的多了感觉比GUI操作方式效率高多了。
slug: kvm-virt-manager-%e5%ae%9e%e7%94%a8%e5%8f%82%e8%80%83%e6%89%8b%e5%86%8c
tags:
- KVM
title: KVM Virt-Manager  实用参考手册
url: /2015/01/06/kvm-virt-manager-e5ae9ee794a8e58f82e88083e6898be5868c/
wordpress_id: 53367
---

# 关于 virt manager


Virt Manager 是一个不错的kvm虚拟机管理工具，能够方便地管理虚拟机。我的测试机目前已经完全转向RHEL7上跑KVM虚拟机，通过virt-manager去管理的方案。

[![topbar_logo](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/topbar_logo.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/topbar_logo.png)

安装virt-manager：yum install -y virt-* ； 装完之后重新启动机器即可使用。


# 建议初始配置


安装完后有几个环境的配置推荐可以做一下。

![点击New Volume](http://martinliu.cn/wp-content/gallery/virt-manager-kvm-1/Screenshot-from-2015-01-06-193413.png)

Storage Pool ： 一个默认的 + 两个自建的



	
  * Default ：这是virt-manager安装时默认创建的，它和操作系统在同一个卷上，我的测试机使用SSD卷，因此我所有虚拟机都会使用这个卷，这样速度比较快

	
  * hd ：这是测试机上普通磁盘的一个目录，目的是把那些不需要快速IO的虚拟机跑着这里，节省SSD的磁盘空间

	
  * iso ：这是普通磁盘上的iso文件目录，单独挂在这是为了，使用方便


![自建的内外1](http://martinliu.cn/wp-content/gallery/virt-manager-kvm-1/Screenshot-from-2015-01-06-210927.png)

虚拟网络 （一个默认+两个新建）



	
  * default ： 这个是安装了virt-manager + kvm 之后就有的，是用NAT的方式，带dhcp，默认虚拟机可以连接物理机所在的外围

	
  * virbr1/virbr2 ：是我根据自己的需要建立的，只能和host物理机通讯，无dhcp


我最近做OpenStack的实践，OpenStack需要最好隔离的几个网络跑不同的数据，因此virbr1/2正好符合OpenStack的测试需求。另外我在物理机的操作系统上搭建了yum源服务器，因此任何一个虚拟机都可以通过http访问我放在物理机上的repo目录，我只需要更新这些repos目录里面的rpm包的内容，我的lab环境中的所有虚拟机（不管是在何网络）都可以使用到最新的系统更新包和软件包了。这样大大提高了虚拟机里面软件测试的效率，所有虚拟机像是在本地安装rpm软件包一样，再也不需要联网下载，我只需要每周去公司联网同步一下这些目录即可。

有了以上配置之后，就可以高效工作了，效率感觉比vmware workstation要高，速度快稳定。下面是虚拟机创建的流程，里面有些我的推荐做法。

![](http://martinliu.cn/nextgen-attach_to_post/preview/id--53382)

本想看下，virt-install 的使用方式，感觉那个参数太多，容易敲错，还是界面比较容易上手，而且出错的机会不高。


# 命令行常用操作指南（持续更新中）


virt-manager主要操作还是在命令行比较高效，特别是下面的这些操作，在使用过程中，比较多用，用的多了感觉比GUI操作方式效率高多了。

virt-manager的命令行功能调用有两种方式：



	
  * 直接 virsh 回车 ，之后就进入了 virsh # 的一个专门的shell，help 就能看的里面支持的所有命令

	
  * 在普通shell下 直接 virsh <操作命令> <参数>，


这两个方式的调用没有差异，感觉全凭个人的操作习惯。

下面是一些常用的虚拟机管理功能命令参数和实例。

开启一个虚拟机


virsh # start server8-a







查看所有虚拟机(on and off)




virsh list --all







关闭一个虚拟机




virsh # shutdown server8-a










对一个虚拟机作一个快照




snapshot-create-as server8-a flat-os "before customization"










查看虚拟的所有快照




snapshot-list server8-a







返回到之前的一个snapshot




virsh # snapshot-revert  --domain server8-a flat-os







克隆一个虚拟机到新文件（用于模板的复制创建新vm，或者vm的备份）  
[root@w540 Desktop]# virt-clone -o rhel70-tmp -n rhel70-tmp-clone -f /data/vm/cloned-new-vm.img  
Cloning rhel7-tmp.img                                                                             | 195 GB  00:00:03       
Clone 'rhel70-tmp-clone' created successfully.
