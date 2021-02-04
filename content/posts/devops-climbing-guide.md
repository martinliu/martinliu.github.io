---
title: "DevOps登山指南"
date: 2018-02-20T00:34:09+08:00
draft: false
description: "DevOps 案例研究 DOES17 San Francisco - DevOps Handbook Experiments in Accelerating Delivery - Nationwide"
subtitle: "美国金融行业Nationwide保险公司DevOps案例研究，来源DOES17 San Francisco，主题-DevOps Handbook Experiments in Accelerating Delivery"
tags: ["DevOps"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/q_auto:eco/Evest.jpg", desc: "DevOps案例研究-Nationwide"}]
postmeta: false
nocomment: true
---

全美互惠保险公司(Nationwide)美国公司。在2017年6月7日，《财富》2017年美国500强排行榜发布，全美互惠保险公司排名第68位。营业收入40074.1百万美元。

这家公司是DevOps Handbook（DevOps实践指南）书中的案例研究之一。这是一家DevOps水平较高的企业，是DevOpsDays大会上分享嘉宾的常客，也是各个DevOps工具厂商（New Relic）经常邀请的案例分享嘉宾。他们也经常参加DevOps企业峰会，曾多次做过自己的DevOps应用状况案例分享。

本文分析和整理了他们在2017年11月旧金山站DevOps企业峰会上他们的演讲，主题为《DevOps Handbook Experiments in Accelerating Delivery - Nationwide》（翻译：使用DevOps Handbook在加速开发交付的过程中的实验）

本文根据这个演讲的YouTube视频整理而成。视频已经上传到腾讯视频，[点这里观看该视频。](https://v.qq.com/x/page/v0555haemus.html)

-------


## DevOps登山指南手册

我在翻译DevOps Handbook的过程中，感觉书中所描述的这家公司的案例研究，并不像本演讲里所说的这样的精彩。

而时光已经很快的流转到了将近2018年，他们的DevOps也经过了几年的发展，本文案例向我们展示了一个金融行业（我们往往认为不太容易实施DevOps的行业）企业，在很大的企业规模了，所取得的令人敬佩的成就。

下面这张图是本文的精华，先给各位呈现出来。他们使用攀登珠穆朗玛峰做为比喻，对DevOps的实施做了生动的诠释。

![DevOps登山指南手册](https://res.cloudinary.com/martinliu/image/upload/devops-climbing-guide.jpg)

本图在Nationwide公司内部的使用场景如下：

1. 本图将DevOps实施核心团对指导产品开发团队（也可以说是业务团队、服务团队、这样的团队他们有200多个）取得的经验总结在一张纸上，供其它有实施DevOps想法的团队参考。
2. 该登山指南简化了对其它非DevOps团队的教育和指引。
3. 他们将DevOps的实施分成三个阶段，分别用大本营、北坡营地和顶峰作比喻。
4. 这三个阶段里的技术实践都来自于DevOps Handbook，通过他们的筛选和整理，并根据自己的经验做了分阶段的规划。

为了知其所以然，我们将继续向下发掘，详细了解这个案例分享所讲的主要内容。下面的内容也包含了我对他们的分析和评论，欲了解原始资料，请请参看我上传到腾讯的视频。

-------



## 主题：DevOps Handbook-在加速交付中的各种实验

分享者介绍。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-001.jpg)

这个演讲距2018年2月也就是三个月，还算是很新鲜的一个案例。Cindy是DevOps团队中的核心人员之一，她的头衔是Director，角色是夏尔巴人（后面会详细解释这个比喻的含义），为业务产品组提供内部的DevOps咨询和辅导。Jim属于业务条线/BU的Dev这一侧，他是业务部门的解决方案架构师。

## Nationwide的核心价值：保护对你最有价值的

公司简介和状况。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-002.jpg)

* 在很多险种上Nationwide都在业内排名第一名，包括：宠物保险、农场保险、公司寿险等等。
* 这是一家有90年历史的老店
* 汽车保险也行业排名第八（后面就是用这个业务为例，来佐证DevOps实施的效果）
* 不光在财富500强企业排名68，还是财富所评选的前100个最佳的工作企业。

-------



## Nationwide IT的规模很大

IT组织的特点和相关数据。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-003.jpg)

* IT组织庞大，结构复杂，业务条线众多
* 在选择应用某个DevOps实践的时候，总是要考虑到规模因素，需要评估该实践是否能在200多个业务开发团队的规模上全面地推广和实施
* IT人员总数超过5100人，其中程序员和测试人员的数量超过2600人；在电脑世界的IT最佳工作地点的排行帮上位居第51名
* 该公司有用200多个产品开发团队，他们服务于23个业务部门BU

-------



## Nationwide IT的组织结构

典型、复杂和庞大的组织结构

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-004.jpg)

* I&O是基础架构和操作运维团队，该组织不仅运维了所有的IT服务，还服务于所有的业务开发团队。
* 多个共享服务团队提供企业级的共享服务，包括Scrum测试等传统开发服务，同时也为企业内部的DevOps实践提供技术咨询，他们支持所有类型的企业应用堆栈
* 业务部门如前所述有23个，有200多个开发团队，Jim服务于金融业务BU
* 该公司的架构模型近似于典型的Dev、QA和Ops架构；他们的Ops组织也是集中式的；如此复杂的架构带来了DevOps流水线的复杂度方面的挑战，为某个业务BU实施的持续交付流水线会横跨多个BU，有时候甚至需要三个BU的CIO级别领导一起来参与决策，这里也会出现项目投资方和项目决策方不统一的难题。

-------



## 从哪里开始

应用DevOps的企业环境背景和定位。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-005.jpg)

* IT组织十年以来追求的战略目标：构建具有全球竞争力的内包式软件开发能力；为此而采用了不同的管理框架和实践，应用和开始的时间点也不同
    * Agile：敏捷软件开发是10年前就开始的，定位和目标是通过敏捷软件开发交付高质量的软件
    * DevOps：今年加入了DevOps实践，定位是如何实现速度、效率和降低风险。
    * Lean IT：定位是确保将IT管理的各种实践（包括以上的敏捷和DevOps）提升和推广到企业级规模。（他们认为在团队级别上任何敏捷和DevOps相关的实践都是很容易实现的，而企业级规模的推广是更高等级的管理，是不容易达到的）
    * CMMI：使用行业规范的软件开发成熟度标准评价和考量自身的软件开发能力，为自身的不断提高提供标准参考。
* 该公司DevOps实践是最晚开始应用的，其它的三个方面使用的历史比较长了，为了达成一个战略目标，需要4个战术层面实践的支持，这些战术的采用时期和定位不同；4个战术从不同的侧面支持了战略目标的实现。该企业也在Lean IT的论坛上分享和演讲过。


-------


## 从哪里开始（续）

应用DevOps的时间轨迹和历程，各个时期的关键词。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-006.jpg)

* 2015-简化：DevOps小屋是入手DevOps实践时，最早使用过的参考框架；他们分析梳理了所有相关的方法论；工具方面专注在部署工具的改进上，所有产品线采用了IBM UrbanCode作为统一的部署工具；可是这个阶段接触的实践还是比较庞杂。
* 2016-组织：在获得了高层领导的支持以后，他们同时在三个方向出击：软件开发模型、精益IT管理和供应链管理；在三个方面都直接提高和优化了DevOps的速度。
* 2017-实验：在取得了天时地利人和之后，他们展开了所谓的“双模实验”的实践道路；从业务需求入手（规划了使用了MMP最小化可市场产品的概念），逐渐抛开了纷繁复杂的实践和方法论，他们开始聚焦在了“程序员体验”上，通过各种实验验证DevOps Handbook中描述的实践是如何影响并提升他们的。孵化和实验各种DevOps Handbook书里的实践。
* 2018-促动：如何把相关的工具推广到200多个开发团队，如何引入Google的SRE模型，将交付流水线作为产品对待，在复杂的组织中，实施跨部门的流水线的挑战依旧不轻。
* 该公司的DevOps实践道路是一步一个台阶的持续改进过程，经历了三年多时间，每个阶段的关键词代表了他们的成果和挑战。

-------


## DevOps团队间的交互模型

【重点】团队组织结构和交互方式。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-007.jpg)

* 这是实验各种DevOps实践的团队组织模型，开展每项DevOps实践都遵循PDCA的持续改进方法。
* 所有团队遵循着三个基础原则：1速度，江湖武功唯快不破，这是他们清醒而简单的唯一追求目标，成为检验所有优化改进的唯一验收标准和条件。2实践者之成功，他们做的并不是自顶向下的、政令式的强推，而是让参与DevOps实践的团队自己提出工作想法，自己来决定在哪里尝试改进能提升速度。3范围，从端到端的价值流全局看，既不推崇极左的做法，也不推崇极右的做法，他们将范围限定在，从一张工作卡片进入DevOps产品代办工作（Backlog）开始，直至将它的成果发布到生产环境中。
* 实施“双模实验”团队的模型，两个团队都提出自己想做的实验想法，双方的工作内容都汇总到一个集中的DevOps产品代办工作队列中，每一项工作/卡片都是一项实验，每一项实验都由两个团队分别完成，A/B团队的做法和实现结果可能不同，这样也自然地应用到了A/B测试的模型。
* DevOps Leadership Team团队里是Cindy和Jim所在的团队（应该是一个虚拟团队组织），他们确保所有代办工作都遵循以上的三个基础原则，另外使用系统性思考来确保每种实验如果取得了成功，在推敲是否它能推广并应用到其它的200多个开发团队。
* DevOps平台团队辅助和优化双模实验团队的工作，例如双模团队可能都需要自动化变更流程（ITSM的管理范畴）的API，而这些工作就可以踢给平台团队做，平台团队负责设计实现这个API，并且保证它具有企业级规模的能力，然后交付双模团队使用即可。
* 治理团队是由该公司的各个CIO级别的利益干系人组成的，上文说过某些复杂的DevOps持续交付流水线会跨三个以上的部门，这些BU的大佬会在这个团队中；他们在每个迭代都会出现在双模团队的工作现场，一起现场查看状况，现场解决问题。Jim认为他们亲自临场观察和了解实验工作的效果，远远比将实验成果作出PPT后再给他们去汇报的效果要好。

-------


## EPIC史诗

【重点】DevOps团队根据Handbook为基础，提出了所有想实验的工作内容。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-008.jpg)

* 开发团队从寻找什么拖慢了速度出发，寻找优化和改进工作内容的方法，在渐梳理和过滤以后，发现最后确定要做的工作都可以在Handbook中得到确认。甚至有些人在讨论某个工作条目的时候，能清晰的告诉大家可以参考Handbook书中的章节和页数。
* DevOps产品代办工作里的EPIC史诗工作必须是在Handbook书中能够出现和参考到的，如果不是的话，团队可能会对它表示质疑。
* 这里Cindy简述了自动化测试这项工作的实验，故事是这样的：开发团队自己描述到，当前的Test Bed已经大到不可管理的程度，测试运行的时间太长了，因此不能保持测试的精简和有效性，这样的情况持续了一段时间以后，大家就失去了对自动化测试的信心。而且由于开发和测试人员不在同一个组织/团队里，团队之间必须进行工作交接（部门墙），导致了大量复测试案例的存在。他们的解决方法是，让开发和测试人员结对子，这样就减少了重复测试。当测试套件又变得精简和绿色了以后，大家又开始相信这些自动化测试了，之后大家对自动化测试的文化转变为：将自动化测试案例失败视为零容忍事件（失败的测试会导致全team的人停下来，并在1天内解决）。另外一个故事关于性能测试，性能测试是通过一个位于俄亥俄州的集中式性能测试团队做的，任何开发团队的申请时间是90天（被识别为最长时间的约束点），他们认为这个前置时间是无法接受的。解决方法是，将性测试脚本和运行权限交还给了开发团队，最后90天的性能周期被缩短为了2小时。
* DevOps团队和管理层对Handbook书里的实践内容达成了共识和一致，上下一致的参考书中这些业界已经验证过的实践，节省了决策和探索DevOps做法和套路的时间。


-------


## 开发者/程序员体验：十八般神兵利器，大量的上下文切换

【重点】2017年的实践核心是“开发者/程序员体验”（程序员要“富养”）

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-009.jpg)

在专注于开发者体验优化的过程中，应用了大量DevOps工具，最后发现如果开发者把它们都用一遍的话，要花好几个小时的时间。为了解决这个问题，他们体验了Rocket.Chat工具，开发者们对此工具提出了一致好评。

为了让公司领导层支持增加这个工具，他们请领导们到现场亲自视察观看开发人员在使用了Rocket.Chat之后，优化的体验。领导们就这样决策增加的这个工具。

-------


## 开发者/程序员体验：拥抱聊天机器人，减少上下文切换

优化后的开发者工具集如下所示。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-010.jpg)

* 开发者直接面对的工具精简了很多，他们几乎只需要专注于写代码和处理代码的提交和PR即可。
* 之前开发者如果需要部署代码，就需要手工的在UrbanCode里点击十几二十次鼠标，才能完成一次部署操作。
* 在使用了聊天机器人之后，他们只需要对聊天机器人说：deploy；即可


-------


## DevOps登山指南

通过这一页纸的手册，为新来的DevOps实践者提供了清晰的指导。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-011.jpg)

攀登高山隐喻了这是一个艰难的旅程。

-------


## 北极星 - 前置时间

【重点】各项DevOps工作的唯一参考指标是“前置时间”（指南针）

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-012.jpg)

选用这个指标的三个原因：

* 这个指标可以在横向的200多个敏捷开发团队里实施；在纵向的组织级、部门级和团队级上，大家都能理解和认可这一指标，都能够掌握前置时间的计算和测量方法。缩短前置时间的目标是清晰的：及时要加快交付速度。
* 各个开发团队可以自行选择优化前置时间的方法和路径，其实这鼓励了团队的创造性。
* 对此指标的度量和持续改进，是可以按天实时进行的，同时还要保证实现部署的零宕机时间。

-------


## DevOps登山用品：地图和装备

DevOps实践者基础的精神和物质需求。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-013.jpg)

* 工具和DevOps实践直接相关
* 每个工具都有其价值和应用场景（例如Rocket.Chat）
* DevOps Handbook（中文书名：DevOp实践指南）的作用是地图，每个DevOps实践团队都进行至少每周一次的读书俱乐部活动，每次都对书中具体的章节进行团队讨论和学习。

-------


## DevOps的支持模型

DevOps支持团队的作用。

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-014.jpg)

为了满足企业级的支持规模，让水平参差不齐的200多个开发团队都能顺利应用DevOps实践，没有这个支持模型是不可能走远的。


* 夏尔巴人团队的作用是支持和辅导DevOps实践团队，提升团队的思想意识观念和技能，帮助它们构建某些特定领域的工作能力。
* 参与DevOps实践的开发团队必须自己登上山顶，哪怕是爬也是自己爬上去。绝不勉强，不想进步的团队就不要参与了。
* 逐渐开展了沉浸式配对的支持模式，让低水平团队的人员在DevOps高水平团队中进行交叉培训，让他们现场看到相同的工作确实可以有不同的、更好的做法。
* 他们进行每月一次的DevOps道场，在道场里DevOps技术顾问现场指导和帮助前来提高的团队。
* 将流水线视为产品，流水线的管理确实也是他们的痛点之一。

-------


## DevOps成功的那一刻

DevOps对业务有毛用？！

![Grafmeyer, Jim, Payne, Cindy, DevOps Handbook Experiments in Accelerating Delivery](https://res.cloudinary.com/martinliu/image/upload/Grafmeyer_Jim_Payne_Cindy_DevOps_Handbook_Experiments_in_Accelerating_Delivery-page-015.jpg)

这个故事是该公司刚开始品尝DevOps成功硕果的那一刻。飓风哈维（是2017年大西洋飓风季中的一个热带气旋。2017年8月25日，登陆美国德克萨斯州沿岸，时速130英里）导致车辆涉水险的申报数量剧增。业务部门的人处理这些车险事件的过程中意识到，他们的业务流程对这个险种的索赔并不友好，于是就来找到了IT部门，提出想要优化这个险种报案和索赔处理。

这是第一次业务部门找上门来提出的业务需求，IT部门在当天就搞定的经历。业务人员和IT部门的人用了一个小时的时间讨论优化方案，决定去掉索赔流程里40%的多余步骤。IT部门开始设计和实施这个想法，决定需要变更多个应用，他们在当天里，在剩下的7个小时内就完成了这些业务需求的开发和测试，这些业务变更的生产环境部署工作是在工作时段进行的，变更在当天的营业时间结束前就上线了。他们始终以速度为先的实践原则在一年后，在这一天里得到了回报。以前需要至少90天的周期才能完成这样的变更，性能测试会就会占用一半以上的前置时间。而他们觉得这次在整个的设计、实施和部署过程中，其实并没有感到什么压力和风险。

-------


## 后记

本文的价值在于，向你展示一个有参考价值的DevOps案例。它的很多特征和成功之处都值得借鉴和思考。本文的文字主要来源于对视频中的叙述，其中也包含了大量我个人的观点和分析；[欢迎读者在观看本案例视频后](https://v.qq.com/x/page/v0555haemus.html)，与我分享和讨论以上内容。





