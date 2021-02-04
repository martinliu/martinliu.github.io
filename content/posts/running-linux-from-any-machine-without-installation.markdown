---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-07-04T14:31:15Z
slug: running-linux-from-any-machine-without-installation
tags:
- linux
- slax
- usb
title: Running Linux from any machine without installation
url: /2008/07/04/running-linux-from-any-machine-without-installation/
wordpress_id: 49215
---

# [![http://www.slax.org/screenshot.php?s=3](http://www.slax.org/images/slax.png)](http://www.slax.org/screenshot.php?s=3)Slax - your pocket operating system

<br />

<blockquote><br />
> 
> Slax is a modern, portable, small and fast Linux operating system with a modular approach  and outstanding design. Despite its small size, Slax provides a wide collection  of pre-installed software for daily use, including a well organized graphical  user interface and useful recovery tools for system administrators.
> 
> <br />
> 
> The modular approach gives you the ability to include any other software  in Slax easily. If you're missing your favourite text editor, networking tool  or game, simply download a module with the software and copy it to Slax,  no need to install, no need to configure.
> 
> <br />
> 
> If you are a beginner or you're just too busy to make it yourself, follow  a few steps to build your own customized operating system by using web-based interface here.
> 
> <br /></blockquote>

<br />

**Slax How to**

<br /><br /><table cellpadding="5" cellspacing="0" border="0" width="100%" ><br /><tbody ><br /><tr ><br />
<td ><br />	
* [Key features of Slax 6](http://www.slax.org/documentation_key_features.php)
<br />	
* [Slax distribution - Slax for CD](http://www.slax.org/documentation_burn_slax.php)
<br />	
* [Slax distribution - Slax for USB](http://www.slax.org/documentation_install_slax.php)
<br />	
* [Verify if your downloaded was not corrupted](http://www.slax.org/documentation_verify_download.php)
<br />	
* [Running Slax from USB Flash keys](http://www.slax.org/documentation_usb_troubleshoot.php)
<br />	
* [Using boot parameters (cheatcodes) in Slax](http://www.slax.org/documentation_boot_cheatcodes.php)
<br />	
* [Understanding the persistent changes](http://www.slax.org/documentation_persistent_changes.php) [ not finished ]
<br />	
* [Using Slax modules](http://www.slax.org/documentation_use_modules.php)
<br />
</td><br /></tr><br /></tbody></table><br />Slax是一个USB Linux，安装它的方式很简单，[下载Slax](http://www.slax.org/get_slax.php)的tar文件到usb key。usb key最好是1GB以上，整个Slax大概六七百MB；usb key现在很便宜，建议买一个大的。如果你是在windows下面下载并安装这个东西，建议最好把usb key先格式化一下，别格式化成NTFS格式，我的usb第一次安装没成功，后来格式化一边在copy tar文件，解压缩后，运行那个安装文件，就是一个bat文件，它会把这个linux的启动菜单装到，usb的引导区。那个bat文件会一闪就停住，关闭窗口。安装就这个结束了，整个过程10分钟左右。推出windows，在笔记本电脑启动的时间，按F12，在系统启动菜单上选择从usb启动。很快slax的启动画面就显示出来了，在这个菜单中，我选择了copy slax to ram；这样它会把整个系统都装入内存运行；我的笔记本电脑有4G内存，所以我想充分利用这个资源提速。进入系统后，系统是一个KDE桌面非常熟悉。如果你想按照其他的程序的话，你可以到slax的网站上下载其他的模块，copy到那个制定的目录中，通过桌面里的模块管理工具或者命令行都可以激活新的应用，下面你就能在程序菜单中找到了。在slax的桌面系统中你可以直接访问到windows的分区，系统在启动时自动把windows的文件系统识别并且加载了。<br /><br />现在你拥有了随身携带的Linux系统了，把它放到包中随身携带吧：）
