---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-02-15T08:45:00Z
slug: smokeping-chart
tags:
- chart
- smokeping
title: 如何看懂Smokeping图表
url: /2007/02/15/smokeping-chart/
wordpress_id: 49139
---

![](http://docs.google.com/File?id=dgt3878v_6z3dfsf)

<br />

<br />

**_RTT(Round-Trip Time) _**

<br />

简单说它是一个数据报在网络上两点中间往返一次的时间。是影响TCP性能和表征网络运行状况的重要参数。在网络中实时、准确地测量大量TCP设备和系统的RTT参数是网络管的重要环节之一。Smokeping就是这样的自动测试系统，它向目标设备和系统发送各种类型的测试数据包，测量、记录和展示RTT。

<br />

<br />

**_Median RTT _****_中间数_**

<br />

它是中间数并不是平均值。Smokeping有多种类型的探针，探针在默认的设置下，每300秒向目标设备发送20测探测数据包。假如这20个数据包都返回的话，它就记录下了20个RTT，那么Median RTT就是第十个包的RTT；如果有5个包丢失的话，那么Median RTT就是第八个返回的包的RTT值。

<br />

<br />

**_Avg RTT _****_评价值_**

<br />

它是每一个测试回合中所有RTT的算术评价值。

<br />

<br />

**_Avg pkt loss_**

<br />

它是丢包率。

<br />

<br />

上图中测试的三个服务器，是用默认的FPing探针探测该服务器是否在线。Smokeping就装在OpenNMS上，可以看出它的RTT最小；奇怪的是它的丢包率却是最大。其它的，一个是美国的一个Web服务器，另一个是美国的Exchange邮件服务器。

<br />

<br />

![](http://docs.google.com/File?id=dgt3878v_7fs5j82)

<br />

_Last 3 Hours_ 最近的3小时

<br />

_Median Ping RTT （__506.2 ms avg）_中间数的平均值是5.6.2毫秒。如果是绿色的短横线，说明一个300秒的周期内所有的包都返回都有RTT的时间记录下来；如果是蓝色的短横线则说明有2个包丢失。

<br />

_Packet Loss：_丢包率。从上图中我们看出全都是绿线，所以丢包率当然是0。

<br />

_Probe：__10 HTTP pings using echoping(1) every 300 seconds_

<br />

这张图是2007-1-11 12:00:05生成的。每一个绿色的短横线都是一个测试回合300秒内用echoping测试HTTP协议10次。绿色画出的是中间数的位置，一个回合中的其它值都在它附近被以灰度的形式被刻画；灰度的范围越小越好，灰色的范围像是烟雾一样笼罩在中间数附近。在中间数附近的烟越小越好，说明网络很平稳。RTT曲线的起伏还显示了网络的负载情况。

<br />

点击这里看一个[网上的Demo](http://oss.oetiker.ch/smokeping-demo/?target=Customers.OP)

<br />

update : 2008-1-18

<br />

现在OpenNMS把smokeping集成了，你可以在OpenNMS中配置使用这个功能。
