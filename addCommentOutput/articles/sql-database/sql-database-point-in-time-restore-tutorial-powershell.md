<properties 
   pageTitle="Restore an Azure SQL database using Point in Time Restore in Azure PowerShell" 
   description="Point in Time Restore, Windows Azure SQL Database, restore database, recover database, Azure PowerShell" 
   services="sql-database" 
   documentationCenter="" 
   authors="elfisher" 
   manager="jeffreyg" 
   editor="v-romcal"/>

<tags
	ms.service="sql-database"
	ms.date="10/08/2015"
	wacn.date=""/>

# Restore an Azure SQL database using Point in Time Restore in Azure PowerShell

> [AZURE.SELECTOR]
- [Point in Time Restore - portal](/documentation/articles/sql-database-point-in-time-restore-tutorial-management-portal)
- [Point in Time Restore - REST API](/documentation/articles/sql-database-point-in-time-restore-tutorial-rest) 

## Overview

This tutorial shows you how to restore an Azure SQL database using Point in Time Restore in [Azure <!-- deleted by customization PowerShell](/documentation/articles/powershell-install-configure) --><!-- keep by customization: begin --> PowerShell](/documentation/articles/install-configure-powershell) <!-- keep by customization: end -->. Azure SQL Database has built-in backups to support self-service Point in Time Restore for Basic, Standard, and Premium service tiers.

Point in Time Restore creates a new database. The service automatically selects the service tier based on the backup used at the restore point. Make sure you have available quota on the logical server to create another database. If you'd like to request an increased quota, contact [Azure <!-- deleted by customization Support](http://azure.microsoft.com/support/options/) --><!-- keep by customization: begin --> Support](/support/contact/) <!-- keep by customization: end -->.

## Restrictions and Security

See [Restore an Azure SQL database using Point in Time Restore in the Azure Management <!-- deleted by customization Portal](/documentation/articles/sql-database-point-in-time-restore-tutorial-management-portal) --><!-- keep by customization: begin --> Portal](/documentation/articles/sql-database-point-in-time-restore-tutorial-management-portal/) <!-- keep by customization: end -->.

## How to: Restore an Azure SQL database using Point in Time Restore in Azure PowerShell

<!-- deleted by customization
> [AZURE.VIDEO restore-a-sql-database-using-point-in-time-restore-with-microsoft-azure-powershell]

You must use certificate based authentication to run the following cmdlets. For more information, see the *Use the certificate method* section in [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure#use-the-certificate-method).

> [AZURE.IMPORTANT] This article contains commands for versions of Azure PowerShell up to *but not including* versions 1.0 and later. You can check your version of Azure PowerShell with the **Get-Module azure | format-table version** command.
-->
<!-- keep by customization: begin -->
<!--<iframe src="http://channel9.msdn.com/Blogs/Windows-Azure/Restore-a-SQL-Database-Using-Point-in-Time-Restore-With-Microsoft-Azure-PowerShell/player" width="960" height="540" allowFullScreen frameBorder="0"></iframe>-->

You must use certificate based authentication to run the following cmdlets. For more information, see the *Use the certificate method* section in [How to install and configure Azure PowerShell](/documentation/articles/install-configure-powershell/#use-the-certificate-method).
<!-- keep by customization: end -->

1. Get the database you want to restore by using the [Get-AzureSqlDatabase](http://msdn.microsoft.com/zh-cn/library/azure/dn546735.aspx) cmdlet. Specify the following parameters:
	* **ServerName** where the database is located.
	* **DatabaseName** of the database you want to restore.	

<!-- deleted by customization
	`$Database = Get-AzureSqlDatabase -ServerName "myserver" –DatabaseName “mydb”`
-->
<!-- keep by customization: begin -->
	`PS C:\>$Database = Get-AzureSqlDatabase -ServerName "myserver" –DatabaseName “mydb”`
<!-- keep by customization: end -->

2. Begin the restore by using the [Start-AzureSqlDatabaseRestore](http://msdn.microsoft.com/zh-cn/library/azure/dn720218.aspx) cmdlet. Specify the following parameters:	
	* **SourceDatabase** you want to restore from.
	* **TargetDatabaseName** of the database you are restoring to.
	* **PointInTime** you want to restore to.

	Store what is returned to a variable called **$RestoreRequest**. This variable contains the restore request ID which is used for monitoring the status of a restore. 

	<!-- deleted by customization `$RestoreRequest --><!-- keep by customization: begin --> `PS C:\>$RestoreRequest <!-- keep by customization: end --> = Start-AzureSqlDatabaseRestore -SourceDatabase $Database –TargetDatabaseName “myrestoredDB” –PointInTime “2015-01-01 06:00:00”`

A restore may take some time to complete. To monitor the status of the restore, use the [Get-AzureSqlDatabaseOperation](http://msdn.microsoft.com/zh-cn/library/azure/dn546738.aspx) cmdlet and specify the following parameters:

* **ServerName** of the database you are restoring to.
* **OperationGuid** which is the Restore Request ID that was stored in the **$RestoreRequest** variable in Step 2.

<!-- deleted by customization
	`Get-AzureSqlDatabaseOperation –ServerName "myserver" –OperationGuid $RestoreRequest.RequestID`
-->
<!-- keep by customization: begin -->
	`PS C:\>Get-AzureSqlDatabaseOperation –ServerName "myserver" –OperationGuid $RestoreRequest.RequestID`
<!-- keep by customization: end -->

The **State** and **PercentComplete** fields show the status of the restore. 

## Next steps

For more information, see the following:  

<!-- deleted by customization
[Azure SQL Database Business Continuity](/documentation/articles/sql-database-business-continuity)
-->
<!-- keep by customization: begin -->
[Azure SQL Database Business Continuity](http://msdn.microsoft.com/zh-cn/library/azure/hh852669.aspx)

[Azure SQL Database Backup and Restore](http://msdn.microsoft.com/zh-cn/library/azure/jj650016.aspx)
<!-- keep by customization: end -->

[Azure SQL Database Point in Time Restore (blog)](http://azure.microsoft.com/blog/2014/10/01/azure-sql-database-point-in-time-restore/)

[Azure PowerShell](https://msdn.microsoft.com/zh-cn/library/azure/jj156055.aspx)