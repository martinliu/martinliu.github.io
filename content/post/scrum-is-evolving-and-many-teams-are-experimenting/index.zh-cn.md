---
title: "Scrum 正在演变，许多团队正在尝试替代方案"
date: 2025-08-28T10:00:00+08:00
description: Scrum 对许多团队来说仍然很有价值，但近年来，软件公司——从初创企业到科技巨头——一直在尝试新的实践方法，以适应更快的周期和更大的自主权。
categories: 
  - "DevOps"
tags:
  - "Scrum"
  - "敏捷开发"
  - "团队管理"
  - "软件开发"
  - "项目管理"
  - "工程文化"
keywords:
  - "Scrum 替代方案"
  - "敏捷开发"
  - "团队自主性"
  - "持续交付"
  - "看板"
  - "Shape Up"
image: "0_RoRZP60AWsV890oG.jpg"
slug: "scrum-is-evolving-and-many-teams-are-experimenting"
draft: false
---

Scrum 对许多团队而言仍然很有价值，但近年来，从初创公司到大型科技公司（Big Tech）的软件企业一直在尝试新的实践，以适应更快的周期和更高的自主性。本文将重点介绍 10 种现代方法，它们可以补充甚至超越传统的 Scrum。本文揭示了 10 种正在取代 Scrum 的现代方法，并解释了如何在你的 Java 开发团队中实施它们。

Scrum 使用率从 2020 年至 2024 年的下降，以及 Kanban、Shape Up 和持续交付（Continuous Delivery）等替代方法在软件开发团队中的兴起。

## 1. 团队自主性优于流程仪式

一些大型科技公司（Big Tech）正在尝试更自主的模型——即使是小型团队也可以尝试其中的一些元素，赋能的工程师比流程驱动的团队能交付更好的结果。虽然 Scrum 强调明确的角色，但一些团队正在尝试更高的自主性，赋予工程师对其代码、部署和决策的端到端所有权。这种转变通常会提高生产力，并减少代码、部署和决策制定中的流程开销。

核心原则很简单：聘用聪明人，然后让他们自由发挥。当工程师可以选择自己的工具、设定自己的时间表并在准备就绪时进行部署时，生产力会飙升高达 30%。这种方法消除了冲刺规划会议（sprint planning meetings）和故事点估算（story point estimation）的开销。

Java 实施示例（任何人都能懂的伪代码）：

```Java
// Autonomous team deployment pipeline
@Component
public class AutonomousDeployment {
    
    @Autowired
    private GitRepository repo;
    
    @Autowired
    private CIService continuousIntegration;
    
    // Engineers trigger deployments directly
    public void deployWhenReady(String featureBranch) {
        if (continuousIntegration.allTestsPass(featureBranch)) {
            repo.mergeToMain(featureBranch);
            deployToProduction();
        }
    }
    
    private void deployToProduction() {
        // Automated deployment without ceremony
        System.out.println("Deploying autonomously - no approval needed");
    }
}
```

## 2. 持续交付而非冲刺发布

许多 Scrum 团队以 2-4 周的周期进行交付。持续交付（Continuous Delivery）扩展了这一理念，实现了每天多次发布，提供了更快的反馈和更小、更安全的变更。持续交付消除了冲刺（sprint）边界的人为限制，并实现了用户的实时反馈。

Amazon 平均每 11.7 秒部署一次代码。这种方法降低了风险，因为每次更改都更小，更容易调试（debug）。如果出现问题，你只需回滚（roll back）一个小的更改，而不是解开一个复杂冲刺所累积的功能。

Java 持续交付（CD）流水线示例（任何人都能懂的伪代码）：

```Java
@RestController
public class FeatureFlagController {
    
    @Autowired
    private FeatureToggleService toggleService;
    
    // Deploy features behind flags - no sprint waiting
    @GetMapping("/api/new-feature")
    public ResponseEntity<?> getNewFeature() {
        if (toggleService.isEnabled("new-checkout-flow")) {
            return ResponseEntity.ok(new EnhancedCheckout());
        }
        return ResponseEntity.ok(new StandardCheckout());
    }
}
```

对比展示了大型科技公司（Big Tech）如何与传统 Scrum 驱动的组织不同地进行项目管理，强调自主性、持续交付（Continuous Delivery）和工程师主导的举措。

## 3. Shape Up：Basecamp 的 6 周专注周期

Basecamp 创建了 Shape Up，旨在解决无休止的积压工作 (backlogs) 和范围蔓延 (scope creep) 等挑战。团队不再管理数百张工单（bug修复或者线上支持），而是专注于一个重要问题整整 6 周，然后进行为期 2 周的冷却期 (cooldown)。

其中一个出色的洞察是“投入预设 (appetite setting)”——即预先决定一个问题值得投入多少时间。如果你无法在 6 周内解决它，那么要么缩减范围，要么放弃它。这消除了困扰 Scrum 团队的无休止的范围谈判。

Shape Up 的 Java 项目结构（任何人都能懂的伪代码）：

```Java
// Six-week focused development approach
public class ShapeUpProject {
    
    private final int CYCLE_WEEKS = 6;
    private final LocalDate startDate;
    private final String appetite; // "6 weeks max"
    private final Problem problemToSolve;
    
    public ShapeUpProject(Problem problem, String timeAppetite) {
        this.problemToSolve = problem;
        this.appetite = timeAppetite;
        this.startDate = LocalDate.now();
    }
    
    // Circuit breaker - kill if scope grows too large
    public boolean shouldContinue() {
        return ChronoUnit.WEEKS.between(startDate, LocalDate.now()) < CYCLE_WEEKS;
    }
}
```

## 4. 看板 (Kanban)：可视流优于冲刺规划

Netflix、Microsoft 和许多其他公司都采用了看板 (Kanban) 流系统。与基于冲刺 (sprint) 的规划不同，看板强调限制在制品 (Work In Progress, WIP) 并优化流系统。团队不再承诺冲刺目标，而是专注于限制在制品并优化其价值交付流。

看板的强大之处在于其简洁性。你有三列：待办 (To Do)、进行中 (Doing)、已完成 (Done)。你对“进行中”状态的项目数量设定限制。这可以防止上下文切换 (context switching)，并帮助团队更快地完成工作，而不是启动更多工作。

看板板实现：

```Java
Traditional Scrum Board:
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │   BACKLOG    │  │    SPRINT    │  │     DONE     │
    │              │  │   COMMITTED  │  │              │
    │ • 200 items  │  │  • 15 items  │  │  • 12 items  │
    │ • Endless    │  │  • Fixed     │  │              │
    │ • Groomed    │  │  • Estimated │  │              │
    └──────────────┘  └──────────────┘  └──────────────┘
    
    Modern Kanban Flow:
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │   TODO       │  │   DOING      │  │     DONE     │
    │              │  │  (WIP: 3)    │  │              │
    │ • Just Next  │  │  • Item A    │  │  • Feature X │
    │ • Priority   │  │  • Item B    │  │  • Bug Fix Y │
    │ • Ready      │  │  • Item C    │  │              │
    └──────────────┘  └──────────────┘  └──────────────┘
```

## 5. 无估算 (No Estimates) 运动：关注流，而非预测

一些团队正在尝试 NoEstimates (无估算) 运动，从故事点 (story points) 转向。他们将工作分解成大小相似的块并跟踪流，这可以减少估算开销。团队不再争论一个任务是 5 个点还是 8 个点，而是专注于将工作分解成大小相似的块并衡量实际流速 (flow rates)。

NoEstimates 方法会问：“我们能在 2-3 天内完成这个任务吗？”如果能，就去做。如果不能，就进一步分解。这完全消除了估算会议，并比传统的故事点提供了更可预测的交付。

NoEstimates 的 Java 实现（任何人都能懂的伪代码）：

```Java
@Entity
public class WorkItem {
    
    private LocalDateTime startTime;
    private LocalDateTime completeTime;
    private boolean isSmallEnough; // Can complete in 2-3 days?
    
    // Track cycle time instead of story points
    public Duration getCycleTime() {
        if (completeTime != null) {
            return Duration.between(startTime, completeTime);
        }
        return Duration.between(startTime, LocalDateTime.now());
    }
    
    // Predictability through consistent sizing
    public boolean isRightSize() {
        return getCycleTime().toDays() <= 3;
    }
}
```

## 6. OKRs 加工程领导力

Intel、Google 和 LinkedIn 等公司将目标与关键结果 (Objectives and Key Results, OKRs) 与工程师主导的执行相结合。工程师不再由产品负责人 (product owners) 编写详细需求，而是理解业务目标并找出最佳技术方案。

该模型将开发者视为问题解决者，而非功能生产机器。工程师与客户沟通，理解各项指标，并提出解决方案。这带来了更具创新性的产品和更高的工作满意度。

Java OKR 集成示例（任何人都能懂的伪代码）：

```Java
@Component
public class TeamOKRTracker {
    
    // Objective: Reduce customer checkout abandonment by 20%
    private final ObjectiveMetric checkoutAbandonment = 
        new ObjectiveMetric("checkout_abandonment", 0.20);
    
    // Engineers decide HOW to achieve the objective
    public void implementSolution() {
        if (checkoutAbandonment.isOnTrack()) {
            System.out.println("Current approach working - continue");
        } else {
            // Engineers pivot based on data, not requirements
            tryNewApproach();
        }
    }
}
```

## 7. Spotify 的小队模型：大规模自主团队

Spotify 彻底改变了大型组织保持敏捷性的方式。他们的模型将人员组织成小队 (squads)（团队）、部落 (tribes)（小队的集合）、章节 (chapters)（基于技能的群体）和兴趣组 (guilds)（共同兴趣社区）。

关键洞察在于，文化和自主性比流程更重要。每个小队选择自己的方法论——有些使用 Scrum，有些使用 Kanban，许多采用混合方法。重要的是在使命和价值观上保持一致。

Java 中的小队结构（任何人都能懂的伪代码）：

```Java
// Spotify-style autonomous squad organization
public class AutonomousSquad {
    
    private String mission = "Make checkout delightful";
    private List<Developer> squadMembers;
    private WorkingMethod chosenMethod; // Squad decides!
    
    // Squads have end-to-end responsibility
    public void deliverFeature(Feature feature) {
        design(feature);
        develop(feature);
        test(feature);
        deploy(feature);
        monitor(feature);
    }
    
    // Cross-pollination with other squads
    public void shareLearningSessions() {
        // Guilds facilitate knowledge sharing
    }
}
```

## 8. DevOps 集成：开发与运维合二为一

最成功的公司已经消除了开发和运维团队之间的移交。开发者不再将代码“一扔了之”，而是端到端 (end-to-end) 地拥有他们的应用程序，包括部署、监控和维护。

这种方法消除了“在我机器上可以运行”的问题，因为开发者要对生产环境性能负责。它还能够实现更快的反馈周期，并减少团队之间的推诿扯皮。

DevOps 流水线集成：

```c
Traditional Handoff Model:
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │    DEV    │───►│    QA     │───►│    OPS    │
    │  "Done"   │    │  "Test"   │    │ "Deploy"  │
    └───────────┘    └───────────┘    └───────────┘
         │                │                │
         ▼                ▼                ▼
    Blame Dev        Blame QA        Blame Ops
    
    Modern DevOps Integration:
    ┌─────────────────────────────────────────────────────┐
    │              FULL-STACK OWNERSHIP                  │
    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐│
    │  │ Code    │  │ Test    │  │ Deploy  │  │ Monitor ││
    │  │         │  │         │  │         │  │         ││
    │  └─────────┘  └─────────┘  └─────────┘  └─────────┘│
    │                    Same Team                        │
    └─────────────────────────────────────────────────────┘
```

## 9. 精益开发：消除浪费，最大化价值

源自丰田制造的精益原则在软件开发中焕发了新的活力。其核心思想是消除任何不能直接为客户创造价值的活动。

在实践中，这意味着更少的会议、更少的文档、更短的反馈周期和更快的决策。采用精益方法的团队将更多时间用于编码，更少时间用于仪式性活动。

精益 Java 开发原则（任何人都能懂的伪代码）：

```Java
@Service
public class LeanDevelopmentService {
    
    // Principle 1: Eliminate waste (unnecessary meetings, docs)
    public void eliminateWaste() {
        // No daily standups if async communication works
        // No estimation meetings if flow is predictable
        // No detailed specs if quick prototypes suffice
    }
    
    // Principle 2: Build quality in (automated testing)
    @Test
    public void testDrivenDevelopment() {
        // Write tests first, eliminate manual testing waste
        assertTrue("Quality built into process", true);
    }
    
    // Principle 3: Deliver fast (continuous deployment)
    public void deliverFast() {
        // Small batches, frequent releases
        System.out.println("Value delivered in hours, not sprints");
    }
}
```

## 10. 混合方法：多种方法论的精华

最明智的公司不会只选择一种方法论并永远墨守成规。他们根据特定背景下的有效性，持续试验和调整，结合不同方法的要素。

例如，一个团队可能使用 Shape Up 的六周周期进行功能开发，使用 Kanban 进行 Bug 修复，并采用持续交付 (continuous delivery) 进行部署。关键在于衡量结果并调整流程，以优化成果，而不是墨守方法论。

混合实现示例（任何人都能懂的伪代码）：

```Java
@Component
public class HybridMethodology {
    
    // Use different approaches for different work types
    public void handleWork(WorkType type) {
        switch (type) {
            case FEATURE_DEVELOPMENT:
                useShapeUpCycle(); // 6-week focused cycles
                break;
            case BUG_FIXES:
                useKanbanFlow(); // Continuous flow
                break;
            case EXPERIMENTS:
                useNoEstimates(); // Quick validation
                break;
            case INFRASTRUCTURE:
                useDevOpsPipeline(); // Automated deployment
                break;
        }
    }
}
```

## 未来已来

数据表明 Scrum 不再是唯一的（或绝对主导的）框架——团队正在将其与更新的实践相结合。那些拥抱自主性、持续交付 (Continuous Delivery) 和以结果为导向的方法的团队，始终优于那些过度依赖流程的团队。适应这些新方法的公司将蓬勃发展，而那些根据自身需求调整流程的团队往往能更快地行动并交付更多价值。

不要等待你的组织强制推行变革。今天就开始在你的团队中试验这些方法吧。尝试一个月不进行估算，为你的下一个功能实现持续部署 (Continuous Deployment)，或者让你的开发人员完全拥有其部署流水线 (Deployment Pipeline)。

你会首先尝试什么？在下面的评论中分享你的实验和结果。

将复杂的技术拆解为简单的文字。如果你正在学习，那么我正是为你而写。
