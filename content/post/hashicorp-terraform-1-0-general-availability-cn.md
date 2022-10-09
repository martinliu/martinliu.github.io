+++
date = 2021-06-15T09:15:22+08:00
title = "Hashicorp 的 Terraform 1.0 正式 GA 了！"
description = "Hashicorp 公司十年磨一剑的经典产品的下载达到 10 亿次的里程碑"
author = "Martin Liu"
categories = ["DevOps"]
tags = ["hashicorp", "terraform", "ica"]
image = "img/2021/06/0gLZ2oH.png"
+++

Terraform 1.0--现在GA了--标志着你的自动化工作流程的互操作性、易于升级和维护方面的一个重要里程碑。

<!--more-->

Terraform 拥有数以亿计的下载量、成千上万的贡献和令人难以置信的社区，是最广泛采用的基础设施即代码工具。达到 1.0 是一个重要的里程碑。



![Terraform 的历史](https://elasticstack-1300734579.cos.ap-nanjing.myqcloud.com/2021-06-15-terrafor-history.png)

本文来自：https://www.hashicorp.com/blog/announcing-hashicorp-terraform-1-0-general-availability

6 月 8 日，在 HashiConf 欧洲会议上，我们很高兴地宣布HashiCorp Terraform 1.0全面上市，这是您自动化工作流程的互操作性、易于升级和维护的一个重要里程碑。Terraform 1.0[立即可供下载](https://www.terraform.io/downloads.html)，也可在HashiCorp Terraform Cloud 中使用。HashiCorp Terraform已经被大小公司的个人和团队广泛使用，成为多云配置和自动化的标准。这篇文章介绍了新的内容，以及1.0的命名对Terraform用户的意义。



## 更好的 Terraform State 互操作性

Terraform 在互操作性方面取得了巨大的进步。Terraform state 现在可以在0.14.x、0.15.x和1.0.x版本之间交叉兼容。远程状态数据源的兼容性现在已经回传，支持0.12.30、0.13.6、0.14.0、0.15.0和1.0.x版本。

## 改进升级体验

从 Terraform 0.15 开始，一直到1.x的生命周期，你现在可以升级到新的 Terraform 版本，你的工作流程将继续运行，就像之前那些版本一样。使用Terraform 1.x不需要升级工具、重构或其他改变。

## 延长维护期

所有Terraform 1.x版本将有至少18个月的维护期。这意味着HashiCorp将继续调查1.0版本的错误和发布功能，至少在这段时间内。这些修复可能会在后续的1.x版本中发布，而不一定是增量的1.0.x版本。

## Terraform插件SDK v1的寿命结束

[Terraform插件SDK](https://github.com/hashicorp/terraform-plugin-sdk/)是一个框架，可以让开发者创建和维护Terraform供应商。HashiCorp将在2021年7月31日结束对插件SDK第一版的支持。Terraform CLI和Terraform Cloud的用户不受此影响，不需要采取任何行动。我们鼓励受到影响的 Terraform Provider 的维护者使用我们的升级指南，转移到Terraform Plugin SDK的第二版本。按照我们的教程，开发您的Provider。其他信息可以在Terraform提供者社区讨论论坛中找到。Terraform插件SDK v1版的生命终结时间表。

## 1.0版本对Terraform意味着什么？

1.0版本是一个巨大的成就，对于Terraform来说更是如此。对于许多为该项目做出贡献的人或参与超过100,000,000次下载的人来说，这已经是一个漫长的过程。但在HashiCorp，我们以一致的、透明的方式对待产品版本和1.0的指定，基于四个关键要求，正如2017年4月关于Packer 1.0发布的博文中所记录的那样。

达到1.0的第一个要求是产品已经被广泛部署，在生产中经过多年的硬化。Terraform自2014年首次发布以来，一直在配置和管理基础设施，并得到了从零售业（星巴克）到证券交易所（TMX集团、德意志交易所集团）到自动驾驶汽车（Cruise）等广泛行业的信任。

第二个要求是，主要的用例要被理解并得到良好的支持。Mitchell Hashimoto和Armon Dadgar早在2014年创建Terraform时，就已经想到了几个用例。从那时起，超过1500名贡献者开启了超过11000个 PR（GitHub 的贡献方式），这些请求增加了新的功能，并支持新的用例，这是我们从未想象过的。

第三个要求规定了一个明确的用户体验。Terraform用户从不同的角度来处理他们的工作流程，因此我们专注于创建直观的用户界面；清晰的文档；全面的、自定进度的学习平台；以及互动的、由教师指导的研讨会。

第四个要求是确保产品的技术架构是成熟和稳定的。

Terraform 1.0以更大的互操作性、更容易的升级以及重要的维护期来巩固你的自动化工作流程和Terraform功能集的稳定性的形式满足了所有四个要求。

