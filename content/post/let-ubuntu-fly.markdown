---
author: Martin Liu
categories:
  - opensource
comments: true
date: 2011-04-10T11:11:27Z
slug: let-ubuntu-fly
tags:
  - opensuse
  - Ubuntu
title: 让Ubuntu飞一会儿
url: /2011/04/10/let-ubuntu-fly/
wordpress_id: 51024
---

很久以前我一直使用的 rpm based Linux，原因很简单，我只要手握一张最新的 DVD，就可以走遍天下都不怕，特别是对 SuSE Linux 的 yast 很依赖，因为它可以帮我解决 rpm 包之间的依赖性。这样工作起来就很简单，基本上是搜索到软件包之后，点击安装既可以搞定所有的软件安装工作。

来到 Ubuntu 世界的我并不很满意，最近一次的 apt-get update，以失败告终，险些把家里的 PC 的一块硬盘给搞丢了，因为升级失败导致分区表失效了，Win 操作系统不认了。直接崩溃，好在那 Live Cd 模式进入还能勉强看得那个盘里的东西，恢复到移动硬盘，重新格式化该分区，才把文件恢复了。着实让我虚惊一场。

![](http://img3.cache.netease.com/www/logo/logo_png.png)我比较喜欢一些小的 LAMP 堆栈式安装的 Linux，如 TurnkeyLinux。安装可以在 10 分钟内搞定系统安装。今年家里的宽度升级到 2MB 了，因此带宽上逐渐能满足 Ubuntu 这种从网上升级的需求。下面就是找国内的升级的源了，进过几个月的使用，最近觉得在北京的联通固定宽带的用户，使用 163 的镜像站点速度还是不错的。再次感谢国内的这样的无私奉献的公司，使得在国内的开源用户可以更快更方便。废话说了一堆：）哈哈下面也就是这几条命了的事情。

第一步，当然要选择近水楼台的 163 了，来参考http://mirrors.163.com/.help/ubuntu.html 的帮助文档，根据你操作系统的版本，更新/etc/apt/sources.list 文件即可，之后你的 Ubuntu 就是从国内的较快的站点上下载包了

第二步，安装多线程 apt 下载加速工具 apt-fast

[bash]
root@lamp ~# apt-get install python-software-properties
root@lamp ~# add-apt-repository ppa:tldm217/tahutek.net
root@lamp ~# apt-get update
root@lamp ~# apt-get install apt-fast
root@lamp ~# apt-fast -v
apt 0.7.25.3ubuntu9.3 for i386 compiled on Sep  9 2010 22:22:02
Supported modules:
*Ver: Standard .deb
*Pkg:  Debian dpkg interface (Priority 30)
S.L: 'deb' Standard Debian binary tree
S.L: 'deb-src' Standard Debian source tree
Idx: Debian Source Index
Idx: Debian Package Index
Idx: Debian Translation Index
Idx: Debian dpkg status file
[/bash]

以后你在安装软件包就是用 apt-fast install 了，而不是 apt-get install，至于 apt-get 么，不管你用还是不用，它就在哪里~~~~
最后一步（可选），如果你还经常要以 cpan 的方式安装 perl 的包的话，那么 163 上不管你用还是不用，他就在哪里，你也可以选择 163 最为 perl 的安装源。安装步骤如下：

[bash]
root@lamp perl/CPAN# pwd
/etc/perl/CPAN
root@lamp perl/CPAN# cp Config.pm Config.pm.bk
root@lamp perl/CPAN# ls
Config.pm  Config.pm.bk  Config.pm~
root@lamp perl/CPAN# vi Config.pm
[/bash]

修改 Config.pm 文件中的 urllist 值，修改成如下即可：

```
'urllist' => [q[http://mirrors.163.com/cpan/]],
```

接下来就可以测试一下了：
[bash]
root@lamp perl/CPAN# cpan -i XML::Entities
[/bash]

如果你有其他让 Ubuntu 加速的方法，请留言：）
