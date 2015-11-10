<properties
   pageTitle="Azure Backup limits table"
   description="Describes system limits for Azure Backup."
   services="backup"
   documentationCenter="NA"
   authors="Jim-Parker"
   manager="jwhit"
   editor="" />
<tags
	ms.service="backup"
	ms.date="10/05/2015"
	wacn.date=""/>


The following limits apply to Azure Backup.

| Limit Identifier | Default Limit |
|---|---|
<!-- deleted by customization
|Number of servers/machines that can be registered against each vault|50 for Windows Server/Client/SCDPM <br/> 200 for IaaS VMs|
|Size of a data source for data stored in Azure vault storage|54400 GB max<sup>1</sup>|
-->
<!-- keep by customization: begin -->
|Number of servers/machines that can be registered against each vault|50|
|Size of a data source for data stored in Azure vault storage|1.65 TB max<sup>1</sup>|
<!-- keep by customization: end -->
|Number of backup vaults that can be created in each Azure subscription|25|
|Number of times backup can be scheduled per day|3 per day for Windows Server/Client <br/> 2 per day for <!-- deleted by customization SCDPM <br/> Once a day for IaaS VMs| --><!-- keep by customization: begin --> SCDPM| <!-- keep by customization: end -->
<!-- deleted by customization
|Data disks attached to an Azure virtual machine for backup|16|

- <sup>1</sup>The 54400 GB limit does not apply to IaaS VM backup.


-->
<!-- keep by customization: begin -->
|Number of recovery points that can be created|366<sup>2</sup>|
|Data disks attached to an Azure virtual machine for backup|5|

- <sup>1</sup>The 1.65TB limit does not apply to IaaS VM backup.
- <sup>2</sup>You can use any permutation to arrive at a number which is less than 366.

<!-- keep by customization: end -->