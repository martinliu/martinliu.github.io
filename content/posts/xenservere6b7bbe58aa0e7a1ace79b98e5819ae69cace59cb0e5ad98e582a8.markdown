---
author: liuadmin
categories:
- XenServer
comments: true
date: 2013-11-25T10:39:00Z
subtitle: 当您的XenServer测试机需要增加硬盘的时候，你需要通过简单的几条指令把新硬盘添加为本地存储。下面的实例情况是：测试机有两块硬盘、OCZ  SSD硬盘一块、SATA
  不通硬盘一块、还有一个U盘插在系统上、SATA的硬盘是我需要加载的新硬盘
slug: xenserver%e6%b7%bb%e5%8a%a0%e7%a1%ac%e7%9b%98%e5%81%9a%e6%9c%ac%e5%9c%b0%e5%ad%98%e5%82%a8
tags:
- featured
- hd
- local storage
- xenserver
title: XenServer 添加硬盘做本地存储
url: /2013/11/25/xenservere6b7bbe58aa0e7a1ace79b98e5819ae69cace59cb0e5ad98e582a8/
wordpress_id: 52591
---

当您的 XenServer 测试机需要增加硬盘的时候，你需要通过简单的几条指令把新硬盘添加为本地存储。

下面的实例情况是：



	
  * 测试机有两块硬盘

	
    * OCZ  SSD硬盘一块

	
    * SATA 不通硬盘一块

	
    * 还有一个U盘插在系统上




	
  * SATA的硬盘是我需要加载的新硬盘

	
  * 这个新的硬盘希望被处理成XenServer本地的SR


添加过程中主要需要使用这样几条指令：

	
  1. 查看当前系统上的检查出来并且挂载中的分区： cat /proc/partitions

	
  2. 详细查看这些存储和设备对应的情况： ls -l /dev/disk/by-id/

	
  3. 创建新的本地SR: xe sr-create content-type=user device-config:device=/dev/disk/by-id/scsi-SATA_ST9320325ASG_5VD7G964 host-uuid=3850317b-d23a-4ed0-87f9-2b27854319e5 name-label="SATA320" shared=false type=lvm


[bash]
[root@XS62 ~]# cat /proc/partitions
major minor #blocks name

7 0 52378 loop0
8 0 250059096 sda
8 1 4193297 sda1
8 2 4193297 sda2
8 3 241669447 sda3
8 16 312571224 sdb
8 17 204800 sdb1
8 18 312235312 sdb2
8 32 4137984 sdc
8 36 4137856 sdc4
252 0 241655808 dm-0

[root@XS62 ~]# ls /dev/disk/by-id/
scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2 scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part3 scsi-SATA_ST9320325ASG_5VD7G964-part2
scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part1 scsi-SATA_ST9320325ASG_5VD7G964 usb-Generic_Flash_Disk_4266F915
scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part2 scsi-SATA_ST9320325ASG_5VD7G964-part1 usb-Generic_Flash_Disk_4266F915-part4

[root@XS62 ~]# ll /dev/disk/by-id/
total 0
lrwxrwxrwx 1 root root 9 Nov 22 19:52 scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2 -> ../../sda
lrwxrwxrwx 1 root root 10 Nov 22 19:52 scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part1 -> ../../sda1
lrwxrwxrwx 1 root root 10 Nov 22 19:52 scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part2 -> ../../sda2
lrwxrwxrwx 1 root root 10 Nov 22 19:52 scsi-SATA_OCZ-AGILITY4_OCZ-DY4J9LY3615W5MF2-part3 -> ../../sda3
lrwxrwxrwx 1 root root 9 Nov 22 19:52 scsi-SATA_ST9320325ASG_5VD7G964 -> ../../sdb
lrwxrwxrwx 1 root root 10 Nov 22 19:52 scsi-SATA_ST9320325ASG_5VD7G964-part1 -> ../../sdb1
lrwxrwxrwx 1 root root 10 Nov 22 19:52 scsi-SATA_ST9320325ASG_5VD7G964-part2 -> ../../sdb2
lrwxrwxrwx 1 root root 9 Nov 22 19:52 usb-Generic_Flash_Disk_4266F915 -> ../../sdc
lrwxrwxrwx 1 root root 10 Nov 22 19:52 usb-Generic_Flash_Disk_4266F915-part4 -> ../../sdc4

[root@XS62 ~]# xe sr-create content-type=user device-config:device=/dev/disk/by-id/scsi-SATA_ST9320325ASG_5VD7G964 host-uuid=3850317b-d23a-4ed0-87f9-2b27854319e5 name-label="SATA320" shared=false type=lvm
cf0893c3-9398-d802-0706-66a8699c3a59
[/bash]

从上面的命令可以看到，最后一条命令完成后，系统返回了新SR的ID;然后在登录XenCenter就可以看到这个存储了，虚拟现在就可以使用这个存储了。
