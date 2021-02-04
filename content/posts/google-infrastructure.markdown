---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-06-21T07:01:58Z
slug: google-infrastructure
tags:
- BigTable
- cluster
- data center
- GFS
- Google
- MapReduce
- opensource
title: What is Google Infrastructure?
url: /2008/06/21/google-infrastructure/
wordpress_id: 49214
---

![](http://i.i.com.com/cnwk.1d/i/bto/20080529/Google_data_center_c2000_Jeff_Dean_400x318.jpg)<br /><br />If you have no idea, you should read this post "[Google spotlights data center inner workings](http://news.cnet.com/8301-10784_3-9955184-7.html?tag=blog.1)".<br /><br />There are some notes I took as blowing.<br /><br />Google Infrastructure:<br />

<br />	
  * clusters of 1,800 servers are pretty routine.
<br />	
  * [an ordinary Google search query that involves 700 to 1,000 servers](http://news.cnet.com/8301-10784_3-9954972-7.html)
<br />	
  * puts 40 servers in each rack
<br />	
  * [Google has 36 data centers across the globe](http://news.cnet.com/8301-10784_3-9917205-7.html); Google has more than 200,000 servers; growing every day.
<br />	
  * Google largely builds its own technology.
<br />	
  * to treat each machine as expendable; Google prefers to invest its money in fault-tolerant software. NOT hardware  fault-tolerant.
<br />	
  * Google uses ordinary hardware components for its servers, it doesn't use conventional packaging. Google required Intel to create custom circuit boards.
<br />	
  * As to the servers themselves, Google likes multicore chips, those with many processing engines on each slice of silicon.
<br />	
  * three core elements of Google's software: [GFS, the Google File System](http://labs.google.com/papers/gfs.html), [BigTable](http://labs.google.com/papers/bigtable.html), and the [MapReduce](http://labs.google.com/papers/mapreduce.html) algorithm.
<br />	
  * Google helps with** a lot of open-source software projects** that helped the company get its start, these packages remain proprietary except in general terms.
<br />	
  * GFS stores each chunk of data, typically 64MB in size, on at least three machines called chunkservers; master servers are responsible for backing up data to a new area if a chunkserver failure occurs.
<br />	
  * The largest BigTable instance manages about 6 petabytes of data spread across thousands of machines.
<br />	
  * On any given day, Google runs about 100,000 MapReduce jobs; each occupies about 400 servers and takes about 5 to 10 minutes to finish.
<br /><br />**总结一下上面的东西：**<br /><br />Google不是买的成品服务器，而是去Intel定制的芯片自己攒的，特别喜欢使用多核的cpu，由于他们的程序都适应与多线程并行计算的方式。一个群集有1800个服务器是非常平常的。Google大概有二十万个服务器，每40个放在一个机架上，分布在全球36个数据中心。Google不使用商业的服务器包括数据库等软件，一来造价太高，二来无法满足扩展性的需求。Google使用了很多的开源软件项目，事实上它们就是站在开源软件的肩膀上发家的；GFS，BitTable等都是它们常用的。广泛使用软件容错技术。<br /><br />**传统商业公司和google的不同：**<br />

<br />	
  1. 从硬件到软件基本都使用现成的商业产品。基础架构中的每个环境都是钱堆出来的。用钱来节省时间，不过google的时间和金钱的节省都是值得学习的。
<br />	
  2. 在容错技术上硬件HA技术用的最多，群集中的服务器数量不多。
<br />	
  3. 不同业务系统之间几乎是孤立的。从数据库到web到关联的网络设备都是一套独立的系统，甚至于按业务系统划分运维的团队。
<br />	
  4. 系统的扩展性比较小，对核心部件：如核心应用服务器或者核心数据库服务器的扩展，垂直扩展比较多，追求单机的多CPU，高主频，高内存。而另一方面：在这些系统上的压力测试和性能调优工作异常的痛苦。
<br />	
  5. 饱受被商业软件公司绑定之苦，如果数据库、应用服务器等出了产品的bug，厂商提供fix一般都需要一定的时间周期-时间代价比较高，原厂的现场技术支持服务金钱代价也比较贵。
<br />	
  6. 从高层看：CTO、CIO、CEO没有正视开源技术。只要预算允许，引入和采购业内流行的商业技术似乎是永恒的明智之举。开源软件技术应用的有不过很少。
<br />	
  7. 从基层看：工程师可能有足够的某项开源的技能，不过没有适当的渠道能反应到上层来提议使用该技术；如果在下面擅自使用了某种技术，非常担心出了IT事故后对后果的承担。开源技术对技术人员只是一个爱好而无法应用与自己的日常工作中。
<br />	
  8. 特别是中国用户对最新潮的IT技术永远保持着极度的热情，不管是硬件和软件买就买最先进的，数据中心的机房最后成为博物馆，新老系统很难整合资源。把基础架构的彻底改变寄希望于未来的某种技术革命，实际上技术变革已经悄悄发生了好几波了，怎么管理现状怎么就是越来越艰难，越来越花钱呢？走中国特色道路真的值得提倡一下了。
<br /><br />Google的这些特点真是引人入胜，任何企业都无法复制；而且也不可能复制，它毕竟是一个商业公司而不是一个开源项目。如何使用现有的技术和人员来打造出你自己的完美基础架构呢？现实中这么多的role model已经证实了很多技术都是可用的，完美的境地也不是空中楼阁。如何集思广益并多多引入开源技术和人才可能是一个需要斟酌的题目。<br /><br />[poll id="3"]
