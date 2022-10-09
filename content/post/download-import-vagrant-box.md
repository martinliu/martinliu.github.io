---
date: 2020-03-26T08:57:57+08:00
title: "如何在墙内正常导入 Vagrant 虚拟机模板"
subtitle: "这是 Vagrant 新用户需要解决的第一个问题"
description: "在墙内如何正常下载所需要的 Vagrant 的虚拟机模板文件"
categories: ["DevOps"]
tags: ["DevOps"]
keywords: ["DevOps"]
image: "/images/vagrant-download-box.jpg"
draft: false
---

当你满心欢喜的安装完了 vagrant 之后，在你第一次 `vagrant up` 命令的时候，是下载超时么？你的内心是什么感受？想放弃了么？

其实你只需要找到国内的 box 文件镜像服务器，或者下载地址，然后手工下载对应的 Box 文件（操作系统镜像文件），并导入即可，本文将帮你铲除这只官方镜像文件下载失败的拦路虎。

![](/images/vagrant-home-page.png)

Vagrant 的优势：

* 虚拟机对于系统级开发和测试工作具有不可替代的作用
* 手工安装的虚拟机非常

## 准备工作

我的测试环境如下，如果你的测试环境和我的不同，但是本操作方法和过程也同样的适用于相似的环境。

环境描述：

* macOS catalina version 10.15.3
* vagrant 2.2.4
* Virtuabox 6.0.15r135660

如果你也百度了’ vagrant box 国内镜像‘的话，结果会使你很失望，清华大学等站点只是缓存了个别的镜像文件，并没有其它版本特别全面的网站，更没有完整的镜像。如果你知道其它国内的镜像站点请告诉我，我会增加到本文。

Ubuntu 的可以浏览这两个目标下载网址。

https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cloud-images/vagrant/

然后用vagrant 下面的命令就可以将 box 下载并且添加到本地。

* ubuntu 18.04 LTS:

vagrant box add https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cloud-images/bionic/current/bionic-server-cloudimg-amd64-vagrant.box --name ubuntu18

* ubunt 16.04 LTS：

vagrant box add https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cloud-images/xenial/current/xenial-server-cloudimg-amd64-vagrant.box --name ubuntu16

* ubuntu14：

vagrant box add https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cloud-images/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box --name ubuntu14

对于 CentOS 而言，它的官网整理的比较好，提供了各种格式的下载，可能需要科学上网才能访问到 Centos 的下载网址。

http://cloud.centos.org/centos/7/vagrant/
http://cloud.centos.org/centos/8/vagrant/

实战建议：你并不需要下载过多的 box 操作系统镜像文件，够用即可。建议将最近有可能使用到的 Box 文件用断点续传的多线程下载工具下载到本机磁盘备用。我下载了一些，关注的微信号‘ MyDevOps ’ 回复 box1 即可获得百度网盘下载地址，这个共享目录中有本文中所提到的所有 Box 文件。


## 导入 Box 文件

用 `vagrant box add` 命令将本地下载好的 box 文件导入到 vagrant 的主目录中，macOS 下是在`~/.vagrant/` 目录里。

使用` vagrant box list `名先查看本地已有的 box 清单，下面的执行结果如下。


```
➜  ~ vagrant box list
Puppetlabs Ubuntu 12.04.2 x86_64, VBox 4.2.10, No Puppet or Chef (virtualbox, 0)
bento/centos-7.1                                                 (virtualbox, 2.2.2)
bento/centos-7.2                                                 (virtualbox, 2.3.1)
bento/centos-8                                                   (virtualbox, 202002.04.0)
bento/ubuntu-16.04                                               (virtualbox, 0)
coreos-alpha                                                     (virtualbox, 1451.2.0)
geerlingguy/centos6                                              (virtualbox, 0)
geerlingguy/centos7                                              (virtualbox, 0)
geerlingguy/ubuntu1604                                           (virtualbox, 0)
ubuntu/trusty64                                                  (virtualbox, 20161207.0.0)
ubuntu/trusty64                                                  (virtualbox, 20170307.0.0)
ubuntu/wily64                                                    (virtualbox, 20160715.0.0)
ubuntu/xenial64                                                  (virtualbox, 20161214.0.1)
ubuntu/xenial64                                                  (virtualbox, 20170307.0.1)
➜  ~
```

使用` vagrant box add `导入，并确认。 参考下面的执行过程

```
➜  ~ vagrant box  add ~/Downloads/box/bionic-server-cloudimg-amd64-vagrant.box --name ubuntu/bionic
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'ubuntu/bionic' (v0) for provider:
    box: Unpacking necessary files from: file:///Users/martin/Downloads/box/bionic-server-cloudimg-amd64-vagrant.box
==> box: Successfully added box 'ubuntu/bionic' (v0) for 'virtualbox'!
➜  ~ vagrant box list
Puppetlabs Ubuntu 12.04.2 x86_64, VBox 4.2.10, No Puppet or Chef (virtualbox, 0)
bento/centos-7.1                                                 (virtualbox, 2.2.2)
bento/centos-7.2                                                 (virtualbox, 2.3.1)
bento/centos-8                                                   (virtualbox, 202002.04.0)
bento/ubuntu-16.04                                               (virtualbox, 0)
coreos-alpha                                                     (virtualbox, 1451.2.0)
geerlingguy/centos6                                              (virtualbox, 0)
geerlingguy/centos7                                              (virtualbox, 0)
geerlingguy/ubuntu1604                                           (virtualbox, 0)
ubuntu/bionic                                                    (virtualbox, 0)
ubuntu/trusty64                                                  (virtualbox, 20161207.0.0)
ubuntu/trusty64                                                  (virtualbox, 20170307.0.0)
ubuntu/wily64                                                    (virtualbox, 20160715.0.0)
ubuntu/xenial64                                                  (virtualbox, 20161214.0.1)
ubuntu/xenial64                                                  (virtualbox, 20170307.0.1)
➜  ~
```

## 校验所导入的 Box

创建一个测试目录，并执行` vagrant init ubuntu/bionic ` ，然后使用 vagrant up 测试。

```
➜  test pwd
/Users/martin/code/test
➜  test vagrant init ubuntu/bionic
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
```

test 目录下面现在生成了一个默认的 Vagrantfile 文件，查看这个默认的 Vagrantfile 配置文件。这是一个很好的学习资料。

```
➜  test cat Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
```

现在可以踏实的运行 vagrant up 了，Ubuntu 的 Box 文件导入通常没有什么问题。默认配置的 Ubuntu 版本 bionic 的 vm 现在就正常启动了。

```
➜  test vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'ubuntu/bionic'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: test_default_1585496539631_90780
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 5.2.34
    default: VirtualBox Version: 6.0
==> default: Mounting shared folders...
    default: /vagrant => /Users/martin/code/test
    
```

现在 ssh 登录到这个崭新的 vm 。

```    
➜  test vagrant ssh
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Mar 29 15:42:53 UTC 2020

  System load:  1.25              Processes:             99
  Usage of /:   10.1% of 9.63GB   Users logged in:       0
  Memory usage: 12%               IP address for enp0s3: 10.0.2.15
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.


vagrant@ubuntu-bionic:~$ top
```
## 导入 CentOS 7 可能遇到的问题

CentOS 7 和 8 的相关版本在我的测试环境中都出现了导入正常 vagrant up 异常的问题，通常网络搜索错误代码后，就可以解决了，如果有任何问题，欢迎到我的微信公众后台留言。




## 总结

Vagrant 的功能性和必要性是非常高的，特别是对于天朝的码农而言，就更加重要了。它是 DevOps 工具链上的知名工具，而它的使用率和广泛性却不高。后续还会出这方面的系列内容，讲解更多关于 Vagrant 的优化和功能。

2io

