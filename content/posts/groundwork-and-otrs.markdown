---
author: liuadmin
categories:
- NSM
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

为了节省服务器，我们可能不得不把所有的监控以及相关的系统都安装到一个物理的机器上。如果是从原代码安装，我相信一定有很多选项能避免它们之间的冲突。假如你是后安装的GroundWork，它会更改系统默认的Apache2的配置，导致以前安装的所有的Web应用都不能用。<br /><br />在我的测试机上，先安装的OTRS，rpm安装，后安装的GroundWork，也是rpm安装。GroundWork安装之后，OTRS不能登陆。根据GroundWork的一些文档我做了，如下的修复步骤。<br />1）vi /etc/apache2/conf.d/otrs.conf  可以看到如下OTRS的web配置信息。<br /># --# added for OTRS ([http://otrs.org/](http://otrs.org/))# --# agent, admin and customer frontendScriptAlias /otrs/ "/opt/otrs/bin/cgi-bin/"Alias /otrs-web/ "/opt/otrs/var/httpd/htdocs/"# load all otrs modulesPerlrequire /opt/otrs/scripts/apache2-perl-startup.pl# Apache::Reload - Reload Perl Modules when Changed on DiskPerlModule Apache2::ReloadPerlInitHandler Apache2::ReloadPerlModule Apache2::RequestRec# set mod_perl2 options#  ErrorDocument 403 /otrs/customer.pl  ErrorDocument 403 /otrs/index.pl  SetHandler  perl-script  PerlResponseHandler ModPerl::Registry  Options +ExecCGI  PerlOptions +ParseHeaders  PerlOptions +SetupEnv  Order allow,deny  Allow from all# directory settings    AllowOverride None    Options +ExecCGI -Includes    Order allow,deny    Allow from all    AllowOverride None    Order allow,deny    Allow from all# MaxRequestsPerChild (so no apache child will be to big!)MaxRequestsPerChild 400<br />2）在GroundWork的主目录下其实也有一个Apache目录，它是原系统Apache的替代品。进入这个目录。<br />3）vi conf/httpd.conf 把otrs.conf文件中所有的内容都粘贴到这个文件中<br />4）GroundWork的apache好像没用用到perl模块，需要加入perl模块的支持；找到有很多“LoadModule”的地方加入下面这一行<br />LoadModule perl_module modules/mod_perl.so<br />5）Copy系统中的mod_perl.so文件到/usr/local/groundwork/apache2/modules<br />6）重新启动gwhttpd服务，也就是GroundWork系统的web服务<br />7）访问OTRS系统 [http://ip/otrs/customer.pl](http://ip/otrs/customer.pl)   成功。<br /><br />下面需要做的是把OTRS的登陆也集成到GroundWork的单点登陆当中；如果在能把GroundWork的报警也自动的集成到OTRS那就是完美了，欲知后事如何，且听下回分解。：）<br /><br />
