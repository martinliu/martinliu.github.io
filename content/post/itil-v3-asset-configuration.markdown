---
author: Martin Liu
categories:
  - CMDB
comments: true
date: 2010-12-20T03:01:40Z
slug: itil-v3-asset-configuration
tags:
  - cmdb
  - ITIL
  - ITSM
title: "[ZT]ITIL V3 服务转换篇 之 资产和配置管理"
url: /2010/12/20/itil-v3-asset-configuration/
wordpress_id: 50844
---

为了定义和控制服务和基础设施组件。维持当前计划中、历史的服务和基础设施状况配置信息的准确性
**一、先介绍几个基本概念
**1、配置项（CI）
配置项是正在或将要在配置管理控制下的资产、服务组件或其他。配置项在复杂性、大小、种类有很大不同，从整个服务或系统包括硬件、[软件](http://portal.vsharing.com/industry/1593.html)、文档、支持人员到单独软件模块或硬件组件。配置项可以集中或分组管理。配置项可以选择使用既定的选择标准、分组、分类和识别方式在整个生命周期中管理和追溯。其包括：
A) 服务 CI 项：服务能力资产、服务资源资产、服务模式、服务包、发布包、验收标准等
B) 组织 CI 项
C) 内部 CI 项
D) 外部 CI 项：包括外部客户需求和协议、供应商发布、分包商及对外服务。
E) 接口 CI 项：端到端的服务，跨越服务提供者的接口
2、配置管理系统（CMS）
为了管理大型复杂的 IT 服务和基础设施，资产和配置管理需要使用配置管理系统 CMS。在指定范围内 CMS 掌握着所有配置项信息。CMS 为所有服务组件与相关事故、问题、已知错误、变更发布、文档、公司数据、供应商、客户信息做关联。
在数据层面 CMS 能使数据库存在多个物理 CMDB 中而后共同组成一个联合的 CMDB。其他数据来源也可以加入 CMS 中。
3、配置管理数据库(CMDB)
所有配置项的信息都包括在配置管理数据库(CMDB)中。配置管理数据库(CMDB)对所有 IT 组件、组件的不同版本和状态以及组件之间的相互关系进行跟踪。在其最基本的形式下，配置管理数据库(CMDB)可能仅由一些纸质表格或一套电子表格 (Spreadsheets)组成。
4、最终介质库(DML)
DML 是用来存储和保护所有已授权的被确认版本介质配置项。 他们存储经过质检的主拷贝版本。这个库可以有一个或多个软件库或存放区来存放开发、测试和实时存储文件。他们包含组织所有软件的主拷贝、购买软件的副本及 受控文件的电子版。DML 包含物理的拷贝存储，DML 是发布管理的基础。

**二、配置管理的目的：
** 1.  确定、控制、记录、报告、审计、验证服务资产和配置项包括版本、基线、组成成分、属性和相关关系。 2.通过服务[生命周期管理](http://plm.vsharing.com/)保护资产完整、配置项等账户。确保只有已授权的组件被使用和已授权变更被执行。 3.通过服务生命周期保护服务资产、配置项的完整性。为了建立和维持一个准确和完整的配置管理系统，确保资产和控制服务、IT 基础设施的配置需求的完整性。

**三、资产、配置管理的活动**

![](http://blog.amteam.org/Uploads/UserDirs/3/1169/467255/b%281%29.jpg)

[![点击查看原图](http://blog.amteam.org/Uploads/UserDirs/3/1169/467255/b%281%29.jpg)](http://blog.amteam.org/Uploads/UserDirs/3/1169/467255/b%281%29.jpg)

1、规划
2、识别
配置项识别过程：
A) 定义和制定标准文件来选择配置项和他们的组件构成
B) 依据标准选择配置项及其组件并记录他们
C) 给配置项分配唯一的标识符
D) 指定每个配置项相关属性
E) 确认每个配置项是受配置项管理来管理
F) 确定每个配置项的责任人
3、控制
必须有效控制信息以维持配置管理数据库(CMDB)的及时更新。一旦某项活动改变了配置项已记录的特征或配置项之间的关系，则必须在配置管理数据库 (CMDB)中记录该项变动。需注意的是：只有变更管理才有权批准对配置项的特征进行变动，事件管理只能改变某个现有的配置项的状态来反映现实状况。
配置管理负责控制组织接收到的所有 IT 组件并需确保这些组件被记录在系统中。硬件可在其已订购或已交付时进行记录，而软件则通常在其被纳入 DML 时进行记录。
4、记录
组件的生命周期可被划分成多个阶段，每个阶段都可以分配一个状态代码，但具体分成几个阶段则取决于公希望记录 IT 基础设施的哪些特征。保持对每次状态变化日期的记录可以提供关于一个产品的生命周期的有用信息，如订购时间、安装时间以及所需的维护和支持。组件的状态决 定了可以对其进行操作的余地。
5、审核和报告
执行审计是为了核实配置管理数据库(CMDB)中记录的信息是否仍然反映了当前的现实状况。这些信息可用来检查和更新配置管理数据库(CMDB)。
在下列情形下需要执行审计：
A) 在建立了新的配置管理数据库(CMDB)之后；
B) 建立配置管理数据库(CMDB)一段时间之后；
C) 重大变更之前或之后；
D) 灾难恢复之后；
E) 其他任何方便的时候。
审计也可以随机地或在配置经理认为配置管理数据库(CMDB)中的信息不正确时进行。如果配置管理系统与审计工具之间存在关联，则可以每天生成针对某个相 关领域的审计报告。在发现差异时，不应该允许审计工具自动更新配置管理数据库(CMDB)。所有的差异都表明变更管理流程可能被忽视了，所以应该对这些差 异进行调查并通过变更管理对这些差异进行追溯性处理。
**三、配置管理管理报告**
配置管理流程的管理报告可能包括下列信息：
a) 有关流程质量的信息；
b) 在审计中发现的记录与实际情形不符的次数；
c) 发现未经批准的配置的次数；
d) 出现已记录的配置不能被找到情形的次数；
e) 审计中发现的有关配置项属性详细程度方面的差异；
f) 处理信息记录请求所需的时间；
g) 超过给定事件或变更次数的配置项的列表；
h) 有关 IT 基础设施的结构和组成的统计信息；
i)  有关 IT 基础设施发展情况及其他方面的信息；
j) 有关改进措施的总结、报告和建议，例如，针对由于业务、技术、市场价格和其他相关变化所导致的配置管理追踪记录的配置项的范围和详细程度的变更所提出建议；
k) 有关实施流程所耗费的人力成本的清单。

**四、配置管理的绩效指标指标**
a) 闲置许可数量;
b) CMDB 错误导致变更失败的数量;
c) 未授权配置数量;
d) 配置项文档错误导致变更失败所引起的事故数量;
e) 因为 CMDB 错误导致违反 SLA 的数量;
f) 无相应配置项刷新的变更请求数量;
g) 不精确配置项百分比;
h) 客户满意度 ;

**五、与其他流程的关系**

![](http://blog.amteam.org/Uploads/UserDirs/3/1169/467255/a.jpg)

转帖学习一下。

From [http://blog.amteam.org/standard/A1159174.html](http://blog.amteam.org/standard/A1159174.html)
