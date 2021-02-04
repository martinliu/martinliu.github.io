---
author: liuadmin
categories:
- Container
comments: true
date: 2016-07-01T03:11:10Z
slug: devops-in-a-box
tags:
- docker
- Habitat
- rancher
title: DevOps 的起点-入手微型数据中心
url: /2016/07/01/devops-in-a-box/
wordpress_id: 54178
---

## 测试环境说明


我的笔记本电脑的环境描述如下。


### OS


MacBook Pro 2011 版， 2.3 GHz Intel Core i5， 8GB DDR3， 256 GB SSD。 OS X EI Capitan version 10.11.5


### Docker


Docker for Mac Version 1.12.0-rc2-beta17 (build: 9779)




```
$ docker version
Client:
 Version:      1.12.0-rc2
 API version:  1.24
 Go version:   go1.6.2
 Git commit:   906eacd
 Built:        Fri Jun 17 20:35:33 2016
 OS/Arch:      darwin/amd64
 Experimental: true

Server:
 Version:      1.12.0-rc2
 API version:  1.24
 Go version:   go1.6.2
 Git commit:   a7119de
 Built:        Wed Jun 29 10:03:33 2016
 OS/Arch:      linux/amd64
 Experimental: true
 
  $ docker-machine version
docker-machine version 0.8.0-rc1, build fffa6c9

martin@localhost ~/Documents                                                                                  [9:38:31]
 $ docker-compose version
docker-compose version 1.8.0-rc1, build 9bf6bc6
docker-py version: 1.8.1
CPython version: 2.7.9
OpenSSL version: OpenSSL 1.0.2h  3 May 2016


```




VirtualBox version 5.0.22r108108


### 本机下载的 Docker 镜像




/Users/martin/Downloads/1.12.0-rc2/boot2docker.iso 

~/Downloads/rancher-all/rancher-agent-v1.0.1.tar 

~/Downloads/rancher-all/rancher-agent-instance-v0.8.1.tar 

~/Downloads/habitat-docker-registry.bintray.io-studio.tar 

~/Downloads/rancher-all/rancher-server-stable.tar


我本机还有一个 Docker Registry 的 vm，这里面提供了我需要积累以后用的镜像存储，想象一下你在飞机上的时候去哪里拉取镜像 ：）


### 本机下载的代码


https://github.com/habitat-sh/habitat-example-plans https://github.com/janeczku/habitat-plans https://github.com/chrisurwin/may2016-demo https://github.com/docker/example-voting-app

注意以上代码可能需要修改才能在本机调试成功。


## 创建 Rancher 服务器




### 生成虚拟机


用 docker-machine 创建 rancher 服务器。




```
docker-machine create rancher --driver virtualbox --virtualbox-cpu-count "1" --virtualbox-disk-size "8000" --virtualbox-memory "1024" --virtualbox-boot2docker-url=/Users/martin/Downloads/1.12.0-rc2/boot2docker.iso && eval $(docker-machine env rancher)

```






### 导入 Rancher 服务器镜像


用 docker-machine ls 应该看到 rancher 这个节点打了星号。否则 docker 命令会执行失败或者错误。




```
docker load < ~/Downloads/rancher-all/rancher-server-stable.tar
docker run -d --restart=always --name rancher-srv -p 8080:8080 rancher/server:stable 
docker logs -f rancher-srv

```



查看 rancher 服务器的 ip 地址。 docker-machine ip rancher

用浏览器打开Rancher 服务器的登录页面。 open http://Rancher_Server_IP:8080

下面是一些如何让虚拟机保持固定 IP 和 rancher 容器存储的数据持久存在的代码，我没有测试成功，留下大家一起搞，成功了，给我一个回复。另外还有关于稿 jekins 和 mirror 的代码。




```
echo "ifconfig eth1 192.168.99.60 netmask 255.255.255.0 broadcast 192.168.99.255 up" | docker-machine ssh node1 sudo tee /var/lib/boot2docker/bootsync.sh > /dev/null
docker-machine regenerate-certs node1 -f
docker-machine ssh ndoe1
sudo mkdir /mnt/sda1/var/lib/rancher 


docker@node1:/mnt/sda1/var/lib/boot2docker$ cat bootsync.sh
ifconfig eth1 192.168.99.60 netmask 255.255.255.0 broadcast 192.168.99.255 up

sudo mkdir /mnt/sda1/var/lib/rancher/
sudo ln -s /mnt/sda1/var/lib/rancher/ /var/lib/



docker load < ~/Downloads/rancher-all/jenkins.tar

docker run -d --name jekins --privileged -p 9001:8080 -v /var/lib/docker/:/var/lib/docker/ -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker  -v /lib64/libdevmapper.so.1.02:/usr/lib/libdevmapper.so.1.02  --label io.rancher.container.network=true jenkins


docker-machine create mirror --driver virtualbox --virtualbox-cpu-count "1" --virtualbox-disk-size "8000" --virtualbox-memory "512" --virtualbox-boot2docker-url=/Users/martin/Downloads/boot2docker.iso 

docker load < ~/Downloads/rancher-all/registry.tar
docker run -d -p 80:5000 --restart=always --name registry registry:2

```





## 容器运行节点 Rancher Agent 节点




### 创建 node1 虚拟机


使用 docker-machine  命令创建容器运行节点。




```
docker-machine create node1 --driver virtualbox --engine-insecure-registry 192.168.99.20:5000 --virtualbox-cpu-count "1" --virtualbox-disk-size "80000" --virtualbox-memory "1024" --virtualbox-boot2docker-url=/Users/martin/Downloads/1.12.0-rc2/boot2docker.iso 

docker-machine create node2 --driver virtualbox --engine-insecure-registry 192.168.99.20:5000 --virtualbox-cpu-count "1" --virtualbox-disk-size "80000" --virtualbox-memory "1024" --virtualbox-boot2docker-url=/Users/martin/Downloads/1.12.0-rc2/boot2docker.iso 

```


在 node1 或者 node2 测试运行一个容器，使用 mirror 中的 busybox 镜像。如果你的笔记本内存小于8GB 的话，node2就别搞了。一个 node 也够用了。




```
docker pull 192.168.99.20:5000/busybox:latest 

```


docker run 一下这个镜像，验证 node1工作正常。


### 加载 Rancher Agent 的镜像


确保 node1 是 docker-machine ls 中打星号的。




```
docker load < ~/Downloads/rancher-all/rancher-agent-v1.0.1.tar
docker load < ~/Downloads/rancher-all/rancher-agent-instance-v0.8.1.tar
docker load < ~/Downloads/habitat-docker-registry.bintray.io-studio.tar

```


你翻墙下载回来的habitat-docker-registry.bintray.io/studio镜像可能需要打标签，否则回头 hab 命令执行失败。 先用 docer images 看下是否所有 image 的标签信息正确。


```
docker tag fc27342e5e0e habitat-docker-registry.bintray.io/studio:latest
```



### 添加 node1 节点到 Rancher Server。






```
docker run -d --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/rancher:/var/lib/rancher rancher/agent:v1.0.1 http://192.168.99.100:8080/v1/scripts/33B68ED65CEF18F6D7BD:1466694000000:lug2KswoXOOQV4d09ZNMGTphVs0

```



<blockquote>注意：以上命令需要到您的 Rancher Server 的页面上获取，否则参数都是不对的。</blockquote>


现在在 Hosts 页面上应该能看到该刚创建的节点。在页面上创建一个最小化的容器（如 busybox），来拉起 Network Agent 容器。


## 调试 habitat 的测试程序


参考的文档 https://www.habitat.sh/tutorials/ 记得一定要把这一组文章先看完，在去调试它的代码，不懂这些基本概念的话，后面对了错了都不知道该怎么搞。

前置条件，翻墙下载 habitat studio 的 docker image 镜像，load 到 node1 上，下面的所有测试都是在 node1 上完成的。


### 安装 hab


habitat 的程序只有一个可执行程序， 目前支持 mac 和 linux 版本。下载地址： https://www.habitat.sh/docs/get-habitat 就是一个 tag 包，解压缩后放到 shell 的 PATH 里面就安装完了。


### 配置 hab cli


运行 hab setup




```
martin@localhost ~/Documents                                                                                  $ hab setup

Habitat CLI Setup
=================

  Welcome to hab setup. Let's get started.

Set up a default origin

  Every package in Habitat belongs to an origin, which indicates the
  person or organization responsible for maintaining that package. Each
  origin also has a key used to cryptographically sign packages in that
  origin.

  Selecting a default origin tells package building operations such as
  'hab pkg build' what key should be used to sign the packages produced.
  If you do not set a default origin now, you will have to tell package
  building commands each time what origin to use.

  For more information on origins and how they are used in building
  packages, please consult the docs at
  https://www.habitat.sh/docs/build-packages-overview/

Set up a default origin? [Yes/no/quit] yes 这里输入 yes

  Enter the name of your origin. If you plan to publish your packages
  publicly, we recommend that you select one that is not already in use on
  the Habitat build service found at https://app.habitat.sh/.

  You already have a default origin set up as `martin', but feel free to
  change it if you wish.

Default origin name: [default: martin] 这是用来做 Habitat 包签名和加密用的标识，在代码里面会用到。

  You already have an origin key for martin created and installed. Great
  work!

GitHub Access Token

  While you can build and run Habitat packages without sharing them on the
  public depot, doing so allows you to collaborate with the Habitat
  community. In addition, it is how you can perform continuous deployment
  with Habitat.

  The depot uses GitHub authentication with an access token
  (https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

  If you would like to share your packages on the depot, please enter your
  GitHub access token. Otherwise, just enter No.

  For more information on sharing packages on the depot, please read the
  documentation at https://www.habitat.sh/docs/share-packages-overview/

Set up a default GitHub access token? [Yes/no/quit] yes 这里选择yes

  Enter your GitHub access token.

  You already have a default auth token set up, but feel free to change it
  if you wish.

GitHub access token: [default: martin-github-token]  这个 token 需要自己去 github 里面生成

Analytics

  The `hab` command-line tool will optionally send anonymous usage data to
  Habitat's Google Analytics account. This is a strictly opt-in activity
  and no tracking will occur unless you respond affirmatively to the
  question below.

  We collect this data to help improve Habitat's user experience. For
  example, we would like to know the category of tasks users are
  performing, and which ones they are having trouble with (e.g. mistyping
  command line arguments).

  To see what kinds of data are sent and how they are anonymized, please
  read more about our analytics here:
  https://www.habitat.sh/docs/about-analytics/

Enable analytics? [yes/No/quit] no 这里选择 no
» Opting out of analytics
☑ Creating /Users/martin/.hab/cache/analytics/OPTED_OUT
★ Analytics opted out, we salute you just the same!

CLI Setup Complete

  That's all for now. Thanks for using Habitat!


martin@localhost ~/Documents                                                                                 $

```





该注意的都写到上面的代码里面了。这个配置的结果在这里




```
$ cat ~/.hab/etc/cli.toml
auth_token = "martin-github-token"
origin = "martin"

```




### 调试 Habitat demo 应用


```
git clone https://github.com/habitat-sh/habitat-example-plans
```


进入到 mytutorialapp 目录，修改 plan.sh 的 第二行代码，我改后的代码是

```
pkg_origin=martin
```

martin 是我在 hab cli 里面配置的 origin。

其实下面的测试就执行了两个 hab 的命令，都是在 hab studi 的 shell里面执行的，这个 shell 其实就是一个studio 容器的 shell。

在运行下面的命令，确保你是和 node1正常通讯的，下面我用 default 节点做演示。做完的演示环境我已经删除了。




```
$ docker-machine ls                                                                                      NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
default   -        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.1

$ docker ps                                                                                              CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES


```


正常的意思是执行所有 docker 命令不报错。


### build habitat demo 代码


进入到代码的 plan.sh 的目录 执行 hab studio enter 命令。




```
martin@localhost ~/Documents/GitHub/habitat-example-plans/mytutorialapp                                      
 $ hab studio enter                                                                                       [±master ●●]
   hab-studio: Creating Studio at /hab/studios/src (default)
   hab-studio: Importing martin secret origin key
» Importing origin key from standard input
★ Imported secret origin key martin-20160630040241.
   hab-studio: Entering Studio at /hab/studios/src (default)
   hab-studio: Exported: HAB_ORIGIN=martin

[1][default:/src:0]# build
   : Loading /src/plan.sh
   mytutorialapp: Plan loaded
   mytutorialapp: hab-plan-build setup
   mytutorialapp: Using HAB_BIN=/hab/pkgs/core/hab/0.7.0/20160614230104/bin/hab for installs, signing, and hashing
   mytutorialapp: Resolving dependencies
» Installing core/node
→ Using core/gcc-libs/5.2.0/20160612075020
→ Using core/glibc/2.22/20160612063629
→ Using core/linux-headers/4.3/20160612063537
↓ Downloading core/node/4.2.6/20160612143531
    6.44 MB / 6.44 MB \ [=======================================================================] 100.00 % 457.82 KB/s  ↓ Downloading core-20160612031944 public origin key
    75 B / 75 B | [=============================================================================] 100.00 % 575.13 KB/s  ☑ Cached core-20160612031944 public origin key
✓ Installed core/node/4.2.6/20160612143531
★ Install of core/node complete with 4 packages installed.
   mytutorialapp: Resolved dependency 'core/node' to /hab/pkgs/core/node/4.2.6/20160612143531
   mytutorialapp: Setting PATH=/hab/pkgs/core/node/4.2.6/20160612143531/bin:/hab/pkgs/core/hab-plan-build/0.7.0/20160614232259/bin:/hab/pkgs/core/bash/4.3.42/20160612075613/bin:/hab/pkgs/core/binutils/2.25.1/20160612064534/bin:/hab/pkgs/core/bzip2/1.0.6/20160612075040/bin:/hab/pkgs/core/coreutils/8.24/20160612075329/bin:/hab/pkgs/core/file/5.24/20160612064523/bin:/hab/pkgs/core/findutils/4.4.2/20160612080341/bin:/hab/pkgs/core/gawk/4.1.3/20160612075739/bin:/hab/pkgs/core/grep/2.22/20160612075540/bin:/hab/pkgs/core/gzip/1.6/20160612080637/bin:/hab/pkgs/core/hab/0.7.0/20160614230104/bin:/hab/pkgs/core/sed/4.2.2/20160612075228/bin:/hab/pkgs/core/tar/1.28/20160612075701/bin:/hab/pkgs/core/unzip/6.0/20160612081414/bin:/hab/pkgs/core/wget/1.16.3/20160612081342/bin:/hab/pkgs/core/xz/5.2.2/20160612080402/bin:/hab/pkgs/core/acl/2.2.52/20160612075215/bin:/hab/pkgs/core/attr/2.4.47/20160612075207/bin:/hab/pkgs/core/glibc/2.22/20160612063629/bin:/hab/pkgs/core/less/481/20160612080021/bin:/hab/pkgs/core/libcap/2.24/20160612075226/bin:/hab/pkgs/core/libidn/1.32/20160612081104/bin:/hab/pkgs/core/ncurses/6.0/20160612075116/bin:/hab/pkgs/core/openssl/1.0.2h/20160612081127/bin:/hab/pkgs/core/pcre/8.38/20160612075520/bin
mkdir: created directory '/hab/cache/src'
   mytutorialapp: Downloading 'https://s3-us-west-2.amazonaws.com/mytutorialapp/mytutorialapp-0.1.0.tar.gz' to 'mytutorialapp-0.1.0.tar.gz'
--2016-07-01 02:27:51--  https://s3-us-west-2.amazonaws.com/mytutorialapp/mytutorialapp-0.1.0.tar.gz
Resolving s3-us-west-2.amazonaws.com (s3-us-west-2.amazonaws.com)... 54.231.184.216
Connecting to s3-us-west-2.amazonaws.com (s3-us-west-2.amazonaws.com)|54.231.184.216|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1041 (1.0K) [application/x-gzip]
Saving to: 'mytutorialapp-0.1.0.tar.gz'

mytutorialapp-0.1.0.tar.gz    100%[===================================================>]   1.02K  --.-KB/s   in 0.03s

2016-07-01 02:28:08 (32.1 KB/s) - 'mytutorialapp-0.1.0.tar.gz' saved [1041/1041]

   mytutorialapp: Downloaded 'mytutorialapp-0.1.0.tar.gz'
   mytutorialapp: Verifying mytutorialapp-0.1.0.tar.gz
   mytutorialapp: Checksum verified for mytutorialapp-0.1.0.tar.gz
   mytutorialapp: Clean the cache
   mytutorialapp: Unpacking mytutorialapp-0.1.0.tar.gz
   mytutorialapp: Setting build environment
   mytutorialapp: Setting PREFIX=/hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725
   mytutorialapp: Setting LD_RUN_PATH=/hab/pkgs/core/node/4.2.6/20160612143531/lib
   mytutorialapp: Setting CFLAGS=-I/hab/pkgs/core/node/4.2.6/20160612143531/include
   mytutorialapp: Setting LDFLAGS=-L/hab/pkgs/core/node/4.2.6/20160612143531/lib
   mytutorialapp: Preparing to build
   mytutorialapp: Building
npm WARN package.json mytutorialapp@0.1.0 No repository field.
npm WARN package.json mytutorialapp@0.1.0 No README data
nconf@0.8.4 node_modules/nconf
├── ini@1.3.4
├── secure-keys@1.0.0
├── async@1.5.2
└── yargs@3.32.0 (decamelize@1.2.0, camelcase@2.1.1, window-size@0.1.4, y18n@3.2.1, os-locale@1.4.0, cliui@3.2.0, string-width@1.0.1)
   mytutorialapp: Installing
'node_modules/nconf' -> '/hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/node_modules/nconf'

忽略了好几百行输出

'node_modules/nconf/node_modules/secure-keys/test/simple-test.js' -> '/hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/node_modules/nconf/node_modules/secure-keys/test/simple-test.js'
'node_modules/nconf/node_modules/secure-keys/test/test.secret.key' -> '/hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/node_modules/nconf/node_modules/secure-keys/test/test.secret.key'
'node_modules/nconf/node_modules/secure-keys/package.json' -> '/hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/node_modules/nconf/node_modules/secure-keys/package.json'
   mytutorialapp: Writing configuration
   mytutorialapp: Writing service management scripts
   mytutorialapp: Stripping unneeded symbols from binaries and libraries
   mytutorialapp: Creating manifest
   mytutorialapp: Building package metadata
   mytutorialapp: Generating blake2b hashes of all files in the package
   mytutorialapp: Generating signed metadata FILES
» Signing mytutorialapp_blake2bsums
☛ Signing mytutorialapp_blake2bsums with martin-20160630040241 to create /hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/FILES
★ Signed artifact /hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725/FILES.
   mytutorialapp: Generating package artifact
/hab/pkgs/core/tar/1.28/20160612075701/bin/tar: Removing leading `/' from member names
/hab/cache/artifacts/.martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.tar (1/1)
  100 %       121.4 KiB / 900.0 KiB = 0.135
» Signing /hab/cache/artifacts/.martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.tar.xz
☛ Signing /hab/cache/artifacts/.martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.tar.xz with martin-20160630040241 to create /hab/cache/artifacts/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart
★ Signed artifact /hab/cache/artifacts/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart.
'/hab/cache/artifacts/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart' -> '/src/results/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart'
   mytutorialapp: hab-plan-build cleanup
   mytutorialapp:
   mytutorialapp: Source Cache: /hab/cache/src/mytutorialapp-0.1.0
   mytutorialapp: Installed Path: /hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725
   mytutorialapp: Artifact: /src/results/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart
   mytutorialapp: Build Report: /src/results/last_build.env
   mytutorialapp: SHA256 Checksum: d4bfb3a44989b8a5b1295eac2600d75f42dd2be6f537344312c8917cba47d05d
   mytutorialapp: Blake2b Checksum: fbff257eb36fffa61e6cbf5ec89fa3f507095f80f5cca610c2bb72685d758706
   mytutorialapp:
   mytutorialapp: I love it when a plan.sh comes together.
   mytutorialapp:
   mytutorialapp: Build time: 1m3s
[2][default:/src:0]#

```



检查结果，在代码的目录中可以看的 result 目录，关注一下这个目录，关键看 build 命令的最后一段。 

```

mytutorialapp: hab-plan-build cleanup mytutorialapp: mytutorialapp: Source Cache: /hab/cache/src/mytutorialapp-0.1.0 mytutorialapp: Installed Path: /hab/pkgs/martin/mytutorialapp/0.1.0/20160701022725 mytutorialapp: Artifact: /src/results/martin-mytutorialapp-0.1.0-20160701022725-x86_64-linux.hart mytutorialapp: Build Report: /src/results/last_build.env mytutorialapp: SHA256 Checksum: d4bfb3a44989b8a5b1295eac2600d75f42dd2be6f537344312c8917cba47d05d mytutorialapp: Blake2b Checksum: fbff257eb36fffa61e6cbf5ec89fa3f507095f80f5cca610c2bb72685d758706 mytutorialapp: mytutorialapp: I love it when a plan.sh comes together. mytutorialapp: mytutorialapp: Build time: 1m3s

```


### 昨晚分享的高潮部分, habitat 导出 docker image


其实就是一条命令，在 habitat Studio 中执行 导出命令 hab pkg export docker martin/mytutorialapp

导出 docker 镜像的过程和 build 的过程一样，都可能会失败；由于它需要到网上下载所需要的代码，下载所需要的 habitat 模块，core/ 开头的都是 habitat出品的核心的模块，他们的想法基本也是说把所有的可能用到的模块都做封装，成为自己的 pkg 格式的内容。然后在用他们的 Habitat 服务来解析、部署和运行。




```
[4][default:/src:0]#  hab pkg export docker martin/mytutorialapp
   hab-studio: Creating Studio at /tmp/hab-pkg-dockerize-XxsS/rootfs (baseimage)
 Using local package for martin/mytutorialapp
 Using local package for core/gcc-libs/5.2.0/20160612075020 via martin/mytutorialapp
 Using local package for core/glibc/2.22/20160612063629 via martin/mytutorialapp
 Using local package for core/linux-headers/4.3/20160612063537 via martin/mytutorialapp
 Using local package for core/node/4.2.6/20160612143531 via martin/mytutorialapp
» Installing core/hab
↓ Downloading core/hab/0.7.0/20160614230104
    2.23 MB / 2.23 MB / [=======================================================================] 100.00 % 500.60 KB/s  ↓ Downloading core-20160612031944 public origin key
    75 B / 75 B | [=============================================================================] 100.00 % 378.76 KB/s  ☑ Cached core-20160612031944 public origin key
✓ Installed core/hab/0.7.0/20160614230104
★ Install of core/hab complete with 1 packages installed.
» Installing core/hab-sup
↓ Downloading core/busybox-static/1.24.2/20160612081725
    510.89 KB / 510.89 KB | [====================================================================] 100.00 % 89.61 KB/s  ✓ Installed core/busybox-static/1.24.2/20160612081725
↓ Downloading core/bzip2/1.0.6/20160612075040
    141.05 KB / 141.05 KB - [===================================================================] 100.00 % 349.94 KB/s  ✓ Installed core/bzip2/1.0.6/20160612075040
↓ Downloading core/cacerts/2016.04.20/20160612081125
    132.32 KB / 132.32 KB | [===================================================================] 100.00 % 370.21 KB/s  ✓ Installed core/cacerts/2016.04.20/20160612081125
→ Using core/gcc-libs/5.2.0/20160612075020
→ Using core/glibc/2.22/20160612063629
↓ Downloading core/libarchive/3.2.0/20160612140528
    584.98 KB / 584.98 KB | [===================================================================] 100.00 % 340.75 KB/s  ✓ Installed core/libarchive/3.2.0/20160612140528
↓ Downloading core/libsodium/1.0.8/20160612140317
    187.96 KB / 187.96 KB \ [===================================================================] 100.00 % 200.27 KB/s  ✓ Installed core/libsodium/1.0.8/20160612140317
→ Using core/linux-headers/4.3/20160612063537
↓ Downloading core/openssl/1.0.2h/20160612081127
    2.10 MB / 2.10 MB | [=======================================================================] 100.00 % 518.78 KB/s  ✓ Installed core/openssl/1.0.2h/20160612081127
↓ Downloading core/xz/5.2.2/20160612080402
    247.38 KB / 247.38 KB \ [===================================================================] 100.00 % 468.42 KB/s  ✓ Installed core/xz/5.2.2/20160612080402
↓ Downloading core/zlib/1.2.8/20160612064520
    73.06 KB / 73.06 KB / [=====================================================================] 100.00 % 315.44 KB/s  ✓ Installed core/zlib/1.2.8/20160612064520
↓ Downloading core/hab-sup/0.7.0/20160614232939
    1.54 MB / 1.54 MB | [=======================================================================] 100.00 % 563.90 KB/s  ✓ Installed core/hab-sup/0.7.0/20160614232939
★ Install of core/hab-sup complete with 12 packages installed.
» Symlinking hab from core/hab into /tmp/hab-pkg-dockerize-XxsS/rootfs/hab/bin
★ Binary hab from core/hab/0.7.0/20160614230104 symlinked to /tmp/hab-pkg-dockerize-XxsS/rootfs/hab/bin/hab
» Symlinking bash from core/busybox-static into /tmp/hab-pkg-dockerize-XxsS/rootfs/bin
★ Binary bash from core/busybox-static/1.24.2/20160612081725 symlinked to /tmp/hab-pkg-dockerize-XxsS/rootfs/bin/bash
» Symlinking sh from core/busybox-static into /tmp/hab-pkg-dockerize-XxsS/rootfs/bin
★ Binary sh from core/busybox-static/1.24.2/20160612081725 symlinked to /tmp/hab-pkg-dockerize-XxsS/rootfs/bin/sh
Sending build context to Docker daemon 194.3 MB
Step 1 : FROM scratch
 --->
Step 2 : ENV export PATH=:/hab/pkgs/core/glibc/2.22/20160612063629/bin:/hab/pkgs/core/node/4.2.6/20160612143531/bin:/hab/pkgs/core/hab-sup/0.7.0/20160614232939/bin:/hab/pkgs/core/busybox-static/1.24.2/20160612081725/bin:/hab/pkgs/core/bzip2/1.0.6/20160612075040/bin:/hab/pkgs/core/glibc/2.22/20160612063629/bin:/hab/pkgs/core/openssl/1.0.2h/20160612081127/bin:/hab/pkgs/core/xz/5.2.2/20160612080402/bin:/hab/pkgs/core/busybox-static/1.24.2/20160612081725/bin:/hab/bin
 ---> Running in 117e90c151e7
 ---> 7f33585a25ae
Removing intermediate container 117e90c151e7
Step 3 : WORKDIR /
 ---> Running in 952257966d96
 ---> c0cf3715cbcf
Removing intermediate container 952257966d96
Step 4 : ADD rootfs /
 ---> d2691da93ccf
Removing intermediate container 4aa80e97ea57
Step 5 : VOLUME /hab/svc/mytutorialapp/data /hab/svc/mytutorialapp/config
 ---> Running in f1edcb653432
 ---> bd8888453939
Removing intermediate container f1edcb653432
Step 6 : EXPOSE 9631 8080
 ---> Running in 9ca7725ed13e
 ---> 256a04cd0fe2
Removing intermediate container 9ca7725ed13e
Step 7 : ENTRYPOINT /init.sh
 ---> Running in 81930dff8f4e
 ---> d7bdec08530e
Removing intermediate container 81930dff8f4e
Step 8 : CMD start martin/mytutorialapp
 ---> Running in c8cc53d92bc8
 ---> 8d5e0fe85395
Removing intermediate container c8cc53d92bc8
Successfully built 8d5e0fe85395
[5][default:/src:0]#

```

查看 docker 镜像是否存在。推出 studio 容器，运行 docker images




```
[5][default:/src:0]# exit
logout

martin@localhost ~/Documents/GitHub/habitat-example-plans/mytutorialapp                                       $ docker images                                                                                          [±master ●●]
REPOSITORY                                  TAG                    IMAGE ID            CREATED             SIZE
martin/mytutorialapp                        0.1.0-20160701024401   8d5e0fe85395        3 minutes ago       187.7 MB
martin/mytutorialapp                        latest                 8d5e0fe85395        3 minutes ago       187.7 MB


```



### 运行这个 demo


在命令行运行

$ docker run -it -p 8080:8080 martin/mytutorialapp

用浏览器打开 node1的 ip 8080 端口，应该可以看到 hello world 页面。

在 rancher web 页面添加测试


### 在 rancher 中上架这个 demo


https://github.com/martinliu/hab-catalog 以上代码是半成品，欢迎协助完成。


### 测试 Rancher 官方的 redis demo


参考文章 http://rancher.com/using-habitat-to-create-rancher-catalog-templates/ 它的 demo 和上架的目录都可以正常测试通过，但是服务运行不起来，报主机名错误，redis 节点的群集建立不起来。

如果您修复了，请回复贴出代码位置。


## 福利：调试 docker 官方投票应用


下载投票实例程序。




```
git clone https://github.com/martinliu/example-voting-app.git

```



进入该程序的目录，修改所有 image 的来源镜像库，修改为指向本地的 mirror 服务器。 1. result/tests/Dcokerfile -> FROM 192.168.99.20:5000/node 2. result/Dockerfile -> FROM 192.168.99.20:5000/node:5.11.0-slim 3. vote/Dockerfile -> FROM 192.168.99.20:5000/python:2.7-alpine 4. worker/Dockerfile -> FROM 192.168.99.20:5000/microsoft/dotnet:1.0.0-preview1 5. docker-compose.yml -> image: 192.168.99.20:5000/redis:alpine 6. docker-compose.yml -> image: 192.168.99.20:5000/postgres:9.4

由于以上应用在构建的过程中需要在线安装各种软件包，最好先翻墙，确认你有足够稳定的国外的互联网访问，建议翻墙到美国，然后在执行项目的构建命令。




```
ping facebook.com
64 bytes from 173.252.90.132: icmp_seq=0 ttl=79 time=4187.066 ms
64 bytes from 173.252.90.132: icmp_seq=1 ttl=79 time=3186.904 ms
64 bytes from 173.252.90.132: icmp_seq=2 ttl=79 time=2515.415 ms
64 bytes from 173.252.90.132: icmp_seq=6 ttl=79 time=296.457 ms
64 bytes from 173.252.90.132: icmp_seq=7 ttl=79 time=410.215 ms
^C
--- facebook.com ping statistics ---
8 packets transmitted, 5 packets received, 37.5% packet loss
round-trip min/avg/max/stddev = 296.457/2119.211/4187.066/1537.275 ms

docker-compose build


```


以上结果表明，翻墙成功，以上结果显示翻墙的效果比较差，延迟和丢包都比较严重，可能到只构建的时候下载软件包失败。

构建完毕之后，可以检查一下是否生产了目标镜像文件，如果输出如下所示，则表明本次本地的项目集成构建成功。




```
$ docker images                                                                                                                            
REPOSITORY                            TAG                 IMAGE ID            CREATED             SIZE
examplevotingapp_result               latest              9bb4126b0905        5 minutes ago       225.8 MB
examplevotingapp_worker               latest              292396a5aba4        6 minutes ago       644.1 MB
examplevotingapp_vote                 latest              28052191beea        10 minutes ago      68.31 MB


```


在当前 node1 节点上做本地的集成结果的功能测试，用 docker-compose 启动这个项目。先检查 compose 文件，然后运行 up。




```
$ docker-compose config                                                                                                                      
networks: {}
services:
  db:
    image: 192.168.99.20:5000/postgres:9.4
  redis:
    image: 192.168.99.20:5000/redis:alpine
    ports:
    - '6379'
  result:
    build:
      context: /Users/martin/Documents/GitHub/example-voting-app/result
    command: nodemon --debug server.js
    ports:
    - 5001:80
    - 5858:5858
    volumes:
    - /Users/martin/Documents/GitHub/example-voting-app/result:/app:rw
  vote:
    build:
      context: /Users/martin/Documents/GitHub/example-voting-app/vote
    command: python app.py
    ports:
    - 5000:80
    volumes:
    - /Users/martin/Documents/GitHub/example-voting-app/vote:/app:rw
  worker:
    build:
      context: /Users/martin/Documents/GitHub/example-voting-app/worker
version: '2.0'
volumes: {}

$ docker-compose up                                                                                                                            
Recreating examplevotingapp_vote_1
Recreating examplevotingapp_worker_1
Starting examplevotingapp_db_1
Starting examplevotingapp_redis_1
Recreating examplevotingapp_result_1
Attaching to examplevotingapp_db_1, examplevotingapp_redis_1, examplevotingapp_worker_1, examplevotingapp_result_1, examplevotingapp_vote_1
redis_1   |                 _._
redis_1   |            _.-``__ ''-._
redis_1   |       _.-``    `.  `_.  ''-._           Redis 3.2.1 (00000000/0) 64 bit
redis_1   |   .-`` .-```.  ```\/    _.,_ ''-._
db_1      | LOG:  database system was shut down at 2016-06-20 09:58:19 UTC
redis_1   |  (    '      ,       .-`  | `,    )     Running in standalone mode
redis_1   |  |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
redis_1   |  |    `-._   `._    /     _.-'    |     PID: 1
redis_1   |   `-._    `-._  `-./  _.-'    _.-'
redis_1   |  |`-._`-._    `-.__.-'    _.-'_.-'|
redis_1   |  |    `-._`-._        _.-'_.-'    |           http://redis.io
redis_1   |   `-._    `-._`-.__.-'_.-'    _.-'
redis_1   |  |`-._`-._    `-.__.-'    _.-'_.-'|
db_1      | LOG:  MultiXact member wraparound protections are now enabled
redis_1   |  |    `-._`-._        _.-'_.-'    |
redis_1   |   `-._    `-._`-.__.-'_.-'    _.-'
db_1      | LOG:  database system is ready to accept connections
redis_1   |       `-._    `-.__.-'    _.-'
redis_1   |           `-._        _.-'
redis_1   |               `-.__.-'
redis_1   |
redis_1   | 1:M 20 Jun 10:13:36.216 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1   | 1:M 20 Jun 10:13:36.216 # Server started, Redis version 3.2.1
redis_1   | 1:M 20 Jun 10:13:36.216 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
db_1      | LOG:  autovacuum launcher started
redis_1   | 1:M 20 Jun 10:13:36.216 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis_1   | 1:M 20 Jun 10:13:36.216 * The server is now ready to accept connections on port 6379
vote_1    |  * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
vote_1    |  * Restarting with stat
result_1  | [nodemon] 1.9.2
result_1  | [nodemon] to restart at any time, enter `rs`
result_1  | [nodemon] watching: *.*
result_1  | [nodemon] starting `node --debug server.js`
result_1  | Debugger listening on port 5858
vote_1    |  * Debugger is active!
vote_1    |  * Debugger pin code: 139-254-286
worker_1  | Found redis at 172.19.0.2
result_1  | Mon, 20 Jun 2016 10:13:40 GMT body-parser deprecated bodyParser: use individual json/urlencoded middlewares at server.js:67:9
result_1  | Mon, 20 Jun 2016 10:13:40 GMT body-parser deprecated undefined extended: provide extended option at ../node_modules/body-parser/index.js:105:29
result_1  | App running on port 80
result_1  | Connected to db


```


打开浏览器测试 vote 应用。




```
open http://192.168.99.114:5000


```



正常显示结果如下图所示： ![voting](http://yzd.io/images/voting-1.jpg)

打开浏览器测试 result 应用。




```
open http://192.168.99.114:5001


```


正常显示结果如下图所示： ![result](http://yzd.io/images/result-1.jpg)

在 Rancher 的 hosts 界面中应该看到这些运行的容器。 ![voting-in-ranche](http://yzd.io/images/voting-in-rancher-1.jpg)

至此所有关于应用构建和功能测试的过程完成，按 ctl + c 结束 docker-compose up 的运行。




```
^CGracefully stopping... (press Ctrl+C again to force)
Stopping examplevotingapp_worker_1 ... done
Stopping examplevotingapp_result_1 ... done
Stopping examplevotingapp_vote_1 ... done
Stopping examplevotingapp_db_1 ... done
Stopping examplevotingapp_redis_1 ... done

```


