<properties
	pageTitle="How to use Azure Redis Cache with Node.js | Windows Azure"
	description="Get started with Azure Redis Cache using Node.js and node_redis."
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.date="12/03/2015"
	wacn.date=""/>

# How to use Azure Redis Cache with Node.js

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache)
- [Node.js](/documentation/articles/cache-nodejs-get-started)
- [Java](/documentation/articles/cache-java-get-started)
- [Python](/documentation/articles/cache-python-get-started)

Azure Redis Cache gives you access to a secure, dedicated Redis cache, managed by Microsoft. Your cache is accessible from any application within Windows Azure.

This topic shows you how to get started with Azure Redis Cache using Node.js. For another example of using Azure Redis Cache with Node.js, see [Build a Node.js Chat Application with Socket.IO on an Azure Website][].


## Prerequisites

Install [node_redis](https://github.com/mranney/node_redis):

    npm install redis

This tutorial uses [node_redis](https://github.com/mranney/node_redis), but you can use any Node.js client listed at [http://redis.io/clients](http://redis.io/clients).

## Create a Redis cache on Azure

<!-- deleted by customization
In the [Azure Management Portal](https://manage.windowsazure.cn/), click **New**, **DATA SERVICE**, and select **Redis Cache**.

  ![][1]

Enter a DNS hostname. It will have the form `<name>
  .redis.cache.chinacloudapi.cn`. Click **Create**.

  ![][2]


  Once you create the cache, [browse to it](/documentation/articles/cache-configure#configure-redis-cache-settings) to view the cache settings. Click the link under **Keys** and copy the primary key. You need this to authenticate requests.

  ![][4]


  ## Enable the non-SSL endpoint


  Click the link under **Ports**, and click **No** for "Allow access only via SSL". This enables the non-SSL port for the cache. The node_redis client currently does not support SSL.

  ![][3]


  ## Add something to the cache and retrieve it

  var redis = require("redis");

  // Add your cache name and access key.
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

## Enable the non-SSL endpoint

You can use the following PowerShell command to enable the non-SSL endpoint

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true

## Add something to the cache and retrieve it

	var redis = require("redis");

	// Add your cache name and access key.
<!-- keep by customization: end -->
  var client = redis.createClient(6379,'<name>.redis.cache.chinacloudapi.cn', {auth_pass: '<key>' });

	client.set("foo", "bar", function(err, reply) {
	    console.log(reply);
	});

	client.get("foo",  function(err, reply) {
	    console.log(reply);
	});


Output:

	OK
	bar


## Next steps

<!-- deleted by customization
- [Enable cache diagnostics](/documentation/articles/cache-how-to-monitor#enable-cache-diagnostics) so you can [monitor](/documentation/articles/cache-how-to-monitor) the health of your cache.
-->
- Read the official [Redis documentation](http://redis.io/documentation).


<!--Image references-->
[1]: ./media/cache-nodejs-get-started/cache01.png
[2]: ./media/cache-nodejs-get-started/cache02.png
[3]: ./media/cache-nodejs-get-started/cache03.png
[4]: ./media/cache-nodejs-get-started/cache04.png

[Build a Node.js Chat Application with Socket.IO on an Azure Website]: <!-- deleted by customization ../app-service-web/web-sites-nodejs-chat-app-socketio.md --><!-- keep by customization: begin --> /documentation/articles/web-sites-nodejs-chat-app-socketio <!-- keep by customization: end -->
