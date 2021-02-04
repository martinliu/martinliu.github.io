---
author: liuadmin
categories:
- Blog
comments: true
date: 2011-03-29T09:13:03Z
slug: how-to-configure-statusnet-default-language
tags:
- default language
- linux
- statusnet
- Ubuntu
- 中文
- 汉化
- 界面
title: How to configure statusnet default language
url: /2011/03/29/how-to-configure-statusnet-default-language/
wordpress_id: 51001
---

If you are playing with statusnet, I bet you could not change default language; English language just shows every where.
So I'd like to write a quick guide to show you how to change perferred langguage as zh_cn.
I have a Ubuntu server with only English language pack.
[bash]
root@lamp www/statusnet# locale -a
C
POSIX
en_GB
[/bash]

I searched  and install Chinese language pack by aptitide
[bash]
root@lamp www/statusnet# aptitude search language-pack-zh
p   language-pack-zh                                                                 - translations for language Chinese (dummy package)
p   language-pack-zh-base                                                            - translations for language Chinese (dummy package)
P   language-pack-zh-hans                                                            - translation updates for language Simplified Chinese
P   language-pack-zh-hans-base                                                       - translations for language Simplified Chinese
p   language-pack-zh-hant                                                            - translation updates for language Traditional Chinese
p   language-pack-zh-hant-base                                                       - translations for language Traditional Chinese
root@lamp www/statusnet# aptitude install language-pack-zh-hans-base
[/bash]

Then I checked it again
[bash]
root@lamp www/statusnet# locale -a
C
POSIX
en_GB
zh_CN.utf8
zh_SG.utf8
[/bash]

Ubuntu OS has translations for language Simplified Chinese right, then I go ahead to configure statusnet config.php file. It only needs one more line as below, you can use your own language.
[php]
$config['site']['language'] = 'zh_CN';
[/php]

The final step, you login statusnet as administrator and go to /admin/site. Then you will select your language from dropdown list. I spend a few days to fix this problem. Just today, I realized my problem is Ubuntu linux server does not have Chinese Language pack yet. Show you my art as below :)
[![如何配置statusnet默认为中文界面](http://7bv9gn.com1.z0.glb.clouddn.com/wp-content/uploads/2011/03/statusnetzhcn-300x152.jpg)](http://martinliu.cn/2011/03/how-to-configure-statusnet-default-language.html/statusnetzhcn)

如何在Ubuntu上配置statusnet默认为中文界面
1）安装中文语言包
2）配置config.php的默认语言
3）statusnet管理员配置站点的默认语言
