+++
date = 2021-02-12T14:42:40+08:00
draft = true
title = "开源 IDS Suricata 4.1.10 新手部署指南"
description = "Suricata 是一款轻量的开源网络流量检测软件，它的周边社区开发了丰富的分析规则"
author = "Martin Liu"
categories = ["Security"]
slug = "suricata-centos7-filebeat"
tags = ["DevOps", "DevSecOps", "IDS", "Suricata"]
[[images]]
  src = "img/2021/flag01.jpg"
  alt = "Valley"
  stretch = "horizontal"
+++
本文基于 CentOS Server 7 环境安装和配置，文中提到的概念和知识也适用于 Suricata 的其它版本和操作系统。网络流量检测结果事件和告警结果使用 Filebeat 发送到 Elastic Stack 中，并使用 Kibana 可视化展示。
<!--more-->

![Suricata Logo](/img/2021/suri-400x400.png)

Suricata 是一款高性能的网络IDS、IPS和网络安全监控引擎。它是由the Open Information Security Foundation开发，是一款开源的系统。软件的源代码可以在它的官网： [http://suricata-ids.org/](http://suricata-ids.org/) 获得。

Suricata 可以作为入侵检测(IDS)引擎、在线入侵防御系统(IPS)、网络安全监控(NSM)以及离线pcap处理工具。它的工作原理是利用规则和签名检查网络流量，并支持Lua脚本来检测复杂的威胁。

![Suricata workflow](/img/2021/20190809183352238.png)

由于 Suricata 能够以 YAML 和 JSON 格式编写日志，因此它可以与其他工具集成，如SIEM、Splunk、Logstash/Elasticsearch、Kibana等，以实现进一步的日志处理和可视化。



## 网络环境介绍

如果是纯粹功能性的测试，你几乎可以在任何操作系统上安装和运行 Suricata 应用，在 Debian 或者 CentOS/RHEL 下使用二进制安装包可能是最快的方法。在单网卡的操作系统里，就能够测试它的所有功能。

在我的实验环境里有一个可网管的交换机，因此可以用端口镜像的方式

The following HTML `<h1>`—`<h6>` elements represent six levels of section headings. `<h1>` is the highest section level while `<h6>` is the lowest.

# H1
## H2
### H3
#### H4
##### H5
###### H6

## Paragraph

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Blockquotes

The blockquote element represents content that is quoted from another source, optionally with a citation which must be within a `footer` or `cite` element, and optionally with in-line changes such as annotations and abbreviations.

#### Blockquote without attribution

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Note** that you can use *Markdown syntax* within a blockquote.

#### Blockquote with attribution

> Don't communicate by sharing memory, share memory by communicating.</p>
> — <cite>Rob Pike[^1]</cite>

[^1]: The above quote is excerpted from Rob Pike's [talk](https://www.youtube.com/watch?v=PAAkCSZUG1c) during Gopherfest, November 18, 2015.

## Tables

Tables aren't part of the core Markdown spec, but Hugo supports supports them out-of-the-box.

   Name | Age
--------|------
    Bob | 27
  Alice | 23

#### Inline Markdown within tables

| Inline&nbsp;&nbsp;&nbsp;     | Markdown&nbsp;&nbsp;&nbsp;  | In&nbsp;&nbsp;&nbsp;                | Table      |
| ---------- | --------- | ----------------- | ---------- |
| *italics*  | **bold**  | ~~strikethrough~~&nbsp;&nbsp;&nbsp; | `code`     |

## Code Blocks

#### Code block with backticks

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example çΩzzz Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
```

e
ddddd

e

e
e
e
e

e


eeee

ççççccccccccccccccccççççççcccccc√√√√√√√√ççççccccccccccccccccççççççcccccc

<iframe width="800" height="600" src="//player.bilibili.com/player.html?aid=797592076&bvid=BV1zy4y1r7qT&cid=250759042&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

#### Code block indented with four spaces

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Example HTML5 Document</title>
    </head>
    <body>
      <p>Test</p>
    </body>
    </html>

#### Code block with Hugo's internal highlight shortcode
{{< highlight html >}}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Example HTML5 Document</title>
</head>
<body>
  <p>Test</p>
</body>
</html>
{{< /highlight >}}

## List Types

#### Ordered List

1. First item
2. Second item
3. Third item

#### Unordered List

* List item
* Another item
* And another item

#### Nested list

* Item
    1. First Sub-item
    2. Second Sub-item

## Other Elements — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Delete</kbd></kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.

