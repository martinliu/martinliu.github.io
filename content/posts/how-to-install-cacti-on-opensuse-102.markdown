---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-06-14T10:02:00Z
slug: how-to-install-cacti-on-opensuse-102
tags:
- cacti
- opensuse
title: How to install Cacti on OpenSuse 10.2
url: /2007/06/14/how-to-install-cacti-on-opensuse-102/
wordpress_id: 49163
---

1.<br />Download Extract the distribution tarball<br />Suse:/opt # wget http://www.cacti.net/downloads/cacti-0.8.6j.tar.gz<br />Suse:/opt # tar zxvf cacti-0.8.6j.tar.gz<br /><br />2.<br />Create the MySQL database:<br />Suse:/opt # mysqladmin --user=root create cacti<br /><br />3.<br />Import the default cacti database:<br />Suse:/opt/cacti-0.8.6j # mysql cacti < user="root"> GRANT ALL ON cacti.* TO cactiuser@localhost IDENTIFIED BY 'cacti';<br />Query OK, 0 rows affected (0.03 sec)<br /><br />mysql> flush privileges;<br />Query OK, 0 rows affected (0.00 sec)<br /><br />mysql> quite<br /><br />5.<br />Edit include/config.php and specify the MySQL user, password and database for your Cacti configuration.<br /><br />Suse:/opt/cacti-0.8.6j # vi include/config.php<br />/* make sure these values refect your actual database/host/user/password */<br />$database_type = "mysql";<br />$database_default = "cacti";<br />$database_hostname = "localhost";<br />$database_username = "cactiuser";<br />$database_password = "cacti";<br />$database_port = "3306";<br /><br />6.<br />Set the appropriate permissions on cacti's directories for graph/log generation. You should execute these commands from inside cacti's directory to change the permissions.<br /><br />Suse:/opt # mv cacti-0.8.6j /srv/www/htdocs/cacti<br />Suse:/opt # useradd cactiuser -d /srv/www/htdocs/cacti<br /><br />7.<br />Add a line to your /etc/crontab file similar to:<br />Suse:/srv/www/htdocs/cacti # vi /etc/crontab<br />*/5 * * * * cactiuser php /srv/www/htdocs/cacti/poller.php > /dev/null 2>&1<br /><br />8.<br />Point your web browser to:<br />http://10.100.113.138/cacti/index.php<br /><br />9.<br />Install cacti patches<br />Access to http://www.cacti.net/download_patches.php<br />Be sure that you are in your Cacti directory when you execute these commands.<br /><br />

wget http://www.cacti.net/downloads/patches/0.8.6j/ping_php_version4_snmpgetnext.patch<br />wget http://www.cacti.net/downloads/patches/0.8.6j/tree_console_missing_hosts.patch<br />wget http://www.cacti.net/downloads/patches/0.8.6j/thumbnail_graphs_not_working.patch<br />wget http://www.cacti.net/downloads/patches/0.8.6j/graph_debug_lockup_fix.patch<br />wget http://www.cacti.net/downloads/patches/0.8.6j/snmpwalk_fix.patch<br />patch -p1 -N < ping_php_version4_snmpgetnext.patch<br />patch -p1 -N < tree_console_missing_hosts.patch<br />patch -p1 -N < thumbnail_graphs_not_working.patch<br />patch -p1 -N < graph_debug_lockup_fix.patch<br />patch -p1 -N < snmpwalk_fix.patch<br /><br />10.<br />Install cactid<br />Download Cacti.tar.gz<br />Suse:/srv/www/htdocs/cacti # wget http://www.cacti.net/downloads/cactid/cacti-cactid-0.8.6i.tar.gz<br />Suse:/srv/www/htdocs/cacti # tar zxvf cacti-cactid-0.8.6i.tar.gz<br />Suse:/srv/www/htdocs/cacti # cd cacti-cactid-0.8.6i/<br />Suse:/srv/www/htdocs/cacti/cacti-cactid-0.8.6i # ./configure<br />encounter a error:<br />configure: error: cannot find SNMP headers. Use --with-snmp to specify non-default path.<br />It seems OpenSuse does not have SNMP headers within installtation DVD. Install cactid latter.<br /><br />This article is referring **[Installation Guide for Unix/Linux](http://www.cacti.net/downloads/docs/html/install_unix.html)**       from cacti.net<br />
