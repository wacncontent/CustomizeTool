<properties 
	pageTitle="Upgrade an Azure SQL server to V12 using PowerShell" 
	description="Upgrade an Azure SQL server to V12 using PowerShell." 
	services="sql-database" 
	documentationCenter="" 
	authors="stevestein" 
	manager="jeffreyg" 
	editor=""/>

<tags
	ms.service="sql-database"
	ms.date="10/08/2015"
	wacn.date=""/>

<!-- deleted by customization
# Upgrade to SQL Database V12 using PowerShell


> [AZURE.SELECTOR]
- [Azure Preview Portal](/documentation/articles/sql-database-v12-upgrade)
- [PowerShell](/documentation/articles/sql-database-upgrade-server)


This article shows you how to upgrade to SQL Database V12 using PowerShell. 

During the process of upgrading to SQL Database V12 you must also update any Web and Business databases to a new service tier. The following directions include using pricing tier and elastic pool recommendations to assist with [updating any Web and Business databases](/documentation/articles/sql-database-upgrade-new-service-tiers) on the server. 
-->
<!-- keep by customization: begin -->
# Upgrade Azure SQL server to V12 with PowerShell
 

This article shows you how to upgrade a SQL Database server to V12 using pricing tier and elastic pool recommendations. 

<!-- keep by customization: end -->


## Prerequisites 

To upgrade a server to V12 with PowerShell, you need to have Azure PowerShell installed and running, and  depending on the version you may need to switch it into resource manager mode to access the Azure Resource Manager PowerShell Cmdlets. 

<!-- deleted by customization
> [AZURE.IMPORTANT] Starting with the release of Azure PowerShell 1.0 Preview, the Switch-AzureMode cmdlet is no longer available, and cmdlets that were in the Azure ResourceManger module have been renamed. The examples in this article use the new PowerShell 1.0 Preview naming convention. For detailed information, see [Deprecation of Switch-AzureMode in Azure PowerShell](https://github.com/Azure/azure-powershell/wiki/Deprecation-of-Switch-AzureMode-in-Azure-PowerShell).

To run PowerShell cmdlets, you need to have Azure PowerShell installed and running, and due to the removal of Switch-AzureMode, you should download and install the latest Azure PowerShell by running the [Microsoft Web Platform Installer](http://go.microsoft.com/fwlink/p/?linkid=320376&clcid=0x409). For detailed information, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).


## Configure your credentials and select your subscription
-->
<!-- keep by customization: begin -->
You can download and install the Azure PowerShell modules by running the [Microsoft Web Platform Installer](http://go.microsoft.com/fwlink/p/?linkid=320376&clcid=0x409). For detailed information, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).

The cmdlets for creating and managing Azure SQL Databases are located in the Azure Resource Manager module. When you start Azure PowerShell, the cmdlets in the Azure module are imported by default. To switch to the Azure Resource Manager module, use the **Switch-AzureMode** cmdlet.

	Switch-AzureMode -Name AzureResourceManager

If you get a warning saying 'The Switch-AzureMode cmdlet is deprecated and will be removed in a future release.' You can ignore it and move on to the next section.

For detailed information, see [Using Windows PowerShell with Resource Manager](/documentation/articles/powershell-azure-resource-manager).



## Configure your credentials
<!-- keep by customization: end -->

To run PowerShell cmdlets against your Azure subscription you must first establish access to your Azure account. Run the following and you will be presented with a sign in screen to enter your credentials. Use the same email and password that you use to sign in to the Azure Management Portal.

	Add-AzureAccount

After successfully signing in you should see some information on screen that includes the Id you signed in with and the Azure subscriptions you have access to.
<!-- keep by customization: begin -->


## Select your Azure subscription
<!-- keep by customization: end -->

To select the subscription you want to work with you need your subscription Id (**-SubscriptionId**) or subscription name (**-SubscriptionName**). You can copy it from the previous step, or if you have multiple subscriptions you can run the **Get-AzureSubscription** cmdlet and copy the desired subscription information from the resultset.

Run the following cmdlet with your subscription information to set your current subscription:

	Select-AzureSubscription -SubscriptionId 4cac86b0-1e56-bbbb-aaaa-000000000000

The following commands will be run against the subscription you just selected above.

## Get Recommendations

To get the recommendation for the server upgrade run the following cmdlet: 

<!-- deleted by customization
    $hint = Get-AzureRMSqlServerUpgradeHint -ResourceGroupName “resourcegroup1” -ServerName “server1” 
-->
<!-- keep by customization: begin -->
    $hint = Get-AzureSqlServerUpgradeHint -ResourceGroupName “resourcegroup1” -ServerName “server1” 
<!-- keep by customization: end -->

For more information, see [Azure SQL Database elastic database pool recommendations](/documentation/articles/sql-database-elastic-pool-portal#elastic-database-pool-pricing-tier-recommendations) and [Azure SQL Database picing tier recommendations](/documentation/articles/sql-database-service-tier-advisor). 



## Start the upgrade

To start the upgrade of the server run the following cmdlet: 

    <!-- deleted by customization Start-AzureRMSqlServerUpgrade --><!-- keep by customization: begin --> Start-AzureSqlServerUpgrade <!-- keep by customization: end --> -ResourceGroupName “resourcegroup1” -ServerName “server1” -ServerVersion 12.0 -DatabaseCollection $hint.Databases -ElasticPoolCollection $hint.ElasticPools


When you run this command upgrade process will begin. You can customize the output of the recommendation and provide the edited recommendation to this cmdlet. 


<!-- deleted by customization
## Upgrade a server
-->
<!-- keep by customization: begin -->
## Upgrade an Azure SQL server
<!-- keep by customization: end -->


    # Adding the account
    #
    Add-AzureAccount
    
<!-- keep by customization: begin -->
    # Switch mode
    #
    Switch-AzureMode -Name AzureResourceManager

<!-- keep by customization: end -->
    # Setting the variables
    #
    $SubscriptionName = 'YOUR_SUBSCRIPTION' 
    $ResourceGroupName = 'YOUR_RESOURCE_GROUP' 
    $ServerName = 'YOUR_SERVER' 
    
    # Selecting the right subscription 
    # 
<!-- deleted by customization
    Select-AzureSubscription -SubscriptionName $SubscriptionName 
-->
<!-- keep by customization: begin -->
    Select-AzureSubscription $SubscriptionName 
<!-- keep by customization: end -->
    
    # Getting the upgrade recommendations 
    #
<!-- deleted by customization
    $hint = Get-AzureRMSqlServerUpgradeHint -ResourceGroupName $ResourceGroupName -ServerName $ServerName 
-->
<!-- keep by customization: begin -->
    $hint = Get-AzureSqlServerUpgradeHint -ResourceGroupName $ResourceGroupName -ServerName $ServerName 
<!-- keep by customization: end -->
    
    # Starting the upgrade process 
    #
    <!-- deleted by customization Start-AzureRMSqlServerUpgrade --><!-- keep by customization: begin --> Start-AzureSqlServerUpgrade <!-- keep by customization: end --> -ResourceGroupName $ResourceGroupName -ServerName $ServerName -ServerVersion 12.0 -DatabaseCollection $hint.Databases -ElasticPoolCollection $hint.ElasticPools


## Custom upgrade mapping

If the recommendations are not appropriate for your server and business case, then you can choose how your databases are upgraded and can map them to either single or elastic databases.

<!-- deleted by customization
ElasticPoolCollection and DatabaseCollection parameters are optional:
    
    # Creating elastic pool mapping
    #
    $elasticPool = New-Object -TypeName Microsoft.Azure.Management.Sql.Models.UpgradeRecommendedElasticPoolProperties 
    $elasticPool.DatabaseDtuMax = 100 
    $elasticPool.DatabaseDtuMin = 0 
    $elasticPool.Dtu = 800 
    $elasticPool.Edition = "Standard" 
    $elasticPool.DatabaseCollection = ("DB1", “DB2”, “DB3”, “DB4”) 
    $elasticPool.Name = "elasticpool_1" 
    $elasticPool.StorageMb = 800 
     
    # Creating single database mapping for 2 databases. DBMain1 mapped to S0 and DBMain2 mapped to S2
    #
    $databaseMap1 = New-Object -TypeName Microsoft.Azure.Management.Sql.Models.UpgradeDatabaseProperties 
    $databaseMap1.Name = "DBMain1" 
    $databaseMap1.TargetEdition = "Standard" 
    $databaseMap1.TargetServiceLevelObjective = "S0"
    
    $databaseMap2 = New-Object -TypeName Microsoft.Azure.Management.Sql.Models.UpgradeDatabaseProperties 
    $databaseMap2.Name = "DBMain2" 
    $databaseMap2.TargetEdition = "Standard" 
    $databaseMap2.TargetServiceLevelObjective = "S2"
     
    # Starting the upgrade
    #
    Start-AzureRMSqlServerUpgrade –ResourceGroupName resourcegroup1 –ServerName server1 -Version 12.0 -DatabaseCollection @($databaseMap1, $databaseMap2) -ElasticPoolCollection @($elasticPool) 

-->
<!-- keep by customization: begin -->
Upgrade databases into an elastic database pool:

    $elasticPool = New-Object -TypeName Microsoft.Azure.Management.Sql.Models.UpgradeRecommendedElasticPoolProperties
    $elasticPool.DatabaseDtuMax = 100  
    $elasticPool.DatabaseDtuMin = 0  
    $elasticPool.Dtu = 800
    $elasticPool.Edition = "Standard"  
    $elasticPool.DatabaseCollection = ("DB1")  
    $elasticPool.Name = "elasticpool_1"  


Upgrade databases into single databases:

    $databaseMap = New-Object -TypeName Microsoft.Azure.Management.Sql.Models.UpgradeDatabaseProperties  
    $databaseMap.Name = "DB2"
    $databaseMap.TargetEdition = "Standard"
    $databaseMap.TargetServiceLevelObjective = "S0"
    Start-AzureSqlServerUpgrade –ResourceGroupName resourcegroup1 –ServerName server1 -Version 12.0 -DatabaseCollection($databaseMap) -ElasticPoolCollection ($elasticPool)
<!-- keep by customization: end -->
    




## Related Information

<!-- deleted by customization
- [Get-AzureRMSqlServerUpgrade](https://msdn.microsoft.com/zh-cn/library/azure/mt603582.aspx)
- [Start-AzureRMSqlServerUpgrade](https://msdn.microsoft.com/zh-cn/library/azure/mt619403.aspx)
- [Stop-AzureRMSqlServerUpgrade](https://msdn.microsoft.com/zh-cn/library/azure/mt603589.aspx)


-->
<!-- keep by customization: begin -->
- [Azure SQL Database Resource Manager Cmdlets](https://msdn.microsoft.com/zh-cn/library/mt163521.aspx)
- [Azure SQL Database Service Management Cmdlets](https://msdn.microsoft.com/zh-cn/library/dn546726.aspx)
 

<!-- keep by customization: end -->