---
title: "用 Mac Mini M4 重构 HomeLab 结构"
description: 年货买了个 Mac Mini M4，打算用它来重构一下 HomeLab 的结构。
date: 2025-01-31T10:03:16+08:00
image: mac-mini-with-ext-nvme-drive.jpg
slug: macmini-m4-homelab-redesign
categories:
    - Blog
tags:
    - homelab
    - macmini
    - orbstack
comments: true
toc: false
---

## 背景

自 MacMini M4 上市来，其丐版在京东上一直很抢手，定时抢了几次，未果。然除夕大清早，见有货，遂下单，初二终于到货。所谓丐版 Mac Mini M4 有 10 核 10 线程，16GB 内存，256GB SSD，订单价格 3581.21 元，国补 + 京东 Plus 会员优惠后的价格，性价比颇高。我将抛弃之前的 HomeLab 设备，用 Mac Mini M4 来重构 HomeLab 的结构。

## 运行 Deepseek-r1 大模型（7b&14b）

被 Deepseek 新闻轰炸了数日，必将其在 Mac Mini M4 上测一下。首先需要下载并安装 ollama 应用，然后下载并运行该模型，并于命令行问一个问题 “macmini m4 适合使用什么参数规模的 Deepseek 模型?”。

```bash
martinliu@Mac-mini ~ % ollama  pull deepseek-r1:7b
pulling manifest 
pulling 96c415656d37... 100% ▕███████████████████████████████████████████████████████████████████▏ 4.7 GB                         
pulling 369ca498f347... 100% ▕███████████████████████████████████████████████████████████████████▏  387 B                         
pulling 6e4c38e1172f... 100% ▕███████████████████████████████████████████████████████████████████▏ 1.1 KB                         
pulling f4d24e9138dd... 100% ▕███████████████████████████████████████████████████████████████████▏  148 B                         
pulling 40fb844194b2... 100% ▕███████████████████████████████████████████████████████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success 

martinliu@Mac-mini ~ % ollama run deepseek-r1:7b
>>> macmini m4 适合使用什么参数规模的 Deepseek 模型?

```

ollama 下载和运行任何模型都很简单，用下面两条命令即可：

* `ollama pull deepseek-r1:7b`：下载 Deepseek-r1 7b 模型。
* `ollama run deepseek-r1:7b`：运行 Deepseek-r1 7b 模型。

我的第一个问题，并未说 Mac Mini 是何配置，而且问的比较模糊，[点这里查看答案全文](q1.txt)。

>答案的结论：Mac mini M4 在适合运行 DeepSeek 的 7B 和 13B 参数规模的模型上表现良好。虽然没有独立显卡，但其强大的计算能力和 macOS 系统的支持使其能够处理这些较大的模型。然而，需考虑系统的资源和应用兼容性，并根据个人需求评估是否值得投资。

测试失败，居然这个模型不知道：自己有 7b ，但没有 13b 这个规格的模型。此回复过程在 10 秒钟左右，并不慢。

顺便推荐一个命令行性能监控工具 “btop” （在 macos 上安装命令 ‘brew install btop’），可以实时监控 CPU 和内存的使用情况，貌似在这 10 多秒的过程中，CPU 使用率没有丝毫的波动，内存使用率在 70%左右。

因首个问答即失败，所以下载 14b 的模型，希望能有足够回答问题的能力。为了在 7b 和 14b 之间做对比，所以在下载 14b 模型前，先对 7b 提出这个相同的问题 “SRE 和 DevOps 的区别和相同之处是什么?一个企业应该先做哪个?”。

* [7b 模型的答案点这里](q2.txt)。很遗憾，7b 模型一开口就把 SRE 名词解释错误了“SRE（Service-Providing Software Engineering）”
* [14b 模型的答案点这里](q3.txt)，不得不说 14b 模型的答案令我满意了。

## 为家庭局域网提供大模型服务

Open WebUI 是个不错的选项。在 Mac Mini M4 上安装 Open WebUI 也很简单，只需运行下面的命令即可：

```bash
docker run -d -p 9005:8080 -e WEBUI_AUTH=False   --add-host=host.docker.internal:host-gateway  -v ./open-webui-data:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

参数解释：

* `-d`：后台运行。
* `-p 9005:8080`：将容器的 8080 端口映射到主机的 9005 端口。
* `-e WEBUI_AUTH=False`：关闭 WebUI 的认证。
* `--add-host=host.docker.internal:host-gateway`：解决容器内无法访问主机的问题。
* `-v ./open-webui-data:/app/backend/data`：将容器内的数据目录映射到主机的 `./open-webui-data` 目录。
* `--name open-webui`：指定容器的名称为 `open-webui`。
* `--restart always`：容器退出时自动重启。
* `ghcr.io/open-webui/open-webui:main`：指定容器的镜像。
  
然后就可以在浏览器中访问 `http://192.168.31.6:9005` 来使用 Open WebUI 了。

![Open WebUI](open-webui.png)

Open WebUI 可以识别出我在后台容器中运行的 Deepseek-r1 14b 模型，它提供了基于网页的问答互动界面，而且对具有政治倾向的问题，回答的不置可否，体现出非常谨慎的态度。

下面是在手机端问的另外一个问题，回答是令我满意的。

![Open WebUI Mobile](iphone-webUI.png)

也就是说：局域网中的任何移动设备和电脑，都可以通过浏览器访问 Open WebUI，来使用 Deepseek-r1 14b 模型。

## 用 OrbStack 运行容器服务

OrbStack 在我的 MacBook Pro 上已经使用了一段时间了，已经平替了 Docker Desktop。而且和一众其它的 K8s 管理工具，包括 MiniKube、Kind 等。个人的一些使用经验总结：

* OrbStack 项目的编程语言有： Go Swift C Rust，它本身启动速度快，轻量。是苹果原生应用。比 Docker Desktop 占用的资源少非常多。
* 创建虚拟机的创建速度飞快，通过预下载的虚拟机镜像文件，结合 cloud-init.yaml 文件，可以在几秒钟内创建一个任意配置的新的虚拟机。
* 虚拟机和容器里的文件系统，都可以通过 Finder 直接访问，非常方便。而且在虚拟机内的 /mnt/ 目录下也能访问到主机的文件系统。
* 可以用 SSH 直接无密码登录虚拟机。
* 容器和虚拟机都无缝衔接 Host 上的网络，并共享科学上网的功能。在也不会下载不到容器镜像了。
* 自动识别 Docker 和 K8s 中的服务定义，并提供本机可信的 HTTPS 证书，实现 HTTPS 访问。可以很方便的进行开发和测试。

基于此，我决定在 Mac Mini M4 上安装 OrbStack，用它来管理所有需要长运行的服务。不过我做了一些定制化的配置：

* 如果用它运行各种 HomeLab 的网络服务，那么存储空间是需要扩展的。我在 Mac Mini M4 上用雷电4 接口连了普通的硬盘盒，内置 2TB 的 NVME 硬盘，实践表明性价比足够用了。
* 将 OrbStack 的默认存储空间设置为外置硬盘，这样可以避免内置硬盘的频繁读写，延长其寿命。而且外置硬盘的容量更大，可以存储更多的数据。
* 在 K8s 和 Docker 之间，我做了一个选择，决定在 Mac Mini M4 上只运行 Docker 容器，而不运行 K8s 集群。因为我觉得 Docker 容器更加轻量，更加简单，后续软件的升级和数据迁移也都更加方便。用 Docker Compose 的方式运行服务，尽量将持久化数据和配置文件放在外置硬盘上，这样即使机器挂了，数据也不会丢失，而且更方便做升级和迁移。

## 娱乐功能

首先，我将使用率较低的两只立体声音箱，通过 Mac Mini M4 的耳机接口，用音频线链接起来了。这样它就变成了一个 AirPlay 推流的目标。在 MacBook Pro 或者 iPhone 上，我可以通过 AirPlay 将音乐推送到 Mac Mini M4 上，然后通过音箱播放出来。这样，房间里就可以很方便的播放各种背景音乐了。音量可音箱上，在 MacBook 上，或者在 iPhone 上都可以调节。

> 从 Macbook 上推流音乐的方式是：打开苹果自家的 Music 软件，导入喜欢听的音乐文件，然后在播放界面，点击右上角的 AirPlay 图标，选择 Mac Mini M4，然后就可以听到音乐了。

![Mac Music AirPlay](mac-music.png)

> 从 iPhone 上可以通过屏幕镜像的功能，将任何视频或者音频 App 的声音推送到 Mac Mini M4 上。这样就可以在 Mac Mini M4 上播放 iPhone 上的任何音乐或者视频的声音了。

## 总结

Mac Mini M4 作为 HomeLab 的核心设备，性价比很高。在增加了外置磁盘空间后，它的性能和容量都可以作为长期运行的低功耗服务器使用。另外，我从即将淘汰的服务器中，拼装了一台开放机箱的 PVE 服务器，它有一颗 12 core 的 Xeon E5 CPU ，有 128GB 内存，有 1 块 520GB 的 NVME 硬盘，还有 4 块总容量为 3TB 的 SSD 硬盘。这台 PVE 上的所有虚拟机和 LXC 都可以访问到 Mac Mini M4 上的所有服务，这样就可以实现资源的共享和互通。PVE 服务器在需要使用的时候，可以开机，不需要的时候，可以关机。未来，我可能只会保留 Mac Mini M4 和这台 PVE 服务器，其它的设备都会被淘汰到海鲜市场。
