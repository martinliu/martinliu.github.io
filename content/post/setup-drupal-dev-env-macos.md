+++
date = 2022-02-05T11:11:55+08:00
title = "img/cos/"
description = "在本地构建可以重复创建、版本控制、持续更新、无缝迁移，且容器化的 Drupal 开发环境。"
author = "Martin Liu"
categories = ["DevOps"]
tags = ["php", "drupal", "github", "docker"]
image = "img/989197bbd274de342caf84c3642d8c6bc7b980ea-1920x700.png"
+++

过年前给自己挖了一个 Drupal 的坑，经过一些时间的研究之后，感觉这个系统和 Remedy 非常神似。说到底它们其实都是表单系统。每个表单表达一种分类的信息而已。Drupal 注重的是表单上的信息点的记录、管理和展示，Remedy 注重的则是每种表单（工作类型）上“工单流程状态”字段变化的记录和管理。

<!--more-->

[DevOps China](https://DevOpsChina.org) 网站的选型之旅，最初使用的是 hugo，但是由于内容更新人员们对 github 系统掌握程度参差不齐，导致对于参与者不友好的问题，这为所有社区内容创建的朋友们设置了一个不必要的门槛。最初设计的是：以官网的内容为最源头参考点，然后同步到其它平台，包括：微信和互动吧等社区对外到入口。最后，微信公众号后台文案编辑的易用性超越了 GitHub 上 Hugo 站点的更新。社区网站维护志愿者也很难投入足够的精力，手工的从微信上同步回社区官网。就这样社区官网的及时更新问题居然持续了两年。

2022年是解决这个问题的时候了。在对 Drupal 经过一定的研究之后，希望这次选型的 Drupal 能不负众望，完美的实现这个艰巨的使命。[【 why drupal ？ 参考文章】](https://stackoverflow.blog/2020/06/23/is-it-time-to-give-drupal-another-look/)

## Drupal 是个内容管理系统

在 macOS 上搭建 PHP + MySQL 的开发环境的工具有很多。我选择使用的是已经绝版的 Acquia Dev Desktop 2 ，它包括了：php 7.3.15 的 php 语言运行环境， MySQL 5.7.29 数据库， Apache/2.4.29 的网页运行服务器， phpMyAdmin 4.9.0.1 数据库管理工具。

![Acquia Dev Desktop 2](img/cos/2022-02-05-2022-02-05_11-08-30.png)

这种集成的 PHP 运行/开发/管理环境，还有很多其它选择，这里不展开。我的目标是：保持最简化和易用，与其它社区伙伴的协作，紧跟 Drupal 版本发布和补丁更新，用容器化实现云上的按需扩展。

首先，我使用 Acquia Dev Desktop 2 创建了一个本地的测试站点，用于学习 Drupal 的使用、定制和开发。它不仅是一个友好的 GUI 工具，其实还附带了 php 开发环境的命令行工具：composer 和 drush 。 使用这两个命令行工具可以完成 Drupal 系统的一键式搭建。在开发一个真实的内容管理系统网站以前，最基础的铺垫工作可能差不多了。

## 一键安装 Drupal 系统

首先，打开 Acquia Dev Desktop 2 ，在界面上点击进入命令行按钮（more -> Open Console）。macOS 系统默认的 termenal 就会被打开，它会在默认环境中增加如下环境变量参数

```sh
Last login: Sat Feb  5 10:25:58 on ttys005
export PHP_ID=php7_3; export PATH="/Applications/DevDesktop/php7_3_x64/bin:/Applications/DevDesktop/mysql/bin:/Applications/DevDesktop/tools:$PATH" && cd "/Users/martin/learning-drupal"
```

这样就可以在你的目标目录中，执行下面的一键安装脚本了：

```sh
# 下载Drupal特定版本的代码库
composer create-project drupal/recommended-project:9.3.5 drupal-dev --no-interaction
cd drupal-dev

# 配置以下可以让我们静默安装 drush 的参数
composer config --no-plugins allow-plugins.composer/installers true
composer config --no-plugins  allow-plugins.drupal/core-composer-scaffold  true
composer config --no-plugins  allow-plugins.drupal/core-project-message true

# 安装 Drupal 站点维护工具 drush
composer require drush/drush  --no-interaction
ln -s vendor/drush/drush/drush ./
./drush version
composer require drush/config-extra  --no-interaction

# 创建目标 MySQL 数据库和用户名/密码
mysqladmin -u root drop local_devopschina -f
mysql -u root -e 'create database local_devopschina'
mysql -u root -e "grant all privileges on local_devopschina.* to ddoc@localhost identified by 'ddoc123'"

# 上面的一切都是为了这个命令可以静默安装，它替代了很多 php 开发的系统在网页上用安装程序进行的初始化工作，下面的数据库 root 密码为空
./drush si standard --locale=zh-hans  --db-url=mysql://ddoc:ddoc123@127.0.0.1:33067/local_devopschina --db-su=root  --site-name="DevOps China" --account-name=admin --account-pass=admin -y

# 安装和启用 Drupal 系统必要的模块和皮肤 【ToDo】

# 生产环境数据迁移，数据库备份的导入，相关文件下载 【ToDo】

# 启动 Drupal 系统
./drush runserver localhost:8090

```

以上是一个写死了的 shell 脚本，还可以对其中的关键参数进行变量替换，使之最终成为一个可以传入参数的可用脚本。

## 进入 Drupal 开发流程

下图展示了 Drupal 网站开发的工作流程。

![Drupal Site Building workflow](img/cos/2022-02-05-Drupal-Site-Building-Workflow.png)

用下面的表格梳理一下：

   序号 | 工作内容  | 概述  | 所需要技能 | 备注
--------|------|------|------|------
1.0 | Content Type | 既是任何一条内容对象的完整定义，也是任何一个可管理实体。系统默认自带了‘文章’和‘基本页面’两个内容类型，隐含的具备了简单的 ‘用户’ 管理系统。在此基础上还需扩展出‘社区合作伙伴’、‘社区活动’等实地。 | 数据库ER设计、数据结构 | 并不需要在 MySQL 中建表，都是在 Drupal 界面完成
2.0 | Fields | 是组成任何内容和实体数据结构的信息点，包含PHP编程语言的数据类型和Drupal 社区里的各种模块，例如‘电话号码’这样的数据结构的引用就是先启用对应的模块| php开发 | Drupal 社区已有模块不满足才做开发
2.1 | Taxonomy | 就像是一个二位数组，在每一个分类里有一堆确切的词汇表。例如社区网站的文章、活动和论坛里的帖子都可以引用“话题”这样一个字段，用于单选或者多选，“话题”这个字段里包含了很多DevOps术语“ci”、“敏捷”、“SRE”等。 | 领域知识、数据机构 | 随着网站内容建设的过程而演进
2.2 | Media | 文档、音频、图片和视频的统一管理，这样方便任意媒体文件的使用；Drupal 9 自带的 Media Libary 模块能够满足需求 | 数字媒体管理、CDN加速 | 所有用户生成媒体都在这个范畴，会严重影响网站速度，依赖与网站 CDN 加速的实施
2.3 | Modules | Drupal 模块非常丰富，从电话号码这样的数据结构，到文本地址到百度地图的转化，到整个知识库结构的定义；社区参与者积分和排名这样的功能将会使用自开发的模块实现 | php开发、数据库 | 需要懂 php 开发语言，可独立开发
3.0 | Path | 每一个内容实体在 Drupal 中被称之为 node，它们都有默认的访问路径，例如：/node/12/；需要整体规划网站的访问路径，不但让网站变得更加有条理，而且还会提高人和搜索引擎的友好程度，Drupal 的相关模块可以实现 | 内容系统梳理 | 尽量保持简单、清晰和持久
4.0 | Permessions | 用户权限需要提前设计，Drupal 除了具有内置的权限机制外，它对任何一个功能模块（内容分类）都可以实施给予角色的矩阵式权限设置，需要提前设计好用户角色类型，权限体系 | 权限设计、信息安全 | 这是实施文章内容上传、论坛和社区活动管理的基础。
4.1 | Workflows | 工作流是 Drupal 系统中默认的功能模块，经过定制以后可以实现社区贡献文章的审核功能。例如开放所有注册用户的投稿权限，投稿文章必须经过审核人员确认后才能发不出来。还可以用于知识库或者编辑的多重审核功能 | 流程定制 | 需要掌握 Drupal 相关模块的使用，确保流程简单易用
5.0 | Layout | 网页布局结构设计，manage display of nodes 这是基础工作 -> blocks -> layout builder -> views -> image styles ，不同的 theme 自带一套 block 的布局  | |
5.1 | Blocks | 实施页面中的每个模块，模块是一个实体可以容纳视频、文字、图片和其他更多，搜索栏，菜单等；他不是内容，是一个 placeholder  |  |
5.2 | Layout Builder | 一个核心模块，拖拽式可视化页面设计实施工具，可以为不同的内容类型、实体和其它创建定制的布局。 |  |
5.3 | Views | 创建数据库查询，过滤和筛选内容，静态的操作或者根据上下文的 。Display【page、block】，format，lields,filter,sort,|  |
6.0 | Add Content | 在以上工作基本完成之后，就可以进入网站内容的填充阶段 | SQL查询 |
6.1 | Menus | 菜单包括网站的主导航菜单，页脚导航和各个页面上可能使用到的分类选项 |  |
6.2 | Site Management | 开发、测试和生产环境之间的迁移和更新流程 | CI、CD、Cloud、DNS、CDN | 用 GitHub 、Docker 和 Azure 等技术实施必要的工作流程
7.0 | Theme | 网站展示风格的开发贯穿于以上所有工作内容的过程中。需要基于某种Drupal网站皮肤作为底板，开发自己的定制皮肤，在需要改进的时候随时调整和更新 | 前端开发、CSS | 图片等美工设计需要交付给社区的设计同学

为了多人、开放式、实现社区网站开发和内容建设的工作，我们还需要一个项目管理工具。这里可以选用 GitHub ：[https://github.com/orgs/DevopsChina/projects/1/](https://github.com/orgs/DevopsChina/projects/1/) 用它可以实现以下功能。

* 任务记录、跟踪和分配
* 统一管理多个代码仓库的任务
* 任务可以和代码库工作相关，也可以无关
* 通过内置的工作流，可以实现代码库 issue & pr 任务的自动关联，状态同步
* 可以创建自定义字段的视图，用于不同目的的跟踪，支持任务清单，ToDoList 等视图。

下一步邀请社区网站工作组召开项目启动会。

## 版本化开发环境

初始化上面所创建的项目文件夹。将其推送到 [https://github.com/DevopsChina/drupal-dev.git](https://github.com/DevopsChina/drupal-dev.git)

先参考 Drupal 代码库 web 目录下的样例文件，在项目目录中创建 .gitignore 文件。应该在这两个文件中排出以下文件，处于演示目的，本项目并没有将其排除在外。

* .env
* sites/*/settings*.php
* sites/*/services*.yml

执行下面的代码推送动作。

```sh
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/DevopsChina/drupal-dev.git
git push -u origin main

```

在完成了代码库初始化工作后，会设置一下 main 主干保护策略。防止直接对 main 的变更。

## 容器化 Drupal 系统

容器化当前的项目需要经过这些操作步骤：

1. 确认当前 Drupal 系统中的配置和内容，这个状态会打包到容器环境中。用 sqldump 导出数据库。
2. 参数化 `web/sites/settings.php` 文件，将变量和密码变成参数。
3. 创建 Drupal 主应用镜像的 `Dockerfile` 。
4. 创建包含数据库服务和开发工具服务的 `docker-compose.yml` 服务定义文件。
5. 在本机测试和确认容器服务中 Drupal 网站的可用性和内容。

### 1 - 确认当前系统状态

在经过初始化的配置后，几乎所有系统级别配置信息都保存在了 MySQL 数据库中，用 sqldump 导出 MySQL 数据库，dump 文件会用于 MySQL 容器服务的初始化文件。字段定义、文章编辑、初始化内容的填充也会产生一些数据文件（图片、文件、视频、音频），这些文件就位于 `web/sites/default/files/` 目录中。

```sh
mkdir sql
mysqldump -u root local_devopschina > sql/dump.sql

```

在项目文件夹中，执行以上命令，就可以得到的到一个大约十几兆的 MySQL 数据库备份文件。

### 2 - 参数化 Drupal 主配置文件

Drupal 的数据库链接字符串和账号信息都位于  `web/sites/settings.php` 文件中。为了确保 Drupal 镜像启动后可以链接到正确的 MySQL 数据库服务。需要改此文件。

原始配置参数：

```php
$databases['default']['default'] = array (
  'database' => 'local_devopschina',
  'username' => 'ddoc',
  'password' => 'ddoc123',
  'prefix' => '',
  'host' => '127.0.0.1',
  'port' => '33067',
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
);

```

备份原始配置文件。由于修改以后在本机用 drush 运行的本地测试 Drupal 应用就中断了。后续可以优化一下：保持原始配置文件不变，参数化一个配置文件的副本，在 Drupal 打包过程中加一个参数化配置文件的覆盖替换动作。

修改为如下内容：

```php
$databases['default']['default'] = array (
  'database' => $_ENV['DBASE'],
  'username' => $_ENV['USER'],
  'password' => $_ENV['PASS'],
  'prefix' => '',
  'host' => $_ENV['HOST'],
  'port' => $_ENV['DPORT'],
  'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql',
  'driver' => 'mysql',
);
```

以上参数化非必要的最佳操作，本文目标在与记录，后续会优化这个步骤。

### 3 - 创建 Drupal 主应用镜像

基于 Drupal 官方的镜像文件创建适合自己项目的 `Dockerfile`。

```dockerfile
FROM drupal:9-php7.4-apache
RUN set -eux; \
 apt-get update; \
 apt-get install -y --no-install-recommends git
```

然后运行 docker build 命令，确认本地可以成功构建这个自定义镜像。

```sh
docker build -t devopschina/drupal-dev .
docker image
```

本测试镜像创建成功后，没有镜像上传的动作，镜像上传到特定的镜像仓库后，就可以实现在云容器服务中的部署。这里省略此 push 步骤。

### 4 - 创建服务定义文件

为了简化本地测试，这里使用 docker-compose 工具。创建包含数据库服务和开发工具服务的 `docker-compose.yml` 服务定义文件。

```yml
version: '3.1'

services:
  # 使用 mysql 作为后端数据库
  db:
    image: mysql:5.7
    container_name: devopschina_db
    restart: always
    volumes:
      # 用本地当前路径 sql 目录中的 sql dump文件初始化 MySQL 数据库
      - ./sql:/docker-entrypoint-initdb.d/
    environment:
      # 用这些环境变量初始化 mysql 数据库，创建目标数据库，创建用户和密码，为 root 用户初始化随机密码
      MYSQL_DATABASE: "${DB}"
      MYSQL_USER: "${DBU}"
      MYSQL_PASSWORD: "${DBP}"
      MYSQL_RANDOM_ROOT_PASSWORD: "1"
  # PHPMyAdmin 数据库管理工具，只用于开发或者测试环境
  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: devopschina_myphpadmin
    restart: always
    environment:
      PMA_HOST: "${DBH}"
      PMA_USER: "${DBU}"
      PMA_PASSWORD: "${DBP}"
      PMA_ARBITRARY: "1"
    ports:
      - 9999:80
  # 使用 drupal 官方镜像 v9 ，指定 php 版本为 7.4
  drupal:
    #image: drupal:9-php7.4-apache 这里以后需要优化为私有镜像名称，而不需要在服务启动的时候做任何构建
    build: .
    container_name: devopschina_drupal
    restart: always
    ports:
      - 9998:80
    working_dir: /opt
    volumes:
# 将当前项目目录加载到容器中，这里产生了一个和本机的依赖，后续优化：通过 Dockerfile 的复制当前开发目录中的成功到容器中
# The 'z' option tells Docker that the volume content will be shared between containers. Docker will label the content with a shared content label. Shared volumes labels allow all containers to read/write content. The 'Z' option tells Docker to label the content with a private unshared label.
      - .:/opt:z
    environment:
      HOST: "${DBH}"
      DBASE: "${DB}"
      USER: "${DBU}"
      PASS: "${DBP}"
# composer update 操作确保容器中的 Drupal 服务运行与当前的最新状态，这个操作也应该后续移植到Dockerfile 文件中
    command: bash -c "composer update && rm /var/www/html && ln -s /opt/web /var/www/html && /usr/local/bin/apache2-foreground"

```

相关测试命令：

* `docker-compose config` 测试所有参数是否被完整且正确的填充，有错误的话，需要修改 .env 文件。
* `docker-compose build` 构建必要的镜像。

### 5 - 本地集成测试

在本机测试和确认容器服务中 Drupal 网站的可用性和内容。

在项目目录中，执行 `docker-compose up` 命令观察整个启动过程，待启动停止后，在浏览器中访问：<http://localhost:9998> ，应该能够看到如下的网页。

![Test Env home page](img/cos/2022-02-05-2022-02-05_23-04-12.png)

## 在云平台部署社区官网

下面是关于后续工作的一些规划：

* 组件新的网站开发团队，召开项目启动会
* 优化以上代码库
* 用一台云主机搭建一个公共的测试环境
* 确认和实施相关基础设施：镜像仓库、用于Drupal迁移的对象存储桶、优化容器化过程、启用一个用于开发评审的容器测试环境、确定生产环境的运行状态【LAMP单机 vs. 容器环境+其它云服务】
