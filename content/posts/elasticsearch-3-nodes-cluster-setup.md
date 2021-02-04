---
date: 2020-08-27T13:54:46+08:00
title: "Elasticsearch 3 节点集群搭建 (7.9.0)"
subtitle: "高可靠性 3 节点的 ES 集群适用于各种应用场景"
description: "高可靠性 3 节点的 ES 集群适用于各种应用场景"
categories: "DevOps"
tags: ["DevOps","Elastic Stack","Elasticsearch"]
keywords: ["DevOps","Elastic Stack","Elasticsearch"]
bigimg: [{src: "/images/abstract-6.jpg", desc: "DevOps"}]
---

最近发布的 Elastic Stack 7.9 ，带来了很多新的特性。Elastic Agent 统一集成数据采集代理是一大亮点。另外还看增加了企业搜索、端点安全防护等组件。Ingest Manager 统一 Beat 配置管理功能让我们向 SaaS 风格的监控工具又迈进了一步。由代理端自行注册到后端，在后端统一纳管所有被管理服务器，将是一种以后非常通用的模式。这样做的好处是：将数据采集端点的配置工作量和复杂度降低到最低。Beats 的各种相关独立模块也在平行的发布，这种双轨模式也可以让用户更弹性的做出选择，能最大程度的保持旧版本部署环境管理模式的延续性。 Ingest manager 的前提条件是：后台 ES 需要启用 api key 安全，启用 ES 客户端的 HTTPS 访问。我们也可以看到这两个功能选项也有其非常广泛的应用需求。本文将用最简单的文字，向你描述一套 3 节点的 ES 集群的搭建方式，这套系统的核心特性如下：

* 启用用户名和密码认证
* 启用集群内 es 节点间 transport.ssl 通讯加密
* 启用 es 的 http 客户端 http.ssl 加密通讯
* 安装脚本中包括创建数字证书的必要命令（没猜错的话，大部分人可能会在这一步花费大量时间）


## 演示环境介绍

我使用的是本地的测试环境，环境配置如下：

* Mac OS
* vagrant
* virtualBox  - CentOS 8 
* Elastic Stack 7.9.0
* ip 和主机名分配见 Vagrantfile 文件
* Vagrant 的 vagrant-hostsupdater 插件实现了 Mac OS 主机和所有虚拟机的 host 文件 DNS 解析的同步，保证所有相关虚拟机都可以解析其它虚拟机的 FQDN，尽量模拟生产环境。

本文所使用的所有配置文件和安装脚本见：https://github.com/DevOps-Coach/elasticstack.git


```
➜  elasticstack git:(master) ✗ vagrant up es1 es2 es3
Bringing machine 'es1' up with 'virtualbox' provider...
Bringing machine 'es2' up with 'virtualbox' provider...
Bringing machine 'es3' up with 'virtualbox' provider...
==> es1: Importing base box 'bento/centos-8'...
==> es1: Matching MAC address for NAT networking...
==> es1: Checking if box 'bento/centos-8' version '202002.04.0' is up to date...

省略中间大量输出。。。。。。

    es3: ● elasticsearch.service - Elasticsearch
    es3:    Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; enabled; vendor preset: disabled)
    es3:    Active: active (running) since Thu 2020-08-27 05:55:21 UTC; 223ms ago
    es3:      Docs: https://www.elastic.co
    es3:  Main PID: 4205 (java)
    es3:     Tasks: 41 (limit: 11499)
    es3:    Memory: 1.2G
    es3:    CGroup: /system.slice/elasticsearch.service
    es3:            ├─4205 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=10 -XX:+AlwaysPreTouch -Xss1m -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djna.nosys=true -XX:-OmitStackTraceInFastThrow -XX:+ShowCodeDetailsInExceptionMessages -Dio.netty.noUnsafe=true -Dio.netty.noKeySetOptimization=true -Dio.netty.recycler.maxCapacityPerThread=0 -Dio.netty.allocator.numDirectArenas=0 -Dlog4j.shutdownHookEnabled=false -Dlog4j2.disable.jmx=true -Djava.locale.providers=SPI,COMPAT -Xms1g -Xmx1g -XX:+UseG1GC -XX:G1ReservePercent=25 -XX:InitiatingHeapOccupancyPercent=30 -Djava.io.tmpdir=/tmp/elasticsearch-14730718416313121303 -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/var/lib/elasticsearch -XX:ErrorFile=/var/log/elasticsearch/hs_err_pid%p.log -Xlog:gc*,gc+age=trace,safepoint:file=/var/log/elasticsearch/gc.log:utctime,pid,tags:filecount=32,filesize=64m -XX:MaxDirectMemorySize=536870912 -Des.path.home=/usr/share/elasticsearch -Des.path.conf=/etc/elasticsearch -Des.distribution.flavor=default -Des.distribution.type=rpm -Des.bundled_jdk=true -cp /usr/share/elasticsearch/lib/* org.elasticsearch.bootstrap.Elasticsearch -p /var/run/elasticsearch/elasticsearch.pid --quiet
    es3:            └─4360 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
    es3:
    es3: Aug 27 05:54:54 es3.zenlab.local systemd[1]: Starting Elasticsearch...
    es3: Aug 27 05:55:21 es3.zenlab.local systemd[1]: Started Elasticsearch.
    es3: Provisioning script works good!
    es3: Please access Elasticsearch https://192.168.50.13:9200
```

最后的系统登录验证命令：

```
➜  elasticstack git:(master) ✗ curl --cacert certs/ca/ca.crt -u elastic 'https://es1.zenlab.local:9200/_cat/nodes?v'
Enter host password for user 'elastic':
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
192.168.50.13           26          95   8    0.03    0.31     0.18 dilmrt    -      es3
192.168.50.12           33          95   0    0.01    0.14     0.09 dilmrt    -      es2
192.168.50.11           36          93   1    0.06    0.16     0.12 dilmrt    *      es1
```

以上命令需要输入 elastic 用户的密码，es1 节点初始化了所有 Elasticsearch 内置用户的密码，需要复制 console 中的那一段密码信息备用。

创建以上所有数字证书和秘钥文件的种子文件是 certs/instance.yml ：

```
# instance.yml
instances:
  - name: 'es1'
    ip: ['192.168.50.11']
    dns: [ 'es1.zenlab.local' ]
  - name: "es2"
    ip: ['192.168.50.12']
    dns: [ 'es2.zenlab.local' ]
  - name: 'es3'
    ip: ['192.168.50.13']
    dns: [ 'es3.zenlab.local' ]
  - name: 'es4'
    ip: ['192.168.50.14']
    dns: [ 'es4.zenlab.local' ]
  - name: "es5"
    ip: ['192.168.50.15']
    dns: [ 'es5.zenlab.local' ]
  - name: 'es6'
    ip: ['192.168.50.16']
    dns: [ 'es6.zenlab.local' ]
  - name: 'es7'
    ip: ['192.168.50.17']
    dns: [ 'es1.zenlab.local' ]
  - name: "es8"
    ip: ['192.168.50.18']
    dns: [ 'es2.zenlab.local' ]
  - name: 'es9'
    ip: ['192.168.50.19']
    dns: [ 'es3.zenlab.local' ]
  - name: 'lk'
    ip: ['192.168.50.20']
    dns: [ 'lk.zenlab.local' ]
```

这里一次性生产了所有我这个本地测试环境里可能用到的数字证书文件。

## Elasticsearch 安装脚本

下面是第一个 Elasticsearch 节点的安装脚本和注释，pre-install-es1.sh ：

```
#!/bin/bash
# author: Martin Liu
# url:martinliu.cn

#指定安装的版本
elastic_version='7.9.0'

#开始安装流程
echo "Provisioning a Elasticsearch "$elastic_version" Server..."
sudo date > /etc/vagrant_provisioned_at

#配置 ES 需要的操作系统参数
sudo swapoff -a
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -p
sudo sh -c "echo 'elasticsearch  -  nofile  65535' >> /etc/security/limits.conf"

#设置个性化 SSH 登录提示信息
sudo sh -c "echo '**** --  --  --  --  --  --  --  -- ****' > /etc/motd"
sudo sh -c "echo '**** Welcome to Elastic Stack Labs' >> /etc/motd"
sudo sh -c "echo '**** --  --  --  --  --  --  --  -- ****' >> /etc/motd"
sudo sh -c "echo '*' >> /etc/motd"

#安装 ES 软件包
sudo rpm -ivh /vagrant/rpm/elasticsearch-$elastic_version-x86_64.rpm 

#创建 ES 集群内部通信加密数字证书，提前清理旧的证书文件和目录
sudo rm -f /vagrant/certs/certs.zip
sudo rm -rf /vagrant/certs/es*
sudo rm -rf /vagrant/certs/ca
sudo rm -rf /vagrant/certs/lk
sudo /usr/share/elasticsearch/bin/elasticsearch-certutil cert -in /vagrant/certs/instance.yml  -pem  -out /vagrant/certs/certs.zip -s

#解压缩所有证书备用
sudo /usr/bin/unzip  /vagrant/certs/certs.zip -d /vagrant/certs/

#部署节点需要的秘钥
sudo cp /vagrant/certs/ca/ca.crt  /etc/elasticsearch/
sudo cp /vagrant/certs/es1/* /etc/elasticsearch/


#更新 ES 默认的配置文件
sudo cp /vagrant/es1.yml /etc/elasticsearch/elasticsearch.yml

#配置和启动 ES 系统服务
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
sudo systemctl status elasticsearch

#初始化 ES 服务器内建用户的密码，这些密码需要在控制台上复制保存备用
sudo /usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto -b

#成功顺利的完成了安装
echo Provisioning script works good!
echo Please access Elasticsearch https://192.168.50.11:9200

```

说明：你也可以参考以上脚本手工执行，如果是非 Vagrant 环境，请注意替换各个命令中相关文件的路径。第二个和第三个节点的安装脚本稍有不同，详情见代码库。

## Elasticsearch 配置文件


下面是第一个 Elasticsearch 节点的参考配置文件， es1.yml ：

```
# ---------------------------------- Cluster -----------------------------------
#设定集群名称
cluster.name: elk4devops

# ------------------------------------ Node ------------------------------------
#设定节点名称，此处使用的是 hostname
node.name: es1

# ----------------------------------- Paths ------------------------------------
#设定 es 服务器数据目录
path.data: /var/lib/elasticsearch
#设定 es 服务器日志目录
path.logs: /var/log/elasticsearch

# ---------------------------------- Network -----------------------------------
#设定此节点加入网络的名称，这里使用的是 FQDN
network.host: es1.zenlab.local

# --------------------------------- Discovery ----------------------------------
#设定初始的 master 节点为 es1
cluster.initial_master_nodes: ["es1"]
discovery.seed_hosts: ["es1.zenlab.local"]

# ------------------------------- TLS and Cert ---------------------------------
#启用用户名和密码认证
xpack.security.enabled: true

#启用 ES 集群内加密传输
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.certificate_authorities: ca.crt
xpack.security.transport.ssl.key: ${node.name}.key
xpack.security.transport.ssl.certificate: ${node.name}.crt

#启用 ES 集群客户端访问加密
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.certificate_authorities: ca.crt
xpack.security.http.ssl.key: ${node.name}.key
xpack.security.http.ssl.certificate: ${node.name}.crt

#  For Elastic Agent
xpack.security.authc.api_key.enabled: true

#启用监控数据收集
xpack.monitoring.collection.enabled: true

#  ------------------------------- App Search ---------------------------------
#提前为 App Search 做好准备
action.auto_create_index: ".app-search-*-logs-*,-.app-search-*,+*"
```

说明：第二个和第三个节点的配置文件稍有不同，详情见代码库。

## 总结

在三节点集群的搭建过程中，最好建议启用各种安全和加密选项，用配置安装脚本最小化工作量；这样一步到位的安全性，可以为后续增加其他 Elastic Stack 的产品组件打下良好的基础，ES 集群的配置尽量完善，尽量覆盖后期的其他各种潜在需求，减少未来配置变更的工作量，让后续的测试越来越轻松。