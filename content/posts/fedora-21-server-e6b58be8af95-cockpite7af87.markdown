---
author: liuadmin
categories:
- opensource
comments: true
date: 2015-01-27T16:22:18Z
subtitle: 从Cockpi的词义上看，它是飞机驾驶仓的意思。而且Fedora 21 server 默认就会安装这个组建。有了它领导再也不用担心你看不走飞机了。总体感觉这个功能非常简洁、实用，很期待早日能融入到RHEL7中来。
slug: fedora-21-server-%e6%b5%8b%e8%af%95-cockpit%e7%af%87
tags:
- cockpit
title: Fedora 21 Server测试 - Cockpit篇
url: /2015/01/27/fedora-21-server-e6b58be8af95-cockpite7af87/
wordpress_id: 53428
---

先上几张Fedora 21 server 安装的截图。

[gallery link="file" ids="53424,53425,53426,53427"]

新的配色还是不错的，重点看第三张图，虽然不全，已经基本上看出F21 服务器版的软件包了。

[![Screenshot from 2015-01-28 00:18:22](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/Screenshot-from-2015-01-28-001822-1024x686.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/Screenshot-from-2015-01-28-001822.png)

安装之后发现确实Cockpit的界面已经可以登陆了，是黑色的风格。

[![Screenshot from 2015-01-27 23:52:18](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/Screenshot-from-2015-01-27-235218-1024x625.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/01/Screenshot-from-2015-01-27-235218.png)

在继续安装和探索之前，我有装了一个默认选项的f21 server ，想通过这个节点的节目添加后统一管理。

[gallery columns="1" size="large" ids="53433,53434,53435,53436,53437,53438,53439,53440,53441,53442,53443,53444,53445,53446,53447,53448"]



我感觉有了这个工具，新手们可以轻松第完成大部分Linux系统的维护工作了。

如果你点击了启用 docker , eth0的网络配置会丢失，会被docker那走作网桥，给他的image用作网关。这个测试最好是虚拟机多网卡。
