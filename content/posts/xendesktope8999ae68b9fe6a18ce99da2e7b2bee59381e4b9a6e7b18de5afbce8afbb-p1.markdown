---
author: liuadmin
categories:
- XenDesktop
comments: true
date: 2013-04-09T02:19:37Z
slug: xendesktop%e8%99%9a%e6%8b%9f%e6%a1%8c%e9%9d%a2%e7%b2%be%e5%93%81%e4%b9%a6%e7%b1%8d%e5%af%bc%e8%af%bb-p1
tags:
- Access
- deploy
- Design
- FlexCast
- Manitain
- XenDesktop
- 虚拟桌面
title: XenDesktop虚拟桌面精品书籍导读(part1)
url: /2013/04/09/xendesktope8999ae68b9fe6a18ce99da2e7b2bee59381e4b9a6e7b18de5afbce8afbb-p1/
wordpress_id: 52322
---

[box color="orange" icon="flag"]
感谢 Eric Yao 的供稿，[@老树皮Eric](http://weibo.com/ericyaozhen)
[/box]

桌面虚拟化项目的实施白皮书 《Citrix Virtual Desktop Handbook 5.x》，[点击下载](http://support.citrix.com/article/CTX136546)。该文档是由Citrix全球顶级Consultant系统架构师Daniel Feller, Thomas Berger, Rich Meesters, Matt Brooks, Ed Duncan 以及 Roger LaMarca等大牛合作完成，它介绍了桌面虚拟化架构设计、方法论、经验总结以及最佳实践等知识，更是包含了一步一步指导手册、真实案例分析以及模板手册等。

序言：关于方法论
一、 Access
二、 Design
三、 Deploy
四、 Manitain
五、 项目计划

第一部分：Access
一、 业务驱动力
二、 数据搜集
三、 用户数据搜集
四、 应用程序数据搜集
五、 用户分类
1. FlexCast模型比较
2. FlexCast模型选择
六、 应用程序评估
七、 项目管理
1. Roadmap
2. 项目团队
a) 业务角色
b) 技术角色

第二部分：Design
一、 概况
二、 用户层 User Layer
1. 终端类型的选择
2. Receiver的选择
3. 资源需求
三、 访问层 Access Layer



序言：关于方法论

Citrix Virtual Desktop handbook会紧密遵循Citrix顾问实施方法论，即如下图所示：



一、 Access

Access阶段主要提供Design阶段所需要的信息，包括：

1. 业务驱动力；

2. 数据搜集：包括用户、应用程序、设备以及基础架构；

3. 用户的分类：用户要根据需要的分类而分成不同的组别，随之应对着不同的FlexCast方法论；

4. 应用程序分类：旧的应用程序应该被删除、应用程序版本应该标准化、非公司程序应该删除，等等这些构成了应用程序的标准化和合理化；

5. 计划：每个用户组都要根据对业务的影响程度指定不同的实施时间优先级，优先级实施进度结果应该随时更新项目进度和计划。

二、 Design

设计阶段主要聚焦在五层的一个方法论上：

1. 用户层：描述推荐的终端以及所需要的用户功能体验；

2. 访问层：描述用户层是如何连接到他们的桌面，例如本地桌面是直接连接StoreFront，而外界用户往往要通过Firewall层才能进来，这就涉及到了FW、VPN等技术；

3. 桌面层：主要指用户的虚拟桌面实现技术，即FlexCast技术，主要好汉三个主要成分，分别是镜像文件、应用程序，以及个性化内容；

4. 控制层：如何管理和维护其他层，又分为访问控制、桌面控制，以及基础架构控制；

5. 硬件层：致力于支撑整个解决方案的硬件物理设备，包括了服务器、CPU、内存、存储设备等；

三、 Deploy

按照第二部分设计好的FlexCast方式实施。

四、 Manitain

主要包含三种不同的活动：

1. 监控：在虚拟桌面环境设计和实施到生产环境以后，持续的监控是必需的。

2. 技术支持；

3. 测试和变更管理：以后会遇到不断的软件和产品更新；

五、 项目计划

一个设计详尽的项目计划对项目成功的实施时至关重要的。项目经理要通过项目计划来监控成本、管理项目组成员、跟进项目实施进度等。同时项目进度要及时通告项目组所有成员让大家都知道项目的进度。

在项目的初期一般只需要做Access阶段的计划，这个时段需要多FlexCast模式、容量、用户分组等有更多的交接，所以无需做Design的计划。如下图所示就是一个计划表：

第一部分：Access

一、 业务驱动力

桌面虚拟化项目的第一步应该是去了解对公司所造成的影响，并且将这些影响定一下来，然后对之以优先级排序。有了这些文字描述管理层和项目管理组才能制定出项目成功实施的标准，设计阶段才能有正确的方法论和架构设计。

下图就定义了一个业务驱动力的优先级示例：

二、 数据搜集

数据搜集阶段负责搜集关键信息数据，包括用户、设备、应用程序，以及基础架构等在下一阶段需要使用的数据。

有三种方法来搜集数据：

1. 手动搜集

小型企业有可能通过访问每台终端，或者是远程连接凡是来搜集数据。

中大型企业一般般都有了ESD（Enterprise Software Deployment），例如微软的SCCM等。可以通过这些平台去搜集应用程序的使用情况等信息。但是ESD一般都不能提供应用程序性能需求和实际使用的信息。

2. 调查表

这也是一个好办法，可以通过管理层去通过行政命令来执行。也可以通过面对面的会议或者是电话沟通来进行；这种方式比手动搜集要显著减少了所花费的时间，但是完成率不高也是一个缺点，不够精确反应实际情况也是一个缺点。

3. 自动化搜集

这样的工具有很多，一般都能自动化生成报表。Citrix公司为了帮助用户节省实施成本，和LanDesk公司合作，为Project Accelerator用户提供了一个60天免费试用的LanDesk FastTack 软件License。LanDesk FastTack 软件是一个专门为Citrix实施方法论开发设计的一个专业信息搜集工具。

上述三种方法的优势和劣势如下表所示：

三、 用户数据搜集

信息搜集表可以参考示例表格：Citrix Virtual Desktop Handbook - Assess Workbook.xlsx

1. 业务特性

业务特性必须通过业务层的管理人员来手动搜集，无法自动化搜集。包括

A. 身份

a) 用户名

b) 部门；

c) 角色

d) 业务经理

e) 所分配的用户组；

B. 业务

a) 主要的数据中心

b) 移动性，下表是示例分类

c) 个性化

d) 安全性

e) 关键性

2. 技术特性

a) 工作负荷

3. 用户环境

a) 用户Profile

i. Profile类型：包括本地、漫游、强制、第三方、未知

ii. Profile版本：Windows XP和Windows Vista/7

iii. Profile位置：文件服务器在哪里

iv. 大小：用户Profile的大小

b) 用户数据主目录

i. 主目录位置

ii. 大小

4. 客户端硬件，包括以下需要搜集的信息：

o Number of CPUs/Cores

o CPU Speed (GHz)

o Memory (GB)

o Disk Size (GB)

o Operating System

o Age of the System (years)

o Peripherals

5. 本地资源映射，包括以下需要搜集的信息：

o Local Drives

o Printing

o Clipboard

o Audio

o COM Port

o USB

o LPT

四、 应用程序数据搜集

信息搜集表可以参考示例表格：Citrix Virtual Desktop Handbook - Assess Workbook.xlsx

1. 身份信息

a) 应用程序名称和版本

b) 应用程序所有者

c) 状态

2. 应用程序技术特性

a) 分配

i. 使用者数量

ii. 部门信息

iii. 个别用户

b) 工作负荷

c) 业务特性

d) 兼容性

五、 用户分类

一旦数据搜集工作完成之后，我们就可以开始准备将用户分成不同的组了，这个时候就要按照FlexCast模型的要求去分配不同的实现方式给不同的用户组了。

我们一般都是按照人物性工作者、分支机构办公人员、移动工作者等方式去区分用户，但是实际上用户的分类远不止这几类，更有甚者，很多用户组都是同时属于上述几个组的。

最快区分用户的方法就是按照用户的需求不同来分组，一旦将用户的需求区分之后，就可以将这些数据填入Citrix Virtual Desktop Handbook - Assess Workbook.xlsx 了。

1. FlexCast模型比较

1) Hosted Shared

2) Hosted VDI，又可以细分为

a) Pooled-Random/Streaming

b) Pooled-Static

c) Pooled/Streamed with Personal vDisk

d) Dedicated

e) Existing

f) Psysical/Remote PC

3) Steamed VHD

4) Local VM

5) On-Demand Apps



下表是关于FlexCast整体技术的一个概览：

2. FlexCast模型选择

在XenApp和XenDesktop之间有很多技术上的区别，但是他们都是通过HDX来提供的最佳用户体验。他们的区别如下：

六、 应用程序评估

在用户分组完成之后，我们已经有了根据需求不同确定下来的不同的用户组，下一步就是向用户提供他们工作需要的应用程序。下面是建议的三部曲：

1. Rationalization 合理化

2. Business Characteristics 业务特性

3. 兼容性



七、 项目管理

1. Roadmap

2. 项目团队

下面的表格示例告诉我们在一个虚拟桌面项目中可以建议的业务角色和技术角色分类。虽然角色有很多种，但是很多角色的存在时间都很短，同时很多角色都由一个人同时完成。项目经理和Citrix架构师自然是贯穿整个项目的角色，其他就不一定了。

a) 业务角色

b) 技术角色
