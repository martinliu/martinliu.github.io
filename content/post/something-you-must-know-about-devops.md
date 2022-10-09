---
title: 关于DevOps 的那些事
subtitle: 我对DevOps的一个比较宏观的总结
date: 2017-09-23
image:  "/images/tf_5.jpg"
tags:
- DevOps
---
DevOps是孕育于敏捷社区，又反哺给整个IT技术行业的，是一次彻底而全面的技术和文化运动。本文从它的出处谈起，一直描述到当前国内的现状。最后总结了相关的核心技术和主要实践。

## DevOps简史

在2008年多伦多举办的敏捷大会（Velocity Conf 2008 ）上，Patrick DeBois 和AndrewClay Shafer 先生首次提议讨论“敏捷基础架构”这个话题。在第二年的敏捷大会上有一个具有里程碑的意义技术分享，来自Flickr公司《每天部署10次》的分享，它激发了随后Patrick DeBios在同年十月，在比利时的根特市举办的首届DevOpsDays活动，这个活动是两天的日程，为了大家方便在twitter上的传播，人们把DevOpsDays这个词简写为 “#DevOps” 。 此后，“DevOps”一词问世了，这个词所包含的理念和实践一时在越来越广大的人群中产生了共鸣，随后成为全球IT界在各种大会和论坛里热议和讨论的焦点话题，很多大型IT论坛也都开设出了DevOps专题讨论。这就是DevOps这个词的由来。DevOpsDays活动随后在Patrick DeBios等相关核心发起人的推动下，在全球范围内蓬勃发展了起来。2010年在美国山景城(Mountain View) 举办的DevOpsDays 活动中，Damon Edwards先生使用“CAMS”这个缩写，高度概括和诠释了DevOps，即文化（Culture）、自动化（Automation）、度量（Measurement or Metrics）和分享（Sharing）。随后Jez Humble先生将“L”精益 (Lean) 原则也加入其中，最终变成了CALMS。


* Culture（文化）- 是指拥抱变革，促进协作和沟通
* Automation（自动化）- 是指将人为干预的环节从价值链中消除
* Lean（精益）- 是指通过使用精益原则促使高频率循环周期
* Metrics（指标）- 是指衡量每一个环节，并通过数据来改进循环周期
* Sharing（分享）- 是指与他人开放分享成功与失败的经验，并在错误中不断学习改进


“CALMS”完全吻合Patrick DeBois先生所一向倡导的“DevOps is a human problem” (DevOps 是关于人的问题) 的理念 。


## DevOpsDays活动的现状

从DevOps概念的产生，到如今它在全球范围内的蔓延和认同，已经经历了9个年头的时间。它的火爆推广也伴随着IT行业的迅速变迁和发展，现在已经到了移动互联网时代的后半场，国内的信息化建设已经完成了很多年；如今各行各业的企业也都亟待完成全方位的数字化转型。IT信息技术的先进程度标志着一个企业的核心能力，任何一个成功的企业，敏捷高效的软件开发创新实力和IT管理综合能力不只是门面而已，而是实实在在的市场竞争能力。DevOps倡导打敏捷、持续交付和ITIL三种实践的组合拳，同时应用精益生产理念为基础的管理思想，这正在逐渐地被广泛的接受和认可。

![devopsdays-map](/images/devopsdays-map.png)


在过去的几年中，国内的各种IT大会也蓬勃发展，其中DevOps相关的专题和分会场也颇受人们的关注。各种云计算、运维等IT技术的社交媒体也都非常重视DevOps这个话题的分享。一个专属于DevOps社群的、国际性的、有影响力的DevOps大会正呼之欲出。在这样的时代背景下DevOpsDays大会北京站在2017年的3月18日来到中国，在同年的8月18日上海，还要举办DevOpsDays Shanghai站的大会。

下面列举一些DevOpsDays大会的相关数据，<a href="http://xn--DevOpsDays-cp3p571r5pfpshp63a.org">数据来源于DevOpsDays.org</a> 网站。从2009年到2016年，已经在全球的61个城市/国家成功地举办了117场。

![year-map](/images/year.png)


<p>下图是在过去九年中DevOpsDays大会在各个城市/国家的分布和举办次数。</p>

![year-map](/images/devops-citys.png)


<p>今年也就是2017年预计举办30场，其中已经有18场确定了举办城市和日期；还有12个城市的召开日期待定；这不包括年内还可能会提出申办的城市。以上数据的统计时间在2017年三月。</p>
<h2 id="devops">DevOps在国内的现状</h2>
<p>随着国内BAT等互联网巨头的崛起，互联网公司的开发运维经验也越来越多的在国内的各种技术大会上传播。从最近这两年（2016年和2017年）的技术活动日程中可以看出，国内互联网从业人员也不约而同的用DevOps来定位和分享自己的优势和经验。他们是传播和分享运维侧DevOps实践的先头部队。</p>
<p>出了技术论坛的分享之外，很多线上线下的大会、论坛和讨论组也都越来越热议DevOps这一专题。国内其它相关流派的人群，例如敏捷和精益等，也对DevOps的蓬勃发展表示比较惊讶，DevOps与老牌的敏捷和精益等阵营也产生过一些争论。但这一切的发生也都增加了人们对于DevOps的更深入的兴趣。</p>
<p>在培训认证这方面，Exin DevOps Master是一个国际认证的培训；其它公司和组织也正在举办关于DevOps工具链的培训，这些培训则注重于技术实操，关注在构建端到端的流水线的搭建方面。从DevOps的职位招聘方面，可以看到DevOps工程师相关的职位越来越多了，在职位需求中DevOps这个技能成了加分项，DevOps相关工具的技能也或将成为简历的亮点。在IT行业内不管是开发还是运维团队的人，都开始了学习和接受的过程。</p>
<p>据我观察DevOps方面的厂商在最近3年呈现爆炸式的发展。我把他们分为三类：</p>
<ol>
<li>搭顺风车型：主要是指所有CaaS容器云平台厂商 。Docker是它是在DevOps的时代背景下产生的，是DevOps技术工具集里不可缺少的一员。国内这些厂商目前的数量在20左右，数目趋于稳定。由于今年（2017）Docker公司商业化版本和开源版本正式的划分开来，这些公司的发展可能或多或少受到一些影响。</li>
<li>直奔主题型：这类厂商专注于开发端到端的、用户体验良好的DevOps流水线平台，这些公司的创始人团队多是来自于BAT公司，因此具有很好的DevOps实战经验，他们开发的产品在持续交付和流水线功能上恰好填补了当前企业在这个方面的工具和技术实践的缺位。目前这类公司的数量还不多，数量呈上升趋势。</li>
<li>BATH型：BAT大家都知道，这里的H指的是华为，这些企业在DevOps平台方面都表现出积极的技术输出的态势。BAT是基于过去的互联网运维的经验做DevOps的产品化。华为是成了独立的研发部门，招募业内这方面的精英前来助阵，打造出一方面可以自用，同时也可以商品化的DevOps产品。</li>
</ol>
<p>目前国内大部分企业慢慢地开始关注了DevOps，大型传统企业也开始逐渐地从各个角度做试点和尝试。试点的角度和方向各不相同，有的从底层基础架构的容器化开始，有的从交付部署流水线的自动化开始；总的来说还处于初级的尝试阶段，还没有大规模成体系的推广。</p>
<p>综上所述，目前国内DevOps发展的阶段还属于起步阶段。就像是ITIL/ITSM在2003年左右的状态。由于DevOps是去中心化的，所以没有唯一、权威的上游厂商的存在，各种理论实践的争执和PK都将终止与解决问题和提高效率的话题上，因此它具有百花齐放百家争鸣的发展条件。个人认为DevOps的实施和落地也不会完全依赖于传统的大型咨询厂商的咨询工作，由于它应该是在企业的内部，在内驱的作用下，自生长出来的；它必须是服务于企业的业务价值流的优化，加速业务价值产出的；而与之相关的工作和责任的担当，外部力量是很难以等量替换和承担的。</p>

<h2 id="">核心技术和工具</h2>

在谈这个话题前先看一下DevOps相关工具集的全貌，如下图所示：<br>

![year-map](/images/devops-tools.png)



<br>
最上面的箭头流程图表示了一个业务服务的全生命周期：开发协作、软件构建、质量测试、交付部署和投产运维。前三个阶段偏传统开发组织的工作内容，后两个阶段基本可以和运维组织的工作对应上。在每个阶段下可以看成是一个大分类，这些分类中还包含若干个小分类。这些工具可以粗放的划分为商业软件和开源软件两类；也可以分为SaaS服务类和企业内部部署型。大部分开源工具都有活跃的用户社区和群众基础，这给企业入手这些工具带来了很大的便利。在需要商业支持的场景里还可以选择使用这些开源软件的企业版。</p>
<p>Docker容器技术在最近三年中异军突起，持续交付的技术门槛因此被降到最低，软件生产供应链的格局和效率被彻底提升；基于Docker的微服务架构实践的热度和成熟度也与日俱增。因此，国内的传统企业纷纷试水DevOps和容器技术，在最近两年的各种技术大会中，我们可以看到国内各个行业出现了在不同维度上的DevOps先行者。他们分享的主题大多集中在自动化运维、容器化和PaaS平台的等项目经验。</p>
<p>从国内众多DevOps实践中，我们能看到下面三个技术尤其重要和火热：</p>
<ol>
<li>容器：容器从根本上解决了软件对环境的依懒性，解决了各个环境之间的差异问题；它可以加速部署的速度，提高部署的效率；降低部署的成本。容器技术是在Linux的基础之上发展起来的，因此它本身的实施成本很低，就是在任何物理机和虚拟机的Linux操作系统上安装Docker服务（仅几十兆）就可以完成所有功能。在任何环境中实施Docker需要考虑好以下几个因素：主机的计算资源特性和容器允许的资源需求相匹配（计算密集型、内存密集型、IO密集型等）；容器网络类型和服务路由的选型；容器镜像仓库的选择等。</li>
<li>持续部署：这是所有企业普遍的短板，需要设计统一的自动化部署流水线作为软件系统部署和更新的基础设施。持续部署流水线底层是有Jenkins之类的工具来完成的，它能实现快速的、可重复使用的、适用于不同部署环境的发布流水线。所有服务都可以通过它实现各种风格的发布；这些发布风格中比较重要的两种：蓝绿部署和灰度发布。</li>
<li>微服务：为了解决传统软件所特有的单体应用的缺陷，用微服务的思路，全面地重构巨石应用，全面的在新系统中应用这种架构。微服务架构是容器技术出现之后，有迅猛发展的一项软件架构技术。它的松耦合和面向服务基础架构的特性都是现代软件和数据中心必备的特质。<br>
以上三种技术相辅相成，有着比较深刻的关联。首先微服务和持续部署各自解决了特别多的传统IT的问题，这些问题都是长期以来制约企业业务发展的难题。容器技术由于它的快速、轻量、微服务化的天然特性，很好的从不同侧面支持了持续交付和微服务架构。容器可以为持续交付提供弹性和高速的系统资源，环境管理和利用率提高了很多；容器的不可变性的特点也更好地支持了微服务架构。</li>
</ol>
<p>我把DevOps的按照不同的技术特征做了从到1.0 到2.0的时代划分，并尽量通过以下维度比较与传统方式的差异。</p>

![year-map](/images/devops-v20.png)

<h2 id="">总结</h2>

<p>我比较认可和接受的企业实践DevOps参考框架如下，其中包含了所需的最佳实践，如下图所示。</p>

![year-map](/images/devops-house.png)


（上图来源于：Exin DevOps白皮书）</p>
<p>下面简要描述一下这四大支柱型最佳实践</p>
<ol>
<li>敏捷管理：在产品的计划、需求、设计和开发阶段主要采用敏捷开发方法论。在这些阶段中DevOps强调，设置合理的任务大小，从而确保能够开展快速迭代和开发；强调持续集成的实施，通过CI提高软件的质量和可用性；强调用更短的发布周期，增强反馈的数量和频度。</li>
<li>持续交付：在开发和部署运营阶段采用持续交付的方法自动化软件系统的发布、变更和升级等工作。DevOps强调使用持续交付工具作为基础架构尽可能的自动化手工部署工作。在研发阶段就开始设计部署自动化的脚本，对其使用流水线工具来操作执行，并辅助自动化测试工具。通过严密的自动化测试方案，确保实现可以重复使用的自动化部署流水线。通过它的反复运作，提高部署的效率，降低部署的风险，提高部署的质量。</li>
<li>ITSM服务管理：DevOps强调从传统的ITSM管理理念上升到关注业务持续性的轻量ITSM管理方法。运维人员在项目的早期要和开发、测试和部署人员充分地沟通和落实运维需求。确保在业务系统开发的初期，系统的业务持续性和可运维性等非功能性需求，都得到充分的落实和满足。</li>
<li>精益管理：业务开发运维的整个生命周期中，以上三类工作实践的所有工作活动中，都必须坚持贯彻精益的原则。DevOps特别强调的点包括：准时制业务流程、精益且无浪费的工作方法、单件流的运作流程、持续改进等。它的这些管理思路需要严格的落实到所有工作环节中。</li>
</ol>
<p>由此可见DevOps在企业，特别是大规模传统企业的落地和推广还是比较复杂的。虽然相关的最佳实践都是已经存在了很多年的；但是，通过DevOps的价值观重构企业从研发到交付到运维的价值流谈何容易。基于我的IT从业经验，我似乎感觉到DevOps不能单独依靠自顶向下的推广，当然高层领导的支持依然是重要的和必备的支持条件之一。 可能还需要中层的带动和底层的创新；借鉴生产制造业已经久经考验的精益制造实践也是势在必行。总之DevOps运动会在近几年给IT行业带来较大影响。</p>
