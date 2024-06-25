+++
date = 2021-11-09T12:58:16+08:00
title = "删除Cisco交换机中的所有VLAN数据"
description = "收了一堆用于召回我的CCNA记忆的破烂，开始折腾一通网络技术。"
author = "Martin Liu"
categories = ["DevOps"]
tags = ["network", "运维"]
image = "img/cos/2021-11-09-bigstock-network-hub-and-patch-cables-12234593-1.jpeg"
slug = "delete-all-vlan-from-cisco-switch"
+++
最近在闲鱼上收了几台网络设备，其中有一台Cisco 3560X作为lab的核心交换机，其它一些都是用于练习网络运维。本文从清除老旧设备上的vlan开始，将会记录我在这些网络设备上的所有重要配置操作。

<!--more-->

## 网络设备的初始化

### Cisco 交换机

Cisco 3560 的初始化是非常容易和方便的，这是一台非常新的设备，拆机后，机箱内部都没有什么积累明显的灰尘。第一次开机的时候通过mini USB口的连线连接，登陆console后发现需要密码才能进入enable模式，然后不得不重置这个设备的所有配置。

* 在交换机开机的情况下，先用mini USB连接好电脑和交换机。
* 拔掉交换机的电源线
* 按住交换机前面板，左上角的mode按钮不放
* 插上交换机电源线
* 保持mode按钮10+秒以上
* 看着交换机正常启动，并且进入了快速配置模式
* 选择进入快速配置模式，或者选择no，进入正常无向导的手工配置模式

到此处为止，你就进入了一个无密码，几乎无配置的状态。虽然现在这是一台几乎空白配置的交换机。但是交换机的文件系统里还是有一个名为vlan.dat的数据文件。这个文件是之前这个交换机的管理员留下的。有了他的存在当你当你执行 ‘ show vlan brief ’ 命令的时候，这个数据文件中的vlan数据有近百行，滚动了半天，非常烦人。因此需要想办法将其删除。

#### 清除VLAN数据文件

参考文章：<https://www.networkstraining.com/deleting-the-vlan-database-from-a-cisco-switch/>

首先查看flash上有哪些文件，使用命令 `show flash`

```
sw-bj-01#show flash:

Directory of flash:/

   10  -rwx        4371   Jan 2 2006 23:55:34 +00:00  config.text
    2  -rwx    26945536  Aug 31 2018 10:01:56 +00:00  c3560e-universalk9-mz.152-4.E6.bin
    3  -rwx    26844160  Feb 28 2019 05:02:21 +00:00  c3560e-universalk9-mz.152-4.E7.bin
    4  -rwx           0  Mar 27 2019 18:36:06 +00:00  merge_config.txt
    5  -rwx        6168   Jan 2 2006 23:55:34 +00:00  multiple-fs
    6  -rwx        2915   Jan 2 2006 00:02:10 +00:00  config.old
    8  -rwx       27468  Mar 27 2019 18:36:05 +00:00  candidate_config.txt
    9  -rwx         736   Jan 2 2006 00:08:27 +00:00  vlan.dat
   11  -rwx        3835   Jan 2 2006 23:55:34 +00:00  private-config.text

57671680 bytes total (3395584 bytes free)
```

上面的命令结果中的倒数第二行就是用来保存vlan信息的文件。然后我们使用 `delete vlan.dat` 命令将其删除即可。然后使用 `copy running-config startup-config` 保存当前的战果。还可以使用 reload 重启一下交换机，再次登陆交换机之后使用 show vlan brief 命令校验当前的交换机上只有默认的6个vlan存在。

#### 启用 ssh 和 web 登陆

每次都适用console线连接并配置交换机？这样还是有点麻烦的，我们需要启用交换机的管理ip和ssh登陆这样以后就可以从网络配置了。以后就可以用Ansible之类的DevOps工具玩NetOps了。配置过程的主要命令如下：

1. 配置管理ip， 参考命令如下：

```
# ip default-gateway 192.168.101.1

# interface vlan 101
(config-if)# ip address 192.168.101.2 255.255.255.0
```

2. 主机名， 参考命令如下：

```
# config t
(config)# hostname myswitch
(config)# ip domain-name thegeekstuff.com
```

3. 创建 RSA 密钥，用于启用ssh登陆，参考命令如下

```
myswitch(config)# crypto key generate rsa
 The name for the keys will be: myswitch.thegeekstuff.com
 Choose the size of the key modulus in the range of 360 to 2048 for your
   General Purpose Keys. Choosing a key modulus greater than 512 may take
   a few minutes.

How many bits in the modulus [512]: 1024
 % Generating 1024 bit RSA keys, keys will be non-exportable...[OK]
```

4. 配置一些 Line VTY 和 console 的参数

```
# line vty 0 4
(config-line)# transport input ssh
(config-line)# login local
(config-line)# password mypassword
(config-line)# exit

# line console 0
(config-line)# logging synchronous
(config-line)# login local
```

5. 设置用户名和密码

```
myswitch# config t
Enter configuration commands, one per line.  End with CNTL/Z.
myswitch(config)# username myusername password mypassword
```

如果你还没有配置enable的密码可以参考下面的命令。

```
myswitch# enable secret myenablepassword
myswitch# service password-encryption
```

6. 校验 ssh 访问

使用命令如下：

```
myswitch# sh ip ssh
SSH Enabled - version 1.99
Authentication timeout: 120 secs; Authentication retries: 3
```

现在你可以用网络上的电脑测试ssh登陆这个交换机的ip了。

### Cisco 路由器

待完成

### Cisco 防火墙

待完成

---- 未完待续 ----
