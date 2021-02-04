---
author: liuadmin
categories:
- Asset Mgmt
comments: true
date: 2008-04-28T02:01:06Z
slug: deploy-asset-management-solution
tags:
- asset
- configuration
- GLPI
- OCSNG
title: Deploy asset management solution
url: /2008/04/28/deploy-asset-management-solution/
wordpress_id: 49202
---

[![](http://www.ocsinventory-ng.org/uploads/images/poster-eng.png)](http://www.ocsinventory-ng.org/uploads/images/poster-eng.png)

This is my second virtual appliance, it suppose to work for production. This is a 100% open source solution for inventory/asset management, it including OCS Inventory NG and GLPI. I encourage you to deploy it in your school or company.

**About virtual appliance / 关于此虚拟应用**



	
  * OpenSuSE 10.2 (root password is martinliu)

	
  * LAMP+Perl

	
  * OCS Inventory v1.02 RC1

	
  * GLPI v0.70.2

	
  * bridged network


You can download it from below.

[Download it 下载](http://demo.wholog.net/AssetMgmt.rar) This source is not available any longer. I will offer it by DVD. 这个地址已经无法下载，请关注我即将推出的DVD版虚机。

**Thanks [BigYue.com](http://www.bigyue.com/) for donated upload space.  感谢****[BigYue.com](http://www.bigyue.com/)****的空间。**

**Run Server / 运行管理服务器（>=2GB RAM）**



	
  1. un-zip the image on a computer which will be network with for any managed nodes to upload inventory information. This host machine should have at least 2GB RAM.

	
  2. Download a wm player and install it.

	
  3. Open virtual machine and power on.

	
  4. At top of boot screen, you will find the ip address of this vm I assume you have a  DHCP server on network. Otherwise you have to configure network manually for this vm.

	
  5. Access to the home page ([http://IP_address_Of_vm/](http://IP_address_Of_vm/)) which I made it for you. On this page, there are login information and entry points.


Now you have a full function asset management solution up an running. You will configure security for the whole system before you do more work with it. You should change the password for root and mysql. Mysql have a blank password. After you done this, you must re-configure database connection for both OCS Inventory NG and GLPI accordingly. Please refer to administration guide.

**Deploy Agent / 安装部署代理**



	
  * For any Unix-like system : you will manually install on each of target computer. Following the installation guide from OCS inventory NG.

	
  * For MS windows system: You can do manually installation too. Also you could distribute agent via AD domain policy automatically, all target machines must logon the AD domain at least once in order to get agent package installed. Agent is running as a windows service if it is installed properly; inventory information will update timely to  the server. The Agent package can be copied to a USB key. You can use it for collecting inventory information for off-line computers, or a computer which you wont have any piece of OSS installed on it. I'm kidding, I guess you love to run OSS on any of your computers, PS: the more the better.


**Management Asset / 管理IT资产**



	
  * Synchronize inventory data from OCS Inventory NG to GLPI. GLPI can do it at interval that you set hourly or daily.

	
  * Those two OSS are just easy to use. You will still read some necessary documents on their web. **请阅读尽可能多的使用手册**

	
  * As long as you use this virtual appliance, I can see your smile face. Don't forget give me comment below and let me know how many nodes do you manage.

	
  * Enjoy and have a lot of fun.


**Support / 支持** This virtual appliance comes with ABSOLUTELY NO SUPPORT. I will try my best to support you, but questions are not guaranteed for a quick answer. I strongly recommend you will go to open source community when you run into any error. I believe you can get support and might help others too.  If you improved this virtual appliance, I am looking forward to see your share. I'd like to hear any good idea from you.

**Notes:**


### From wikipedia: [Comparison of open source configuration management software](http://en.wikipedia.org/wiki/Comparison_of_open_source_configuration_management_software)
