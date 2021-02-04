---
author: liuadmin
categories:
- XenDesktop
comments: true
date: 2013-05-07T02:36:41Z
slug: xendesktop%e8%99%9a%e6%8b%9f%e6%a1%8c%e9%9d%a2%e7%b2%be%e5%93%81%e4%b9%a6%e7%b1%8d%e5%af%bc%e8%af%bbpart5
tags:
- Citrix
- PVS
- XenDesktop
title: XenDesktop虚拟桌面精品书籍导读(part5)
url: /2013/05/07/xendesktope8999ae68b9fe6a18ce99da2e7b2bee59381e4b9a6e7b18de5afbce8afbbpart5/
wordpress_id: 52408
---

[box color="orange" icon="flag"]
感谢 Eric Yao 的供稿，[@老树皮Eric](http://weibo.com/ericyaozhen)
[/box]

今天是[《Citrix Virtual Desktop Handbook》](http://support.citrix.com/article/CTX136546)第二讲的最后一期，专门论述一下PVS的设计。在本期之后我会把所有以往的内容整合在一个完整的白皮书中，稍等几日。。。

请期待基于本系列5篇文章的完整版中文白皮书下载。

Citrix桌面虚拟化实施部署白皮书 第二讲之第五期：PVS的设计



	
  1. Provisioning Services


Citrix Provisioning Services（PVS）使用流化的技术简化了虚拟桌面和物理桌面的部署。计算机从一个单个的共享磁盘镜像上被实时制备（Provisioned），管理员完全不需要去管理或者是给每个单独的用户操作系统打补丁。



**1)        ****决断：****Farm****（场）的数量******

一个Provisioning Services的场代表着Provisioning Services基础架构的最高层级。所有在一个场的Provisioning Servers（服务器）都共享同一个SQL 数据库哦Citrix License服务器。当确定需要多少个Provisioning Services的场时，我们一般需要考虑以下几个因素：

l  **网络：**Provisioning Servers会始终和场数据库通信以获取系统配置信息。因此，一般来说每个target devices聚集的地理位置应该部署一个独立的场，当然，如果异地之间的网速足够快，理论上也可以只建立一个Provisioning Services场。

l  **重要程度：**管理者应该决定它可以容仍什么样的风险。尽管可能性非常的低，但是Provisioning Services场如果出问题还是会影响整个组织架构的使用。如果一个公司需要非常高等级的可用性，那么多个场的搭建就可以避免这个问题。

l  **可管理性：**管理者可能需要在基于组织架构划分的基础上，例如国家、地区，又或者是不同部门之间，来进行单独的系统管理。尽管听起来这会增加管理的复杂程度，但是实际上只会增加有限多的配置、桌面创建过程，以及操作系统镜像更新。



**2)        ****决断：站点（****Sites****）的数量******

每个Provisioning Services的场都包含一个或者多个的站点。一个Provisioning Services的站点是一个逻辑的实体组成部分，包含了Provisioning Servers（服务器）、vDisk pools，以及target devices的集合。多个站点共享同一个数据库。Target devices可以在同一个站点中容错到其他的Provisioning Servers上。在以下的情况下我们建议创建多个站点：

l  **网络：**站点用来控制Provisioning Services的流数据量。例如，一个站点可以根据站点、rack、或者是刀箱来创建，以确保流数据始终保持在本地而不变成一个网络瓶颈。

l  **组织架构：**另外一个需要创建多个站点的实际理由是企业组织架构的改变。例如，两个公司通过收购合并了，但是有需要在企业整合过程中保持资源的独立。



3)         **决断：数据库的配置**

Provisioning Services的数据库存储有所有一个场内的的系统配置信息。Provisioning Services 6.X版本支持一下版本的SQL数据库，包括Express、标准版、企业版的SQL Server 2005、2008R2以及2012版。选择哪一个SQL版本其实是取决于你需要哪一个级别的容错水平。以下的表格是一个SQL 2008R2版本的示例：



Provisioning Services场的数据库的大小很少会超过250M容量，即使在大型环境下也不会。所以，在测试环境下Express版本是最佳选择，因为不需要容错功能。

下面的公式是用来计算Provisioning Services的数据库的容量大小：





4)         **决断：数据库；离线模式**

如果到Provisioning Services场的数据库的连接断开，已经连接到Provisioning Servers的target devices仍然可以正常工作，但是新的target devices将会无法启动。

支持离线数据库功能可以让Provisioning Services在失去连接到数据库后仍然可以保持正常操作。在服务器启动时会对数据库做个快照，然后定期保持同步。如果连接丢失，Stream Services会使用最新的一个快照以获取场的配置信息。一旦数据库连接建立起来了，Stream过程会把断线期间的变化同步到数据库中。

_需要注意的是，离线数据库功能默认下是关闭状态的，而且也仅仅是在生产环境下的稳定的场环境下推荐使用。评估环境下不推荐使用_



5)         **决断：服务帐号**

Stream和SOAP服务会和其他许多不同的Provisioning Services基础架构中的组件进行通信，如下图所示：





6)         **决断：设备集合**

设备集合是用来创建和管理target devices逻辑组。创建设备集合可以简化设备管理，因为将来的操作可以不用基于target device级别，而是基于集合这个级别。

设备集合可以基于物理地理位置、子网范围、组织架构中不同的部门来设计。也可以考虑基于vDisk的分配来创建不同的设备集合，这样所有分配到一个特定vDisk的所有的target devices就能被快速的定位。



7)         **决断：****Provisioning Server****（服务器）的内存**

运行Provisioning Services的Windows操作系统会把vDisk的部分内容缓存在内存（系统缓存）中以降低从存储中读取的操作。从存储中读取数据的速度是显著低于从内存中读取数据的，所以，正确计算Provisioning Servers的内存是非常关键的。请参见以下的公式：



简单地说，就是给每个vDisk分配2G左右的内存。



8)         **决断：****Scale Up****还是****Scale Out**

_题外话：首先对这两个词进行一下解释：_

_Scale Out(__向外扩展)__：就是指企业可以根据需求增加不同的服务器应用，依靠多部服务器协同运算，借负载平衡及容错等功能来提高运算能力及可靠度。_

_Scale Up(__向上扩展)__：指企业后端大型服务器以增加处理器等运算资源进行升级以获得对应用性能的要求。_

随着Farm场的增长，管理员需要作出决定以判断是不是需要给Provisioning Server增加更高的资源，也可以是在场中增加更加多的Provisioning Servers，一下了可以是考虑因素：

l  **冗余：**将用户符合扩展到其他负荷不重的服务器上会有助于降低当Provisioning Servers宕机情况下爱所影响的用户数量。如果公司无法接受单点高性能服务器宕机所造成的损失，那就考虑Scaling Out，就是我们说的向外扩展（既增加多台服务器）。

l  **容错时间：**在一个单台的Provisioning Server上所连接的Target Devices越多，在服务器宕机后所需要的恢复时间也就越多。Citrix的内部测试显示在Provisioning Services 5.6 SP2版本下，1500台Target Devices需要大约8分钟恢复生产能力；

l  **数据中心容量：**数据中心一般都是只有有限的空间、电源、冷却能力，此时，可以考虑Scaling Up，即向上扩展（增加单台服务器的处理能力）。

l  **硬件成本：**刚开始时，可能Scale Up会有更高的性价比，但是继续往后可能Scale Out会开始更具性价比，应该做一个成本分析；



9)         **决断：****vDisk****的存储位置**

一个场可以包含一个或者多个的vDisk存储。一般来说有两个主要的选择：

l  **本地存储或者是DAS****：**DAS可以是本地的，或者是基于Block的存储类型，Provisioning Server可以直接访问，例如SATA、SCSI、iSCSI，以及光纤。本地的vDisk就只能被本地的Provisioning Server所反问，因此，vDisk应当被手动或者自动的复制到其他的vDisk存储位置上。

**_注意：_**_将vDisk__部署在本地存储上并不会造成单点故障，因为Provisioning Service__的负载均衡技术可以让target devices__自动的在其他Provisioning Servers__之间做容错动作。_

l  **NAS****：**NAS是一种基于文件级存储的solution。NAS协议包括CIFS和NFS。NAS vDisk可以被多个Provisioning Server同时所访问。NAS由于不需要vDisk复制功能所以能保证vDisk在一个场内的多台Provisioning Server之间保持连续性。

**_注意：_**_NAS__反而会造成单点故障，如果网络共享功能不可用，所有从这个vDisk__上Streamed__的target device__都会变得不可用了。_



10)     **决断：评估存储容量**

一个vDisk包含了一个VHD基础镜像文件、一个properties文件（.pvd），也可以能包含了一个链条VHD差异磁盘（.avhd）。每当一个vDisk被Provisioning Services versioing所更新时，一个新的差异磁盘就会被创建。

一个vDisk所占空间的评估因素大致有以下几点：

l  **vDisk****的总容量：**顾名思义

l  **vDisk chain****的最大版本数：**vDisk versioning简化了vDisk升级以及管理的负担，他能够更加灵活和健壮的管理vDisks。

**_备注：_**_太多的差异磁盘会显著降低Provisioning Services__的性能，建议不要超过5-7__个的版本数。_

l  **vDisk****版本变化百分比：**差异磁盘的大小是随着对vDisk的改动多少而随着变化的。改得越多，差异磁盘的大小就越大。以下的计算公式可以用于计算vDisk容量：



举例如下：

比如你计划部署三个vDisk：

  Windows 7 (x64) image = 40GB

  Windows 7 (x86) image = 35GB

  Windows XP image = 20GB

每个vDisk都不会超过5个差异磁盘。预计一个差异磁盘大致是20%的主vDisk镜像文件大小，那么估计Provisioning Services存储所需要的空间如下：





11)     **决断：****RAID****级别**

存储子系统的RAID级别会对应用程序和用户的工作负荷产生直接的影响。RAID 0、1以及10对读操作是最优，而RAID 5和6是对写操作是最优。对于Provisioning Services来说，不同的RAID级别有如下推荐配置：





Provisioning Services中vDisk主要是读操作，而对Write Cache来说主要是写操作。所以：

l  **Write Cache****：**推荐RAID 0、1、10因为这几种RAID的写惩罚较低

l  **vDisk ****存储：**推荐RAID 0、1、5、10，它可以让读操作分配到RAID中的其他磁盘中；

如果可能，建议将vDisk放在RAID5上，而写缓存放在RAID10上。如果vDisk和写缓存一定要放在一起，那么建议采用RAID10。



12)     **决断：写缓存的位置**

写缓存可以有以下位置：

l  **缓存在Target Device****的硬盘上：**由于Provisioning Servers不用处理写请求，放在这里会减轻Provisioning Servers的资源消耗。尽管没有放在内存中这么快，这种方式的读写都是在本地，还是能提供快速的响应时间；****

l  **缓存在Target Device****的硬盘上永久保存：**和第一种方式类似，区别在于用户重启之后存储永久保存。该功能目前还是测试阶段，仅在Windows 2008 R2和windows 7上支持。

l  **缓存在Target Device****的内存中：**尽管这种方式在性能上是最优的，但是如果RAM别耗尽了也会印象系统的稳定性；

l  **缓存在Provisioning Server****的磁盘上：**缓存在Provisioning Server的磁盘上作为临时文件存储。所有的写操作均发生在Provisioning Server服务器上。这样配置当然会增加Provisioning Server的磁盘IO操作和网络负担。配置上这种方式最为简单，不过这种方式下target device由于所有的到写缓存的读写请求都必须经过网络，target device的性能会受到较大影响。这种方式仅在POC阶段推荐！

l  **缓存在Provisioning Server****的磁盘上永久保存：**和上一种方式基本类似，区别在于用户重启之后存储永久保存。这种方式的好处在于target device能够保存对vDisk所做的改变，在重启之后也仍然保留。任何对vDisk的改变都会将缓存文件强制标记为失效状态。例如，如果vDisk被设置为Private Image Mode，一下所有的操作都会导致缓存文件被标记为失效状态：

n  o  Placing a vDisk in Maintenance mode

n  o  Mapping the drive from the console

n  o  Changing the location of the write cache file

n  o  Using Automatic update

写缓存包含了target device的MAC地址和磁盘识别符，他能独一无二的区分出每一台target device。一个target device可以被分配多个vDisk，因此，也可以关联多个缓存文件。

将写缓存部署在target device上是最为推荐的配置方法，因为既不用消耗而外的RAM内存，又不会减少Provisioning Servers的扩展性。



13)     **决断：写缓存的大小**

写缓存的大小取决于很多隐私，一般来说都是基于评估和典型的用户配置文件大小。一般来说应当能够存储一下数据：

n  Temporary application data

n  User profile temp files

n  Windows Event Logs

n  Citrix Logs

n  Antivirus pattern files

n  Citrix Application Streaming/Microsoft App-V Cache

_备注：启用了用户配置文件重定向操作能减少写缓存所需要的大小。_



写缓存的大小极大程度上取决于安装或者是Streamed到vDisk上的应用程序的大小以及用户配置文件的大小。推荐配置的起点是2GB。对于大部分虚拟桌面来说，我们有如下推荐配置：



此外，Windows的pagefile也会写入和写缓存同样的磁盘中，所以：



例如，如果Windows 7的vDisk设计是1.5GB的pagefile，那么写缓存的一个安全的评估数据应该是：



不过由于Hypervisor都不能将磁盘精确到小数点后，我们姑且分配4GB的空间吧。



14)     **决断：****vDisk****的格式**

Provisioning Services支持固定磁盘以及动态磁盘格式。

l  **固定磁盘格式：**对于私有模式（private mode）的vDisk，固定尺寸大小的vDisk可以对存储vDisk磁盘上进行的磁盘碎片整理操作，这对写操作的性能提升会有帮助。不过在私有模式下，访问vDisk受限于一个target device，我们说仅当对vDisk进行维护模式时才有实际意义。

l  **动态磁盘：**相比较而言他需要更少的磁盘空间，但是在写操作上性能会显著降低。尽管在共享模式下（Shared Mode）的vDisk不会对vDisk执行写操作，不过对完成vDisk合并时所要花费的时间会增加许多。



15)     **决断：****vDisk****的大小**

vDisk的大小主要取决于操作系统以及安装在操作系统上的应用程序的多少，我们预估的大小如下表所示：





vDisk的大小如果设置的太小或者是太大，日后我们还可以在Provisioning Services中调整。为了精确的评估vDisk的大小，请遵循以下的准则：

l  **Target Device****的空间：**确认目前作为主target device服务的计算机所正在使用的磁盘空间大小；****

l  **应用程序大小：**当应用程序安装时，所需要的空间也在增长。计划大25%的增长



16)     **决断：****vDisk****复制**

如果vDisk是存储在DAS上就需要在他自己有变化的时候复制到其他DAS上。Provisioning Services支持vDisk从本地复制到Provisioning Servers上，也可以支持在使用共享存储时跨越多个站点之间的复制。复制可以是手动或者是自动：

l  **手动复制：**简单，但是更耗时；

l  **自动复制：**大型环境下自动复制更快。一些自动化工具，例如Microsoft DFS-R还支持带宽控制。唯一缺点是如果复制出错，管理员还不支持，除非复制平台支持复制重传。



17)     **决断：微软****Volume Licensing**

Provisioning Services支持Microsoft Key Management Service (KMS)和Multiple Activation Key (MAK) volume licensing。

l  **KMS Volume Licensing****：**可以在用户的本地网络上激活，无需连接到微软的网站。一台KMS服务器支持不受限的JMS客户端。微软公司推荐部署两台KMS服务器。****

n  Office 2010的部署只支持KSM激活方式；

l  **MAK Volume Licensing****：**MS的一次性激活方式。



18)     **决断：高可用**

Provisioning Services是虚拟桌面基础架构中最重要的组成部分，因此为了避免单点故障，需要考虑一下推荐步骤：

l  **MAK Volume Licensing****：**MS的一次性激活方式。

l  **数据库：**Provisioning Services支持两种数据库的高可用方式：

n  离线的数据库；

n  镜像数据库

l  **Provisioning Servers****（PVS****服务器）：**所有在一个站点之间的Provisioning Servers都能够被配置为向target device提供同一个vDisk。每个站点最少部署两台PVS服务器。

n  Provisioning Services启动文件应当配置为高可用。在启动文件中可以配置高达4台PVS服务器的列表。Target Device会按照顺序连接这些PVS服务器。后续所响应的服务器可以不是当初提供Streaming服务的服务器。当然，我们也可以配置负载均衡。

l  **vDisk****和存储：**对于DAS上存储的vDisk，应当做好同步操作。对于NAS上的vDisk，NAS存储必须提供一条高可用的网络共享连接；

l  **网络：**Provisioning Servers（PVS服务器）的网卡应当配置为Teamed。



19)     **决断：带宽需求**

带宽评估对于整体性能是有至关重要的，特别是当Target Device启动的时候。带宽是随着操作系统的不同而有所区别的。Target Device启动所需要的时间可以参考下面的公式：



例如，500个Windows 7的Target Devices在1G以太网下需要40M启动：

1.  1 GB Ethernet = 125MB/s

2.  500 targets x 40 MB = 20GB

3.  20GB/125MBs = 160 seconds

下面的表格列举了在10GB网络下启动500台不同操作系统的Target Device时大致的带宽和启动加载时间：





备注：防火墙会增加网络延迟，同时也会造成网络瓶颈，如果可能，最好禁用防火墙，如果实在不能避免，最好能开放一下端口的完全访问能力：





20)     **决断：网络配置**

为PVS服务器提供10Gbps网络能提供最够需要的带宽，如果做不到的话，1Gbps也可以提供足够的带宽，但是有可能会成为PVS服务器的瓶颈。将多块网卡做Teaming处理能提供更高的吞吐量，增加网络性能，也能阻止网络的单点故障。下表列出了PVS服务器的网络配置属性，从最大容量到最小：



以下的NIC属性应当正确配置在PVS服务器以及Target Devices的NIC上：



简单地说，就是禁用Checksum Offloading属性；关闭Auto Negotiation，使用强制配置；启用Jumbo Frame。



21)     **决断：交换机配置**

用于PVS服务器和Target Devices的网络交换机应当做一下优化：

l  **生成树协议（Spanning Tree Protocol****）/PortFast****：**禁用生成树协议，启用PortFast；

l  **风暴控制 Storm Control****：**在Cisco Catalyst交换机上将Unicast流量值设置大一些，或者是禁用Unicast Filtering。

l  **Broadcast Helper****：**启用之，这样可以转发PXE和TFTP流量；



22)     **决断：****Bootstrap****交付**

在一个Target Device开始启动过程的时候，他会首先加载一个bootstrap程序，该程序会初始化Target Device和PVS服务器之间的流化会话过程。有三种方法让Target Device能收到bootstrap程序：

l  **Broadcast Helper****：**启用之，这样可以转发PXE和TFTP流量；

l  **使用带有DHCP****选项的PXE****方式；**

l  **使用不带有DHCP****选项的PXE****方式；**

l  **使用Boot Device Manager****；**

在企业无法提供PXE或者是TFTP服务的情况下，或者是无法对DHCP Scope选项修改的情况下，可以考虑使用Boot Device Management工具通过一个ISO文件来提供bootstrap文件。



23)     **决断：审计**

默认下审计功能是禁用的，管理员可以将将其打开。打开后该工具可以记录在Provisioning Services场内组件所做的配置修改记录，并将结果记录至数据库中。



24)     **决断：防病毒**

大部分的防病毒软件都会是扫描所有的文件和系统进程，对性能影响很大。所以在PVS环境下必须优化防病毒软件的配置。请参见CTX124185 - Provisioning Services Antivirus Best Practices。
