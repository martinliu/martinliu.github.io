---
author: liuadmin
categories:
- CloudStack
comments: true
date: 2013-09-03T08:25:46Z
subtitle: 迪斯尼是一个有魔力的组织，在它的电影里冤家可以变伙伴。甚至CloudStack和OpenStack两大私有云死对头来到迪斯尼这个神奇的地方也可以“在一起”。当迪斯尼决定建设自己的云计算基础设施时，与很多企业一样面临一个艰难的抉择，从众多云计算技术方案和产品中选择一条道路。如今的云计算市场规模已
  达数百亿美元，水已经很深，领头的是亚马逊这样的公共云巨头，以及亚马逊的对手们：Rackspace、Google、CloudStack、 Eucalyptus、OpenNebula等多种私有云和公共云技术与服务，每家都有绝活和独到之处。
slug: cloudstack-swift
tags:
- cloudstack
- openstack
- swift
title: CloudStack+Swift 我心中的黄金搭档
url: /2013/09/03/cloudstack-swift/
wordpress_id: 52563
---

迪斯尼是一个有魔力的组织，在它的电影里冤家可以变伙伴。甚至CloudStack和OpenStack两大私有云死对头来到迪斯尼这个神奇的地方也可以“在一起”。当迪斯尼决定建设自己的云计算基础设施时，与很多企业一样面临一个艰难的抉择，从众多云计算技术方案和产品中选择一条道路。如今的云计算市场规模已 达数百亿美元，水已经很深，领头的是亚马逊这样的公共云巨头，以及亚马逊的对手们：Rackspace、Google、CloudStack、 Eucalyptus、OpenNebula等多种私有云和公共云技术与服务，每家都有绝活和独到之处。<!--more-->

[![disney-cloudstack](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/09/disney-cloudstack.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/09/disney-cloudstack.png)

对于身价上千亿美元的娱乐和媒体巨头迪斯尼来说，业界可供选择的云计算路线太多，到底是走公共云、私有云、混合云还是多重云的路子？

迪斯尼的选择是走自己的路。（迪斯尼的系统架构师Lopez将9月9日在[CloudBeat](http://cloudbeat2013-intext.eventbrite.com/)上介绍其云计算建设经验。）

在概念验证阶段，迪斯尼更加青睐CloudStack，在私有云领域CloudStack吸引力很多大型用户，如Zynga和诺基亚都选择了 CloudStack。迪斯尼的系统架构师Lopez表示，相比OpenStack，CloudStack的部署和运行速度要快得多。迪斯尼可以在数天能 部署好CloudStack服务，而OpenStack则需要数周。当然，两大私有云服务部署周期相差如此之大的部分原因也与迪斯尼的特殊要求和原有技术 投资有关。

不管怎样，迪斯尼目前对CloudStack非常满意，但迪斯尼的团队希望在私有云中增加对象存储技术。这一次迪斯尼倾向使用OpenStack阵 营的对象存储工具——Swift。事实上，开源的OpenStack之所以如此流行，与大量参与者提供的丰富功能密不可分，Swift就是一个很好的例 子。

于是，迪斯尼的团队与Citrix合作，确保OpenStack的Swift技术能够与CloudStack搭建的私有云紧密集成。在迪斯尼这个神奇的地方，OpenStack和CloudStack之间的深沟裂隙被弥合了。

在迪斯尼的案例中，CIO能够参考的经验是：云计算的实施方案并非黑白分明，非此即彼，随着云计算服务商提供越来越多的相对独立的云计算功能，CIO们可以不受“站队”的局限，从不同阵营选择最好的云计算工具进行整合。


<blockquote>开源世界里面没有绝对的对手和敌人，只有融合和共荣 --Marti Liu</blockquote>




## How Disney built a giant cloud by bolting two together


下面这个文章值得读一下。
[http://venturebeat.com/2013/08/30/how-disney-built-a-giant-cloud-by-bolting-two-together/](http://venturebeat.com/2013/08/30/how-disney-built-a-giant-cloud-by-bolting-two-together/)


## 转帖：迪斯尼云计算之路选择CloudStack


[原文链接](http://www.ctocio.com/ccnews/13420.html)： 文章来自[IT经理网](http://www.ctocio.com)
