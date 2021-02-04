---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-05-13T11:40:00Z
slug: install-opennms-132-on-opensuse-102-system-the-simplest-version
tags:
- OpenNMS
- opensuse
title: Install OpenNMS 1.3.2 on OpenSuse 10.2 system (The simplest version  )
url: /2007/05/13/install-opennms-132-on-opensuse-102-system-the-simplest-version/
wordpress_id: 49154
---

1>Install dependence packages<br />zliu3:~yast -i rrdtool<br />zliu3:~yast -i postgresql<br />zliu3:~ # rpm -qa |grep rrdtool<br />rrdtool-1.2.15-25<br />zliu3:~ # rpm -qa |grep postgresql<br />postgresql-8.1.5-13<br />postgresql-libs-8.1.5-13<br />postgresql-contrib-8.1.5-13<br />postgresql-pl-8.1.5-15<br />postgresql-server-8.1.5-13<br />rcpostgresql start<br />copy jdk/tomcat 5.5 package files to /opt<br />cd /opt<br />tar xzvf jdk1.5.tar.gz<br />tar xzvf tomcat5.5.tar.gz<br />export  JAVA_HOME=/opt/jdk1.5.0_09<br />export OPENNMS_HOME=/opt/opennms<br />export  CATALINA_HOME=/opt/apache-tomcat-5.5.20<br />export PATH=$PATH:$JAVA_HOME/bin<br />java -version<br />$CATALINA_HOME/bin/startup.sh<br />Test Tomcat 5.5 http://Ip_address:8080/<br />vi /var/lib/pgsql/data/postgresql.conf<br /># - Connection Settings - <br />max_connections = 256<br /><br />vi /var/lib/pgsql/data/pg_hba.conf<br />[refer to install guide] <br />#local  all    all             ident   sameuser<br />local all all trust<br />host all all 127.0.0.1 255.255.255.255 trust<br />host all all ::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff trust<br /><br />rcpostgresql restart<br /><br />2>Install and configure OpenNMS<br />Copy OpenNMS rpm packages to /root<br />rpm -ivh opennms*<br />$OPENNMS_HOME/bin/runjava -s<br />$OPENNMS_HOME/bin/install -dis<br />$OPENNMS_HOME/bin/install -y -w $CATALINA_HOME/conf/Catalina/localhost<br />$CATALINA_HOME/bin/shutdown.sh<br />$CATALINA_HOME/bin/startup.sh<br />/etc/init.d/opennms start<br />/etc/init.d/opennms -v status<br />OpenNMS.Eventd         : running<br />OpenNMS.Trapd          : running<br />OpenNMS.Dhcpd          : running<br />OpenNMS.Actiond        : running<br />OpenNMS.Capsd          : running<br />OpenNMS.Notifd         : running<br />OpenNMS.Scriptd        : running<br />OpenNMS.Rtcd           : running<br />OpenNMS.Pollerd        : running<br />OpenNMS.PollerBackEnd  : running<br />OpenNMS.Collectd       : running<br />OpenNMS.Threshd        : running<br />OpenNMS.Discovery      : running<br />OpenNMS.Vacuumd        : running<br />OpenNMS.EventTranslator: running<br />OpenNMS.PassiveStatusd : running<br /><br />Test OpenNMS login page http://ip_address:8080/opennms
