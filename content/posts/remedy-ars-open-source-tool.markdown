---
author: liuadmin
categories:
- BMC
comments: true
date: 2011-03-01T15:46:51Z
slug: remedy-ars-open-source-tool
tags:
- ARAPI
- ARS
- ARSperl
- BMC
- opensource
- php
- pyARS
- remedy
title: Remedy ARS 开源工具知多少
url: /2011/03/01/remedy-ars-open-source-tool/
wordpress_id: 50968
---

Remedy ARS是全球最大市场份额的产品，是为业内广泛接受的成熟产品套件；虽然他始终是私有的软件产品，但是围绕其周围，还是不断有新的开源工具出现。下面就介绍几种这样的软件。

ARInside is a  free open-source utility to create a static html documentation of your  AR-Server. If you need something to quickly browse through your workflow,  ARInside might be worth a try.
ARInside 3.0.2 has  some new features, lots of bugfixes and other  improvements.
Just to name a few:
- documentation improvements
- 64-bit platform support
- experimental support for Solaris and AIX
- basic ARS 7.6.x support
- huge performance plus on big installations

这是一个ARS服务器扫描的工具，可以形成一个静态的文档，能够作为一个状态的参考极限，这样方便你对当前的服务器上的所有对象和工作流有个全面的了解。最大的好处是能够统计和技术，而且不用登陆Dev Studio了。一图胜千言，下面大家看后就明白它能做什么。

![Front page of ARInside docs ](http://arinside.org/screenshots/1?format=raw)

看后还闲着干嘛，赶紧去下载使用吧。

其他的关于Remedy ARS 开源的项目我也在sf.net里面大致搜索了一下，下面是个简单的参考清单。


## [Remedy Outlook Integration](http://sourceforge.net/projects/roi/) Updated 2006-09-08


The Remedy Integration for Outlook (ROI) synchronizes tickets from any  Remedy AR System application to your Outlook task list or calendar.


## [Remedy ARAPI PHP extension](http://sourceforge.net/projects/php-arapi/) Updated 2009-07-19


Extension to PHP for integration to Remedy Action Request System. First  release will be focused on reading and manipulating data. Later version  will give access to arapi-application structure functions.


## [Jasper Reports data provider for Remedy](http://sourceforge.net/projects/jaspars/) Updated 2006-08-16


jaspars provides a Jasper Reports custom data source (JRDataSource)  compatible with the Remedy AR System. See  http://www.mypathworks.com/arslist/Public?id=8ae4b6940c259f32010c3707fbae01bf  for more information and usage instructions.


## [ARSperl](http://sourceforge.net/projects/arsperl/) Updated 2008-05-06


ARSperl is an integration kit for Perl5 and Remedy ARSystem API. It  provides a large subset of the functionality found in the ARS C API


## [AR Cache Purge](http://sourceforge.net/projects/arcachepurge/) Updated 2009-05-27


AR Cache Purge automates the process of clearing BMC Remedy user cache  on client machines. It first checks the registry for the Home folders(s)  and then removes the .arf and .arv files. It handles multiple users and  home folders on a single machine.


## [pyARS](http://sourceforge.net/projects/pyars/) Updated 2010-12-20


The pyARS python module allows developers to use BMC's ARSystem (Remedy  ARS) and Atrium CMDB functions from within Python. Using Python's  interactive shell, it is extremely easy to retrieve and modify data  entries as well as workflow objects.


## [COM Objects for the AR System](http://sourceforge.net/projects/coarse/) Updated 2006-01-10


Coarse (COM Objects for the AR System), provides an automation  compatible COM API to the AR System (Remedy only provides a C API and a  Java API).  It is compatible with VB6, VBA, VBScript, and JScript.   Based on the RTL Sourceforge project.


