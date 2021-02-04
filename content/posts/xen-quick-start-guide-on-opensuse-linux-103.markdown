---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-08-27T14:43:05Z
slug: xen-quick-start-guide-on-opensuse-linux-103
tags:
- opensuse
- Virtualization
- xen
title: Xen quick start guide on openSuSE Linux 10.3
url: /2008/08/27/xen-quick-start-guide-on-opensuse-linux-103/
wordpress_id: 49225
---

If you had installed VMWare workstation on any Linux, you may have kernel source problem. Because a default Linux installation do not include kernel source package. I'm just saying that you should always play with open source Virtualization, Xen or Virtial Box are all good stuff to run ;)  . I got some screen-shots for you if you don't have idea how do install Xen. The true is Xen is faster then VMWare on my laptop. I would not work with VMWare anymore.<br /><br />My laptop is a DELL D630 with openSuSE Linux 10.3 and XP (just for work).<br /><br />**1) Install Xen packages via yast from DVD.**<br />[![](http://lh4.ggpht.com/liuzh66/SLJtOGpR9lI/AAAAAAAAAos/rLsgH5aLcDk/s400/xen-packages.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238369405654660690)<br /><br /><!--more-->I just installed all of six Xen packages. openSuSE Linux 10.3 installation DVD has Xen version 3.18<br />Then Yast control center have one new group 'Virtualization'<br />[![](http://lh5.ggpht.com/liuzh66/SLJtYcWxSrI/AAAAAAAAAo0/285FBxGvv9w/s400/Yast-Control%20Center.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238369583281294002)<br /><br />You should reboot machine, a new Xen section will be already in GRUB menu, after boot in Xen. Xen server will be started.<br /><br />**2)Create a new Virtual machine by clicking 'create virtual machines' icon**<br /><br />[![](http://lh3.ggpht.com/liuzh66/SLJv51ZlCdI/AAAAAAAAAqQ/Xh89uajyLB0/s400/co1.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238372355962898898)<br />I select opensuse because I have only install DVD in my hand.<br />[![](http://lh4.ggpht.com/liuzh66/SLJwKIIF7SI/AAAAAAAAAqY/m7-V80GunBA/s400/co2.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238372635867737378)<br />The new virtual machine has only one 4GB virtual HD as default, it is actually a file, for sure your physical HD have enough free space. You must add at least one CD-Rom, it map to a physical CD/DVD-ROM.<br />[![](http://lh4.ggpht.com/liuzh66/SLJwbPYRr-I/AAAAAAAAAqg/3qpmrTjPhYE/s400/co3.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238372929872441314)<br />For configure network, you might read Xen use guide. I use bridge for this virtual machine.<br />[![](http://lh5.ggpht.com/liuzh66/SLJwt5BT07I/AAAAAAAAAqo/u58PHzmvOG0/s400/co4.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238373250288047026)<br />Review all of settings, you can change anywhere at this window. Insert install DVD in DVD-ROM, and clicking Ok.<br />[![](http://lh6.ggpht.com/liuzh66/SLJw36WAYmI/AAAAAAAAAqw/7Pj7drfcekM/s400/co5.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238373422441980514)<br /><br />**3)Inside a pop-up TightVNC window, Install Linux as normal **<br />[![](http://lh5.ggpht.com/liuzh66/SLJxKpOIS_I/AAAAAAAAAq4/uYY_Yow8N3g/s400/co6.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238373744263056370)<br />[![](http://lh4.ggpht.com/liuzh66/SLJxcZY4KfI/AAAAAAAAArA/8voGa3L5HCM/s400/co7.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238374049250814450)<br />[![](http://lh6.ggpht.com/liuzh66/SLJxpPb_SuI/AAAAAAAAArI/JEtDfU6US-0/s400/co8.jpg)](http://picasaweb.google.com/liuzh66/Xen/photo#5238374269917809378)<br /><br />Notes:<br />

<br />	
  * You'd better have your host machine on the network, if eth0 is not up; the virtual machine can not connect with the host machine.
<br />	
  * You may turn on the full Virtualization support in BIOS, in order to create a Windows virtual machine. It depends on CPU.
<br />
