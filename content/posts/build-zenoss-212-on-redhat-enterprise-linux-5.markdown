---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-01-30T13:22:00Z
slug: build-zenoss-212-on-redhat-enterprise-linux-5
tags:
- NSM
- RHEL 5
- Zenoss
title: Build Zenoss 2.1.2 on Redhat Enterprise Linux 5
url: /2008/01/30/build-zenoss-212-on-redhat-enterprise-linux-5/
wordpress_id: 49182
---

![](http://www.zenoss.com/images/logo.gif) Well, it is the first time to running a RHEL 5 for me, at same time got zenoss built successfully on it. zenoss-2.1.2 was build from source, the whole process went a while since RHEL is in one of my VMware session; CPU %sy was pretty high during building source code.<br />

# Build zenoss-2.1.2

<br />The INSTALL.txt file is good enough, my installation how-to can be really sample:<br />

<br />	
  * Read INSTALL.txt
<br />	
  * add zenoss user
<br />	
  * start mysql
<br />	
  * upload zenoss tarball to zenoss home directory
<br />	
  * login as zenoss
<br />	
  * untar zenoss tarball then run the following, good luck!
<br /><br />

<blockquote>-bash-3.1$ ls<br />appliance_update.sh  conf             install-functions.sh  shared-functions.sh<br />autoinstall          COPYRIGHT.txt    install.sh            zen2dump.py<br />build-functions.sh   docs             INSTALL.txt           ZEN2UPGRADE.txt<br />build-noprompt.sh    externallibs     libzenoss             zensocket<br />build.sh             fs               LICENSE.txt           zenwipe.sh<br />CHANGES.txt          genpatchdeps.py  MacOS<br />checkall.sh          GNUmakefile      rpm<br />-bash-3.1$ ./install.sh <br /><br />This installer actually builds Zenoss.<br />For a simpler installation try the VMPlayer Appliance image,<br />or use RPMs for Redhat based systems. <br /><br />Building... <br /><br />Password for the Zenoss "admin" user [zenoss]:<br />Enter the password again:<br />MySQL server hostname [localhost]:<br />MySQL server root username [root]:<br />MySQL server root password []:<br />MySQL event database name [events]:<br />MySQL username for Zenoss events database [zenoss]:<br />MySQL password for zenoss [zenoss]:<br />/usr/bin/python2.4 genpatchdeps.py >.patchdeps<br />installing into //usr/local/zenoss<br />build log is in zenbuild.log<br />unpacking Zope-2.8.8-final in build/<br />configuring build/Zope-2.8.8-final/makefile<br />installing libzenos/Products.tar.gz<br />installing libzenos/bin.tar.gz<br />installing libzenos/extras.tar.gz<br />mkdir -p //usr/local/zenoss/skel/etc<br />cp conf/zope.conf.in //usr/local/zenoss/skel/etc/zenoss.conf.in<br />installing zope<br />unpacking TwistedSNMP-0.3.13 in build/<br />patching file snmpprotocol.py<br />patching file v3/agentproxy.py<br />patching file v3/agentproxy.py<br />patching file tableretriever.py<br />patching file snmpprotocol.py<br />unpacking pysnmp-3.4.3 in build/<br />patching file pysnmp/proto/rfc1155.py<br />patching file pysnmp/proto/rfc1155.py<br />patching file pysnmp/proto/rfc1155.py<br />patching file pysnmp/proto/rfc1155.py<br />installing pysnmp<br />unpacking Twisted-2.5.0 in build/<br />patching file TwistedCore-2.5.0/twisted/internet/process.py<br />Hunk #1 succeeded at 315 (offset -20 lines).<br />unpacking pycrypto-1.9a6 in build/<br />installing pycrypto<br />installing twisted<br />installing twistedsnmp<br />making zensocket<br />gmake[1]: Entering directory `/usr/local/zenoss/zenoss-2.1.2/zensocket'<br />gcc -o zensocket -Wall -pedantic -D__GNU_LIBRARY__ -g  zensocket.c<br />rm -f //usr/local/zenoss/bin/zensocket<br />cp zensocket //usr/local/zenoss/bin/zensocket<br />gmake[1]: Leaving directory `/usr/local/zenoss/zenoss-2.1.2/zensocket'<br />unpacking pynetsnmp-0.27.0 in build/<br />unpacking ctypes-1.0.1 in build/<br />installing ctypes<br />installing pynetsnmp<br />unpacking MySQL-python-1.2.0 in build/<br />patching file setup.py<br />patching file _mysql.c<br />Hunk #1 succeeded at 440 (offset -37 lines).<br />Hunk #3 succeeded at 460 (offset -37 lines).<br />Hunk #5 succeeded at 526 (offset -37 lines).<br />installing mysql-python<br />unpacking rrdtool-1.2.23 in build/<br />unpacking libart_lgpl-2.3.17 in build/<br />configuring build/libart_lgpl-2.3.17/Makefile<br />installing libart<br />unpacking freetype-2.1.9 in build/<br />configuring build/freetype-2.1.9/Makefile<br />installing freetype<br />unpacking libpng-1.2.8-config in build/<br />configuring build/libpng-1.2.8-config/Makefile<br />installing libpng<br />configuring build/rrdtool-1.2.23/Makefile<br />installing rrdtool<br />rm -rf //usr/local/zenoss/share/rrdtool/examples<br />rm -rf //usr/local/zenoss/lib/perl<br />unpacking epydoc-3.0beta1 in build/<br />patching file epydoc/apidoc.py<br />patching file epydoc/docbuilder.py<br />patching file epydoc/docintrospecter.py<br />installing epydoc<br />unpacking python-snpp-1.1.1 in build/<br />installing snpp<br />unpacking Yapps-2.1.1 in build/<br />installing yapps<br />unpacking nagios-plugins-1.4.5 in build/<br />configuring build/nagios-plugins-1.4.5/Makefile<br />installing nagios<br />unpacking libsmi-0.4.5 in build/<br />configuring build/libsmi-0.4.5/Makefile<br />installing libsmi<br />unpacking wmi-0.1.5 in build/<br />unpacking pyip-0.7 in build/<br />patching file icmp.py<br />installing pyip<br />unpacking simplejson-1.4 in build/<br />cp externallibs/setuptools*.egg build/simplejson-1.4<br />installing simplejson<br />installing conf/snmpd.conf<br />installing conf/zenactions.conf<br />installing conf/zenbackup.conf<br />installing conf/zencommand.conf<br />installing conf/zendisc.conf<br />installing conf/zeneventlog.conf<br />installing conf/zenhub.conf<br />installing conf/zenmib.conf<br />installing conf/zenmigrate.conf<br />installing conf/zenmodeler.conf<br />installing conf/zenpack.conf<br />installing conf/zenperfsnmp.conf<br />installing conf/zenping.conf<br />installing conf/zenprocess.conf<br />installing conf/zenrender.conf<br />installing conf/zenstatus.conf<br />installing conf/zensyslog.conf<br />installing conf/zentrap.conf<br />installing conf/zenwin.conf<br />installing conf/zenwinmodeler.conf<br />installing conf/zenxevent.conf<br />installing conf/zope.conf.in<br />installing conf/hubpasswd<br />Wrote file /usr/local/zenoss/etc/zeo.conf<br />Wrote file /usr/local/zenoss/bin/zeoctl<br />Changed mode for /usr/local/zenoss/bin/zeoctl to 755<br />Wrote file /usr/local/zenoss/bin/runzeo<br />Changed mode for /usr/local/zenoss/bin/runzeo to 755<br />Starting Zope Object Database<br />. daemon process started, pid=15476<br />Loading initial Zenoss objects into the Zeo database<br />(this can take a few minutes)<br />ZentinelPortal loaded at zport<br />Starting Zope Server<br />. daemon process started, pid=15499 <br /><br />=========================================================<br />zensocket must be setuid. As root, execute the following:<br />chown root:zenoss /usr/local/zenoss/bin/zensocket<br />chmod 04750 /usr/local/zenoss/bin/zensocket<br />========================================================= <br /><br />Successfully installed Zenoss</blockquote>

<br />

### Start Daemons:

<br />bash$ $ZENHOME/bin/zenoss start<br /><br />bash$ $ZENHOME/bin/zenoss status<br />

<br />	
  * Then I access to Zenoss portal, got this error.
<br /><br />

###  HTTP Status 404 - /zport/dmd

<br />

<blockquote>* * *
> 
> **type** Status report**message** _/zport/dmd_**description** _The requested resource (/zport/dmd) is not available._<br /><br />
> 
> * * *
> 
> <br />
> 
> ##### Apache Tomcat/5.5.20
> 
> <br /></blockquote>

<br />I reboot the RHEL server, then start mysql and zenoss. Finally, everything goes smoothly. Let's take this nice zenoss portal.<br /><br />[![image](http://lh4.google.com/liuzh66/R6B8iX2WoeI/AAAAAAAAAdY/HOxPPiOhDZ0/image5.png)](http://lh4.google.com/liuzh66/R6B8iX2WoeI/AAAAAAAAAdY/HOxPPiOhDZ0/image5.png)<br /><br />On my RHEL, mysql, snmp and python were installed with OS; other packages might installed from zenoss source tarball. I am not sure about this, you could check above to see my install log.<br /><br />**Install tips:**<br />

<br />	
  * Package dependence should be consider before you build Zenoss source code. A full RHEL install is a lazy idea to solve this problem; but it is still the best practice if you are new to both Linux and Zenoss.
<br />	
  * Start zenoss daemons might take one minute or more. If you access to zenoss portal immediately, you could get a HTTP Status 404 error. Before you see balance stone, please be patience.
<br /><br />

# Auto-Discovery of Devices

<br />It's time to read ZenossAdminGuide211.pdf; BTW that's a good document. I will go ahead to note down what I did in my testing evn.  Please turn to P47, I will go from there. For sure you have something discovered, please read the following tips:<br />

<br />	
  * **The Zenoss machine should have snmp installed**, including the following packages:
<br /><br />

<blockquote>[root@localhost ~]# rpm -qa|grep snmp<br />net-snmp-libs-5.3.1-19.el5<br />net-snmp-5.3.1-19.el5<br />net-snmp-utils-5.3.1-19.el5<br />net-snmp-perl-5.3.1-19.el5</blockquote>

<br />As far as I know net-snmp-utils-5.3.1-19.el5 is a necessary. Without this package, you do not have ability to snmpwalk any device via SNMP protocol; in other word you can not get enough information about that remote device.<br />

<br />	
  * **Add a right network ID**, here is a example:
<br /><br />

<blockquote>ID: 192.168.6.0 -->  for 192.168.6.0/24 subnet</blockquote>

<br />

<br />	
  * **snmpwalk at least one snmp-enable device**, here is a example:
<br /><br />

<blockquote>[root@localhost snmp]# snmpwalk -v 1 -c public  192.168.6.131 system<br />SNMPv2-MIB::sysDescr.0 = STRING: SunOS unknown 5.10 Generic_120012-14 i86pc<br />SNMPv2-MIB::sysObjectID.0 = OID: NET-SNMP-MIB::netSnmpAgentOIDs.3<br />DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (146417) 0:24:24.17<br />SNMPv2-MIB::sysContact.0 = STRING: "System administrator"<br />SNMPv2-MIB::sysName.0 = STRING: unknown<br />SNMPv2-MIB::sysLocation.0 = STRING: "System administrators office"<br />SNMPv2-MIB::sysServices.0 = INTEGER: 72<br />SNMPv2-MIB::sysORLastChange.0 = Timeticks: (96) 0:00:00.96<br />SNMPv2-MIB::sysORID.1 = OID: IF-MIB::ifMIB<br />SNMPv2-MIB::sysORID.2 = OID: SNMPv2-MIB::snmpMIB<br />SNMPv2-MIB::sysORID.3 = OID: TCP-MIB::tcpMIB<br />SNMPv2-MIB::sysORID.4 = OID: IP-MIB::ip<br />SNMPv2-MIB::sysORID.5 = OID: UDP-MIB::udpMIB<br />SNMPv2-MIB::sysORID.6 = OID: SNMP-VIEW-BASED-ACM-MIB::vacmBasicGroup<br />SNMPv2-MIB::sysORID.7 = OID: SNMP-FRAMEWORK-MIB::snmpFrameworkMIBCompliance<br />SNMPv2-MIB::sysORID.8 = OID: SNMP-MPD-MIB::snmpMPDCompliance<br />SNMPv2-MIB::sysORID.9 = OID: SNMP-USER-BASED-SM-MIB::usmMIBCompliance<br />SNMPv2-MIB::sysORDescr.1 = STRING: The MIB module to describe generic objects for network interface sub-layers<br />SNMPv2-MIB::sysORDescr.2 = STRING: The MIB module for SNMPv2 entities<br />SNMPv2-MIB::sysORDescr.3 = STRING: The MIB module for managing TCP implementations<br />SNMPv2-MIB::sysORDescr.4 = STRING: The MIB module for managing IP and ICMP implementations<br />SNMPv2-MIB::sysORDescr.5 = STRING: The MIB module for managing UDP implementations<br />SNMPv2-MIB::sysORDescr.6 = STRING: View-based Access Control Model for SNMP.<br />SNMPv2-MIB::sysORDescr.7 = STRING: The SNMP Management Architecture MIB.<br />SNMPv2-MIB::sysORDescr.8 = STRING: The MIB for Message Processing and Dispatching.<br />SNMPv2-MIB::sysORDescr.9 = STRING: The management information definitions for the SNMP User-based Security Model.<br />SNMPv2-MIB::sysORUpTime.1 = Timeticks: (88) 0:00:00.88<br />SNMPv2-MIB::sysORUpTime.2 = Timeticks: (88) 0:00:00.88<br />SNMPv2-MIB::sysORUpTime.3 = Timeticks: (88) 0:00:00.88<br />SNMPv2-MIB::sysORUpTime.4 = Timeticks: (88) 0:00:00.88<br />SNMPv2-MIB::sysORUpTime.5 = Timeticks: (88) 0:00:00.88<br />SNMPv2-MIB::sysORUpTime.6 = Timeticks: (90) 0:00:00.90<br />SNMPv2-MIB::sysORUpTime.7 = Timeticks: (96) 0:00:00.96<br />SNMPv2-MIB::sysORUpTime.8 = Timeticks: (96) 0:00:00.96<br />SNMPv2-MIB::sysORUpTime.9 = Timeticks: (96) 0:00:00.96<br /><br />As you can see here: it is a Solaris 10 system. I just downloaded it last night, get it up and running in another VMWare session on my laptop. You should configure snmp service for Solaris in order to monitoring it via snmp protocol. I will past my /etc/snmp/conf/snmpd.conf below:<br /><br /># cat snmpd.conf<br /># Copyright 1988 - 07/17/00 un Microsystems, Inc. All Rights Reserved.<br />#ident  "@(#)snmpd.conf 2.24    00/07/17 SMI" <br /><br /># See below for file format and supported keywords <br /><br />sysdescr        Sun SNMP Agent,<br />syscontact      System administrator<br />sysLocation     System administrators office<br />#<br />system-group-read-community     public<br />#system-group-write-community    private<br />#<br />read-community  public<br />#write-community private<br />#<br />trap            192.168.6.130<br />trap-community  SNMP-trap<br />#<br />#kernel-file     /vmunix<br />#<br />#managers        lvs golden<br />managers        192.168.6.130<br /><br />192.168.6.130 is Zenoss ip address; you have to restart snmpd daemon after you change something in this file. Here is another tips for Solaris OS. Be default root can not login via ssh or telnet; you have to add another user. You will login as this new user, then su to root.</blockquote>

<br />Let's see what I got after done all of above.<br /><br />[![image](http://lh6.google.com/liuzh66/R6B8p32WogI/AAAAAAAAAds/L_RLc73gmeQ/image8.png)](http://lh6.google.com/liuzh66/R6B8p32WogI/AAAAAAAAAds/L_RLc73gmeQ/image8.png)<br /><br />[![image](http://lh3.google.com/liuzh66/R6B8wH2WoiI/AAAAAAAAAd8/lzmTaSebDdw/image4.png)](http://lh3.google.com/liuzh66/R6B8wH2WoiI/AAAAAAAAAd8/lzmTaSebDdw/image4.png)<br /><br />Zenoss has a pretty good network map, it is a flash map; you can drag things on this map. Before I end this blog, I'd like to summary my questions blow:<br />

<br />	
  1. Because my RHEL installation is big enough, I don't know what are dependence packages for Zenoss; no time to list all of them. Does have this list?
<br />	
  2. I've no idea how to configure snmpd on Solaris. What I did was just modified /etc/snmp/conf/snmpd.conf
<br />	
  3. How to restart snmp daemon for Solaris?
<br />	
  4. Do you have any good blog about zenoss?
<br /><br />I will write a Chinese blog after this one to conclusion zenoss installation. Please give a hint if you have any comment.
