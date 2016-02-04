<properties 
	pageTitle="How to configure data persistence for a Premium Azure Redis Cache" 
	description="Learn how to configure and manage data persistence your Premium tier Azure Redis Cache instances" 
	services="redis-cache" 
	documentationCenter="" 
	authors="steved0x" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="cache"
	ms.date="12/03/2015"
	wacn.date=""/>

# How to configure data persistence for a Premium Azure Redis Cache

Azure Redis Cache has different cache offerings which provide flexibility in the choice of cache size and features, including the new Premium tier.

The Azure Redis Cache premium tier includes clustering, persistence, and virtual network support. This article describes how to configure persistence in a premium Azure Redis Cache instance.

For information on other premium cache features, see [How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering) and [How to configure Virtual Network support for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-vnet).

## What is data persistence?
Redis persistence allows you to persist data stored in Redis. You can also take snapshots and back up the data which you can load in case of a hardware failure. This is a huge advantage over Basic or Standard tier where all the data is stored in memory and there can be potential data loss in case of a failure where Cache nodes are down. 

Azure Redis Cache offers Redis persistence using the [RDB model](http://redis.io/topics/persistence), where the data is stored in an Azure storage account. When persistence is configured, Azure Redis Cache persists a snapshot of the Redis cache in a Redis binary format to disk based on a configurable backup frequency. If a catastrophic event occurs that disables both the primary and replica cache, the cache is reconstructed using the most recent snapshot.

Persistence can be configured from the **New Redis Cache** blade during cache creation and on the **Settings** blade for existing premium caches.

## Create a premium cache

In Windows Azure China, Redis Cache can only be managed by Azure PowerShell or Azure CLI


[AZURE.INCLUDE [azurerm-azurechinacloud-environment-parameter](../includes/azurerm-azurechinacloud-environment-parameter.md)]


Use the following PowerShell Script to create a premium cache with Redis persistence:

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-WestUS"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 6GB -Sku Premium -RedisConfiguration @{"rdb-backup-enabled"="true"; "rdb-backup-frequency"="60"; "rdb-backup-max-snapshot-count"="1"; "rdb-storage-connection-string"="DefaultEndpointsProtocol=[http|https];AccountName=myAccountName;AccountKey=myAccountKey;EndpointSuffix=core.chinacloudapi.cn"}

The steps in the following section describe how to configure Redis persistence on your new premium cache.

## Configure Redis persistence

You can use **Set-AzureRmRedisCache** PowerShell command to configure Redis data persistence:

	Set-AzureRmRedisCache -Name $cacheName  -ResourceGroupName $resourceGroupName -RedisConfiguration @{"rdb-backup-enabled"="true"; "rdb-backup-frequency"="60"; "rdb-backup-max-snapshot-count"="1"; "rdb-storage-connection-string"="DefaultEndpointsProtocol=[http|https];AccountName=myAccountName;AccountKey=myAccountKey;EndpointSuffix=core.chinacloudapi.cn"}

As you can see in this PowerShell command, for **-RedisConfiguration** parameter, you can set "rdb-backup-enabled" to be true to enable RDB, and false to disable it.

To configure the backup interval, you can set "rdb-backup-frequency" to 15 which means **15 Minutes**, 30 which means **30 minutes**, 60 which means **60 minutes**, 360 which means **6 hours**, 720 which means **12 hours**, 1440 which means and **24 hours**. This interval starts counting down after the previous backup operation successfully completes and when it elapses a new backup is initiated.

To configure a Storage Account, you can "rdb-storage-connection-string" to a connection String in Windows Azure China. As you can see in the command above, you need to specify BlobEndpoint, QueueEndpoint, TableEndpoint in your connection string.

>[AZURE.IMPORTANT] If the storage key for your persistence account is regenerated, you must update your "rdb-backup-frequency".

The next backup (or first backup for new caches) is initiated once the backup frequency interval elapses.



## Persistence FAQ

The following list contains answers to commonly asked questions about Azure Redis Cache persistence.

## Can I enable persistence on a previously created cache?

Yes, Redis persistence can be configured both at cache creation and on existing premium caches.

## Can I change the backup frequency after I create the cache?

Yes, you can change the backup frequency on the **Redis data persistence** blade. For instructions, see [Configure Redis persistence](#configure-redis-persistence).

## Why if I have a backup frequency of 60 minutes there is more than 60 minutes between backups?

The backup frequency interval does not start until the previous backup process has completed successfully. If the backup frequency is 60 minutes and it takes a backup process 15 minutes to successfully complete, the next backup won't start until 75 minutes after the start time of the previous backup.

## What happens to the old backups when a new backup is made

All backups except for the most recent one are automatically deleted. This deletion may not happen immediately but older backups are not persisted indefinitely.

## Next steps
Learn how to use more premium cache features.

-	[How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering)
-	[How to configure Virtual Network support for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-vnet)
  
<!-- IMAGES -->

[redis-cache-new-cache-menu]: ./media/cache-how-to-premium-persistence/redis-cache-new-cache-menu.png

[redis-cache-premium-pricing-tier]: ./media/cache-how-to-premium-persistence/redis-cache-premium-pricing-tier.png

[redis-cache-persistence]: ./media/cache-how-to-premium-persistence/redis-cache-persistence.png

[redis-cache-persistence-selected]: ./media/cache-how-to-premium-persistence/redis-cache-persistence-selected.png

[redis-cache-settings]: ./media/cache-how-to-premium-persistence/redis-cache-settings.png