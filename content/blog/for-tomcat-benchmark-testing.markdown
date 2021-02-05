---
author: liuadmin
categories:
- Infrastructure
comments: true
date: 2009-07-04T05:36:03Z
slug: for-tomcat-benchmark-testing
tags:
- benchmark
- opensource
- Tomcat
title: For tomcat benchmark testing
url: /2009/07/04/for-tomcat-benchmark-testing/
wordpress_id: 49258
---

Tomcat Configuration  查看一下可以配置的参数![TomCat](http://tech.tomarea.com/wp-content/uploads/2009/02/tomcat-300x261.jpg)<br /><br />**设置JVM的参数Setting JVM Options for Tomcat**<br /><br />Edit the /usr/locat/apache-tomcat/bin/catalina.sh file and add the JVM options to the JAVA_OPTS environment variable.JVM Option Value Description<br />-Xmx 4g The maximum Java heap size.<br />-Xms 4g The initial Java heap size.<br />-Xmn 1g The size of young generation.<br />-XX:+UseParallelGC – To use parallel garbage collection for scavenges.<br />-XX:PermSize 50m The initial size of permanent generation.<br />注释：上面两个4g的值，我没试过，我用8GB内存windows的机器1.5GB能启动，超过了Tomcat服务就启动不了了。<br /><br />**配置Tomcat Connector Attributes**<br />Edit the /usr/locat/apache-tomcat/conf/server.xml file and add the attributes listed in Table 3 to the Connector element.<br /><br />下面是个例子供参考<br /><Connector port="8080" protocol="HTTP/1.1" maxThreads="3000" acceptCount="200" /><br />Tomcat Configuration Attribute Value Description<br />The maximum number of request processing threads to be created by this connector, which therefore determines the maximum number of simultaneous requests that can be handled. If not specified, the default value for this attribute is 40. If an executor is associated with this connector, this attribute is ignored and the connector executes tasks using the executor rather than an internal thread pool.<br />maxThreads 3000<br />The maximum queue length for incoming connection requests when all<br />possible request processing threads are in use. Any requests received when<br />the queue is full are refused. The default value is 10.<br />acceptCount 2000<br />The number of request processing threads that are created when this connector<br />is first started. The connector also verifies that it has the specified number of<br />idle processing threads available. This attribute should be set to a value smaller<br />than that set for maxThreads. The default value is 4.<br />minSpareThreads 500<br />The maximum number of unused request processing threads that are allowed<br />to exist until the thread pool starts stopping the unnecessary threads. The<br />default value is 50.<br />maxSpareThreads 2000<br />Set to “true” if you want calls to request.getRemoteHost() to perform DNS<br />lookups in order to return the actual host name of the remote client. Set to<br />enableLookups false “false” to skip the DNS lookup and return the IP address in String form instead<br />(thereby improving performance). By default, DNS lookups are enabled.<br /><br />上面的值比我实际使用的大，我的200并发测试通过了，硬件配置见前一帖。
