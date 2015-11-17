deletion:

deleted:

		preview

reason: ()

deleted:

		preview

reason: ()

deleted:

		Each metric includes two versions. One metric measures performance for the entire cache, and for caches that use [clustering](/documentation/articles/cache-how-to-premium-clustering), a second version of the metric that includes `(Shard 0-9)` in the name measures performance for a single shard in a cache. For example if a cache has 4 shards, `Cache Hits` is the total amount of hits for the entire cache, and `Cache Hits (Shard 3)` is just the hits for that shard of the cache.

reason: ()

deleted:

		## How to monitor a premium cache with clustering
		
		Premium caches that have [clustering](/documentation/articles/cache-how-to-premium-clustering) enabled can have up to 10 shards. Each shard has its own metrics, and these metrics are aggregated to provide metrics for the cache as a whole. Each metric includes two versions. One metric measures performance for the entire cache and a second version of the metric that includes `(Shard 0-9)` in the name measures performance for a single shard in a cache. For example if a cache has 3 shards, `Cache Hits` is the total amount of hits for the entire cache, and `Cache Hits (Shard 2)` is just the hits for that shard of the cache.
		
		Each monitoring chart displays the top level metrics for the cache along with the metrics for each cache shard.
		
		![Monitor][redis-cache-premium-monitor]
		
		Hovering the mouse over the data points displays the details for that point in time. 
		
		![Monitor][redis-cache-premium-point-summary]
		
		The larger values are typically the aggregate values for the cache while the smaller values are the individual metrics for the shard. Note that in this example there are three shards and the cache hits are distributed evenly across the shards.
		
		![Monitor][redis-cache-premium-point-shard]
		
		To see more detail click the chart to view an expanded view on the **Metric** blade.
		
		![Monitor][redis-cache-premium-chart-detail]
		
		By default each chart includes the top-level cache performance counter as well as the performance counters for the individual shards. You can customize these on the **Edit Chart** blade.
		
		![Monitor][redis-cache-premium-edit]
		
		For more information on the available performance counters, see [Available metrics and reporting intervals](#available-metrics-and-reporting-intervals).

reason: ()

deleted:

		[redis-cache-premium-monitor]: ./media/cache-how-to-monitor/redis-cache-premium-monitor.png
		
		[redis-cache-premium-edit]: ./media/cache-how-to-monitor/redis-cache-premium-edit.png
		
		[redis-cache-premium-chart-detail]: ./media/cache-how-to-monitor/redis-cache-premium-chart-detail.png
		
		[redis-cache-premium-point-summary]: ./media/cache-how-to-monitor/redis-cache-premium-point-summary.png
		
		[redis-cache-premium-point-shard]: ./media/cache-how-to-monitor/redis-cache-premium-point-shard.png

reason: ()

replacement:

deleted:

		[browse](/documentation/articles/cache-configure)

replaced by:

		[browse](https://msdn.microsoft.com/zh-cn/library/azure/cbe6d113-7bdc-4664-a59d-ff0df6f4e214#CacheSettings)

reason: ()

deleted:

		preview portal](https://manage.windowsazure.cn)

replaced by:

		Management Portal](https://manage.windowsazure.cn/)

reason: ()

deleted:

		preview portal

replaced by:

		Azure Management Portal

reason: ()

deleted:

		preview portal

replaced by:

		Azure Management Portal

reason: ()

deleted:

		| Used Memory       | The amount of cache memory used for key/value pairs in the cache in MB during the specified reporting interval. This value maps to the Redis INFO `used_memory` command. This does not include metadata or fragmentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
		| Used Memory RSS   | The amount of cache memory used in MB during the specified reporting interval, including fragmentation and metadata. This value maps to the Redis INFO `used_memory_rss` command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

replaced by:

		| Used Memory       | The amount of cache memory used in MB during the specified reporting interval. This value maps to the Redis INFO `used_memory` command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

reason: ()

