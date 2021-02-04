---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2009-07-04T05:37:57Z
slug: tomcat%e5%8e%8b%e5%8a%9b%e6%b5%8b%e8%af%95-%e6%8c%ba%e4%bd%8f200%e5%b9%b6%e5%8f%91
tags:
- benchmark
- loadrunner
- Tomcat
title: Tomcat压力测试-挺住200并发
url: /2009/07/04/tomcate58e8be58a9be6b58be8af95-e68cbae4bd8f200e5b9b6e58f91/
wordpress_id: 49259
---

![tomcat.jpg](http://www.willisms.com/archives/tomcat.jpg)<br />最近在CCB的测试中有一项是住系统登陆页面的压力测试。我一直就很担心是否能通过压力测试，因为一个同事告诉我上次他的结果是80就不行了。总结一下，我这次成功的原因主要就是两个地方：<br />1）设置Tomcat启动和最大内存使用都是1500MB<br />2）修改server.xml中关于连接数等参数(回头贴出我的那些配置内容)<br /><br />我的服务器配置如下：<br />Dell 2950 1C4核，8GB内存，单块136GB硬盘，Windows2003系统，JDK1.6，Tomcat 5.5.21<br /><br />另外，我一直以为Loadrunner需要真实Lic文件才能用，没想到的是，我随便在网上搜了一个也能用，真是神奇啊！ 不过还是反对盗版哈哈:)
