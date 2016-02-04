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


# How to: Configure firewall settings on SQL Database using TSQL


> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/sql-database-configure-firewall-settings)
- [TSQL](/documentation/articles/sql-database-configure-firewall-settings-tsql)
- [PowerShell](/documentation/articles/sql-database-configure-firewall-settings-powershell)
- [REST API](/documentation/articles/sql-database-configure-firewall-settings-rest)


Windows Azure SQL Database uses firewall rules to allow connections to your servers and databases. You can define server-level and database-level firewall settings for the master or a user database in your Azure SQL Database server to selectively allow access to the database.

> [AZURE.IMPORTANT] To allow applications from Azure to connect to your database server, Azure connections must be enabled. For more information about firewall rules and enabling connections from Azure, see [Azure SQL Database Firewall](/documentation/articles/sql-database-firewall-configure). You may have to open some additional TCP ports if you are making connections inside the Azure cloud boundary. For more information, see the **V12 of SQL Database: Outside vs inside** section of [Ports beyond 1433 for ADO.NET 4.5 and SQL Database V12](/documentation/articles/sql-database-develop-direct-route-ports-adonet-v12)


## Manage server-level firewall rules through Transact-SQL

1. Launch a query window through the Management Portal or through SQL Server Management Studio.
2. Verify you are connected to the master database.
3. Server-level firewall rules can be selected, created, updated, or deleted from within the query window.
4. To create or update server-level firewall rules, execute the sp_set_firewall rule stored procedure. The following example enables a range of IP addresses on the server Contoso.<br/>Start by seeing what rules already exist.

		SELECT * FROM sys.firewall_rules ORDER BY name;

	Next, add a firewall rule.

		EXECUTE sp_set_firewall_rule @name = N'ContosoFirewallRule',
			@start_ip_address = '192.168.1.1', @end_ip_address = '192.168.1.10'

	To delete a server-level firewall rule, execute the sp_delete_firewall_rule stored procedure. The following example deletes the rule named ContosoFirewallRule.
 
		EXECUTE sp_delete_firewall_rule @name = N'ContosoFirewallRule'
 
 
## Database-level firewall rules

1. After creating a server-level firewall for your IP address, launch a query window through the Management Portal or through SQL Server Management Studio.
2. Connect to the database for which you want to create a database-level firewall rule.

	To create a new or update an existing database-level firewall rule, execute the sp_set_database_firewall_rule stored procedure. The following example creates a new firewall rule named ContosoFirewallRule.
 
		EXEC sp_set_database_firewall_rule @name = N'ContosoFirewallRule', @start_ip_address = '192.168.1.11', @end_ip_address = '192.168.1.11'
 
	To delete an existing database-level firewall rule, execute the sp_delete_database_firewall_rule stored procedure. The following example deletes the rule named ContosoFirewallRule.
 
		EXEC sp_delete_database_firewall_rule @name = N'ContosoFirewallRule'


## Next steps

For a tutorial on creating a database, see [Create your first Azure SQL Database](/documentation/articles/sql-database-get-started).
For help in connecting to an Azure SQL database from open source or third-party applications, see [Guidelines for Connecting to Azure SQL Database Programmatically](https://msdn.microsoft.com/zh-cn/library/azure/ee336282.aspx).
To understand how to navigate to databases see [Managing Databases and Logins in Azure SQL Database](https://msdn.microsoft.com/zh-cn/library/azure/ee336235.aspx).

