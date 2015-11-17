deletion:

deleted:

		>[AZURE.NOTE] The Azure Redis Cache Premium tier is currently in preview. During the preview period, premium features can only be configured during the cache creation process. For more information on using premium cache features, see [How to configure persistence for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-persistence), [How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering), and [How to configure Virtual Network support for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-vnet).

reason: ()

deleted:

		and Premium

reason: ()

deleted:

		and Premium

reason: ()

deleted:

		preview

reason: ()

deleted:

		preview

reason: ()

deleted:

		preview

reason: ()

deleted:

		-	Premium caches
			-	P1 (6 GB - 60 GB) - up to 7,500 connections
			-	P2 (13 GB - 130 GB) - up to 15,000 connections
			-	P3 (26 GB - 260 GB) - up to 30,000 connections
			-	P4 (53 GB - 530 GB) - up to 40,000 connections

reason: ()

replacement:

deleted:

		Caches can be accessed in the [Azure preview portal](https://manage.windowsazure.cn) using the **Browse** blade.
		
		![Azure Redis Cache Browse Blade](./media/cache-configure/IC796920.png)

replaced by:

		Caches can be accessed in the [Windows Azure Management Portal](http://manage.windowsazure.cn/) using the **Browse** blade.
		
		![Azure Redis Cache Browse Blade](./media/cache-configure/IC796920.png)

reason: ()

deleted:

		portal](/documentation/articles/role-based-access-control-configure/)

replaced by:

		portal](/documentation/articles/role-based-access-control-configure)

reason: ()

deleted:

		-	Basic and Standard caches
			-	C0 (250 MB) cache - up to 256 connections

replaced by:

		-	C0 (250 MB) cache - up to 256 connections

reason: ()

deleted:

		preview portal

replaced by:

		Azure Management Portal

reason: ()

deleted:

		You can securely issue commands to your Azure Redis Cache instances using the **Redis Console**, which is available for Standard and Premium caches.
		
		>[AZURE.IMPORTANT] The Redis Console does not work with VNET or clustering. 
		>
		>-	[VNET](/documentation/articles/cache-how-to-premium-vnet) - When your cache is part of a VNET, only clients in the VNET can access the cache. Because the Redis Console uses the redis-cli.exe client hosted on VMs that are not part of your VNET, it can't connect to your cache.
		>-	[Clustering](/documentation/articles/cache-how-to-premium-clustering) - The Redis Console uses the redis-cli.exe client which does not support clustering at this time. The redis-cli utility in the [unstable](http://redis.io/download) branch of the Redis repository at GitHub implements basic support when started with the `-c` switch. For more information see [Playing with the cluster](http://redis.io/topics/cluster-tutorial#playing-with-the-cluster) on [http://redis.io](http://redis.io) in the [Redis cluster tutorial](http://redis.io/topics/cluster-tutorial).
		
		To access the Redis Console, click **Console** from the **Redis Cache** blade.
		
		![Redis console](./media/cache-configure/redis-console-menu.png)

replaced by:

		You can securely issue commands to your Azure Redis Cache instances using the **Redis Console**, which is available for Standard caches. To access the Redis Console, click **Console** from the **Redis Cache** blade.
		
		![Redis console](./media/cache-configure/redis-console-menu.png)
		
		>[AZURE.IMPORTANT] The Redis Console is only available for Standard caches.

reason: ()

