---
author: liuadmin
categories:
- WordPress1
comments: true
date: 2016-01-10T01:01:25Z
subtitle: Github.io可以帮你免费host静态的web站点，站点的代码需要放在github.com上，可见这是一种鼓励人们使用github.com的方法。在github.com上创建与网站对应的仓库，并更新它，就可以实现网站的更新。github.io域名的网站也支持cname，这样你可以用自己的域名访问它了。
slug: '%e7%94%a8-jekyll-github-%e5%bb%ba%e7%ab%8b%e9%9d%99%e6%80%81%e7%ab%99%e7%82%b9'
tags:
- github
- jekyll
title: 用 Jekyll + Github 建立静态站点
url: /2016/01/10/e794a8-jekyll-github-e5bbbae7ab8be99d99e68081e7ab99e782b9/
wordpress_id: 54118
---

## 新建库


建立一个用户名开头的库，如我的github用户名是 martinliu， 新建的库的名字为 martinliu.github.io ; 这个库将是存放web页面的。包括该域名下的站点的所有相关页码代码文件和相关css,图片等文件。



## 更新并上传新库



参考的命令如下：

[bash]
git clone https://github.com/martinliu/martinliu.github.io
cd martinliu.github.io
echo "Martin Liu's Github Homepage" > index.html
git add --all
git commit -m "Initial commit"
git push -u origin master
[/bash]

打开浏览器测试你的网站，访问网址： http://martinliu.github.io ， 你已经可以看到你的初始化页码了。



## Jekyll博客系统



Github网站上推荐使用Jekyll创建和管理这个博客系统。它是支持Markdown语法，不需要使用数据库，纯文本的静态网站和博客系统。使用它可以建立和管理一个风格美观，容易管理的网站，生成的网页可以上传到以上生成的网站库中。



## 安装Jekyll系统



我的测试系统：Fedora 23。操作步骤如下。
安装依赖的包和ruby环境

[bash]
dnf install ruby  ruby-devel gem gcc libffi redhat-rpm-config
[/bash]

更用国内的rubygem源
[bash]
gem source -r https://rubygems.org/
gem source -a http://mirrors.aliyun.com/rubygems/
gem update --system

gem install jekyll
[/bash]

##本地测试jekyll站点
进入克隆到本地的库，并创建jekyll站点。

[bash]
cd martinliu.github.io
rm index.html

jekyll new .
New jekyll site installed in /root/martinliu.github.io.
[root@demo-w540 martinliu.github.io]# ls
about.md     css       _includes   _layouts  _sass
_config.yml  feed.xml  index.html  _posts
[root@demo-w540 martinliu.github.io]# jekyll server
Configuration file: /root/martinliu.github.io/_config.yml
Source: /root/martinliu.github.io
Destination: /root/martinliu.github.io/_site
Incremental build: disabled. Enable with --incremental
Generating...
done in 0.205 seconds.
Auto-regeneration: enabled for '/root/martinliu.github.io'
Configuration file: /root/martinliu.github.io/_config.yml
Server address: http://127.0.0.1:4000/
Server running... press ctrl-c to stop.
[/bash]

编辑站点的相关文件，测试成功之后，在上传到github上，然可到 maritnliu.github.io 上检查和本地的显示效果是否相同。


