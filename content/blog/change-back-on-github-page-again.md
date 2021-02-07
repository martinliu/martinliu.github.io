+++
title = "在 Github 上搭建基于 Hugo 的免费个人博客"
description = "GitHub-pages 功能承载个人博客内容，GitHub Actions 功能实现自动化部署。Hugo 为你提供博客所需要的所有功能。"
author = "Martin Liu"
date = "2021-02-06"
tags = ["github", "ci", "cd", "github-pages"]
categories = ["blog", "Devops"]
[[images]]
  src = "img/2019/03/pic03.jpg"
  alt = "Valley"
  stretch = "horizontal"
+++

最近更新了新的博客样式，再次搬迁回到了 GitHub 平台，并使用了 Github Action 的自动化 CI/CD 发布功能。这个是一个任何人都可以拥有的方案，现在用最简洁的语言分享给大家。
<!--more-->

## 新主题

这次选择了名为 “HUGO FUTURE IMPERFECT SLIM” 的模板。

它的功能非常丰富：

* 界面简洁，兼具丰富的格式，博客文章有头图
* 带有侧栏
* 带有 ‘about’ ‘categories’ ‘contact’ 等独立页面格式，无头图
* 具有多语言支持和菜单选择
* 带有搜索页面
* 带有讨论功能

这些都是今后可以使用到的功能。

## 网站所在位置

DNS 使用 Cloudflare 解析，启用了完全 HTTPS 访问，附加 https 重定向的页面规则。

在 Github 上启用了 github-page 的自定义页面，并且支持 https 访问。

Github 上使用 master 作为开发分支，更新后部署到 gh-pages 分支。

## 网站的部署

部署使用了 Github Action 的功能。

```
# Workflow to build and deploy site to Github Pages using Hugo

# Name of Workflow
name: Deploy github-pages

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [ master ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "deploy"
  deploy:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:

    # Step 1 - Checks-out your repository under $GITHUB_WORKSPACE
    - name: Checkout
      uses: actions/checkout@v2
      with:
          submodules: true  # Fetch Hugo themes
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

    # Step 2 - Sets up the latest version of Hugo
    - name: Setup Hugo
      uses: peaceiris/actions-hugo@v2
      with:
          hugo-version: 'latest'

    # Step 3 - Clean and don't fail
    - name: Clean public directory
      run: rm -rf public

    # Step 4 - Builds the site using the latest version of Hugo
    # Also specifies the theme we want to use
    - name: Build
      run: hugo --minify

    # Step 5 - Create name file
    - name: Create cname file
      run: echo 'martinliu.cn' > public/CNAME

    # Step 6 - Push our generated site to our gh-pages branch
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
          github_token: ${{ secrets.DEPLOY_KEY }}
          publish_dir: ./public
```


#### 后续事项

1. 样式表加载问题
2. 就文章头图加载问题
3. 多分支工作

