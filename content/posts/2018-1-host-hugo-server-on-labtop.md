---
title: "Host a Hugo Server on Labtop"
date: 2018-01-04T07:33:32+08:00
draft: false
subtitle: "把笔记本上的Hugo站点分享给局域网里的其它人"
categories: "blog"
tags: ["hugo"]
bigimg: [{src: "http://martinliu.qiniudn.com/images/abstract-3.jpg"}]
---

# 将笔记本上的Hugo站点分享给局域网里的其他人

我的笔记本上有好几个Hugo做的静态的站点，有自己的个人Blog，有公司产品的培训文档；其中的有些站点内容，有可能是不方便发布到Internet上，有可能是你的观众并没有条件访问Internet，但是使大家同在一个局域网里是一个很现实很方便的做法。那么怎样以最小的代价实现这个需求呢？

## 选择Hugo服务器启动参数

为了满足以上需求，在启动Hugo服务器的时候需要增加两个参数，如下所示：

```
martin@bogon:source/martinliu-hugo ‹master*›$ hugo server --bind 192.168.1.107 --baseURL http://192.168.1.107/
Started building sites ...

Built site for language en:
0 draft content
0 future content
0 expired content
387 regular pages created
1100 other pages created
0 non-page files copied
668 paginator pages created
509 tags created
37 categories created
total in 922 ms
Watching for changes in /Users/martin/source/martinliu-hugo/{content,static,themes}
Serving pages from memory
Web Server is available at http://192.168.1.107:1313/ (bind address 192.168.1.107)
Press Ctrl+C to stop
```

对以上参数的解释：

* --bind 192.168.1.107 ：这个192的IP地址是笔记本目前局域网（Wifi）的地址，其他人需要和你同在这个局域网里，或者能够访问到这个网段的地址
* --baseURL http://192.168.1.107/ ： 这会覆盖Hugo站点里根目录下配置文件里的baseURL参数，有可能配置文件中这个参数是类似于 http://martinliu.cn/ ，如果不加这个参数的话网站上的相关图片会显示不出来。

## 配置笔记本电脑的防火墙

以macOS为例，当你启动了这个Hugo服务器的时候，你访问 Security & Privacy 配置的时候，选择 Firewall 标签的时候，会自动弹出一个对话框，询问是否允许 incoming 的网络连接到 hugo 的应用服务。点击允许即可，这样防火墙配置里就多了一条配置，如下图所示：

![firewall](http://martinliu.qiniudn.com/images/hugo-firewall-rule.jpeg)

## 总结

Hugo可以很方便的将本地站点分享给局域网里的其它人，只需要在启动的时候加上适当的参数，配置好本机的防火墙策略即可。