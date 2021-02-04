---
author: liuadmin
categories:
- ITIL/ITSM
comments: true
date: 2010-08-09T01:08:31Z
slug: remedy-lb-midtier-server-group-configure
tags:
- ARS
- Atrium
- BMC
- cmdb
- LB
- Mid-tier
- remedy
title: Remedy Server Group及负载均衡配置参考步骤
url: /2010/08/09/remedy-lb-midtier-server-group-configure/
wordpress_id: 50734
---

[![](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2010/08/RemedyITSMArch-253x300.jpg)](http://martinliu.cn/2010/08/remedy-lb-midtier-server-group-configure.html/remedyitsmarch)上图为大型用户环境下Remedy ITSM的部署架构，作为本安装步骤参考模型。所不同的是，如下配置步骤只应用了一个最上面的负载均衡器，每个Web对应连接一个ARS服务器，简化掉了中间放在ARS前的负载均衡器。

**第一步** 安装前的准备工作。
确定Remedy ARS的服务别名，例如“AtriumCMDB”。在所有的Web服务器（Mid-tier所安装的服务器）的host文件中加入一条Ip地址解析，例如：


<blockquote>192.168.10.11   AtriumCMDB</blockquote>


此ARS服务别名指向的是该Web服务器所对应的ARS服务器，例如：Web1中AtriumCMDB对应的ip为ARS1，Web2对应ARS2，Web3对应ARS3，以此类推。

**第二步**安装第一台ARS服务器
默认所有的ARS都安装了数据库客户端程序，如果是Oracle数据库，ARS上的客户端程序的大小版本号必须和远程数据库的大小版本号完全一致。Windows平台的Oracle客户端只支持32位的程序。在所有ARS服务器的host文件中加入一条Ip地址解析，例如：


<blockquote>192.168.10.11   AtriumCMDB</blockquote>


此IP地址为每台ARS自己的对外提供ARS服务的IP。ARS上安装完JDK之后，开始安装ARS，安装过程中服务器别名输入AtriumCMDB，其他的选项都按需要配置，所有有关服务器端组件、服务端口、密码、安装路径的信息都要做详细记录，用来安装Server Group中其他成员使用。安装完第一台服务器的ARS之后，申请Remedy License，打License，包括其他所有CMDB、ITSM相关应用模块的License，打完License后导出成文件备用。ARS安装成功之后，顺序安装其他应用，顺序时CMDB 》ITSM  其他。安装完毕后，通过Remedy User来确认所有应用功能是否正常。

**第三步 **配置第一台ARS服务器为Server Group中的管理服务器
配置方法参照，ARS Configuration Guide中的Server Group的相关章节。配置完毕之后打开Server Group的Log，从启动ARS服务之后，查看该Log看Server Group工作是否正常。

**第四步** 安装Server Group中的成员ARS服务器
准备工作参考第一台ARS服务器。运行ARS安装程序，选择Server Group，选择输入AtriumCMDB别名，选择共享的数据库，其他参数与第一台保持一致。安装完毕之后。使用ARS自带的Sample应用新增一个city，在ARS1上查询ARS2上新增的记录。同样参考的Server Group的相关章节，对ARS2进行配置。在ARS2上查看Server Group的日志，确认该ARS已经加入了以第一台ARS为管理服务器的群集中。为第二台ARS服务器打License。在确认第二台ARS服务器成功加入之后，安装CMDB应用。安装完毕之后，在第二台ARS服务器上，使用Remedy User客户端，打开CMDB的相关表单进行新增和查询操作；然后在ARS1上检查操作结果，保证两边一致。安装ITSM：直接把第一台ARS服务器的ar.cfg文件覆盖到第二台ARS的ar.cfg上，一定要修改第一台ARS服务器主机名的哪一行，把它修改为第二台ARS的主机名。复制第一台ARS的ITSM安装目录到第二台ARS的相同路径中，重启ARS服务。查看arerror.log文件看看ARS启动的是否正常。在第二台ARS上使用Remedy User确认ITSM应用是否工作正常，如果一切工作正常，则第二台ARS服务器安装完毕。按照相同的方式安装其他的ARS服务器。

**第五步** 配置每台ARS的ranking
按照ARS Configuration Guide中的Server Group的相关章节配置每台ARS服务器处理不同后台工作流的ranking。

**第六步** 安装配置所有Web服务器的Remedy Mid-tier
安装Remedy Mid-tier软件，都指向相同的ARS服务别名AtriumCMDB，当然该别名被解析为它所对应的ARS服务器的IP地址。使用浏览器测试每台Web服务器，保证Remedy Mid-tier都能正常工作。

**第七步** 配置F5负载均衡
配置F5的分发策略，按不同ARS服务器的用途，来分别不同的用户请求。考虑管理和接口功能的ARS负担少量的用户交互。开发一个jsp的程序部署在Mid-tier的shared目录中，用它来判断Web所对应的ARS的可用性，以此作为唯一判断条件来分发用户请求给可用的web服务器。
