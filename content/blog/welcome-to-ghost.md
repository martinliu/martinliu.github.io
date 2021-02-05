---
title: 切换到Ghost+七牛
subtitle: 折腾
date: 2017-09-21
tags: ["blog"]
bigimg: [{src: "/images/abstract-12.jpg"}]
---




在经历了一个很长的周期之后，我的blog又回到了最原始的状态。很早以前学习网页开发的时候，用写字板编写html代码，后来是Asp，工作以后是用Blogspot，之后是WordPress，然后是Jekyll+github，现在是Ghost+七牛。

4个拐点

我的blog经历了四个转折点，下面稍微说下，为啥选择了某个平台，为啥后来又放弃了。

1.     免费博客平台：最初我试用了几个国内外免费的服务，最后发现Blogspot的体验要优于其他所有平台，而且具备一定的定制能力，还没有广告。然后就一直用到了Blogspot被墙的时候，那时候我还没有买域名。记得MSN的Space也用过，如果你没有用过MSN的话，当我没说这句话。总之免费blog空间的弊端就是，你码的字和图片是给别人的，不属于你自己，没有延续性。

2.     WordPress：是我用的时间最长的平台，它的好处是可以host在任何php虚拟空间和云主机上；优势就是功能强。曾经浪花费了大量的时间，在测试和感受各种插件和皮肤上。而且WP的搬家工作也容易，因此换了很多个空间，一共有多少个主机空间现在已经都忘了。放弃WP的原因：维护LAMP堆栈的工作量还是有的，即使在PHP的虚拟空间里，这个系统的优化工作还是持续不断的要做的，否则网站速度会很慢，而且时快时慢，网站的访问性能其实无法保证。因此在这个过程中必须使用CDN服务，七牛的wp插件是我用的最长时间的，因此我早期的blog的图片都在七牛上，它给我了一个备份和加速图片的福利。性能不稳定，页面打开速度慢是放弃它的主要原因。

3.     Jekyll+GitHub：选择这个组合，开始于我重度使用Github的时候。而且macOS上安装Jekyll这种静态blog程序很方便，捣鼓起来之后，就感觉比WP方便简单直接多了。发现这个方式非常轻量和简洁。而且Github.io的免费静态网站host服务还支持自定义域名。因此，我做了把之前所有WP的文章导出为MD格式文档的数据迁移工作。由于之前WP文章里的图，已近都存放在七牛里了，因此这次我做了一个出乎意料敏捷轻松的转身。使用过程中，逐渐发现了Jekyll的各种不足，界面和格式的定制工作还是有的，即使用几十刀买的皮肤都会让你用到难以忍受，毕竟不是想developer那样天天写代码，也逐渐感到Jekyll的简洁变成了简陋。代码定制的工作量和难度大是放弃它的主要原因。

4.     Ghost+七牛：其实早就瞄上Ghost了，可是一种没有下决心换。直到最近我开始把Ghost安装在Mac OS的笔记本电脑上，发现在本机编辑和维护文章资料，速度飞快，和以前WP在线编辑简直是天壤之别。如果Ghost应用跑在自己的笔记本电脑上的话，既可以离线工作，像之前用Jekyll+Github组合一样，也更可以不需要购买任何虚拟主机和空间了，在本机离线工作的速度和效率好，而且稳定太多了。 buster这个程序是这次切换到Ghost的催化剂，它可以把Ghost网站的全站导出成静态文件，线上就只需要一个CDN空间了。七牛的qshell工具可以方便地把本地的静态网站文件夹，同步到CDN的buckte存储中。切换到这个方案的原因是：网站变为纯静态网页，全站html/css和图片全面上CDN，配置全球加速网站域名，享用七牛的免费套餐。

下面花一点篇幅介绍一下目前的blog环境细节。简单地说：目前是在笔记本上跑Ghost服务器，这样就省去了云主机和虚拟主机空间的需求，把ghost的站点导出为静态网页和图片，然后增量地上传到七牛的CDN上去。
Ghost本地安装

我的操作系统是MacOS，用的是2017款MBP。

先安装node.js，进入https://nodejs.org/en/ 在网站的首页上就可以下载到安装包，下载安装即可。也可以用 brew 安装。安装完了以后就获得了 npm 包管理程序。

之后参考https://docs.ghost.org/v1.0.0/docs/install#pre-requisites 的文档安装 ghost-cli ； 然后用ghost的命令行来实现ghost程序的安装和升级。

用ghost-cli安装ghost服务器的时候，要选择local的方式，它会使用sqllite作为数据库，这样做管理和维护Ghost应用栈的工作就都在本地了。

ghost服务器的初始化 ghost install local 这个命令会问你几个问题，全都用默认即可。安装完之后就可以看到服务器运行的状态了。

```
martin@mbp ghost status
Process manager 'systemd' will not run on this system, defaulting to 'local'

│ Name      │ Location       │ Version │ Status               │ URL                    │ Port │ Process Manager │

│ localhost │ ~/source/ghost │ 1.8.7   │ running (production) │ http://martinliu.cn/ │ 2368 │ systemd         │
```

这样就表明本地安装成功，访问 http://martinliu.cn/ghost 建立管理员账户，登录以后，就可以在本地编辑和维护blog文章了。
Buster安装和使用

Buster的安装也很简单，网上有很多安装使用攻略，此处忽略。我用下面的命令来把Ghost网站做导出：

```
buster generate --new-domain=martinliu.cn

```
在ghost的根目录下运行这个命令，就可以把本地的ghost网站都导出到一个名为static的目录里。可以直接在这个目录里打开这些html纯静态的网页，可以浏览和验证格式是否正常，一般不需要这样做，格式一般不会出错的。
配置七牛CDN

七牛提供了本地的qshell，用于上传和同步文件到云端的存储里。安装过程文档见 https://github.com/qiniu/qshell

我在ghost的根目录下，编辑了一个上传网站的配置文件upload.conf，内容如下：

```
{
   "src_dir"            :   "/Users/martin/source/ghost/static",
   "access_key"         :   "XXXXXXXkAA9TYrcDmQPBAAcB7",
   "secret_key"         :   "XXXXXXXXXXXXXXXXXXXXXndwt",
   "bucket"             :   "martinliu-cn"，
   "ignore_dir"         :   false,
   "overwrite"          :   true,
   "check_exists"       :   true,
   "check_hash"         :   true,
   "rescan_local"       :   true,
   "log_file"           :   "./upload.log",
   "log_level"          :   "info",
   "log_rotate"         :   1,
   "log_stdout"         :   true,
   "file_type"          :   0
}

```
以上这个配置很重要，它的目的是实现：

*     增量上传
*     修改的文件覆盖上传

感谢七牛的工程师茅工，在我调试以上需求的时候，给我提供了及时的帮助。而且七牛的免费账户也可以开工单获取技术支持，支持的响应速度还不错。

这样执行 qshell qupload 10 upload.conf 既可以完成一次上传同步工作，这个步骤是唯一需要在线操作的步骤。这条命令的输出结果如下：

```
2017/09/25 00:00:21 [I] File `tag/cloud/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/coding/index.html => tag/coding/index.html [113/119, 95.0%] ...
2017/09/25 00:00:21 [I] File `tag/coding/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/devops/index.html => tag/devops/index.html [114/119, 95.8%] ...
2017/09/25 00:00:21 [I] File `tag/devops/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/getting-started/index.html => tag/getting-started/index.html [115/119, 96.6%] ...
2017/09/25 00:00:21 [I] File `tag/getting-started/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/journey/index.html => tag/journey/index.html [116/119, 97.5%] ...
2017/09/25 00:00:21 [I] File `tag/journey/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/opensource/index.html => tag/opensource/index.html [117/119, 98.3%] ...
2017/09/25 00:00:21 [I] File `tag/opensource/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/tag/running/index.html => tag/running/index.html [118/119, 99.2%] ...
2017/09/25 00:00:22 [I] File `tag/running/index.html` exists in bucket, hash match, ignore this upload
Uploading /Users/martin/source/ghost/static/test.html => test.html [119/119, 100.0%] ...
2017/09/25 00:00:22 [I] File `test.html` exists in bucket, hash match, ignore this upload
2017/09/25 00:00:22 [I] -------------Upload Result--------------
2017/09/25 00:00:22 [I]               Total:       119
2017/09/25 00:00:22 [I]             Success:         0
2017/09/25 00:00:22 [I]             Failure:         0
2017/09/25 00:00:22 [I]        NotOverwrite:         0
2017/09/25 00:00:22 [I]             Skipped:       119
2017/09/25 00:00:22 [I]            Duration:  36.533056019s
2017/09/25 00:00:22 [I] ----------------------------------------

See upload log at path ./upload.log

```
七牛的域名配置如下图所示：
![Google-Chrome-5](/images/Google-Chrome-5.jpg)



### Blog工作流

下面就是我目前的blog工作流程说明。

*     启动本地的ghost服务器，开始编辑和维护blog文章，如新写一篇blog；其实我也根本就不关这个服务器，感觉它也没有什么消耗。这样的话飞机上的无聊时间，可以彻底得到充分利用了。
*     在本地发布和预览blog文章和内容，修订并定稿。
*     运行Buster命令导出全站文章到本地。
*     在想更新上线新内容的时候，在联网的情况下，运行qshell上传同步命令，把本地static文件夹和七牛上的存储bucket同步一下。

至此我完成了从动态blog到纯静态blog的转型，现在网页html和图片文件全都在七牛的CDN里，而且域名 martinliu.cn 的访问配置成了全球加速。

目前使用的是七牛的免费流量和空间套餐，套餐内的各种数量限制如下。


![Screen-Shot-2017-09-23-at-11.21.57-A](/images/Screen-Shot-2017-09-23-at-11.21.57-AM.png)



目前的疑问是这个免费套餐是否够用，不知道这个羊毛多久会被我薅完。我会定期在本文跟新以上解决方案，在使用期间的各种配置细节变更，或者遇到的问题和解决方法。

TO-Do

    把static变成一个git库，以后配置Jenkins，基于它的变化，自动化触发后续的更新和上传动作
    在上传前运行htlm和css文件的压缩工具（命令行执行），优化页面尺寸
    在上传前运行图片的压缩工具（命令行执行），优化图片尺寸
    在Ghost里加入评论功能
    加入Google网站统计代码
    测试Ghost网站备份和迁移过程，保证当前的ghost服务器崩溃了，数据不会丢失

