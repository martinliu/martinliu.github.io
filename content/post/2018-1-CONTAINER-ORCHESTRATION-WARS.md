---
title: "容器编排器之战"
date: 2018-01-12T23:33:32+08:00
draft: false
subtitle: "虽然容器编排器之战已经被K8s终结，可是这篇文章对架构分层的整理和分析还是值得架构师们借鉴的"
categories: ["devops"]
tags: ["container"]
image:  "images/abstract-11.jpg"
slug: "container-orchestration-wars"
---

K8s在2017年底为这场速战速决的站点话上了句号，结果是所有竞争对手都选择了增加对K8s的支持。在各自的编排器框架里内置了K8s。本文是根据Mesosphere公司的大拿Karl KARL ISENBERG在各种大会上分享过多次的一份演讲稿改版的。

## KARL ISENBERG 是谁？

所在公司?

* Mesosphere（当前）
* Pivotal

做过的产品?

* DC/OS
* opensource
* CloudFoundry
* BOSH

联络信息：

* github.com/karlkfi
* twitter.com/karlkfi
* linkedin.com/in/karlkfi
* karl.isenberg.us

## 基础架构的进化

传统的应用架构在逐渐向下面两种架构演变。

### 可扩展的单体应用架构

![Screen Shot 2018-01-12 at 11.42.23 P](images/Screen%20Shot%202018-01-12%20at%2011.42.23%20PM.png)

关键词：

* Online 基于互联网
* Latency Routed 用户访问基于延迟路由
* Multi-Region 多区部署
* Load Balanced 负载均衡接入
* Multi-Zone 多个Zone
* Replicated  应用实例多副本
* Auto-Scaled 容量自动化收缩
* Data Replication  区内数据多副本
* Data Synchronization   跨区数据同步

### 可扩展的微服务架构

![Screen Shot 2018-01-12 at 11.50.47 P](images/Screen%20Shot%202018-01-12%20at%2011.50.47%20PM.png)

上图出处：Wheel of Doom ，来自[A Journey into Microservices by Hailo](https://sudo.hailoapp.com/services/2015/03/09/journey-into-a-microservice-world-part-3/)

### 应用+裸金属服务器

APPLICATION
PROVISIONING
ON
BARE METAL

![Screen Shot 2018-01-12 at 11.54.26 P](images/Screen%20Shot%202018-01-12%20at%2011.54.26%20PM.png)

### 应用+IaaS

APPLICATION
PROVISIONING
ON
VIRTUAL INFRASTRUCTURE
PLATFORM
(IaaS)

> “Ultimately, utility cloud providers have
exposed how difficult it is to properly operate
data centers — and reminded all of us that the
ability to expertly operate infrastructure is
what really fuels the consumption of open
source infrastructure.”
--Brian Stein (Rackspace VP - 2017)

![Screen Shot 2018-01-12 at 11.58.36 P](images/images/Screen%20Shot%202018-01-12%20at%2011.58.36%20PM.png)

### 应用+PaaS/aPaaS+IaaS

APPLICATION
PLATFORM
(PaaS / aPaaS)
ON
INFRASTRUCTURE
PLATFORM
(IaaS)

> “The goal of Cloud Foundry is to put more of the
controls back in the hands of developers so they can
self-provision, so there aren’t a lot of roadblocks in their way. But it gives a lot of guardrails.”
-- Chip Childers (Cloud Foundry Foundation CTO - 2017)
![Screen Shot 2018-01-13 at 12.03.37 A](images/Screen%20Shot%202018-01-13%20at%2012.03.37%20AM.png)

### 容器编排器+IaaS

CONTAINER
ORCHESTRATION
ON
INFRASTRUCTURE
PLATFORM
(IaaS)

> “...traditional “PaaS” roles have now been
taken over by containers… The piece that is
left for PaaS is the part that was always the
most important part of PaaS in the first place,
and that’s the opinionated developer
experience.”
--Brendan Burns (Kubernetes Cofounder - 2017)

![Screen Shot 2018-01-13 at 12.08.37 A](images/Screen%20Shot%202018-01-13%20at%2012.08.37%20AM.png)

### CaaS+IaaS

CONTAINER
PLATFORM
(CaaS)
ON
INFRASTRUCTURE
PLATFORM
(IaaS)
![Screen Shot 2018-01-13 at 12.10.28 A](images/Screen%20Shot%202018-01-13%20at%2012.10.28%20AM.png)

### CaaS+裸金属服务器

CONTAINER
PLATFORM
(CaaS)
ON
BARE METAL

![Screen Shot 2018-01-13 at 12.11.42 A](images/Screen%20Shot%202018-01-13%20at%2012.11.42%20AM.png)

### FaaS+IaaS

FUNCTION
PLATFORM
(FaaS)
ON
INFRASTRUCTURE
PLATFORM
(IaaS)

> “If your PaaS can efficiently start instances in 20ms that run for half a second, then call it serverless.”
--Adrian Cockcroft-(AWS VP - 2016)

![Screen Shot 2018-01-13 at 12.13.46 A](images/Screen%20Shot%202018-01-13%20at%2012.13.46%20AM.png)

### FaaS+CaaS

FUNCTION
PLATFORM
(FaaS)
ON
CONTAINER
PLATFORM
(CaaS)
![Screen Shot 2018-01-13 at 6.43.06 A](images/Screen%20Shot%202018-01-13%20at%206.43.06%20AM.png)

### FaaS+CaaS+IaaS

FUNCTION PLATFORM
(FaaS)
ON
CONTAINER PLATFORM
(CaaS)
ON
INFRASTRUCTURE PLATFORM
(IaaS)

![Screen Shot 2018-01-13 at 6.44.49 A](images/Screen%20Shot%202018-01-13%20at%206.44.49%20AM.png)

## 平台频谱 - PLATFORM SPECTRUM

从左到右，资源的抽象程度不断提高；最左侧的弹性最高，最右侧的速率最高。
![Screen Shot 2018-01-13 at 6.47.36 A](images/Screen%20Shot%202018-01-13%20at%206.47.36%20AM.png)

下图是不同类型里的厂商和软件。
![Screen Shot 2018-01-13 at 6.48.19 A](images/Screen%20Shot%202018-01-13%20at%206.48.19%20AM.png)

## 容器平台层次

容器编排器的层次如下：
![Screen Shot 2018-01-13 at 6.49.36 A](images/Screen%20Shot%202018-01-13%20at%206.49.36%20AM.png)

* User workloads 用户工作负载
* Distributed container management 分布式容器管理
* Local container management 本地容器管理
* Container agnostic infrastructure 容器无关性基础架构

容器平台的层次如下：
![Screen Shot 2018-01-13 at 6.51.23 A](images/Screen%20Shot%202018-01-13%20at%206.51.23%20AM.png)

CONTAINER PLATFORM

* User workloads 用户工作负载
* System management & service enablement  系统管理和服务管理
* Distributed container management 分布式容器管理
* Local container management 本地容器管理
* Container aware infrastructure 容器感知的基础架构
* Container agnostic infrastructure 容器无关的基础架构

分布式操作系统的层次如下：
![Screen Shot 2018-01-13 at 6.52.52 A](images/Screen%20Shot%202018-01-13%20at%206.52.52%20AM.png)

## 容器平台功能点

CONTAINER
PLATFORM
CAPABILITIES

### 运行态的能力

1 容器

* Resource Isolation
* Resource Constraints
* Process Tree
* Environment Isolation
* Shell / Exec

2 镜像

* Build
* Layers
* Download
* Cache
* Publish
* Prune

3 网络

* Container
* Bridge
* Host
* Virtual
* Overlay
* Remote
* User-defined
* Port Mapping

4 数据卷

* Ephemeral
* Host
* Backup / Restore
* Copy In / Out
* Shared

### 编排器的能力

调度

* Placement
* Replication/Scaling
* Readiness Checking
* Resurrection
* Rescheduling
* Rolling Updates
* Collocation
* Daemons
* Cron Jobs

资源管理

* Memory
* CPU
* GPU
* Ephemeral Volumes
* Remote Persistent Volumes
* Local Persistent Volumes
* Ports
* IPs (per container)

服务管理

* Labels
* Groups/Namespaces
* Dependencies
* Load Balancing (L7)
* VIPs (L3/L4 LB)
* DNS
* DNS Proxy
* Secrets
* Config Mgmt

### 运维方面的能力

管理

* GUI
* CLI
* Metrics API
* Logs API
* Events API
* Rolling Upgrades
* Backups & Restores

MULTI-INFRASTRUCTURE

* Multi-cloud
* Multi-zone
* Multi-region
* Hybrid-cloud
* Federation

系统服务

* Auto-Scaling
* Package Management
* Service Catalog
* Service Brokers
* Admin Proxy
* API Gateway

### 平台的能力

容器网络

* Overlay
* Routing
* Network Address Translation (NAT)
* Firewalls
* Access Control Lists
* Quality of Service

容器存储

* Local Volumes
* Remote Volumes
* Block Storage
* File System Storage
* Object Storage

平台数据库

* Lock Service
* Key-Value Database
* Relational Database
* Time Series Database

安全

* User Accounts
* Service Accounts
* System/User Space
* E2E Encryption
* Non-root User Workloads
* Audit Logging
* Public Key Infrastructure
* Certifications

多租户

* User Groups
* Permissions
* RBAC
* ABAC
* Resource Sharing
  * FIFO
  * Fair
  * Quotas
* Branding
* Quality of Service

非功能需求

稳定性

* Performance
* Responsiveness
* Efficiency

可用性

* Fault Tolerance
* Robustness,
* Reliability,
* Resilience,
* Disaster Recovery

灵活性

* Format Support,
* Interoperability,
* Extensibility,
* Container Runtimes

可用度

* Familiarity,
* Maintainability,
* Compatibility,
* Debuggability

可移植性

* Host OS,
* Cloud,
* Bare-Metal,
* Hybrid

安全性

* Encryption Quality,
* Vulnerability Process,
* Fast Patching,
* Backporting

## 容器平台对比

市场里的主要技术厂商如下。
![Screen Shot 2018-01-13 at 6.57.44 A](images/Screen%20Shot%202018-01-13%20at%206.57.44%20AM.png)

其它值得考虑的厂商如下。

![Screen Shot 2018-01-13 at 6.58.36 A](images/Screen%20Shot%202018-01-13%20at%206.58.36%20AM.png)

下面的能力对比的时间点是 06/2017，这个时候K8s是否能胜出还是个悬念。

### 调度

图示说明：

* 绿勾：包含此能力
* 横杠：New/External/Partial/Experimental

![Screen Shot 2018-01-13 at 6.59.42 A](images/Screen%20Shot%202018-01-13%20at%206.59.42%20AM.png)

### 资源管理

![Screen Shot 2018-01-13 at 7.00.38 A](images/Screen%20Shot%202018-01-13%20at%207.00.38%20AM.png)

### 服务管理

![Screen Shot 2018-01-13 at 7.01.16 A](images/Screen%20Shot%202018-01-13%20at%207.01.16%20AM.png)

## 如何选择

### 第一阵营：重量级

KUBERNETES

* Huge community
* Solid API
* Some assembly required
* Multitude of vendors/installers

OPENSHIFT

* Application platform based on Kubernetes
* Always trailing Kubernetes releases
* No assembly required
* Open core, enterprise platform

DC/OS

* Runs native applications (non-Docker)
* Specialized in data services
* Ambitious scope (on-prem AWS)
* No assembly required
* Open core, enterprise platform

DOCKER

* Huge community
* Fast moving API
* Integrated orchestration and runtime
* Recent pivot from runtime to orchestration
* Open core, enterprise platform

### 第二阵营：轻量级

EC2 CONTAINER SERVICE (ECS)

* Hosted-only solution
* Tight integration with AWS services
* Closed platform

RANCHER CATTLE

* Gateway to Kubernetes, Mesos, and Docker
* Open platform, enterprise support

NOMAD

* Provisioner with orchestration features
* Runs native applications (non-Docker)
* Tight integration with Vault and Consul
* Some assembly required
* Open platform, enterprise support

KONTENA

* Simple to set up
* No assembly required
* Open core, enterprise platform

### Karl个人的考察点？

* Which is more important to you: **velocity or flexibility**?
* Do you want an **opinionated** application platform?
* Do you need to support **Big Data** initiatives and pipelines?
* Do you want a **hosted** solution?
* Are you willing to **build out your own integrations**?
* Do you need **on-prem & hybrid** capabilities?
* Do you want to avoid infrastructure **lock-in**?
* Are you already invested in a specific infrastructure?
* Are you already invested in a specific operating system?
* Do you need **federation and multi-region**support?
* Do you want **multi-tenancy** or is multi-instance good enough?
* How important are seamless automated **rolling upgrades**?
* **How many nines** do your customers need?
* How important is reverse compatibility & API **stability**?
* Do you need to support **non-Docker workloads**?
