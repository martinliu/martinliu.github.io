---
date: 2018-03-24T20:51:01+08:00
title: "容器化应用的设计原则"
subtitle: "云原生容器怎么装配，来自Red Hat咨询团队大牛的最佳实践和经验总结"
description: "来自Red Hat咨询团队大牛的最佳实践和经验总结"
categories: "Container"
tags: ["DevOps","Container","Red Hat"]
keywords: ["DevOps","Container","Red Hat"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/BingWallpaper-2018-03-20.jpg", desc: "DevOps"}]
---

本文来自于Red Hat咨询顾问Bilgin Ibryam所编写的一篇白皮书，名为《PRINCIPLES OF CONTAINER-BASED APPLICATION DESIGN》。这篇文章在作者的Blog上发表后，作者的twitter被Kubernetes官方twitter转发。白皮书在Red Hat官网的下载地址：[https://www.redhat.com/en/resources/cloud-native-container-design-whitepaper](https://www.redhat.com/en/resources/cloud-native-container-design-whitepaper) 文本是对这篇文章的学习和整理。

先回顾经典的软件设计原则：

* 保持简单，愚蠢（KISS） 
* 不要重复自己（DRY） 
* 你不会需要它 （YAGNI） 
* 关注点分离（SoC） 
* Single responsibility, Open/closed, Liskov substitution, Interface segregation, Dependency inversion （SOLID） 


然后是Red Hat的云原生容器设计原则：

* 唯一关注性原则（SCP） 
* 高度可观测性原则（HOP） 
* 生命周期一致性原则（LCP） 
* 镜像不可变性原则（IIP） 
* 进程可处置性原则（PDP） 
* 自包含性原则（S-CP） 
* 运行时约束性原则（RCP）

很多组织都理解云原生的重要性和必要性，但是并不知道从哪里开始。那么请确保：云原生平台和容器化应用能无缝的运行在一起，并且具备抵御故障的能力，甚至在底层的基础架构出现宕机的时候，也能通过过弹性扩展的方式表现出可靠性。本文描述了容器化应用时需要遵循的基本准则，实施这些原则有助于使之与云原生平台Kubernetes更加适配。

## 唯一关注性原则 SINGLE CONCERN PRINCIPLE（SCP）

在许多方面，唯一关注性原则与来自SOLID的SRP是类似的，它建议一个类应该只有一个责任。SRP背后的动机是每个责任是变更的一个轴心，一个类应该有，且也只有一个需要改变的理由。SCP原则中的“关注”一词强调关注是一种更高层次的抽象的责任，而且它更好地将范围描述为一个容器而不是一个类。虽然SRP的主要动机是变化原因的唯一性，而SCP的主要动机是容器镜像重用和可替换性。如果你创建一个解决单个问题的容器，并且以功能完整的方式来实现，不同应用程序中的容器镜像重用的可能性就会更高。 

因此，SCP原则规定每个集容器都应该解决一个问题，并做得很好。 实现这一点，通常比在面向对象的世界中实现SRP更容易，容器通常管理的一个单一的进程，大多数情况下一个进程解决一个问题。

![scp 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/scp.png)

如果你的容器化微服务需要解决多个问题，它可以使用这样的模式，将多个容器用sidecar和init-containers的模式合并成一个部署单元（pod），这样每个容器仍然是处理单个问题。同样，您可以替换处理同样问题的容器。 例如，将Web服务器容器或队列实现容器，更新为更具可扩展性的容器。 

## 高度可观测性原则 HIGH OBSERVABILITY PRINCIPLE（HOP） 

容器提供了一种统一的方式来打包和运行应用程序，将它们视为一个黑盒子对象。 但任何旨在成为云原生公民的容器都必须提供API支持，要为运行时环境编写接口（API），以观察容器的健康状况和行为。 这是自动化容器更新和生命周期回收的基本先决条件和统一的方式，从而提高系统的弹性和用户体验。

![hop 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/hop.png)


实际上，您的容器化应用程序必须至少为其提供不同类型的健康检查的API--活动和就绪等状态。更好的应用程序的行为则必须提供其他手段来观察容器化应用程序的状态。应用程序应该将重要事件记录到标准错误（STDERR）和标准输出（STDOUT）中，从而通过统一的日志聚合工具（诸如Fluentd和Logstash之类的工具）进行分析，并与跟踪和指标收集库相结合，例如OpenTracing，Prometheus等。

将您的应用程序视为黑盒子，但实施所有必要的API以帮助平台对其进行观测，并以最佳方式管理您的应用程序。 

## 生命周期一致性原则 LIFE-CYCLE CONFORMANCE PRINCIPLE（LCP） 

HOP规定了你的容器提供供平台观测的API。 LCP则规定：您的应用程序有办法读取来自平台的事件。 此外，除了获得事件以外，容器还应该对这些事件相应地作出反应。这就是此原则名字由来。这几乎就像在应用程序通过一个“写入API”与平台进行交互。

![lcp 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/lcp.png)


来自管理平台的各种事件都是为了帮助您管理您的容器的生命周期的。决定处理哪些事件取决于您的应用程序 以及是否对这些事件做出反应。

但有些事件比其他事件更重要。例如，任何需要一个干净的关闭进程，这就需要捕获信号：终止（SIGTERM）消息，并尽可能迅速关闭。 这是为了避免通过强制关闭信号：kill（SIGKILL），之后跟随一个SIGTERM。

还有其他事件，例如PostStart和PreStop，可能对您的应用程序生命周期管理也非常重要。 例如，某些应用程序需要在服务之前进行预热请求和一些需要在关闭干净之前释放资源。 


## 镜像不可变性原则 IMAGE IMMUTABILITY PRINCIPLE（IIP）

IMAGE IMMUTABILITY PRINCIPLE（IIP）容器化的应用程序是不可变更的，镜像一旦完成了构建，预计在不同的环境中运行都不会改变。这意味着在因外部环境的不同，在需要的时候需要使用外部手法处理所依赖的外部配置数据，而不是每个环境修改或者构建不同的容器。而容器应用程序中的任何变更，都应该因此触发构建新的容器映像，并在所有环境中重用它。相同于这个原理的，不可变服务器和不可变基础架构的概念也很受欢迎，并且对于服务器/主机管理也是如此。

![iip 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/iip.png)

在遵循IIP原则的情况下，应该防止为不同的环境创建相似的容器镜像，要始终坚持为所有环境只配置一个容器映像。 这个原则允许在应用程序更新期间，采用自动回滚和前滚等做法，这是云原生自动化的重要方面。

## 进程可处置性原则 PROCESS DISPOSABILITY PRINCIPLE（PDP）

迁移到容器应用程序的主要动机之一是：容器需要尽可能做到临时性，并做好在任何时候被另一个容器实例替换的准备。需要更换容器的原因有很多，比如：健康检查失败、缩容、应用程序将容器迁移到不同的主机，平台资源匮乏或其它的问题。

![pdp 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/pdp.png)


这意味着容器化的应用程序必须保持其状态为向外扩展的或分布式和冗余的。这也意味着应用程序应该快速启动和关闭，甚至为彻底的硬件故障做好准备。 实施这一原则的另一个有用的做法是创建小容器。 容器在云原生环境可以自动调度并在不同的主机上启动。较小的容器可以实现更快启动时间，因为在重新启动之前容器镜像需要被物理地复制到主机系统。

## 自包含性原则 SELF-CONTAINMENT PRINCIPLE（S-CP）

这个原则规定一个容器应该在构建时包含所有需要的东西。容器的存在应该仅仅依赖于Linux®内核，在并添加相关额外的库，在容器构建时加入它们。除了库之外，它还应该包含语言运行时，应用程序平台（如果需要），以及运行所需的其他依赖关系，等运行容器化应用所需要的诸如此类的东西。

![s-cp 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/s-cp.png)


唯一的例外是：由于不同环境之间差异，并且只能在运行时提供的配置; 例如，通过Kubernetes提供的ConfigMap。 

某些应用程序由多个容器组件组成。 例如，容器化的Web应用程序也可能需要数据库容器。 根据这个原则，并不建议合并两个容器。相反，它建议的是数据库容器只包含运行数据库所需的所有内容，Web应用程序容器只包含运行Web应用程序所需的所有内容，如Web服务器。 在运行时，Web应用程序容器将根据需要依赖于并访问数据库容器。 


## 运行时约束性原则 RUNTIME CONFINEMENT PRINCIPLE（RCP）

S-CP从构建时的角度查看容器，并关注于生成的二进制文件及其内容。但是容器不仅仅是磁盘上一个只有尺寸大小的单一维度的黑盒子。 容器运行时有多个维度，例如内存使用维度，CPU使用维度等资源消耗维度。

![rcp 容器化应用的设计原则](https://res.cloudinary.com/martinliu/image/upload/rcp.png)

这个RCP原则建议每个容器申报资源需求，并发送信息到平台。它应该分享容器的资源配置文件，从CPU，内存，网络，磁盘的角度声明。这影响到平台如何执行调度，自动扩展，容量 管理以及容器常规的服务级别协议（SLA）等。

除了向平台声明容器的资源需求之外，还有一点也很重要， 应用被约束在使用所声明的资源需求内。如果应用程序对资源的使用保持在约束的范围内，则当资源匮乏发生时，平台不太可能将其终止和迁移。


## 结论 

云原生不仅仅是一种最终状态 - 它也是一种工作方式。 本份白皮书描述了一系列容器应用的基本原则，必须遵守才能成为优秀的云原生公民。 

除了这些原则之外，创建良好的容器应用程序还需要熟悉其他容器相关的最佳实践和技术。 尽管上述原则非常根本，适用于大多数用例，下面列出的最佳实践在应用和不应用的时候，则需要判断力。以下是一些与容器相关的更常见的最佳实践： 

* **镜像要尽可能的小**。 通过清理临时文件，并避免安装不必要的软件包来构建小尺寸镜像。 这减少了容器的尺寸，构建时间和复制容器镜像的网络传输时间。 
* **支持任意用户ID**。 避免使用sudo命令或要求特定用户名运行你的容器。 
* **标记重要的端口**。 虽然可以在运行时指定端口号，然而使用EXPOSE命令在运行的时候指定，则可以让镜像的使用者更轻松。
* **为持久数据使用卷**。 在容器摧毁之后还需要保存的容器数据的，必须将数据写入一个数据卷。 
* **设置镜像元数据**。 以标签和注释形式存在的镜像元数据可以使您的容器镜像更加实用，从而为使用您的容器的开发人员提供了更好的体验。 
* **使主机和镜像同步**。 一些容器应用需要容器在某些属性（如时间和机器ID）上与主机同步。 

这里是指向各种模式和最佳实践的资源的链接，以帮助您能有效地实现上述目标： 

* • https://www.slideshare.net/luebken/container-patterns 
* • https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices 
* • http://docs.projectatomic.io/container-best-practices 
* • https://docs.openshift.com/enterprise/3.0/creating_images/guidelines.html 
* • https://www.usenix.org/system/files/conference/hotcloud16/hotcloud16_burns.pdf 
* • https://leanpub.com/k8spatterns/ 
* • https://12factor.net





