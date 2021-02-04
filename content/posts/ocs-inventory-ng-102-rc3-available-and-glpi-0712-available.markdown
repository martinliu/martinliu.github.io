---
author: liuadmin
categories:
- Asset Mgmt
comments: true
date: 2008-11-27T05:15:26Z
slug: ocs-inventory-ng-102-rc3-available-and-glpi-0712-available
tags:
- GLPI
- inventory
- OCSNG
title: '[项目更新] OCS Inventory NG 1.02 RC3 available and GLPI 0.71.2 available'
url: /2008/11/27/ocs-inventory-ng-102-rc3-available-and-glpi-0712-available/
wordpress_id: 49242
---

如果你了解OCS Inventory NG 的话，您可能会发现这个问题，在家里用adsl上网，可能访问不到这个项目的网站，所以要想下载这个项目的软件，可以去sorceforge.net下载。<br /><br />10/28/2008 OCS Inventory NG Server 1.02 RC3 发布了Patch1，Patch1主要是修复了一些数据库创建和更新的问题，具体的内容如下所示：<br />

<blockquote>In the database creation/update process launched through Administration Console (install.php), défault settings for cache and download directories are missing.<br /><br />Also, default values in dynamic group computation are not set correctly. So dynamic group of computers are not updated correctly in Communication Server.<br /><br />We've also included Remi patch in install.php to avoid overriding database username and password if you've changed them. Thanks Remi.</blockquote>

<br />OCS Inventory NG在sorceForge的下载网址 http://sourceforge.net/projects/ocsinventory/<br /><br />**15 September 2008 GLPI 0.71.2 发布 **<br /><br />这也是一个bug修复的版本，没有新增什么功能。修复的问题如下所示。<br /><table border="0" ><br /><tbody ><br /><tr ><br /><tr ><br />
<td style="border: 1px dotted #27900d;padding: 5px" valign="top" ><br /><br />

[#1094](https://dev.indepnet.net/glpi/ticket/1094)
    Auth Method Change if old one does not exists
[#1109](https://dev.indepnet.net/glpi/ticket/1109)
    Clean update for end_warranty_buy on search system
[#1110](https://dev.indepnet.net/glpi/ticket/1110)
    OEM Computer selection problem on licenses
[#1111](https://dev.indepnet.net/glpi/ticket/1111)
    Keep reminder and bookmark when author is deleted
[#1112](https://dev.indepnet.net/glpi/ticket/1112)
    Bookmark creation right problem
[#1113](https://dev.indepnet.net/glpi/ticket/1113)
    Mail formatting
[#1114](https://dev.indepnet.net/glpi/ticket/1114)
    Clean log on cartridge / consumable
[#1115](https://dev.indepnet.net/glpi/ticket/1115)
    logout with noAuto for auto logged users
[#1119](https://dev.indepnet.net/glpi/ticket/1119)
    Mailgate followup import problem due to author check
[#1120](https://dev.indepnet.net/glpi/ticket/1120)
    Cartridge restore bug
[#1121](https://dev.indepnet.net/glpi/ticket/1121)
    Clean Ignore process in software dictionnary
[#1122](https://dev.indepnet.net/glpi/ticket/1122)
    Correct stats computation
[#1131](https://dev.indepnet.net/glpi/ticket/1131)
    Search engine problem for plugin field which need group by
[#1133](https://dev.indepnet.net/glpi/ticket/1133)
    Bug on database connection error
</td><br /></tr><br /></tr><br /></tbody></table><br />

<blockquote></blockquote>
