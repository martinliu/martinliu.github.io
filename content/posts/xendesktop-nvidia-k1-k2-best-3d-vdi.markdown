---
author: liuadmin
categories:
- XenDesktop
comments: true
date: 2013-08-16T11:52:58Z
subtitle: Citrix + nVIDIA K1 k2 + XenServer （GPU 直通） + HDX 3D Pro = 业内最好的3D虚拟桌面平台方案；而且这个方案里还能具有，其它全部的使用场景，包括：vdi，共享桌面，虚拟应用，流桌面，远程物理桌面等等方式。可以说这是一举多得，面面俱到的解决方案。
slug: xendesktop-nvidia-k1-k2-best-3d-vdi
tags:
- 2D
- 3D
- NVIDIA
- VDI
- 虚拟应用
title: XenDesktop + nVIDIA K1/K2 = BEST 3D VDI
url: /2013/08/16/xendesktop-nvidia-k1-k2-best-3d-vdi/
wordpress_id: 52549
---

今天公司到货了K1，K2的GPU卡，这让我不得不学习一下这个产品。


[![grid-overview-header](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/08/grid-overview-header.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/08/grid-overview-header.jpg)


 <!--more-->

到货实物如下：

[gallery link="file" ids="52542,52543,52544,52545,52546,52547"]

此卡的简单技术指标如下。
<table cellpadding="0" width="560" cellspacing="0" border="0" >
<tbody >
<tr >

<td bgcolor="#e8e7e7" width="186" >
</td>

<td bgcolor="#e8e7e7" width="186" >


## GRID K1



</td>

<td bgcolor="#e8e7e7" width="186" >


## GRID K2



</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Number of GPUs
</td>

<td bgcolor="#f1f1f1" width="186" >4 x entry Kepler GPUs
</td>

<td bgcolor="#f1f1f1" width="186" >2 x high-end Kepler GPUs
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Total NVIDIA CUDA cores
</td>

<td bgcolor="#f1f1f1" width="186" >768
</td>

<td bgcolor="#f1f1f1" width="186" >3072
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Total memory size
</td>

<td bgcolor="#f1f1f1" width="186" >16 GB DDR3
</td>

<td bgcolor="#f1f1f1" width="186" >8 GB GDDR5
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Max power
</td>

<td bgcolor="#f1f1f1" width="186" >130 W
</td>

<td bgcolor="#f1f1f1" width="186" >225 W
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Board length
</td>

<td bgcolor="#f1f1f1" width="186" >10.5”
</td>

<td bgcolor="#f1f1f1" width="186" >10.5”
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Board height
</td>

<td bgcolor="#f1f1f1" width="186" >4.4”
</td>

<td bgcolor="#f1f1f1" width="186" >4.4”
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Board width
</td>

<td bgcolor="#f1f1f1" width="186" >Dual slot
</td>

<td bgcolor="#f1f1f1" width="186" >Dual slot
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Display IO
</td>

<td bgcolor="#f1f1f1" width="186" >None
</td>

<td bgcolor="#f1f1f1" width="186" >None
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Aux power
</td>

<td bgcolor="#f1f1f1" width="186" >6-pin connector
</td>

<td bgcolor="#f1f1f1" width="186" >8-pin connector
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >PCIe
</td>

<td bgcolor="#f1f1f1" width="186" >x16
</td>

<td bgcolor="#f1f1f1" width="186" >x16
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >PCIe generation
</td>

<td bgcolor="#f1f1f1" width="186" >Gen3 (Gen2 compatible)
</td>

<td bgcolor="#f1f1f1" width="186" >Gen3 (Gen2 compatible)
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="186" >Cooling solution
</td>

<td bgcolor="#f1f1f1" width="186" >Passive
</td>

<td bgcolor="#f1f1f1" width="186" >Passive
</td>
</tr>
</tbody>
</table>


[![NVIDIA_vGPU_News](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/08/NVIDIA_vGPU_News.jpg)](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2013/08/NVIDIA_vGPU_News.jpg)

详细 K1 K2 技术参数指标，[ 下载 ； ](http://www.nvidia.com/content/cloud-computing/pdf/nvidia-grid-datasheet-k1-k2.pdf) 这个表格清晰的说明了这两种卡的硬件技术参数。重要的是看它软件合作伙伴这一块。硬件在好，没有支持的软件也不行，我们必须还有看看它的软件合作伙伴：[http://www.nvidia.com/object/grid-software-partners.html](http://www.nvidia.com/object/grid-software-partners.html)

首先，是认证的虚拟应用合作伙伴，这里只有Citrix XenApp；只有Citrix可以做3D设计软件的应用虚拟化；其它无人能及，基于Citrix的应用虚拟化可以真正的把一块GPU的共享程度达到最大，能够更加节约支撑的硬件资源。节省每一度电。还要看支持的API的版本号，这个说明了对3D软件的兼容性，如果这个版本号类型少，支持的低，那么这种方案是不可用的；由于3D软件根本就跑不动。
<table cellpadding="0" width="560" cellspacing="0" border="0" >
<tbody >
<tr >

<td bgcolor="#f1f1f1" width="175" >
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >NVIDIA Driver
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >API
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >GRID K1
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >GRID K2
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="175" >**Citrix**
[XenApp 6.5 with OpenGL 4.3](http://www.nvidia.com/object/xenapp.html)
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >NVIDIA CUDA
DirectX 9,10,11
OpenGL 4.3
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>
</tr>
</tbody>
</table>
其次，要看认证的虚拟桌合作伙伴厂商，这里稍微多点；这里关键看点是NVIDIA Driver这一列。你有可能会说NVIDIA的显卡驱动难道不能装到所有类型的VDI虚拟桌面中么？我我想这个表格就是答案。一个GPU经过服务器虚拟化层之后，只有Citrix的虚拟桌面能够拿到NVIDIA的原生驱动，也就是说只有Citrix的VDI能够通过NVidia的显卡驱动，穿透服务器虚拟化层直接调用到GPU的原生指令进行运算。而VMwere也有NVIDIA的驱动啊！注意，它的驱动是装在那里的，它的驱动是装在hypervistor上的；也就是说虚拟机必须通过这个模拟的驱动程序层使用GPU的运算能力，这个驱动层做的是GPU指令的翻译和仿真，它实在不能让虚拟桌面的虚拟操作系统中的3D软件透过API直接调用GPU的运算指令。这意味这GPU的性能的折损，这意味您花高昂价格采购的服务器虚拟化软件正在浪费您花更贵价格买来的GPU，k1、k2的卡市场价格都3万多的。这样的方案是否值得买，必须考虑一下。最后要看View5.2 with vSGA，两点在vSGA，这个东西对很对3D软件来说是不可用，不可以接受的。甚至于某些专业3D/2D软件在这显示模式下，连安装都成问题。
<table cellpadding="0" width="560" cellspacing="0" border="0" >
<tbody >
<tr >

<td bgcolor="#f1f1f1" width="175" >
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >NVIDIA Driver
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >API
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >GRID K1
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >GRID K2
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="175" >**Citrix**
[XenDesktop FP1 with NVIDIA GRID vGPU](http://www.nvidia.com/object/xendesktop-vgpu.html)
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >NVIDIA CUDA
DirectX 9,10,11
OpenGL 4.3
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="175" >**Microsoft**
[RemoteFX](http://www.nvidia.com/object/quadro-remotefx.html)
Windows Server 2012
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >-
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >DirectX 9,10,11
OpenGL 1.1
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>
</tr>
<tr >

<td bgcolor="#f1f1f1" width="175" >**VMware**
View 5.2 with vSGA
</td>

<td bgcolor="#f1f1f1" align="center" width="66" >-
</td>

<td bgcolor="#f1f1f1" align="center" width="102" >DirectX 9
OpenGL 2.1
</td>

<td bgcolor="#f1f1f1" align="center" width="78" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>

<td bgcolor="#f1f1f1" align="center" width="72" >![Yes](http://www.nvidia.com/docs/IO/123679/check-mark.png)
</td>
</tr>
</tbody>
</table>
也可能某些厂商说：我有vGPU技术。这是用CPU模拟GPU的技术。您可以想想，如果这个技术真的存在的话那么我们只需要有一家公司就行了，就是Intel，而不需要另外一家Nvidia了。这个技术说白了也是仿真模拟，专业的3D/2D软件真正消耗越来越多的计算资源，在某些业务场景下模拟GPU是没法完成工作的，你总不能等待一个渲染和处理要等上几周去完成吧？而且设计师的时间是宝贵的，也不能让操作有顿挫和卡顿出现的。下面的视频，解释了在同一种虚拟桌面情况下，有GPU加速和，无GPU加速（CPU模拟）的操作对比。


总之，Citrix + nVIDIA K1 k2 + XenServer （GPU 直通） + HDX 3D Pro = 业内最好的3D虚拟桌面平台方案；而且这个方案里还能具有，其它全部的使用场景，包括：vdi，共享桌面，虚拟应用，流桌面，远程物理桌面等等方式。可以说这是一举多得，面面俱到的解决方案。
