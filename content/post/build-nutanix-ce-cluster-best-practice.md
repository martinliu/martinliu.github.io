+++
date = 2022-02-20T23:05:40+08:00
title = "HCI | 超融合平台线上训练营第二期"
description = "进阶学习vSphere虚拟化与Nutanix社区版超融合平台的集成，体验资源超分、精简制备和混合分层存储等极致体验。"
author = "Martin Liu"
categories = ["DevOps"]
tags = ["超融合", "HCI", "nutanix", "vsphere"]
image = "img/cos/2022-02-21-hci-nutanix.jpeg"
slug = "hci-nutanix-ce-training-camp"
+++

本文总结了我从单机的 Home Lab 环境，发展到三节点 Nutanix 超融合混合盘集群的经验和教训。

<!--more-->

## 为什么需要超融合集群

我的 Home lab 的进化史

- 长期保持一些特定功能的虚拟机
- 在本地保持丰富的虚拟机模版和快照
- 将照片和视频家庭资料放到媒体服务器中【Plex】
- 探索IoT智能家居，家庭安防等项目
- 充分利用虚拟话带来的福利，计算和存储资源超量分配
- 利用高级分布式软件定义存储都高级功能，空间的节省：压缩，去重，纠删码等；性能提升：虚拟机享受全闪存本地磁盘+精简制备；同时享用性能和空间：通过 SSD+HDD的混合容量存储池实现鱼和熊掌兼得。
- 本地实验室网速提升到万兆以太网，尝试最新的数据中心DPU（智能网卡）、边缘计算和IoT趣味设备。
- 排除家用 NAS主机（群晖）、ALL in One 主机、云和容器等选项

其他可能选项

- VMware 的 ESXi 平台 + VSAN ；熟悉 VMware 技术栈； 或被人带着追捧者多用。
- Citrix 的 XenServer + 家用集中存储；少见家用的人。
- 其他的开源虚拟化选项 Proxmox ，单机版家用服务区比较常见。

## 各种系统使用体验

不论是单机的服务器/NAS，总之使用场景的需求是越用越多的，HomeLab 用的时间越久，想要做的事情就会越多。

### Intel NUC

这是一台 Nutanix 售前工程师标配的测试机。我用了好几年，非常皮实耐用。

**硬件平台**：

- 集成主板，i7 8 Core + 集成 Intel 显卡
- 32GB 内存，DDR4 - 2133 MHz
- SSD 500GB x 2 ， M.2 nvme 接口

**使用体验**：

1. CPU和内存资源都比较有限
2. 散热不理想，风扇噪音越用越大
3. 无法扩展
4. 不适合长期开机
5. 安装 Nutanix CE （AHV） 超级轻松，从不会遇到失败，hypervisor 安装在U盘上。安装后，调低 cvm 的资源，剩余可用资源，所剩无几。

### Lenovo P720

公有云虽然是完全可用的，但是无法满足我企业数据中心相关技术的本地体验。还是需要搞一台配置高的，资源更多的机器，因此入手了第二台测试机，为了放置空间和电费都更容易接受，折中选择了二手的品牌机工作站。

硬件平台：

- Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz 14 core x 2
- 64 GB ，还有很多空余插槽
- SSD ：120 GB + 256GB ，一共有四个 3.5 寸的标准磁盘位。
- 安装 VMWare ESXi + vCenter
  - 超分资源+精简存储制备
  - 广泛的开源虚拟机模版下载
  - 大量开源和私有企业技术支持

经过一年多的扩容，截止到现在的配置如下：

- 56 logical core： 2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz -14 core 【保持】
- 128 GB DDR4 2011Mhz 【感谢上海网友】
- HDD：西部数据WD 4Tb 5400rpm x 2 【增加了两块 HDD】
- SSD：三星750 Evo 120GB，三星870 Evo 250 GB，三星870 Evo 1TB 【新增一块 SSD】
- NIC：Boardcom BCM57412 NetXtreme-E 10Gb SPF+双口 【感谢panpan】

使用体验：

1. 存储空间不足，虚拟机越来越多，需要不断买新磁盘扩容
2. CPU&内存有限，无法做一些性能基准测试
3. 想扩展为单机版 VSAN ，或者 VSAN 群集，但是它无法支持SSD+HDD的混合容量磁盘组
3. 只有两张千兆网卡（主板集成），无法实现集群情况下高速的网络数据I/O
3. 虚拟机开多了，导致CPU过热，机器会自动关机后，机器暂时无法启动，不得不替换了更好的散热器

单机工作站的 HomeLab 模式无法实现，我对更多集群型软件的部署使用场景，包括：

- Elasticsearch 冷热温多层架构 + ELK 全家桶的长期数据本地保留
- 高可用 K8S 集群搭建和长期持有
*更多 DevOps 开源工具链的搭建，新版本更新，长期随时可用
- 还有其它，不赘述。

## 建议平台选型

为了实现三节点的超融合群集，双十一出手购买了一些产品。

### 国产主板套装 x 2

国产套版的性价比和评价其实都还是ok的，满心怀疑的开始测试起来。

- 华南金牌 x99-AD4   - 单路
  - 12 CPUs x Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz
  - 64 GB - DDR4 - 2400Mhz

- 磁盘接口：
  - nvme接口：1 x M.2 - AHV 可用，ESXi不可用
  - NGFF接口:  1 x M.2 - 同上
  - sSATA x 2：空闲
  - SATA x 6:
    - SSD1: KINGSTON 60GB x 2
    - SSD2: Samsung SSD 860  500GB + Samsung  MZ7TE 256GB
    - HDD3/4: 西部数据WD 4Tb 5400rpm x 4

- 主板集成RTL8111/8168/8411 千兆网卡，ESXi 7/6 都不能直接兼容
- 显卡：无集成显卡，ATI Radeon HD 2GB x 2 - 买错了，最好是集成显卡。
- 万兆网卡： Boardcom BCM57412 NetXtreme-E 10Gb SPF+双口 【感谢panpan】 x 2
- 千兆网卡：
  - Intel 82576 千兆双口 x 1 （ESX i 6/7 兼容）
  - Intel I340-T2 千兆双口 x 1 （ESX i 7 不兼容）

- 机箱：开放式亚克力透明双层机箱 x 2

使用经验：

1. BIOS 中的Boot模式一定要设置为Legacy模式
2. 忽略主板集成网卡，除非你非常擅长将驱动注入ESXi 的iso文件，安装前兆或者万兆网卡
4. Nutanix CE安装的时候需要网卡驱动正常，ESXi 虚拟化必须能从本地web服务器下载iso安装文件
5. AHV虚拟化安装很正常，连nvme接口的M.2磁盘都可以正常使用
6. ESXi虚拟化安装的结果是失败的，但是手工可以拯救CVM，步骤可以忍受。

### 超微豪华高仿Nutanix

新购了一块超微主板，做下对比测试，缓解一下华南主板坑多的低落心情。

- 单路：SuperMicro X10SRL-F
- CPU：E5-2690 v3 @2.60 GHz，12 core
- SATA3: x 10
  - SSD 1/2
  - HDD x2
- 主板集成双千兆网卡 （ESXi 6/7 兼容）

用这块主板 + 以上华南金牌的全套磁盘+CPU+内存+万兆网卡，安装Nutanix CE，ESXi 6/7都可以顺利安装，连CVM都能够自动创建成功，不需要手工拯救失败的CVM，这个平台安装部署Nutanix CE 应该是毫无压力感。

超微主板是Nutanix原厂超融合硬件平台的供应商，这任选了一块测试版的兼容性就确实没话说。不用再测，不用在多了，关键是把上面的国产廉价平台能用起来。

### 方案汇总

| 类型        | 主板 | 内存 | SSD | HDD | 网络 | 节点 | 价格 |
| ----------- | ---- | ---- | --- | --- | ----------- | ----------- | ----------- |
| 最小可平台 | Intel NUC |32GB|500GB x 2|USB/hypervisor| 1G1/2 | 1 | 7+千左右 |
| 工作站平台 | Lenovo P710 |128GB|1/2/3+|1/2/3/4/5+| 1Gx2/10Gx2 | 1 | 8+千左右 |
| 国产套版 | 华南x99-AD4 |64GB|2|1/2/3/4| 1Gx2+10Gx2 | 1/3/4 | 7+千左右/2套 |
| 超微平台 | SuperMicro X10SRL-F |/|/|/| / | 1/3/4 | 随意搭配，参考市价 |
| 旧服务器 | Dell/Lenvov/HP/浪潮 |/|2+直通|2+直通| 1Gx2+10Gx2 | 1/3/4 | 参考市价 |

### 其他组件的选择

下面是对于自选平台的DYI的建议：

- 机箱：根据主板的选择，开放式主板方便使用水冷系统，热量容易散发，可以借助环境的空气散热，选择封闭机箱则需要注意CPU散热器的选择，确保CPU工作温度正常。
- 电源：CPU和显卡电耗需要提前计算，确保电源供电攻略足够。
- 显卡：主板尽量带集成显卡，保持系统最简化可用，后续如果需要GPU了，可以在加显卡，确保主板有两个PCIx16的插槽。
- 网卡：尽量选择ESXi7可以识别免驱动的，7这个版本兼容的网卡类型比6少很多，安装过程中需要IP地址，免得给自己找麻烦，我的一块千兆网卡不能被7正常驱动，因此ESXi的版本无奈降到6.7u3。
- PCI插槽：建议16x至少2个，用于显卡和万兆网卡，其它速率的若干，用于兼容其它可能的网卡或者设备。

## 集群搭建流程

![test machine](img/cos/2022-02-21-WechatIMG1773.jpeg)

### 准备工作

注册Nutanix社区帐号，<https://next.nutanix.com/，必须用公司邮箱注册，才能下载最新的Nutanix> CE安装镜像，和其它相关组件。在首次登陆Nutanix CE群集的时候，也需要输入这个帐号和密码验证。

准备安装镜像：

1. Windows 10 + Ruft
2. 下载 Nutanix-2020-9016.tar
3. Fedora 35 Live CD
4. 16 GB U 盘 x2

准备网络环境

1. 千兆 + 万兆 （DAC 铜缆）
2. DHCP + DNS + Internet 网络
3. Web 服务器 + esxi702a.iso 「不安装 vsphere 虚拟化的不需要 web 服务器」

### 安装流程

1. Fedora Live CD 启动，磁盘工具删除分区
2. 插好网线
3. Nutanix 安装盘启动，观察网卡 IP 地址获取
4. 设置 Hypervisor 类型、磁盘布局、集群信息等，建议不要勾选创建点节点集群的选项，后期手工创建更可控。

![setup](img/cos/2022-02-21-WechatIMG1774.jpeg)
5. 同意软件许可
6. 等待 Hypervisor （ahv一般较快，或者vsphere）成功安装

![hypervisor 安装过程中](img/cos/2022-02-21-WechatIMG1775.jpeg)

![hypervisor 安装完毕](img/cos/2022-02-21-WechatIMG1776.jpeg)

5. 安装后重启服务器，首次 host 启动，观察 cvm 启动过程和结果，等待 CVM 就绪，确认 CVM 上硬盘的挂载情况
6. 登录后确保集群处于未配置状态
7. 重复以上步骤，安装其他 2 ～ 3 个节点 【CE 最多支持4个节点】
8. 检查和确认集群的状态，每个节点都输出，集群未配置，准备工作就绪。
9. 在其中一个 cvm 上，运行创建 Nutanix 集群的命令， cluster create
10. 首次登陆集群，完成初始化配置
11. 配置并确认网络配置，在存储迟管理的地方，创建过载到所有vsphere 主机的共享 NFS 统一存储空间。存储资源就绪。
12. 安装部署 vcenter，在 Prism 中注册 vcenter
13. 安装虚拟机模版
14. 创建虚拟机测试
15. 运行基本的性能验收测试
16. 正式投产
17. 可选：安装 PC、Fileserver、CALM、K8s

### 问题解决

- 【Hypervisor】安装过程中 screen is terminating

![terminal screen](img/cos/2022-02-21-WechatIMG1777.jpeg)

- 【vSphere虚拟化】虚拟化安装成功，但是重启后 cvm 创建失败

![failed-install](img/cos/2022-02-21-WechatIMG1778.jpeg)

![CVM failed](img/cos/2022-02-21-2021-11-27_22-00-44.png)

- 【vSphere虚拟化】cvm 创建成功且运行正常，但是不能正常挂载 HDD

![CVM lost one hdd](img/cos/2022-02-21-2022-02-21_19-17-50.png)
![CVM lost one HDD](img/cos/2022-02-21-2022-02-21_19-16-35.png)

### ESXi 安装后 CVM 创建失败/HDD挂载问题

由于安装程序无法正常初始化所有磁盘，直通的HDD没有正常加载，初始化脚本有小bug导致。手工挂在直通HDD，修复有bug的python代码，重新初始化创建 cvm，确保 CVM 虚拟机最后能正常运行。

处理方法：

1. 网页访问 ESXi 的 ip 地址 ，使用默认的用户名【root】和密码【nutanix/4u】登录，查看确认如下：
   1. 存储-设备下面是否所有磁盘都可见
   2. 网络：所有uplink，网卡，两个虚拟交换机，五个port group
2. SSH 登陆 ESXi host ，查看错误日志的内容：`/bootbank/Nutanix/firstboot/esx_first_boot_launcher.log`；查看是否是如下的常见错误：

   ```sh
   FATAL Fatal exception encountered:
   Traceback (most recent call last):
     File "/bootbank/Nutanix/firstboot/esx_first_boot.py", line 2516, in <module>
       main()
     File "/bootbank/Nutanix/firstboot/esx_first_boot.py", line 2361, in main
       create_svm_vmx_and_attach_rdm_disks_ce()
     File "/bootbank/Nutanix/firstboot/esx_first_boot.py", line 1478, in create_svm_vmx_and_attach_rdm_disks_ce
       dev_paths = get_disk_locations_ce()
     File "/bootbank/Nutanix/firstboot/esx_first_boot.py", line 1019, in get_disk_locations_ce
       device_identifiers.remove(disk[:-3])
   ValueError: list.remove(x): x not in list 
   ```

3. 使用这篇文章[https://next.nutanix.com/discussion-forum-14/esxi-failed-install-on-hpe-dl380-gen9-ce-2020-09-16-38898](https://next.nutanix.com/discussion-forum-14/esxi-failed-install-on-hpe-dl380-gen9-ce-2020-09-16-38898)中的解决方案，查看这个论坛帖子需要注册论坛的账号。

4. 使用上文的方案，运行修改后的 esx_first_boot.py 程序。等待程序执行完毕，在ESXi web client中观察CVM的创建过程。

5. CVM 创建成功运行起来之后，你会发现它可能只挂载了SSD，下面需要手工加载加载系统中的HDD。

   1. ssh 登陆 ESXi host
   2. 用命令 `ls /vmfs/devices/disks/` 查看系统上的所有磁盘设备，记录未挂载上的HDD的设备路径，例如：`/vmfs/devices/disks/t10.ATA_____WDC_WD40EFRX2D68N32N0_________________________WD2DWCC7K0ZN6E93`
   3. 进入 CVM 虚拟机的配置文件目录 【如：`/vmfs/volumes/NTNX-local-ds-4abcf92c-A/`】，创建所有HDD的直通磁盘，参考命令：`vmkfstools -z /vmfs/devices/disks/t10.ATA_____WDC_WD40EFRX2D68N32N0_________________________WD`
      `2DWCC7K0ZN6E93  ./wd4t-1.vmdk`
   4. 在ESXi web client中，关机（PowerOff） CVM，修改配置
   1. 将上一步创建的直通HDD添加进来
   2. 修改虚拟机选项的操作系统，改为CentOS7
   5. 查看CVM虚拟机所有磁盘，确保所有SSD和HDD都已经加载，先不要修改其它任何配置，开机，观察虚拟机是否可以正常启动。

6. ssh登陆CVM虚拟机的操作系统，使用默认用户名【nutanix】和密码【nutanix/4u】。用ping其它集群节点的（host和cvm）ip地址，确保网关和DNS服务器都可达。

CVM 正常运行后，才可以作为空白节点加入群集，或者用于创建新群集。

## 经验教训

1. 在 Nutanix 官方用户论坛的CE板块搜索问题或提问，你不是孤独的。
2. 散热器买专用的，通用的套具安装费劲，适配的并会很好
3. 磁盘至少使用 Fedora live cd 的磁盘工具查看状态，避免坏盘。
4. cvm 创建失败应该是可以修复的
5. 安装过程需要联网
6. 集成显卡更好，
7. 相同的错误复发时要记得赶紧收工，明天再搞

## 其他可用资源

HCI超融合技术对于了解它的人来说很火热，但是还有很多不太了解HCI的人；HCI的用户对它也有不同的使用场景和期望。请大家参与这个《中国超融合状态调查》，我们每月为参与本调查的朋友进行抽奖，抽奖结果在下次直播的时候公布。扫码参与调查。

![CVM HDD](img/cos/2022-01-04-dc.png)

我们为希望学习HCI技术的朋友们创建了一个qq群，希望可以给大家带来一定帮助。扫码加入我们的QQ群。

![CVM HDD](img/cos/2022-01-04-qq.png)

## 下期预告

HCI系统的搭建还有很多问题值得一起探讨和学习，HCI超融合系统软件还有很多功能可以学习了解。我们为DevOps社区的朋友们新开辟了这个HCI板块，希望以后会每个月为大家输出一期新的内容。下期直播的简介如下：

- 日期：2022 年 3 月 22 日， 下午 1点开始
- 内容：Nutanix CE 的多集群管理
- 主持人：刘征，吴孔辉
- 直播平台：B站搜/关注：中国DevOps社区
- 直播抽奖：未知神秘礼物 🎁
- 报名：互动吧搜/关注：中国DevOps社区
