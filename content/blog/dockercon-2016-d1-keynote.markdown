---
author: liuadmin
categories:
- Blog
comments: true
date: 2016-06-20T19:30:33Z
slug: dockercon-2016-d1-keynote
tags:
- docker
title: DockerCon 2016 D1 Keynote
url: /2016/06/20/dockercon-2016-d1-keynote/
wordpress_id: 54151
---

看点：开场乌龟引起了喵星人大战，首次有吉祥物开启的科技盛会。 和往常一样 CEO 和 CTO 挑大梁将首日 keynote。 所罗门提出了 Docker 技术发展的三个核心方向和着眼点，并在每个方向上做了新技术发布。 1. 开发者体验提升， 正式发布 Docker for Mac/Windws 2. 编排能力的提升，正式发布 Docker 1.12 ，其中有四项能力提升；这是要废掉所有其他编排器的节奏啊~ 3. 运维体验提升，正式发布 beta.docker.com ；这是和公有云深度结合的产品，分为 AWS 和 Azure 两个模块。 一共有三个实景演示，都没有出现问题，演示很成功。


## 现场录音



点上面的播放键，播放整场录音。请注意中间的数秒钟乃至数十秒的中断是正常，请快进收听。


## 开场


屏幕上出现了乌龟开始做 demo，运行了一个容器。 猫咪大战，混乱了，猫星人入侵了。猫叫~~乱作一团··· 发生了什么？ dockercon16 吹起了号角。 乌龟再次出现在电脑上，运行了另外一个容器惊喜，这次是美妙的音乐。 调皮的乌龟折腾完了之后，主题曲想起来。4000多人的场子，大家很期待。


## CEO Ben Golub 演讲


![2](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/2.jpg)

Ben Golub CEO 出场。 Today we are all docker blue. 欢迎所有人。 我们和前两年的不同，我们发布了1.0 等等。 谈了很多 Docker 取得的成就。 感谢和表扬了社区。 感谢2900+贡献者。 社区的状态动态，每周超过300 PR，三分之二来自 Docker 公司之外。 docker meetup 的状况， 250+城市举行，125K 人参加聚会。 内容构建方面，docker hub 上有 460K 个应用，到目前为止有4.1B 此镜像下载。 感谢 docker 的生态社区。 讲述了这两年的使用场景的变化。Docker 逐渐成为了企业级的应用。 所有穿着红色衣服的起立，他们是 Dockr 公司的员工，感谢他们，请鼓掌。 感谢今年的赞助商。 向 Demo Gods 致敬，给神献上祭品，保证后续的演示顺利。 we pray to the old codes and the new.


## CTO 所罗门演讲


所罗门出场。 我去，4000多人在场，我老爸也在家看我视频直播。 很荣欣大家来参加，感谢大家来参会。 谁参加过 DockerCon14？ 我们要开始做很多的 demo 在会议过程中。 最精彩的部分是，我们来自全球各个行业的不同层面，多样性简直是不可思议。原因是：Programming is changing the world. 我们在一起的原因是：Docker 是编程创新的助力工具。 We’re building Docker incrementally, in the open. 最好的工具目前看不是那些软件工具巨人的公司提供的，而是来自社区和群众的创新，是你们指引着我们构建了愈来愈多的工具。 社区告诉我们几个方面需要努力。


### 1 开发者体验


构建最好的工具，这个工具需要有这些特质：



	
  1. get out of the way;

	
  2. adopt to you；

	
  3. make the powerful simple


我们努力地践行着这些理念。 Docker for Mac/Windows 将是最无缝的开发者体验。 Making things easy is really hard. 我们在寻找最佳的系统工程师，我们收购了 Unikernel 公司。 在移动游戏行业里面找到最佳的设计者。


### 第一个演示 – Docker for Mac


演示者登台。 我是个开发者，今天第一天上班。 安装了 Docker for Mac 打开这个应用，启动它。 克隆 
```
git clone viting-app 
```
运行 
```
docker-compose up
```
 打开投票应用的两个web界面。 我不知道这个应用是什么，但是一个命令就启动了所有5个服务。 我发现了程序的 bug。 是否我第一天上班就能修复它？ 分析了一下程序架构图。 查看 docker-compose.yml 文件。 找到了一个 debug 显示的的那一行。 在代码中加入了 live debug 的断点。 开始 review 代码，发现了奇怪的地方。 找到了 git 上的代码，增加了评论，提出源码结果计算方法有问题。 现在删除了有问题的哪一行代码。 删除了断点。 用 live debug 的方式修复代码。 回到程序界面，发现 bug 没了。 做 git commit 提交修正后的代码。 查看了该应用在 staging 环境的情况，发现也有相同的结果计算的问题。 进入该环境的 Docker Cloud界面，看到了这个运行环境。 查看 result 服务的构建策略是自动构建。 Docker Cloud 自动接收了新的代码，Staging 环境的构建完成并通过了测试脚本，程序正常了。 查看云里的 Staging 环境的 bug 也被除掉了。demo 结束。


### Splice 的 CTO Matt 案例分享


Splice 的 CTO Matt；我们做的是个音乐服务的技术，我们构建的服务像是给音乐人用的 github。 每天都有人上传上很多 TB 的音乐数据。 我们在 Mac 上开发，在 Linux 上部署。 我们使用多种数据存储。 Docker 让我们保持多种环境的一致，降低了 debug 的时间。 所有的程序运行在容器中。 我们一天更新线上的业务20多次。 Developer 的第一天工作就能为业务提供价值。 我们使用 Docker for Mac。


### 2 Orchestration 编排能力


我们听到很多 happy user 的故事。 感谢所有7万多 Docker for Mac beta 的反馈参与者。 我宣布 Docker for Mac/Widnwos beta 完全开放下载。 很多人告诉我们需要在 Orchestration 上更加努力。 它在 ship 方面提供支持，能发布你整个的应用，让你不再关心单个的容器。 Orchestration是个技术活，只有专家才能干。很少人能做这个工作。 可是用户怎么能即不出现手头人才短缺，又不被某些厂商在这方面给技术锁定呢？ 更好的方法是什么？ Docker 1.12 将内置编排功能。 最佳的编排技术将是 Docker 自己。

![3](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2016/06/3.jpg)

我们先提前介绍一些它的新功能。



	
  * Swarm mode

	
  * Cryptographic node identity

	
  * Docker Service API

	
  * Build-in Routing Mesh


非常简单的演示，你就明白了。 欢迎第三个 编排的演示 Docker 1.12 技术。


### 第二个演示 – docker swarm 功能演示


两个人上场。 用一个新的机器，上面只安装了 docker。 有三个节点。 第一个节点上初始化群集 docker swarm init 第二个节点上加入群集 docker swarm join 在第三个节点上加入群集 docker swarm join 三节点的群集建立完成。

为毛它没有让输入任何安全的信息和选项，这就对了，我们有内置的 PKI 安全通讯机制。 所有节点都有自己的身份标识。密钥定期自动变化。所有通讯都可以追述到发起者的身份。

你们都懂 docker run 子命令。 docker service 命令是新来的子命令。 service 的定义是将要维持服务的状态。




```
docker service create --name voting-app -p 5000 
docker service ls


```


所有的服务只启动了一个容器，分布在三个节点上。

看到投票应用页面显示了。

浏览器访问了第一个节点的 ip:5000 ，然后第二个节点的 ip:5000 端口，发现实际上访问到了第一个节点上的的容器。这就是新的容器路由的功能。所有的节点访问这个服务的端口，都可以路由到该服务的容器里。


```
docker service scale 6
```


现在扩容服务的容器。 每次刷新页面，页面上容器的ID都在变，这是群集内置的 round robin 负载均衡策略，把访问分发到所有容器。这就是内置的负载均衡功能。

我们升级这个 app 吧。




```
docker service update 


```

演示容器镜像文件的更新 选择另外一个 tag 的镜像来升级 现在我们可以对电影投票了

滚动升级可以支持 加上一次升级2个容器的升级选项，因此它现在是做两个一次的服务容器升级，直到所有容器都升级结束。

我们说的自愈功能是说，能让应用可以在机器宕机的时候，业务也不中断。 请把有两个容器的 node3 关机。 调度器现在自动在 node2上长出刚才运行在 node3上的那两个容器。保持6个容器的服务配置。

演示成功，并没有出问题。


### Zenly 的创始人案例分享


所罗门高兴的再次上台。 这说明我们的祭品生效了，演示没有出毛问题。 docker 1.12 在几周后就发布，Docker for Mac beta 版本上现在就有这些功能。你们这些已经安装的现在就可以尝试这些功能。 我们自由的扩容业务应用，而服务速度不受到影响。 在大规模的关键业务中的部署才是目标。我们请 Zenly 的兄弟们上台。

Zenly 的人喝了两杯祭品的冰咖啡上台了。 我们有1M 用户，是最近的三个月内获得的。 500M events/day 一共才 6 engineers 我们运行业务在云上。 我们现在把部分业务迁移回自己的物理机。 我们在10台物理机上运行部分业务。 部分运行在 GCE 上。 我们感觉按需扩容很爽。


### 3 运维体验


我们谈到开发者体验，业务编排。 群众还告诉我们“Ops experience” 运维体验是需要关注第三个侧面。 Docker 应该深度和云基础架构集成。


#### beta.docker.com 发布


我宣布beta.docker.com 发布。包括 docker for aws 和 docker for Azure 是最原生的 AWS 和 Azure 体验。是和云基础架构最深的集成。 现在可以用 AWS CloudFormation 来部署 Swarm 群集。 可以自动配置所有的负载均衡端口等配置。


#### www.docker.com/dab 发布


www.docker.com/dab 是新的可移植多容器应用打包格式。 这是新的 ops 体验。是让 developer 和 Ops 更容易工作在一起的方案。


### 第三个演示 – 云运维体验


Developer：我想赶紧回家。我还需要赶紧交货。




```
docker compose bundle 

```



产生了一个.dab 文件，齐活了。 把应用的 .dab 文件给 Ops 即可。 Ops：你的应用是 docker的么？ 额的个神啊！ 我喜欢在 AWS 上用Docker。 看我新建Stack的 AWS 向导，这里可以配置了一个新的 docker swarm 群集。 看我这有一个已经部署了100节点的群集。 所有网络、存储、负载均衡都不用手动配置。 复制 这个网址。 在 Mac 电脑的 shell 粘贴 ，后点击回车。 我们进入了命令行 docker for aws 的特殊的 shell 我能看的所有群集和主机的状态 把你的 .dab 文件给我，就欧了~ 用 USB copy 给你。 把文件 copy 给了 Ops scp .dab 文件到 swarm 群集中。 在进入 shell ls 能看的这个文件




```
docker deploy  voting-app  xxx.dab 


```


看这些所有服务都运行了




```
docker service ls
docker service update -p 80:80  voting-app
docker service update -p 8080:8080  result-app
docker service scale 


```



扩容这些服务的容器数量 打开浏览器确认应用部署结果，找到 ELB 的配置，配置已经自动生成了。 浏览器中访问 ELB 的80端口上看的投票页面 在 ELB 的 8080 端口看的结果页面 这下应用部署完毕。 原来你的 Ops 工作怎么这么简单啊！！ I got go home ~~~


## 结束


所罗门感谢大家，所请访问 docker.com/getdocker 有需要的尽管说。 请在这几天内，尽量多的告诉我们，你们的需求和使用场景。 请告诉我们 what we build next ! thank you very much ！！


## 注意


我是 Maritn Liu 为您播报本次大会的各种信息，对以上内容有任何问题和疑问请加我微信咨询，我的微信号是 martinliu_cn ，这篇文章也会在我的微信公众号（aws-faq）和 ”刀客微播报“上发布。以上会议记录中所有命令的操作并不是准确的演示者输入，尽量参考这些命令来想想其可能的参数和语法，如果你安装了最新版本的 Docker for Mac 可以自己试一下。


