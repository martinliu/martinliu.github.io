---
author: liuadmin
categories:
- ITSM
comments: true
date: 2007-12-27T02:12:00Z
slug: otrs
tags:
- ITIL
- ITSM
- OTRS
title: OTRS.ORG，it is time to check it out；不得不：）
url: /2007/12/27/otrs/
wordpress_id: 49177
---

一贯喜欢按照Google的指引在互联网上穿梭的你，是否发现了下面的这个现象。如果你搜索itil，无论选择所有网页、中文网页还是简体中文网页；你是否发现了在右边的赞助商连接中，OTRS.org总是能出现在第四个。OTRS.ORG是什么？和ITIL有什么关系？<br /><br />[![image](http://lh6.google.com/liuzh66/R3MJ_YClhPI/AAAAAAAAAJY/q27YWv9OFMs/image%5B7%5D.png)](http://lh6.google.com/liuzh66/R3MJ_YClhPI/AAAAAAAAAJY/q27YWv9OFMs/image%5B7%5D)<br /><br />热衷于开源ITSM的我不得不揭示这些答案。<br />

# 什么是OTRS

<br />这是一个开始于2001年的开源项目。OTRS是Open Ticket Request System的缩写。它的老家在[www.otrs.org](http://www.otrs.org)；下面是来自它首页的简介：<br />[![demo screenshot](http://otrs.org/images/screen-1.1/zoom-s.gif)](http://otrs.org/demo/)<br /><br />OTRS is an _O_pen source _T_icket _R_equest _S_ystem (also well known as _trouble ticket system_) with many features to manage customer telephone calls and e-mails. The system is built to allow your support, sales, pre-sales, billing, internal IT, helpdesk, etc. department to react quickly to inbound inquiries. Do you receive many e-mails and want to answer them with a team of agents? You're going to love the OTRS! It is distributed under the [GNU General Public License (GPL)](http://www.gnu.org/copyleft/gpl.txt) and tested on Linux, Solaris, AIX, FreeBSD, OpenBSD, Mac OS 10.x and Windows. The [((otrs))](http://www.otrs.de/) company provides commercial services (e.g. support, consulting, training, pre-build-systems, etc.) for the OTRS ([English](http://www.otrs.com/) and [German](http://www.otrs.de/)). Try our [demo system](http://otrs.org/demo/) to get an impression of this kind of magic.<br /><br />从这个简介中可以看出，这就是著名的‘问题单管理系统’；用来管理用户的电话或者邮件的请求。它能帮你的很快的受理各种问题和查询。比方说很多企业的IT支持部门，大多数都是工作在救火队模式下；对于期待问题解决的用户来说，也只能做到把奶喂给会哭的孩子；往往IT支持部门分身乏术，好像天天都处于缺奶的状态。对于IT支持或者运维部门的挂历者来说，他们也很难说出：我的员工很忙，都忙于什么事情。显然这是一种缺乏管理，缺乏流程的状态；不过要对这种局面进行管理，提高管理往往是非常难。最难的是在跨出第一步：记录，跟踪，处理所有问题。来自OTRS的问题：您是不是收到很多email（或者电话），并且希望通过一个支持团队回答？那么你将爱上OTRS!<br /><br />OTRS是一个在GPL许可证下被分发的软件，被在Linux, Solaris, AIX, FreeBSD, OpenBSD, Mac OS 10.x 和Windows下测设过。<br /><br />[((otrs))](http://www.otrs.de/) 公司提供OTRS的技术支持、咨询、培训、安装等商业服务。由于这个软件是德国人开发的，所以他们提供英语和德语的服务。<br /><br />我跟踪这个项目大概有一年左右的时间，亲眼目睹了它从一个普通的问题单管理系统变为一个兼容ITIL的服务台工具的过程。它从07年4月的它发布了第一个ITIL兼容的版本OTRS::ITSM 1.0 BETA2；这应该也是开源领域里的一个大事件吧，第一个像样的开源ITSM解决方案横空初始。按照它官方的声明，它做为OTRS的一个重要的插件（我是这么理解的，或者说是扩展模块）能支持ITIL中的事件管理、问题管理和配置管理/cmdb。<br />

# OTRS有哪些功能

<br />详细的功能描述在[http://otrs.org/feature/](http://otrs.org/feature/)<br />我简单总结以下几点：<br />

<br />	
  * 纯Web用户界面支持包括简体中文，繁体中文在内的10＋种语言，能够灵活定制界面，支持附件，支持单点登陆。
<br />	
  * 邮件接口，支持MIME附件，能自动回复，自动根据邮件头分派邮件，自动邮件提示用户Ticket状态的变化。
<br />	
  * Ticket功能，定义不同的受理队列，支持Ticket的锁定、回复、历史、优先级、受理时间计算、批量处理、等待等操作。支持全文检索，工作量和访问列表控制。
<br />	
  * 系统功能，按照日历时间计算SLA，提供LDAP和SQL数据库认证用户，自定义订单号格式，数据库支持MySQL, PostgeSQL, MaxDB/SAPDB, Oracle and DB2，前端和后台都支持UTF-8字符集
<br />	
  * 系统架构图 [http://otrs.org/images/BigPicture.gif](http://otrs.org/images/BigPicture.gif)
<br /><br />

# 如何使用OTRS

<br />下载和安装都非常简单，您可以参考它们的官方文档，文档非常详细，能看出德国人的细严谨的风格。下载网址： [http://otrs.org/download/](http://otrs.org/download/) 文档： [http://doc.otrs.org/2.2/en/html/](http://doc.otrs.org/2.2/en/html/) 安装说明：选择一个文档中支持的操作系统，建议Linux；如果是新手而且对Perl，apache和mysql不熟悉，建议直接选择完全安装；下载安装包，参考文档安装，使用。<br />

# 后记

<br />OTRS一个非常经典的项目，德国工艺，德国品质保证～～～Oops怎么听起来像是卖假木地板或者家具的广告呵呵！！个人非常喜欢此项目，相信您用了之后不会后悔；真的后悔了也别和我联系哈:-) have fun～～
