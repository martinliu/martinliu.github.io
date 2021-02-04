---
title: Tips for Docker on Mac
subtitle: macOS上的一些docker使用tips
date: 2017-09-26
bigimg: [{src: "/images/sandrali-3.JPG",  desc: "前门 by Sandra Li" }]
tags:
- DevOps
- Docker
postmeta: false
---

# Tips for Docker on Mac

在macOS上使用Docker很长时间了，本文总结一些我不想忘记的tips，方便自己反复使用的同时，也顺便总结分享一下，留下本文作为长期更新的备忘录。

## 搭建私有镜像库
运行一个本地镜像库


```
$ docker run -d  -p 5000:5000 --restart=always --name registry registry:2
```

这条命令会从docker hub 下载 registry:2 镜像，在本机运行一个镜像库服务。

下载一个测试用的镜像。


```
$ docker pull ubuntu:16.04
```

给这个镜像打上私有镜像库的标签

```
$ docker tag ubuntu:16.04 localhost:5000/ubuntu:16.04
```
push这个测试镜像到本地的镜像库

```
$ docker push localhost:5000/ubuntu:16.04
```
这时候你会发现我的本地这样岂不是有了两份相同的镜像了，有这个必要么？是不是多余了？下面几个场景中会用到：

当你用docker-machine在本机启动1个vm的时候，你运行任何docker run或者docker-compose up的时候你可能需要一个之前在本地就有的image，这是一种分享本机image给docker-machine vm的一种方式。

当你用docker-machine在本机启动多个个vm的时候，你可能会把它们作出docker Swarm群集，当你在这个群集上启动一个服务的时候，docker compose文件中的镜像地址可以引用这个本地地址，引用地址类似这样 image: 192.168.99.1:5000/influxdb

当你用 minikube start启动了一个minikube的vm的时候，你可能也需要本机的docker镜像，尤其是在你做demo的时候，这是最快的下载途径。
需要注意的是，以上三种情况都需要指定一下--engine-insecure-registry 192.168.99.1:5000 这个参数。

## 自动化创建Docker Swarm群集

在我的文件目录中存放着这个脚本

```
cat create-swarm.sh
docker-machine create manager  --engine-insecure-registry 192.168.99.1:5000
docker-machine create agent1  --engine-insecure-registry 192.168.99.1:5000
docker-machine create agent2  --engine-insecure-registry 192.168.99.1:5000
docker-machine create agent3  --engine-insecure-registry 192.168.99.1:5000
eval `docker-machine env manager`
docker swarm init --advertise-addr `docker-machine ip manager`
docker-machine ssh agent1 docker swarm join --token `docker swarm join-token -q worker` `docker-machine ip manager`:2377
docker-machine ssh agent2 docker swarm join --token `docker swarm join-token -q worker` `docker-machine ip manager`:2377
docker-machine ssh agent3 docker swarm join --token `docker swarm join-token -q worker` `docker-machine ip manager`:2377
docker node ls
```

解释一下上面的代码：创建四个docker-machine vm，初始化swarm群集，把三个worker节点加入群集。这样四节点的群集就up and running了。

清除以上群集虚拟机的命令如下：

```
docker-machine rm -y manager agent1 agent2 agent3
```


