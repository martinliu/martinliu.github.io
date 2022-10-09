---
title: 更新到 Jimmy Cai 的 Stack Hugo Theme
description:  上一个皮肤用了一段时间以后，发现作者已经停止更新很久了，而 Hugo 的版本和新功能还更新的挺快的，是时候给 blog 穿一件新衣服了。
slug: change-to-jimmy-stack-theme
date: 2022-10-09 00:00:00+0000
image: 2022-10-1-beijing-guomao.jpg
categories:
    - blog
tags:
    - hugo
    - github
    - HomeLab
---

趁着更新 Blog 皮肤的机会，也把我拖延很久的一些优化补一补。

最新版本的 Hugo 可以使用 Hugo modules 功能加载一个新的 Theme，我是第一次通过这种方式添加新皮肤，犯了几个错误：

1. 首先不应该用 `git clone theme-url theme/` 或者其他手工下载的方式了，应该使用文档中说的 `hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v3` 方法。
2. 在本地测试的话，需要确保本地的 Hugo 安装的是 extended 的扩展版本，否则有些短代码用不了。用这条命令检查 `hugo version` ，应该返回类似这样的信息：`hugo v0.104.2+extended darwin/arm64 BuildDate=unknown`

更新了 GitHub Action 的工作流，实现了如下的想法：

* deploy-2-page.yml : 在所有分支的 push 操作上触发构建动作，并且把更新的网站内容发布到 GitHub Pages 的部署分支中，用这个方式实现线上的网站内容预览；当新的分支在本地预览正常后，就可以 push 到远程了，push 之后就可以先在 martinliu.github.io 的域名下实现分支合并前的线上预览，如果线上预览正常的话，在进行合并分支 pr 的操作；如果线上预览有问题，则继续在本地更新，直到线上预览正常之后在合并。
* page-deploy.yml : 当 master 分支上收到 pr 时触发这个发布操作，我将 GitHub Pages 的免费空间当做了发布前的预览的空间；而网站的内容是通过 CloudFlare 的 Pages 功能 host 的。通过这种方式，将 GitHub 的所有功能和空间作为开发服务；而 CloudFlare 定位为 DNS 和静态内的生产环境。

根据这款新皮肤的提示，我查看了最新的 Hugo 的文档，为了发挥这个皮肤的图像 resize 功能，并且遵从新的编写 post 的规范。以后的所有新文章的 md 文件和图片文件都需要放到一个独立的新目录中。

新创建一篇 post 的时候使用这个命令：

```sh
hugo new content/post/new-blog-test/index.md
```

在站点的根目录下执行这条命令后，会帮你创建新的目录和 `index.md` 文件；由于我的站点默认使用了中文语言，因此，如果我想写一篇英文的文章的话，我就需要将 md 文件的名字写成 `index.en.md` ；这个皮肤支持双语的，如果这篇文章也有中英两个版本的话，md 文件就应该有两个：

* index.zh-cn.md
* index.en.md

这样就有了中英文的两个独立的页面，而且两种语言各自的页面上，都会有一个语言切换的按钮，所以这个皮肤对于双语，或者多语言写作的人来说，应该是非常顺手的一个选择。我将主导航的那些页面都做出了双语的版本。

由于，我最后的所有静态文件和图片都发布到了 CloudFlare 的 Pages 服务里，而且它们还提供 CDN 服务，而这个功能在 GitHub Pages 空间中是不提供的。因此，以前我用 GitHub Pages host 这个 blog 的时候，每次编写和发布新文章的时候，还需要手工的将图片上传到其它第三方的图床空间中，然后在更新 md 文章中图片的网址，其实还是比较繁琐和麻烦的。

这个国庆节期间，我基本上也完成了 home lab 的 Rack 搭建项目，初步效果如下：

![](new-rack.png)

以上这张图片放置在了和 md 文件相同的目录中，插入这张图片的代码就变得异常简单了 `![](new-rack.png)` ；而且图片也被拉伸到了和文章页面宽度等宽，大小合适的情况下会充满页面宽度，而且能够自适应浏览器显示器的宽度。

后续会出一些关于这个 home lab 的文章。

关于这个皮肤的使用文档，请访问： https://docs.stack.jimmycai.com/

如果你也喜欢这个风格的皮肤，请查看： [hugo-theme-stack-stater](https://github.com/CaiJimmy/hugo-theme-stack-starter)


遗留问题：

* 左上角的头像图片无法正常显示
* 添加一种免费好用的评论互动插件