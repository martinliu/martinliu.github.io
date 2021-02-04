---
author: liuadmin
categories:
- NSM
- Tools
comments: true
date: 2010-12-22T07:28:45Z
slug: fiddler-timers
tags:
- fiddler
title: 'Fiddler Timers '
url: /2010/12/22/fiddler-timers/
wordpress_id: 50848
---

![Fiddler](http://www.fiddler2.com/Fiddler/images/FiddlerLogo.png)Fiddler is a Web Debugging Proxy which logs all HTTP(S) traffic between your computer and the Internet. Fiddler allows you to inspect all HTTP(S) traffic, set breakpoints, and "fiddle" with incoming or outgoing data. Fiddler includes a powerful event-based scripting subsystem, and can be extended using any .NET language.Fiddler is freeware and can debug traffic from virtually any application, including Internet Explorer, Mozilla Firefox, Opera, and thousands more. 







	
  * **ClientConnected**- Exact time that the client browser made a TCP/IP connection to Fiddler.

	
  * **ClientBeginRequest**– Time at which this HTTP request began. May be much later than ClientConnected due to client connection reuse.

	
  * **ClientDoneRequest** - Exact time that the client browser finished sending the HTTP request to Fiddler.

	
  * **DNSTime** - # milliseconds Fiddler spent in DNS looking up the server's IP address.

	
  * **GatewayDeterminationTime** - # milliseconds Fiddler  spent determining the upstream gateway proxy to use (e.g. processing  autoproxy script). Mutually exclusive to DNSTime.

	
  * **TCPConnectTime** - # milliseconds Fiddler spent TCP/IP connecting to that server's IP address.

	
  * **HTTPSHandshakeTime** – Amount of time spent in HTTPS handshake

	
  * **ServerConnected** – Time at which this connection to  the server was made. May be much earlier than ClientConnected due to  server connection reuse.

	
  * **FiddlerBeginRequest** – The time at which Fiddler began sending the HTTP request to the server.

	
  * **ServerGotRequest** - Exact time that Fiddler finished (re)sending the HTTP request to the server.

	
  * **ServerBeginResponse** - Exact time that Fiddler got the first bytes of the server's HTTP response.

	
  * **ServerDoneResponse** - Exact time that Fiddler got the last bytes of the server's HTTP response.

	
  * **ClientBeginResponse** - Exact time that Fiddler began transmitting the HTTP response to the client browser.

	
  * **ClientDoneResponse**- Exact time that Fiddler finished transmitting the HTTP response to the client browser.


**Can i find out how long the server needs to process my request ?**
(ServerBeginResponse - ServerGotRequest) is probably what you want.

**Can i find out how long the request needs to pass through the network?**
I'm not sure that's what you really want to know, but it would be:

(ServerGotRequest - ClientDoneRequest) - (DNSTime + TCPConnectTime)


