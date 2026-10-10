---
title: "AWS China Region Parity Tracker"
slug: aws-china-parity
description: "Item-by-item measurements comparing Beijing, Ningxia and us-east-1: version parity, feature gaps, quota limits, pricing and developer experience. All data from hands-on read-only API testing, continuously updated."
date: 2026-10-10T09:00:00+08:00
lastmod: 2026-10-10T09:00:00+08:00
layout: "page"
menu:
  main:
    weight: 2
    params:
      icon: archives
---

## Cite this page

- **Data version**: 2026-10-10 (measured 2026-10-07 / 10-08). This tracker is continuously updated — when citing, always include the data version so readers don't mix old and new numbers.
- **Reproduce it**: every number on this page comes from hands-on, read-only API calls at zero cost. The exact commands are in "How to reproduce" (Section 8) near the end of this page — any China-region account can rerun them.
- **Markdown citation** (copy as-is):

  ```markdown
  AWS China Region Parity Tracker (data version 2026-10-10), Martin Liu's Blog,
  https://martinliu.cn/en/aws-china-parity/
  ```

- **HTML citation** (copy as-is):

  ```html
  <a href="https://martinliu.cn/en/aws-china-parity/">AWS China Region Parity Tracker</a> (item-by-item measurements of AWS Beijing/Ningxia vs us-east-1, data collected 2026-10-07/08, Martin Liu's Blog)
  ```

---

> **The question this page answers**: if you put your architecture in the AWS China Regions
> (Beijing `cn-north-1` / Ningxia `cn-northwest-1`), what actually changes?
>
> The official service catalog tells you *whether* a service exists. It does not tell you
> "it exists, but only half of it works." This page covers that second half.
> **Continuously updated** — new measurements are appended, old conclusions are kept and annotated.

**Source**: hands-on read-only API calls (`describe` / `list` / `get` / `query`) plus dual-source
DoH endpoint verification (both `dns.google` and `223.5.5.5` must agree before a conclusion is drawn).
**Tested**: 2026-10-07 to 2026-10-08 ｜ **Accounts**: China `097279986018`, Global `207916078113`
**Method**: read-only throughout, no resources created, zero cost. Commands in "How to reproduce".

---

## 1. Summary

| Dimension | Parity | In one line |
|---|---|---|
| Engine & component versions | 🟢 High | 14 of 18 sampled items are identical across all three regions |
| Compute & database capability | 🟢 High | DynamoDB is fully at parity; EKS / RDS / DocumentDB / ElastiCache core surfaces are complete |
| Accelerated compute & AI | 🔴 Low | Only 3 GPU chips vs 9 globally; the entire Bedrock family is **not deployed** |
| Quotas & governance | 🟡 Medium | Multi-account governance (Organizations + Identity Center + SCP) **works fully** — but it is a separate instance from Global |
| Cost | 🟡 Medium | Ningxia is near us-east-1 (sometimes cheaper); Beijing runs 20%–50% higher |
| Developer experience | 🟡 Medium | CLI is transparent; no CloudShell; container registry access needs its own path |

**Bottom line**: the China Regions are not a "shrunken version" — the **boundaries sit in different places**.
Core compute, database, container and observability work well and are priced favourably.
AI is capped by silicon, not by quota.

---

## 2. Version parity: 14 of 18 items identical

| Component | us-east-1 | Beijing | Ningxia |
|---|---|---|---|
| EKS cluster versions | 1.32 – 1.37 | identical | identical |
| EKS vpc-cni addon | 117 versions | 117 | 117 |
| RDS MySQL / MariaDB | parity | identical | identical |
| Aurora MySQL | 35 versions, latest 3.13.0 | 32, latest **3.13.0 (in sync)** | same as Beijing |
| Aurora PostgreSQL | 46 versions, latest 18.6 | 40, latest **18.4 (2 minor versions behind)** | same as Beijing |
| DocumentDB | 356 engine versions | 318 | 319 |
| OpenSearch | parity | identical | identical |
| ElastiCache Redis / Valkey / Memcached | latest 7.1 / 9.1 / 1.6.6 | all in sync | all in sync |

Measured with `eks describe-cluster-versions` and `rds describe-db-engine-versions` per region.

> **Conclusion**: "China lags on versions" largely does not hold for containers and databases.
> Valkey — a 2024 engine — is already there. The one real difference is
> **Aurora PostgreSQL (2 minor versions behind)**. If your migration hinges on a specific
> PG minor version, that is the only place worth a dedicated check.

---

## 3. Feature surface: a checkmark does not mean it works

### 3.1 Accelerated instances — the widest gap

| Metric | us-east-1 | Beijing | Ningxia |
|---|---|---|---|
| EC2 instance types | 1,375 | 432 | 461 |
| Accelerated (GPU) instance types | 57 | 19 | 19 |

**China has 3 chips**: NVIDIA T4 (`g4dn`, 2018), NVIDIA A10G (`g5`, 2021), AWS Inferentia (`inf1`, 2020).
**Global has 9**: adds T4g, L4, L40S, A100, H100, H200, Trainium.
**11 whole families are absent**: `g5g` `g6` `g6e` `g6f` `inf2` `p4d` `p4de` `p5` `p5en` `trn1` `trn1n`.

Two details that matter:

1. **Within a family, sizes are complete** — g4dn 7/7, g5 8/8, inf1 4/4.
   The reduction is "whole families missing", not "sizes trimmed". So selection is simple:
   if the family is there, it is complete.
2. **The largest single instance in China is `g5.48xlarge`** (8×A10G, 192 vCPU, 768 GB RAM),
   versus `p5` (8×H100 80GB) globally. **Your AI ceiling is set by silicon, not by quota.**

### 3.2 AI services: "not deployed", not "not yet enabled"

Dual-source DoH verification:

| Service | Beijing | Note |
|---|---|---|
| Bedrock (control plane / Runtime) | ❌ not deployed (NXDOMAIN) | no endpoint in either region |
| Amazon Q Business | ❌ not deployed | |
| Q Developer / CodeWhisperer | ❌ not deployed | |
| OpenSearch Serverless (`aoss`) | ❌ not deployed | |
| Rekognition / Polly / Textract / Translate | ❌ not deployed | |
| **SageMaker (API / Runtime)** | ✅ **endpoint exists** | self-managed route works |
| Control: CodeBuild | ✅ endpoint exists | DevOps tooling is fine |

> "Not deployed" and "not yet enabled" are different things: the former does not even resolve in DNS,
> the latter is visible in the console but greyed out. For architecture decisions the difference is
> decisive: **don't wait, change the plan.** On AWS China, running AI means **SageMaker, self-managed**.

### 3.3 CloudFront (Ningxia)

| Capability | Result |
|---|---|
| `list-distributions` | ✅ available |
| CloudFront Functions | ❌ `not supported in this region` |
| Key Value Store | ❌ not supported |
| Real-time logs | ❌ not supported |

Edge compute is entirely absent, so Lambda@Edge is unavailable by extension.

> ⚠️ Also essential: **CloudFront support in China (Ningxia) ended on 2027-05-31.**
> This is not a feature gap, it is a service exit. Architectures still using CloudFront Ningxia
> need a migration plan.

### 3.4 Route 53 and domains

Hosted zones ✅, health checks ✅, traffic policies ❌ (`InvalidAction`),
domain registration ❌ (use a third-party registrar + ICP filing).

### 3.5 Observability (CloudWatch family)

| Sub-feature | us-east-1 | Beijing / Ningxia |
|---|---|---|
| Metrics | ✅ | ✅ parity |
| Synthetics (canaries) | ✅ | ✅ parity |
| Application Signals (SLO) | ✅ | ✅ parity |
| **RUM** | ✅ | ❌ `Account is not authorized` |
| Evidently (A/B) | ✅ | ⚠️ under review (likely unavailable) |

> The core three (metrics / canaries / SLO) are at full parity — SLO engineering works in China.
> **RUM being unavailable** is the most practical observability gap: if you want to know how slow
> your site really is for mainland users, you have to build the RUM path yourself.

### 3.6 DynamoDB: fully at parity

`list-tables` / `list-backups` / `list-global-tables` all work; account throughput caps
(80,000 read / 80,000 write) and table caps (40,000 / 40,000) are **identical across all three regions**.

> The data layer is the easiest thing to move. One caveat: the `global-tables` API responding
> **does not mean you can build a cross-partition global table** — partitions are isolated,
> so cross-partition replication is yours to build.

### 3.7 Multi-account governance: available, but separate

| Item | Global | China |
|---|---|---|
| Organizations | available | ✅ **available and enabled** (`o-luixbqu4eu`, 2 SCPs) |
| IAM Identity Center | available (0 instances) | ✅ **available and enabled** (Permission Sets API works) |
| Identity Center endpoints (portal / OIDC / directory) | — | ✅ all present |
| Cross-partition link | ❌ fully independent | ❌ same |

> This is **more optimistic than expected**: Organizations + Identity Center + SCP are
> **fully functional** inside the China partition, not a stripped-down version. You can run a
> parallel multi-account governance stack there.
>
> But the two stacks **cannot be joined**. Cross-partition accounts need two IAM systems.
> That is not a configuration problem.

---

## 4. Quotas: the traps worth knowing up front

| Quota | us-east-1 | Beijing | Ningxia |
|---|---|---|---|
| EC2 On-Demand Standard vCPU | 32 | **8** | **8** |
| EC2 Spot Standard vCPU | 32 | **8** | **8** |
| RDS DB instances | — | **20** | 20 |
| Athena Active DML queries | — | **20** | 20 |
| Lambda control-plane API rate | — | **15/sec** | 15/sec |
| SSL certs per CloudFront distribution | — | **1** | 1 |

> **EC2 on-demand vCPU defaults to 8.** This is the first thing that trips up a new account:
> to run even a `g5.12xlarge` (48 vCPU) proof of concept, you must file a quota increase first.

> Small numbers like **Lambda control plane at 15/sec, Athena at 20 concurrent queries, or one
> SSL cert per CloudFront distribution** hurt automation pipelines far more than resource quotas do.
> Most of them are **not adjustable** — there is no ticket to raise, only the architecture to change.

### 4.1 Disproving our own "quotas are unavailable in China" conclusion

Our first pass saw `ListServiceQuotas` return 29 items and `GetServiceQuota(L-B99A9384)` throw
`NoSuchResource`, which looked like "Lambda concurrency quota is invisible in China". The real cause:

- the China `service-quotas` API is **perfectly healthy**;
- `GetServiceQuota` (the *applied* layer) cannot find an item that has **never been initialised**;
- `GetAWSDefaultServiceQuota` (the *default* layer) immediately returned **1,000**.

**Lesson**: query **both layers** (default as the floor, applied as validation). Checking only one
produces wrong conclusions — and if you write IaC quota guards, write them against both.

> Environment trap worth recording: with a fake-IP proxy, `dig` returns `198.18.x.x` even for
> **fabricated domains**. Never trust system DNS for endpoint checks; use dual-source DoH.

---

## 5. Cost: Ningxia beats Beijing, and can beat us-east-1

On-demand, Linux, Shared (`pricing get-products`):

| Instance | us-east-1 (USD) | Beijing (CNY) | Beijing → USD | Ningxia (CNY) | Ningxia → USD | Ningxia vs us-east-1 |
|---|---|---|---|---|---|---|
| m5.xlarge | 0.192 | 2.026 | 0.285 **(+48%)** | 1.356 | 0.191 | **-1%** |
| c6i.2xlarge | 0.340 | 2.958 | 0.417 **(+23%)** | 1.972 | 0.278 | **-18%** |
| g4dn.xlarge | 0.526 | 5.223 | 0.736 **(+40%)** | 3.711 | 0.523 | **-1%** |
| g5.12xlarge | 5.672 | 53.641 | 7.556 **(+33%)** | 37.781 | 5.321 | **-6%** |

> **Two counter-intuitive results**:
> 1. **Within China, Beijing and Ningxia can differ by 30%–45%.** It is not "China is expensive",
>    it is "Beijing is expensive".
> 2. **Ningxia is sometimes cheaper than us-east-1** (c6i.2xlarge is 18% lower).
>    Changing your default region from Beijing to Ningxia is free cost optimisation.

**GPU ladder (on-demand CNY/hour, Beijing)**

| Instance | GPU | Beijing | Ningxia |
|---|---|---|---|
| g4dn.xlarge | 1×T4 | 5.223 | 3.711 |
| g5.xlarge | 1×A10G | 9.514 | 6.701 |
| g5.2xlarge | 1×A10G | 11.462 | 8.073 |
| g5.12xlarge | 4×A10G | 53.641 | 37.781 |

> ⚠️ **An open question** (not resolved — verify before quoting): the Beijing g5 hourly price is not
> proportional to GPU count. `g5.12xlarge` (4 GPUs, CNY 53.64) costs *more* than `g5.16xlarge`
> (1 GPU, CNY 38.74). It survived a double-filtered pricing API check and may be a large-instance
> surcharge or a data-source lag. Confirm with the console pricing calculator before any large purchase.

---

## 6. Developer experience

| Item | Situation |
|---|---|
| `docs.amazonaws.cn` | China-specific documentation, independent of global docs |
| AWS CLI dual profile | `default` (China) and `global` (us-east-1) coexist on one machine; endpoint differences are transparent |
| Direct connectivity from mainland | works |
| **CloudShell** | ❌ no endpoint in China (NXDOMAIN across candidate domains) |
| Domain registration | ❌ not supported; third-party registrar + ICP filing required |
| Container registry pulls | Docker Hub / GitHub / upstream K8s registries are largely unreachable from mainland nodes; build a mirror or proxy |
| GitHub | broadly usable; clones of small/medium repos are acceptable, so you can build in-country |

> The most practical item for DevOps teams: **design your image channel early**.
> It is not an AWS China limitation, it is mainland network reality — and it decides
> whether your CI/CD pipeline runs at all.

---

## 7. Open items (uncertainty is not hidden here)

- [ ] Comprehend / Transcribe endpoint status (empty DoH answers, needs console confirmation)
- [ ] Beijing g5 price ladder anomaly (`g5.12xlarge` > `g5.16xlarge`)
- [ ] S3 Tables completeness in China (API reachable, feature surface unverified)
- [ ] Lambda actual concurrency default (default layer 1,000, applied layer uninitialised)
- [ ] `route53domains` registration in China (endpoint reachable, officially unsupported)
- [ ] SageMaker Notebook endpoint (no DoH record, contradicts the main SageMaker endpoint)
- [ ] Evidently availability in China (leaning unavailable)
- [ ] Which ElastiCache node SKUs are missing vs the 236 available globally

---

## 8. How to reproduce

Everything is read-only and free. Any China account can run this:

| Test | Command / API |
|---|---|
| EKS versions | `aws eks describe-cluster-versions --region <r>` |
| RDS engines | `aws rds describe-db-engine-versions --engine aurora-mysql --region <r>` |
| Instance breadth | `aws ec2 describe-instance-type-offerings --region <r>` |
| GPU detail | `aws ec2 describe-instance-types --instance-types <list>` (read `GpuInfo`) |
| Quotas | `aws service-quotas list-service-quotas --service-code <svc> --region <r>`<br>`aws service-quotas get-aws-default-service-quota --service-code <svc> --quota-code <code> --region <r>` ← **do not skip this layer** |
| Pricing | `aws pricing get-products --service-code AmazonEC2 --filters Type=TERM_MATCH,Field=regionCode,Value=<r> ...` (query via the us-east-1 endpoint) |
| Endpoint existence | Dual DoH: `https://dns.google/resolve?name=<host>&type=A` + `https://223.5.5.5/resolve` |

---

## 9. Changelog

| Date | Change |
|---|---|
| 2026-10-10 | First release. Based on two rounds of read-only measurement (2026-10-07 / 10-08), covering 30+ service surfaces across 5 dimensions. |

---

The measurements are only the starting point. What decides a project is usually the next question:
**where exactly does your architecture sit on these lines?** If your team is evaluating or migrating
to AWS China, send over the architecture and we will walk it against all five dimensions:

{{< china-ready >}}
