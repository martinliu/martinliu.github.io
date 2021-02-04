---
author: liuadmin
categories:
- Tools
comments: true
date: 2015-06-18T14:14:51Z
subtitle: icinga2是一个优秀的监控软件，它是2009年从nagios中分支出来的一个项目，经过重写的监控内核，目前已经从1版本发展到2，并且今天发布了2.3.5。它是在运环境中很好的监控选择，主要优势不光是自身的，更多的是社区的，nagios社区n多年来积累下来的大量监控插件。
slug: icinga2-%e7%9b%91%e6%8e%a7%e5%b7%a5%e5%85%b7%e8%af%84%e6%b5%8b
tags:
- icinga2
- monitor
- Nagios
title: icinga2 监控工具评测
url: /2015/06/18/icinga2-e79b91e68ea7e5b7a5e585b7e8af84e6b58b/
wordpress_id: 53788
---

本来想写一个安装手册，可是安装完成之后发现其实非常简单，最后就把题目改为评测了。本文也不是全面的评测文章，关于它的能力和功能，待后续了解的深入了在继续更新本文。


## icinga2 架构分析


请下载和查看这个icinga2官方的文档：[su_button url="http://pan.baidu.com/s/1qW3JkJE" target="blank" style="stroked" background="#cccc00" size="6" icon="icon: cubes"]下载点这里[/su_button]

[![Selection_001](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/06/Selection_001-1024x542.png)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/06/Selection_001.png)

为什么用icinga，原因如下：

[su_list icon="icon: eye"]



	
  * Nagios的架构不能扩展

	
  * 增加模块是比较困难的

	
  * 不是群集和分布式监控架构

	
  * 安全性相对糟糕

	
  * 配置功能有限


[/su_list]


## 安装配置


icinga2的安装可以说非常简洁，基本上配置好yum源，几条命令就装万了，而且就可以用了。只是在web界面选择和配置上稍微有点麻烦，它目前有三个可以安装配置的界面：classic, icinga-web, icinga-web2； classic太老了，不具有极其强烈的怀旧情节，就别碰了。建议生产环境中还是使用icinga-web；web2太新了，很多集成的项目的都还没有做好，还比较初级，功能不完善。





~~待续~~~~
