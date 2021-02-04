---
author: liuadmin
categories:
- BMC
comments: true
date: 2011-05-07T10:31:36Z
slug: let-remedy-ars-fly-2
tags:
- ARS
- ITSM
- oracle
- remedy
- Tomcat
- 性能调优
title: 让Remedy飞一会
url: /2011/05/07/let-remedy-ars-fly-2/
wordpress_id: 51051
---

![](http://www.ibm.com/developerworks/cn/websphere/techjournal/0909_blythe/images/figure6.jpg)Remedy应用的性能优化是一个在系统建设过程中需要长期关注的问题，而不是在上线的前一天晚上去解决的问题，我也碰到过很棘手的性能问题，它确实爆发了，而且恰好在上线前夕爆发；之后感觉除了点背之外，感觉比较遗憾的是：为啥这个性能问题不早点爆发！

那么如何持续改进Remedy的性能？首先是硬件环境的准备情况，是否能在项目开始的第一天，就把开发，测试，生产环境统一装好。而不是到上线的前夕才去动生产环境。甚至于有条件的情况下，可不可以直接在生产环境上做开发，这样做的好处：让生产环境上性能优化的时间周期和机会尽可能的多，尽可能的长。当然这种机会毕竟不多，那么是否可以做到生产环境和开发环境的尽早的同步，也就是说：在开发到了一个小的阶段的时候，生产环境就可能就绪，就可以使用，这样把未成型的系统先部署上去，以便有机会做多次的生产系统性能调优。比较生产系统的性能最优化是项目的一大目标，不能等到最后才去仓促应战。曾经听说某行流程平台上线的第二天就挂了一次，这都是血淋淋的教训。总结一下：尽早的建设生产系统，优化生产系统，把开发好的那部分程序尽早迁移到生产上，长期的追逐系统性能，甚至于在生产环境上对此系统做压力测试。这些工作如果能够做的话，我想在上线日我们一定不会紧张。

如何追逐测试系统的性能。可以使用Web profiling工具如Fiddler。使用这种工具对某些特定操作持续的测试，把每次的测试结果保存下来，把时间记录到一个表格中。可以考虑测试如下内容：用户登录、打开事件控制台、创建一个事件单、搜索事件单等等，其他流程也类似。保证每次点击的次数都相同。其实从Fildder的分析数据中也可能得到很有价值的数据，如：那个Web调用的时间消耗最长，那些Web资源的请求出错。找出时间消耗做多的调用，就可以有针对性的优化应用了。总之：使用一种工具，在开发的整个过程中持续测试和优化，记录所有测试结果，这样在上线前对系统的性就能有客观参考依据。

另外要注意Remedy系统是一个标准的3层架构应用，你需要在系统调优的时候，有这样几种人的帮助：压力测试工具高手、JVM调优专家、数据库调优专家和Remed性能调优专家。还需要参考下列的参数配置。


## Mid-tier优化参数建议


关于Mid-tier的一点建议，目前普通使用的Java应用服务器都是Tomcat，我一向是开源软件的粉丝，但是，还是建议如果有条件的话，还是上商业的产品，如Weblogic或者Websphere。这样可以获得能多一点的支持。
鉴于大多数系统还都是用的BMC的产品自带的Tomcat，下面是一些建议的参数配置。


### 1-HTTP keep-alive


Keep-alive count:  infinite (minimum 5000)
Connection timeout:90000 ms (minimum 60000 ms)


### 2-JVM settings


JVM heap：-Xms1024m –Xmx1024m
MaxPermSize：-XX:MaxPermSize=256m
以Windows系统为例，可以使用Tomcat的配置界面工具，配置这两个参数。


### 3-Threads configuration of the application server hosting the mid tier


maxThreads：500
acceptCount：100

关于1和3的 参数文件：tomcat dir/conf/sever.xml 的实例代码：
[xml]

<Connector URIEncoding="UTF-8" acceptCount="100" connectionTimeout="90000"

maxHttpHeaderSize="8192" maxKeepAliveRequests="-1" maxThreads="500"

port="80" protocol="HTTP/1.1" redirectPort="8443"/>

[/xml]

以上参数配置并不是万能的，只是给出一个优化配置的基础，以此为起点调起来可能会更靠谱。


### Fine tuning the mid tier


Mid tier parameter or service：   Recommended value
**Enable Cache Persistence**：Always on for a production environment
**Prefetch or preload service**： Use prefetch only when a specific set of AR System forms are known. Otherwise, use preload (recommended).
**Recommended preload procedure**： 1.Turn on Enable Cache Persistence. 2.Turn on preload. 3.Allow preload to finish preloading all user facing AR System forms. 4.Turn off preload (allowing statistical service to take over).
**arsystem.formhtmljs_expiry_interval **和 **arsystem.resource_expiry_interval**： Set both parameters to the same value to reflect how often you want the browser to check with the mid tier for updates. In a deployment environment where the AR System applications are not modified, set to 604800 (1 week) or higher. The minimum recommended value is 86400 (1 day). For the new values to take effect, restart the mid tier.
**Definition Change Check Interva**l： In a deployment environment where the AR System applications are not modified, turn this off. Otherwise, map this to the frequency of your AR System application modification. For example, if you push changes out every Sunday, set this frequency to 604800 (1 week).
**arsystem.log_level**： Severe. This can also be set through the Mid Tier Configuration Tool


## ARS优化参数建议


打开ar.cfg参考一下参数，修改后重启ARS服务。

**Delay-Recache-Time:300**
** Max-Entries-Per-Query:2000**
** Next-ID-Block-Size:100**
** Server-Side-Table-Chunk-Size:1000**
** Allow-Unqual-Queries:F**
** Cache-Mode:0**
** Debug-mode:0**
** Submitter-Mode:1**
** CMDB-Cache-Refresh-Interval:600**


## 数据库优化参数建议


数据库方面一定要依靠有经验的DBA，靠他们帮你搞定下面这两条：
• Configuring your AR System database server for optimal performance
• Diagnosing and resolving issues.
另外如果你是Oracle11g的数据库，可以自己动手搞定下面这一条：
Oracle 10g/11g database settings are recommended: Cursor_sharing = FORCE
在数据库上做如下操作：
[sql]
alter system set cursor_sharing=FORCE scope=both;
[/sql]
然后在ar.cfg里面加入这个参数。
Oracle-Cursor-Sharing: FORCE
然后重启ARS服务即可。

以上参数配置部分参考了BMC的官方文档《BMC Remedy AR System Server 7.6 Performance Tuning for Business Service Management 199037.pdf》，感兴趣的话可以去官方站点的文档下载里下载，该文章对以上参数有详细的解释。
