---
date: 2020-06-21T18:42:56+08:00
title: "Beats 摄入数据的最佳实践"
subtitle: "使 Elastic Stack 安全、能适应和可扩展的实战配置"
description: "使 Elastic Stack 安全、能适应和可扩展的实战配置"
categories: "DevOps"
tags: ["Elastic","Beats"]
keywords: ["Metricbeat","Elastic Stack","Filebeat"]
bigimg: [{src: "/images/locked-up.jpg", desc: "DevOps"}]
---

本文概要：配置 ES 3 节点全加密，Kibana 的 SSL 加密配置，Beats 的高可靠性加密传输，用 RBAC 怎样把权限控制到最小，在配置文件中消除明文密码，这些你都做到了么？如何保证安全、能适应和可扩展的配置 Elastic Stack 技术栈，让我们从 Bests 的角度开始讲解。

## 前言

本文使用的软版本：

* Elastic Stack 7.8.0
* macOS 10.15.5
* Vagrant 2.2.9
* VirtualBox 6.0
* CentOS 8.0

下面的配置和测试过程基于以下 Vagrantfile ，你可以在其它任何同等的环境中测试下面的所有配置。


```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Every Vagrant development environment requires a box. You can search for
# boxes at https://atlas.hashicorp.com/search.
BOX_IMAGE = "bento/centos-8"
ES_COUNT = 3
NODE_COUNT = 4


Vagrant.configure("2") do |config|

  #设置所有 guest 使用相同的静态 dns 解析 /etc/hosts
  config.vm.provision :hosts, :sync_hosts => true
  #用 vagrant 默认密钥对 ssh 登录
  config.ssh.insert_key = false
  
  # 用于部署 Elasticsearch 服务器的集群
  (1..ES_COUNT).each do |i|
    config.vm.define "es#{i}" do |es_config|
      es_config.vm.box = BOX_IMAGE
      es_config.vm.hostname = "es#{i}.zenlab.local"
      es_config.vm.network :private_network, ip: "192.168.50.#{i + 10}"
      es_config.vm.provision :hosts, :sync_hosts => true
      es_config.vm.provider :virtualbox do |vb|
        vb.memory = 2048
        vb.cpus = 1 
      end
      es_config.vm.provision :shell, path: 'pre-install-ES.sh'
    end
  end
  
  # 用于部署 Kibana、Logstash 、APM Server、Heatbeat 和 Packetbeat
  config.vm.define "lk" do |lk_config|
    lk_config.vm.box = BOX_IMAGE
    lk_config.vm.hostname = "lk.zenlab.local"
    lk_config.vm.network :private_network, ip: "192.168.50.20"
    lk_config.vm.network 'forwarded_port', guest: 5601, host: 5601
    lk_config.vm.provision :hosts, :sync_hosts => true
    lk_config.vm.provider :virtualbox do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end
    #logstash_config.vm.provision :shell, path: 'pre-install-ES.sh'
  end

  # 两个被管理节点，用于部署监控应用和各种 Beats 代理
  (1..NODE_COUNT).each do |i|
    config.vm.define "node#{i}" do |node_config|
      node_config.vm.box = BOX_IMAGE
      node_config.vm.hostname = "node#{i}.zenlab.local"
      node_config.vm.network :private_network, ip: "192.168.50.#{i + 20}"
      node_config.vm.provider :virtualbox do |vb|
        vb.memory = 1024
        vb.cpus = 1
      end
      node_config.vm.provision :shell, path: 'pre-install-beats.sh'
    end
  end

# Install avahi on all machines  
  config.vm.provision "shell", inline: <<-SHELL
    sh -c "echo 'Welcome to Elastic Stack!'" 
  SHELL
end
```

注：下文中所有路径中的 `/vagrant/` 目录是本 vagrant 测试环境中，所有虚拟机的共享目录，是所有节点上配置文件的原路径。如果你使用的不是 vagrant 环境，你需要在下面的测试中适当的替换。


## 三节点 Elasticsearch 服务器集群

在每个节点上使用下面的初始化脚本，部署 Elasticsearch 服务器。

使用` vagrant up es1 es2 es3 `命令创建并启动 ES 服务器三个节点。

```
# pre-install-ES.sh

elastic_version='7.8.0'
echo "Provisioning a Elasticsearch "$elastic_version" Server..."

sudo date > /etc/vagrant_provisioned_at
sudo swapoff -a
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -p
sudo sh -c "echo 'elasticsearch  -  nofile  65535' >> /etc/security/limits.conf"
sudo sh -c "echo '**** --  --  --  --  --  --  --  -- ****' > /etc/motd"
sudo sh -c "echo '**** Welcome to Elastic Stack Labs' >> /etc/motd"
sudo sh -c "echo '**** --  --  --  --  --  --  --  -- ****' >> /etc/motd"
sudo sh -c "echo '*' >> /etc/motd"
sudo rpm -ivh /vagrant/rpm/elasticsearch-$elastic_version-x86_64.rpm 

```

上面的脚本简单的初始化了几个操作系统参数，然后完成了 rpm 包的安装。非vagrant 环境的需要手工上传 rpm 安装文件，和运行以上的命令。

### 配置首个 ES 服务器节点

登录 es1 节点`vagrant ssh es1` ；

创建用于节点间传输所需要的数字证书和秘钥文件，下面是所使用的种子文件。

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
  - name: 'lk'
    ip: ['192.168.50.20']
    dns: [ 'lk.zenlab.local' ]
```

用  ` elasticsearch-certutil` 创建证书文件包。


```
sudo /usr/share/elasticsearch/bin/elasticsearch-certutil cert --ca --pem --in /vagrant/certs/instance.yml  --out /vagrant/certs/certs.zip
```
将得到的 zip 文件解压缩在适当的目录里备用。

重要步骤：在 Elasticsearch 的配置文件目录中放置必要的数字证书文件。

```
sudo mkdir /etc/elasticsearch/certs
sudo cp /vagrant/certs/ca/ca.crt  /etc/elasticsearch/certs
sudo cp /vagrant/certs/es1/* /etc/elasticsearch/certs
sudo ls /etc/elasticsearch/certs
```
在 certs 目录中有三个文件：

1. ca.crt CA 根证书
2. es1.crt 服务器证书
3. es1.key 私钥文件

CA 根证书是在所有节点上发起对 ES 服务的 HTTPS 服务所需要的客户端证书。 es1.crt 和 es1.key 这样的必要对需要在所有 ES 节点上部署，用于 ES 节点间的 transport 协议加密传输，每个 ES 节点都是用自己的密钥对文件。

在 ES1 的主配置文件中打开安全选项和其它必要配置，示例配置文件如下。

```
# elasticsearch.yml
# ---------------------------------- Cluster -----------------------------------
cluster.name: elk4devops

# ------------------------------------ Node ------------------------------------
node.name: es1

# ----------------------------------- Paths ------------------------------------
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch

# ---------------------------------- Network -----------------------------------
network.host: es1.zenlab.local

# --------------------------------- Discovery ----------------------------------
cluster.initial_master_nodes: ["es1"]
discovery.seed_hosts: [ "es1.zenlab.local" ]

# ------------------------------- TLS and Cert ---------------------------------
xpack.security.enabled: true

#外部服务加密配置
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.key: certs/es1.key
xpack.security.http.ssl.certificate: certs/es1.crt
xpack.security.http.ssl.certificate_authorities: certs/ca.crt

#集群内通讯加密配置
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.key: certs/es1.key
xpack.security.transport.ssl.certificate: certs/es1.crt
xpack.security.transport.ssl.certificate_authorities: certs/ca.crt

xpack.monitoring.collection.enabled: true

#  ------------------------------- App Search ---------------------------------
action.auto_create_index: ".app-search-*-logs-*,-.app-search-*,+*"
```
使用以上配置文件覆盖Elasticsearch 默认的配置文件，首次启动第一个 ES 节点的服务。


```
sudo cp /vagrant/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
sudo systemctl daemon-reload
sudo systemctl start elasticsearch
```

用下面的命令查看启动日志，直到 elasticsearch 服务正常启动。

```
sudo tail -f /var/log/elasticsearch/elk4devops.log
```

用下面的命令初始化 Elasticsearch 系统内置账号为随机复杂密码。


```
sudo /usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto -u "https://es1.zenlab.local:9200" -b


Changed password for user apm_system
PASSWORD apm_system = irpVThXpbFDrdq2rBQUC

Changed password for user kibana_system
PASSWORD kibana_system = CxGNlkqQMbcp6u6XuCbk

Changed password for user kibana
PASSWORD kibana = CxGNlkqQMbcp6u6XuCbk

Changed password for user logstash_system
PASSWORD logstash_system = EOUiCyQQ97IHwUJs8Eum

Changed password for user beats_system
PASSWORD beats_system = EF8OdPmcpy1bUCgFVQ90

Changed password for user remote_monitoring_user
PASSWORD remote_monitoring_user = 3ZRBVo5Omu33McoOKgwE

Changed password for user elastic
PASSWORD elastic = ZSzN2idoU6hFa4f0ulPP
```

将上面随机生成的密码保存在安全的地方备用，这些内置的超级用户权限大，一旦遗失了密码，可能会造成重大的数据泄露。


用上面创建的账户测试第一个 ES 节点是否可以通过 https 正常访问，这里也测试 ca 公钥的可用性。

```
curl --cacert /vagrant/certs/ca/ca.crt -u elastic 'https://es1.zenlab.local:9200/_cat/nodes?v'

```
在 es1 服务器的命令行运行以上命令，输入 elastic 的密码。应该可以看到正常的输出。`/vagrant/certs/ca/ca.crt` 这个路径替换成你的环境中的相关 ca 证书文件路径。



### 配置第二个和第三个 ES 服务器节点

剩下的两个节点在加入集群之前都已经通过初始化脚本安装完了 rpm 安装包。剩下的就是逐个节点的部署之前生产的证书文件和修改后的 elasticsearc.yml 主配置文件。在本文档参考的环境中使用如下命令。

登录 es 2 ` vagrant ssh es2`

配置 es2 的证书和秘钥文件，下面的复制原路径需要替换成你所使用的实际路径。

```sh
sudo mkdir /etc/elasticsearch/certs
sudo cp /vagrant/certs/ca/ca.crt  /etc/elasticsearch/certs
sudo cp /vagrant/certs/es2/* /etc/elasticsearch/certs
sudo ls /etc/elasticsearch/certs
```

部署 es2 的配置文件，然后启动这个节点的 Elasticsearch 服务。

```sh
sudo cp /vagrant/elasticsearch2.yml /etc/elasticsearch/elasticsearch.yml
sudo systemctl daemon-reload
sudo systemctl start elasticsearch
```
`elasticsearch2.yml ` 文件的内容如下。


```yml
# ---------------------------------- Cluster -----------------------------------
cluster.name: elk4devops

# ------------------------------------ Node ------------------------------------
node.name: es2

# ----------------------------------- Paths ------------------------------------
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch

# ---------------------------------- Network -----------------------------------
network.host: es2.zenlab.local

# --------------------------------- Discovery ----------------------------------
cluster.initial_master_nodes: ["es1"]
discovery.seed_hosts: [ "es1.zenlab.local" ]

# ------------------------------- TLS and Cert ---------------------------------
xpack.security.enabled: true

xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.key: certs/es2.key
xpack.security.http.ssl.certificate: certs/es2.crt
xpack.security.http.ssl.certificate_authorities: certs/ca.crt

xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.key: certs/es2.key
xpack.security.transport.ssl.certificate: certs/es2.crt
xpack.security.transport.ssl.certificate_authorities: certs/ca.crt

xpack.monitoring.collection.enabled: true

#  ------------------------------- App Search ---------------------------------
action.auto_create_index: ".app-search-*-logs-*,-.app-search-*,+*"
```

在 es2 的命令用下面的命令查看是否该节点正常加入了集群。


```sh
curl --cacert /vagrant/certs/ca/ca.crt -u elastic 'https://es1.zenlab.local:9200/_cat/nodes?v'
Enter host password for user 'elastic':
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
192.168.50.11           37          94   0    0.00    0.05     0.06 dilmrt    *      es1
192.168.50.12           17          96   9    0.49    0.20     0.07 dilmrt    -      es2
```

注意上面 ca.crt 文件的路径，要输入的是 elasstic 用户的密码。 正常情况下两个节点都会出现在结果清单中。

用相似的命令初始化和启动 es3 节点的服务。es3 的主配置文件样例如下。

```sh
# ---------------------------------- Cluster -----------------------------------
cluster.name: elk4devops

# ------------------------------------ Node ------------------------------------
node.name: es3

# ----------------------------------- Paths ------------------------------------
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch

# ---------------------------------- Network -----------------------------------
network.host: es3.zenlab.local

# --------------------------------- Discovery ----------------------------------
cluster.initial_master_nodes: ["es1"]
discovery.seed_hosts: [ "es1.zenlab.local" ]

# ------------------------------- TLS and Cert ---------------------------------
xpack.security.enabled: true

xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.key: certs/es3.key
xpack.security.http.ssl.certificate: certs/es3.crt
xpack.security.http.ssl.certificate_authorities: certs/ca.crt

xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.key: certs/es3.key
xpack.security.transport.ssl.certificate: certs/es3.crt
xpack.security.transport.ssl.certificate_authorities: certs/ca.crt

xpack.monitoring.collection.enabled: true

#  ------------------------------- App Search ---------------------------------
action.auto_create_index: ".app-search-*-logs-*,-.app-search-*,+*"

```
最终集群的测试状态如下：


```sh
[vagrant@es1 ~]$ curl --cacert /vagrant/certs/ca/ca.crt -u elastic 'https://es1.zenlab.local:9200/_cat/nodes?v'
Enter host password for user 'elastic':
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
192.168.50.11           20          96   6    0.18    0.09     0.03 dilmrt    *      es1
192.168.50.13           50          96   2    0.02    0.07     0.03 dilmrt    -      es3
192.168.50.12           25          96   1    0.00    0.02     0.00 dilmrt    -      es2
```

## 配置 Kibana 服务器

服务是必要的的管理界面，是数据搜索、可视化的重要工具。在 Elasticsearch 服务打开了外部 https 加密访问的情况下，Kibana 服务器的安装和配置也需要做如下调整。

Kibana 的 rpm 安装这里省略。下面直接进入相关的主要配置步骤。

复制用于链接 ES 集群的证书


```
sudo mkdir /etc/kibana/certs
sudo cp /vagrant/certs/ca/ca.crt  /etc/kibana/certs
sudo cp /vagrant/certs/lk/* /etc/kibana/certs
sudo ls /etc/kibana/certs
```

修改默认的 kibana.yml 配置文件，然后覆盖默认的配置文件后启动 kibana 服务。


```
sudo cp /vagrant/kibna.yml /etc/kibana/kibana.yml
sudo cat /etc/kibana/kibana.yml
sudo systemctl start kibana
```

监控 kibana 的启动日志，直到它正常启动。


```
sudo tail -f /var/log/messages
```

启动后，使用浏览器访问  `https://lk.zenlab.lcoal:5601 ` Kibana 服务，使用 elastic 用户的密码登录，确保 Kibana 正常启动。

## 配置权限 Beats 账号

在使用 Beats 采集监控数据的时候，Beats 的配置文件中需要配置一个后台 Elasticsearch 服务访问账号，安全起见需求需要将这个账号配置为只写权限。配置步骤如下。

在 Kibana 的用户管理中创建名为 `beats-writer` 的角色，如下图所示。

![](/images/writer-role.jpeg)

以上这个角色拥有 filebeat 和 Metricbeat 两个索引的访问权限，这里是为了评估用户角色管理的工作量，否则可以每个索引单独设置一套必要权限的角色和用户，从而实现更安全的防护。

然后创建名为 `beats-writer` 的用户，设置一个密码，将它赋予 `beats-writer` 的角色（上面创建的）。


![](/images/beats-writer-user.jpeg)

这样它就可以用于所有 Beats 节点的配置了。


## 初始化首个 Beats 节点

在 vagrant 测试环境中启动第一个用于测试 Beats 的节点。

`vagrant up node1`

这里使用了初始脚本安装相关的 rpm 安装包。

```
#!/bin/bash
# author: Martin Liu
# url:martinliu.cn
elastic_version='7.8.0'
echo "Installing a Filebeat "$elastic_version" agent..."

sudo rpm -ivh /vagrant/rpm/filebeat-$elastic_version-x86_64.rpm
sudo systemctl enable  filebeat.service
sudo rpm -ivh /vagrant/rpm/metricbeat-$elastic_version-x86_64.rpm
sudo systemctl enable  metricbeat.service
sudo rpm -ivh /vagrant/rpm/auditbeat-$elastic_version-x86_64.rpm
sudo systemctl enable  auditbeat.service
```
登录该节点进行 Beats 的初始化配置。目前 Elasticsearch 集群还是空白的，还没有初始化任何 Beats 相关的索引、可视化和仪表板。这个初始化工作是通过，每种 Beats 的 setup 命令完成的。这个 setup 命令只需要在一个节点上成功执行一次即可，其它节点的配置文件中，连 setup 命令相关的配置都不需要。

这里使用的 filebeat.yml 参考文件如下：

```
#=========================== Filebeat inputs =============================
filebeat.inputs:
- type: log
  enabled: false
  paths:
    - /var/log/*.log

#============================= Filebeat modules ===============================
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true
  reload.period: 5s

#==================== Elasticsearch template setting ==========================
setup.template.settings:
  index.number_of_shards: 1
  index.codec: best_compression

#============================== Kibana =====================================
setup.kibana:
  host: "https://lk.zenlab.local:5601"  

#-------------------------- Elasticsearch output ------------------------------
output.elasticsearch:
  hosts: ["es1.zenlab.local:9200"]
  username: "elastic"
  password: "1l1lqVMMWMbLI6DCH0dQ"
  protocol: https

#================================ Processors =====================================
processors:
  - add_host_metadata: 
      netinfo.enabled: true
      cache.ttl: 5m
      geo:
        name: bj-dc-01
        location: 35.5528, 116.2360
        continent_name: Asia
        country_iso_code: CN
        region_name: Beijing
        region_iso_code: CN-BJ
        city_name: Beijing 
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~
```

目前的计划是配置 Beats 直接访问 Elasticsearch 后台服务，不通过 Logstash 中转。以后增加这个参考配置。

在执行 filebeat setup 命令之前，还需要在 Beats 节点上部署上面生成的 ca 公钥文件。参考命令如下。


```
sudo update-ca-trust enable
sudo cp /vagrant/certs/ca/ca.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract
```

这里把 ca.crt 公钥文件部署到了 CentOS 操作系统的的可信 CA 发放机构的目录中，其它操作系统中的这个证书路径可能不同，需要做替换，包括以上的证书更新命令也可能需要调整。

经过以上的配置之后，用之前的 curl 命令测试一下是否这个证书生效了。



```sh
[vagrant@es1 ~]$ curl -u elastic 'https://es1.zenlab.local:9200/_cat/nodes?v'
Enter host password for user 'elastic':
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
192.168.50.11           20          96   6    0.18    0.09     0.03 dilmrt    *      es1
192.168.50.13           50          96   2    0.02    0.07     0.03 dilmrt    -      es3
192.168.50.12           25          96   1    0.00    0.02     0.00 dilmrt    -      es2
```


这次在参数中故意省略了 ca 证书文件路径，如果 curl 可以正常访问，那么 Beats 程序也可以，而且不需要在 Beats 配置文件中生命公钥的路径，更有利于在以后切换到另外一套 CA 秘钥后，配置文件的更新工作。


这里省略 Beats 配置文件的展示，参考一下命令做初始化前的准备。


```
sudo cp -f /vagrant/filebeat.yml /etc/filebeat/filebeat.yml
sudo cp -f /vagrant/metricbeat.yml /etc/metricbeat/metricbeat.yml
sudo filebeat modules enable system
```

为了测试的方便起见，在 filebeat.yml 和 metricbeat.yml 文件中使用了超级用户 elastic ，如果这个动作伴随着 Elastic Stack 的版本升级需要经常发生，此处需要配置一个 Beats setup 用的专用角色和账户，从而避免多次使用超级用户。

下面运行 setup 命令：

```
filebeat setup
metricbeat setup
```
这两个命令正常运行后，在 Kibana 里会增加增加相关的索引、pipeline、可视化和仪表板等对象。

使用下面的命令测试 filebeat 和 metricbeat 是否能正常的采集数据并传输到后台。

```
filebeat -e 
metricbeat -e 
```
如果报错的话，将 level 在配置文件中设置为 debug，方便调试。调试成功之后，应该在 Kibana 的界面中，可以看到 node1 节点，点击后能看到实时更新过来的日志和监控指标。

![](/images/metric-node1.jpeg)




## 在新的节点上部署 Beats

在新的需要部署 Beats 的节点上，可以使用下面的脚本配置和部署。

add-agent.sh
```
#!/bin/bash
# author: Martin Liu
# url:martinliu.cn

elastic_version='7.8.0'
b_user='beats-writer'
b_pwd='DevOps1234'

echo "############## Installing a Beats "$elastic_version" agent..."
sudo rpm -ivh /vagrant/rpm/filebeat-$elastic_version-x86_64.rpm
sudo systemctl enable  filebeat.service
sudo filebeat modules enable system
sudo rpm -ivh /vagrant/rpm/metricbeat-$elastic_version-x86_64.rpm
sudo systemctl enable  metricbeat.service

echo "################### Setup Public CA..."
sudo update-ca-trust enable
sudo cp /vagrant/certs/ca/ca.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract

echo "################### Update Beats configuration files ..."
sudo cp -f /vagrant/filebeat-v1.yml /etc/filebeat/filebeat.yml
sudo cp -f /vagrant/metricbeat-v1.yml /etc/metricbeat/metricbeat.yml

echo "################### Setup Keystor for Beats ..."
echo $b_user  | sudo filebeat keystore add BEATS_WRITER_USERNAME --stdin --force
echo $b_pwd   | sudo filebeat keystore add BEATS_WRITER_PW --stdin --force
echo $b_user  | sudo metricbeat keystore add BEATS_WRITER_USERNAME --stdin --force
echo $b_pwd   | sudo metricbeat keystore add BEATS_WRITER_PW --stdin --force

echo "################### Start Beats services ..."

sudo systemctl start  metricbeat.service
sudo systemctl start  filebeat.service
```

简单说明以上脚本的功能：

* 用 rpm 安装包安装所需要的 Beats，filebeat 开启 system 模块。
* 在目标操作系统里部署必须的 ca 证书到默认路径中，并启用。从而省略在所有 beats 文件中生命公钥文件的路径。
* 覆盖更新默认的 Beats 配置文件。
* 创建并初始化 Beats 配置文件中所需要的 beats-writer 用户名和密码。从而消除消除所有明文密码。以上脚本只需要在节点上更新的时候才允许，允许后删除，从而不会留下任何明文密码和账户信息。Beats 的任何模块配置中，如果需要配置任何密码账户也需要如法炮制，从而保证基本的安全性。
* 启动 Beats 服务

以上脚本所使用的配置文件文件如下。

filebeat-v1.yml

```
filebeat.inputs:
- type: log
  enabled: false
  paths:
    - /var/log/*.log

#============================= Filebeat modules ===============================
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true
  reload.period: 60s

#-------------------------- Elasticsearch output ------------------------------
output.elasticsearch:
  hosts: ["es1.zenlab.local:9200","es2.zenlab.local:9200","es3.zenlab.local:9200"]
  password: ${BEATS_WRITER_PW}
  username: ${BEATS_WRITER_USERNAME}
  protocol: https

#================================ Processors =====================================
processors:
  - add_host_metadata: 
      netinfo.enabled: true
      cache.ttl: 5m
      geo:
        name: bj-dc-01
        location: 35.5528, 116.2360
        continent_name: Asia
        country_iso_code: CN
        region_name: Beijing
        region_iso_code: CN-BJ
        city_name: Beijing 
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~
  - add_fields:
      target: ''
      fields:
        service.name: 'Elastic Cloud'
        service.id: 'ec-ww'

#==================== Best Practice Configuration ==========================
setup.ilm.check_exists: false
logging.level: error
queue.spool: ~
```


metricbeat.yml

```
# =========================== Modules configuration ============================
metricbeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: true
  reload.period: 120s

#-------------------------- Elasticsearch output ------------------------------
output.elasticsearch:
  hosts: ["es1.zenlab.local:9200","es2.zenlab.local:9200","es3.zenlab.local:9200"]
  password: ${BEATS_WRITER_PW}
  username: ${BEATS_WRITER_USERNAME}
  protocol: https

#================================ Processors =====================================
processors:
  - add_host_metadata: 
      netinfo.enabled: true
      cache.ttl: 5m
      geo:
        name: bj-dc-01
        location: 35.5528, 116.2360
        continent_name: Asia
        country_iso_code: CN
        region_name: Beijing
        region_iso_code: CN-BJ
        city_name: Beijing 
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~
  - add_fields:
      target: ''
      fields:
        service.name: 'Elastic Cloud'
        service.id: 'ec-ww'

#==================== Best Practice Configuration ==========================
setup.ilm.check_exists: false
logging.level: error
queue.spool: ~
```

解释一下相关的重要配置。

* netinfo.enabled: true 收集所有网卡的配置信息，覆盖多块网卡的情况
* geo: 地理位置信息对以后基于位置的查询打下基础，这对于监控和信息安全都非常重要。为以后基于 host 的上下文关联打下基础，方便在 apm、log、metric、heartbeat 和机器学习的界面中相互跳转。
* add_fields: 在 fields 下面维护 ECS 数据定义中的必要的有意义的数据，在网上查询 ECS 的数据定义，这些字段可以优化以后的搜索逻辑。
* 最后一段是其它必要的最佳实践设置
* output.elasticsearch : 这里使用了三个 ES 节点的链接地址，这里应该使用至少 2 个 Elasticsearch 集群中的 ingest 节点。 

## 总结

本文没有展开说明和配置的地方包括：对 Best 节点的工作状态的监控；对索引生命周期规则的调优（用尽磁盘），冷热数据的自动化迁移规则。

完成的配置包括：

* 配置 ES 3 节点集群内部的 TLS 加密传输，对外的 HTTPS 加密协议服务
* Kibana 基于证书的 SSL 加密配置
* Beats 的高可靠性后台传输数据，TLS加密传输数据
* 用基于角色的访问控制，创建了只写权限的 beats-writer 角色和用户。
* 用 beats 的 keystore 将配置文件中的明文密码消除。






