---
author: Martin Liu
categories:
  - opensource
comments: true
date: 2016-06-22T02:35:39Z
slug: closing-general-session-moby-docks-cool-hacks
tags:
  - docker
  - twitter
title: DockerCon 2016 D2 超萌码头酷黑客 大会圆满闭幕
url: /2016/06/22/closing-general-session-moby-docks-cool-hacks/
wordpress_id: 54161
---

Closing General Session 的主题是 Moby Dock‘s Cool Hacks ； 从字面意思上看，这个主题的意思是“超萌码头酷黑客”的意思。我已经看到了关于最后一天开幕主题演讲的评论，说是“剑指商业”什么的；而我认为 Docker 从开始的第一天，无论它是否开源，它都是为了商业利益而已。话在说回到开源，Docker 只是完美的应用了开源软件这种实践而已；而且 docker 把开源这种模式应用的如此成功，并在商业上也如此让人眼红和侧目，这也算是开源软件商业化登峰造极的一种极端性个案。个人认为开源无疑是在软件行业中做出爆款技术当之无愧的首选的实践方式。我在红帽碰到很多参与开源十几二十年的老黑客，他们不乏会表达关于开源纯洁性沦丧的抱怨；我对此也非常理解和认同。而我更认同开源可以对软件技术带来无比活力的这个积极的方面。

言归正传，小编我还是“模拟现场”播报一下大会闭幕主题演讲的盛况。这是大会的结束的 session，现场的人数明显的少于第一天开幕式的人。在十几分钟内，人们稀稀拉拉的进入了会场。会场中的座位大约还有一部分空位。美女 Mano 和 黑客 Kristie 作为主要演讲人上台。美女上台后先用手机自拍了几下。两个人开始宣布，Docker 大会之后举行为期一个月的黑客大赛，这是我们的传统，Docker 大会虽然今天会结束，而 docer 黑客大赛将从今天开始。我们来请大家欣赏三个非常酷的黑客项目演示。

本次大会的录音点这里  [http://www.ximalaya.com/32280565/sound/17388272](http://www.ximalaya.com/32280565/sound/17388272)

## 黑客演示 1：微服务自毁平台

Jeff 登场。Jeff 开始讲述微服务的故事，我们都在试图让基础架构做到冗余，容所有的服务都冗余，让群集能够自愈；但是故障，断网，宕机还是会发生。我们所做的这些真的能够保证业务不宕机么，服务不终端么？你怎么能确认这一点？因此回归到故障的发生上吧？如果服务要出故障，请让它有规律的发生。请程序猿和 ops 都投入到故障处理的战斗中，以此为契机来优化和改造应用，让应用变的更加强壮。我们都听说过混乱猴子，而 Jeff 团队正式帮人们构建一堆这样的工具的人。

有一个思路是：如何让我的系统的服务出故障，如何主动的在系统中注入故障。我们需要一种特殊的编排工具来在系统中模拟和触发故障的发生。我用容器做工具平台来触发故障注入的动作。当然这个故障是在容器架构的微服务系统中触发这个动作。

Jeff 开始做这个  Demo。说：如果你的”网络没有故障，天下太平。“其实这很无聊的说，有木有？有木有？我现在开始用工具来注入 网络延迟的网络故障吧！ 。用一个基于策略的工具。配置一个网络故障模拟的策略，故障什么时间发生，发生多久。这里设计一个每 10 秒钟注入一次网络延迟故障提高到 600ms 的故障。然后配置故障影响的范围，这里使用 Docker 的 lable 来做故障发生节点的选择的条件。符合标签的系统将受到这次故障影响。我们的这个故障模拟编排系统，帮您提前体验故障的发生。现在你看故障发生了，从这些容器里面 ping google 的网络延迟比之前大多了， 目前延迟到了 600ms。希望你们能开始体验和使用这个而工具。

## 黑客演示 2：Serverless 架构的应用不是梦

Ben 是大家在 Docker 大会喜闻乐见的一个黑客，他经常给做 demo 和 session。他绝对符合超萌的标准。

![40906 (1)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/40906-1.jpeg)

Ben 开讲，Serverless 是如何做的？ben 认为 Serverless 是一种全新的应用编程的思路，而 docer 可以很好的支持这种思路，并实现和执行这种思路。docer 群集可以让 Serverless 引用按需执行，并让该应用的底层变得资源冗余并路由可达。ben 开始演示   他的几张 slides， 说 Sererless == docker 这个概念。本开始讲解：如何用 Serverless 架构来实现投票应用的改造。如何把这个 5 个服务模块的纯粹容器微服务系统转换为 serverless 架构的应用。开始修改源代码，把发入队列的票，变成一个处理投票的容，把 http 服务器变成一个 CGIHander（）服务；但是  nodejs  不支持 CGIhander，肿么办？我用 perl 重写了这部分，为毛用 perl，被忘了它乃是古董级的黑客神器的好不好，呵呵！改造完之后的系统架构如下。架构是把处理 postgresql 意外的模块都重写了。数据库保留在最下层。这种 Serverless 重构实践遵从的原则如下。

![2](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/2-1.jpg)

三个原则翻译一下：

1. 把每个模块的核心功能打包，并作为容器来运行。解读：这意味着把所有服务模块组重构，把每个服务模块中的核心功能代码作为一个在容器里面跑的对象。这里其实牵扯到很深的业务重构和应用重构，程序猿或将抛弃以前的代码，甚至以前所习惯使用的程序开发堆栈。

2. 把这些容器用 Docker 的 Swarm 跑起来。解读：docker 原生的 Swarm 编排能力将为您的应用提供，功能的运行，workload 的分布，服务的冗余，服务的路由等等支持；这样的架构能支持到 Serverless 的应用的模型。

3. 从容器中去运行其它容器。解读：容器编排平台或将不是容器生命起源的唯一起点，容器里面的应用可能可以决定系统中需要滋生出什么样的容器，当然说的是需要实现和运行什么功能的容器。

好了，目前为止，ben 的心的应用重构完成，还是用 docker-compose up 启动了改造之后的应用。现在看到了这个 serverless 的应用工作正常。

Ben 说：我们在这 demo 了 serverless  应用的改造的过程，可以看到 docker 是如何支持这种应用架构的。你可以打包 web front 为服务，它自动的在 Swarm 群集上无限延展这个服务。成为分布式计算的架构。还可以打包微服务的其它应用模块为 Serverless 应用架构。欢迎大家 参与到我的 Serverless github 项目中，和我一起互动，把 Serverless 在 docker 上的应用搞起来。[https://github.com/bfirsh/serverless-docker](https://github.com/bfirsh/serverless-docker)  这里包括了以上演示的应用。

## 黑客演示 3：在线更新的无人机

这个团队做 in the air update 无人机实时演示。无人机其实是树莓派加他们的 docker 软件系统。这是一个嵌入式系统的设计。

![3](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/3-1.jpg)

![4](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/4.jpg)

![5](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/5.jpg)

实时新旧系统的切换秘密在这里。新版的容器会先运行起来，新系统用一个队列来接收旧系统的数据，这些数据是新旧系统交接的必要的数据，系统会判断需要多长时间，需要收集那些数据来完成这个交接的过程。直到旧系统到新系统的割接完毕。

程序猿开始更新 v1 的代码，加入了摄像头实时视频功能。更新提交了 v2 的镜像文件。在下图可以实时的监视到无人机的状态。

![6](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/6.jpg)

![1](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/1-1.jpg)

无人机在在线更新软件中。并没有掉地上哈哈哈！

![6.1](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/6.1.jpg)

右下角是新版本软件的摄像头把大会现场的视频拍摄，并实时传递到控制台的效果。此图上面的那个图，中间凸起震荡的那个块是无人机软件升级实时更新的过程。

本黑科技演示完毕。

## hackathon 黑客大赛启动

主此人再次上台启动了黑客大赛。

![7](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/7.jpg)

为期一个月的 hackathon 正式开始。

## 最后看点

CEO CTO 上台感谢赞助商。所罗门开始讲黑客骚扰现象。号召大家通过[ http://hackharassment.com](http://hackharassment.com) 网站来抵制中现象。

Bump UP 是通过手环实现的，人们的手环彼此碰撞会在系统中增加一个点数。宣布了碰撞点数最多的前 5 名，感谢他们在本次大会中，积极的和其它人互动和沟通，请他们去领奖。所罗门号召所有现场的人再次相互碰撞手环，系统系统的点数增加到两百万。来解锁 Docker 奖学金基金。很快大家碰撞起来。奖学金解锁。

感谢进三千名的社区 贡献者，感谢 docker 的员工。所有人发来的自拍形成了一个西雅图拼图。最后大会圆满结束。

看到最后的才能做最后的评论。这更感觉是一个黑客大会，引入了 docker 对社会的责任感的概念。商业财富越大的人社会责任感应该更多。更像是黑客公司商业成功之后，继续创新，并开始践行自己的社会责任的大会。大会并没有结束，黑客大赛在接下来的一个月里将在全球各地延续。
