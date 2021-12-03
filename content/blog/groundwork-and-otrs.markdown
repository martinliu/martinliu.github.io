---
author: Martin Liu
categories:
  - itsm
comments: true
date: 2007-02-27T09:40:00Z
slug: groundwork-and-otrs
tags:
  - GroundWork
  - OTRS
title: GroundWork和OTRS系统的集成问题
url: /2007/02/27/groundwork-and-otrs/
wordpress_id: 49143
---

为了节省服务器，我们可能不得不把所有的监控以及相关的系统都安装到一个物理的机器上。如果是从原代码安装，我相信一定有很多选项能避免它们之间的冲突。假如你是后安装的 GroundWork，它会更改系统默认的 Apache2 的配置，导致以前安装的所有的 Web 应用都不能用。<br /><br />在我的测试机上，先安装的 OTRS，rpm 安装，后安装的 GroundWork，也是 rpm 安装。GroundWork 安装之后，OTRS 不能登陆。根据 GroundWork 的一些文档我做了，如下的修复步骤。<br />1）vi /etc/apache2/conf.d/otrs.conf 可以看到如下 OTRS 的 web 配置信息。<br /># --# added for OTRS ([http://otrs.org/](http://otrs.org/))# --# agent, admin and customer frontendScriptAlias /otrs/ "/opt/otrs/bin/cgi-bin/"Alias /otrs-web/ "/opt/otrs/var/httpd/htdocs/"# load all otrs modulesPerlrequire /opt/otrs/scripts/apache2-perl-startup.pl# Apache::Reload - Reload Perl Modules when Changed on DiskPerlModule Apache2::ReloadPerlInitHandler Apache2::ReloadPerlModule Apache2::RequestRec# set mod_perl2 options# ErrorDocument 403 /otrs/customer.pl ErrorDocument 403 /otrs/index.pl SetHandler perl-script PerlResponseHandler ModPerl::Registry Options +ExecCGI PerlOptions +ParseHeaders PerlOptions +SetupEnv Order allow,deny Allow from all# directory settings AllowOverride None Options +ExecCGI -Includes Order allow,deny Allow from all AllowOverride None Order allow,deny Allow from all# MaxRequestsPerChild (so no apache child will be to big!)MaxRequestsPerChild 400<br />2）在 GroundWork 的主目录下其实也有一个 Apache 目录，它是原系统 Apache 的替代品。进入这个目录。<br />3）vi conf/httpd.conf 把 otrs.conf 文件中所有的内容都粘贴到这个文件中<br />4）GroundWork 的 apache 好像没用用到 perl 模块，需要加入 perl 模块的支持；找到有很多“LoadModule”的地方加入下面这一行<br />LoadModule perl_module modules/mod_perl.so<br />5）Copy 系统中的 mod_perl.so 文件到/usr/local/groundwork/apache2/modules<br />6）重新启动 gwhttpd 服务，也就是 GroundWork 系统的 web 服务<br />7）访问 OTRS 系统 [http://ip/otrs/customer.pl](http://ip/otrs/customer.pl) 成功。<br /><br />下面需要做的是把 OTRS 的登陆也集成到 GroundWork 的单点登陆当中；如果在能把 GroundWork 的报警也自动的集成到 OTRS 那就是完美了，欲知后事如何，且听下回分解。：）<br /><br />
