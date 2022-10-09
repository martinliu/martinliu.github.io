---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2010-08-09T01:08:31Z
slug: remedy-lb-midtier-server-group-configure
tags:
  - ARS

  - remedy
title: Remedy Server Group及负载均衡配置参考步骤
url: /2010/08/09/remedy-lb-midtier-server-group-configure/
wordpress_id: 50734
---

[![](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2010/08/RemedyITSMArch-253x300.jpg)](http://martinliu.cn/2010/08/remedy-lb-midtier-server-group-configure.html/remedyitsmarch)上图为大型用户环境下 Remedy ITSM 的部署架构，作为本安装步骤参考模型。所不同的是，如下配置步骤只应用了一个最上面的负载均衡器，每个 Web 对应连接一个 ARS 服务器，简化掉了中间放在 ARS 前的负载均衡器。

**第一步** 安装前的准备工作。
确定 Remedy ARS 的服务别名，例如“AtriumCMDB”。在所有的 Web 服务器（Mid-tier 所安装的服务器）的 host 文件中加入一条 Ip 地址解析，例如：

<blockquote>192.168.10.11   AtriumCMDB</blockquote>

此 ARS 服务别名指向的是该 Web 服务器所对应的 ARS 服务器，例如：Web1 中 AtriumCMDB 对应的 ip 为 ARS1，Web2 对应 ARS2，Web3 对应 ARS3，以此类推。

**第二步**安装第一台 ARS 服务器
默认所有的 ARS 都安装了数据库客户端程序，如果是 Oracle 数据库，ARS 上的客户端程序的大小版本号必须和远程数据库的大小版本号完全一致。Windows 平台的 Oracle 客户端只支持 32 位的程序。在所有 ARS 服务器的 host 文件中加入一条 Ip 地址解析，例如：

<blockquote>192.168.10.11   AtriumCMDB</blockquote>

此 IP 地址为每台 ARS 自己的对外提供 ARS 服务的 IP。ARS 上安装完 JDK 之后，开始安装 ARS，安装过程中服务器别名输入 AtriumCMDB，其他的选项都按需要配置，所有有关服务器端组件、服务端口、密码、安装路径的信息都要做详细记录，用来安装 Server Group 中其他成员使用。安装完第一台服务器的 ARS 之后，申请 Remedy License，打 License，包括其他所有 CMDB、ITSM 相关应用模块的 License，打完 License 后导出成文件备用。ARS 安装成功之后，顺序安装其他应用，顺序时 CMDB 》ITSM  其他。安装完毕后，通过 Remedy User 来确认所有应用功能是否正常。

**第三步 **配置第一台 ARS 服务器为 Server Group 中的管理服务器
配置方法参照，ARS Configuration Guide 中的 Server Group 的相关章节。配置完毕之后打开 Server Group 的 Log，从启动 ARS 服务之后，查看该 Log 看 Server Group 工作是否正常。

**第四步** 安装 Server Group 中的成员 ARS 服务器
准备工作参考第一台 ARS 服务器。运行 ARS 安装程序，选择 Server Group，选择输入 AtriumCMDB 别名，选择共享的数据库，其他参数与第一台保持一致。安装完毕之后。使用 ARS 自带的 Sample 应用新增一个 city，在 ARS1 上查询 ARS2 上新增的记录。同样参考的 Server Group 的相关章节，对 ARS2 进行配置。在 ARS2 上查看 Server Group 的日志，确认该 ARS 已经加入了以第一台 ARS 为管理服务器的群集中。为第二台 ARS 服务器打 License。在确认第二台 ARS 服务器成功加入之后，安装 CMDB 应用。安装完毕之后，在第二台 ARS 服务器上，使用 Remedy User 客户端，打开 CMDB 的相关表单进行新增和查询操作；然后在 ARS1 上检查操作结果，保证两边一致。安装 ITSM：直接把第一台 ARS 服务器的 ar.cfg 文件覆盖到第二台 ARS 的 ar.cfg 上，一定要修改第一台 ARS 服务器主机名的哪一行，把它修改为第二台 ARS 的主机名。复制第一台 ARS 的 ITSM 安装目录到第二台 ARS 的相同路径中，重启 ARS 服务。查看 arerror.log 文件看看 ARS 启动的是否正常。在第二台 ARS 上使用 Remedy User 确认 ITSM 应用是否工作正常，如果一切工作正常，则第二台 ARS 服务器安装完毕。按照相同的方式安装其他的 ARS 服务器。

**第五步** 配置每台 ARS 的 ranking
按照 ARS Configuration Guide 中的 Server Group 的相关章节配置每台 ARS 服务器处理不同后台工作流的 ranking。

**第六步** 安装配置所有 Web 服务器的 Remedy Mid-tier
安装 Remedy Mid-tier 软件，都指向相同的 ARS 服务别名 AtriumCMDB，当然该别名被解析为它所对应的 ARS 服务器的 IP 地址。使用浏览器测试每台 Web 服务器，保证 Remedy Mid-tier 都能正常工作。

**第七步** 配置 F5 负载均衡
配置 F5 的分发策略，按不同 ARS 服务器的用途，来分别不同的用户请求。考虑管理和接口功能的 ARS 负担少量的用户交互。开发一个 jsp 的程序部署在 Mid-tier 的 shared 目录中，用它来判断 Web 所对应的 ARS 的可用性，以此作为唯一判断条件来分发用户请求给可用的 web 服务器。
