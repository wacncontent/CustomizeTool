<properties
	pageTitle="How to: Configure firewall settings | Windows Azure"
	description="Learn how to configure the firewall for IP addresses that access Azure SQL databases."
	services="sql-database"
	documentationCenter=""
	authors="BYHAM"
	manager="jeffreyg"
	editor=""/>


<tags
	ms.service="sql-database"
	ms.date="11/13/2015"
	wacn.date=""/>


# How to: Configure firewall settings on SQL Database using PowerShell


> [AZURE.SELECTOR]
<!-- deleted by customization
- [Azure Management Portal](/documentation/articles/sql-database-configure-firewall-settings)
-->
- [TSQL](/documentation/articles/sql-database-configure-firewall-settings-tsql)
- [PowerShell](/documentation/articles/sql-database-configure-firewall-settings-powershell)
- [REST API](/documentation/articles/sql-database-configure-firewall-settings-rest)


Windows Azure SQL Database uses firewall rules to allow connections to your servers and databases. You can define server-level and database-level firewall settings for the master or a user database in your Azure SQL Database server to selectively allow access to the database.

> [AZURE.IMPORTANT] To allow applications from Azure to connect to your database server, Azure connections must be enabled. For more information about firewall rules and enabling connections from Azure, see [Azure SQL Database Firewall](/documentation/articles/sql-database-firewall-configure). You may have to open some additional TCP ports if you are making connections inside the Azure cloud boundary. For more information, see the **V12 of SQL Database: Outside vs inside** section of [Ports beyond 1433 for ADO.NET 4.5 and SQL Database V12](/documentation/articles/sql-database-develop-direct-route-ports-adonet-v12)


## Manage server-level firewall rules through Azure PowerShell
1. Launch Azure PowerShell.
2. Server-level firewall rules can be created, updated, and deleted using Azure PowerShell. 

	To create a new server-level firewall rule, execute the New-AzureSqlDatabaseServerFirewallRule cmdlet. The following example enables a range of IP addresses on the server Contoso.
 
		New-AzureSqlDatabaseServerFirewallRule -StartIPAddress 192.168.1.1 -EndIPAddress 192.168.1.10 -RuleName ContosoFirewallRule -ServerName Contoso
 
	To modify an existing server-level firewall rule, execute the Set-AzureSqlDatabaseServerFirewallRule cmdlet. The following example changes the range of acceptable IP addresses for the rule named ContosoFirewallRule.
 
		Set-AzureSqlDatabaseServerFirewallRule -StartIPAddress 192.168.1.4 -EndIPAddress 192.168.1.10 -RuleName ContosoFirewallRule -ServerName Contoso

	To delete an existing server-level firewall rule, execute the Remove-AzureSqlDatabaseServerFirewallRule cmdlet. The following example deletes the rule named ContosoFirewallRule.

		Remove-AzureSqlDatabaseServerFirewallRule -RuleName ContosoFirewallRule -ServerName Contoso


## Manage firewall rules using PowerShell

* [New-AzureSqlDatabaseServerFirewallRule](https://msdn.microsoft.com/zh-cn/library/azure/dn546724.aspx)
* [Remove-AzureSqlDatabaseServerFirewallRule](https://msdn.microsoft.com/zh-cn/library/azure/dn546727.aspx)
* [Set-AzureSqlDatabaseServerFirewallRule](https://msdn.microsoft.com/zh-cn/library/azure/dn546739.aspx)
* [Get-AzureSqlDatabaseServerFirewallRule](https://msdn.microsoft.com/zh-cn/library/azure/dn546731.aspx)
 
## Next steps

For a tutorial on creating a database, see [Create your first Azure SQL Database](/documentation/articles/sql-database-get-started).
For help in connecting to an Azure SQL database from open source or third-party applications, see [Guidelines for Connecting to Azure SQL Database Programmatically](https://msdn.microsoft.com/zh-cn/library/azure/ee336282.aspx).
To understand how to navigate to databases see [Managing Databases and Logins in Azure SQL Database](https://msdn.microsoft.com/zh-cn/library/azure/ee336235.aspx).

<!--Image references-->
[1]: ./media/sql-database-configure-firewall-settings/AzurePortalBrowseForFirewall.png
[2]: ./media/sql-database-configure-firewall-settings/AzurePortalFirewallSettings.png
<!--anchors-->

 
