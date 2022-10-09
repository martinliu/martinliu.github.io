---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-02-25T03:09:00Z
slug: nagios-nagvis
tags:
  - Nagios
  - nagvis
title: Nagios华丽的外衣NagVis
url: /2007/02/25/nagios-nagvis/
wordpress_id: 49141
---

如果你用过 Nagios 的话，它的 2D、3D Map 一定会给你留下一些印象；2D Map 的确能比较试用一点，不过看上去还是挺难看的。NagVis 就是看到了这一点，它力求能让各种状态信息表达的更炫，更好看；它可以说是 Nagios 的一个不错的插件，直接 copy 到 Nagios 的相关目录下，配置一下就行了。它的效果如下图所示：![](http://www.nagvis.org/lib/exe/fetch.php?w=250&h=&cache=cache&media=nagvis_mail_service.png)<br />说的在玄虚一点它可以是一个“业务流程管理视图”[CA Unicenter 中的名词，OpenView 里也有类似的概念]。其实就是把原子的监控对象：被监控节点和节点上的服务；和业务系统或者 IT 的逻辑关系相结合起来。例如：我的业务系统 A 的其中一个数据库服务器的数据库进程停了，这个可以影响到所有物理包含或者逻辑包含它的对象的状态。NagVis 试图用漂亮的图标来表达这些状态和关系，是管理者能看的更加直观。
