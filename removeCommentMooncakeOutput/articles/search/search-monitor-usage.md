<properties 
   pageTitle="Monitor usage and statistics in an Azure Search service | Windows Azure | Hosted cloud search service" 
   description="Track resource consumption and index size for Azure Search, a hosted cloud search service on Windows Azure." 
   services="search" 
   documentationCenter="" 
   authors="HeidiSteen" 
   manager="mblythe" 
   editor=""
   tags="azure-portal"/>

<tags
	ms.service="search"
	ms.date="11/04/2015"
	wacn.date=""/>

# Monitor usage and statistics in an Azure Search service

Tracking the growth of indexes and document size can help you proactively adjust capacity before hitting the upper limit you've established for your service. 

To monitor resource usage, counts and statistics are easily viewed in the [Azure Management Portal](https://manage.windowsazure.cn), but you can also obtain the information programmatically if you are building a custom service administration tool. This article covers the steps for both techniques.

##View counts and metrics in the portal 

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn). 

2. Open the service dashboard of your Azure Search service. Tiles for the service can be found on the Home page, or you can browse to the service from Browse on the JumpBar. See [Create a service](/documentation/articles/search-create-service-portal) for step-by-step instructions.

The Usage section includes a meter that tells you what portion of available resources are currently in use.

  ![][1]

Recall that the shared service has a maximum of one replica and partition each. Additionally, it can only support 10,000 documents in total or 50 MB of data, whichever comes first.

##Get index statistics using the REST API

Both the Azure Search REST API and the .NET SDK provide programmatic access to service metrics.  If you are using [indexers](https://msdn.microsoft.com/zh-cn/library/azure/dn946891.aspx) to load an index from Azure SQL Database or DocumentDB, an additional API is available to get the numbers you require. 

  + [Get Index Statistics](https://msdn.microsoft.com/zh-cn/library/azure/dn798942.aspx)
  + [Count Documents](https://msdn.microsoft.com/zh-cn/library/azure/dn798924.aspx)
  + [Get Indexer Status](https://msdn.microsoft.com/zh-cn/library/azure/dn946884.aspx)

## Next steps

Review [Limits and capacity](/documentation/articles/search-limits-quotas-capacity) to determine the combination of partitions and replicas you'll need if existing capacity is insufficient. 

Visit [Manage your Search service on Windows Azure](/documentation/articles/search-manage) for more information on service administration.

<!--Image references-->
[1]: ./media/search-monitor-usage/AzureSearch-Monitor1.PNG




 