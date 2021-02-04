---
author: liuadmin
categories:
- CMS/CMDB
comments: true
date: 2011-01-12T05:08:23Z
slug: bmc-atrium-cmdb-ci
tags:
- Atrium
- BMC
- ci
- cmdb
- relationship
title: BMC Atrium CMDB CI数据迁移
url: /2011/01/12/bmc-atrium-cmdb-ci/
wordpress_id: 50859
---

在不同的CMDB服务器之间做数据迁移之前一定要注意两点：1）保持两边的CDM相同；2）先导入CI数据在导入CI相关的关系数据。另外就是每个类导入完毕之后要做数据完整性和正确性的抽检。以下使用的工具是cmdbdriver，该命令初始化和一般性的参数介绍请参考相关文档。

_**CI数据导出示例**_

Command: xexpdt
XEXPORT DATA
Export instance data from all classes? (F):
Classes to export data from:
Class and its subclasses, From namespace (1,2) (1):
Namespace (): BMC.CORE
Class name (): BMC_ComputerSystem
Dataset ID (): BMC.ASSET
Filename for exported data: C:\DEMO\cs-ci
Exporting Class BMC_ComputerSystem
i=0: namespaceName = BMC.CORE, className = BMC_ComputerSystemExported without errorsExporting Class BMC_MainframeExporti
ng Class BMC_PrinterExporting Class BMC_StorageSubsystem
CMDBExportData  results
ReturnCode:  OK
Status List : 0 items

到相应目录下面找到导出的文件，导出的结果至少是两个文件一个是META_FILE其他的才是CI数据文件。

_**关系数据导出示例**_

Command: xexpdt
XEXPORT DATA
Export instance data from all classes? (F):
Classes to export data from:
Class and its subclasses, From namespace (1,2) (1):
Namespace (): BMC.CORE
Class name (): BMC_Dependency
Dataset ID (): BMC.ASSET
Filename for exported data: C:\DEMO\REL-DEP.XML
Exporting Class BMC_Dependency
i=0: namespaceName = BMC.CORE, className = BMC_DependencyExported without errorsExporting Class BMC_AccountOnSystemExpor
ting Class BMC_HostedAccessPointExporting Class BMC_HostedServiceExporting Class BMC_InventoryBulkItemsExporting Class B
MC_InventoryComputerSystemsExporting Class BMC_InventoryEquipmentExporting Class BMC_InventorySystemComponents
CMDBExportData  results
ReturnCode:  OK
Status List : 0 items

到相应目录下面找到导出的文件，导出的结果至少是两个文件一个是META_FILE其他的才是CI数据文件。

_**导入数据示例**_

Command: impdt
IMPORT INSTANCE DATA
Handle duplicate Instance Ids:
(Error/New ID for Dup/Merge/New ID for All) (1-4) (1): 3
Filename containing import data: c:\demo\cs-ci_0_0  (导入包含CI数据的文件)

CMDBImportData  results
ReturnCode:  OK
Status List : 0 items
Total items Processed             :  2
Items Imported successfully       :  2
Items for which Import failed     :  0

Command: impdt
IMPORT INSTANCE DATA
Handle duplicate Instance Ids:
(Error/New ID for Dup/Merge/New ID for All) (1-4) (1): 3
Filename containing import data: c:\demo\REL-DEP.XML_0_0 (导入包含关系数据的文件)

CMDBImportData  results
ReturnCode:  OK
Status List : 0 items
Total items Processed             :  1
Items Imported successfully       :  1
Items for which Import failed     :  0

导入完毕之后使用Remedy User到相应的表格中查找，确认导入的数据是否正确。
