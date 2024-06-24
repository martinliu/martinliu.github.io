+++
title = "在 Github 上搭建基于 Hugo 的免费个人博客"
description = "GitHub-pages 功能承载个人博客内容，GitHub Actions 功能实现自动化部署。Hugo 为你提供博客所需要的所有功能。"
author = "Martin Liu"
date = "2021-02-06"
tags = ["github", "ci", "cd", "github-pages"]
categories = ["blog", "Devops"]
image = "img/2019/03/pic03.jpg"
slug = "github-hugo-blog"
+++

最近更新了新的博客样式，再次搬迁回到了 GitHub 平台，并使用了 Github Action 的自动化 CI/CD 发布功能。这个是一个任何人都可以拥有的方案，现在用最简洁的语言分享给大家。
<!--more-->

选择将博客搭建在 Github 上的原因包括：

* Github Pages 是一个免费使用的功能，在不强求网站访问速度，考虑持久性的情况下，Github Pages 不失为一根优秀的羊毛。
* 用 master 分支管理 hugo 站点的所有代码和文件（markdown、网站模板和图片），用 gh-pages 分支存放 Hugo 编译后的网站发布文件
* Github Actions 功能实现了自动化的编译和部署功能，使用它所提供的工作流将 master 分支中的更新编译后发布到 gh-pages 分支中

而 Hugo 是一款比较流行的静态网站管理软件，可以在各种操作系统轻松的安装本地的博客环境，在本地的操作系统上实现博客的预览和测试。Hugo 的社区提供了大量的免费网站模板，不同类型的模板可以满足各种网站需求。

## 选择 Hugo 博客主题

在 https://themes.gohugo.io/ 可以搜索到大量的免费网站模板。我这次选择了名为 “HUGO FUTURE IMPERFECT SLIM” 的模板。

这是一个功能非常丰富的模板：

* 界面简洁，兼具丰富的格式，博客文章有头图
* 带有侧栏
* 带有 ‘about’ ‘categories’ ‘contact’ 等独立页面格式，无头图
* 具有多语言支持和菜单选择
* 带有搜索页面
* 带有讨论功能

对我而言这些都是很快就都可以用到的功能。

Hugo 博客本地安装和配置新手指南，参考这两篇文章。

1. [零基础使用 Hugo 和 GitHub 搭建个人博客](https://zhuanlan.zhihu.com/p/102131163)
2. [使用 Hugo 生成静态博客教程](https://sb.sb/blog/migrate-to-hugo/)

## GitHub Pages 新手指南

在 https://pages.github.com/ 提供了视频和文字版本的新手指南教程。为了方便新手理解，下面就使用‘user or organization site’这个最常用的选项做简要说明：

1. 创建与自己的 **Github 用户/组织** 同名前缀的公开代码仓库，例如：zhangsan/zhangsan.github.io
2. 选择在命令行里（前提是安装配置好了 Git，否则使用图形化界面 GitHub Desktop 工具）
3. 克隆第一步创建的那个代码库到本地电脑的目录中。
4. 创建只包含 ‘Hello World’ 为内容的主页测试文件。
5. 推送本地的更新到 Github 服务器端
6. 在本地的浏览器中查看测试网页 http://zhagnsan.github.io/

GitHub Pages 的新手指南已经包含在了上一节推荐的两篇文章中。

## 使用 Github Actions 自动化发布博客更新

本地的测试环境是非常重要的，可以帮我们快速的掌握 Hugo 的基本使用方式，测试和选择网站模板。在模板确定了以后，就进入了日常的内容更新过程中，平常内容更新的工作都是在 master 分支中进行。并不会在本地操作 gh-pages 分支，这个分支里只会存放的是 Hugo 编译之后结果内容，即 public 目录中的内容。

你可以在代码库的 Actions 标签页面中，创建一个默认的演示工作流文件，在本地做一个测试更新，用 push 动作测试触发和执行它。从无到有的创建新工作流文件的过程在这里不讲解。

在本使用 Github Actions 的功能的主要目的如下：

1. 通过 master 分支的 push 事件，触发自动化工作流，即 CI/CD 工作流，这里是持续部署的过程。
2. 将 master 分支的内容签出，使用新配置的 Hugo 软件构建全站的所有内容
3. 将构建后的结果发布更新到 gh-pages 分支中。

下面是我所使用的工作流代码和注释。

```
# 将 Hubo 博客构建后部署到 Github Pages
name: Deploy github-pages

# 在 master 主干分支的任何 push 事件都会触发本 DevOps 工作流水线
on:
  push:
    branches: [ master ]

# 以下是本串行执行工作流的所有组成部分
jobs:
  # 这里只定义了一个名为 "deploy" 的多步骤作业
  build-deploy-hugo-blog:
    # 将后续的所有工作步骤都运行在最新版的 ubuntu 操作系统上
    runs-on: ubuntu-latest

    # 本构建和部署作业的所有步骤定义如下
    steps:

    # Step 1 - Checks-out 你的代码库到 $GITHUB_WORKSPACE
    - name: Checkout blog code repo
      uses: actions/checkout@v2 # 这是 Github 官方提供的一个动作模块
      with:
          submodules: true  # 同步更新所使用的 Hugo 模板
          fetch-depth: 0    # 更新到该模板最新的版本

    # Step 2 - 配置最新版本的 Hugo 环境
    - name: Setup Hugo
      uses: peaceiris/actions-hugo@v2  # 这是 Github Actions 市场中的一个动作模块
      with:
          hugo-version: 'latest'

    # Step 3 - 清理代码库中 public 目录中的内容
    - name: Clean public directory
      run: rm -rf public  # 彻底删除这个目录

    # Step 4 - 用最新版本的 Hugo 构建个人博客站点
    - name: Build blog site
      run: hugo --minify

    # Step 5 - 创建用于私有域名所需要的 CNAME 文件
    - name: Create CNAME file
      run: echo 'martinliu.cn' > public/CNAME

    # Step 6 - 将构建好的博客站点推送发布到 gh-pages 分支
    - name: Deploy blog to Github-pages
      uses: peaceiris/actions-gh-pages@v3
      with:
          github_token: ${{ secrets.DEPLOY_KEY }}
          publish_dir: ./public
```


## 后续事项

1. 解决旧文章头图空白的问题
2. 增加文章评论功能
3. 增加 CDN 功能

