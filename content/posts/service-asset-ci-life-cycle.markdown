---
author: liuadmin
categories:
- Asset Mgmt
- CMS/CMDB
comments: true
date: 2009-12-13T07:45:00Z
slug: service-asset-ci-life-cycle
tags:
- asset
- ci
- cmdb
- cms
- ITIL
- lifecycle
- sacm
- status
- v3
title: 资产CI的一生
url: /2009/12/13/service-asset-ci-life-cycle/
wordpress_id: 49570
---

在ITIL v3以后，配置管理进化为“服务资产和配置管理SACM”，换句话说，资产和配置管理不分家。两个流程应该是融合的。从微观上看资产管理设计到CI的所有生命周期状态，而这个服务资产在CMDB中出现的状态为整个生命周期中的一部分。<br />

![](http://www.butterfliesandart.com/Butterfly_Life_Cycle/Lifecycle3large.jpg)

<br /><br />最好能通过资产管理为统一入口，来完成对CMDB中资产的生命周期管理。例如：一台服务器在到货以后，完成资产入库后，就应该在CMDB中自动创建CI，在上架部署了软件后，有配置资产自动采集工具，采集回详细配置信息后，资产状态就自动变为“部署”，当在运行维护中服务器宕机或者维护时，在资产管理中也能看到更新的信息。下面是建议的服务资产的生命周期状态:<br /><table cellpadding="0" cellspacing="0" border="1" width="709" > <br /><tbody ><br /><tr ><br />
<td width="69" height="32" >编号
</td><br />
<td width="115" >状态名称
</td><br />
<td width="526" >状态描述
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >1
</td><br />
<td width="115" >到货
</td><br />
<td width="526" >表示为CI的物品在采购以后，被相关部门签收。
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >2
</td><br />
<td width="115" >组装
</td><br />
<td width="526" >设备的组件在被组装的过程中
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >3
</td><br />
<td width="115" >维护
</td><br />
<td width="526" >该设备处于宕机后的维护状态
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >4
</td><br />
<td width="115" >宕机
</td><br />
<td width="526" >该设备处于宕机状态，还未对其进行维护
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >5
</td><br />
<td width="115" >终止
</td><br />
<td width="526" >不在处于被部署的状态
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >6
</td><br />
<td width="115" >转移
</td><br />
<td width="526" >该设备正在被转移到其它的地点或者机房途中
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >7
</td><br />
<td width="115" >删除
</td><br />
<td width="526" >配置项被标记为删除状态
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >8
</td><br />
<td width="115" >库存
</td><br />
<td width="526" >设备处于库存中，还没有被部署
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >9
</td><br />
<td width="115" >借出
</td><br />
<td width="526" >已被其他单位或者部门借走
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >10
</td><br />
<td width="115" >处理
</td><br />
<td width="526" >该设备已经被拆卸，其本身已经不可用
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >11
</td><br />
<td width="115" >保留
</td><br />
<td width="526" >该设备已经被某单位或者部门预订，已经不再库存中了
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >12
</td><br />
<td width="115" >返厂
</td><br />
<td width="526" >由于设备已经被损坏或者过保，必须被退回厂商
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >13
</td><br />
<td width="115" >部署
</td><br />
<td width="526" >CI的默认状态，表示设备处于正常的生产运行状态
</td><br /></tr><br /><tr ><br />
<td width="69" height="34" >14
</td><br />
<td width="115" >订购
</td><br />
<td width="526" >该设备已经被订购，还未到货，仍然不可用
</td><br /></tr><br /></tbody></table><br />配置项管理和资产管理的联系和区别。<br />

<blockquote>Service Asset and Configuration Management (SACM) = Configuration Management + Asset Management<br /><br />Configuration Management<br />@The Process responsible for maintaining information about Configuration Items required to deliver an IT Service, including their Relationships<br />@This information is managed throughout the Lifecycle of the CI<br /><br />Asset Management<br />@Asset Management is the Process responsible for tracking and reporting the value and ownership of financial Assets throughout their Lifecycle.</blockquote>
