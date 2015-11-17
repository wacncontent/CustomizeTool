deletion:

deleted:

		> [AZURE.NOTE] This article contains commands for versions of Azure PowerShell up to *but not including* versions 1.0.0 and later. You can check your version of Azure PowerShell with the **Get-Module azure | format-table version** command. The Azure PowerShell command blocks in this article are in the process of being tested and updated to support the new cmdlets in Azure PowerShell versions 1.0.0 and later. Thank you for your patience.

reason: ()

deleted:

		> [AZURE.NOTE] Because these virtual machines are for an intranet application, they are not assigned a public IP address or a DNS domain name label and exposed to the Internet. However, this also means that you cannot connect to them from the Azure Preview portal. The **Connect** button will be unavailable when you view the properties of the virtual machine. Use the Remote Desktop Connection accessory or another Remote Desktop tool to connect to the virtual machine using its private IP address or intranet DNS name.

reason: ()

replacement:

deleted:

		[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] classic deployment model.
		
		
		In this phase of deploying a high-availability line of business application in Azure infrastructure services, you configure the two computers running SQL Server and the cluster majority node computer, and then combine them into a Windows Server cluster.

replaced by:

		In this phase of deploying a a high-availability line of business application in Azure infrastructure services, you configure the two computers running SQL Server and the cluster majority node computer, and then combine them into a Windows Server cluster.

reason: ()

deleted:

		> [AZURE.NOTE] These instructions use a SQL Server image in the Azure image gallery and you are charged ongoing costs for the use of the SQL Server license. It is also possible to create virtual machines in Azure and install your own SQL Server licenses, but you must have Software Assurance and License Mobility to use your SQL Server license on a virtual machine, including an Azure virtual machine. For more information about installing SQL Server on a virtual machine, see [Installation for SQL Server](https://msdn.microsoft.com/zh-cn/library/bb500469.aspx).

replaced by:

		> [AZURE.NOTE] These instructions use a SQL Server image in the Azure image gallery and you are charged ongoing costs for the use of the SQL Server license. It is also possible to create virtual machines in Azure and install your own SQL Server licenses, but those instructions are not included here.

reason: ()

