---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2008-04-05T14:19:20Z
slug: get-right-size-of-oss
tags:
- oss
title: Get right-size of OSS
url: /2008/04/05/get-right-size-of-oss/
wordpress_id: 49196
---

6yeas ago, I had a open source talk with my friend Tom Chen. The topic was " does oss suppose to work for large enterprise for mission critical business?" Until last week, I thought I found answer by myself; the OSS does works for bank business in China. During last week, I deployed my company's product on CCB's machines. Those machines are part of e-banking system, 1/4th of them are on Redhat Enterprise Linux 4 update6. As we all know CCB is one of big four bank in China, those Linux machines are running Apache for web-tier of e-banking system. A 160MB installation image was ftp to every managed nodes, untar it then ran a same install script. I felt Linux boxes took less time then other HP-UX boxes, they are similar servers I mean similar hardware. Actually CCB have many Linux servers all over the country then I touched at this time.<br /><br />I had a business travel in Urumchi lat year. I met another bank customer there. When we were talking about what kind of OS they have. They impressed me very much. They said part of servers are on SuSE Enterprise Linux, they are just virus-free and lower maintenance cost then M$ Windows. They are just use those SuSE Linux to running IBM DB2 database for some bank business. They like Linux, but not use it everywhere. I didn't tell them that is my favorite Linux distribution. Just look back 5 years, I would say more and more companies are using OSS or they are considering have more OSS for  their business.<br /><br />Let's get back to my topic: what OSS could be good for you? Do you have confidence for have more OSS for your business system? I think you need to just have the right-size of OSS. You have to figure by yourself. The following are my suggestions:<br />

<br />	
  * OSS adoption might take years, you should have a plan.
<br />	
  * Starting from one single on-going project, you could migrate all or part of a business system to OSS(Linux for OS, Tomcat for mid-tier, or what every you'd like to use)
<br />	
  * Monitoring the entire IT by same way by 24 hours. You must have availability and performance report for every node. Then you could analyses those history report to figure out if OSS does a good job or not. A incident report of whole IT support org is highly recommended.
<br />	
  * Having more OSS engineers might speed up the process you move forward to OSS.
<br /><br />If you like my thought in this post, you would like to see this [old one](http://www.martinliu.cn/2007/06/12/%e5%bb%ba%e7%ab%8b%e4%b8%80%e4%b8%aa%e5%bc%80%e6%ba%90%e4%bc%81%e4%b8%9a/).
