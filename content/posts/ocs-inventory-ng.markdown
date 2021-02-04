---
author: liuadmin
categories:
- Asset Mgmt
comments: true
date: 2010-07-16T19:03:17Z
slug: ocs-inventory-ng
tags:
- GLPI
- linux
- OCSNG
title: OCS inventory NG 两三事
url: /2010/07/16/ocs-inventory-ng/
wordpress_id: 50670
---

![](http://www.ocsinventory-ng.org/uploads/images/why-ocs.png)头等大事是有关于OCSNG很快就要出UTF8多语言支持版的Windows采集代理程序。新闻如下：
** 新版windows采集代理被彻底重写，它将包括下面的新特性：**
- 全Unicode代理，多语言UTF-8支持
- Native 32 and 64 bits agent
- BIOS AssetTag 收集
- 硬盘序列号收集
- 部署返回码收集
- 全 HTTPS 支持
- Socks 4 、5 HTTP 代理支持
- FTP, FTPS 和SMB 包部署支持
- 二进制插件支持

另外，是一本新书的发布，这是我见到的第一本系统介绍OCSNG的图书。[![](https://www.packtpub.com/sites/default/files/imagecache/productview/1100_MockupCover_0.jpg)](http://www.packtpub.com/ocs-inventory-ng-1-02-it-inventory-and-resource-management/book?utm_source=martinliu.cn&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_003818)可能是由于我写过一些相关的post，该书的出版社发邮件给我，想请我review，并写写书评。处于对OCSNG和GLPI的喜爱，忍不住诱惑，就答应了。很快的我得到了这本书的电子版。虽然没有时间看完，浏览了几章后，还是可以说这本书写的是非常实用。特别是对系统的安装、配置、部署和使用都从系统管理员的角度写的非常到位。书上没什么废话，文字写的比较随意，很易懂的随意。可喜的是该书还捎带着把GLPI也给介绍了，包括如何与OCSNG做集成配置，以及GLPI的主要功能说明。对于这种偏门的开源软件系统能有如此细致使用的介绍实属难得，更何况我对OCSNG和GLPI的网站文档本身就不敢恭维。这里提供一个样章供参考 ["Introduction to IT Inventory and Resource Management"](https://www.packtpub.com/sites/default/files/1100-chapter-1-introduction-to-it-inventory-and-resource%20.pdf)

最后，还是期待新版OCSNG的Window采集代理程序能早点发布吧。期望它发布之时我有时间做这样一个虚机，以便分享给各位感兴趣的人。规划如下：



	
  * 基于Fedora 10

	
  * 安装OCSNG_UNIX_SERVER-1.3.2. + glpi-0.78-RC2

	
  * 做一定系统的基本优化，配置OCSNG和GPLI的集成

	
  * 期望该虚机能应用于实际的网络环境中


