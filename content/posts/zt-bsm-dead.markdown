---
author: liuadmin
categories:
- ITSM
comments: true
date: 2010-09-17T18:46:09Z
slug: zt-bsm-dead
tags:
- BMC
- BSM
- CA
- cloud
- cmdb
- Integrien
- ITSM
- virtuali
- VMWare
title: '[ZT] Old BSM is dead'
url: /2010/09/17/zt-bsm-dead/
wordpress_id: 50807
---

![](http://www.smarthomecn.com/upload/2008_11/081112102554402.jpg)随着云计算和虚拟化的来临，IT架构愈加复杂，老一套的IT管理方案只能监控静态的基础架构。老一套的CMDB和BSM给运维无法带来实质性的帮助，需要能够具有自适应、自学习IT环境的能力，管理工具需要对IT环境的变化有感知，有学习功能，否则无法对业务故障的处理给予应有的支持。转帖自学一下这个文章，老外从IT架构的历史讲起，横跨跨服务保证和CMDB等领域，讲的还是很不错的。
[The Significance of the VMware Integrien Acquisition](http://www.virtualizationpractice.com/blog/?p=7186)
While it may seem that with Integrien [VMware](http://www.virtualizationpractice.com/blog/?page_id=2983) has acquired yet one more piece of the puzzle (a puzzle whose final  form no one knows), this acquisition is perhaps one of the most  significant if not the most significant that [VMware](http://www.virtualizationpractice.com/blog/?page_id=2983) has done. To understand the significance of this acquisition, one has  to step back and examine a bit of history in the Systems Management  business.

For as long as there have  been computers, operating systems and business critical applications,  there has been monitoring of these items to make sure they were working  (available) and performing well for their constituents. In the early  days of the computer industry (through about 1982) computer systems were  vertical monoliths where a customer would buy “an accounting system”  and that purchase would include hardware, systems software, and  applications software. All of this usually came from one vendor so there  was one throat to choke when it did not work.

Starting with the  delivery of the PC, then Ethernet LAN’s and Novel Netware, and finally  Windows Servers and the Internet, the industry reorganized along  horizontal dimensions. A computer system was now a multi-layer cake and  you could buy each cake from one of many vendors whose products were  largely interchangeable with each other, and compatible with adjacent  layers. So you could buy an Intel based server from one of N vendors,  put either Linux or Windows on it, but a Java applications server from  one of N vendors on that and then buy applications from thousands of  different vendors.

This horizontal layering of the industry was heavily promoted by [Microsoft](http://www.virtualizationpractice.com/blog/?s=microsoft) and Intel (who “owned” two key layers of the cake), and also ushered in  the tremendous innovation and price competition that continues to drive  our industry today. Moore’s Law says that microprocessor performance  doubles roughly every 18 months or so, and with those increases in  price/performance come the more for less mentality that we have all  become accustomed to.

With this freedom of choice at every layer  of the cake however came problems. The first problem was complexity.  There were now too many cooks in the kitchen which meant that there were  both too many and not one single throat for the CIO to choke when  something went wrong. The management software industry reacted to this  by inventing a marketecture, Business Service Management (BSM). The idea  behind BSM was to identify the key business services that applications  or combinations of applications delivered to users (the ability to enter  and order and ship the resulting product is a business service as is  the ability of a consumer to transfer funds from one banking account to  another), and to then map all of the software and hardware  infrastructure that this business service depended upon and to manage  that collection of linked resources as an entity.

While Business Service Management sounded like a great idea, it in fact ended up as a miserable failure. The reasons were:



	
  * There were many applications for which it was just too hard to measure  their performance (in response time terms). Web applications turned out  to be pretty easy, but fat client Win32 applications written to  proprietary client/server protocols turned out to be very hard. It  turned out that for most enterprises, more than half of the business  critical applications were in the hard pile (fat client/Win32) and less  than half were the easy web applications.

	
  * Many BSM frameworks  relied upon scripts and synthetic transactions to measure response time  and end user experience. However this approach failed for many  enterprises due to the large number of applications that comprised a  business service and how rapidly these applications were changing. For  example if synthetic transactions were used to measure the performance  of a set of transactions, and a company had 500 business critical  applications (not a very high number – some companies have thousands),  and each application was updated once a year, then that would translate  into 10 updates a week for the monitoring scripts.

	
  * The same is true for  most passive monitoring approaches that rely upon templates to identify  transactions in applications protocols. There are many products that can  measure the response time of transactions from the perspective of the  web server by attaching physical or virtual appliance to a span port on  the switch that services the web server. However all such products  require configuration to understand what set of granular http  request/responses combine to create a transaction of interest.  Maintaining these configurations across hundreds of applications and  thousands of transactions proved to be a major impediment to  instrumenting their service level in any kind of a broad and systematic  manner.

	
  * It turned out to be a nightmare to identify the hardware  and software that supported each business service. This gave rise to  the need for Configuration Management Databases (CMDB’s) that were  supposed to get populated with the hardware and software assets and  their relationships to each other. The effort to put in place a CMDB and  to maintain it turned out to doom the CMDB projects and the associated  BSM projects at many companies.

	
  * The BSM vendors were unable to  evolve their products at the same rate as the innovation of the vendors  who contributed products to the layers in the cake. New devices (laptops  that were not always connected), new protocols (ICA, VOIP), new  operating systems (Linux), new languages (Java, C#), and new user  interfaces (first the browser and then rich Internet applications) all  occurred at a pace that no one vendor could keep up with.

	
  * When  the BSM vendors got overwhelmed by innovation, vendors of point  monitoring solutions stepped in to monitor the newest layer or item in a  layer.  This lead to a proliferation of monitoring tools which were not  integrated with each other.

	
  * When a problem occurred even if one  had a BSM product and a CMDB it still horribly difficult to know  exactly what path the failed transaction took through the entire  hardware and software infrastructure. The BSM tools were rarely aware of  every element of the stack and the tactical monitors that had been  bought to fill in the cracks were not integrated with the BSM tools nor  each other.


In summary we entered the age of virtualization  and the cloud with both BSM and their supporting CMDB’s having failed at  monitoring and managing a static infrastructure where applications and  services largely stayed on dedicated hardware. In other words, before  virtualization and the dynamic data center it was impossible for anyone  in IT to see a problem and get told in a deterministic manner exactly  where the problem was and how to fix it.

**The Impact of Virtualization and the Cloud**

Since  holistic end-to-end monitoring of business services was essentially  broken (or not attainable) before virtualization, it is reasonable to  assume that virtualization and the cloud will only make this problem  worse. This will occur for the following reasons:



	
  1. Virtualization  increases workload density and the dynamic operation of workloads. This  will require both continuous mapping of application to infrastructure  dependencies and more more frequent (near real time) collection of  performance data. Just the requirements for real time mapping and real  time data completely overwhelm existing monitoring systems. Hyperic has a  good blog on this point [here](http://blog.hyperic.com/vfabric-hyperic-weaves-performance-management-into-cloud-applications/).

	
  2. Inferring  application performance from resource utilization statistics becomes  impossible. This was possible on physical hardware, but on hardware that  is shared via virtualization it no longers works. Hence the need for  Infrastructure [Performance Management](http://www.virtualizationpractice.com/blog/?cat=9) solutions that measure Infrastructure Response Time. We expect Infrastructure [Performance Management](http://www.virtualizationpractice.com/blog/?cat=9) solutions from vendors like [Akorri](http://www.virtualizationpractice.com/blog/?page_id=1603), [CA](http://www.virtualizationpractice.com/blog/?page_id=6234) Technologies ([CA](http://www.virtualizationpractice.com/blog/?page_id=6234) Virtual Assurance), [Virtual Instruments](http://www.virtualizationpractice.com/blog/?page_id=6476), and [Xangati](http://www.virtualizationpractice.com/blog/?page_id=3551) to form the foundation layer of whatever will replace BSM.

	
  3. Application  will now get moved from cluster to cluster and ultimately from data  center to data center (private cloud – hybrid cloud – public cloud). APM  solutions will need to track the applications no matter where they go,  and seamlessly work across different IP networks. Leading virtualization  aware APM solutions like those from [AppDynamics](http://www.virtualizationpractice.com/blog/?page_id=4724), [BlueStripe](http://www.virtualizationpractice.com/blog/?page_id=2416), and [New Relic](http://www.virtualizationpractice.com/blog/?page_id=1505) meet these needs today and will likely form the APM layer of whatever replaces BSM.


All  of the above together combine to create one new result for Systems  Management. That new result is that in the general case it will be  impossible to deterministically do root cause in a dynamic environment.  This was explored in detail in this [post](http://www.virtualizationpractice.com/blog/?p=5915).

**The Significance of the Integrien Acquisition**

The Integrien acquisition by [VMware](http://www.virtualizationpractice.com/blog/?page_id=2983) is significant because it means that [VMware](http://www.virtualizationpractice.com/blog/?page_id=2983) has recognized that only a dynamic, statistical, self-configuring,  and  self-learning approach can keep up with the rate of change in these new  dynamic IT environments. The self-learning approach simply means that  you feed the system the metrics that get collected about the system and  it figures out which ones are important, how the metrics are related to  each other, and lets you know when anomalies have occurred.

This  acquisition is all the more significant because this is not garden  variety technology. There have only ever been three companies this this  space. ProactiveNet was acquired by BMC a few years ago. [Netuitive](http://www.virtualizationpractice.com/blog/?page_id=7123) has been around since the late 1990′s and it took the company until the  mid 2000′s before the product had matured into something that really  just worked when you plugged it in. Integrien is a fairly recent entry  in this field and is now part of [VMware](http://www.virtualizationpractice.com/blog/?page_id=2983) – which leaves [Netuitive](http://www.virtualizationpractice.com/blog/?page_id=7123) as the only remaining independent player.

**The New Dynamic BSM – Service Assurance**

Since  the old BSM is dead due to a brittle and difficult to update technology  approach it is reasonable to ask what will replace it. The answer is  most likely a set of Infrastructure [Performance Management](http://www.virtualizationpractice.com/blog/?cat=9) tools ([Akorri](http://www.virtualizationpractice.com/blog/?page_id=1603), [CA](http://www.virtualizationpractice.com/blog/?page_id=6234) Virtual Assurance, [Virtual Instruments](http://www.virtualizationpractice.com/blog/?page_id=6476), [Xangati](http://www.virtualizationpractice.com/blog/?page_id=3551)) integrated with a set of next generation APM tools ([AppDynamics](http://www.virtualizationpractice.com/blog/?page_id=4724), [BlueStripe](http://www.virtualizationpractice.com/blog/?page_id=2416), [New Relic](http://www.virtualizationpractice.com/blog/?page_id=1505))  vis these self learning technologies. When this occurs, we will have a  system that adapts on its own to changing conditions in the environment  leaving IT staff available to interpret results (and not raw monitoring  data). We will also have taken an important step towards dynamic service  assurance which was discussed in detail in this [post](http://www.virtualizationpractice.com/blog/?p=5472).

**Understanding and Evaluating these Technologies**

For  most IT professionals either they or someone on their staff can digg in  and understand how the technologies that they use work. However unless  you have an advanced degree in statistics and/or mathematics you are not  going to be able to dig an and decide for yourself based upon how these  products work which one you should choose. Rather what you should do is  apply the following criteria in making your selection:



	
  1. Decide  exactly what you want the product to do for you. These products are  extremely flexible. You can feed them every alarm that is generated by  all of your monitoring solutions and let them sort out the good ones  from the bad ones. Or you can feed them revenue per minute for one key  business application and let them figure what causes degradations in  revenue per minute.

	
  2. Make sure that the product has connectors to  what you already use to collect metrics from your systems. These  products are not in the data collection business (with some exceptions).  They rely upon other products to collect data from them. They must  therefore be interfaced with your existing monitoring solutions.

	
  3. How  hands off and plug and play will the product be in practice? This is  the key criteria to the long term value of such a solution to your  enterprise. Previous attempts at statistical approaches (neural nets)  failed because the product had to be “retrained” every time conditions  changed. Make sure that the product you select can automatically select  and weight the inputs that it bases decisions off of and these these  decisions are automatically updated over time. Self-learning needs to be  a continuous thing, not just a one time or periodic thing.

	
  4. Make  sure that the product can handle time based (time series) as well as  event based data. Performance metrics tend to be time based, but many  performance problems are caused by configuration changes which are  events. Make sure that the product can cross-correlate configuration  change events with performance degradations.

	
  5. Carefully assess  the scale of the solution. This means how many inputs can the solution  take per unit of time. Right now most of these solutions operate at 15  minute or 5 minute intervals. Monitoring a dynamic system may require  intervals of 10 or even 5 seconds (or perhaps even real time continuous  streams of monitoring data).


**Summary**

Self-learning [performance management](http://www.virtualizationpractice.com/blog/?cat=9) solutions like Integrien and [Netuitive](http://www.virtualizationpractice.com/blog/?page_id=7123) are going to be absolutely an essential part of the migration to  dynamic data centers and IT as a Service. Once these dynamic data  centers scale out to the thousands of applications in a typical  enterprise, and scale up to address the most performance critical  applications, the rate of change in the environment will be too high for  legacy tools and manual administration to be able to keep. up. These  automated self-learning approaches will be the only way in which IT  Operations will be able to stay on top of these new environments while  staying within staffing and budget constraints.
