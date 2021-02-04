---
date: 2020-04-11T09:36:49+08:00
title: "随心所欲的为应用无痛添加搜索功能"
subtitle: ""
description: ""
categories: "DevOps"
tags: ["elk"]
keywords: ["DevOps","elastic stack","app-search"]
bigimg: [{src: "https://res.cloudinary.com/martinliu/image/upload/abstract-1.jpg", desc: "DevOps"}]
---

开发搜索功能从此再也不用犯愁了，有了 App Search ，为应用增加搜索功能一下子变得简单了很多。本文描述了如何轻松上手这套搜索平台的所有步骤。

什么是 App Search? 这是一套强大的 API 和开发者工具集，以构建功能强大的面向用户的搜索应用为目标。相关详细介绍见 https://www.elastic.co/cn/app-search

![](/images/apps1.jpg)

丰富的开箱即用功能:

* 为相关性搜索应用场景而优化
* 拼写错误容忍
* 相关度调整
* 支持第三方 API 客户端，且具备强大的 API
* 独立的 API 日志和搜索分析
* 自动化扩展&运维支持
* Search UI library


## 环境准备

测试环境现需要一台 Elasticsearch 服务器，或者和下面等同的环境。

本文的环境描述如下：

* macOS 10.15.4
* vagrant 2.2.7
* virtualbox 6.0.15
* 虚拟机模板 bento/centos-8
* elasticsearch 7.6.1
* app-search 7.6.1
* jdk-11.06

本文的测试环境基于 Vagrant + VirtualBox 的组合环境搭建而成，基础安装工作可以一键完成。

主要脚本 Vagrantfile、pre-install-ES.sh 请参考此代码库：

https://github.com/martinliu/elastic-labs/tree/master/app-search 

开启并登陆这套安装环境的命令如下。


```
vagrant up
vagrant ssh
```

在以上命令的启动信息里找到如下的 elastic 用户密码部分备用。

```
master1: Changed password for user elastic
master1: PASSWORD elastic = eczHJ7NPrsO1B1BRA8SS
```

## 安装 App Search

浏览 App Search 的安装文档： https://swiftype.com/documentation/app-search/self-managed/installation

安装 App Search 所需的 JDK 8 或者 11 ，本文安装的是 Oracle 的 JDK 11。本文假设所有的安装文件和已经编辑好的配置文件都放在了 /vagrant 目录下。

`sudo rpm -ivh /vagrant/rpm/jdk-11.0.6_linux-x64_bin.rpm`

安装 App Search 服务器。

`sudo rpm -ivh /vagrant/rpm/app-search-7.6.1.rpm `

浏览 App Search 服务器默认的配置文件，了解有哪些可用选项。

`sudo more /usr/share/app-search/config/app-search.yml `

将 Elasticsearch 服务器安装时产生的随机密码更新到 app-search.yml 文件中，并且定制它的内容如下：

```
allow_es_settings_modification: true
elasticsearch.host: http://192.168.50.10:9200
elasticsearch.username: elastic
elasticsearch.password: eczHJ7NPrsO1B1BRA8SS
app_search.external_url: http://192.168.50.10:3002
app_search.listen_host: 192.168.50.10
app_search.listen_port: 3002
log_directory: /var/log/app-search
filebeat_log_directory: /var/log/app-search
```

将更新好的 app-search.yml 更新到它默认的路径中。

`sudo cp /vagrant/appsearch/app-search.yml /usr/share/app-search/config/app-search.yml`

启动 App Search 服务器。

`sudo /usr/share/app-search/bin/app-search`

在启动日志中，找到如下的默认用户名和密码。

```
#########################################################

*** Default user credentials have been setup. These are only printed once, so please ensure they are recorded. ***
      username: app_search
      password: vjqmjhv2s5rzixjc

#########################################################

```
在服务器初始化启动完毕之后，用上面的用户名和密码，在浏览器中登录 App Search 服务器 http://192.168.50.10:3002 

到此为止，App Search 服务器的安装就完成了。它其实是一个基于 Elasticsearch 的搜索服务平台。

它的特点是帮助开发者随心所欲的为已有的或者正在开发的项目增加功能强大的搜索功能，而且将搜索功能的实施成本降低到无痛点的程度。App Search 可以覆盖的使用场景如下：

* SaaS / web 应用
* 复杂的电商应用
* 客户支持服务站点
* Geo 地理搜索
* 公司官网
* 内部的搜索
* 还有更多其他

## 创建名为 games 的搜索引擎

在首页的创建引擎的输入框中输入 games， 语言选择默认选项，点击创建。浏览新创建的引擎，点击左下角的菜单 Credentials，复制 privite-key 备用。

![](/images/apps2.jpg)

找到这个搜索引擎的 API 调用网址备用。
`http://192.168.50.10:3002/api/as/v1/`

![](/images/apps3.jpg)


## 通过 API 索引数据文档

需要通过 App Search 提供的 API 索引一份具有 4000+ 条数据的 json 文件。数据文件见代码库中的 `video-games.json` 。本文使用 Ruby 编写了一个上传脚本，见 `upload.rb` ，该脚本使用了名为 elastic-app-search  的客户端库。你可以使用其他编程语音，实现待接入系统和 App Search 服务器的对接，并与之保持同步，保持待搜索数据的更新。

```
# `gem install elastic-app-search progress_bar`

require 'elastic-app-search'
require 'json'
require 'progress_bar'

API_ENDPOINT = 'http://192.168.50.10:3002/api/as//v1/'
API_KEY = 'private-jdhcmi1yhy8wjxo6upb4qki3'
ENGINE_NAME = 'games'

client = Elastic::AppSearch::Client.new(:api_key => API_KEY, :api_endpoint => API_ENDPOINT)
file = File.read('./video-games.json')
data = JSON.parse(file)
bar = ProgressBar.new(data.count / 100)

data.each_slice(100) do |slice|
  client.index_documents(ENGINE_NAME, slice)
  bar.increment!
end

```
以上脚本中的 API_ENDPOINT 和 API_KEY 需要更新，与当前测试系统匹配。这个脚本的运行效果如下：

```
➜  app-search git:(master) ✗ ruby upload.rb
[##########################################################################] [40/40] [100.00%] [00:54] [00:00] [ 0.73/s]

```
索引之后，在搜引擎的 Documents 页面，浏览索引后的数据，用 Query Tester 进行一些搜索，了解这些数据的内容，注意观察当前搜索的结果和排序。

## 修订 Schema

开发者可以按照需要随时修改 Schema，实际上这是一个 Schema 的平台。 Schema 的修改后，数据即可生效，在这个过程中前端用户的搜索体验不会受到任何影响。

![](/images/apps4.jpg)


修改三个字段的定义，并增加 language 字段，点击右上角的 Update Type 按钮生效。



## 按需进行搜索设置

### 创建同义词

为 Pokemon 创建同义词 Pikachu，如下图所示。

![](/images/apps5.jpg)

### 调整搜索字段的权重

为 globa_sales 增加 Functional Boost 1。
![](/images/apps6.jpg)

为 Name 增加 weight 3 ，点击右上角的 Save 保存。在这个过程中观察右侧的搜结果的动态变化，还可以做其他字段的修改，知道搜素结果满意为止。

![](/images/apps7.jpg)

### 创建 curations

故意将某条搜索结果置顶，这有可能因为，这款游戏目前是热评游戏，是畅销爆款，是高利率商品，是广告商品，或者其他业务原因。可以给某个关键字，置顶一条或者多条搜索结果。下面将 pokemon 的 pokemon-ranger-ds-2006 这款产品置顶。点击右上角的 Query Tester 测试一下效果。

![](/images/apps8.jpg)

## 创建用户端搜索界面

Reference UI 是提供给用户使用的搜索界面，它可以是只有一个输入框，也可以是比较复杂的条件查询。如下所示。

![](/images/apps10.jpg)

调整之后点击 Create Preview 按钮，进入搜素界面的确认页面，尝试使用所设定的搜索功能。满意后点击右上角的 Download ZIP Package  按钮下载这个界面的所有代码。

![](/images/apps11.jpg)

在本地解压缩这份搜索代码，并进行调试。

在命令行，进入这个目录，先执行 `npm install `命令，然后执行` npm start `命令。

```
Compiled successfully!

You can now view app-search-reference-ui-react in the browser.

  Local:            http://localhost:3000/
  On Your Network:  http://192.168.1.6:3000/

Note that the development build is not optimized.
To create a production build, use npm run build.
```

在弹出的网页中，在本地测试这个搜索界面的可用性。最后运行 `npm run build` 命令，

```
➜  games-react-demo-ui git:(master) ✗ npm run build

> app-search-reference-ui-react@1.2.0 build /Users/martin/code/elastic-labs/app-search/games-react-demo-ui
> npm-run-all build-css build-js


> app-search-reference-ui-react@1.2.0 build-css /Users/martin/code/elastic-labs/app-search/games-react-demo-ui
> node-sass-chokidar src/ -o src/

No input files were found.

> app-search-reference-ui-react@1.2.0 build-js /Users/martin/code/elastic-labs/app-search/games-react-demo-ui
> node ./scripts/build-no-chunks.js

Creating an optimized production build...
Browserslist: caniuse-lite is outdated. Please run next command `npm update`
Browserslist: caniuse-lite is outdated. Please run next command `npm update`
Compiled successfully.

File sizes after gzip:

  109.1 KB  build/static/js/main.2f745bc0.js
  3.64 KB   build/static/css/main.e43852a4.css

The project was built assuming it is hosted at the server root.
You can control this with the homepage field in your package.json.
For example, add this to build it for GitHub Pages:

  "homepage" : "http://myname.github.io/myapp",

The build folder is ready to be deployed.
You may serve it with a static server:

  npm install -g serve
  serve -s build

Find out more about deployment here:

  https://bit.ly/CRA-deploy

```
最后将构建结果部署到一个目标的先安装的 Nginx 服务器上。

```
sudo yum install -y nginx
sudo mv -f build/* /usr/share/nginx/html
```

在浏览器中访问 Nginx 服务器 `http://192.168.50.10/index.html` 观察最终的实现效果。
![](/images/apps12.jpg)

## 总结

使用 App Search 搜索平台，开发者可以快速的开发出一套定制化的搜索系统，轻松的实现后台搜索业务逻辑的调整，并轻松的将用户搜索界面测试后部署上线。

