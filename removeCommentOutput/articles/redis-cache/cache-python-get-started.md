<properties
	pageTitle="How to use Azure Redis Cache with Python | Windows Azure"
	description="Get started with Azure Redis Cache using Python"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.date="10/05/2015"
	wacn.date=""/>

# How to use Azure Redis Cache with Python

This topic shows you how to get started with Azure Redis Cache using Python.


## Prerequisites

Install [redis-py](https://github.com/andymccurdy/redis-py).


## Create a Redis cache on Azure

In the [Azure preview portal](https://manage.windowsazure.cn/), click **New**, **DATA SERVICE**, and select **Redis Cache**.

  ![][1]

Enter a DNS hostname. It will have the form `<name>.redis.cache.chinacloudapi.cn`. Click **Create**.

  ![][2]

Once you create the cache, click on it in the preview portal to view the cache settings. You will need:

- **Hostname.** You entered this name when you created the cache.
- **Port.** Click the link under **Ports** to view the ports. Use the SSL port.
- **Access Key.** Click the link under **Keys** and copy the primary key.

## Add something to the cache and retrieve it

    >>> import redis
    >>> r = redis.StrictRedis(host='<name>.redis.cache.chinacloudapi.cn',
          port=6380, db=0, password='<key>', ssl=True)
    >>> r.set('foo', 'bar')
    True
    >>> r.get('foo')
    b'bar'

Replace *&lt;name&gt;* with your cache name and *&lt;key&gt;* with your access key.


<!--Image references-->
[1]: ./media/cache-python-get-started/cache01.png
[2]: ./media/cache-python-get-started/cache02.png