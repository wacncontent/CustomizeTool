<properties 
	pageTitle="Using Recovery Manager to fix shard map problems | Windows Azure" 
	description="Use the RecoveryManager class to solve problems with shard maps" 
	services="sql-database" 
	documentationCenter=""  
	manager="jeffreyg"
	authors="ddove"/>

<tags 
	ms.service="sql-database" 
	ms.date="11/09/2015" 
	wacn.date=""/>

# Using the RecoveryManager class to fix shard map problems

The [RecoveryManager](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.recovery.recoverymanager.aspx) class provides ADO.Net applications the ability to easily  detect and correct any inconsistencies between the global shard map (GSM) and the local shard map (LSM) in a sharded database enviroment. 

The GSM and LSM track the mapping of each database in a sharded environment. Occasionally, a break occurs between the GSM and the LSM. in that case, use the RecoveryManager class to detect and repair the break.

The RecoveryManager class is part of the [Elastic Database client library](/documentation/articles/sql-database-elastic-database-client-library). 


![Shard map][1]


For term definitions, see [Elastic Database tools glossary](/documentation/articles/sql-database-elastic-scale-glossary). To understand how the **ShardMapManager** is used to manage data in a sharded solution, see [Shard map management](/documentation/articles/sql-database-elastic-scale-shard-map-management).


## Why use the recovery manager?

In a sharded database environment, there are a number of database servers. Each server contains a number of databases--one per user in a multitenant solution. Each database must be mapped, so that calls can be accurately routed to the correct server and database. Databases are tracked according to a sharding key, and each server is assigned a range of key values. For example, a sharding key may represent the customer names from "D" to "F." The mapping of all servers and their key ranges are contained in the global shard map. Each server also contains a map of the databases contained on the shard--this is known as the local shard map. The LSM is used to validate cached data. (When an app connects to a shard, the mapping is cached with the app for quick retrieval. The LSM validates the mapping.) 

You can move data from one shard to another using a tool such as the Elastic Database client tools library. If a break occurs during the move, the GSM and LSM may become out of sync. Other reasons include:

1. An inconsistency caused by the deletion of a shard whose range is believed to no longer be in use, or by the renaming of a shard. Deleting a shard results in an **orphaned shard mapping**. A renamed database can similarly cause an orphaned shard mapping. In that case, the shard location simply needs to be updated. 
2. A geo-failover event occurs. To continue, one must update the server name, database name and/or shard mapping details for any and all shards in a shard map. In case of a geo-failover, such recovery logic should be automated within the failover workflow. 
3. Either a shard or the ShardMapManager database is restored to an earlier point-in time. 
 
Automating recovery actions enables a frictionless manageability for geo-enabled databases and avoids manual human actions. It also helps with recovery scenarios where data is accidentally deleted. 

For more information about Azure SQL Database Elastic Database tools, Geo-Replication and Restore, please see the following: 

* [Elastic Database features for Azure SQL Database](/documentation/articles/sql-database-elastic-scale-introduction) 
* [Azure SQL Database Business Continuity](/documentation/articles/sql-database-business-continuity) 
* [Get started with elastic database tools](/documentation/articles/sql-database-elastic-scale-get-started)  
* [ShardMap Management](/documentation/articles/sql-database-elastic-scale-shard-map-management)

## Retrieving RecoveryManager from a ShardMapManager 

The first step is to create a RecoveryManager instance. The [GetRecoveryManager method](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.shardmapmanager.getrecoverymanager.aspx) returns the recovery manager for the current [ShardMapManager](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.shardmapmanager.aspx) instance. In order to address any inconsistencies in the shard map, you must first retrieve the RecoveryManager for the particular shard map. 

	ShardMapManager smm = ShardMapManagerFactory.GetSqlShardMapManager(smmConnnectionString,  
             ShardMapManagerLoadPolicy.Lazy);
             RecoveryManager rm = smm.GetRecoveryManager(); 

In this example, the RecoveryManager is initialized from the ShardMapManager. The ShardMapManager containing a ShardMap is also already initialized. 

Since this application code manipulates the shard map itself, the credentials used in the factory method (in the above example, smmConnectionString) should be credentials that have read-write permissions on the GSM database referenced by the connection string. These credentials are typically different from credentials used to open connections for data-dependent routing. For more information, see [Using credentials in the elastic database client](/documentation/articles/sql-database-elastic-scale-manage-credentials).

## Removing a shard from the ShardMap after a shard is deleted

The [DetachShard method](https://msdn.microsoft.com/zh-cn/library/azure/dn842083.aspx) detaches the given shard from the shard map and deletes mappings associated with the shard.  

* The location parameter is the shard location, specifically server name and database name, of the shard being detached. 
* The shardMapName parameter is the shard map name. This is only required when multiple shard maps are managed by the same shard map manager. Optional. 

**Important**:  Use this technique only if you are certain that the range for the updated mapping is empty. The methods above do not check data for the range being moved, so it is best to include checks in your code.

The example below uses the RecoveryManager to remove shards from the Shard Map; the shard map reflects the shard location in the GSM  prior to the deletion of the shard. Because the shard was deleted, it is assumed this was intentional, and the sharding key range is no longer in use. If this is not the case, you can execute point-in time restore to recover the shard from an earlier point-in-time. (In that case, review the section below to detect shard inconsistencies.) Since it is assumed the database deletion was intentional, the final administrative cleanup action is to delete the entry to the shard in the shard map manager. This prevents the application from inadvertently writing information to a range which is not expected.
	
	rm.DetachShard(s.Location, customerMap); 

## To detect mapping differences 

The [DetectMappingDifferences method](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.recovery.recoverymanager.detectmappingdifferences.aspx) selects and returns one of the shard maps (either local or global) as the source of truth and reconciles mappings on both shard maps (GSM and LSM).

	rm.DetectMappingDifferences(location, shardMapName);

* The *location* parameter is the shard location, specifically server name and database name, of the shard. 
* The *shardMapName* parameter is the shard map name. This is only required if multiple shard maps are managed by the same shard map manager. Optional. 

## To resolve mapping differences

The [ResolveMappingDifferences method](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.recovery.recoverymanager.resolvemappingdifferences.aspx) selects one of the shard maps (either local or global) as the source of truth and reconciles mappings on both shard maps (GSM and LSM).

	ResolveMappingDifferences (RecoveryToken, MappingDifferenceResolution);
   
* The *RecoveryToken* parameter enumerates the differences in the mappings between the GSM and the LSM for the specific shard. 

* The [MappingDifferenceResolution enumeration](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.recovery.mappingdifferenceresolution.aspx) is used to indicate the method for resolving the difference between the shard mappings. **MappingDifferenceResolution.KeepShardMapping** is recommended in the event that the LSM contains the accurate mapping and therefore the mapping in the shard should be used. This is typically the case in the event of a failover: the shard now resides on a new server. Since the shard must first be removed from the GSM (using the RecoveryManager.DetachShard method), a mapping no longer exists on the GSM. Therefore, the the LSM must be used to re-establish the shard mapping.

## Attach a shard to the ShardMap after a shard is restored 

The [AttachShard method](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.sqldatabase.elasticscale.shardmanagement.recovery.recoverymanager.attachshard.aspx) attaches the given shard to the shard map. It then detects any shard map inconsistencies and updates the mappings to match the shard at the point of the shard restoration. It is assumed that the database is also renamed to reflect the original database name (prior to when the shard was restored), since the point-in time restoration defaults to a new database appended with the timestamp. 

	rm.AttachShard(location, shardMapName) 

* The *location* parameter is the server name and database name, of the shard being attached. 

* The *shardMapName* parameter is the shard map name. This is only required when multiple shard maps are managed by the same shard map manager. Optional. 

This example adds a shard to the Shard Map which has been recently restored from an earlier point-in time. Since the shard (namely the mapping for the shard in the LSM) has been restored, it is potentially inconsistent with the shard entry in the GSM. Outside of this example code, the shard was restored and renamed to the original name of the database. Since it was restored, it is assumed the mapping in the LSM is the trusted mapping. 

	rm.AttachShard(s.Location, customerMap); 
	var gs = rm.DetectMappingDifferences(s.Location); 
	  foreach (RecoveryToken g in gs) 
	   { 
	   rm.ResolveMappingDifferences(g, MappingDifferenceResolution.KeepShardMapping); 
	   } 

## Updating shard locations after a geo-failover (restore) of the shards

In the event of a geo-failover, the secondary database is made write accessible and becomes the new primary database. The name of the server, and potentially the database (depending on your configuration), may be different from the original primary. Therefore the mapping entries for the shard in the GSM and LSM must be fixed. Similarly, if the database is restored to a different name or location, or to an earlier point in time, this might cause inconsistencies in the shard maps. The Shard Map Manager handles the distribution of open connections to the correct database. Distribution is based on the data in the shard map and the value of the sharding key that is the target of the applicationâs request. After a geo-failover, this information must be updated with the accurate server name, database name and shard mapping of the recovered database. 

## Best practices

Geo-Failover and recovery are operations typically managed by a cloud administrator of the application intentionally utilizing one of Azure SQL Databases business continuity features. Business continuity planning requires processes, procedures, and measures to ensure that business operations can continue without interruption. The methods available as part of the RecoveryManager class should be used within this work flow to ensure the GSM and LSM are kept up-to-date based on the recovery action taken. There are 5 basic steps to properly ensuring the GSM and LSM reflect the accurate information after a failover event. The application code to execute these steps can be integrated into existing tools and workflow. 

1. Retrieve the Recovery Manager from the ShardMapManager. 
2. Detach the old shard from the shard map.
3. Attach the new shard to the shard map, including the new shard location.
4. Detect inconsistencies in the mapping between the GSM and LSM. 
5. Resolve differences between the GSM and the LSM, trusting the LSM. 

This example performs the follwing steps:
1. Removes shards from the Shard Map which reflect shard locations prior to the failover event.
2. Attaches shards to the Shard Map reflecting the new shard locations (the parameter "Configuration.SecondaryServer" is the new server name but the same database name).
3. Retrieves the recovery tokens by detecting mapping differences between the GSM and the LSM for each shard. 
4. Resolves the inconsistencies by trusting the mapping from the LSM of each shard. 

	var shards = smm.GetShards(); 
	foreach (shard s in shards) 
	{ 
	 if (s.Location.Server == Configuration.PrimaryServer) 
		 { 
		  ShardLocation slNew = new ShardLocation(Configuration.SecondaryServer, s.Location.Database); 
		
		  rm.DetachShard(s.Location); 
		
		  rm.AttachShard(slNew); 
		
		  var gs = rm.DetectMappingDifferences(slNew); 
	
		  foreach (RecoveryToken g in gs) 
			{ 
			   rm.ResolveMappingDifferences(g, 						MappingDifferenceResolution.KeepShardMapping); 
			} 
		} 
	} 



[AZURE.INCLUDE [elastic-scale-include](../includes/elastic-scale-include.md)]


<!--Image references-->
[1]: ./media/sql-database-elastic-database-recovery-manager/recovery-manager.png
 