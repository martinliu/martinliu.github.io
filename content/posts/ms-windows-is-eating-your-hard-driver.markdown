---
author: liuadmin
categories:
- Blog
comments: true
date: 2008-10-24T00:52:53Z
slug: ms-windows-is-eating-your-hard-driver
tags:
- bladelogic
- FolderSize
- opensource
- opensuse
title: M$ Windows is eating your hard driver
url: /2008/10/24/ms-windows-is-eating-your-hard-driver/
wordpress_id: 49235
---

![](http://lh5.ggpht.com/liuzh66/SQEZ0RBOw_I/AAAAAAAAA38/Ulq2AKwYejU/s800/Access%20is%20denied.jpg)No matter Bill says how friendly M$ Windows is. It is eating more and more my free disk space. Toady I figured out some tips for releasing disk space. In Windows file explore, you can not see the folder size without checking on property. So you may need a tool, something like FolderSizes. FolderSize helps me to know more about my heard diver. It shows me there is a folder 'System Volume information", this folder is 6.20GB big. What the hell is that??? I can not even see it in file explore. Then I check on Folder Options, here are so many hiding options for you. In order to take out that big folder, I unchecked '"Hide protected operating system files and folders", then the folder shows up. But I can not open it sine I really wants to know what hell is been hidden in that folder. A error message box popup up"Assess is denied." WOW this is my laptop, I am not able to access the folder. Is this a M$ asset? In FolderSize, I can go inside this folder; it has so many files. Everything in this folder looks like patch file. I have no idea where and when it went down my computer; or this dame OS made it. Now I'm deleting these files and folders in folder 'System Volume information" from FolderSize. Another error message box popup up; it says "Cannot delete XXX000.ps1: It is being used by another person or program". Kidding me? Does anyone share this laptop with me at this moment? Fortunately I have openSuSe, I issued rm -rf command after booted into openSuse. Now 6.2GB space was released.<br /><br /><!--more--><br /><br />Within FolderSize, one more fat folder was identified out, It is ''C:\Documents and Settings\LocalService\Local Settings\Application Data\Google'. I have Google Desktop on my laptop, but I did not use Google desktop search too much, but it take me near 2GBs space. I realized Google desktop indexed my whole hard drive anyway. I have to uninstalled Google Desktop and deleted that folder. Now I got more 2GB space.<br /><br />M$ Windows also did anther favorite for me to created a fat pagefile.sys. It is 3.5 GB; Big~~ isn't it? My laptop have 4GBs physical RAM, but XP only use 3.5GB. As same 32bit OS, openSuSE does use all of 4GB. Since I am short of free space, pagefile.sys was changed to 1.5GB. SO, 2GB spaces was saved.<br /><br />In XP file system, there are some files can not be deleted. I bet you do have some files like that. Those files are already useless, but you can't get rid of them. [ForceDel.exe](http://www.threatexpert.com/files/ForceDel.exe.html) can delete them all. This tiny tool saved me more then 1GB space.<br /><br />6.2+2+2+1=11.2GB<br /><br />There are more screen-shots, please check out: http://picasaweb.google.com/liuzh66/Mis and comment.<br /><br />Ok now I'm be able to create at least two VMWare machines for my work. I hope those tips are helpful for you.<br /><br />In this week, I'm so busy on a Bladelogic product POC testing for CCB which is one of the biggest bank in China. At evening, I usually had to study on ITIL v3 stuff in order to get myself ready for a upcoming training next month. But tonight I'd like to take time off of the work.<br /><br />**XP磁盘空间节省偏方**<br />

<br />
  * 通过类似于FolderSize的工具找出磁盘中占比重比较大的目录，识别需要删除的目录
<br />	
  * 对于System Volume information里的文件，可以用一个USB或者CD引导的Linux系统启动机器，删除；然后再关闭xp中的系统恢复功能
<br />	
  * 如果你不经常使用Google Desktop，或者已经删除了这个程序的话，一定记得删除它建的索引
<br /><br /><br />
