---
author: Martin Liu
categories:
  - cloud-computing
comments: true
date: 2013-04-07T10:27:38Z
subtitle: WinXP在XenServer上显示"XenServer tools not installed"的解决办法
slug: xenserver-tools-not-installed
tags:
  - xenserver
title: 解决XenServer tools not installed
url: /2013/04/07/xenserver-tools-not-installed/
wordpress_id: 52311
---

[box color="orange" icon="flag"]
鸣谢：Michael Zhang 的经验分享，有需要的请收藏备用。
[/box]

刚刚搞定了 POC 环境中一个很诡异的问题。把过程写出来以供大家参考。建议可以把这个设置放到 POC 的实施手册中。
刚开始做 POC 时，我们安装了 XP 的模板，并且安装了同版本的 XenTools，此时 XenCenter 面板上显示虚机的 IP 地址没有问题。但是跑了一段时间后发现，所有的虚机的 IP 地址都显示不出来了，并且 XenCenter 面板上显示 XenServer tools not installed，虚机的内存信息，Disk IO 等信息，都没有显示：
[![xentools1](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools1.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools1.png)

[![xentools8](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools8.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools8.png)

后来重装了模板，重新发布了虚机，一切就 OK 了，此时我认为是原先的模板有问题，所以导致了这个 issue。
但是后来跑了几天，某台虚机又出现了类似的症状，此时我意识到应该不是模板的问题了。然后我就检查了这台虚机的 Service，发现：

[![xentools2](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools2.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools2.png)

这个 Service 就是 XenTool 的 Service，因为没有启动，所以导致了上述的问题。
但是当我用手工试图重启该 Service 的时候，系统报改 Service 启动时停止，没有给出任何原因。Windows Event Log 里也没看到任何报错。
后来上网查了下，原来是 Windows Event Log 的 Application 类的 log 满了以后，会导致该 Service 启动异常。
看了下 XP 的 Windows Event Log 的 Application 类日志的属性，默认只有 64K：

[![xentools3](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools3.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools3.png)

我把上面的日志文件大小阀值改成了 1024K，清空 Application 类的 log，重启上面的 Service, 成功，问题解决。

[![xentools5](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools5.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools5.png)
[![xentools6](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools6.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools6.png)

[![xentools7](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools7.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/04/xentools7.png)

上述类似的问题我记得也有兄弟曾经遇到过，发邮件出来问过，当时怀疑是 XenServer 跟 VDA 的时间不同步造成，现在感觉也许跟这个原因有关。

[box color="gray" icon="order-check"]
欢迎投稿，请发邮件到： liuzh66@gmail.com
[/box]
