---
title: "2024 年 Gartner 可观测性平台魔力象限"
date: 2024-08-15T10:04:45+08:00
description:  本文介绍了 2024 年 Gartner 可观测性平台魔力象限，探讨了 AWS、BMC、Chronosphere、Datadog、Dynatrace、Elastic 和 Grafana Labs 等供应商的优势和注意事项。
slug: 2024-Magic-Quadrant-for-Observability-Platforms
image: pexels-pavel-danilyuk-9143804.jpg
categories:
    - SRE
tags:
    - 可观测性
    - Gartner
    - DevOps
comments: true
toc: true

---

可观测性平台通过分析、可视化、自动化以及 AI 技术，将遥测数据转化为可执行的洞察。虽然大多数平台都包括应用性能监控（APM）功能，但仅靠 APM 是不够的。I&O 领导者可以参考此研究，探索相关供应商及解决方案。

## 市场定义与描述

Gartner 将可观测性平台定义为：能够从日志、指标、事件和追踪等多种来源获取遥测数据（运营数据）的产品。它们旨在帮助企业了解应用、服务及基础设施的健康状况、性能表现，及行为趋势。可观测性平台可以通过人工操作或机器智能分析遥测数据，识别影响终端用户体验的系统行为变化，例如服务中断或性能下降。这些平台可以让问题在早期，甚至是预防阶段就得到解决。可观测性解决方案被广泛的应用于 IT 运营/运维、站点稳定性工程师/SRE、云与平台团队、应用开发人员，以及产品负责人。

现代企业高度依赖关键的数字应用和服务，这些应用和服务不仅是创收工具，还直接影响客户体验和企业运营效率。中断、性能下降和不稳定现象都会直接冲击企业的营收、客户满意度及品牌形象。

可观测性平台能帮助企业提升关键应用和服务的可用性、性能和恢复力。成功投资和部署可观测性平台能够避免收入损失，同时加快产品开发周期，改善品牌形象。

以下是可观测性平台解决的一些典型场景或业务问题：

- **IT 运营**：IT 运营团队负责确保生产环境中的应用和服务始终可用、迅速响应且性能卓越，尤其是在高峰期。可观测性平台可以在问题出现时及时发出告警，并帮助团队通过数据分析找到根本原因。
- **平台工程**：平台工程师的工作类似于 IT 运营和软件开发。可观测性平台帮助他们确保生产环境始终达到服务质量目标 (SLO)，同时推动持续的数据驱动改进与平台优化。
- **软件开发**：开发团队将可观测性平台集成到 CI/CD 流水线中，提供新代码部署的快速反馈，加快新功能发布，同时提高产品的恢复力。
- **业务分析**：业务分析师利用可观测性平台分析企业的关键业务指标，例如零售商可能会评估放弃购物车的成本和客户的平均消费金额。

### 必备功能

可观测性平台至少应具备以下基本功能：

- 获取、存储并分析运营遥测数据流，数据来源包括但不限于指标、事件、日志和追踪信息。
- 识别并分析应用、服务或基础设施的行为变化，从而判断是否存在可用性中断、性能下降，或是否对终端用户体验产生了影响。
- 通过提供拓扑依赖关系映射和业务服务之间的关联，为遥测数据增加上下文信息，进一步丰富数据内容。

### 常见功能

可观测性平台通常具备以下功能：

- 监控通过浏览器、移动应用和 API 提供的应用与服务的用户体验。
- 与其他运营管理、服务管理和软件开发技术集成，如 IT 服务管理、配置管理数据库、事件与事故响应管理、编排与自动化及 DevOps 工具。
- 从公有云平台（如 Amazon CloudWatch、Microsoft Azure Monitor 和 Google Cloud Operations）收集遥测数据。
- 支持多种遥测数据类型（如追踪、指标和日志）的交互式分析，帮助深入了解用户与应用行为。
- 借助高级分析与机器学习，提供基于数据的洞察，超越手动查询或分析的能力。
- 自动发现并映射相关的基础设施、网络和应用组件及服务。
- 支持成本管理功能，能够度量和优化应用工作负载成本，或优化可观测性平台的利用率和支出。
- 业务流程与活动监控，例如用户的登录到结账流程、转化率追踪漏斗分析、客户注册或贷款申请的流程。
- 提供应用安全功能，能够识别受监控应用中的已知漏洞，并阻止对这些漏洞的攻击尝试。

## 魔力象限

![图 1: Y24Q3 可观测性平台魔力象限](Figure-1.png)

供应商优势与注意事项分析如下。  

### Amazon Web Services  

Amazon Web Services (AWS) 在此次魔力象限中被归类为挑战者。AWS 的可观测性解决方案包括 Amazon CloudWatch、AWS X-Ray、Amazon Managed Service for Prometheus、Amazon Managed Grafana 和 AWS Distro for OpenTelemetry，支持端到端的 observability 使用场景。这些服务是 AWS Cloud Operations 的一部分，涵盖治理和财务管理。AWS 的业务遍布全球，其客户主要为大型企业，并且 AWS 定期发布和更新产品。

#### 优势

- **应用信号**：AWS 于 2023 年末推出了 CloudWatch Application Signals，这是第一个专注于应用程序监控的 CloudWatch 服务。通过此服务，运维人员可以通过设定服务质量目标 (SLO) 并使用服务视图来管理系统健康和性能，同时对出现的问题进行分类。
- **统一的可观测性平台**：AWS 支持 OpenTelemetry、Prometheus 和 Selenium 等行业标准，提升了跨平台的互操作性。即使没有使用代理，AWS 之外的工作负载也可以通过 Managed Grafana 服务进行监控和可视化。
- **全球影响力**：AWS 在全球范围内扩展迅速，已宣布新增四个地区和 18 个本地区域。Observability 服务全球可用，客户可以根据需求决定如何设置遥测数据在生命周期中的存储策略。

#### 注意事项

- **竞争环境**：尽管 AWS 可观测性工具近年来有所改进，如推出 CloudWatch Application Signals 和 Internet Monitor，但 AWS 也为本研究中的许多供应商提供托管服务，并通过 AWS Marketplace 与其合作。此种合作关系在时间上优先考虑客户选择，但与 AWS 平台的统一性存在矛盾。
- **成本管理**：与 AWS 其他服务类似，observability 按需付费，基于多种消费模式，可能不完全适应所有运营模式或使用场景。
- **服务复杂性**：AWS 提供多达 28 种监控与 observability 服务，尽管这展示了广泛的产品线，但也容易引起客户混淆。改进的文档有助于客户根据实际需求区分 CloudWatch 的功能。

### BMC  

BMC 在本次魔力象限中被归类为利基参与者。其 BMC Helix Operations Management 平台提供了丰富的 ServiceOps 和 observability 功能，涵盖 BMC Helix Discovery 及其他组件。BMC 在 IT 服务管理领域中拥有重要地位，其 BMC Helix ITSM（前称 Remedy）产品以及主机解决方案有着广泛的应用。BMC 的业务覆盖全球主要市场。

#### 优势

- **广泛的客户基础**：作为传统的“四大” IT 运营技术供应商之一，BMC 在大型企业和政府机构中具有重要影响力。这种既有的影响力使 BMC 在向 observability 过渡时具备优势。
- **服务运营集成**：BMC 的可观测性解决方案可以与第三方工具兼容，同时与其自身的 ITSM、发现工具和 CMDB 紧密集成，具有潜在的工具整合优势。
- **故障分析工具**：该平台提供健康时间线和健康评分功能，帮助用户了解应用程序或服务的性能变化，还支持快速检查变化情况。它还具备“情况解释”功能，通过 BMC HelixGPT 等 AI 技术，解释问题可能的根本原因。

#### 注意事项

- **产品组合复杂性**：BMC 的解决方案依赖其众多产品组件，尽管可以单独授权使用，但某些功能仍需依赖自定义仪表板。例如，SLO 功能并非开箱即用。
- **定价不透明**：BMC 未公开其定价，除非是针对政府客户或云市场的定价。这与 observability 行业的趋势不符，客户通常希望在早期获取价格信息以进行成本评估。
- **现有 BMC 环境**：BMC 的大部分客户仍在使用其旧有技术，如 BMC PATROL 和 TrueSight。BMC 已对其产品进行现代化改造，如推出云原生的 Helix 平台，并收购了 Netreo。因此，客户需要明确的升级路径指导，以顺利过渡到新平台。

### Chronosphere  

Chronosphere 在此次魔力象限中被评为领导者。其可观测性平台解决方案包括 Chronosphere Observability Platform 和 Chronosphere Telemetry Pipeline，业务主要集中在美国和 EMEA 地区，客户大多来自北美。

Chronosphere 的创始人在 Uber 工作期间开发了 M3DB 时间序列数据库，如今公司仍在支持这一开源项目。近期，Chronosphere 收购了遥测管道供应商 Calyptia（Fluent Bit 的创建者），并与 CrowdStrike 建立了合作，作为其日志获取和分析产品的基础。

#### 优势

- **遥测数据管理与治理**：Chronosphere 提供一个控制平面，客户可以使用该平台分析遥测数据的使用情况，并在数据收集时制定策略与规则。这使得成本优化和数据治理变得更加高效，这是其他供应商难以提供的功能。
- **依托开源技术**：Chronosphere 支持 Prometheus 风格的指标采集以及 OpenTelemetry，用于收集指标、日志和追踪数据。这为那些不愿继续自行管理 Prometheus 或 Jaeger 环境的组织提供了迁移便利。收购 Calyptia 也带来了 Fluent Bit 这一开源工具，进一步丰富了 Chronosphere 的遥测管道能力。
- **单租户架构**：Chronosphere 为每位客户提供独立的租户环境和专属存储空间。这有效避免了不同客户之间的资源争用，同时提高了数据安全性。

#### 注意事项

- **地理覆盖范围**：尽管 Chronosphere 的服务可以在全球使用，但其平台目前仅托管在美国的公有云区域。这可能会引发某些客户对数据主权的担忧，或在某些地区导致延迟问题。公司计划于 2024 年在 EMEA 地区部署托管服务。
- **数字体验监控功能缺乏**：Chronosphere 目前不提供专门的数字体验监控功能，如合成监控或真实用户监控（RUM）。虽然客户可以将数字体验监控的遥测数据上传至 Chronosphere 进行分析，但这些数据的生成和传输需要客户自行解决。
- **缺少自带代理**：Chronosphere 不包含自带的埋点代理，因此被监控的系统需要以与 Prometheus 或 OpenTelemetry 兼容的方式进行埋点，或使用 Fluent Bit 支持的格式。Chronosphere 也支持从其他供应商的代理获取遥测数据，客户可选择兼容的代理进行使用。

### Datadog  

Datadog 在此次魔力象限中被评为领导者。其 SaaS 平台不仅提供可观测性解决方案，还覆盖云安全领域。Datadog 的业务主要集中在美国和 EMEA 地区，同时在亚太和拉丁美洲市场逐步扩展，服务的客户从初创企业到大型企业。近期，Datadog 对其平台进行了多项改进，包括升级仪表板、笔记本和 Watchdog AI 功能，推出了 Flex Logs、移动应用测试、数据流监控以及动态埋点功能。此外，还推出了事件管理功能，将 Datadog 和其他 可观测性工具中的事件整合到统一视图中进行管理。

#### 优势

- **战略愿景与销售执行力**：Datadog 迅速构建了多项新功能，涵盖 APM、日志管理、数字体验监控（DEM）、安全和软件交付等领域，赢得了许多寻求高端解决方案的企业的青睐。其产品驱动增长（PLG）模式帮助企业在大中小规模的组织中扩大客户基础并提升客户参与度。
- **可视化能力**：Datadog 提供了强大且用户友好的可视化功能，使用户能够在一个界面中查看所有遥测数据，并支持通过小部件轻松定制仪表板。
- **产品发展路线**：Datadog 具备强大的产品发展规划，专注于提升 observability、DevSecOps、自动化修复、软件交付以及遥测数据的治理。其策略是打造一个将所有功能无缝整合在一起的平台。

#### 注意事项

- **定价问题**：虽然 Datadog 在官网上提供了详细的定价信息，但一些客户反映，随着使用量的增长，成本可能迅速上升。为了应对这一问题，Datadog 提供了可配置的遥测数据获取控制，帮助客户在预算范围内管理成本。
- **复杂的业务模式**：随着产品线的扩展，Datadog 目前在其官网上提供 20 个独立的产品模块，每个模块都有独立的定价结构，这可能让客户在理解和谈判价格时感到困惑。为了简化流程，Datadog 已开始推出捆绑产品选项。
- **代理管理功能缺乏**：目前，Datadog 缺乏针对代理群组的管理和自动化部署功能，这给大规模部署带来了一定的复杂性。该公司表示，相关功能正在开发中，并已进入测试阶段。

### Dynatrace  

Dynatrace 在此次魔力象限中被评为领导者。其 observability 和安全平台包含多个模块，包括基础设施与应用可观测性、安全分析与防护、数字体验管理、自动化功能以及业务分析。Dynatrace 的客户遍布全球，尤其集中在拉丁美洲、亚太地区等各大市场，主要为大型企业和科技驱动型公司。Dynatrace 最近收购了开发者工具供应商 Rookout 和安全厂商 Runecast，进一步扩展其产品线。

#### 优势

- **广泛的产品组合**：Dynatrace 提供全面的 observability 和安全解决方案，尤其受到大型企业的青睐。其覆盖范围包括现代架构（如 Kubernetes、容器、云函数）的可观测性，及主机和 SAP 等传统企业解决方案的监控。
- **AI 技术创新**：Dynatrace 对其 Davis AI 引擎进行了重大升级，全面采用 AI 技术进行因果分析和预测建模，并且推出了基于生成式 AI 的智能助手，显著提升了平台的智能化水平。
- **平台的灵活性与扩展性**：Dynatrace 的 AppEngine 和 AutomationEngine 使平台具备更强的扩展能力，用户和第三方开发者可以针对特定行业或业务需求开发定制应用和自动化流程，超越了简单的健康监控和性能分析。

#### 注意事项

- **采购的复杂性**：Dynatrace 于 2023 年引入了新的订阅模式 Dynatrace Platform Subscription（DPS），要求客户承诺年度最低消费额度并使用递减率定价机制。虽然很多客户接受了该模式，并能够使用所有的 Dynatrace 产品，但一些采购部门对最低承诺和新组件的定价模式保持谨慎。
- **日志管理应用的进展缓慢**：尽管 Dynatrace 在 2023 年推出了新机制，能够高效处理大量日志数据，客户对此技术表示出浓厚兴趣，但目前并未出现广泛采用 Dynatrace 进行大规模日志管理的趋势。
- **对中小企业的适应性**：Dynatrace 主要为大型企业设计，虽然通过公有云市场可以降低部分门槛，但中小企业可能因为成本原因，选择将其用于监控最核心的业务系统。

### Elastic  

Elastic 在此次魔力象限中被评为领导者。Elastic Observability 基于广泛使用的 Elastic Search AI 平台（原 Elasticsearch）构建，同时支撑其搜索和安全产品。Elastic Observability 可以通过 SaaS 提供，也可自托管使用。公司总部位于北美，客户主要分布在美洲和 EMEA 地区，并在亚太地区实现了显著增长。Elastic 的未来发展规划包括通过新查询语言和 AI 助手提升分析能力和站点稳定性工程（SRE）效率。

#### 优势

- **深度 AI 集成**：Elastic 在其平台中深度集成了 AI，提供 30 多种机器学习模型、定制模型集成，并配备了基于检索增强生成（RAG）的 AI 助手，增强了传统数据分析能力。
- **开放性与灵活性**：Elastic Observability 源自开源的 Elasticsearch 数据平台，能够在大规模下处理多样化的高基数数据。其开放架构为平台提供了极高的灵活性和可扩展性。
- **多样化的部署选择**：Elastic Observability 支持全球多个区域的部署，涵盖所有主要云服务提供商，并提供自托管选项。这使得它能够满足不同客户的数据主权需求，并符合区域性法规要求，例如美国政府的 FedRAMP 认证。

#### 注意事项

- **市场认知度低**：尽管 Elastic 的搜索和安全产品知名度较高，但其可观测性产品的市场认知度和应用率仍有待提升。公司正在积极推动其可观测性产品的市场销售和推广。
- **学习曲线较陡峭**：作为开源软件，Elastic 可能需要更多的学习和培训时间，尤其是对于计划自托管的组织，需确保有足够的技术能力支持。
- **定价模型复杂**：Elastic 采用基于计算资源的定价模型，与其他厂商的定价模式不同。尽管 Elastic 提供了定价计算器，但在采购、成本评估和预算预测过程中，可能较难进行直观比较。

### Grafana Labs  

Grafana Labs 也是本次魔力象限中的领导者。公司创建于开源项目 Grafana 之上，并推出了诸如 Loki、Tempo、Mimir 等其他开源项目。Grafana Labs 的可观测性平台包括 Grafana Cloud 可视化、指标、日志、配置文件以及机器学习功能，客户遍布全球，主要集中在美洲和 EMEA 地区。

#### 优势

- **全球托管灵活性**：Grafana Cloud 目前在全球 19 个 AWS、Azure 和 GCP 区域托管，使客户能够根据延迟需求和数据主权选择合适的托管位置。
- **持续功能更新**：在过去的 12 个月里，Grafana Labs 显著增强了 Grafana Cloud 的功能，特别是在应用程序监控、SLO 管理和自适应指标方面，这些功能可以帮助企业更有效地管理成本。
- **灵活的数据集成**：Grafana 平台能够连接不同的遥测收集系统，并实现跨系统的数据可视化和告警，避免了数据迁移或存储在 Grafana Cloud 中的需求，极大增强了其组合能力。

#### 注意事项

- **学习曲线较高**：随着功能的不断扩展，掌握 Grafana 平台变得更加复杂，配置可能需要手动编辑 YAML 或 JSON 文件，这对初学者来说具有挑战性。
- **成本预测困难**：新用户可能会发现难以预测在 Grafana Cloud 上的指标支出，尤其是活动系列和每分钟数据点等度量标准并不容易获得。使用免费的 Grafana Cloud 版本可能有助于缓解这一问题。
- **合作竞争关系的复杂性**：Grafana Labs 与其他 observability 供应商之间的合作关系可能会变得复杂，尤其是在其自身业务快速扩展的情况下。尽管与 AWS、Google 和 Microsoft 的合作有助于缓解这一问题，但仍需保持关注。

### Honeycomb

Honeycomb 是本次魔力象限中的远见者。其 observability 服务基于优化的数据存储和查询引擎，专注于探测应用和基础设施中的模式和异常。Honeycomb 作为可观测性平台，支持 APM 使用场景，并以 SaaS 形式提供服务。其客户遍布全球，主要集中在北美和 EMEA 地区。  
最近的更新包括推出了 Kubernetes 监控功能和前端可观测性功能（现阶段为早期访问版本）。

#### 优势

- **Kubernetes 专用工具**：2023 年，Honeycomb 推出了 Kubernetes 监控工具，使 SRE 能够更快速地诊断容器化环境中的问题。
- **高度参与的客户社区**：Honeycomb 与其用户群保持紧密联系，定期举办研讨会，活跃的 Slack 社区以及社交媒体互动，让客户能够直接提供反馈。
- **全球化扩展**：2024 年初，Honeycomb 在欧洲部署了基于 SaaS 的新实例，使客户能够根据数据主权要求选择将 observability 数据存储在美国、欧盟，或同时存储在两者之间。

#### 注意事项

- **企业市场的影响力有限**：虽然 Honeycomb 在云原生和技术驱动型企业中很受欢迎，但在更广泛的企业市场中其影响力相对较小，Gartner 客户较少将其作为可观测性平台的候选供应商。
- **技术导向的聚焦**：Honeycomb 的宣传主要面向技术专家，特别是 SRE 和平台团队，可能忽略了提供商业和客户行为洞察的潜力，而这些内容往往是 I&O 预算持有者更关心的。
- **定价难以预测**：Honeycomb 的定价基于摄取到平台中的事件量，客户难以预测事件数量以及未来 12 个月的增长。

### IBM  

IBM 是本次魔力象限中的远见者。IBM 的 Instana可观测性平台既可以作为 SaaS 提供，也可以通过自托管方式部署，使用单代理架构。其客户主要为中大型企业，集中在北美和西欧。IBM 的监控产品覆盖从主机到现代云架构。IBM 还计划收购基础设施自动化公司 HashiCorp，该公司的 Terraform 产品与许多可观测性平台都有集成。

#### 优势

- **精确的遥测数据**：Instana 以每秒级别的精度收集指标，并在三秒内生成通知，这为提升可用性和确保服务质量目标 (SLO) 达成提供了支持。
- **简单的定价模式**：IBM Instana 采用按主机计费的简单定价模式，在市场中具备竞争力。
- **AI 集成优势**：Instana 提供自动化 observability，利用 AI 生成洞察并辅助决策。IBM 最近推出了 watsonx 和 Concert，这些生成式 AI 技术将进一步扩展 Instana 的智能化功能。

#### 注意事项

- **有限的安全功能**：Instana 的安全功能较为有限，更多依赖 IBM 其他产品提供这方面的支持。虽然 Gartner 认为安全功能是可选的，但客户需要根据需求决定是否需要集成安全解决方案。
- **市场认知度不足**：IBM Instana 在市场中的知名度较低，很多现有的 IBM 客户甚至不知道这一产品的存在，即使他们正在寻找可观测性解决方案。虽然 IBM 为使用其传统 IT 工具的客户提供了升级到 Instana 的路径，但很多客户对此并不知情。
- **日志摄取的限制**：目前 Instana 的日志摄取仅限于应用日志和容器化环境。扩展到更广泛的环境是其 2024 年的发展计划之一。

### LogicMonitor

LogicMonitor 是本次魔力象限中的远见者。其 LM Envision 平台从混合基础设施监控发展为可观测性解决方案。LogicMonitor 提供无代理的 SaaS 平台，涵盖基础设施、网络、SD-WAN、云和应用监控，并具备 AI 功能。客户主要来自美洲和 EMEA，且在亚太地区业务不断扩展。过去一年内，LogicMonitor 发布了多项新工具，包括 Edwin AI（用于事件摄取与关联）、生成式 AI 聊天机器人 LM Copilot 以及用于云成本管理的 LM 成本优化。

#### 优势

- **高扩展性**：LogicMonitor 使用无代理收集器来监控资源，这些收集器可根据服务器容量和数据需求进行自动负载均衡，确保高数据处理能力，并支持故障切换。其平台提供 99.9% 的可用性 SLA，确保监控始终可用。
- **容器支持广泛**：LogicMonitor 对 Kubernetes 容器环境提供了强大的支持，无需修改容器代码即可进行监控。
- **简单定价**：LogicMonitor 的定价模式简洁明了，适用于各种规模的企业，尤其适合托管服务提供商（MSP）模式下的企业。

#### 注意事项

- **observability 功能有限**：尽管 LogicMonitor 近年来有所投资，但它仍然主要专注于基础设施和网络监控，缺乏数字体验监控和威胁检测等功能，与同行相比存在差距。
- **仪表板和用户界面**：尽管提供了多种监控模板，但 LogicMonitor 的用户界面在市场上相对落后，操作时需要多次点击才能深入分析数据和获取上下文信息。公司正在发布新界面，预计将有所改善。
- **市场影响力**：尽管投入了大量市场宣传，但 LogicMonitor 在市场上的认知度仍然有限，特别是在 observability 领域的扩展上，客户认知度仍需提升。

### Logz.io

Logz.io 作为远见者，基于开源技术提供其 Open 360可观测性平台，涵盖应用、Kubernetes 和基础设施监控，支持日志管理和云安全信息及事件管理（SIEM）。Logz.io 的客户多为开源技术友好的中小型企业，主要分布在美洲和 EMEA 地区。其未来规划包括进一步利用生成式 AI 增强平台能力，并引入业务导向功能，如 SLO 管理。

#### 优势

- **成本优化**：Logz.io 专注于降低 observability 成本，其数据优化中心提供强大的遥测成本管理功能，如数据过滤、分层存储、追踪采样等。
- **从开源到企业的无缝衔接**：对于已经使用开源监控工具的企业，Logz.io 提供了快速实现企业级 observability 的路径。
- **全球化业务**：Logz.io 的 Open 360 平台在全球多个 SaaS 实例上运行，支持多语言并符合区域性数据安全法规，客户遍布全球。

#### 注意事项

- **缺乏前端监控**：Logz.io 主要专注于通过开源技术收集后台遥测数据，但在前端用户监控和会话回放等功能方面支持不足。
- **技术导向过强**：Logz.io 平台过于关注技术细节，缺少业务监控和漏斗分析等更贴合商业需求的功能。
- **市场知名度不足**：尽管 Logz.io 的客户基础在增长，但主要集中在中小型企业，与其他供应商相比，其市场可见度较低，较少出现在客户的候选名单中。

### Microsoft  

Microsoft 在此次魔力象限中被评为挑战者。其 Azure Monitor 是一款原生的 Azure 可观测性平台，专注于中大型企业。公司业务遍布全球。除了引入生成式 AI 功能外，Microsoft 的未来计划还包括一种低成本的日志存储机制和基于服务组的应用建模。

#### 优势

- **AI 集成**：Microsoft 与 OpenAI 的合作带来了生成式 AI 能力，如通过 Copilot 接口集成到 Azure Monitor 中。Kusto Query Language (KQL) 也支持机器学习，并可以创建处理日志数据的机器学习流水线。
- **Prometheus 支持**：Azure Monitor 引入了 Prometheus 托管服务，支持从 Azure Kubernetes Service (AKS) 等服务摄取数据，利用 PromQL 进行分析，并通过 Grafana 实现可视化和告警功能。
- **安全监控集成**：Microsoft 的 Sentinel 和 Defender 产品与 Azure Monitor 无缝集成，提供跨运营和安全功能的统一分析和事件响应能力。

#### 注意事项

- **SLO 管理缺乏**：Azure Monitor 尚未提供直接的 SLO 管理功能，相关功能预计在 2024 年推出。当前的 SLO 管理流程相对繁琐。
- **OpenTelemetry 支持延迟**：尽管 Azure Monitor 可以摄取 OpenTelemetry 数据，但尚不支持直接通过收集器接口处理 OpenTelemetry Protocol (OTLP) 数据。相关功能在 2024 年进入公测。
- **Prometheus 兼容性问题**：Azure Monitor 对 Prometheus 的支持目前与开源版本存在一些不兼容问题。

### New Relic  

New Relic 在此次魔力象限中被评为领导者。其可观测性平台以 SaaS 形式提供，涵盖 APM、AI 监控、数字体验、基础设施监控、日志管理和安全功能。客户主要为中大型企业，遍布美洲、EMEA 和亚太地区。最近，New Relic 在日志存储优化、AI 监控和应用安全方面进行了增强，并在 2023 年 11 月被 Francisco Partners 和 TPG 收购。

#### 优势

- **灵活的定价**：New Relic 提供基于摄取量和用户数量的定价模式，以及新的基于计算量的定价，客户可以根据使用量灵活调整成本。
- **AI 监控**：New Relic 的 AI 监控功能使工程师能够监控 AI 模型的性能，并比较大语言模型（LLM）的成本和效率。
- **统一的数据平台**：New Relic 的遥测数据平台 (TDP) 专为高效管理遥测数据而优化，支持高基数数据，并原生支持 OpenTelemetry。

#### 注意事项

- **实施复杂性**：一些客户反映，初始设置和配置过程较为复杂，特别是对于不熟悉该平台的用户。
- **地理覆盖有限**：New Relic 的服务交付平台主要位于美国和 EMEA，特别是依赖 AWS 托管的 SaaS 平台。亚太地区的企业可能需要确保其服务符合区域性要求。
- **收购影响**：New Relic 被收购后，客户对其产品路线图和稳定性有所关注。公司表示已加大平台创新投资，但未来发展仍有待观察。

### Oracle

Oracle 在本次魔力象限中被评为利基参与者。其 Oracle Cloud Observability and Management (O&M) 平台支持混合和多云环境中的应用、日志、基础设施和数据库监控，尤其侧重于 Oracle Cloud Infrastructure (OCI) 和企业应用。Oracle 客户遍布全球，涵盖各行业的中大型企业，包括政府机构。未来，Oracle 计划进一步提升 O&M 为 SRE 团队的体验，集成 ITSM，并专注于日志管理和分析。

#### 优势

- **全球覆盖**：Oracle 拥有全球化的业务，支持多种语言，并符合区域性法规要求。通过欧盟主权云、FedRAMP 认证以及 OCI 专用区域，Oracle 提供了符合数据主权要求的解决方案。
- **全面的 Oracle 集成**：Oracle 的 O&M 不仅适用于 OCI，还支持 E-Business Suite 和 PeopleSoft 等应用，客户可以使用定制仪表板和自动化监控，提升用户体验。
- **多云支持**：Oracle 一直致力于提供支持多云环境的 O&M 解决方案，不局限于自家生态，适应多云工作负载的需求。

#### 注意事项

- **市场认知度较低**：虽然 Oracle 将 O&M 定位为多云解决方案，但该产品在现有客户群之外的认知度较低，较少出现在 Gartner 的客户咨询中。
- **生成式 AI 发展较慢**：虽然大多数供应商在 2023 年都引入了生成式 AI，Oracle 在这方面的进展较为缓慢，目前相关功能仍在开发中。
- **缺乏业务导向功能**：尽管支持 Apdex 评分，O&M 尚未引入全面的 SLO 管理或错误预算管理功能，难以完全满足 SRE 团队的需求。

### ServiceNow

ServiceNow 是本次魔力象限中的远见者。其可观测性平台包括 Cloud Observability（原 Lightstep）以及 IT 运营管理 (ITOM) 和 IT 服务管理 (ITSM) 功能。ServiceNow 客户遍布全球，涵盖各行业，其产品路线图侧重于全面引入生成式 AI 功能。

#### 优势

- **支持 OpenTelemetry**：ServiceNow Cloud Observability 从设计上就支持 OpenTelemetry 数据的摄取和分析，包括基于 Open Agent 管理协议 (OpAmp) 的收集器管理功能。
- **强劲的市场影响力**：ServiceNow 在企业市场中拥有稳固的基础，特别是在大型企业中，其 ITSM 产品的广泛应用使其能够推动 Cloud Observability 的使用。
- **全面的产品组合**：Cloud Observability 正逐步与 ServiceNow 的 ITOM 和 ITSM 产品整合，成为 ServiceNow 客户寻求可观测性平台的一个自然选择。

#### 注意事项

- **认知度不足**：Gartner 的客户反馈表明，许多企业对 ServiceNow 的 Cloud可观测性解决方案并不熟悉，市场推广力度不及专注于 observability 的供应商。
- **产品组合复杂性**：Cloud Observability 与 ServiceNow 的其他产品组合并行但独立存在，功能如 SLO 管理属于 ITOM，需要额外购买，增加了复杂性。
- **路线图缺乏创新**：与市场领导者相比，ServiceNow 在 Cloud Observability 上的创新较少，未来发展方向较为保守。

### Splunk  

Splunk 在本次魔力象限中被评为领导者。其可观测性平台包括 Splunk Platform、Splunk IT Service Intelligence 和 Splunk Observability Cloud。Splunk 的客户主要为全球的大型企业。2024 年 3 月 18 日，Cisco 完成了对 Splunk 的收购，并将 AppDynamics 整合到 Splunk 的可观测性产品中。本报告中的参考信息收集于收购完成之前，因此仍然使用 Splunk 的名称。

#### 优势

- **支持 OpenTelemetry**：Splunk 强大的 OpenTelemetry 支持使其在可观测性平台中表现出色，提供对 Linux、Windows 和 Kubernetes 的全方位支持。
- **SLO 管理功能**：Splunk Observability 提供了便捷的工作流，帮助客户通过 UI 或自动化工具如 Terraform 管理 SLO，还支持 SLO 消耗率分析告警。
- **一体化解决方案**：Splunk 通过紧密集成的可观测性平台，能够无缝地支持 IT 运营、工程和网络安全领域的多种使用场景。

#### 注意事项

- **收购带来的不确定性**：Cisco 收购 Splunk 后，产品线整合尚未完成，未来销售流程可能存在不确定性。
- **地理覆盖差异**：Splunk Cloud 的覆盖范围大于 Splunk Observability Cloud，前者在北美、EMEA 和亚太地区有更广泛的分布。对于有严格数据主权要求的客户，需详细检查其具体位置。
- **定价复杂**：Splunk 的定价模式较为复杂，可能会给客户带来预测成本的难题，特别是在数据摄取和使用量变化较大的情况下。

### Sumo Logic  

Sumo Logic 在此次魔力象限中被评为利基参与者。其可观测性平台专注于提供可用性、性能和安全分析，主要服务于全球中小型企业。Sumo Logic 最近推出了基于 AI 的异常检测和优化功能，客户主要分布在美洲和亚太地区。

#### 优势

- **灵活的定价模式**：Sumo Logic 的定价基于分析而非数据摄取，这意味着客户只需为数据分析付费，而数据摄取成本为 $0。
- **支持 OpenTelemetry**：Sumo Logic 为所有客户提供 OpenTelemetry 支持，简化了遥测数据的收集和分析。
- **全球覆盖**：Sumo Logic 平台在全球多个 AWS 区域可用，支持数据驻留和主权要求。

#### 注意事项

- **日志为中心**：Sumo Logic 主要定位为日志分析工具，尽管支持追踪和指标，但对于需要深入应用监控的企业可能不够全面。
- **市场增速缓慢**：尽管 Sumo Logic 总体收入有所增长，但可观测性平台的收入增长自 2022 年以来几乎停滞不前。
- **缺乏原生合成监控**：Sumo Logic 没有提供原生的合成监控功能，客户需要使用其他工具来实现此功能，尽管它支持与 Catchpoint 的开箱即用集成。

### 添加和删除的供应商  

随着市场变化，我们会不断审查和调整魔力象限的纳入标准。因此，魔力象限中的供应商组合可能会随时间发生变化。一年中出现的供应商在次年消失，并不意味着我们对该供应商的看法发生了改变。这可能反映了市场的变化，进而调整了评估标准，或是供应商自身的重点发生了转移。

#### 新增  

以下供应商符合纳入标准，并被添加至魔力象限：

- BMC
- Chronosphere
- LogicMonitor

#### 删除  

- **Broadcom** 被删除是因为未能达到市场的客户兴趣指标 (CII) 门槛。
- **Cisco** 被删除是因为 Cisco Observability Platform 产品已停用。
- **ManageEngine** 被删除是因为未能达到 CII 门槛。
- **Riverbed** 被删除是因为未能达到 CII 门槛。
- **SolarWinds** 被删除是因为未能满足本次研究的纳入标准。

## 纳入和排除标准  

魔力象限的研究通过识别并分析市场中最具相关性的供应商及其产品，帮助客户了解市场状况。为了支持市场识别，通常我们会选择不超过 20 个最具代表性的供应商进行研究。要符合纳入标准，供应商必须满足以下要求：

### 市场参与标准  

- 截至 2024 年 3 月 14 日，产品或服务必须普遍可用，能够通过常规销售渠道提供给所有客户。
- 供应商必须直接销售可观测性平台，并提供至少一线的客户支持服务，包括产品文档、安装指南和参考示例。
- 供应商应展示清晰的产品路线图和市场策略。

### 性能门槛  

-可观测性平台必须在两个或多个地理区域拥有至少 50 位付费的生产环境客户。
-可观测性平台在最近 12 个月内的年收入至少达到 7500 万美元，或者年收入至少达到 1000 万美元，并且年收入增长率达到 25%。

此外，供应商必须在 Gartner 的客户兴趣指标 (CII) 中位居前列。CII 指标通过反映客户兴趣、供应商互动和客户反馈的加权组合来计算。

### 荣誉提名  

我们正在观察超过 40 家供应商的表现，虽然此次研究重点分析了 17 家供应商，但未被纳入并不意味着它们不具备实力。

- **Observe**：这家公司是最早基于 Snowflake 数据平台构建可观测性平台的供应商之一，在其 2024 年 B 轮融资后表现强劲，尽管未达到此次研究的非功能性要求，但仍是市场中的重要力量。

## 评估标准  

### 执行能力  

Gartner 分析师根据供应商的质量和效率来评估其执行能力。我们评估供应商的过程、系统、方法或程序是否能够使其在市场中保持竞争力、运营高效且富有成效，并能够带来积极的收入增长、客户留存率和声誉。最终，供应商的表现评估将依据其利用自身愿景实现成功的能力。

### 产品  

此标准主要关注供应商在可观测性平台市场中的核心技术竞争力，涵盖当前产品功能、质量和特性。此外，还考虑其产品的可扩展性、稳定性、集成性以及安全特性。

### 整体可行性  

评估供应商整体财务状况及其业务单元的财务健康度，考虑盈利能力、收入来源的地理分布以及研发投入。

### 销售执行/定价  

评估供应商在市场中的销售表现，重点关注其定价模式的透明度、价值以及复杂性。还包括对定价与折扣、新老客户业务以及与竞争对手的动态对比。

### 市场响应能力  

衡量供应商根据客户需求变化和市场动态调整策略的灵活性，评估其应对竞争和响应客户反馈的能力。

### 市场执行  

评估供应商的市场推广活动，关注其传递信息的清晰度、质量、创意和效果，以及其品牌影响力、产品知名度和客户认同感的提升。

### 客户体验  

重点评估客户通过供应商产品和服务实现预期结果的体验，包括客户支持计划、售后服务和区域内合作伙伴的支持情况。高端客户的特别支持项目也在评估范围内。

### 运营  

衡量供应商实现目标并履行承诺的能力，评估其组织结构、技能和合作关系的质量，特别是其遵守服务级别协议 (SLA) 的表现。还考虑其与云服务提供商的合作以及处理停机事件的能力。

表 1 列出了魔力象限中关于执行能力的具体评估标准。

| 评估标准             | 权重   |
| -------------------- | ------ |
| 客户体验             | 高     |
| 市场响应能力/记录     | 高     |
| 市场推广执行          | 中     |
| 运营                 | 低     |
| 整体可行性            | 中     |
| 产品或服务            | 高     |
| 销售执行/定价         | 中     |

### 愿景的完整性  

Gartner 分析师通过评估供应商对当前市场机会的理解能力，以及其阐述未来市场方向、创新和客户需求的能力来衡量其表现。最终，供应商的愿景展望和其实现未来目标的能力将作为评估依据。

### 市场理解  

此标准衡量供应商对客户需求的把握，以及如何将这些需求转化为产品。具有清晰市场愿景的供应商能够倾听和理解客户需求，并通过其创新推动市场发展。供应商对 observability 领域的深入理解及其与 APM 的区别也是评估的重要因素。

### 营销策略  

评估供应商是否具备清晰的差异化营销信息，以及是否通过社交媒体、广告和客户项目等渠道有效传递这些信息。创新的市场推广策略和真实的差异化也在考量范围内。

### 销售策略  

评估供应商的销售策略是否能够利用直接和间接销售、营销、服务和合作伙伴网络，扩大市场覆盖和客户基础。渠道策略及对购买决策者的理解也是关键考量因素。

### 产品策略  

评估供应商在产品开发和交付上的策略是否满足当前及未来的市场需求，是否具备差异化功能和持续创新的能力。产品路线图的质量及投资优先级也在评估范围内。

### 商业模式  

评估供应商的商业模式是否设计合理且执行有效，能否持续取得成功。考量因素包括对定价模式的预判、业务逻辑以及与开源社区的关系。

### 创新  

评估供应商在新兴技术领域的创新能力，以及对 AI/ML 等新技术的运用，是否能推动产品开发，并与第三方和合作伙伴建立协同效应。

### 地理战略  

评估供应商是否具备针对全球市场的战略，能否通过本地资源、合作伙伴和 SaaS 平台满足各地区的需求。考量因素包括区域员工数量、SaaS 平台位置及地区化市场策略的调整。

本次魔力象限中使用的愿景完整性评估标准列于表 2。

| 评估标准               | 权重   |
| ---------------------- | ------ |
| 市场理解               | 高     |
| 市场策略               | 中     |
| 销售策略               | 中     |
| 产品策略               | 高     |
| 商业模式               | 高     |
| 垂直行业策略           | 未评级 |
| 创新                   | 高     |
| 地理策略               | 中     |

## 象限描述  

### 领导者  

领导者象限中的供应商提供强大的可观测性产品，能够满足市场的广泛需求，并在扩展客户基础方面非常成功。他们拥有广泛的产品组合，提供卓越的分析能力和可见性，且能够与其他 ITOM 技术无缝集成。领导者具备优异的愿景与执行力，能够满足当前和未来市场的需求，同时持续在创新和客户体验方面表现出色。

### 挑战者  

挑战者象限中的供应商通常具备广泛的市场覆盖和大规模的客户部署。他们在执行方面表现强劲，得益于公司整体的销售和品牌影响力。这些供应商通常提供广泛的产品组合，部分供应商可能正处于产品转型阶段，逐步调整其市场焦点。

### 远见者  

远见者象限中的供应商具备创新计划，能够应对市场需求，但其产品组合尚不成熟。他们在执行方面的能力略低，通常在应对市场变化、整合产品功能以及扩大市场份额方面相对较弱。

### 利基参与者  

利基参与者象限中的供应商主要专注于特定市场或垂直领域，或仅满足有限的使用场景需求。由于他们无法在所有核心功能上表现出深度，通常无法满足更广泛市场的需求。纳入该象限并不意味着其在所竞争市场中的价值受到质疑。

### 背景  

**可观测性平台：未来展望**

过去几年里，observability 市场一直在快速发展，竞争激烈，供应商背景和规模各异，开源产品的比例也逐渐增加。虽然产品质量和功能不断提升，但随之而来的成本也在上涨。许多客户开始质疑是否值得为 observability 支付高昂的成本。

IT 运营同样受到了 AI 技术的深刻影响，尤其是在本次魔力象限项目中，这一现象尤为明显。客户常常询问 AI 在 IT 运营中的角色，以及它与 AIOps 的关系。

可观测性平台本质上是数据管理和分析工具，越来越多的工具开始将 AI 技术作为基础功能，包括自适应阈值、异常检测等。AI 在可观测性平台中的作用将继续演进，但 Gartner 鼓励客户根据具体的用例评估产品的适用性，而非仅仅关注特定技术的有无。

市场中的可观测性产品种类繁多，几乎总有一个产品能够满足客户的独特需求。由于魔力象限的篇幅限制，许多优秀的供应商未能被纳入本次研究。如果有任何问题，欢迎联系我们。

## 市场概览  

从 APM（应用性能管理）到可观测性平台的发展，反映了市场的更广泛趋势。随着商业数字化、云的普及以及技术在日常生活中扮演的核心角色，工作负载和遥测数据的复杂性和规模都在不断增长，这对理解系统健康、性能和用户体验的能力提出了更高的要求。

### 市场扩展  

- **现有客户中的扩展**：过去，APM 工具主要用于监控少量关键应用。但随着可观测性平台功能的提升、部署的简化以及价格下降，更多的应用开始使用这些工具。面对经济波动，组织更倾向于选择能够全面覆盖遥测数据的“全栈”解决方案。
- **新行业的扩展**：APM 和 可观测性工具最初多应用于 IT 系统成熟的大型企业。如今，中小企业也逐渐采用这些工具，特别是那些基于开源技术的解决方案，帮助他们更轻松地转向现代可观测性平台。
- **云服务商的竞争**：随着企业在 observability 上的投入增加，云服务商（CSP）也开始推出具备竞争力的原生 可观测性工具，尤其在多平台环境中，它们的吸引力越来越大。

### 未来趋势  

未来几年，可观测性平台市场将继续受到以下趋势的推动：

- **数据整合需求**：用户需要在不切换工具的情况下，整合和分析来自不同源的遥测数据。
- **AI 驱动的自主功能**：随着 AI 的进步，监控工具将逐渐融入自适应阈值、异常检测等自动化功能，甚至具备更高层次的优化能力。
- **网络安全集成**：可观测性平台开始增加网络安全功能，未来可能成为此领域的重要竞争者。
- **AI 和 LLM 监控**：随着 AI 和大语言模型工作负载的部署，可观测性平台将优先支持这些新兴领域。
- **集中式 observability 团队**：越来越多的组织成立专门团队来集中管理 SLO、遥测数据和事故响应。
- **SaaS 和云服务监控**：随着更多关键业务依赖 SaaS 和云服务，可观测性平台供应商将继续扩展对这些领域的支持。
- **并购与整合**：市场的重组仍在继续，未来将有更多并购、产品更新和整合，这将改变供应商格局。

## 证据  

本次研究基于过去 12 个月中超过 1000 次客户互动。此外，我们还结合了来自 Gartner Peer Insights、客户咨询以及公开资料的信息，以补充供应商提供的数据。

### 评估标准定义

#### 执行能力  

- **产品/服务**：评估供应商为市场提供的核心产品和服务，包括当前产品功能、质量、特性、以及是否通过 OEM 协议或合作伙伴提供。
- **整体可行性**：衡量供应商整体的财务健康状况及其业务单元的成功，评估其继续投资、创新和提供产品的能力。
- **销售执行/定价**：评估供应商在销售中的能力，包括交易管理、定价策略、售前支持和销售渠道的整体效率。
- **市场响应能力/记录**：评估供应商根据市场机会、客户需求变化和竞争对手行为的响应能力，以及其在应对市场变化中的灵活性。
- **市场执行**：评估供应商推广其品牌、提升产品知名度和影响客户心智的能力。包括宣传、促销、思想领导力等活动的效果。
- **客户体验**：衡量供应商通过产品和服务帮助客户取得成功的能力，特别是技术支持、客户服务以及服务级别协议等方面的表现。
- **运营**：评估供应商是否具备有效管理和运营其业务的能力，包括组织结构、项目管理、系统和其他运营工具的质量。

#### 愿景完整性  

- **市场理解**：衡量供应商理解客户需求并将其转化为产品和服务的能力，展示出清晰的愿景，并能够通过这些愿景引领市场发展。
- **营销策略**：供应商的营销信息是否清晰、具有差异化，并通过多种渠道有效传达。
- **销售策略**：评估供应商的销售策略是否覆盖全面，包括直接和间接销售渠道的利用，以及市场覆盖的深度和广度。
- **产品策略**：供应商在产品开发和交付中的策略是否能够满足当前和未来的市场需求，并体现差异化。
- **商业模式**：评估供应商的商业模式是否合理且具备可持续性。
- **垂直/行业策略**：供应商在特定市场细分中的资源配置和产品战略。
- **创新**：供应商在新技术、整合和协同创新方面的能力和投资力度。
- **地理战略**：评估供应商是否具备全球扩展的战略，能够根据不同地区的需求调整资源和产品策略。

原文：<https://www.gartner.com/doc/reprints?id=1-2HXS17MG&ct=240627&st=sb>

❤️ Feature Photo by Pavel Danilyuk: <https://www.pexels.com/photo/a-bearded-man-with-a-hat-using-binoculars-9143804/>