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
	ms.date="12/16/2015"
        wacn.date=""/>


# How to: Configure firewall settings on SQL Database using the Azure Management Portal


> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/sql-database-configure-firewall-settings)
- [TSQL](/documentation/articles/sql-database-configure-firewall-settings-tsql)
- [PowerShell](/documentation/articles/sql-database-configure-firewall-settings-powershell)
- [REST API](/documentation/articles/sql-database-configure-firewall-settings-rest)


SQL Database uses firewall rules to allow connections to your servers and databases. You can define server-level and database-level firewall settings for the master or a user database in your SQL Database logical server to selectively allow access to the database.

> [AZURE.IMPORTANT] To allow applications from Azure to connect to your database server, Azure connections must be enabled. For more information about firewall rules and enabling connections from Azure, see [Azure SQL Database Firewall](/documentation/articles/sql-database-firewall-configure). You may have to open some additional TCP ports if you are making connections inside the Azure cloud boundary. For more information, see the **V12 of SQL Database: Outside vs inside** section of [Ports beyond 1433 for ADO.NET 4.5 and SQL Database V12](/documentation/articles/sql-database-develop-direct-route-ports-adonet-v12)


### Manage server-level firewall rules through the Azure Management Portal


[AZURE.INCLUDE [sql-database-include-ip-address-22-v12portal](../includes/sql-database-include-ip-address-22-v12portal.md)]


## Manage server-level firewall rules 

1. In the Azure Management Portal, click **SQL Databases**. All databases and their corresponding servers are listed here.
2. Click **Servers** at the top of the page.
3. Click the arrow beside the server for which you want to manage firewall rules.
4. Click **Configure** at the top of the page.

	*  To add the current computer, click Add to the Allowed IP Addresses.
	*  To add additional IP addresses, type in the Rule Name, Start IP Address, and End IP Address.
	*  To modify an existing rule, click any of the fields in the rule and modify.
	*  To delete an existing rule, hover over the rule until the X appears at the end of the row. Click X to remove the rule.
5. Click **Save** at the bottom of the page to save the changes.


## Next steps

For a tutorial on creating a database, see [Create your first Azure SQL Database](/documentation/articles/sql-database-get-started).
For help in connecting to an Azure SQL database from open source or third-party applications, see [Guidelines for Connecting to Azure SQL Database Programmatically](https://msdn.microsoft.com/zh-cn/library/azure/ee336282.aspx).
To understand how to navigate to databases see [Managing Databases and Logins in Azure SQL Database](https://msdn.microsoft.com/zh-cn/library/azure/ee336235.aspx).

<!--Image references-->
[1]: ./media/sql-database-configure-firewall-settings/AzurePortalBrowseForFirewall.png
[2]: ./media/sql-database-configure-firewall-settings/AzurePortalFirewallSettings.png
<!--anchors-->

 
