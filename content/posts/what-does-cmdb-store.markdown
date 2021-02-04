---
author: liuadmin
categories:
- CMS/CMDB
comments: true
date: 2009-10-05T15:21:24Z
slug: what-does-cmdb-store
tags:
- ci
- cmdb
- cms
- relationship
- 添加新标签
title: CMDB中存什么？
url: /2009/10/05/what-does-cmdb-store/
wordpress_id: 49393
---

[caption id="" align="alignnone" width="406" caption="dmtf.org"]![dmtf.org](http://www.dmtf.org/home/Computer_stoxx.JPG)[/caption]<br /><br />当然是配置项和它们之间的关系，即：CI 和  Relationship。  那么如何规划那些类型的CI和Relationship需要保存到CMDB中呢？可以参考的数据模型是DMTF的通用信息模型，它是以面相对象的方式来描述各类CI和关系。它是一个工具用来帮你对环境中的各种物理和逻辑的CI和关系进行分类，参考这个模型选择一些有用的类（广度），然后在参考它对每个类属性的描述（粒度）。这些类的选择只是一个初步的研究，每个CMDB厂商和工具对其实施和参考的力度都不同，也需要看您具体实施的是什么工具。例如：你需要描述银行基金业务系统，你可能选择的CI类包括：客户群、业务流程、业务活动、业务服务、IT服务、应用系统、应用、软件服务器、服务器、网络、存储等；关系包括：组件、依赖和影响。CI类和关系的选择也基本上遵循够用就好的原则；而且每个类对应的CI实例都需要有人负责管理维护，需遵循，谁负责、谁维护的原则保障其属性的精确性。对于整个CMDB来说如果存在没有Onwer的CI或者关系，如果它是由自动化配置发现工具来更新的；那么它可以存在，如果不是的话，它可能根本就不该存在。所以CMDB中保存的数据不是越多，越细越好；而是够用就好，能保证更新就好。由于数据根本就不是免费的，即使国内的人力成本低，也不应该雇用一帮专职更新CMDB的人。  综上所述：我们说明了CMDB中数据选取和存放的最基本原则和方法，在CMDB产品选型过程中需要着重考察产品的数据模型本身和其管理的能力，还包括其CI和关系的扩展和定制能力；包括数据类型的支持和界面定制的程度。那么CMDB中的CI和关系有该如何展现呢？这是CMDB系统的另外一个功能：可视化。下面是一个CI和关系展示的实例供参考：<br />[http://media-001.yo2cdn.com/wp-content/uploads/266/26670/2009/10/s1-4-blog.swf#swf&width=320&height=320]<br />[](http://martinliu.cn/2009/10/05/what-does-cmdb-store/s1-4-blog/)[全屏查看或者下载Flash文件](http://media-001.yo2cdn.com/wp-content/uploads/266/26670/2009/10/s1-4-blog.swf)<br />第一代的配置展示方式是，纯数据表格方式。第二代具有一种固定格式的图形展示方式，除了那几张视图外，别的需要单独开发。下一代的具有各种视图定制功能，并且支持关系和ci的过滤等等。
