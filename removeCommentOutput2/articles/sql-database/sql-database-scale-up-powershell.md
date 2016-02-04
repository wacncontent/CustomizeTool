<properties 
    pageTitle="Change the service tier and performance level of an Azure SQL database using PowerShell" 
    description="Change the service tier and performance level of an Azure SQL database shows how to scale your SQL database up or down with PowerShell. Changing the pricing tier of an Azure SQL database with PowerShell." 
	services="sql-database"
	documentationCenter=""
	authors="stevestein"
	manager="jeffreyg"
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="12/01/2015"
	wacn.date=""/>


# Change the service tier and performance level (pricing tier) of a SQL database with PowerShell

**Single database**

> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/sql-database-scale-up)
- [PowerShell](/documentation/articles/sql-database-scale-up-powershell)


This article shows how to change the service tier and performance level of your SQL database with PowerShell.

Use the information in [Upgrade SQL Database Web/Business Databases to New Service Tiers](/documentation/articles/sql-database-upgrade-new-service-tiers) and [Azure SQL Database Service Tiers and Performance Levels](/documentation/articles/sql-database-service-tiers) to determine the appropriate service tier and performance level for your Azure SQL Database.

> [AZURE.IMPORTANT] Changing the service tier and performance level of a SQL database is an online operation. This means your database will remain online and available during the entire operation with no downtime.

- To downgrade a database, the database should be smaller than the maximum allowed size of the target service tier. 
- When upgrading a database with [Standard Geo-Replication](https://msdn.microsoft.com/zh-cn/library/azure/dn758204.aspx) or [Active Geo-Replication](https://msdn.microsoft.com/zh-cn/library/azure/dn741339.aspx) enabled, you must first upgrade its secondary databases to the desired performance tier before upgrading the primary database.
- When downgrading from a Premium service tier, you must first terminate all Geo-Replication relationships. You can follow the steps described in the [Terminate a Continuous Copy Relationship](https://msdn.microsoft.com/zh-cn/library/azure/dn741323.aspx) topic to stop the replication process between the primary and the active secondary databases.
- The restore service offerings are different for the various service tiers. If you are downgrading you may lose the ability to restore to a point in time, or have a lower backup retention period. For more information, see [Azure SQL Database Backup and Restore](https://msdn.microsoft.com/zh-cn/library/azure/jj650016.aspx).
- You can make up to four individual database changes (service tier or performance levels) within a 24 hour period.
- The new properties for the database are not applied until the changes are complete.



**To complete this article you need the following:**

- An Azure subscription. If you need an Azure subscription simply click **FREE TRIAL** at the top of this page, and then come back to finish this article.
- An Azure SQL database. If you do not have a SQL database, create one following the steps in this article: [Create your first Azure SQL Database](/documentation/articles/sql-database-get-started).
- Azure PowerShell.


To run PowerShell cmdlets, you need to have Azure PowerShell installed and running. For detailed information, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).



## Configure your credentials and select your subscription

First you must establish access to your Azure account so start PowerShell and then run the following cmdlet. In the login screen enter the same email and password that you use to sign in to the Azure Management Portal.

	Add-AzureRmAccount

After successfully signing in you will see some information on screen that includes the Id you signed in with and the Azure subscriptions you have access to.


### Select your Azure subscription

To select the subscription you need your subscription Id or subscription name (**-SubscriptionName**). You can copy the subscription Id from the information displayed from previous step, or if you have multiple subscriptions and need more details you can run the **Get-AzureSubscription** cmdlet and copy the desired subscription information from the resultset. Once you have your subscription run the following cmdlet:

	$SubscriptionId = "4cac86b0-1e56-bbbb-aaaa-000000000000"
    Select-AzureRmSubscription -SubscriptionId $SubscriptionId

After successfully running **Select-AzureSubscription** you are returned to the PowerShell prompt. If you have more than one subscription you can run **Get-AzureSubscription** and verify the subscription you want to use shows **IsCurrent: True**.


 


## Change the service tier and performance level of your SQL database

Run the **Set-AzureRmSqlDatabase** cmdlet and set the **-RequestedServiceObjectiveName** to the performance level of the desired pricing tier; for example *S0*, *S1*, *S2*, *S3*, *P1*, *P2*, ...

    $ResourceGroupName = "resourceGroupName"
    
    $ServerName = "serverName"
    $DatabaseName = "databaseName"

    $NewEdition = "Standard"
    $NewPricingTier = "S2"

    $ScaleRequest = Set-AzureRmSqlDatabase -DatabaseName $DatabaseName -ServerName $ServerName -ResourceGroupName $ResourceGroupName -Edition $NewEdition -RequestedServiceObjectiveName $NewPricingTier


  

   


## Sample PowerShell script to change the service tier and performance level of your SQL database

    

    
    $SubscriptionId = "4cac86b0-1e56-bbbb-aaaa-000000000000"
    
    $ResourceGroupName = "resourceGroupName"
    $Location = "China East"
    
    $ServerName = "serverName"
    $DatabaseName = "databaseName"
    
    $NewEdition = "Standard"
    $NewPricingTier = "S2"
    
    Add-AzureRmAccount
    Select-AzureRmSubscription -SubscriptionId $SubscriptionId
    
    $ScaleRequest = Set-AzureRmSqlDatabase -DatabaseName $DatabaseName -ServerName $ServerName -ResourceGroupName $ResourceGroupName -Edition $NewEdition -RequestedServiceObjectiveName $NewPricingTier
    
    $ScaleRequest
    
        


## Next steps

- [Scale out and in](/documentation/articles/sql-database-elastic-scale-get-started)
- [Connect and query a SQL database with SSMS](/documentation/articles/sql-database-connect-query-ssms)
- [Export an Azure SQL database](/documentation/articles/sql-database-export-powershell)

## Additional resources

- [Business Continuity Overview](/documentation/articles/sql-database-business-continuity)
- [SQL Database documentation](/documentation/services/sql-databases)
- [Azure SQL Database Cmdlets](https://msdn.microsoft.com/zh-cn/library/azure/mt163521.aspx)