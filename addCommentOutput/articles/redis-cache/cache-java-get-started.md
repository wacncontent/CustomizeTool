<properties
   pageTitle="How to use Azure Redis Cache with Java | Windows Azure"
	description="Get started with Azure Redis Cache using Java"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="cache"
	ms.date="12/03/2015"
	wacn.date=""/>

# How to use Azure Redis Cache with Java

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache)
- [Node.js](/documentation/articles/cache-nodejs-get-started)
- [Java](/documentation/articles/cache-java-get-started)
- [Python](/documentation/articles/cache-python-get-started)

Azure Redis Cache gives you access to a dedicated Redis cache, managed by Microsoft. Your cache is accessible from any application within Windows Azure.

This topic shows you how to get started with Azure Redis Cache using Java.


## Prerequisites

[Jedis](https://github.com/xetorthio/jedis) - Java client for Redis

This tutorial uses Jedis, but you can use any Java client listed at [http://redis.io/clients](http://redis.io/clients).


## Create a Redis cache on Azure

<!-- deleted by customization
In the [Azure Management Portal](https://manage.windowsazure.cn/), click **New**, **DATA SERVICE**, and select **Redis Cache**.

  ![][1]

Enter a DNS hostname. It will have the form `<name>.redis.cache.chinacloudapi.cn`. Click **Create**.

  ![][2]

Once you create the cache, click on it in the Azure Management Portal to view the cache settings. Click the link under **Keys** and copy the primary key. You need this to authenticate requests.

  ![][4]
-->
<!-- keep by customization: begin -->
In Windows Azure China, Redis Cache can only be managed by Azure PowerShell or Azure CLI

[AZURE.INCLUDE [azurerm-azurechinacloud-environment-parameter](../includes/azurerm-azurechinacloud-environment-parameter.md)]

Use the following PowerShell Script to create a cache:

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-ChinaNorth"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 250MB -Sku Basic
<!-- keep by customization: end -->


## Enable the non-SSL endpoint

<!-- deleted by customization

Click the link under **Ports**, and click **No** for "Allow access only via SSL". This enables the non-SSL port for the cache. The Jedis client currently does not support SSL.

  ![][3]
-->
<!-- keep by customization: begin -->
You can use the following PowerShell command to enable the non-SSL endpoint

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true
<!-- keep by customization: end -->


## Add something to the cache and retrieve it

	package com.mycompany.app;
	import redis.clients.jedis.Jedis;
	import redis.clients.jedis.JedisShardInfo;

<!-- deleted by customization
	/* Make sure you turn on non-SSL port in Azure Redis using the Configuration section in the Azure Management Portal */
-->
<!-- keep by customization: begin -->
	/* Make sure you turn on non-SSL port in Azure Redis using Azure PowerShell */
<!-- keep by customization: end -->
	public class App
	{
	  public static void main( String[] args )
	  {
        /* In this line, replace <name> with your cache name: */
	    JedisShardInfo shardInfo = new JedisShardInfo("<name>.redis.cache.chinacloudapi.cn", 6379);
	    shardInfo.setPassword("<key>"); /* Use your access key. */
	    Jedis jedis = new Jedis(shardInfo);
     	jedis.set("foo", "bar");
     	String value = jedis.get("foo");
	  }
	}


## Next steps

- [Enable cache diagnostics](https://msdn.microsoft.com/zh-cn/library/azure/dn763945.aspx#EnableDiagnostics) so you can [monitor](https://msdn.microsoft.com/zh-cn/library/azure/dn763945.aspx) the health of your cache.
- Read the official [Redis documentation](http://redis.io/documentation).


<!--Image references-->
[1]: ./media/cache-java-get-started/cache01.png
[2]: ./media/cache-java-get-started/cache02.png
[3]: ./media/cache-java-get-started/cache03.png
[4]: ./media/cache-java-get-started/cache04.png
