---
date: 2017-01-10T00:00:00Z
subtitle: 本文描述了AHV虚拟化的虚拟机模板的制作过程。
tags:
- Nutanix
title: Nutanix AHV 虚拟机模板制作
---

本文描述了AHV虚拟化的虚拟机模板的制作过程。首先使用ssh登录cvm，进入acropolis命令行。

## 找出模板对应的虚拟机

使用 vm.disk_get 命令，按多次tab，显示虚拟机清单，复制模板机名称

~~~
<acropolis> vm.disk_get vm-fedora25
ide.0 {
  addr {
    bus: "ide"
    index: 0
  }
  cdrom: True
  empty: True
}
scsi.0 {
  addr {
    bus: "scsi"
    index: 0
  }
  container_id: 4427
  container_uuid: "9279ba2c-8e8d-4aea-b00f-410df5a18a23"
  vmdisk_size: 10737418240
  vmdisk_uuid: "7476458e-7917-4df8-b830-a0df5a95dae9"
}
~~~

## 创建模板镜像

使用从虚拟机磁盘克隆出镜像的命令。

~~~

<acropolis> image.create fedora25-Template clone_from_vmdisk=7476458e-7917-4df8-b830-a0df5a95dae9 image_type=kDiskImage annotation='Fedora 25 Server Template'
fedora25-Template: complete

~~~

## 模板测试

登录Prism界面，点击镜像服务，确认清单中刚才创建的虚拟机模板镜像；进入vm页面，创建虚拟机，使用 fedora25-Template 镜像做磁盘
