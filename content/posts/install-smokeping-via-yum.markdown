---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-02-16T16:38:00Z
slug: install-smokeping-via-yum
tags:
- smokeping
- Yum
title: Install Smokeping via yum
url: /2007/02/16/install-smokeping-via-yum/
wordpress_id: 49140
---

From :[ http://ai.net.nz/horde/wicked/display.php?page=SmokePing](http://www2.blogger.com/img/gl.link.gif)<br />

## Install needed packages

<br />**rrdtool**<br />
```
`yum install rrdtool
```

```
<br />**perl-CGI-SpeedyCGI**<br />
```
`yum install perl-CGI-SpeedyCGI
```

```
<br />**fping**<br />
```
`yum install fping
```

```
<br />** Or do them all together:**<br />
```
`yum install rrdtool perl-CGI-SpeedyCGI fping
```

```
<br />**Smokeping**<br />
```
`wget http://people.ee.ethz.ch/~oetiker/webtools/smokeping/pub/smokeping-2.0.9.tar.gztar xvzf smokeping-2.0.9.tar.gzmv smokeping-2.0.9 /usr/local/smokepingchown -R root:root /usr/local/smokeping<br /><br />cd /usr/local/smokeping/binfor foo in *.dist; do cp $foo `basename $foo .dist`; done<br /><br />cd  /usr/local/smokeping/etc/for foo in *.dist; do cp $foo `basename $foo .dist`; done<br /><br />cd /usr/local/smokeping/htdocsfor foo in *.dist; do cp $foo `basename $foo .dist`; done
```

```
<br />**pico /usr/local/smokeping/bin/smokeping**<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >_**Default**_
</td><br />
<td class="table-cell" >_**New**_
</td><br /></tr><br /><tr ><br />
<td class="table-cell" > #!/usr/sepp/bin/perl-5.8.4 -w
</td><br />
<td class="table-cell" > #!/usr/bin/perl -w
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(/usr/pack/rrdtool-1.0.49-to/lib/perl);
</td><br />
<td class="table-cell" >use lib qw(/usr/lib64/perl5/vendor_perl/5.8.5/x86_64-linux-thread-multi/auto/RRDs);
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >** or if a i386 system use**
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(/usr/pack/rrdtool-1.0.49-to/lib/perl);
</td><br />
<td class="table-cell" >use lib qw(/usr/lib/perl5/vendor_perl/5.8.5/i386-linux-thread-multi/auto/RRDs);
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(lib);
</td><br />
<td class="table-cell" >use lib qw(/usr/local/smokeping/lib);
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >use Smokeping 2.000008;
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >Smokeping::main("etc/config.dist");
</td><br />
<td class="table-cell" >Smokeping::main("/usr/local/smokeping/etc/config");
</td><br /></tr><br /></table><br />**pico /usr/local/smokeping/htdocs/smokeping.cgi**<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >_**Default**_
</td><br />
<td class="table-cell" >_**New**_
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >#!/usr/sepp/bin/speedy -w
</td><br />
<td class="table-cell" >#!/usr/bin/speedy -w
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(/usr/pack/rrdtool-1.0.33-to/lib/perl);
</td><br />
<td class="table-cell" >use lib qw(/usr/lib64/perl5/vendor_perl/5.8.5/x86_64-linux-thread-multi/auto/RRDs);
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >** or if a i386 system use**
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(/usr/pack/rrdtool-1.0.49-to/lib/perl);
</td><br />
<td class="table-cell" >use lib qw(/usr/lib/perl5/vendor_perl/5.8.5/i386-linux-thread-multi/auto/RRDs);
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >use lib qw(/home/oetiker/data/projects/AADJ-smokeping/dist/lib);
</td><br />
<td class="table-cell" >use lib qw(/usr/local/smokeping/lib);
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >use CGI::Carp qw(fatalsToBrowser);
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >use Smokeping 2.000008;
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >Smokeping::cgi("/home/oetiker/data/projects/AADJ-smokeping/dist/etc/config");
</td><br />
<td class="table-cell" >Smokeping::cgi("/usr/local/smokeping/etc/config");
</td><br /></tr><br /></table><br />
```
`cp /usr/local/smokeping/htdocs/smokeping.cgi /var/www/cgi-bin<br /><br />pico /usr/local/smokeping/etc/config
```

```
<br />**etc/config**<br />*** General ***<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >_**Default**_
</td><br />
<td class="table-cell" >_**New**_
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >owner = Joe Random
</td><br />
<td class="table-cell" >owner = Tony Someone
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >contact = joe@some.place.xyz
</td><br />
<td class="table-cell" >contact = tony@somehhere
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >mailhost = smtp.mailhost.abc
</td><br />
<td class="table-cell" >mailhost = smtp.somewhere
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >sendmail = /usr/lib/sendmail
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >imgcache = /home/oetiker/public_html/.simg
</td><br />
<td class="table-cell" >imgcache = /var/www/html/smokeping/img
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >imgurl = ../.simg
</td><br />
<td class="table-cell" >imgurl = http://mail.somewhere.net/smokeping/img
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >datadir = /home/oetiker/data/projects/AADJ-smokeping/dist/var
</td><br />
<td class="table-cell" >datadir = /usr/local/smokeping/var
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >piddir = /home/oetiker/data/projects/AADJ-smokeping/dist/var
</td><br />
<td class="table-cell" >piddir = /usr/local/smokeping/var
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >cgiurl = http://people.ee.ethz.ch/~oetiker/smokeping/smokeping.cgi
</td><br />
<td class="table-cell" >cgiurl = http://mail.somewhere.net/cgi-bin/smokeping.cgi
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >smokemail = /home/oetiker/data/projects/AADJ-smokeping/dist/etc/smokemail.dist
</td><br />
<td class="table-cell" >smokemail = /usr/local/smokeping/etc/smokemail
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >tmail = /home/oetiker/data/projects/AADJ-smokeping/dist/etc/tmail.dist
</td><br />
<td class="table-cell" >tmail = /usr/local/smokeping/etc/tmail
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td colspan="2" class="table-cell" >syslogfacility = local0
</td><br /></tr><br /></table><br />*** Alerts ***<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >to = 
</td><br />
<td class="table-cell" >to = someone@your.place
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >from = smokealert@ 
</td><br />
<td class="table-cell" >from = smokealert@your.smoke.server
</td><br /></tr><br /></table><br />*** Presentation ***<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >template = /home/oetiker/data/projects/AADJ-smokeping/dist/etc/basepage.html.dist
</td><br />
<td class="table-cell" >template = /usr/local/smokeping/etc/basepage.html
</td><br /></tr><br /></table><br />*** Probes ***<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >binary = /usr/sepp/bin/fping 
</td><br />
<td class="table-cell" >binary = /usr/sbin/fping
</td><br /></tr><br /></table><br />For some strange reason I had to make this change to /usr/sbin/fping<br />chown apache /usr/sbin/fping<br /><br />*** Targets ***<br /><table class="table" ><br /><tr ><br />
<td class="table-cell" >+ World
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >menu = World Connectivity
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >title= World Connectivity
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >++ New Zealand
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >menu = New Zealand Servers
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >title = New Zealand Server
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >_ _
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >+++ a Server
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >menu = My Server
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >title = My Server
</td><br /></tr><br /><tr ><br />
<td class="table-cell" >host = something.newskies.net
</td><br /></tr><br /></table><br />_ _<br />
```
`mkdir -p /var/www/html/smokeping/imgchown -R apache:apache /var/www/html/smokeping/img<br /><br />mkdir /usr/local/smokeping/var<br /><br />/usr/local/smokeping/bin/smokeping &<br /><br />#ps aux | grep smokeroot      8384  0.0  2.5  14976  3272 ?        Ss   May24   0:01 /usr/local/smokeping/bin/smokeping [FPing]apache    8435  0.0  1.7  11100  2168 ?        Ss   May24   0:02 /usr/bin/speedy_backend -w /var/www/cgi-bin/smokeping.cgiapache    8436  0.3  3.9  12648  5036 ?        S    May24   2:04 /usr/bin/speedy_backend -w /var/www/cgi-bin/smokeping.cgi
```

```
<br />
```
`vi /etc/rc.d/rc.local/usr/local/smokeping/bin/smokeping &
```

```
<br />

* * *
