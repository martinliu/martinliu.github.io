---
author: liuadmin
categories:
- RHEL
comments: true
date: 2015-03-23T02:47:45Z
subtitle: 昨天晚上还不知道何谓zsh，自从看了一个如何增加Mac OS的工作效率的视频之后，开始折腾这个shell。后来还发现它可以安装和配置在Linux，而且效果基本是一样的。所谓要装13，就装的像一点把。入手zsh应该可以增加Demo的绚丽程度，不仅工作方便了，而且观众YY的空间更大了一点：）哈哈
slug: '%e5%85%a5%e6%89%8b-zsh-%e5%92%8c-oh-my-zsh'
tags:
- bash
- shell
- zsh
title: 入手 zsh 和 oh-my-zsh
url: /2015/03/23/e585a5e6898b-zsh-e5928c-oh-my-zsh/
wordpress_id: 53605
---

![zsh](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/zsh.gif)

安装zsh在任何系统上几乎都是差不多。Zsh 是一款功能强大的交互式 shell，与 Bash 相比，Zsh 下面几点表现令人印象深刻：

[wm_list bullet="icon-linux" class=""]



	
  * 自动补全

	
  * 拼写纠错

	
  * 定制性强

	
  * 美观的命令提示符（这点吸引力最大）


[/wm_list]

相信你安装之后，对上面几点会有更加真切的感受！

下面是RHEL 7 上的安装过程。

[bash]

[root@w540]~# yum install git
[root@w540]~# curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
[root@w540]~# cat .zshrc
# Path to your oh-my-zsh installation.
export ZSH=/root/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
#ZSH_THEME="robbyrussell"
ZSH_THEME="bira" # 后面的文字都省略，我就修改了这个文件的这一个参数，bira的提示符感觉比较新颖和实用
[root@w540]~# zsh
╭─root@w540 ~
╰─$ ls
anaconda-ks.cfg Desktop Documents Downloads initial-setup-ks.cfg ist Music Pictures Public Templates Videos
╭─root@w540 ~
╰─$
[/bash]

下面是装完之后的截图，以后我的测试机的默认shell应该都是这个样子了：）

[![rhel7-zsh-ohmyzsh](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/rhel7-zsh-ohmyzsh.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/rhel7-zsh-ohmyzsh.jpg)

zsh的功能还是比较强大的，然后再加上ohmyzsh这套配置参数文件和工具插件，shell下地工作效率应该可以提高了。下面是一下参考网站：

[wm_list bullet="icon-linux" class=""]



	
  * oh-my-zsh入手中文参考：[http://tuhaihe.com/2013/05/17/oh-my-zsh.html](http://tuhaihe.com/2013/05/17/oh-my-zsh.html)

	
  * oh-my-zsh 官网（作者认为这是他此生做的最有意义的一件事）：[http://ohmyz.sh/](http://ohmyz.sh/)

	
  * zsh 官网：[http://www.zsh.org/](http://www.zsh.org/)


[/wm_list]

Mac OS X用户则建议实用iTerm2来替换原声的terminal。下载item2在这里：[http://iterm2.com/](http://iterm2.com/)

[![iterm2-logo](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/iterm2-logo.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/03/iterm2-logo.jpg)
