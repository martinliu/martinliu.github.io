---
title: Game of Cloud 对比三大主流公有云厂商
subtitle: 云之战
date: 2017-09-07
tags: ["cloud"]
bigimg: [{src: "/images/abstract-10.jpg"}]
---

在全球范围内，公有云发展的正如火如荼，对IT行业技术的发展产生了很大的影响，从私有云到公有云，到混合云，再到云原生应用和DevOps。这一连串的连锁，也反映出了最近10年来IT行业发展的主流趋势。

## 各种味道的云计算

参考来源：[Battle of the clouds: Amazon Web Services vs. Microsoft Azure vs. Google Cloud Platform](https://www.networkworld.com/article/3173056/cloud-computing/battle-of-the-clouds-amazon-web-services-vs-microsoft-azure-vs-google-cloud-platform.html?upd=1504859548812) 作者 Brandon Butler, Senior Editor, Network World ，FEB 22, 2017 12:42 PM PT Which flavor of IaaS public cloud has what you need?

![15048603211912](/images/15048603211912.jpg)


对于行业观察者而言Amazon AWS是IaaS公有云市场里，不容争辩的领导者。而Azure正在逐渐缩小与AWS之间的差距，后来者GCP正大踏步的走来。

根据Gartner对云厂商的深度评估，它分析了云厂商对企业工作负载的满足情况，AWS在最近的三年里，在234项功能对比中，保持着92%的满足度，Azure从75%上升到了88%。GCP也进入到了70%的程度。如下图所示：

Gartner对IaaS厂商的评估
![15048608641706](/images/15048608641706.jpg)


重点看Required这一列的百分比。这些企业级功能被分类为三个级别：

1.     Required 必须具备的；
2.     Preferred 最好能具备的；
3.     Optional：推荐具备的。

### Amazon Web Services

AWS是IaaS公有云市场的缔造者，它在2006年发布了第一项云服务Simple Storage Service - S3；Gartner认为它是最成熟的公有云服务提供商，它的功能从广度和深度上，都能最广泛的，能覆盖各种使用场景。它的优缺点如下图所示：

![15048620083336](/images/15048620083336.jpg)


AWS的优缺点
优点 	缺点
最大和最成熟的公有云IaaS厂商，具有最强大和多样性的功能集合，被Garter称为：最广泛使用场景里的”安全之选“ 	尽管AWS的入门和上手是容易的，它还是需要专业人士的管理和驾驭。由于它的功能性的宽广，这会让用老用于也难于面对多种的实施方案，需要第三方的专业顾问帮忙。
市场里的思想领袖和创新者，不断推出各种IaaS的新特性，例如Lambda无服务计算平台 	对于用户的时间和实施能力而言，AWS有时候创新速度太快了，用户的知识很快就会过时，需要他们持续地更新AWS功能和平台的知识。
AWS的云市场具有最广泛的第三方工具的选择。而且它的顾问和专家的人数也是最多的，他们可以帮助到AWS的用户。 	AWS一直以来都不是追求高价格。用户在每次购买服务的时候都有不同折扣，有时候需要使用第三方的工具帮忙管理成本。

从技术的角度看，AWS持续创新的速度和动力都是非常强大的，服务更新的频率和速度非常快，在某种程度上超过了客户的适应和学习的速度，增加了客户的学习成本。它的SLA的规定有时候过于繁琐的，例如：需要客户的工作负载必须跨两个AZ部署，这会增加客户的成本。刨除以上所有对于客户的挑战，Gartner依然称之为云计算使用的“安全之选”。

### Microsoft Azure

微软Azure逐渐变成了//Application development platform as a service (PaaS)的PaaS平台，其实它可以提供包括IaaS、PaaS和SaaS等广泛的服务。微软Azure最大的优势可能是他广大的企业客户基础。很多客户已经把Office系统迁移到了Office 365 SaaS服务上了，微软继续给用户提供大量的IaaS使用折扣（点卡），鼓励用户上云。

Azure从功能角度看不管是计算、存储，还是数据库和IoT等方面，都与AWS非常的接近和匹配。微软试图通过混合云的策略区别于AWS。因此它提供了Azure Stack私有云方案。

![15048652573559](/images/15048652573559.jpg)


Microsoft Azure的优势和劣势
优点 	缺点
微软在构建Azure全球的数据中心基础设施方面和云功能开发上已经做出了巨大的投资。Gatner说Azure在IaaS公有云方面是”足够好了” 	尽管Aure具有了大多数Gartner企业工作负载所需的功能，这些产品和API在某些情况下还不像它的友商AWS那样的成熟。
微软和几乎所有的大型企业具有长期和稳定的关系，在现有的企业协议EA里提供了非常具有吸引力的Azure的供给。 	与Azure云集成的第三方公司的产品数量有限，相对于AWS，它的专家顾问社区也比较小。
微软Azure提供集成化的IaaS、PaaS和SaaS（Office 365）。Azure是已经多年投资于微软系列产品者的理想的选择。它的混合云的方案是很有吸引力的，包括Hyper-V，Windows Server，Active Direcitory， Visual Studio 和最近的Azure Stack。 	在区域的设计中，Azure和AWS不同，它的Zone的概念和AWS不同，这会让工作负载的备份相对的稍微有点难。尽管在支持开源和非微软技术方面花费了大量的精力，微软公司任然不算是一个开源的领导者，而AWS和Google的云则是开源技术工作负载的一个更中立的选择。

显然Azure最适合运行的是微软类型的工作负载，或者最适用于把已有的微软平台应用跑在公有云中。对于那些企业客户的EA，其中会包含一定数目的Azure点卡，不用可惜，用起来的话，Azure的使用还是比较经济的。

Azure没有AZ的概念可谓是技术上的硬伤，比起AWS，这会导致跨区的备份略显麻烦一点。 业内Azure的专家和顾问还是相对较少。Gartner IaaS Magic Quadrant认为Azure对于大多数企业工作负载而言，已经是 足够用了“good enough”。

### Google Cloud Platform

GCP与Azure类似，开始于PaaS，然后扩展到IaaS。分析师认为它特别适合跑某些使用场景，包括容器、大数据和机器学习。GCP在全球范围的数据中心相对较少。

Google也有类似于Office 365 的办公套件SaaS服务，是G Suite，它的价格策略是，用的人越多，单价越便宜。

GCP还是在发展中的云计算，从功能上讲，根据Gartner的年度评估，GCP仅满足70%的必选功能。技术上的优势在于：Google是开源的大数据（Hadoop、 Spark 等）技术、机器学习技术（Tensorflow）和容器编排技术（Kubernetes），它在开发者社区里从来没有缺少过粉丝，它对技术发展的影响不可小觑，这些影响最终都可以通过吸引用户使用GCP来使Google收益，并把这些技术变现。

![15048666386599](/images/15048666386599.jpg)


Google Cloud Platform

在2016年Google招聘了VMWare的联合创始人Diane Greene，这标志着它计划向企业级能力和市场挺进。
Game of Cloud 公有云的游戏

分析师认为对于大多数云的用户来说，并不是做的“零和游戏”的选择，很多人使用多云的策略。多云管理平台厂商RightScale，对1000个用户的调查分析 可以看出，用户57%的应用在AWS上，34%的应用在Azure上，15%跑在GCP上。85%的 RightScale的用户使用多云的策略，可能是：公有云+私有云；或者公有云A+公有云B+？？。

## 硬碰硬功能对比

### 计算

![15048779648996](/images/15048779648996.png)

AWS 	Azure 	GCP
EC2 云中的虚拟服务器 	Virtual Machines 在几秒钟内预配好 Windows 和 Linux 虚拟机 	Compute Engine: Run VMs on Google's infrastructure
EC2 Container Service/Registry 运行和管理 Docker 容器，容器镜像仓库服务。 	Service Fabric 在 Windows 或 Linux 上开发微服务和安排容器 	Container Engineer: Container cluster, Workloads, Discovery&load balancing, Configuration, storage
Lightsail 启动和管理虚拟专有服务器 	App Service 快速创建适用于 Web 和移动的强大云应用 	Cloud Launcher: Cloud Launcher lets you quickly deploy software on Google Cloud Platform
Elastic Beanstalk 运行和管理 Web 应用 	Cloud Services 创建高度可用且可无限缩放的云应用程序和 API 	App Engine: PaaS for apps and backends
Lambda 运行您的代码以响应事件 	Functions 使用无服务器代码处理事件 	Cloud Functions : Serverless Applications on Google’s Infrastructure
Batch 运行任意规模的批处理作业 	Batch 云规模的作业计划和计算管理 	无专门的服务，Google App Engine provides a Cron service. Using this service for scheduling and Google Cloud Pub/Sub for distributed messaging, you can build an application to reliably schedule tasks across a fleet of Compute Engine instances.
Auto Scaling 自动化弹性扩展 	Virtual Machine Scale Sets 管理并扩展到数千台 Linux 和 Windows 虚拟机 	Instance Groups: managed instance groups can automatically scale the number of instances in the group.

从概念上讲，提供的虚拟机功能是没什么差别的，包括虚拟机的自动化扩容和缩容功能都是类似的。区别在于其他的相关功能上。

AWS在Serverlesss架构方面的Lambda是最领先的，它有最丰富的云市场，能提供最丰富的第三方应用服务，通过Lightsail和云市场都可以一键式启动特定配置的预装应用虚拟机/虚拟机集合。

Azure在发布Winddows客户端应用上是有优势的。在其它功能上基本上可以和AWS对齐。

GCP的明显优势是GEK，K8S如日中天的热度刺激人么对其GKE和GCE的关注和使用。

###全世界数据中心覆盖

#### AWS Location 数据中心在全球的覆盖

AWS Regions and Availability Zones

![15048815252579](/images/15048815252579.png)

https://aws.amazon.com/about-aws/global-infrastructure/


已经开放的区和AZ：
US East
N. Virginia (6), Ohio (3)

US West
N. California (3), Oregon (3)

Asia Pacific
Mumbai (2), Seoul (2), Singapore (2), Sydney (3), Tokyo (3)

Canada
Central (2)

China
Beijing (2)

Europe
Frankfurt (3), Ireland (3), London (2)

South America
São Paulo (3)

AWS GovCloud (US-West) (2)

绿色的圈是要开放的区。

China

France

Hong Kong

Sweden

AWS GovCloud (US-East)


#### Azure Region

https://azure.microsoft.com/en-us/regions/


![15048814480576](/images/15048814480576.png)


蓝色三角的是要开放的区。

#### GCP 的 Cloud Locations

https://cloud.google.com/about/locations/
![15048816324535](/images/15048816324535.png)


蓝色的是要开放的区。

GCP的另外一个卖点是它的全球高速光缆链接的网络。
![15048819181658](/images/15048819181658.png)



### 存储服务

参考来源： https://www.networkworld.com/article/3191520/cloud-computing/deep-dive-on-aws-vs-azure-vs-google-cloud-storage-options.html

#### 块存储对比
![15048819776777](/images/15048819776777.jpg)


#### 对象存储
![15048820049019](/images/15048820049019.jpg)


#### 文件存储
![15048820280796](/images/15048820280796.jpg)


## Game of Clouds
AWS 2017 云市场应用排名

From: https://www.cloudendure.com/blog/aws-cloud-computing-map-game-of-clouds-2017

![Game-of-Clouds-12.07.17](/images/Game-of-Clouds-12.07.17.jpg)


AWS的云市场反映出它强大的第三方伙伴和生态系统。

**Azure Stack**

这是它区别于其它云的功能点，是可以在企业数据中心里部署的私有云IaaS平台。它与Azure公有云遥相呼应，为客户提供了混合云方案。

本地运行 Azure 服务 根据你的需求正确组合云和本地部署来满足业务和技术要求。Azure 基础结构即服务 (IaaS) 传输远优于传统虚拟化。借助虚拟机规模集，新式工作负荷的真正自动扩展可实现快速部署。一致的 Azure 平台即服务 (PaaS) 功能将混合部署选择和可移植性引入云应用程序。因此，可在本地运行完全托管的 PaaS、无服务器计算、分布式微服务体系结构和容器管理。

生成跨混合云环境的新式应用程序 Azure Stack 是 Azure 的扩展，将云计算的敏捷性和快节奏创新引入到本地环境。只有 Azure Stack 才能让你从组织的数据中心提供 Azure 服务，同时适度平衡灵活性和控制程度，实现真正一致性的混合云部署。

利用一致的环境加速开发 无论应用是在 Azure 还是在 Azure Stack 上运行，开发人员都能以相同的方式生成和部署应用程序，从而实现工作效率最大化。一套工具 - 使用相同的应用程序模块、自助服务门户和由 Azure Resource Manager 启用的 API。常规 DevOps — 通过 Jenkins 和 Visual Studio Team Services 体验持续部署和集成，通过 Chef 和 Azure PowerShell DSC 扩展体验自动化。 开源 — 使用 Java、Python、Node.js、PHP、Docker 集成式容器、Mesosphere DC/OS 和 Cloud Foundry 等众多开源技术。


