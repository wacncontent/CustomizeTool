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

In the [Azure Management Portal](https://manage.windowsazure.cn/), click **New**, **DATA SERVICE**, and select **Redis Cache**.

  ![][1]

Enter a DNS hostname. It will have the form `<name>.redis.cache.chinacloudapi.cn`. Click **Create**.

  ![][2]


  Once you create the cache, [browse to it](/documentation/articles/cache-configure#configure-redis-cache-settings) to view the cache settings. Click the link under **Keys** and copy the primary key. You need this to authenticate requests.

  ![][4]

## Add something to the cache and retrieve it

```js
var redis = require("redis");

// Add your cache name and access key.
var client = redis.createClient(6380,'<name>.redis.cache.chinacloudapi.cn', {auth_pass: '<key>', tls: {servername: '<name>.redis.cache.chinacloudapi.cn'}});

client.set("foo", "bar", function(err, reply) {
  console.log(reply);
});

client.get("foo",  function(err, reply) {
  console.log(reply);
});
```

Output:

	OK
	bar


## Next steps

- [Enable cache diagnostics](/documentation/articles/cache-how-to-monitor#enable-cache-diagnostics) so you can [monitor](/documentation/articles/cache-how-to-monitor) the health of your cache.
- Read the official [Redis documentation](http://redis.io/documentation).


<!--Image references-->
[1]: ./media/cache-nodejs-get-started/cache01.png
[2]: ./media/cache-nodejs-get-started/cache02.png
[3]: ./media/cache-nodejs-get-started/cache03.png
[4]: ./media/cache-nodejs-get-started/cache04.png

[Build a Node.js Chat Application with Socket.IO on an Azure Website]: ../app-service-web/web-sites-nodejs-chat-app-socketio.md
