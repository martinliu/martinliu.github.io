---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2011-02-10T17:12:30Z
subtitle: 在64位windows服务器上安装ARS7.5所需要了解的一些注意事项和技巧
slug: 64-windows-ars-75-install-tips
tags:
  - ARS
  - itsm
  - remedy
title: 在64位Windows上安装ARS7.5
url: /2011/02/10/64-windows-ars-75-install-tips/
wordpress_id: 50930
---

![ARS 7.5 安装](data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBggGBQkIBwgKCQkKDRYODQwMDRoTFBAWHxwhIB8cHh4jJzIqIyUvJR4eKzssLzM1ODg4ISo9QTw2QTI3ODUBCQoKDQsNGQ4OGTUkHiQ1NTU1NTU1LzU1NTU1NTU1NS41NCw1NTQ0NTU1NTU1LDUpNDQ1NDUsNSwsMDQsNDU1Nf/AABEIADAAMAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAGBwMEBQIIAf/EADUQAAEDAwMCAwUFCQAAAAAAAAECAwQFERIAITEGEyJBYQdRcYGhFBUjMkJSYpGiscHR4fD/xAAYAQADAQEAAAAAAAAAAAAAAAACAwQFAf/EACERAAICAgICAwEAAAAAAAAAAAECABEDIRJBBDEiMnET/9oADAMBAAIRAxEAPwB4k2FzofqUqoyX1NMK+zRySEOJBzUoevAB9RqR6rOuVtbLOK47ACXEHZRXfe3vABB+R11VKolKMUfl/Sm/5/U/u/RQOjAqTu93uDU6miQ6vuEynl7d5RCSo/E2G3Hy1aV09TGFpXTmhElHxNvRiEqSPOxVcAEXFjvzqjKkqdRZZUEFJCUKbuL38h/HbXPUtb+6KO8+xHvitsIB8itaWx4rb2ve39L6qxKCCT1JAd0O5pR+oJlEdSJTxl0/LxLdBVISCd1EiwIA8gm+i+PIalx0Px3EuNLF0qSdjpXTejSlky01upLnIR3SpTy+x3LXI7OVsL/pva22q/sy60WquCG9kzCllTbLAOQQ8FWunjFKrLUQByfPnSWC5LKCqlqck0xubESuJEVUmSpTxeJcBSAApZFiSRYgW92q7lWQ5buEKxIOyj+nn/X11BFeEOnN0+UC1IintuoPiAI38uefI86ru1doKxTyFWOQvz/nz/tq5sAbYMzASNGWJE9CyVqUFeQSk/8AfM839NY3UNZiSGWaWAJDk5SQ1dRDYxOdyRvYY3G25Fjtqd6tuEfhWSpJuFWO/lcj04toUkSEOV2jOhfgL7hJKhz2zz6+vGhCfzIXptRuL5OIWTYnWSWEsOOQDHCcG5RWoOFJ2C8cMciN7cX0DxK6ilzFqh4wpkF3JFjmnPc5DK973JsRYE7bW005akntKBBSWUG99rW0lE06TWOr5UKA33pMh/FtGQTkbe8kDR5cS4FDKPcrykkfkbntMp0uhVs1aOw8unSUDvuJUSGnSoglQtsCMAL+eg1uroWpZ8ON7JCj7+Pjf+bXoaVFZnRXI8ptLrLqcVoUNiNJfq/2R1anyHpPT2MmCVfhxgSXkBR4FxuBsLlV9K8fOK4tE58BvksHXarhgoqzsb2SvG/qT5W4v5cawZT2cZlpSGwEvNhKsAlQuoA29222Pu+OvlRYqNInriVBtceS2QVNrSLjYEfQjUNPYnVeWxBgR1SpKlhSW0DxLCPGQPkkm+i8g/UxOPTi4wa9Rn6dTnXk1CXgG7ttB5WKU22HPAG1tQ+xHo+RUqz9/wA9h37Kxmph5RI7joXYEftAAKHxGuq71ZCqrBpLQcTVCBGMRQGfe/L2+ecttNP2dUGV0z0HTqZPLf2hnuKX2ySBm4pYG4G4CgD631zzXUheJmgFv3P/2Q==)刚才终于把 ARS 装上了。费了我两天的力气终于搞定了。错误其实很简单的，现象很多人都见过，ARS 在安装完所有的文件后，在系统中建完 ARS 的服务以后，会继续启动服务，才能做最后的程序文件导入的相关操作。

错误的现象是：在启动服务的时，安装程序一直停止在“Starting Remedy ARS services....”的屏幕，去 arerror 日志里面可以看到无法连接到 SQL 数据库的错误。

我的安装错误的原因其实很简单：

1. 如果是 64 为的 Windows 操作系统，默认的安装路径是 C:\Program Files (x86)\目录

2. Oracle 客户端没有正确的安装

解决的方法如下：

1. 修改 ars 默认的安装路径，尽量把它放在一个较短的而且没有特殊字符的路径里，如 D:\bmc\

2. ARS 7.5 sp6 支持的 Oracle 客户端是 32 位的，如果你在 64 位 OS 上安装的是 64 位的 Oracle 数据+客户端（sqlplus），那么默认的这个 64 为的客户端是不能用的，需要安装一个 62 位的客户端，而且需要时 10g 的，此版本也不支持 11g 的客户端；另外在安装 32 位的 oracle 客户端的时候最好也不要在路径中有特殊字符如符号和下划线之类的

ARS7.5 本身是 32 位的可支持程序，所以它所需要的 JDK 和 Oracle 都需要是 32 位的版本。如果你安装的是 7.6.04，就不需要考虑 32 位的问题，由于它本身就是 64 位的程序了，所以 JDK 和 Oracle 都需要使用相应的 64 为的程序。
