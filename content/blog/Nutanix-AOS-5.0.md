---
date: 2017-01-04T00:00:00Z
subtitle: 新看点快速一览
image:
  feature: RoyalBarge_ROW9071716647_1920x1080.jpg
tags:
- Nutanix
title: Nutanix AOS 5.0 新版本新特性
url: /2017/01/04/Nutanix-AOS-5.0/
---

Nutanix AOS 5.0 是一个很重要的功能更新大版本，它一气儿带来了46项之多的新功能；在您安装或者测试这个版本>    之前，先通过本文快速了解一下这些更新，可能是更加节省时间的方法。

## 主要功能清单
myvirtualcloud.net网站用了4个blog，讲了下面的36项新特性：

1. Cisco UCS B-Series Blade Servers Support
2. Acropolis Affinity and Anti-affinity
3. Acropolis Dynamic Scheduling (DRS++)
4. REST API 2.0 and 3.0
5. Support for XenServer TechPreview
6. Network Visualization
7. What-if analysis for New workloads and Allocation-based forecasting
8. Native Self-Service Portal
9. Snapshots – Self Service Restore UI
10. Network Partner Integration Framework
11. Metro Availability Witness
12. VM Flash Mode Improvements
13. Acropolis File Services GA (ESXi and AHV)
14. Acropolis Block Services (CHAP authentication)
15. Oracle VM and Oracle Linux Certified for AHV
16. SAP Netweaver stack Certified for AHV
17. Prism Search Improvements (support for Boolean expressions)
18. I/O Metrics Visualization
19. 1-Click Licensing
20. LCM – Lifecycle Manager
21. Additional Prism Improvements
22. AHV Scale Improvements
23. AHV CPU and Memory Hot Add (Tech Preview)
24. Advanced Compression for Cold Data
25. Acropolis Change Block Tracking (CBT) for Backup Vendors
26. Predictable Performance with Autonomic QoS
27. NCC 3.0 with Prism Integration
28. 1-Node Replication Target
29. Improved Mixed Workload Support with QoS
30. Simplified SATADOM Replacement Workflow
31. Mixed Node Support with Adaptive Replica Selection
32. Dynamically Decreased Erasure Coding Stripes – Node Removals
33. Multi Metadata Disk Support for use available SSDs on the node for metadata
34. Erasure Coding(EC) support for changing the Replication Factor (RF) on containers
35. Inline Compression for OpLog
36. Linux Kernel Upgrade

* [Nutanix 5.0 Features Overview (Beyond Marketing) – Part 1](http://myvirtualcloud.net/nutanix-5-0-features-overview-beyond-marketing-part-1/)
* [Nutanix 5.0 Features Overview (Beyond Marketing) – Part 2](http://myvirtualcloud.net/nutanix-5-0-features-overview-beyond-marketing-part-2/)
* [Nutanix 5.0 Features Overview (Beyond Marketing) – Part 3](http://myvirtualcloud.net/nutanix-5-0-features-overview-beyond-marketing-part-3/)
* [Nutanix 5.0 Features Overview (Beyond Marketing) – Part 4](http://myvirtualcloud.net/nutanix-5-0-features-overview-beyond-marketing-part-4/)



## Nutanix官方Blog新版本介绍

Nutanix 官方Blog的新版本发布帖  [The 5.0 Release is Here](https://www.nutanix.com/2017/01/03/5-0-release/)

Nutanix AOS 5.0 is available now for you to download and will carry a huge payload of innovation across Acropolis – the data plane, Prism – the management plane and AHV – built-in hypervisor. Over the last couple of months we have spoken about different capabilities that will be part of this release. Before we get into details of the release, it is important to take a step back and understand how the core platform is evolving.

![](/images/14835396530706.png)
* These services are announced but will be generally available in a subsequent product release

To deliver on the vision of Enterprise Cloud and offer public cloud-like services within the datacenter, it is important for us to provide infrastructure services similar to what the public cloud offers. Different workloads have different infrastructure needs and it is important to provide services that can be “turned-on” and “turned-off” based on applications needs – all without having to touch the underlying physical infrastructure. This is exactly what AWS does and that is what we are working towards with our Enterprise Cloud Platform as well.

Here is a comparison of some of these infrastructure services offered by AWS and Nutanix. The core tenets of the public cloud and the pay-as-you-grow economics are as applicable to Nutanix as it is to the public cloud.

![](/images/14835397395341.png)

The 5.0 release adds new infrastructure services to the platform and enhances the ones that already exist; delivering greater flexibility and potential cost savings for IT organizations of all sizes. With over 45 new capabilities in the software and hundreds of feature enhancements, this release is definitely a huge milestone for us.

While it is impossible for us to cover all the capabilities in detail in one single blog, let me attempt to do a quick walk through of the ones we think you will love!

### Acropolis – Data Plane Enhancements

**Acropolis File Services (AFS)Generally Available:**  AFS is a natively built file storage service that eliminates the need for standalone NAS solutions. This capability was in Tech Preview for the past several months and is generally available with the 5.0 release. With AFS, customers can consolidate their virtual machines and the file data they rely on within the same cluster. AFS will work on ESXi and AHV hypervisors for a wide variety of use cases such as user-profiles, home directories, archives and more. You can learn more about this capability in this blog. Here is a quick summary [blog on AFS.](https://next.nutanix.com/t5/Nutanix-Connect-Blog/Ten-Things-you-need-to-know-about-Nutanix-Acropolis-File/ba-p/14524)

**Acropolis Block Services (ABS) Enhancements:** ABS, like AFS, is natively built to expose storage to non-virtualized workloads. This capability was introduced in the 4.7 release. We have significantly enhanced ABS in 5.0 with support for dynamic load balancing and flash pinning for better performance, improved security through CHAP for safer client-server conversations and online resizing for higher availability. Additionally, Oracle joins the list of certified workloads on ABS. Here is a quick summary [blog on ABS.](http://next.nutanix.com/t5/Nutanix-Connect-Blog/Ten-Things-you-need-to-know-about-Nutanix-Acropolis-Block/ba-p/14969)

![](/images/14835399454618.png)


**Metro Availability Witness:** Metro Availability is Nutanix’s synchronous replication solution for DR. Metro Availability Witness is a light-weight service that will be able to run anywhere to enable automatic failover from one site to another without service disruption by monitoring the status of both sites.

**Compression Enhancements:** The compression algorithm used for capacity optimization has significantly improved in the 5.0 release resulting in more efficient data compression. Additionally, on All-flash systems, compression will be turned on by default. With compression, deduplication, erasure coding and other native capacity optimization capabilities, customers can achieve up to 4:1 savings (depending on data type).

**Single-node Replication Target:** One of the common asks from Remote and Branch office/SMB customers was to have a single-node backup/replication target for smaller deployments of Nutanix. This enables customers to use native backup capabilities and replicate data to a storage heavy node of Nutanix that can be on the same site or a different remote site. With 5.0, this is possible with the single Nutanix node having ~40TB of raw capacity and act as a destination for backup/snapshot data.


### AHV – Hypervisor Enhancements

AHV, the native hypervisor solution from Nutanix, continues to grow leaps and bounds with several customers standardizing on AHV for all workloads. We have continued to add newer capabilities with every release of the product. 5.0 is no different and adds a couple of very important capabilities.

![New AHV capabilities over the last few releases](/images/14835400613035.png)

![AHV Adoption over the last several quarters](/images/14835400780807.png)


**AHV Affinity Rules:** Workloads such as Microsoft SQL or Oracle are often attached to a specific node for licensing, security or HW configuration related reasons. With affinity rules, virtual machines can now be “pinned” to a specific host or a set of hosts. Additionally AHV will also support VM VM anti-affinity rules to try ensure that specific VMs are never on the same host together.

**Acropolis Dynamic Scheduling (ADS):** AHV has supported intelligent initial placement for a while now to make sure VMs are placed on the most optimal hosts when they are initially deployed. With ADS, the hypervisor can detect CPU, memory and storage controller hotspots and can move deployed VMs to a host that is ideal suited. Legacy hypervisor solutions factor in CPU and memory alone while making similar decisions. But with AHV, the VM placement algorithms will also factor in storage resources as well as storage controller bottlenecks before making a decision.

**CPU/Memory Hot Add:** With this capability, administrators can add vCPU and memory to a running VM without any service impact. As applications evolve, it is important to dynamically adjust resources assigned to them so that there is no performance impact for the end user. This is what the hot add feature will enable. In the 5.0 release, this feature will be available in Tech preview and is expected to be generally available in a subsequent release.

With these capabilities, AHV is ready for all your production workloads and there is very little reason as to why any virtualized workload cannot be run on Nutanix and on AHV. Nutanix customers are already standardizing on AHV and are seeing significant savings in the overall cost of ownership across their entire infrastructure stack.

### Prism – Management Plane Enhancements

Over the last year Prism has evolved into a product suite of its own – with Prism Starter and Prism Pro, customers now have an option of choosing a one-click infrastructure management solution or a one-click infra management and operations management solution based on their needs.

![5.0 brings enhancements to both Prism Starter and Prism Pro.](/img/14835402328470.png)


**Prism Self-Service:** Self-service will bring the goodness of AWS to enterprise datacenters. With this new capability, end-users can login to Prism with their own AD credentials and deploy and monitor applications whenever they want, based on Admin set policies. This removes common friction around developers and end users having to rely on IT admins for common tasks. Instead, administrators just assign resources for specific users or AD groups and end users have complete independence to perform actions that he/she is allowed to do. Here is a quick blog that summarizes this capability.

**Network Visualization:** This is another key capability that is part of Prism. With Network Visualization, administrators will be able to get an end-to-end operational view of the infrastructure all the way down to the networking layer. With views that provide insight into how virtual machines are connected to the host, NICs, the top of rack switches, the VLANs they are part of as well as the health of these connections, administrators will be able to get all the information they want about their infrastructure in a single screen, without having to rely on separate tools. This will help isolating and fixing common networking issues that result in application downtimes.

**ESXi Management:** The simplicity of VM management with Prism will extend to ESXi as well with this release – common VM operations that customers relied on vCenter for will be performed from within Prism. One of the common asks from customers was to not go back and forth to vCenter and instead consolidate all operations on Prism. In the first release as part of 5.0, Prism will enable administrators to perform common VM operations such as VM create, update, delete, clone etc. from within Prism. Combining VM operations and the rich monitoring and analytics, vCenter is only needed for less common maintenance and configuration tasks. With the hypervisor becoming commodity, end users get greater simplicity at the management layer.

**Just-in-time Capacity Forecasting (available in Prism Pro):** This is probably one of the most important additions to Prism. Just-in-time forecasting will enable IT to stay ahead of the game by modeling and understanding infrastructure needs based on application requirements even before applications are deployed. This way, IT not only understands application-centric capacity usage patterns and what can be done to optimize existing capacity, they can also plan their infrastructure needs for the future and deploy infrastructure if and only when they need them at “byte” sized granularity all based on recommendations from Prism.

**Search Enhancements (Available in Prism Pro):** One of the core aspects to delivering a personalized and consumer-grade management experience is to enable administrators to perform actions the same way they would do it in their personal lives. Prism Search, a Google like search engine, was introduced earlier this year so that administrators can perform all administrative actions through a simple search query. With support for Boolean expressions, saved searches, auto correct, synonyms based search and more, the 5.0 release will take Prism Search to a whole new level. As an example, administrators can type in “vm iops <1500” and quickly see all the VMs across all the sites that have IOPS less than 1500.


有用链接：

* 西瓜哥的微信文章介绍了部分上面的更新 [点这里。](https://mp.weixin.qq.com/s?__biz=MjM5NDQyNDQ0Mw==&mid=2652388531&idx=1&sn=44f49e138cbebe8f1a70cb36e7ebaf89&chksm=bd6b6fa78a1ce6b1a38eac1e4c308fe884c002dec40c7af0c73b6b274302af02f99fa9b5f613&mpshare=1&scene=1&srcid=0104VgmkmVpxE0kSlIgn7V89&key=b43a3af60b96e11efa7e8bf122519516151d18bab4ca2fa3f7cf1902edfb954a06c0633b1df245e14db446d84260e066f2d9ec85061191375b314c56d2d7b962c9727f37051f72a5010ca075676292b8&ascene=0&uin=ODYyMzEyOTQw&devicetype=iMac+MacBookPro13%2C1+OSX+OSX+10.12.2+build(16C67)&version=12010210&nettype=WIFI&fontScale=100&pass_ticket=V632gZ8yDTJQ9PL42foZMyhmNQ%2BjF8QFSkTj2plVSn7%2FT1HC452ubIAxwDppYh%2BA)
* [Acropolis 5.0 release notes](https://portal.nutanix.com/#/page/docs/details?targetId=Release-Notes-Acr-v50:Release-Notes-Acr-v50)
* [Nutanix Cluster Check 3.0 release notes](https://portal.nutanix.com/#/page/docs/details?targetId=Release-Notes-NCC-v3:rel-Release-Notes-NCC-v30.html)
* [Nutanix Cluster Check 3.0 download](https://portal.nutanix.com/#/page/static/supportTools)
* [PRISM Central 5.0 release notes](https://portal.nutanix.com/#/page/docs/details?targetId=Release-Notes-Prism-Central-v50:rel-Release-Notes-Prism-Central-v50.html)


