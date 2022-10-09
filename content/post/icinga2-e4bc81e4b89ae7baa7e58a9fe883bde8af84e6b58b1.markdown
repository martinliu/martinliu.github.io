---
author: Martin Liu
categories:
  - blog
comments: true
date: 2015-07-09T08:44:43Z
subtitle: 本评测从 icinga2 软件的功能使用和体验入手，详细验证了用户认证，权限管理，管理服务器的群集高可用和分布式部署架构。这些功能在企业用户中是普遍的需求。还涉及到了监控架构中，各个节点的通信加密的方式。
slug: icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1
tags:
  - icinga2
title: icinga2 企业级功能评测1
url: /2015/07/09/icinga2-e4bc81e4b89ae7baa7e58a9fe883bde8af84e6b58b1/
wordpress_id: 53828
---

## Icingaweb 2 用户权限管理

icingaweb 2 是诸多 GUI 中最新的一种，也有替代其它之前所有 GUI 的趋势，目前看还比较新，只有最基本的功能。登陆 Web 界面的用户，用户和组的信息可以使用自己的数据库存储或者配置文件存储，也可以使用外部的 LDAP 集成，使用 php-ldap 模块集成外部的 LDAP/MS AD 服务器。
具有完整的 RBAC 模式; User -> Group -> Role = Permission Set（操作 action） + monitoring/filter/objects(范围 scope)

[![Icinga Web - create group](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/Icinga-Web-create-group-1024x659.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-web-create-group/) [![Icinga Web - create role](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/Icinga-Web-create-role-1024x659.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-web-create-role/) [![Icinga Web - create user](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/Icinga-Web-create-user-1024x659.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-web-create-user/) [![Icinga Web - assign user to group](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/Icinga-Web-assign-user-to-group-1024x659.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-web-assign-user-to-group/)

## Icinga2 的联系人和联系人组

在 icinga2 服务器端，在配置文件中定义了组和用户，他们在 Web GUI 界面上叫做 Contacts / Contactgroups 。

[bash]
[root@icinga2-test conf.d]# cat users.conf
/\*\*

- The example user 'icingaadmin' and the example
- group 'icingaadmins'.
  \*/

object User "icingaadmin" {
import "generic-user"

display_name = "Icinga 2 Admin"
groups = [ "icingaadmins" ]

email = "martin@aws-faq.com"
}

object UserGroup "icingaadmins" {
display_name = "Icinga 2 Admin Group"
}
[/bash]

User / UserGruop 是 Icinga 出发通知的对象，定义在这个配置文件中，使用规则把他们和监控对象（host/service/等）关联起来，在通知规则中实现不同的通知策略。如发邮件等。

## Icinga2 的 HA 和分布式架构

[![icinga-cluster](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/icinga-cluster-1024x288.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-cluster/)

icinga2 的 Cluster 是通过多个运行的实例配置在一起的，有这样几个特性：实例之间使用 SSL 的加密通信；彼此之间是双向连接；用 Zone 来分隔不同租户的配置域；基于 Hash 的负载分配；系统的各种功能组件由 Cluster 来管理其分布。它可以实现某个节点宕机后的自动分布监控数据采集命令在其它节点上的执行。

[![icinga-zone](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2015/07/icinga-zone-1024x712.png)](http://martinliu.cn/icinga2-%e4%bc%81%e4%b8%9a%e7%ba%a7%e5%8a%9f%e8%83%bd%e8%af%84%e6%b5%8b1/icinga-zone/)

icinga2 Client 是远程执行的一种节点，它和 Cluster 中的所有节点形成群集，在数据中心的其它网段或者地点采集本地的监控状态数据，然后把结果传送回上级的 Cluster 群集节点。icinga2 可以通过配置向导完成远程 client/Satellite 卫星节点的配置。它们之间的通行是基于证书的 TLS 加密，这个证书可以借用 puppet 的证书。远程 Client/Satellite 节点可以运行在三种模式下：具有本地监控配置，没有本地监控配置，靠上级群集发送监控配置。

其它企业级功能在后续文章中继续评测，您可以通过下面的评论，来提出您所关注的待评测功能。
