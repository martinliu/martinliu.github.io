---
author: liuadmin
categories:
- XenDesktop
comments: true
date: 2013-04-15T06:44:52Z
slug: xendesktop%e4%b8%ad%e5%a6%82%e4%bd%95%e9%87%8d%e5%ae%9a%e5%90%91usb%e8%ae%be%e5%a4%87
tags:
- hdx
- usb
- XenDesktop
title: XenDesktop中如何重定向USB设备
url: /2013/04/15/xendesktope4b8ade5a682e4bd95e9878de5ae9ae59091usbe8aebee5a487/
wordpress_id: 52334
---

![hdx-monitor-banner.png](webkit-fake-url://C94F41EF-2B27-43A6-8999-EBAB0037856E/hdx-monitor-banner.png)

原文出处：[http://support.citrix.com/article/CTX136751](http://support.citrix.com/article/CTX136751)  这篇文章你还不会，你就out了！

**概要**

本文描述如何映射默认下被禁用的USB设备。

**要求**

当重定向USB设备，终端用户必须首先识别USB设备，将其映射到会话中。假如设备需要特殊驱动，则驱动必须同时安装在客户机和虚拟桌面代理（VDA）上。如果终端识别驱动，设备在没有驱动的情况下仍可映射，但是VDA上需安装驱动以确保工作正常。

**背景**

特定USB Class默认下被禁用因为它们主要用于本地工作站，例如智能卡阅读器。

**步骤**

**注意**!这个修复需改变注册表。错误使用注册表编辑器可能产生严重问题，导致你需要重装操作系统。Citrix不承诺解决错误使用注册表编辑器的问题。使用注册表编辑器存在风险。确保修改前备份注册表。

完成以下步骤查找设备的Class ID和Hardware ID：






	
  * 打开终端客户机的设备管理器，查找需要重定向的USB设备。





![ipboard01](http://support.citrix.com/article/html/images/CTX136751-1.gif)






	
  * 右击设备选择**属性**。注意在Details面板上，显示如下图的Hardware ID 和 Class ID。





![](http://support.citrix.com/article/html/images/CTX136751-2.gif)

![](http://support.citrix.com/article/html/images/CTX136751-3.gif)






	
  * 在**Citrix Desktop Studio** > **HDX 策略** > **用户**中，点击**新建**USB 设备重定向策略。





![](http://support.citrix.com/article/html/images/CTX136751-4.gif)






	
  * 点击下一步，**类别**中选择**USB设备** > **客户端USB设备重定向，**点击**添加**，选择**允许**后**确定**。





![](http://support.citrix.com/article/html/images/CTX136751-5.gif)

然后，类别中选择USB设备 > 客户端USB设备重定向规则，点击添加

![](http://support.citrix.com/article/html/images/CTX136751-6.gif)

点击**新建**添加允许的Hardware ID：

![](http://support.citrix.com/article/html/images/CTX136751-7.gif)

**确定**后点击**下一步**，最后**应用**此策略。






	
  * 在终端设备，查看注册表HKLM\Software\_WOW6432Node_\Citrix\Ica Client\GenericUSB，设置_DeviceRules_值为‘Allow: VID=0911 PID=1844’





你可以删除_deny class rule_以使能此class的所有设备。但是，为防止非法重定向，增加**Allow**规则方法更优。

**注意：**当增加**Allow**规则，确保它置于规则列表顶部，使它比规则**Deny**优先级更高。

![](http://support.citrix.com/article/html/images/CTX136751-8.gif)

此时在Desktop Viewer 上可见对应USB设备。

![](http://support.citrix.com/article/html/images/CTX136751-9.gif)






	
  * 假如点击设备仍不能映射至会话中，尝试手动在VDA的注册表中添加允许标记：
HKLM\Software\Policies\Citrix\ICA_Client\USB\DeviceRules。





**更多信息**

默认值存储于VDA注册表的HKLM\SOFTWARE\Citrix\PortICA\GenericUSB Type=String Name="DeviceRules"，但是，不建议修改此值，因为当VDA自检，它首先查看HKLM\Software\Policies\Citrix\ICA_Client\USB\DeviceRules，再查看本地路径。优选修改规则方法是使用组管理对象（GPO）模板。

**注意：**你必须修改终端客户机注册表以允许对应的USB class。

查看更多: [http://support.citrix.com/proddocs/topic/xendesktop-rho/ps-ref-policies-usb-devices.html](http://support.citrix.com/proddocs/topic/xendesktop-rho/ps-ref-policies-usb-devices.html)
