---
date: 2020-07-15T00:09:53+08:00
title: "Skaffold 让 K8s 开发者更加酸爽"
subtitle: "Skaffold是本地 Kubernetes 开发者的又一个利器"
description: "Skaffold是本地 Kubernetes 开发者的又一个利器"
categories: "DevOps"
tags: ["DevOps","Kubernetes","CI"]
keywords: ["DevOps","Kubernetes","CI","CD","Skaffold"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/abstract-1.jpg", desc: "DevOps"}]
---


![](/images/skaffold.png)

今天介绍一个本地 Kubernetes 开发的利器 Skaffold。
这是我偶然间发现的一个工具，询问了一下周围的人，居然还没有人用过。测试之后，确实有一种不吐不快的感觉。

## 简介

![](/images/intro.gif)


Skaffold Google 开发的一个开源项目。是一个非常轻量的命令行工具，就是一个可执行文件。它的主页上是这样的介绍它的。

* 轻量：Skaffold只是一个客户端工具。由于集群上不需要任何的相关组件，您的集群没有任何开销或维护负担。
* 运行在任何地方：Skaffold是与世界分享你的项目的最简单的方法："git clone"，然后 "skaffold run"。此外，你还可以使用配置文件、本地用户配置、环境变量和标志来轻松地集成不同环境的差异。
* 功能丰富：Skaffold拥有许多Kubernetes原生开发的基本功能，包括基于策略的打镜像标签、资源端口转发和日志、文件同步等。
* 优化你的开发：Skaffold使内部循环紧密，高度优化，让您在开发的同时得到即时反馈。

## 客户评价

![](/images/forgerock.png)

"我们的客户很喜欢[Kubernetes]，但一直给我们反馈说在Kubernetes上开发很麻烦。Skaffold一针见血地解决了这个问题。以前需要几分钟才能部署的docker镜像或配置的更改，现在只需要几秒钟。Skaffold的插件架构使我们能够部署到Helm或Kustomize，并使用各种docker构建插件，如Kaniko。Skaffold用一个精简的工具取代了我们定制的实用程序和脚本集合，并且易于使用。"
Warren Strange，ForgeRock的工程总监。

![](/images/quora.png)

"当我们评估我们可以使用Kubernetes的工作流程时，Skaffold脱颖而出，成为我们在开发和部署中都想要的工具。它为我们提供了一个跨应用程序的通用入口点，我们也可以为CI/CD重用。现在，我们所有的Kubernetes应用的CI/CD管道在构建和部署时都使用Skaffold。"
Taylor Barrella，Quora的软件工程师


![](/images/tng.png)

"Skaffold是一个了不起的工具，它为我们简化了开发和交付。Skaffold通过覆盖两个维度，击中了我们的甜蜜点。第一，从本地开发、集成测试到交付的整个开发周期。第二，Skaffold让我们能够在Linux、OSX和Windows上独立开发，不需要特定的平台逻辑。"
Martin Höfling，TNG技术咨询有限公司首席顾问

## 推荐首次测试流程

前置条件，你的开发用工作电脑上已经安装了它需要调用的 kubectl 和 docker 命令，kubectl 需要有至少一个可用的配置，这个配置可以指向任一一个你有权限部署的 Kubernetes 集群。

我在 macOS 上，直接运行 `‌brew install skaffold` 即可，其它系统参考：https://skaffold.dev/docs/install/

克隆 Skaffold 的代码库到本地，获取必要的测试应用代码。

`‌git clone https://github.com/GoogleContainerTools/skaffold`

进入代码库中的‘hello world’示例应用。

执行：`‌cd skaffold/examples/getting-started`

执行 `‌skaffold dev` ，你会看到 Skaffold 进入了这个项目的构建和运行的状态，执行结果是持续的输出 ”[getting-started] Hello world!“ 

现在 Skaffold 就进入了 /getting-started 的监视状态。观察任何代码文件的修改存盘动作，每次代码的变更会触发 Skaffold 流水线的执行，skaffold.yaml 文件中描述了本地流水线中的相关动作：

* 使用 Dockerfile 从源头构建Docker镜像。
* 用Docker镜像的内容的sha256哈希值来打上标签。
* 更新 Kubernetes manifest k8s-pod.yaml，以使用上一步构建的镜像。
* 使用 kubectl apply -f 部署 Kubernetes manifest。
* 从已部署的应用程序取回日志在本地控制台显示。

现在用代码编辑器打开这个项目唯一的程序文件 main.go ，修改其中的 Hello World 为其它你想到的词，保存后，观察构建的过程。

## 推荐微服务测试

参考以下视频，测试 Skaffold 代码库中的 microservice 项目。

## Skaffold 流水线阶段

Skaffold 主要会用到五个阶段。

![](/images/workflow.png)

其所有阶段如下：

* Init ：	generate a starting point for Skaffold configuration	
* Build ：build images with different builders	
* Tag ：	tag images based on different policies	
* Test	 ：test images with structure tests	
* Deploy	 ：deploy with kubectl, kustomize or helm	
* File Sync ：	sync changed files directly to containers	
* Log ： Tailing	tail logs from workloads	
* Port Forwarding	 ：forward ports from services and arbitrary resources to localhost	
* Cleanup ：	cleanup manifests and images

当你启动Skaffold时，它就会收集你项目中的源代码，并使用你所选择的工具构建工件；工件一旦成功构建，就会根据你的需要进行标记，并推送到你指定的仓库中。在工作流程的最后，Skaffold还帮助你将工件部署到你的Kubernetes集群中，同样使用你喜欢的工具。

Skaffold允许你跳过各个阶段。例如，如果你在本地使用Minikube运行Kubernetes，Skaffold不会将工件推送到远程仓库。

每个阶段的详情见：https://skaffold.dev/docs/pipeline-stages/


## 架构设计

Skaffold 秉承着插件化的设计思想。

![](/images/architecture.png)

以上架构内置了对下来工具的支持：

* Build
	- Dockerfile locally, in-cluster with kaniko or on cloud using Google Cloud Build
	- Jib Maven and Jib Gradle locally or on cloud using Google Cloud Build
	- Bazel locally
	- Cloud Native Buildpacks locally or on cloud using Google Cloud Build
	- Custom script locally or in-cluster
* Test
	- container-structure-test
* Tag
- 	Git tagger
- 	Sha256 tagger
- 	Env Template tagger
- 	DateTime tagger
* Deploy
- 	Kubernetes Command-Line Interface (kubectl)
- 	Helm
- 	kustomize


## 总结

Skaffold 确实让基于 Kubernetes 的开发者的本地工作环境更加优化和整洁了。希望本文对你的工作有所帮助。

