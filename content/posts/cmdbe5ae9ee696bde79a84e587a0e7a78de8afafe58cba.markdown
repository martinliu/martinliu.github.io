---
author: liuadmin
categories:
- ITSM
comments: true
date: 2009-07-04T05:44:02Z
slug: cmdb%e5%ae%9e%e6%96%bd%e7%9a%84%e5%87%a0%e7%a7%8d%e8%af%af%e5%8c%ba
tags:
- cmdb
- cms
title: CMDB实施的几种误区
url: /2009/07/04/cmdbe5ae9ee696bde79a84e587a0e7a78de8afafe58cba/
wordpress_id: 49263
---

![itilv3model](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/266/26670/2008/11/itilv3model.jpg)<br /><br />上面是ITIL v3的定义，CMDB的定义和v2没有变化。可以看出CMDB是一个存储配置记录的数据库，非常多的用户一拍脑门“不就是一个数据库么！我们也可以自己开发一个的。”。这样的情况下，IT组织的不同部门都可能会各自立门户，开发自己的配置管理信息库；例如：资产管理、终端分发和管理、机房管理等等。数据重复、数据不一致、配置信息不对称；无法得到跨部门和系统的报告。所以V3提出了CMS系统，它是CMDB系统的下一代管理系统。CMS系统需要 具有对现有信息资料的兼容性，CMS的建立不能忘记过去；一定要集成已有配置信息。<br />[![](http://lh6.ggpht.com/_KU0istEHv9w/Sb5fe4XU89I/AAAAAAAABWA/gqfJomNUHhM/snap008.jpg)](http://lh6.ggpht.com/_KU0istEHv9w/Sb5fe4XU89I/AAAAAAAABWA/gqfJomNUHhM/snap008.jpg)错误一：配置信息是一个独立的配置管理系统，由专人负责数据的更新和维护，手工的管理和维护所有数据。<br /><br />[![](http://lh6.ggpht.com/_KU0istEHv9w/Sb5feqLlKaI/AAAAAAAABV4/rmdsoBoBuiA/snap007.jpg)](http://lh6.ggpht.com/_KU0istEHv9w/Sb5feqLlKaI/AAAAAAAABV4/rmdsoBoBuiA/snap007.jpg)错误二：最配置管理就是要做的细，我要管理到机房中的每一根网线，CI的属性需要设计的非常多，越细致越好。<br /><br />[![](http://lh6.ggpht.com/_KU0istEHv9w/Sb5feHYTZVI/AAAAAAAABVw/4Ns9PAPzrJw/snap006.jpg)](http://lh6.ggpht.com/_KU0istEHv9w/Sb5feHYTZVI/AAAAAAAABVw/4Ns9PAPzrJw/snap006.jpg)错误三：我们自己有开发人员，我们有CMDB的需求，那就开始做吧，先看法着看看，不就是一个数据的增删改查么！！<br /><br />配置管理或者说CMDB的建设可以说是目前，国内ITIL用户共同的瓶颈。ITIL项目中实施最多的三个流程是：Incident Management、Problem Management 和 Change Management。已经实施完毕以上三个流程的用户问的最多的一个问题是：一个故障单、问题单或者变更单一定要和CI想关联么？在解决处理的时候寻找目标CI或者根源CI是必须的么？<br /><br />如果ITIL是一种公共语言的话，那么Incident Management、Problem Management 和 Change Management等所有流程都是句式或者时态。而CI则是主语或者宾语，您觉得没有主语或者缺少宾语的句子，会传递怎么的信息呢？
