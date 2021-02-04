---
author: liuadmin
categories:
- XenDesktop
comments: true
date: 2013-04-15T06:52:55Z
slug: xendesktop%e8%99%9a%e6%8b%9f%e6%a1%8c%e9%9d%a2%e7%b2%be%e5%93%81%e4%b9%a6%e7%b1%8d%e5%af%bc%e8%af%bbpart2
tags:
- hdx
- XenDesktop
title: XenDesktop虚拟桌面精品书籍导读(part2)
url: /2013/04/15/xendesktope8999ae68b9fe6a18ce99da2e7b2bee59381e4b9a6e7b18de5afbce8afbbpart2/
wordpress_id: 52336
---

[box color="orange" icon="flag"]
感谢 Eric Yao 的供稿，[@老树皮Eric](http://weibo.com/ericyaozhen)
[/box]

桌面虚拟化项目的实施白皮书 《Citrix Virtual Desktop Handbook 5.x》，[点击下载](http://support.citrix.com/article/CTX136546)。




上周一我们介绍了《Citrix桌面虚拟化实施部署白皮书》的第二部分《设计篇 Design》的第一单元：用户层。今天我们继续往前进，开讲第二单元：访问层的部分。

三、 访问层 Access Layer

访问层的设计主要是基于每个用户组和终端设备的移动性需求。

1) 决断：认证点

让用户在什么地点做认证是管理员的决定，一般而言，有四个认证点：

a) Web Interface：给XA和XD提供安全访问；

b) StoreFront：为Receiver交付认证能力和资源；

c) Secure Gateway (Web Interface): Secure Gateway是一个Windows的应用程序，她和WI配合工作；

d) Access Gateway: 硬件

具体采用哪种方式认证由用户组的移动需求来决定，推荐方案如下：

2) 决断：预认证策略

如果我们使用的是Access Gateway，我们就可以选择是否采用预认证策略，这些策略可以是确定终端是否满足某种接入网络前的扫描条件。

我们可以配置的策略包括测试防病毒软件、防火墙软件、操作系统，甚至是注册表键值。XA和XD可以利用这些策略的检查结果确认后续的动作，包括剪贴板是否开启，打印机映射，甚至是否开启特定的应用程序访问权限。例如，如果用户没有安装防病毒软件，可以配置策略隐藏敏感的应用程序。

下面的图标从流程上示例策略配置是如何流转的：



3) 决断：认证策略

l Web Interface, Secure Gateway (Web Interface), or StoreFront: StoreFront是未来的方向，而Web Interface已经是行将就木，所以下面的策略主要是用在StoreFront上，当然也适用于Web Interface

n 用户名/密码

n Domain Pass-Through：允许从用户设备上透传Domain登录信息，用户登录到加入域的电脑后自动登录到Store；

n Access Gateway Pass-Through：用户登录到Access Gateway后自动登录到Store

l Access Gateway：NetScaler支持几种不同的认证手段。下面分别列出了几种主要的认证方法，每种方法都可以单独使用，但是在实践中，我们进场组合起来以提供多因素认证。

n LDAP：轻型目录访问协议是我们最为熟悉的认证方法了，它是一种基于TCP协议的目录访问服务，例如MS的活动目录就是其中一种实现形式。

n Radius（aka Token）：Radius全名是Remote Authentication Dial In User Service，这是一种基于UDP传输协议的安全认证协议。除了认证外，它还提供授权和计费功能。Access Gateway转发用户输入的用户名和密码给Radius服务器，Radius服务器可以立即检查用户名和密码，也可以转发给目录服务器。

n 客户端证书：用户登录到Access Gateway虚拟服务器后，可以通过本地的客户端证书的属性来做认证。客户端证书通常在用户端的形式是智能卡，或者是Common Access Cards (CACs)的形式，再通过客户端本地的读卡器来读取信息。

采用什么认证形式通常都是取决于安全的需求，以及使用什么认证点。下表给出了一个基于安全需求级别的示例：

4) 决断：会话策略

采用Access Gateway作为认证点的用户必须有对应的会话策略来定义用户体验。会话策略的制定是基于Receiver在设计阶段制定的。一般而言，首先我们会将设备分为非移动设备和移动设备两种：

l 移动设备：表达式定义为：“REQ.HTTP.HEADER User-Agent CONTAINS CitrixReceiver”，该语句将移动设备设置为比非移动设备更高优先级以保证移动设备的匹配性。

l 非移动设备：表达式定义为：“ns_true”，即所有流量。

更多信息，可以参考Citrix公开电子文档：Receiver and Plug-ins

BTW，另外一种会话策略是采用终端的扫描方法。

5) 决断：会话Profile（Session Profile）

每个会话策略（Session Policy）都必须定义一个对应的Session Profile（姑且翻译成会话配置文件）。这个会话配置文件定义了用户去访问资源时的访问细节。有两种定义到虚拟桌面环境的访问方式的会话配置文件的形式：

l SSL VPN：传统的VPN方式，将网络全部打通。这种方式并不一定十分安全，因为这能导致客户端到内网服务器的攻击访问。

另外一种办法是考虑是否在SSL VPN中开辟一条给客户端网络流量的单独通道。这样通过receiver的流量智慧限制在指定的端口，只能访问指定的服务器资源等。

上述两种方式各有利弊，第一种方式虽然安全性差了，但是可以做客户端流量可以被企业的网络过滤设备，例如入侵检测设备做监视和控制。

l HDX Proxy：在HDX 代理方式下，用户是通过Access Gateway连接到他们的虚拟桌面和虚拟应用。这种方式下完全没有将内部资源暴露到公网上，此时Access Gateway充当了一个微型VPN的作用，它仅处理HDX的流量。其他的流量，例如电子邮件，又或者是使用者上网的流量都不经过Access Gateway。

6) 决断：访问带宽

最后的访问层决断就是要决定虚拟桌面所需要的最大并发网络带宽。其中很重要的一个关键环节就是决定采用NetScaler Access Gateway的哪一个平台。

每个用户所需要的带宽关键还是要看计算的需求。一个时不时才用一下电脑的ERP使用者和一个在电脑前屁股都不挪窝的OA用户肯定带宽要求是不同的，如果是CAD画图的用户那就更不用说了。

理想情况下带宽的使用情况是通过带宽分析工具来给出来，不过我们还是可以给出一些经验值：



总带宽的的计算公式可以这样来定义：

总带宽 = 平均带宽 × 最大并发用户值

更多细节，可以参考Citrix的知识库文章：

XenDesktop Planning Guide: User Bandwidth Requirements ： [XenDesktop Planning Guide: User Bandwidth Requirements](https://mail.citrix.com/owa/redir.aspx?C=5BdyIzIzrEOfoVxvpzfMxnn5HIs1DdAIlS0opaj6UrOPgSysoUakkdkru0zo0okQlYOGYaDEspc.&URL=http%3a%2f%2fsupport.citrix.com%2farticle%2fCTX126191)


