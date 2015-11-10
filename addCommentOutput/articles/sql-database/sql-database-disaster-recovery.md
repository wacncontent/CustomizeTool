<properties 
   pageTitle="SQL Database Disaster Recovery" 
   description="Learn how  to recover a database from a regional datacenter outage or failure with the Azure SQL Database Geo-replication and Geo-restore capabilities." 
   services="sql-database" 
   documentationCenter="" 
   authors="elfisher" 
   manager="jeffreyg" 
   editor="monicar"/>

<tags
	ms.service="sql-database"
	ms.date="07/14/2015"
	wacn.date=""/>

# Recover an Azure SQL Database from an outage

Azure SQL Database's offers a few outage recovery capabilities:

- Active Geo-Replication [(blog)](http://azure.microsoft.com/blog/2014/07/12/spotlight-on-sql-database-active-geo-replication/)
- Standard Geo-Replication [(blog)](http://azure.microsoft.com/blog/2014/09/03/azure-sql-database-standard-geo-replication/)
- Geo-restore [(blog)](http://azure.microsoft.com/blog/2014/09/13/azure-sql-database-geo-restore/)

To learn about preparing for disaster and when to recover your database, visit our [Design for Business Continuity](/documentation/articles/sql-database-business-continuity-design) page. 

##When to initiate recovery 

The recovery operation impacts the application. It requires changing the SQL connection string and could result in permanent data loss. Therefore it should be done only when the outage is likely to last longer than your application's RTO. When the application is deployed to production you should perform regular monitoring of the application health and use the following data points to assert that the recovery is warranted:

1. Permanent connectivity failure from the application tier to the database.
2. Your Azure Management Portal shows an alert about an incident in the region with broad impact.

## Failover to the Geo-Replicated secondary database
> [AZURE.NOTE] You must configure [Standard Geo-Replication](https://msdn.microsoft.com/zh-cn/library/azure/dn758204.aspx) or [Active Geo-Replication](https://msdn.microsoft.com/zh-cn/library/azure/dn741339.aspx) to have a secondary database to use for failover. Geo-Replication is only available for Standard and Premium databases. 

In the event of an outage on the primary database, you can failover to a secondary database to restore availability. To do this you will need to force terminate the continuous copy relationship. For a full description of terminating continuous copy relationships go [here](https://msdn.microsoft.com/zh-cn/library/azure/dn741323.aspx). 



###Azure Management Portal
1. Log in to the [Azure Management <!-- deleted by customization Portal](https://portal.Azure.com) --><!-- keep by customization: begin --> Portal](https://manage.windowsazure.cn) <!-- keep by customization: end -->
2. On the left side of the screen select **BROWSE** and then select **SQL Databases**
3. Navigate to your database and select it. 
4. At the bottom of your database blade select the **Geo Replication map**.
4. Under **Secondaries** right click on the row with the name of the database you want to recover to and select **Stop**.

After the continuous copy relationship is terminated, you can configure your recovered database to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
###PowerShell
Use PowerShell to programmatically perform database recovery.

To terminate the relationship from the secondary database, use the <!-- deleted by customization [Stop-AzureSqlDatabaseCopy](https://msdn.microsoft.com/zh-cn/library/dn720223) --><!-- keep by customization: begin --> [Stop-AzureSqlDatabaseCopy](https://msdn.microsoft.com/zh-CN/library/dn720223) <!-- keep by customization: end --> cmdlet.
		
		$myDbCopy = Get-AzureSqlDatabaseCopy -ServerName "SecondaryServerName" -DatabaseName "SecondaryDatabaseName"
		$myDbCopy | Stop-AzureSqlDatabaseCopy -ServerName "SecondaryServerName" -ForcedTermination
		 
After the continuous copy relationship is terminated, you can configure your recovered database to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
###REST API 
Use REST to programmatically perform database recovery.

1. Get the database continuous copy using the [Get Database <!-- deleted by customization Copy](https://msdn.microsoft.com/zh-cn/library/azure/dn509570.aspx) --><!-- keep by customization: begin --> Copy](https://msdn.microsoft.com/zh-CN/library/azure/dn509570.aspx) <!-- keep by customization: end --> operation.
2. Stop the database continuous copy using the [Stop Database <!-- deleted by customization Copy](https://msdn.microsoft.com/zh-cn/library/azure/dn509573.aspx) --><!-- keep by customization: begin --> Copy](https://msdn.microsoft.com/zh-CN/library/azure/dn509573.aspx) <!-- keep by customization: end --> operation.
Use the secondary server name and database name in the Stop Database Copy request URI

 After the continuous copy relationship is terminated, you can configure your recovered database to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
## Recovery using Geo-Restore

In the event of an outage of a database, you can recover your database from its latest geo redundant backup using Geo-Restore. 

<!-- deleted by customization
> [AZURE.NOTE] Recovering a database creates a new database. It is important to make sure the server you are recovering to has enough DTU capacity for the new database. You can request an increase of this quota by [contacting support](http://azure.microsoft.com/blog/azure-limits-quotas-increase-requests/).

-->
###Azure Management Portal
1. Log in to the [Azure Management <!-- deleted by customization Portal](https://portal.Azure.com) --><!-- keep by customization: begin --> Portal](https://manage.windowsazure.cn) <!-- keep by customization: end -->
2. On the left side of the screen select **NEW**, then select **Data and Storage**, and then select **SQL Database**
2. Select **BACKUP** as the source  and then select the geo redundant backup you want to recover from.
3. Specify the rest of the database properties and then click **Create**.
4. The database restore process will begin and can be monitored using **NOTIFICATIONS** on the left side of the screen.

After the database is recovered you can configure it to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
###PowerShell 
Use PowerShell to programmatically perform database recovery.

<!-- deleted by customization
To start a Geo-Restore request, use the [start-AzureSqlDatabaseRecovery](https://msdn.microsoft.com/zh-cn/library/azure/dn720224.aspx) cmdlet. For a detailed walk through, please see our [how-to video](http://azure.microsoft.com/documentation/videos/restore-a-sql-database-using-geo-restore-with-microsoft-azure-powershell/).
-->
<!-- keep by customization: begin -->
To start a Geo-Restore request, use the [start-AzureSqlDatabaseRecovery](https://msdn.microsoft.com/zh-CN/library/azure/dn720224.aspx) cmdlet.
<!-- keep by customization: end -->

		$Database = Get-AzureSqlRecoverableDatabase -ServerName "ServerName" –DatabaseName “DatabaseToBeRecovered"
		$RecoveryRequest = Start-AzureSqlDatabaseRecovery -SourceDatabase $Database –TargetDatabaseName “NewDatabaseName” –TargetServerName “TargetServerName”
		Get-AzureSqlDatabaseOperation –ServerName "TargetServerName" –OperationGuid $RecoveryRequest.RequestID

After the database is recovered you can configure it to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
###REST API 

Use REST to programmatically perform database recovery.

1.	Get your list of recoverable databases using the [List Recoverable <!-- deleted by customization Databases](http://msdn.microsoft.com/zh-cn/library/azure/dn800984.aspx) --><!-- keep by customization: begin --> Databases](https://msdn.microsoft.com/zh-CN/library/azure/dn800984.aspx) <!-- keep by customization: end --> operation.
	
2.	Get the database you want to recover using the [Get Recoverable <!-- deleted by customization Database](http://msdn.microsoft.com/zh-cn/library/azure/dn800985.aspx) --><!-- keep by customization: begin --> Database](https://msdn.microsoft.com/zh-CN/library/azure/dn800985.aspx) <!-- keep by customization: end --> operation.
	
3.	Create the recovery request using the [Create Database Recovery <!-- deleted by customization Request](http://msdn.microsoft.com/zh-cn/library/azure/dn800986.aspx) --><!-- keep by customization: begin --> Request](https://msdn.microsoft.com/zh-CN/library/azure/dn800986.aspx) <!-- keep by customization: end --> operation.
	
4.	Track the status of the recovery using the [Database Operation <!-- deleted by customization Status](http://msdn.microsoft.com/zh-cn/library/azure/dn720371.aspx) --><!-- keep by customization: begin --> Status](https://msdn.microsoft.com/zh-CN/library/azure/dn720371.aspx) <!-- keep by customization: end --> operation.

After the database is recovered you can configure it to be used by following the [Finalize a Recovered Database](/documentation/articles/sql-database-recovered-finalize) guide.
