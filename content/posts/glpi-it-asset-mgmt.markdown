---
author: liuadmin
categories:
- Asset Mgmt
comments: true
date: 2007-04-30T03:49:00Z
slug: glpi-it-asset-mgmt
tags:
- GLPI
title: GLPI –IT资源生命周期管理
url: /2007/04/30/glpi-it-asset-mgmt/
wordpress_id: 49151
---

[![](http://bp2.blogger.com/_KU0istEHv9w/RjVt3XwKBiI/AAAAAAAAADU/8AXj0w-tXTg/s400/computer.JPG)](http://bp2.blogger.com/_KU0istEHv9w/RjVt3XwKBiI/AAAAAAAAADU/8AXj0w-tXTg/s1600-h/computer.JPG)<br />[![](http://bp2.blogger.com/_KU0istEHv9w/RjVt3XwKBjI/AAAAAAAAADc/94EbtEVA1_I/s400/logo-glpi.png)](http://bp2.blogger.com/_KU0istEHv9w/RjVt3XwKBjI/AAAAAAAAADc/94EbtEVA1_I/s1600-h/logo-glpi.png) GLPI是一个法国的开源项目，之所会了解到这个项目，是由于OCSNG的原因。当我安装并使用了一下它之后立刻产生了以下问题：1）它仅仅是一个对现有设备Inventory的工具，对新设备的采购和计划无法实现。2）它仅仅是一个技术工具，能提供CMDB相关的配置信息数据，相关的流程如何实现：计划，采购，使用，变更和报废。<br /><br />没想到在安装试用了GLPI之后着一切都疑问都散去了。那就先讲讲安装过程。环境准备，我的测是环境如下：Dell Inspiron 600M笔记本（70GB HD, 1GB RAM），由于硬件资源实在有限，所以我喜欢使用VMWare作为测试环境。在VMWere中安装SuSE 10.1，最小安装；安装apache,perl,php,mysql和其它相关的包，由于Yast的包管理实在好用，所以为整个安装过程带来了很多方便。如果您也想测试的这个软件系统的话，最简单的方式则是：找一个物理的机器做SuSE 10.1的全安装，这样的安装过程绝对不会有找不到那些依赖组建的问题。软件安装：OCSNG / GLPI的安装模式都是相同的基本相似的比较简单；再次就不多话了；我猜您可能会碰到的问题有：GLPI的登陆用户名和密码的问题。所有可以利用的相关文档里好像没用提到这个信息，昏！可能是我的运气不好，的确没找到，不过最终被我猜到：）[登录密码在安装向导的导数第二个页面上]<br /><br />OCSNG需要安装Agent，Agent会在目标设备上做清单扫描，上传Inventory信息；它的三层结构可能会是企业级用户的好消息，它还能方便的通过Windows 域的组策略部署代理，也就是说只要用户登陆域，代理就能顺利安装部署。OCSNG趋向做全面的客户端管理：inventory、license管理等方面。<br /><br />从上面的GPLI的screenshot可以看出和一个笔记本电脑相关的一切。先讲讲它的来由，GPLI解决的是OCSNG的上层问题：计划，购买，部署，跟踪，变更，维护，退休。它管理的是所有业务和流程层面的东西。GPLI的数据来自OSCNG的数据库，它能自动从OSCNG中定期更新inventory信息。截屏中的电脑是我在我的笔记本上安装了OSCNG后，做的首次扫描后的结果，在GPLI中配置了和OSCNG的集成后，它就变成了一个GPLI中的管理数据。可以看到，和一个电脑资产相关的所有硬件信息，软件信息，help desk请求，文档，链接，注释和变更历史记录等。GPLI中有对外的HelpDesk模块，这能方便最终用户对设备维护的请求。<br /><br />GPLI和OSCNG很好的结合可能做到“IT资源生命周期管理”，参考文档：[http://glpi-project.org/wiki/doku.php?id=en:cyclevie](http://glpi-project.org/wiki/doku.php?id=en:cyclevie)<br /><br />如果对把它们所实现的功能和ITIL框架对应一下，或许IT服务财务管理，能力管理，配置管理和发布管理等流程能与之能有某些联系。
