---
title: 为Docker Swarm群集配置Nutanix持久存储
subtitle: 在Nutanix平台上为Docker配置存储
date: 2017-11-02
tags: ["Nutanix","docker"]
bigimg: [{src: "/images/abstract-4.jpg"}]
---

本文介绍如何用Docker卷插件的方式，给Docker Swarm的群集挂载Nutanix存储。[Nutanix Container Volume Plug-in ](https://store.docker.com/plugins/nutanix-dvp-docker-volume-plug-in)简称DVP，可以给容器提供数据持久化的功能。

本文使用ownCloud网盘应用做功能测试。测试的过程如下，安装部署Docker Datacenter，配置好群集，在UCP的界面里调用DVP插件建持久的数据卷，建立ownCloud服务，部署和测试该服务。




## Nutanix DVP (Docker Volume Plug-in)安装和配置

这一部分描述DVP的安装部署过程，需要连接互联网；安装调试完毕之后，作虚拟机的镜像模板使用。这样Docker Swarm的其它节点也都不需要重复这个步骤了。

本文使用的是Docker社区文档稳定版 17.03.1-ce ；本文使用的OS是CentOS 7.3。所Docker安装的版本如下：

```
[root@centos7-temp]# docker version
Client:
 Version:      17.03.1-ce
 API version:  1.27
 Go version:   go1.7.5
 Git commit:   c6d412e
 Built:        Mon Mar 27 17:05:44 2017
 OS/Arch:      linux/amd64

Server:
 Version:      17.03.1-ce
 API version:  1.27 (minimum version 1.12)
 Go version:   go1.7.5
 Git commit:   c6d412e
 Built:        Mon Mar 27 17:05:44 2017
 OS/Arch:      linux/amd64
 Experimental: false
 
[root@centos7-temp]# rpm -qa|grep docker
docker-ce-17.03.1.ce-1.el7.centos.x86_64
docker-ce-selinux-17.03.1.ce-1.el7.centos.noarch

```

本文使用的Docker 安装yum源如下：

```
[root@centos7-temp]# cat /etc/yum.repos.d/docker-ce.repo
[docker-ce-stable]
name=Docker CE Stable - $basearch
baseurl=https://download.docker.com/linux/centos/7/$basearch/stable
enabled=1
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-stable-debuginfo]
name=Docker CE Stable - Debuginfo $basearch
baseurl=https://download.docker.com/linux/centos/7/debug-$basearch/stable
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-stable-source]
name=Docker CE Stable - Sources
baseurl=https://download.docker.com/linux/centos/7/source/stable
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-edge]
name=Docker CE Edge - $basearch
baseurl=https://download.docker.com/linux/centos/7/$basearch/edge
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-edge-debuginfo]
name=Docker CE Edge - Debuginfo $basearch
baseurl=https://download.docker.com/linux/centos/7/debug-$basearch/edge
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-edge-source]
name=Docker CE Edge - Sources
baseurl=https://download.docker.com/linux/centos/7/source/edge
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-test]
name=Docker CE Test - $basearch
baseurl=https://download.docker.com/linux/centos/7/$basearch/test
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-test-debuginfo]
name=Docker CE Test - Debuginfo $basearch
baseurl=https://download.docker.com/linux/centos/7/debug-$basearch/test
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg

[docker-ce-test-source]
name=Docker CE Test - Sources
baseurl=https://download.docker.com/linux/centos/7/source/test
enabled=0
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg
```


本机所使用的所有安装源如下：

```
[root@centos7-temp]# yum repolist
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
repo id                                   repo name                                                         status
base/7/x86_64                             CentOS-7 - Base - mirrors.aliyun.com                               9,363
docker-ce-stable/x86_64                   Docker CE Stable - x86_64                                              4
epel/x86_64                               Extra Packages for Enterprise Linux 7 - x86_64                    11,808
extras/7/x86_64                           CentOS-7 - Extras - mirrors.aliyun.com                               381
updates/7/x86_64                          CentOS-7 - Updates - mirrors.aliyun.com                            1,859
repolist: 23,415
```

安装docker引擎，并启动服务，并校验服务状态。安装过程参考如下：

```
[root@centos7-temp]# yum install -y docker-ce
[root@centos7-temp]# systemctl enable docker
[root@centos7-temp]# systemctl start docker
[root@centos7-temp]# systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2017-06-20 20:30:49 CST; 19min ago
     Docs: https://docs.docker.com
 Main PID: 875 (dockerd)
   CGroup: /system.slice/docker.service
           ├─ 875 /usr/bin/dockerd
           ├─ 942 docker-containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-in...
           ├─2008 docker-containerd-shim 0ca2346b6126de702fb4dda5f807c0a69a402eb643f15c142730277d0eb7bbcb /var/...
           └─0ca2346b6126de702fb4dda5f807c0a69a402eb643f15c142730277d0eb7bbcb
             └─2038 /usr/bin/python /code/main.py --prism-ip 10.68.69.22 --dataservices-ip 10.68.69.23 --prism-...
```

到目前为止，Docker安装配置完成。

下面开始安装DVP，安装和配置过程参考页面。

[https://store.docker.com/plugins/nutanix-dvp-docker-volume-plug-in](https://store.docker.com/plugins/nutanix-dvp-docker-volume-plug-in)

下面是给操作系统安装iscsi initiator服务的参考步骤：


```
yum install -y iscsi-initiator-utils 
systemd-tmpfiles --create
systemctl start iscsid
systemctl enable iscsid
systemctl status iscsid
● iscsid.service - Open-iSCSI
   Loaded: loaded (/usr/lib/systemd/system/iscsid.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2017-06-20 20:30:46 CST; 24min ago
     Docs: man:iscsid(8)
           man:iscsiadm(8)
 Main PID: 888 (iscsid)
   CGroup: /system.slice/iscsid.service
           ├─882 /usr/sbin/iscsid
           └─888 /usr/sbin/iscsid

Jun 20 20:30:46 centos7-temp.zenlab.local systemd[1]: Starting Open-iSCSI...
Jun 20 20:30:46 centos7-temp.zenlab.local iscsid[878]: iSCSI logger with pid=882 started!
Jun 20 20:30:46 centos7-temp.zenlab.local systemd[1]: Failed to read PID from file /var/run/iscsid.pid: Inva...ent
Jun 20 20:30:46 centos7-temp.zenlab.local systemd[1]: Started Open-iSCSI.
Jun 20 20:30:47 centos7-temp.zenlab.local iscsid[882]: iSCSI daemon with pid=888 started!
Hint: Some lines were ellipsized, use -l to show in full.
```

> 解释一下DVP的工作原理是，它是让Docker主机通过iSCSI协议连接Nutanix的存储服务。DVP插件的配置里包含了连接存储服务和存储容器（这个容器是Nutanix的存储术语，非Docker说的容器）的相关信息。这样Docker主机上用该卷插件建立的数据卷都会指向Nutanix后台的存储容器中；数据通过iSCSI协议连接Nutanix存储服务的时候，就可以利用到Nutanix群集提供的负载均衡能力；当数据块写入Nutanix存储池的过程中和之后，就可以利用到到Nutanix存储容器所具备的其它重要特性：数据块2~3副本的高可靠性、冷热数据分成、压缩、去重、纠删码等；而且存储空间对于容器或者Docker Swarm里的服务都是透明和无限容量的。

现在做一些安装DVP的准备工作，询问Nutanix系统管理员下面信息：

* 获得Prism 的IP
* 获得Nutanix群集数据服务的IP，这个IP是群集上的虚拟服务IP
* 获得群集的用户名和密码
* 新建一个测试存储容器，获得容器名

参考下面的DVP安装命令：

```
docker plugin install ntnx/nutanix_volume_plugin PRISM_IP="10.68.69.22" DATASERVICES_IP="10.68.69.23" PRISM_PASSWORD="nutanix/4u" PRISM_USERNAME="admin" DEFAULT_CONTAINER="ddc-sc1" --alias nutanix
```

以上的命令执行结果如下：

```
[root@centos7-temp]# docker plugin install ntnx/nutanix_volume_plugin PRISM_IP="10.68.69.22" DATASERVICES_IP="10.68.69.23" PRISM_PASSWORD="nutanix/4u" PRISM_USERNAME="admin" DEFAULT_CONTAINER="ddc-sc1" --alias nutanix
Plugin "ntnx/nutanix_volume_plugin" is requesting the following privileges:
 - network: [host]
 - mount: [/dev]
 - mount: [/lib/modules]
 - mount: [/etc/iscsi]
 - mount: [/var/lock/iscsi]
 - mount: [/proc]
 - allow-all-devices: [true]
 - capabilities: [CAP_SYS_ADMIN CAP_SYS_PTRACE CAP_IPC_LOCK CAP_IPC_OWNER CAP_NET_ADMIN CAP_MKNOD CAP_SYS_MODULE]
Do you grant the above permissions? [y/N] y （输入y，按回车）
latest: Pulling from ntnx/nutanix_volume_plugin
be892c8cb64d: Download complete
Digest: sha256:5a3730ffae077eb6ddc0c125620283d56852528b686cbe42f2f58696eab82c0d
Status: Downloaded newer image for ntnx/nutanix_volume_plugin:latest
Installed plugin ntnx/nutanix_volume_plugin
```

确认VDP安装结果，这个插件应该是最新版、启动的状态，如下：

```
[root@centos7-temp]# docker plugin ls
ID                  NAME                DESCRIPTION                        ENABLED
f0e38fbc11b3        nutanix:latest      Nutanix volume plugin for docker   true
```

执行下面的测试，确认DVP工作正常。
```
[root@centos7-temp]# docker volume create testvol -d nutanix:latest
testvol
[root@centos7-temp]# docker volume ls
DRIVER              VOLUME NAME
nutanix:latest      testvol
[root@centos7-temp]#
```

回到Nutanix的Prisum界面（主要的群集管理图形化界面）中查看Storage --> table  --> Volume Group，应该能看到这个命令所创建的名为testvol的数据卷。如下图所示：


![](/images/Screen%20Shot%202017-06-20%20at%209.07.13%20PM.png)


在命令行删除这个测试的卷。

```
[root@centos7-temp]# docker volume rm testvol
testvol
[root@centos7-temp]# docker volume ls
DRIVER              VOLUME NAME
[root@centos7-temp]#
```

在回到Prisum界面中查看刚才看到的那个卷应该就消失了。到此为止所有节点的DVP部署配置工作就完毕了，并且确认docker服务和DVP功能都很正常。用 sys-unconfig 命令关机，把这个虚拟机在Prisum里面做一个快照备用，也可以在Nutanix的acli命令行里面把它做成一个基础镜像。


我们已经理解和熟悉了DVP的基本操作，配置和部署，下面开始安装Docker Datacenter；Docker Datacenter的架构图如下所示：
![](/images/14979754711332.jpg)

本文安装的架构是：

1. 一个 UCP manager 节点
2. 一个 DTR 节点
3. 两个 worker node 节点

在Nutanix的Prisum中用刚才制作的那个快照或者镜像模板，克隆/新建4个虚拟机。虚拟机的参考配置如下：

* 2 vCPU
* 4GB RAM
* 50GB Disk

## 安装UCP（Docker Universal Control Plane）节点

在Nutanix的Prisum中从刚才新建的四个虚拟机中选择一个，Power on开机；ssh登录到操作系统内之后，设定主机名和IP地址。

安装配置参考文档：https://docs.docker.com/datacenter/ucp/2.1/guides/admin/install/install-offline/#download-the-offline-package

注意事项，提前下载好安装包，这个tar包里面包含了UCP需要的所有镜像，可以一次性导入到UCP的节点上。

```
wget https://packages.docker.com/caas/ucp_images_2.1.4.tar.gz -O docker-datacenter.tar.gz

docker load < docker-datacenter.tar.gz
```

载入完毕后，可以看到如下镜像。

```
[root@ucp-master ~]# docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
docker/ucp-metrics      2.1.4               e3e24ef156bd        3 weeks ago         92.2 MB
docker/ucp-swarm        2.1.4               d8b51d6801e5        3 weeks ago         21 MB
docker/ucp-hrm          2.1.4               38a19323327d        3 weeks ago         14.8 MB
docker/ucp-etcd         2.1.4               9aa382502e19        3 weeks ago         38.5 MB
docker/ucp-controller   2.1.4               5a852aa3039e        3 weeks ago         28 MB
docker/ucp-dsinfo       2.1.4               66ee9368796a        3 weeks ago         159 MB
docker/ucp              2.1.4               7a28dbfc44e4        3 weeks ago         19.1 MB
docker/ucp              latest              7a28dbfc44e4        3 weeks ago         19.1 MB
docker/ucp-cfssl        2.1.4               acdc1f147711        3 weeks ago         15.1 MB
docker/ucp-compose      2.1.4               25775e989077        3 weeks ago         32.9 MB
docker/ucp-auth-store   2.1.4               f27ad13dee6c        3 weeks ago         58.7 MB
docker/ucp-agent        2.1.4               d716a096c331        3 weeks ago         22.5 MB
docker/ucp-auth         2.1.4               1f4739cd3c08        3 weeks ago         25.1 MB
[root@ucp-master ~]#
```

安装UCP的命令参考如下：

```
docker run --rm -it --name ucp \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/ucp:2.1.4 install \
  --host-address 10.68.69.12 \
  --interactive
```

以上命令中10.68.69.12是UCP主机的ip地址，建议UCP使用固定IP。以上命令完毕后用浏览器访问这个IP。

参考以下文档，完成UCP的安装步骤，其中需要到Docker网站获得30天的试用版许可证文件。

https://docs.docker.com/datacenter/ucp/2.1/guides/admin/install/

能够正常登陆访问UCP之后，在首页下方点击 【Add Node】按钮，获得加其它节点到群集里的命令，参考命令如下：

```
docker swarm join \
  --token SWMTKN-1-1310ah7gzj9e7bk6a5yobo2qyiwf93ybrd29flkved1zqydd6i-7pir0884sag5pjofwzjq5o1um \
  10.68.69.12:2377
```
  
把以上命令记录在写字板中备用。

## 加3个节点到群集里  

把剩下的三个虚拟机开机，进入操作系统后设定主机名和IP。其中的一个安装DTR（Docker镜像仓库）的节点建议使用固定IP。

在每个操作系统里面用docker命令确认DVP是否正常。

* docker plugin ls
* docker volume ls
* systemctl status iscsid

下面就可以把上一步所记录命令在命令行里面执行以下，完毕之后回到UCP的界面中查看是否它们已经添加成功。如下图所示：
![Screen Shot 2017-06-20 at 9.49.32 P](/images//Screen%20Shot%202017-06-20%20at%209.49.32%20PM.png)




## 安装DTR-Docker镜像仓库

在UCP首页的下方，找到并点击 【Install DTR】的按钮，取得安装命令（记得从清单中选择固定IP地址的DTR主机）；在登录DTR主机的控制台里面输入这个命令，命令如下：

```
docker run -it --rm \
  docker/dtr:2.2.5 install \
  --ucp-node 10.68.69.12 \
  --ucp-insecure-tls
```

DTR节点没有离线安装的整合包，它需要联网下载很多相关镜像，如果网络速度不是很快的话，下载和安装的过程需要至少半个小时，过程中还需要输入UCP的管理员，用户名和密码。

参考文档如：
https://docs.docker.com/datacenter/dtr/2.2/guides/admin/install/#step-3-install-dtr

DTR正常工作了以后，登录建立一个名为owncloud的镜像库，点击【New Rrepository】输入owncloud。
在一个节点上下载owncloud镜像，添加新的tag，上传到这个镜像到镜像库里备用。参考命令如下：

```
docker login dtr.zenlab.local
docker pull owncloud
docker tag owncloud:latest dtr.zenlab.local/admin/owncloud:latest
docker push dtr.zenlab.local/admin/owncloud:latest
```
![Screen Shot 2017-06-20 at 10.10.13 P](/images/Screen%20Shot%202017-06-20%20at%2010.10.13%20PM.png)



注意：如果你的环境中没有DNS，就把dtr.zenlab.local换成DTR的IP地址。

以上这个步骤主要是方便以后，反复使用和测试这个镜像的可能性，如果所有的节点都有高速的互联网链接，可以忽略以上步骤。

## Docker Swarm群集中使用DVP
这里使用UCP的图形化界面，在一个所有节点都配置和部署了VDP的群集上，给群集挂载外部Nutanix的数据卷。

登录UCP主页，点击Resource，点击Volumes，点击 【Create Volume】，输入相关参数，如下图所示。图中的sizeMb=500000这个参数是制定VolumeGroup的大小，不设定这个参数的话，默认是10GB。
![Screen Shot 2017-06-21 at 12.22.24 A](/images/Screen%20Shot%202017-06-21%20at%2012.22.24%20AM.png)

在到Nutanix的Prism里面查看这个Volume Group是否存在。应该如下图所示：

![Screen Shot 2017-06-21 at 12.23.32 A](/images/Screen%20Shot%202017-06-21%20at%2012.23.32%20AM.png)


## 部署OwnCloud网盘服务

登录UCP主页，点击 Service ， 点击 【Create a Service】按钮；开始建立这个服务。输入服务名，镜像名；点击 【Next】按钮。

![Screen Shot 2017-06-20 at 10.49.10 P](/images/Screen%20Shot%202017-06-20%20at%2010.49.10%20PM.png)


点击 【Next】按钮。进入 Resource页面，这里需要配置端口和数据卷。
![Screen Shot 2017-06-20 at 10.49.35 P](/images/Screen%20Shot%202017-06-20%20at%2010.49.35%20PM.png)

![Screen Shot 2017-06-20 at 10.49.58 P](/images/Screen%20Shot%202017-06-20%20at%2010.49.58%20PM.png)



最后点击【Deploy Now】按钮。 部署完毕之后，显示这个服务的状态为正常。
![Screen Shot 2017-06-21 at 12.25.51 A](/images/Screen%20Shot%202017-06-21%20at%2012.25.51%20AM.png)

![Screen Shot 2017-06-20 at 10.52.28 P](/images/Screen%20Shot%202017-06-20%20at%2010.52.28%20PM.png)

点击这个服务，到这个页面的最下方，找到右下角的发布端口的链接，点击后，就可以看到ownCloud的初始化配置页面了。
![Screen Shot 2017-06-20 at 10.53.24 P](/images/Screen%20Shot%202017-06-20%20at%2010.53.24%20PM.png)



输入管理员的用户名和密码，进入之后，上传一些图片，测试一下功能是否正常。

![Screen Shot 2017-06-20 at 10.54.06 P](/images/Screen%20Shot%202017-06-20%20at%2010.54.06%20PM.png)


尝试一些Docker Datacenter的高级功能，如服务的高可用性；同时Nutanix的DVP在底层保障了数据的持久性和完全性。测试步骤如下：

1. 找到运行owncloud的容器，删除这个容器
2. 在服务页面查看owncloud服务的状态变化
3. 等ownCloud的状态恢复正常之后
4. 再次登录ownCloud页面
5. 查看和确认刚才上传的文件是否还在

## 总结
Nutanix是一种融合和了计算、存储和虚拟化（内置KVM）的超融合平台。Nutanix DVP (Docker Volume Plug-in)可以让平台里的容器用上持久化存储服务。DVP不仅可以给单独虚拟机里的容器提供持久卷服务，还能给类似于Docker Swarm的其它容器编排平台提供持久化数据服务功能。我后续的文章还会分享路测试Kubernetes等其它平台。 








