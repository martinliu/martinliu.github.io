---
author: liuadmin
categories:
- NSM
comments: true
date: 2008-05-16T07:30:04Z
slug: iso-open-source-software
tags:
- cacti
- cactiez
- iso
- Nagios
- nessus
- ntop
- ossim
- snort
title: ISO open source software
url: /2008/05/16/iso-open-source-software/
wordpress_id: 49206
---

![](http://thelegendarywolf.googlepages.com/dvd.jpg)<br /><br />There are some projects do have ISO file for downloading. That means you could run this solution with in 20 minutes on a physics machine or a vmware session. You can just download this ISO image file and burn it on a blank cd; then you will insert it into DVD/CD driver of your target machine, after press few enter keys; You finally  got all software on this box. Reboot this machine, you get everything up an running on it; including a Linux OS and everything which the solution depends on.<br /><br />I had tested out only few of ISO open source software.<br />

<br />	
  * [CactiEZ](http://cactiusers.org/index.php)
<br />	
  * [OSSIM](http://www.ossim.net/)
<br /><br />It looks like actually two open source software collections. Let's look inside those ISO files, it is a bootable Linux install disk with all necessary software.<br /><br />CactiEZ has following parts:<br /><br />	
  1. Cacti and plugins (Discovery, flowviewer, mac Track, nTop, syslog, Thold, etc..)
<br />	
  2. Nagios
<br /><br />CactiEZ is focusing on Cacti. Now it does not provide free download. You will pay few $$$; it's  a great ISO open source software and worthy to pay for [Jimmy's](http://cactiusers.org/forums/profile.php?mode=viewprofile&u=2) effort. I have a old version for you to download. [click here.](http://demo.wholog.net/CactiEZ.iso) [下载 cactiez](http://demo.wholog.net/CactiEZ.iso)<br /><br />There is [architecture picture of OSSIM](http://www.ossim.net/dokuwiki/doku.php?id=documentation:architecture). OAAIM use sensor for collecting data over network. A typical OSSIM Sensor configuration would do the following functions:<br />

<br />	
  1. IDS (Snort)
<br />	
  2. Vulnerability Scanner (Nessus)
<br />	
  3. Anomaly Detection (Spade, p0f, pads, arpwatch, RRD ab behaviour)
<br />	
  4. Network Monitoring and Profiling (Ntop)
<br />	
  5. Collecting from local routers, firewalls, IDS’s, etc
<br />	
  6. It could even act as a Firewall
<br /><br />I love ISO open source software, for the following reasons:<br /><br />	
  * Easy to install on a physic machine.
<br />	
  * Time Saving. You just use it right away after you load everything and reboot that machine.
<br /><br />Linux is basically  a ISO based open source software. If you know more others, not Linux; please let me know.
