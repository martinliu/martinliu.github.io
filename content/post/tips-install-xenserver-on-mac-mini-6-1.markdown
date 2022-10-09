---
author: Martin Liu
categories:
  - cloud
comments: true
date: 2013-02-21T09:24:38Z
slug: tips-install-xenserver-on-mac-mini-6-1
tags:
  - cloud
title: "TIPS install XenServer on Mac Mini 6.1 "
url: /2013/02/21/tips-install-xenserver-on-mac-mini-6-1/
wordpress_id: 52253
---

[caption id="attachment_52258" align="aligncenter" width="640"]![mac-mini-2012-with-XenServer](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/mac-mini-2012-vs-old-mac-mini.jpg) mac-mini-2012-with-XenServer[/caption]

今天尝试在 Mac Mini 上安装 XenServer，下面把经验共享一下。我遇到的问题有两个：

1. 网卡无法识别：使用默认安装盘安装，提示没有检测到网卡，安装无法继续

2. 网卡驱动植入失败：在按了 F9 加载驱动的时候，没有发现驱动程序，无法继续安装

3. 安装完毕之后，重启，屏幕上显示一个带问号的文件夹，一闪一闪无法正常启动 XenServer

经过一番折腾，发现这些点主意一下，应该就没有问题。

[caption id="attachment_52255" align="aligncenter" width="300"]![启动Macmini](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot-300x224.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot.jpg) 启动 Macmini[/caption]

在启动 Mac Mini 的时候，在“咚”的一声之前，就按住 ALT 键，否则没法出现上面的屏幕，我用的是 USB 盘启动，所以要选择右侧的图标。

[caption id="attachment_52256" align="aligncenter" width="300"]![进入menu.c32菜单](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot2-300x224.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot2.jpg) 进入 menu.c32 菜单[/caption]

我遵循前人的经验，乖乖到此来禁止 gpt；首先在这里要迅速输入 menu.c32，输入完了就过了，就必须重新关机，重启 mac mini。

[caption id="attachment_52257" align="aligncenter" width="300"]![输入disable-gpt参数](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot3-300x224.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/boot3.jpg) 输入 disable-gpt 参数[/caption]

进入这个屏幕了，要快速按 TAB 键，否则启动参数无法编辑，输入 disable-gpt 参数的机会就失去了。编辑启动参数的时候，把参数加载第二个---（三个短横线）前即可，上图我为了拍照在参数之前加了很多空格，其实这个参数和前后要至少一个空格就够了。

在进入安装的屏幕后，如果是 XenServer6.0.201 的源安装盘，还必须下载 tg3 的网卡驱动，并且用工具打入 iso 文件，这样安装的时候，就可以选择到加载网卡启动，否则 6.0.201 的安装盘即不自带此网卡驱动，也无法正常识别附加的驱动。网卡驱动下载地址为：[http://support.citrix.com/article/CTX135328](http://support.citrix.com/article/CTX135328)  要把加压后的 iso 文件，再次加压到对应的目录里才行，直接把解压后的几个文件放入目录，安装程序是无法识别到网卡驱动的。如果能正常识别的话，会出现选择框，让你选择  Broadcom tg3。如果是 XenServer6.1 的安装盘，就不需要折腾驱动了，原盘自带了 Broadcom tg3 网卡驱动。下面有两张截图，供必须要使用 XenServer 6.0.201 的人参考。

[caption id="attachment_52250" align="aligncenter" width="300"]![XenServer 6.0.201 with driver](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/xenserver6.1-300x215.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/xenserver6.1.jpg) XenServer 6.0.201 with driver[/caption]

[caption id="attachment_52251" align="aligncenter" width="300"]![xs-repository-list 实例](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/xs-repository-list-300x253.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/02/xs-repository-list.jpg) xs-repository-list 实例[/caption]

即使你不是安装 XenServer6.0.201，也推荐使用 UltraISO 来把 iso 文件写入一个 USB 盘来安装，因为 Mac Mini 没有光驱，而且这样不用刻盘，更加环保一点。

最后一个 Tips：这个可能是解决问题 3 的技巧，在安装的最后一个屏幕上，安装程序提示移除 Mac Mini 上的其他所有截至，然后点击回车完成安装。在这个屏幕上要识时务的把安装 U 盘从机器上拔除，然后点击回车来重启 Mac Mini。经过我的验证，拔出 U 盘后好像没有在遇到过闪烁文件夹的重启不了的问题。建议都使用自带 Broadcom tg3 网卡驱动的 6.1 来安装，否则 6.0.201 安装完成之后，一旦打了补丁，还需要下载 for 这个补丁的新版本的网卡驱动，在重新手工打上该驱动，否则网卡会起不起来。
