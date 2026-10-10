---
title: "AWS 中国区服务对等性追踪"
slug: aws-china-parity
description: "北京、宁夏与 us-east-1 的逐项实测对照：版本同步、功能面对等、配额边界、定价差异与开发者体验。所有数据来自只读 API 一手实测，持续更新。"
date: 2026-10-10T09:00:00+08:00
lastmod: 2026-10-10T09:00:00+08:00
layout: "page"
menu:
  main:
    weight: 2
    params:
      icon: archives
---

## 引用本页数据

- **数据版本**：2026-10-10（实测日期 2026-10-07 / 10-08）。本页持续更新，引用时请注明数据版本，避免新旧数据混用。
- **复现方法**：本页全部数据来自只读 API 实测、零费用，复现命令见文末「八、复现方法」一节，有中国区账号即可自行验证。
- **Markdown 引用片段**（可直接复制）：

  ```markdown
  AWS 中国区服务对等性追踪（数据版本 2026-10-10），Martin Liu's Blog，
  https://martinliu.cn/aws-china-parity/
  ```

- **HTML 引用片段**（可直接复制）：

  ```html
  <a href="https://martinliu.cn/aws-china-parity/">AWS 中国区服务对等性追踪</a>（AWS 北京/宁夏与 us-east-1 逐项实测，数据日期 2026-10-07/08，Martin Liu's Blog）
  ```

---

> **这一页在回答一个问题**：把架构放到 AWS 中国区（北京 cn-north-1 / 宁夏 cn-northwest-1），
> 到底哪些东西会不一样？
>
> 官方服务目录能告诉你「这个服务在不在」。它不会告诉你「在，但只能用一半」。
> 这一页补的就是后面那半。**本页长期更新**，每次实测追加，不删旧结论，只标注变化。

**数据来源**：只读 API 实测（describe / list / get / query）+ DoH 端点双源交叉验证。
**测试日期**：2026-10-07 至 2026-10-08 ｜ **账号**：中国区 `097279986018`、国际区 `207916078113`
**方法**：全程只读，未创建任何资源，零费用。命令见文末「复现方法」。

---

## 一、结论速览

| 维度 | 对等程度 | 一句话 |
|---|---|---|
| 引擎与组件版本 | 🟢 高 | 18 项抽测，14 项三区完全一致；有代差的只有 Aurora PostgreSQL 与 Amazon MQ |
| 计算与数据库能力 | 🟢 高 | DynamoDB 完全对等；EKS / RDS / DocumentDB / ElastiCache 核心面齐全 |
| 加速实例与 AI | 🔴 低 | GPU 只有 3 种芯片（国际区 9 种）；Bedrock 等一整套 AI 服务**未部署** |
| 配额与治理 | 🟡 中 | 多账号治理（Organizations + Identity Center + SCP）**完整可用**，只是与国际区两套互不相通；配额查询有坑 |
| 成本 | 🟡 中 | 宁夏定价接近美东（部分机型更低），北京普遍贵 20%~50% |
| 开发者体验 | 🟡 中 | CLI 体验一致；无 CloudShell；镜像拉取需自建通道 |

**一句话**：中国区不是「缩水版」，是**边界位置不同**。核心计算、数据库、容器、可观测性体面且定价友好；
AI 服务的天花板由芯片决定。

---

## 二、版本同步：抽测 18 项，14 项完全一致

| 组件 | us-east-1 | 北京 cn-north-1 | 宁夏 cn-northwest-1 |
|---|---|---|---|
| EKS 集群版本 | 1.32 – 1.37 | 完全一致 | 完全一致 |
| EKS vpc-cni addon | 117 个版本 | 117 | 117 |
| RDS MySQL | 对等 | 完全一致 | 完全一致 |
| RDS MariaDB | 对等 | 完全一致 | 完全一致 |
| Aurora MySQL | 35 个版本，最新 3.13.0 | 32 个，最新 **3.13.0（同步）** | 同北京 |
| Aurora PostgreSQL | 46 个版本，最新 18.6 | 40 个，最新 **18.4（落后 2 个小版本）** | 同北京 |
| DocumentDB | 356 个引擎版本 | 318 | 319 |
| OpenSearch | 对等 | 完全一致 | 完全一致 |
| ElastiCache Redis | 6 个版本，最新 7.1 | 同步 | 同步 |
| ElastiCache Valkey | 6 个版本，最新 9.1 | 同步（**2024 年才发布的新引擎也没落下**） | 同步 |
| ElastiCache Memcached | 11 个版本，最新 1.6.6 | 同步 | 同步 |

`eks describe-cluster-versions`、`rds describe-db-engine-versions` 逐区跑出来的结果。

> **结论**：「中国区版本落后」这个说法，在容器与数据库这条线上基本不成立。
> 唯一有实际代差的是 **Aurora PostgreSQL（差 2 个小版本）**。
> 如果你的迁移方案卡在 PG 某个小版本的新特性上，这是唯一需要单独确认的地方。

---

## 三、功能面：目录打了勾，不代表能用

### 3.1 加速实例（GPU）：这是落差最大的一层

| 指标 | us-east-1 | 北京 | 宁夏 |
|---|---|---|---|
| EC2 实例类型总数 | 1,375 | 432 | 461 |
| 加速实例（GPU/加速器）数 | 57 | 19 | 19 |

**中国区有 3 种芯片**：

| 芯片 | 实例族 | 代次 |
|---|---|---|
| NVIDIA T4 | g4dn | 2018 |
| NVIDIA A10G | g5 | 2021 |
| AWS Inferentia | inf1 | 2020 |

**国际区另有 9 种**：T4g(g5g)、L4(g6)、L40S(g6e)、A100(p4d/p4de)、H100(p5)、H200(p5en)、Trainium(trn1/trn1n)。
**整族缺席的共 11 个**：`g5g` `g6` `g6e` `g6f` `inf2` `p4d` `p4de` `p5` `p5en` `trn1` `trn1n`。

两个重要细节：

1. **同族内部规格完全一致** —— g4dn 7/7、g5 8/8、inf1 4/4。
   缩水方式是「整族缺席」，不是「砍规格」。所以选型逻辑很简单：这族在，就是完整的。
2. **中国区目前最大单机是 `g5.48xlarge`**（8×A10G，192 vCPU，768 GB 内存）。
   对照国际区的 `p5`（8×H100 80GB）。**AI 训练的天花板由芯片决定，不由配额决定。**

### 3.2 AI 服务：不是「暂未开通」，是「服务未部署」

DoH 双源交叉验证（`dns.google` + `223.5.5.5`，两者一致才下结论）：

| 服务 | 北京 | 说明 |
|---|---|---|
| Bedrock（控制面 / Runtime） | ❌ 未部署（NXDOMAIN） | 两区均无端点 |
| Amazon Q Business | ❌ 未部署 | |
| Q Developer / CodeWhisperer | ❌ 未部署 | |
| OpenSearch Serverless (aoss) | ❌ 未部署 | |
| Rekognition | ❌ 未部署 | 旧目录清单称在列，端点实测不在 |
| Polly / Textract / Translate | ❌ 未部署 | |
| **SageMaker（API / Runtime）** | ✅ **端点存在** | 自建路线可用 |
| 对照：CodeBuild | ✅ 端点存在 | DevOps 线正常 |

> 注意「未部署」和「暂未开通」是两回事：前者是域名都不解析，后者是控制台里能看到但点不动。
> 对架构决策的含义完全不同：**别等，得换方案**。
> 中国区跑 AI，路线只剩 **SageMaker 自建**一条。

### 3.3 CloudFront（宁夏）

| 能力 | 结果 |
|---|---|
| `list-distributions` | ✅ 可用 |
| CloudFront Functions | ❌ `not supported in this region` |
| Key Value Store | ❌ 不支持 |
| 实时日志（realtime log configs） | ❌ 不支持 |

**宁夏 CloudFront 只保留分发能力**，边缘函数体系整体缺失，Lambda@Edge 随之为不可用。

> ⚠️ 另外一件必须知道的事：**CloudFront 在中国（宁夏）的支持已于 2027-05-31 结束**。
> 这不是功能差异，是服务退出。仍在用 CloudFront 宁夏分发的架构需要迁移规划。

### 3.4 Route 53 与域名

| 能力 | 宁夏 |
|---|---|
| Hosted Zones | ✅ 可用 |
| 健康检查 | ✅ 可用 |
| 流量策略（Traffic Policies） | ❌ `InvalidAction` |
| 域名注册（route53domains） | ❌ 中国区不支持，需第三方注册商 |

### 3.5 可观测性（CloudWatch 家族）

| 子功能 | us-east-1 | 北京 / 宁夏 |
|---|---|---|
| 基础指标 | ✅ | ✅ 对等 |
| Synthetics（拨测 canary） | ✅ | ✅ 对等 |
| Application Signals（SLO） | ✅ | ✅ 对等 |
| **RUM（真实用户监控）** | ✅ | ❌ `Account is not authorized` |
| Evidently（A/B 实验） | ✅ | ⚠️ 待复核（倾向不可用） |

> 核心三件（指标 / 拨测 / SLO）完全对等，SLO 工程可以直接落地中国区。
> **RUM 不可用**是中国区可观测性上最实际的一个缺口 —— 想知道「大陆用户到底多慢」，
> 得自己搭 RUM 链路（这也是我们做中国可达性诊断时会补的第一块数据）。

### 3.6 DynamoDB：完全对等

`list-tables` / `list-backups` / `list-global-tables` 三区全部可用；
账号容量上限读 80,000 / 写 80,000，表容量上限读 40,000 / 写 40,000，**三区数值完全一致**。

> 数据层是搬得最省心的一块。
> 唯一的保留意见：`global-tables` API 可查，**不代表能建跨分区全球表** —— 分区隔离，跨分区同步需自建。

### 3.7 多账号治理：能搭，但两套不通

| 项目 | 国际区 | 中国区 |
|---|---|---|
| Organizations | 可用 | ✅ **可用且已启用**（`o-luixbqu4eu`，SCP 2 条） |
| IAM Identity Center | 可用（0 实例） | ✅ **可用且已启用**（Permission Sets API 可用） |
| Identity Center 端点（门户 / OIDC / 目录） | — | ✅ 全部存在 |
| 跨分区打通 | ❌ 与国际区 org 完全独立 | ❌ 同左 |

> 这是一条**比预期乐观**的发现：中国区内的 Organizations + Identity Center + SCP
> 是**完整可用**的，不是阉割版。出海团队可以在中国区搭一套与国际区平行的多账号治理体系。
>
> 但两套**互不相通**。跨分区账号，得用两套 IAM 体系管，这不是配置问题。

---

## 四、配额：几个必须提前知道的坑

### 4.1 默认值差异

| 配额项 | us-east-1 | 北京 | 宁夏 |
|---|---|---|---|
| EC2 On-Demand Standard vCPU | 32 | **8** | **8** |
| EC2 Spot Standard vCPU | 32 | **8** | **8** |
| Lambda 并发（Console 显示） | 1,000 | 1,000 | 1,000 |
| RDS DB instances | — | **20** | 20 |
| Athena Active DML queries | — | **20** | 20 |
| Lambda 控制面 API 速率 | — | **15 次/秒** | 15 次/秒 |
| CloudFront 每分发可绑 SSL 证书 | — | **1** | 1 |

> **EC2 按需 vCPU 默认只有 8**，这是新账号最容易被绊倒的一项：
> 想跑一个 `g5.12xlarge`（48 vCPU）的 PoC，第一件事是提工单扩容。

> **Lambda 控制面 15 次/秒、Athena 20 并发、CloudFront 单分发 1 张证书**这类「小数字」，
> 对自动化流水线的影响远大于资源类配额。CI/CD 和 BI 团队最容易先撞墙，而且这些多半是
> **不可调**的（只能改架构，没有工单可提）。

### 4.2 一个把「中国区配额不可用」证伪的过程

初测时我们看到 `ListServiceQuotas` 返回 29 项、`GetServiceQuota(L-B99A9384)` 报 `NoSuchResource`，
一度判断「中国区 Lambda 并发配额查不到」。复核后真因是：

- 中国区 service-quotas **API 完全正常**；
- `GetServiceQuota`（applied 层）在**配额未初始化**时查不到该项；
- 换 `GetAWSDefaultServiceQuota`（default 层）立即返回 **1,000**。

**教训**：查配额要**两层都查**（default 兜底 + applied 校验），只看一层会得出错误结论。
写 IaC 配额守卫时按这两层写。

> 顺带记录一个环境陷阱：本机 fake-IP 代理会让 `dig` 对**编造的域名**也返回 `198.18.x.x`。
> 所有端点判断必须以 DoH 双源交叉为准，系统 DNS 不可信。

---

## 五、成本：宁夏比北京便宜，部分机型比美东还低

按需 · Linux · Shared 定价（`pricing get-products`）：

| 实例 | us-east-1 (USD) | 北京 (CNY) | 北京折 USD | 宁夏 (CNY) | 宁夏折 USD | 宁夏 vs 美东 |
|---|---|---|---|---|---|---|
| m5.xlarge | 0.192 | 2.026 | 0.285 **(+48%)** | 1.356 | 0.191 | **-1%** |
| c6i.2xlarge | 0.340 | 2.958 | 0.417 **(+23%)** | 1.972 | 0.278 | **-18%** |
| g4dn.xlarge | 0.526 | 5.223 | 0.736 **(+40%)** | 3.711 | 0.523 | **-1%** |
| g5.12xlarge | 5.672 | 53.641 | 7.556 **(+33%)** | 37.781 | 5.321 | **-6%** |

> **两个反直觉结论**：
> 1. **同一个中国区内部，北京和宁夏差价可以到 30%~45%**。不是「中国区贵」，是「北京贵」。
> 2. **宁夏部分机型比美东还便宜**（c6i.2xlarge 低 18%）。把选型默认值从「北京」改成「宁夏」，
>    是零改造成本的成本优化。

**GPU 全梯度（按需 CNY/小时，北京）**

| 实例 | GPU | 北京 | 宁夏 |
|---|---|---|---|
| g4dn.xlarge | 1×T4 | 5.223 | 3.711 |
| g5.xlarge | 1×A10G | 9.514 | 6.701 |
| g5.2xlarge | 1×A10G | 11.462 | 8.073 |
| g5.12xlarge | 4×A10G | 53.641 | 37.781 |

> ⚠️ **一个存疑点**（未定论，引用前请自行复核）：北京 g5 系列的按小时价与 GPU 数量不成正比 ——
> `g5.12xlarge`（4 GPU，53.64 元）反而高于 `g5.16xlarge`（1 GPU，38.74 元）。
> pricing API 双过滤器复核后仍如此，疑为大规格附加费或数据源延迟。
> 大额采购前建议用控制台定价计算器三重确认。

---

## 六、开发者体验

| 项 | 情况 |
|---|---|
| `docs.amazonaws.cn` | 中国区专属文档站，独立于 global docs |
| AWS CLI 双 profile | 同机 `default`(中国区) 与 `global`(us-east-1) 并存无冲突，endpoint 差异对 CLI 透明 |
| 从大陆直连中国区服务 | 无网络问题 |
| **CloudShell** | ❌ 中国区无对应端点（多候选域名 NXDOMAIN） |
| 域名注册 | ❌ 不支持，需第三方注册商 + ICP 备案 |
| 容器镜像拉取 | Docker Hub / GitHub / K8s 官方源在大陆节点基本不可达；需自建镜像仓库或代理回源 |
| GitHub | 基本可用，中小仓库克隆时间可接受，可在境内自行构建 |

> 对 DevOps 团队最实际的一条：**镜像通道要提前设计**。
> 这不是中国区 AWS 的限制，是大陆网络的现实，但它会直接决定你的 CI/CD 能不能跑起来。

---

## 七、待复核清单（本页不掩盖不确定性）

以下项目尚未定论，**在定论前不要当作事实引用**：

- [ ] Comprehend / Transcribe 端点状态（DoH 空应答，需控制台确认）
- [ ] 北京 g5 系列定价梯度反常（`g5.12xlarge` > `g5.16xlarge`）
- [ ] S3 Tables 中国区功能完整度（API 可达，功能面未验证）
- [ ] Lambda 并发实际默认值（default 层 1,000，applied 层未初始化）
- [ ] `route53domains` 中国区注册功能（端点可达但官方文档明确不支持）
- [ ] SageMaker Notebook 端点（DoH 无记录，与 SageMaker 主端点存在矛盾）
- [ ] Evidently 中国区可用性（倾向不可用）
- [ ] ElastiCache 节点 SKU 差异中缺失的具体型号

---

## 八、复现方法

全部只读，零费用。有中国区账号就能自己跑一遍：

| 测试 | 命令 / API |
|---|---|
| EKS 版本 | `aws eks describe-cluster-versions --region <r>` |
| RDS 引擎 | `aws rds describe-db-engine-versions --engine aurora-mysql --region <r>` |
| 实例广度 | `aws ec2 describe-instance-type-offerings --region <r>` |
| GPU 详情 | `aws ec2 describe-instance-types --instance-types <list>`（读 `GpuInfo`） |
| 配额 | `aws service-quotas list-service-quotas --service-code <svc> --region <r>`<br>`aws service-quotas get-aws-default-service-quota --service-code <svc> --quota-code <code> --region <r>` ← **别漏这一层** |
| 定价 | `aws pricing get-products --service-code AmazonEC2 --filters Type=TERM_MATCH,Field=regionCode,Value=<r> ...`（统一走 us-east-1 端点） |
| 端点存在性 | DoH 双源：`https://dns.google/resolve?name=<host>&type=A` + `https://223.5.5.5/resolve` |

---

## 九、更新记录

| 日期 | 变更 |
|---|---|
| 2026-10-10 | 首版发布。数据基于 2026-10-07 / 10-08 两轮只读实测，覆盖 30+ 服务面、5 个维度。 |

---

实测数据只是起点。真正决定项目成败的往往是下一步：**你的这套架构，具体压在哪条线上**。
如果你的团队正在做中国区选型或迁移评审，可以把架构图发过来，我们按这一页的五个维度逐项过一遍：

{{< china-ready >}}
