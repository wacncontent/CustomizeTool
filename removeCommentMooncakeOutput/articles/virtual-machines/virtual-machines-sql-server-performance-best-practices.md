<!-- rename to virtual-machines-windows-sql-performance -->

<properties 
	pageTitle="Performance best practices for SQL Server | Azure"
	description="Provides best practices for optimizing SQL Server performance in Azure VMs."
	services="virtual-machines"
	documentationCenter="na"
	authors="rothja"
	manager="jeffreyg"
	editor="monicar" 
	tags="azure-service-management" />
	
<tags
	ms.service="virtual-machines"
	ms.date="12/22/2015"
	wacn.date=""/>

# Performance best practices for SQL Server in Azure Virtual Machines

## Overview

This topic provides best practices for optimizing SQL Server performance in Azure Virtual Machine. While running SQL Server in Azure Virtual Machines, we recommend that you continue using the same database performance tuning options that are applicable to SQL Server in on-premises server environment. However, the performance of a relational database in a public cloud depends on many factors such as the size of a virtual machine, and the configuration of the data disks.

When creating SQL Server images, consider using the Azure portal to take advantage of features, such as the default use of Premium Storage, and other options, such as Automated Patching, Automated Backup, and AlwaysOn configurations.

This paper is focused on getting the best performance for SQL Server on Azure VMs. If your workload is less demanding, you might not require every optimization listed below. Consider your performance needs and workload patterns as you evaluate these recommendations.

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)]

## Quick check list

The following is a quick check list for optimal performance of SQL Server on Azure Virtual Machines:

|Area|Optimizations|
|---|---|
|**VM size**|[DS3](/documentation/articles/virtual-machines-linux-sizes/#standard-tier-ds-series) or higher for SQL Enterprise edition.<br/><br/>[DS2](/documentation/articles/virtual-machines-linux-sizes/#standard-tier-ds-series) or higher for SQL Standard and Web editions.|
|**Storage**|Use [Premium Storage](/documentation/articles/storage-premium-storage/).<br/><br/>Keep the [storage account](/documentation/articles/storage-create-storage-account/) and SQL Server VM in the same region.<br/><br/>Disable Azure [geo-redundant storage](/documentation/articles/storage-redundancy/) (geo-replication) on the storage account.|
|**Disks**|Use a minimum of 2 [P30 disks](/documentation/articles/storage-premium-storage/#scalability-and-performance-targets-when-using-premium-storage) (1 for log files; 1 for data files and TempDB).<br/><br/>Avoid using operating system or temporary disks for database storage or logging.<br/><br/>Enable read caching on the disk(s) hosting the data files and TempDB.<br/><br/>Do not enable caching on disk(s) hosting the log file.<br/><br/>Stripe multiple Azure data disks to get increased IO throughput.<br/><br/>Format with documented allocation sizes.|
|**I/O**|Enable database page compression.<br/><br/>Enable instant file initialization for data files.<br/><br/>Limit or disable autogrow on the database.<br/><br/>Disable autoshrink on the database.<br/><br/>Move all databases to data disks, including system databases.<br/><br/>Move SQL Server error log and trace file directories to data disks.<br/><br/>Setup default backup and database file locations.<br/><br/>Enable locked pages.<br/><br/>Apply SQL Server performance fixes.|
|**Feature-specific**|Back up directly to blob storage.|

For more information, please follow the guidelines provided in the following sub sections.

## Virtual machine size and storage account considerations

For performance sensitive applications, it's recommended that you use the following virtual machines sizes:

- **SQL Server Enterprise Edition**: DS3 or higher

- **SQL Server Standard and Web Editions**: DS2 or higher

For up-to-date information on supported virtual machine sizes, see [Sizes for Virtual Machines](/documentation/articles/virtual-machines-linux-sizes/).

In addition, we recommend that you create your Azure storage account in the same data center as your SQL Server virtual machines to reduce transfer delays. When creating a storage account, disable geo-replication as consistent write order across multiple disks is not guaranteed. Instead, consider configuring a SQL Server disaster recovery technology between two Azure data centers. For more information, see [High Availability and Disaster Recovery for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-high-availability-dr/).

## Disks and performance considerations

When you create an Azure Virtual Machine, the platform will attach at least one disk to the VM for your operating system disk. This disk is a VHD stored as a page blob in storage. You can also attach additional disks to your virtual machine as data disks, and these will be stored in storage as page blobs. There is another disk present in Azure Virtual Machines called the temporary disk. This is a disk on the node that can be used for scratch space.

### Operating system disk

An operating system disk is a VHD that you can boot and mount as a running version of an operating system and is labeled as **C** drive.

Default caching policy on the operating system disk is **Read/Write**. For performance sensitive applications, we recommend that you use data disks instead of the operating system disk. See the section on Data Disks below.

### Temporary disk

The temporary storage drive, labeled as the **D**: drive, is not persisted to Azure blob storage. Do not store your data or log files on the **D**: drive.

Only store TempDB and/or Buffer Pool Extensions on the **D** drive when using the D-Series or G-Series Virtual Machines (VMs). Unlike the other VM series, the **D** drive in the D-Series and G-Series VMs is SSD-based. This can improve the performance of workloads that heavily use temporary objects or that have working sets which don't fit in memory. For more information, see [Using SSDs in Azure VMs to store SQL Server TempDB and Buffer Pool Extensions](http://blogs.technet.com/b/dataplatforminsider/archive/2014/09/25/using-ssds-in-azure-vms-to-store-sql-server-tempdb-and-buffer-pool-extensions.aspx).

For VMs that support Premium storage, we recommend storing TempDB on a disk that supports Premium Storage with read caching enabled.

### Data Disk

- **Number of data disks for data and log files**: At a minimum, use 2 [P30 disks](/documentation/articles/storage-premium-storage/#scalability-and-performance-targets-when-using-premium-storage) where one disk contains the log file(s) and the other contains the data file(s) and TempDB. For more throughput, you might require additional data disks. To determine the number of data disks, you need to analyze the number of IOPS available for your data and log disk(s). For that information, see the tables on IOPS per [VM size](/documentation/articles/virtual-machines-linux-sizes/) and disk size in the following article: [Using Premium Storage for Disks](/documentation/articles/storage-premium-storage/). If you require more bandwidth, you can attach additional disks use Disk Striping. If you are not using Premium Storage, the recommendation is to add the maximum number of data disks supported by your [VM size](/documentation/articles/virtual-machines-linux-sizes/) and use Disk Striping. For more information about Disk Striping, see the related section below.

- **Caching policy**: Enable read caching on the data disks hosting your data files and TempDB only. If you are not using Premium Storage, do not enable any caching on any data disks. For instructions on configuring disk caching, see the following topics: [Set-AzureOSDisk](https://msdn.microsoft.com/zh-cn/library/azure/jj152847) and [Set-AzureDataDisk](https://msdn.microsoft.com/zh-cn/library/azure/jj152851.aspx).

- **NTFS allocation unit size**: When formatting the data disk, it is recommended that you use a 64-KB allocation unit size for data and log files as well as TempDB.

- **Disk Striping**: We recommend that you follow these guidelines: 

	- For Windows 8/Windows Server 2012 or later, use [Storage Spaces](https://technet.microsoft.com/zh-cn/library/hh831739.aspx). Set stripe size to 64 KB for OLTP workloads and 256 KB for data warehousing workloads to avoid performance impact due to partition misalignment. In addition, set column count = number of physical disks. To configure a Storage Space with more than 8 disks you must use PowerShell (not Server Manager UI) to explicitly set the number of columns to match the number of disks. For more information on how to configure [Storage Spaces](https://technet.microsoft.com/zh-cn/library/hh831739.aspx), see [Storage Spaces Cmdlets in Windows PowerShell](https://technet.microsoft.com/zh-cn/library/jj851254.aspx)
	
	- For Windows 2008 R2 or earlier, you can use dynamic disks (OS striped volumes) and the stripe size is always 64 KB. Note that this option is deprecated as of Windows 8/Windows Server 2012. For information, see the support statement at [Virtual Disk Service is transitioning to Windows Storage Management API](https://msdn.microsoft.com/zh-cn/library/windows/desktop/hh848071.aspx).
	
	- If your workload is not log intensive and does not need dedicated IOPs, you can configure just one storage pool. Otherwise, create two storage pools, one for the log file(s) and another storage pool for the data file(s) and TempDB. Determine the number of disks associated with each storage pool based on your load expectations. Keep in mind that different VM sizes allow different numbers of attached data disks. For more information, see [Sizes for Virtual Machines](/documentation/articles/virtual-machines-linux-sizes/).

## I/O performance considerations

- The best results with Premium Storage are achieved when you parallelize your application and requests. Premium Storage is designed for scenarios where the IO queue depth is greater than 1, so you will see little or no performance gains for single-threaded serial requests (even if they are storage intensive). For example, this could impact the single-threaded test results of performance analysis tools, such as SQLIO.

- Consider using [database page compression](https://msdn.microsoft.com/zh-cn/library/cc280449.aspx) as it can help improve performance of I/O intensive workloads. However, the data compression might increase the CPU consumption on the database server.

- Consider compressing any data files when transferring in/out of Azure.

- Consider enabling instant file initialization to reduce the time that is required for initial file allocation. To take advantage of instant file initialization, you grant the SQL Server (MSSQLSERVER) service account with SE_MANAGE_VOLUME_NAME and add it to the **Perform Volume Maintenance Tasks** security policy. If you are using a SQL Server platform image for Azure, the default service account (NT Service\MSSQLSERVER) isn't added to the **Perform Volume Maintenance Tasks** security policy. In other words, instant file initialization is not enabled in a SQL Server Azure platform image. After adding the SQL Server service account to the **Perform Volume Maintenance Tasks** security policy, restart the SQL Server service. There could be security considerations for using this feature. For more information, see [Database File Initialization](https://msdn.microsoft.com/zh-cn/library/ms175935.aspx).

- **autogrow** is considered to be merely a contingency for unexpected growth. Do not manage your data and log growth on a day-to-day basis with autogrow. If autogrow is used, pre-grow the file using the Size switch.

- Make sure **autoshrink** is disabled to avoid unnecessary overhead that can negatively affect performance.

- If you are running SQL Server 2012, install Service Pack 1 Cumulative Update 10. This update contains the fix for poor performance on I/O when you execute select into temporary table statement in SQL Server 2012. For information, see this [knowledge base article](http://support.microsoft.com/kb/2958012).

- Establish locked pages to reduce IO and any paging activities.

## Feature specific performance considerations

Some deployments may achieve additional performance benefits using more advanced configuration techniques. The following list highlights some SQL Server features that can help you to achieve better performance:

- **Backup to Azure storage**: When performing backups for SQL Server running in Azure virtual machines, you can use [SQL Server Backup to URL](https://msdn.microsoft.com/zh-cn/library/dn435916.aspx). This feature is available starting with SQL Server 2012 SP1 CU2 and recommended for backing up to the attached data disks. When you backup/restore to/from Azure storage, follow the recommendations provided at [SQL Server Backup to URL Best Practices and Troubleshooting and Restoring from Backups Stored in Azure Storage](https://msdn.microsoft.com/zh-cn/library/jj919149.aspx). You can also automate these backups using [Automated Backup for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-classic-sql-automated-backup/).

	Prior to SQL Server 2012, you can use [SQL Server Backup to Azure Tool](https://www.microsoft.com/download/details.aspx?id=40740). This tool can help to increase backup throughput using multiple backup stripe targets.

- **SQL Server Data Files in Azure**: This new feature, [SQL Server Data Files in Azure](https://msdn.microsoft.com/zh-cn/library/dn385720.aspx), is available starting with SQL Server 2014. Running SQL Server with data files in Azure demonstrates comparable performance characteristics as using Azure data disks.

## Next Steps

If you are interested in exploring SQL Server and Premium Storage in more depth, see the article [Use Azure Premium Storage with SQL Server on Virtual Machines](/documentation/articles/virtual-machines-windows-classic-sql-server-premium-storage/).

For security best practices, see [Security Considerations for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-security/).

Review other SQL Server Virtual Machine topics at [SQL Server on Azure Virtual Machines Overview](/documentation/articles/virtual-machines-windows-sql-server-iaas-overview/).
