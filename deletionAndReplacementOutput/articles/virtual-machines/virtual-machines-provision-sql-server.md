deletion:

deleted:

		>[AZURE.NOTE] This article describes how to provision a SQL Server VM with the existing Azure Management Portal. However, it is also possible to create and manage SQL Server VMs in the [new Portal](https://manage.windowsazure.cn). There are some advantages to the new portal, such as defaulting to the use of Premium Storage, and other options, such as Automated Patching, Automated Backup, and AlwaysOn configurations. Future content will cover step-by-step instructions.

reason: ()

replacement:

deleted:

		[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.
		.

replaced by:

		[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-include.md)] This article covers creating a resource with the classic deployment model.

reason: ()

deleted:

		> - For production workloads, we recommend using Premium Storage with the following minimum recommended sizes: **DS3** for SQL Server Enterprise edition and **DS2** for SQL Server Standard edition. For more information, see [Performance Best Practices for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-sql-server-performance-best-practices).
			> - The  selected size limits the number of data disks you can configure. For most up-to-date information on available virtual machine sizes and the number of data disks that you can attach to a virtual machine, see [Virtual Machine Sizes for Azure](/documentation/articles/virtual-machines-size-specs).

replaced by:

		> - A2 is the smallest size recommended for production workloads. 
		    > - The minimum recommended size for a virtual machine is A3 when using SQL Server Enterprise Edition.
		    > - Select A3 or higher when using SQL Server Enterprise Edition.
		   	> - Select A4 or higher when using SQL Server 2012 or 2014 Enterprise Optimized for Transactional Workloads images.  
		   	> - Select A7 or higher when using SQL Server 2012 or 2014 Enterprise Optimized for Data Warehousing Workloads images. 
		   	> - For the best performance use DS2 or DS3 with Premium Storage. For more information, see [Performance Best Practices for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-sql-server-performance-best-practices).
			> - The size selected  limits the number of data disks you can configure. For most up-to-date information on available virtual machine sizes and the number of data disks that you can attach to a virtual machine, see [Virtual Machine Sizes for Azure](/documentation/articles/virtual-machines-size-specs).

reason: ()

