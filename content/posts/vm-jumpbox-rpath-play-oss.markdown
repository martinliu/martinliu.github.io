---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-04-02T06:46:29Z
slug: vm-jumpbox-rpath-play-oss
tags:
- JumpBox
- OTRS
- rPath
- VMWare
title: 虚拟让你轻松玩开源
url: /2008/04/02/vm-jumpbox-rpath-play-oss/
wordpress_id: 49194
---

[![](http://www.martinliu.cn/wp-content/uploads/2008/04/homepage-promo.png)](http://www.martinliu.cn/wp-content/uploads/2008/04/homepage-promo.png)开源一般都是谁在玩？我觉得还是开发人员比较多，通常有开发背景的人才会比较轻松的去下载源代码，编译并运行。现在网上有很多能让您轻松搞定开源软件的方法，虚拟技术的发展使我们能更轻松的获取并运行开源的解决方案。向往糖果盒子中放巧克力一样容易。<br /><br />最近我收到了几个[OTRS](http://otrs.org)的新版发布的新闻邮件。先说说关于OTRS的一些新闻，2008-03-31发布了最新的一个版本 [OTRS 2.2.6 (Ipanema)](http://otrs.org/news/2008/otrs_2_2_6/)。这个版本是一个2.2.6的安全补丁修复版，修复了一些安全的bug，同时有提供了另外两种语言的支持：土耳其和越南语；当然OTRS是能够支持简繁体的中文的。而且关于语言方面的翻译对照表也是可以自行修改的，可以把流程当中的一些术语翻译成符合你企业实用习惯的名称。OTRS后台能支持非常多的数据库，包括Oracle，MS SQL等非开源数据库，它的核心程序是用Perl写的，这些程序运行在Apache web服务器上，客户端是用的纯web的方式，后台的管理提供Web和命令行两种方式。它的安装对于我来说不是很方便，安装文档中并没有写的很详细需要哪行Perl的包，apache上需要安装哪行Perl相关的东西；不过您对Perl非常熟练的话相信没有这个问题。导致的问题是我在安装了ORTS之后，它或者它的某些程序运行不了。<br /><br />总结一下体验开源软件可能的一些步骤：<br />

<br />	
  1. 安装某个版本的Linux
<br />	
  2. 下载开源软件的安装包或者源码，开发人员可能更多回去下载源码，编译安装
<br />	
  3. 寻找次软件相关的安装文档和攻略，一步一步的照做。
<br />	
  4. 配置系统来满足次软件的安装和运行条件
<br />	
  5. 管理和运行该软件需要的服务，例如MySQL，apache等
<br />	
  6. 运行该软件
<br />	
  7. 继续查看软件的使用文档，学更多内容，体验感兴趣的功能
<br /><br />在这一个过程中可能遇到的问题有：<br /><br />	
  * 痛苦与重新安装操作系统，往往系统中的一些包会缺少或者版本不符合安装需求，如果对Linux系统包管理不熟练的话这是最容易出现的问题。
<br />	
  * 痛苦与对底层支持应用的配置和管理，底层依赖的系统服务可能有数据库、web服务器或者应用服务器等；至今记得我第一次被迫在PostgreSQL中创建数据和用户的痛苦
<br />	
  * 有些OSS项目文档做的非常好，有些不好，那么安装和配置OSS的过程也可能会非常麻烦；毕竟很多配置文件的修改都需要手工修改配置文件
<br /><br />

<blockquote>那么如何清除体验OSS的拦路虎，轻松无痛体验OSS呢？</blockquote>

<br />应用虚拟技术可能是一个比较好的方式，目前我找到两个比较好的网站能提供OSS虚拟应用下载的，如下所示。<br /><br />![](http://www.rpath.com/conary-static//apps/mint/images/corplogo.gif)<br /><br />[http://www.rpath.com/rbuilder/](http://www.rpath.com/rbuilder/)<br /><br />![](http://www.jumpbox.com/sites/all/themes/jumpbox/logo-white.gif)<br /><br />[http://www.jumpbox.com/](http://www.jumpbox.com/)<br /><br />这两个网站的区别是：JumpBox是提供开源软件包下载和相关服务的，当然下载肯定是免费的；rPath不但提供下载而且能给你空间去攒一个你自己的虚拟应用。<br /><br />当然VWMare的网站也能提供这些虚拟应用的下载：[http://www.vmware.com/appliances/](http://www.vmware.com/appliances/)<br /><br />这里不想讨论虚拟技术的好处，不过它确实给体验和应用OSS带来很多方便。我第一次下载的虚拟应用是Zenoss，下载总共花了10分钟，下载的过程当中我在看Zenoss的文档，下载的虚拟机运行起来之后，我做的第一件事情就是运行自动发现网络设备的命令了。<br /><br />通过虚拟这个桥梁，更加节约了我们体验和应用OSS的时间。我想这应该是开源和虚拟共同给我们带来的好处，道理很简单如果你下载并且使用一份包含Windows操作系统的应用，而没有给MS交钱的话，那么你就是盗版使用Windows了。更没有人会给你免费安装配置一套商业应用软件。<br /><br />那么让我们从体验OTRS开始把，什么是OTRS请参考本博客中的文章。你可以从JumpBox下载并运行OTRS2.2.6，下载地址是：[http://downloads2.jumpbox.com/otrs-1.0.1.zip ](http://downloads2.jumpbox.com/otrs-1.0.1.zip)
