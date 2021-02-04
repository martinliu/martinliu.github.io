---
author: liuadmin
categories:
- CloudForms
comments: true
date: 2015-03-30T03:13:47Z
subtitle: 下载CloudForms最新版本的rhev的虚拟机，导入到rhevm的nfs export存储中。从模板生成虚拟机。运行和配置CloudForms虚拟机，这样它就可以管理这个rhevm的环境了。
slug: import-cloudforms-into-rhevm
tags:
- cfme
title: Import CloudForms  into rhevm
url: /2015/03/30/import-cloudforms-into-rhevm/
wordpress_id: 53659
---

[bash]
[root@rhevm03 export]# cat /etc/exports
/var/lib/exports/iso *(rw)
/export/rhev_import_export_disk *(rw,sync,no_subtree_check,all_squash,anonuid=36,anongid=36)
/export/template *(rw,sync,no_subtree_check,all_squash,anonuid=36,anongid=36)
# [root@rhevm03 export]# engine-image-uploader -N cfme5351 -e export-nfs-rhevm -v -m upload /tmp/cfme-rhevm-5.3-51.x86_64.rhevm.ova
[/bash]

然后从Web Console上导入这个模板，创建一个目标规格的虚拟机。
