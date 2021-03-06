<properties
	pageTitle="How to use Azure Redis Cache with Node.js | Azure"
	description="Get started with Azure Redis Cache using Node.js and node_redis."
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="douge"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.devlang="nodejs"
	ms.topic="hero-article"
	ms.tgt_pltfrm="cache-redis"
	ms.workload="tbd"
	ms.date="08/16/2016"
	wacn.date=""
	ms.author="sdanie"/>

# How to use Azure Redis Cache with Node.js

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache/)
- [ASP.NET](/documentation/articles/cache-web-app-howto/)
- [Node.js](/documentation/articles/cache-nodejs-get-started/)
- [Java](/documentation/articles/cache-java-get-started/)
- [Python](/documentation/articles/cache-python-get-started/)

Azure Redis Cache gives you access to a secure, dedicated Redis cache, managed by Microsoft. Your cache is accessible from any application within Azure.

This topic shows you how to get started with Azure Redis Cache using Node.js. For another example of using Azure Redis Cache with Node.js, see [Build a Node.js Chat Application with Socket.IO on an Azure Website](/documentation/articles/web-sites-nodejs-chat-app-socketio/).


## Prerequisites

Install [node_redis](https://github.com/mranney/node_redis):

    npm install redis

This tutorial uses [node_redis](https://github.com/mranney/node_redis). For examples of using other Node.js clients, see the individual documentation for the Node.js clients listed at [Node.js Redis clients](http://redis.io/clients#nodejs).

## Create a Redis cache on Azure

[AZURE.INCLUDE [redis-cache-create](../../includes/redis-cache-create.md)]

## Retrieve the host name and access keys

[AZURE.INCLUDE [redis-cache-create](../../includes/redis-cache-access-keys.md)]

## Connect to the cache securely using SSL

The latest builds of [node_redis](https://github.com/mranney/node_redis) provide support for connecting to Azure Redis Cache using SSL. The following example shows how to connect to Azure Redis Cache using the SSL endpoint of 6380. Replace `<name>` with the name of your cache and `<key>` with either your primary or secondary key as described in the previous [Retrieve the host name and access keys](#retrieve-the-host-name-and-access-keys) section.

	 var redis = require("redis");
	
	  // Add your cache name and access key.
	var client = redis.createClient(6380,'<name>.redis.cache.chinacloudapi.cn', {auth_pass: '<key>', tls: {servername: '<name>.redis.cache.chinacloudapi.cn'}});


## Add something to the cache and retrieve it

The following example shows you how to connect to an Azure Redis Cache instance, and store and retrieve an item from the cache. For more examples of using Redis with the [node_redis](https://github.com/mranney/node_redis) client, see [http://redis.js.org/](http://redis.js.org/).

	 var redis = require("redis");
	
	  // Add your cache name and access key.
	var client = redis.createClient(6380,'<name>.redis.cache.chinacloudapi.cn', {auth_pass: '<key>', tls: {servername: '<name>.redis.cache.chinacloudapi.cn'}});
	
	client.set("key1", "value", function(err, reply) {
		    console.log(reply);
		});
	
	client.get("key1",  function(err, reply) {
		    console.log(reply);
		});

Output:

	OK
	value


## Next steps

- [Enable cache diagnostics](/documentation/articles/cache-how-to-monitor/#enable-cache-diagnostics) so you can [monitor](/documentation/articles/cache-how-to-monitor/) the health of your cache.
- Read the official [Redis documentation](http://redis.io/documentation).



