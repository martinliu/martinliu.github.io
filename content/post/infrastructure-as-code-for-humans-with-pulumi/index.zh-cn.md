---
title: "告别Terraform：使用为人类设计的基础设施即代码Pulumi"
date: 2024-01-08T11:01:38+08:00
description: 正当 Terraform 被 CNCF 切了 Toufu 之后，大家应该考虑一下 Pulumi 了。
slug: infrastructure-as-code-for-humans-with-pulumi
image: 0_94eq9GcVBbFH3TeR.webp
categories:
    - DevOps
tags:
    - iac
    - pulumi
    - terraform
comments: true
toc: true
---

本文原作者：[Santiago González](https://medium.com/aws-tip/say-goodbye-to-terraform-infrastructure-as-code-for-humans-with-pulumi-76e72de1c3d9)

事先声明一下：本文并非另一篇黑HashiCorp更改Terraform许可的文章。我还有很多不再使用Terraform的考虑。在这篇文章中，我们将回顾Pulumi相对于Terraform的一些优势。这并不意味着要成为Pulumi的追捧者。它只是Terraform的替代解决方案之一，使开发人员能够直观地使用基础设施配置工具。

## 为什么讨厌Terraform？

显然，我在这里写的一切都是主观的，也可能是错的。但这里总结的一切表明了，与我类似的其他许多尝试拥抱Terraform的人，希望用它作为IcA工具所遭受的挫折。

* **学习曲线**：Terraform拥有自己专用的领域特定语言（HCL），作为一种定义基础设施的独特方式，与传统编程语言迥然不同。这种语言遵循着对其他语言而言比较陌生的逻辑。因此，对团队来说，学习他是需要：付出极大努力，并且遵循这种... 魔鬼般逻辑的语言更是需要额外的努力。
* **违背DevOps原则的DevOps工具**：如果你在Terraform中编写代码的已经很复杂了，想象一下去编写测试，有可能是什么样子。在这里，您可以了解一下要如何才能做到这一点。这绝对是疯狂的。实际上，这意味着：并非在Terraform的代码上直接实施测试。至少我从来没见过这样的。
* **秘钥管理**：Terraform需要与第三方解决方案集成来实现秘钥的管理。或者，您大可以使用环境变量。
* **团队生产力**：其实很难找到一个开发人员的简历上，就写着他已经熟悉了 Terraform。因此，这意味着：你必须使用一种与项目上所使用的语言相异的语言来实现基础设施的配置，由于使用和学习其他新语言的额外工作量，会导致生产力的下降。

## Pulumi能做什么？

以下是使Pulumi相对于Terraform更好的功能。

```java
import com.pulumi.pulumi;
import com.pulumi.pulumi.aws.ec2;
import com.pulumi.pulumi.aws.rds;
import com.pulumi.pulumi.aws.vpc;

public class Main {
    public static void main(String[] args) {
        // Crear una VPC
        Vpc myVpc = new Vpc("myVpc", VpcArgs.builder()
                .cidrBlock("10.0.0.0/16")
                .build());

        // Crear un grupo de subredes
        SubnetGroup dbSubnetGroup = new SubnetGroup("myDbSubnetGroup", SubnetGroupArgs.builder()
                .subnetIds(myVpc.getPrivateSubnetIds())
                .build());

        // Crear una instancia de AWS DocumentDB
        Cluster documentDbCluster = new Cluster("myDocumentDBCluster", ClusterArgs.builder()
                .clusterIdentifier("my-docdb-cluster")
                .availabilityZones("us-east-1a", "us-east-1b")
                .dbSubnetGroupName(dbSubnetGroup.getId())
                .masterUsername("admin")
                .masterPassword("mysecretpassword")
                .skipFinalSnapshot(true)
                .storageEncrypted(true)
                .applyImmediately(true)
                .engine("docdb")
                .engineVersion("4.0")
                .instanceType("db.r5.large")
                .build());

        pulumi.export("clusterEndpoint", documentDbCluster.getEndpoint());
    }
}
```

### 语言支持

多语言和多云支持：使其具有很大的灵活性。这使您能够使用与软件项目相同的编程语言，让它对开发人员而言更加友好。此外，它实现了对所需架构的更好抽象，并且还能实现“在产生云账单之前就进行代码测试”。

### Pulumi具有秘钥存储

它使用集成的秘钥存储来保护所有敏感数据。这个秘钥存储解决方案在各种部署场景中无缝运行，无论您是使用我们托管的Pulumi服务、自托管的Pulumi服务、还是自我管理的后端。当您使用'pulumi new'或'pulumi stack init'创建堆栈时，Pulumi服务会自动保护好秘钥信息。如果你选择使用AWS S3或Google Cloud Storage等自我管理的云存储后端，也是在使用'pulumi new'初始化新堆栈时定义的口令来保护秘钥。无论场景如何，每个Pulumi堆栈都会收到唯一的加密密钥。

### 团队生产力

如果团队使用了与其项目相关联（相同）的程序开发语言，那么，他们就将更容易的对所需使用的组件负责和提供支持。这样，使用和理解具有HCL结构的项目的工作量就被消除了，团队可以继续专注于开发功能，而减少了开发成本和时间。

### 使用Terraform状态

Pulumi提供了访问和利用本地和远程Terraform状态的能力。在过渡到Pulumi或您组织内的各个团队具有不同的工具偏好时，这可能非常有价值。通过诸如状态引用支持之类的功能，您基于Terraform的构建的基础架构之上，构建Pulumi中的项目，例如利用Terraform所创建的关键VPC详细信息，如VPC ID和子网ID等信息。这简化了Pulumi和Terraform之间的集成，使其从 Terraform 的迁移变成了一个无缝的过程。

### 测试

您可以选择所喜欢的测试框架，并开发进行对基础设施进行必要验证的单元和集成测试。

```java
import spock.lang.Specification
import io.pulumi.pulumi
import io.pulumi.pulumi.aws.s3.Bucket
import io.pulumi.pulumi.runtime.Mocks
import org.mockito.Mockito

class PulumiIntegrationTest extends Specification {

    def setup() {
        // Set up AWS and Pulumi configurations for testing
        pulumi.runtime.setMocks(new Mocks()) // Configure Pulumi mocks
    }

    def cleanup() {
        // Clean up configurations after tests
        pulumi.runtime.setMocks(null) // Restore Pulumi mocks
    }

    def "test AWS S3 bucket creation"() {
        given:
        // Set up the environment for the Pulumi program
        def program = new pulumi.Stack("mystack")

        when:
        // Execute the Pulumi program that creates the S3 bucket
        program.apply()

        then:
        // Verify that the S3 bucket was created successfully
        def bucketName = program.getOutput(Bucket.BucketName)
        assert bucketName != null && bucketName != ""

        cleanup:
        // Perform additional cleanup tasks if necessary
    }
}
```

## TL;DR; 太长不读

尽管Terraform拥有着强大的社区支持，但实际上，对于开发团队来说，通常大家还是觉得太复杂，难以用它实现 IaC 基础设施即代码的管理。这主要是由于学习曲线及其HCL语言，它与命令性语言的逻辑不一致。由于替代解决方案如Pulumi的出现，我们可以使用软件项目中的程序语言配置基础设施资源。实际上，与Terraform相比，Pulumi会提高效率和生产力。如果您尚未决定使用哪种IaC工具，值得 先考虑Terraform可能对您的组织产生的潜在影响。

来源：<https://medium.com/aws-tip/say-goodbye-to-terraform-infrastructure-as-code-for-humans-with-pulumi-76e72de1c3d9>

Feature picture ❤️ :  kike [vega on Unsplash](https://unsplash.com/@kikekiks?utm_source=medium&utm_medium=referral)