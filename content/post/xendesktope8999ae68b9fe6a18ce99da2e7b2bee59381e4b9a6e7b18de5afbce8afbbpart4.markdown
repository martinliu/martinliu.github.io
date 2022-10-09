---
author: Martin Liu
categories:
  - infrastructure
comments: true
date: 2013-05-02T04:22:36Z
slug: xendesktop%e8%99%9a%e6%8b%9f%e6%a1%8c%e9%9d%a2%e7%b2%be%e5%93%81%e4%b9%a6%e7%b1%8d%e5%af%bc%e8%af%bbpart4
tags:
  - xendesktop
title: XenDesktop虚拟桌面精品书籍导读(part4)
url: /2013/05/02/xendesktope8999ae68b9fe6a18ce99da2e7b2bee59381e4b9a6e7b18de5afbce8afbbpart4/
wordpress_id: 52401
---

[su_box color="orange" icon="flag"]
感谢 Eric Yao 的供稿，[@老树皮 Eric](http://weibo.com/ericyaozhen)
[/su_box]

桌面虚拟化项目的实施白皮书  《Citrix Virtual Desktop Handbook 5.x》，[点击下载](http://support.citrix.com/article/CTX136546)。

## 四、      控制层 Control Layer

控制层是设计架构的第四层。在上面有关用户的三个层面我们所做的决定都会汇总起来到控制层。

1. 访问控制器

访问控制器子层的职责是给每个用户提供予以支持访问控制层的基础架构组件。这么说可能比较绕口，那就换个说法吧，访问控制器一般包括例如 Web Interface、StoreFront，以及 NetScaler Access Gateway；

1)        远程访问架构

如果有用户需要远程或者是离线的移动访问能力，那么就要设计远程访问基础架构了。

1. **A.        \*\***决断：拓扑\*\*

网络拓扑的设计对远程访问架构能够支撑功能性、性能以及安全性至关重要。远程访问架构应当和安全团队一起合作以确保符合企业的安全规范。以下三种主要的拓扑结构我们在设计师可以考虑，每种的安全性逐渐递增：

l  **1-Arm (Normal Security\*\***，单臂模式)\***\*：**在这种架构下，Access Gateway 使用一个物理的或者是逻辑的 Bonded 的网络接口，再加上 VLAN 和 IP 子网的设计，来传递用户和后台虚拟桌面的流量。

l  **2-Arm (High Security \*\***双臂模式)\***\*：**在双臂模式下，Access Gateway 利用两张或者更多的物理或者逻辑 Bonded 的网络接口卡，再加上 VLAN 和 IP 子网的设计，来传递用户和后台虚拟桌面的流量。前段用户的流量被导向这些网络接口卡的第一张网卡上，前后端的流量是被分离设计的，就是说说后端虚拟桌面架构服务器的流量是被定向到第二张网卡上的。通过这样的设计我们就可以 DMZ 区来分离前后端的流量，同时还可以定制防火墙策略和流量监控策略。\*\*\*\*

l  **Double-Hop DMZ (Very High Security): **这种模式既利用了双臂拓扑下的特性，又使用了两个单独的 Access Gateway 设备。有一些企业使用了三个物理的/逻辑的防火墙结构来保护他们的内部网络。这三个防火墙将 DMZ 区划分为两个区域来提供额外的内部网络安全。

在第一个 DMZ 区的 Access Gateway 设备处理用户的连接，完成 SSL VPN 的安全功能。这个 Access Gateway 设备加密客户端连接，判断用户的认证方式，控制能够访问的内部网络服务器；

第二个 DMZ 区域的 Access Gateway 设备充当与一个代理设备角色。这个 Access Gateway 设备启用 ICA 协议将客户端连接穿越第二个 DMZ 区到后端的服务器场。在第一个 DMZ 区的 Access Gateway 设备和内部网络的 Secure 　 Ticket 　 Authority（STA）也是通过第二个 DMZ 区的 Access Gateway 设备来进行代理的。

1. **B.        \*\***决断：平台\*\*

在 Access Gateway 部分，我们曾经讨论过只要是涉及到远程访问，我们都会考虑 NetScaler Access 　 Gateway 设备。问了确定合适的 NetScaler 平台来满足项目需求，必须确定一些关键资源。由于所有的远程访问流量都是通过 SSL（安全套接层）来加密，再通过 HTTPs 的 HTTP（超文本协议）协议来传输。所以有两种资源 metric 需要确认：

l  **SSL\*\***吞吐量：\*\*SSL 吞吐量是定义为每秒钟能处理的 GB SSL 流量；

l  **SSL\*\***每秒交易量（TPS\***\*）：**TPS metric 定义在每秒每个应用程序交付控制器（ADC）能处理的 SSL 交易数量

关于这两个参数的更详细解释，可以参考：[Best Practices for implementing 2048-bit SSL](http://assets.citrix.com/NetScaler_0911/ASSETS/Citrix_2048_SSL_Best_Practices.pdf)

平均的 SSL 带宽开销在和虚拟桌面的开销比较起来时经常忽略。但是 SSL 带宽的计算将会有助于确定总带宽是否足够。固定带宽加上数据包头开销常常随着加密算法的不同而变化，总带宽开销也常常随着数据包尺寸大小的变化而不同。理想状态下，开销数字应当通过 POC 或者是 Pilot 来实际测试得来，但是在没有这些数据的情况下，在工作负荷带宽基础上加上 2%是一个合理的数字。因此，在确定 NetScaler 平台的时候，SSL 的吞吐量常常是最大并发带宽乘以 1.02，即：

SSL 吞吐量 = 最大并发带宽 × 1.02

例如：假设 128M 是最大的并发带宽，那么最合适的 NetScaler 模型应当计算为：

约 130Mbps = 128M × 1.02

NetScaler 有三种平台，每种都提供了大量的不同的扩展性：

l  **VPX\*\***：**VPX 平台的 NetScaler 和硬件的 NetScaler 提供完全一致的功能，不过他只适合于小型的测试环境使用。\*\***

l  **MDX\*\***：**NetScaler MDX 是 NetScaler 设备的硬件版本。他能支持大型网络可扩展环境；\*\***

l  **SDX\*\***：**NetScaler SDX 设备是在物理 NetScaler 设备和虚拟 NetScaler 设备之间的一个桥梁。一个 SDX 设备能够划分为多个虚拟的 NetScaler 设备。\*\***

2)        StoreFront

Citrix StoreFront 是 Web Interface 的下一代产品，它验证用户连接到后台的 XenDesktop 站点、XenApp 场，以及 AppController（SaaS 应用），然后枚举或者是聚合可用的桌面和应用程序到商店以便让用户通过不同操作系统平台上的 Receiver 来访问，包括安卓、iOS、Linux、Windows、Win8/RT 以及 Web 站点。

1. **C.         \*\***决断：Web Interface\***\*还是 StoreFront**

Web Interface 和 StoreFront 是两种不同的解决方案，在一些功能方面有重叠。所以我们要认真评估我们的需求。一般来说，新的方案应该使用 StoreFront，因为 Web Interface 已经不再有新功能添加了。可以参考下面的链接了解 Citrix 桌面产品的生命周期：[Lifecycle Milestones for Citrix XenDesktop](http://www.citrix.com/support/product-lifecycle/milestones/xendesktop.html)

下面的表格也示例了在何种情况下该使用什么产品：

下面的表格对两种产品在未来功能的开发目标上进行了一个对比，Web Interface 已经不再会有革命性的功能添加了：

下面的表格是功能对比：

有一些 Web Interface 有的功能也会被完全整合到未来的 StoreFront 新版本中去：

1. **A.        \*\***决断：Web \***\*服务的高可用**

如果 StoreFront 服务器不可用，或者是其他对应的 Web 服务不可用了，那么用户就不能连接到新的会话，例如打开新的虚拟桌面，无法打开应用程序等操作，因此，至少需要规划两台 StoreFront 来预防单点故障问题。我们可以考虑的方案包括：

l  **DNS Round Robin\*\***：**在多个服务器之间提供基本的负载均衡功能，无法做到是否可用性的检查；在服务器宕机时，部分用户会受到影响。\*\***

l  **Windows NLB\*\***：\*\*是 Windows 的一个服务。可以做一些基本的检查来判断服务器是否可用，但是无法判断单个服务的状态。

l  **Citrix NetScaler\*\***：\*\*智能硬件设备，能检查 StoreFront 服务的状态，根据用户请求主动激活负载均衡状态。

1. **B.        \*\***决断：应用程序订阅数据库的高可用\*\*

StoreFront 的配置数据都存储在每一台 StoreFront 服务器的本地，然后被复制到服务器组中的其他的系统中。对比之下，用户应用程序订阅信息存储在应用程序订阅数据库中，该数据库可以是本地的 StoreFront 服务器，也可以是推荐的一个专门的 Microsoft SQL Server。

如果应用程序订阅数据库不可用，以下功能将不可用：

l  用户不能在管理他们的应用程序订阅；

l  无法登陆至 Web 方式的 Reciever，但是已经建立起来的会话可以继续正常工作；

为了防止应用程序订阅数据库成为单点故障点，Citrix 推荐 SQL 的高可用方案：

l  **自动容错的 SQL\*\***镜像：**数据库镜像提供了一种比数据库 Clustering 更简单的快速容错方法。数据库镜像技术在每一个镜像点上需要一个标准的 SQL 标准版服务器 License，在加上一个 witness 服务器的 SQL Express License 即可。更多细节可以参考文档：[Configuring StoreFront using the Configuration Files.](http://support.citrix.com/proddocs/topic/dws-storefront-12/dws-configure-conf-file.html)\*\***

l  **SQl Clustering: **微软的技术，不过老实说，相比较 Mirroring 技术配置太复杂，此外，自动容错的过程也更慢。在 License 上，每个 Cluster 节点都需要一个企业版的 SQL license。\*\*\*\*

l  **Hypervisor\*\***高可用：\*\*数据库部署在一台虚拟机上，通过 Hypervisor 的高可用来实现。这个技术比镜像或者是 clustering 都要便宜，因为只需要一个 SQl Express License 和一台 SQL Server（需要一个具备 HA 功能的 Hypervisor License）。不过，这个技术容错过程较慢，也仅仅是当 SQl Server 的操作系统宕机时才能启动容错机制。如果数据库服务出现错误是无法被 Hypervisor 层检测到的。

_注意：未来的 StoreFront**版本将不会再使用应用程序订阅数据库（Application Subscription Database**），相反，预订信息会自动的在 StoreFront**服务器组中的 StoreFront**服务器中自动复制。_

1. **C.         \*\***决断：容量规划\*\*

基于扩展性的测试，单个 StoreFront 服务器可以支持的用户数是无限制的，受限制的是在这个服务器上每小时之内用户同时操作的动作。这是因为仅仅当用户执行一个动作的时候，例如在 Receiver 中订阅一个应用程序是，StoreFront 才被使用。当用户连接到所发布的资源时，StoreFront 实际上是 idle 状态的。因此，下面的表格所展示的内容介绍的是没鸟的请求时，或者是每小时的请求数。我们建立了一个前提条件是每用户在每小时之内启动了五个应用程序，订阅了 2 个应用程序，取消订阅了一个应用程序，总共每小时是 8 个操作量。

注意：上述数字是在仿真环境下测试得来：基于 SSL 的 XenApp6.5，发布了 100+个应用程序，每个用户在 5 秒钟之内完成操作的。

StoreFront 对 CPU 的数量更敏感，也就是说对 CPU 的消耗更大，而不是对内存消耗更大。推荐的企业 StoreFront 服务器是 4 个 vCPU 和 4GB RAM。

1. **D.        \*\***但服务器扩展性 – \***\*应用程序订阅数据库**

应用程序订阅数据库包含了每个用户订阅的一系列资源列表情况。基于测试环境下，推荐的一个储存应用程序订阅数据库独立 SQL 服务器的配置是 4vCPU 和 4GB RAM。

数据库的增长速度大约是每个订阅 10KB 空间消耗：

数据库大小 = （用户数 × 每用户的订阅数） × 10KB

1 个订阅 = 1 个用户订阅一个应用程序，例如，1000 个用户订阅 10 个应用程序就是 100MB。

1. 桌面控制器

这部分内容主要是介绍 XenClient 部分，请大家自行参见[原始文档](http://support.citrix.com/article/CTX136546)。

下期预告：下一期我们介绍最后的部分：Provisioning Services
