---
date: 2017-01-29T00:00:00Z
subtitle: 本文使用Nutanix CE版本的群集来完成默认的KVM虚拟化下，Windows 10虚拟机的安装
tags:
- Nutanix
title: Nutanix AHV（KVM）Windows虚拟机安装全攻略
---

# Windows 虚拟机安装
Nutanix的AHV虚拟机是基于KVM的。本文件假设您使用和安装的是Nutanix社区版本的群集。在上面安装Windows虚拟机的步骤如下：

1. 下载操作系统安装光盘
2. 上传操作系统安装光盘到Nutanix群集 （安装Windows虚拟机需要 Fedora virtio 驱动）
3. 新建和配置虚拟机
4. 安装OS
5. 安装Nutanix Guest Tools （NGT）

下面用安装Windows 10举例，说明详细的安装步骤。

## 第一步：下载操作系统 ISO
如果你需要下载 Ubuntu Desktop [点这里](https://www.ubuntu.com/desktop)。

从微软的TechNet Evaluation Center下载 [Microsoft ISO](https://www.microsoft.com/en-us/evalcenter/) 注意，评估的服务器版只能使用180天，桌面版能使用90天。

## 第二步：上传ISO文件到Nutanix群集
Nutanix群集上提供了镜像服务，可以存储几种格式的镜像：ISO格式的操作系统安装镜像，虚拟机的磁盘(如KVM格式等)。这些镜像文件可以被虚拟机通过挂载CD-ROM设备使用，或者直接克隆出虚拟机的磁盘。操作步骤如下。

点击右上角的齿轮图标，选择image configuration
![](/images/14857476024029.jpg)

点击 upload image按钮

![](/images/14857476555578.jpg)

界面字段解释：

* Name: 镜像文件的名字（用ISO来与磁盘镜像区分一下）
* Image Type: 选择 ISO
* Container: 选择用来存储ISO文件的容器
* Image Source: 选择上传文件作为镜像来源
* Save: 点击Save按钮可以看到上传的进度条。

![](/images/14857477053373.jpg)

在上传成功之后，镜像清单中显示刚才的镜像为 Active 状态。

![](/images/14857479049693.jpg)


由于Nutanix的hypervisor是基于Linux KVM技术，它需要附加的Windows驱动，需要下载 Fedora Windows virtio 驱动。 下载地址如下：

[https://fedoraproject.org/wiki/Windows_Virtio_Drivers](https://fedoraproject.org/wiki/Windows_Virtio_Drivers)

点击第三条 Direct download

![](/images/14857480805485.jpg)


点击 “Stable virtio-win iso” 下载最新的驱动 ISO 文件。

![](/images/14857481167991.jpg)

下载到的文件名如：virtio-win-0.1.126.iso；重复上述Windows IOS文件上传的步骤，把这个文件上传到镜像服务中。

Fedora 的开源版 VirtIO驱动和Nutanix的版本稍微有些不同。Nutanix的 VirtioIO驱动是经过数字签名的，能从Nutanix客户门户下载。由于Nutanix CE社区版是提供给所有人做体验测试的，因此这里使用的是开源版本的VirtioIO驱动，而不是Nutanix的官方版本的驱动。

##第三步：创建和配置虚拟机

我们已经准备好了Windows 10 ISO文件和 Fedora VirtIO驱动IOS文件，现在可以安装虚拟机了。步骤如下：

点击 Home--VM


 ![](/images/14857485236059.jpg)


点击右侧的 Create VM 按钮。

![](/images/14857485706681.jpg)


在下面的页面中输入虚拟机的配置。

![](/images/14857486182975.jpg)
![](/images/14857486277811.jpg)

主要配置介绍如下：
![](/images/14857486605678.jpg)

* Name: Win10Desktop  虚拟机的名称
* vCPUs: 2  两颗虚拟CPU
* Number of Cores per vCPU: 1
* Memory: 2GB (只是做测试的话，2GB可以了)

下面添加用于虚拟机挂载Windows 10 安装盘的 CDROM设备。删除默认的CDROM设备。
![](/images/14857489095951.jpg)

由于偶尔安装Windows 10的时候默认的CDROM驱动器中Fedora Virtio驱动会显示不出来，因此删除默认的CDROM设备。

添加vm系统安装的磁盘。点击添加磁盘，输入如下实例信息，得到一块40GB的SCSI磁盘用来安装Window 10操作系统。

![](/images/14857490738212.jpg)


添加一个新的CDROM驱动盘，用来挂载 Windows 10 的ISO镜像文件，如下图所示。

* Type: CDROM 类型
* Operation: Clone from Image Service
* Bus Type: IDE 类型的应该是默认类型
* Image: 选择刚才上传的 Win10ISO

![](/images/14857492195172.jpg)

添加一个新的CDROM设备，用来挂载 Fedora Virtio驱动IOS文件，如下图所示。

* Type: CDROM 类型
* Operation: Clone from Image Service
* Bus Type: IDE
* Image: 选择 FedoraVirtISO

配置完成之后的磁盘配置布局如下。

![](/images/14857493954380.jpg)


现在来添加网卡，点击下面的按钮。

![](/images/14857494220235.jpg)


使用默认的ID为0的网络，如下图所示。（此VLAN时之前建立好的）

![](/images/14857494722709.jpg)

现在所有配置都已经完成，点击 Save 保存按钮。


 ![](/images/14857495029831.jpg)

页面的状态栏会出现一个绿色的执行的提示，表示后天虚拟机正在创建中。

![](/images/14857495959115.jpg)



## 第四步：运行并安装虚拟机

做如下操作来开启并运行虚拟机，进入Windows操作系统的安装过程。

1. 点击到 VM 视图
2. 点击 Table
3. 点击  Win10Desktop VM 刚才创建的虚拟机
4. 点击  Power on
5. 当 VM 启动了, 点击  Launch Console 进入控制台页面。

![](/images/14857496408859.jpg)

在Windows安装的界面，选择Custom ：高级安装选项。

![](/images/14857499695677.jpg)

由于我们使用的 AHV 是KVM虚拟化，所以需要加载Virtio驱动。点击 Load Driver 按钮。

![](/images/14857502423986.jpg)

点击 Browse 浏览。

![](/images/14857502795932.jpg)

点击并浏览驱动器 E： （这是之前我们挂载 Fedora Virtio ISO文件的CDROM）

![](/images/14857503335113.jpg)

浏览驱动盘到目录 vioscsi

![](/images/14857504369501.jpg)

选择 w10 目录

![](/images/14857504579467.jpg)


选择 amd64 目录，点击 ok

![](/images/14857504816806.jpg)


选择所显示出来的 Red Hat VirtIO SCSI 驱动，点击 Next

![](/images/14857505411190.jpg)

这样刚才创建的 40GB的磁盘就可以看到了，选择 Next

![](/images/14857506028586.jpg)

点击了 Next 按钮之后， Windows 10 开始安装，这个过程大约是3~10分钟不等。最后就到了Windows的账户创建的环节。虽然现在Windows已经安装完成了，还需要进入Windows的设备管理器中查看一下，设备的状态。

* 右击Windows的图标
* 选择 Device Manager

![](/images/14858815713785.jpg)



在设备官开启中，我们需要更新一下网卡设备的驱动。

![](/images/14858816384447.jpg)

右击网卡设备，选择 Update Driver Software...

![](/images/14858816757065.jpg)

点击 Browse，选择当前的 virtio-win-0.11 ，也就是 Fedora VirtIO 驱动的光驱设备，点击 Next

![](/images/14858817470182.jpg)


选中了合适的目录后，网卡设备的驱动安装正常了显示如下：

![](/images/14858818602337.jpg)

到目前为止，我们的Windows 10 虚拟机安装完毕了。

## 第五步： 安装Nutanix Guest Tools （NGT）

Nutanix Guest Tools 可以实现自服务恢复和应用一致性快照功能，它需要Microsoft Volume Shadow Copy Services (VSS)服务的配合。下面来安装它。

1. 进入虚拟机的清单视图
2. 点击 Table
3. 点击选中刚才安装的Windows 10 虚拟机
4. 点击 Enable NGT （这个操作需要有一个空闲的CDROM设备，可以点击虚拟机的编辑，把之前的两个光驱中挂载的ISO盘退出一个）
5. 在后续的窗口中点击 Yes

![](/images/14858821642374.jpg)


在网页上成功启用了NGT之后，进入Windows 10桌面的控制台页面。打开Windows的资源管理器，双击带有Nutanix图标的CDROM设备，进入该设备安装NGT软件。

![](/images/14858823586478.jpg)

点击 Install 按钮。

![](/images/14858823893756.jpg)

跟随安装向导完成NGT的安装。安装完成之后，在Windows10中关机，在网页上编辑这个虚拟机的配置，删除多余的CDROM设备，之后在开机。至此Windows10虚拟机的安装过程全部完毕。

扩展阅读：[Nutanix AHV 虚拟机模板制作](http://martinliu.cn/2017/01/10/clone-ahv-vm-template/)
