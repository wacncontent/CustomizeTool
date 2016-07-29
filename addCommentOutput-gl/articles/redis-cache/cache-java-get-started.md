<properties
   pageTitle="How to use Azure Redis Cache with Java | Microsoft Azure"
	description="Get started with Azure Redis Cache using Java"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="douge"
	editor=""/>

<tags
	ms.service="cache"
	ms.date="05/31/2016"
	wacn.date=""/>

# How to use Azure Redis Cache with Java

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache/)
- [ASP.NET](/documentation/articles/cache-web-app-howto/)
- [Node.js](/documentation/articles/cache-nodejs-get-started/)
- [Java](/documentation/articles/cache-java-get-started/)
- [Python](/documentation/articles/cache-python-get-started/)

Azure Redis Cache gives you access to a dedicated Redis cache, managed by Microsoft. Your cache is accessible from any application within  Microsoft  Azure.

This topic shows you how to get started with Azure Redis Cache using Java.

## Prerequisites

[Jedis](https://github.com/xetorthio/jedis) - Java client for Redis

This tutorial uses Jedis, but you can use any Java client listed at [http://redis.io/clients](http://redis.io/clients).

## Create a Redis cache on Azure

[AZURE.INCLUDE [redis-cache-create](../includes/redis-cache-create.md)]

## Retrieve the host name and access keys

[AZURE.INCLUDE [redis-cache-create](../includes/redis-cache-access-keys.md)]


## Enable the non-SSL endpoint


Some Redis clients don't support SSL, and by default the [non-SSL port is disabled for new Azure Redis Cache instances](/documentation/articles/cache-configure/#access-ports). At the time of this writing, the [Jedis](https://github.com/xetorthio/jedis) client doesn't support SSL. 


[AZURE.INCLUDE [redis-cache-create](../includes/redis-cache-non-ssl-port.md)]




## Add something to the cache and retrieve it

	package com.mycompany.app;
	import redis.clients.jedis.Jedis;
	import redis.clients.jedis.JedisShardInfo;


	/* Make sure you turn on non-SSL port in Azure Redis using the Configuration section in the Azure Portal */


	/* Make sure you turn on non-SSL port in Azure Redis using Azure PowerShell */

	public class App
	{
	  public static void main( String[] args )
	  {
        /* In this line, replace <name> with your cache name: */
	    JedisShardInfo shardInfo = new  JedisShardInfo("<name>.redis.cache.windows.net"  JedisShardInfo("<name>.redis.cache.chinacloudapi.cn" , 6379);
	    shardInfo.setPassword("<key>"); /* Use your access key. */
	    Jedis jedis = new Jedis(shardInfo);
     	jedis.set("foo", "bar");
     	String value = jedis.get("foo");
	  }
	}


## Next steps


- [Enable cache diagnostics](https://msdn.microsoft.com/library/azure/dn763945.aspx#EnableDiagnostics) so you can [monitor](https://msdn.microsoft.com/library/azure/dn763945.aspx) the health of your cache.

- Read the official [Redis documentation](http://redis.io/documentation).

