<properties 
	pageTitle="Whatâs new in the latest update to Azure Search | Windows Azure | Hosted cloud search service" 
	description="Release notes for Azure Search describing the latest updates to the service" 
	services="search" 
	documentationCenter="" 
	authors="HeidiSteen" 
	manager="mblythe" 
	editor=""/>

<tags
	ms.service="search"
	ms.date="11/04/2015"
	wacn.date=""/>

<!-- deleted by customization #Whatâs --><!-- keep by customization: begin --> #What’s <!-- keep by customization: end --> new in the latest update to Azure Search#

Azure Search <!-- deleted by customization is cloud hosted search service on Windows Azure. It --> is generally available, offering a 99.9% availability service-level agreement (SLA) for supported configurations of the [2015-02-28 version of the <!-- deleted by customization API](https://msdn.microsoft.com/zh-cn/library/azure/dn798935.aspx) --><!-- keep by customization: begin --> API](https://msdn.microsoft.com/library/azure/dn798935.aspx) <!-- keep by customization: end -->.

##How features are versioned and rolled out

Features are released separately or jointly through the [REST <!-- deleted by customization API](https://msdn.microsoft.com/zh-cn/library/azure/dn798935.aspx) --><!-- keep by customization: begin --> API](https://msdn.microsoft.com/library/azure/dn798935.aspx) <!-- keep by customization: end -->, [.NET SDK](http://go.microsoft.com/fwlink/?LinkId=528216), or the service dashboard in the [Azure <!-- deleted by customization Management Portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> portal](https://portal.azure.com) <!-- keep by customization: end -->.

Both the .NET library and REST APIs have multiple versions. Older APIs remain operational as we roll out new features. You can visit [Search service <!-- deleted by customization versioning](https://msdn.microsoft.com/zh-cn/library/azure/dn864560.aspx) --><!-- keep by customization: begin --> versioning](https://msdn.microsoft.com/library/azure/dn864560.aspx) <!-- keep by customization: end --> to learn more about our versioning policy.


##Api-version 2015-02-28-Preview
**Re-released: 2015 September**

This version adds new [Lucene query syntax <!-- deleted by customization support](https://msdn.microsoft.com/zh-cn/library/azure/mt589323.aspx) --><!-- keep by customization: begin --> support](https://msdn.microsoft.com/library/azure/mt589323.aspx) <!-- keep by customization: end --> that can be used against the [preview version of the Azure Search Service REST <!-- deleted by customization API](/documentation/articles/search-api-2015-02-28-preview) --><!-- keep by customization: begin --> API](search-api-2015-02-28-preview.md) <!-- keep by customization: end -->. To use the new syntax, you must specify the `queryType` in a Search Documents operation.

Additionally, both of the following features are transitioned out of preview, and are now part of the official API on MSDN:
<!-- deleted by customization
- [Natural language processors](/documentation/articles/search-language-support)
-->
<!-- keep by customization: begin -->
- Natural language processors
<!-- keep by customization: end -->
- POST in search, suggestions, and lookup queries

##.NET SDK 0.10.0-preview
**Released: 2015 August**

This is the second iteration of the .NET client library, Microsoft.Azure.Search.dll. This version adds support for creating, managing, and using Indexers via .NET classes. Additionally, for Azure SQL Indexers, there is new support for indexing geography points.

<!-- deleted by customization
- [Indexers Class](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.models.indexer.aspx)
- [DataSource Class](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.models.datasource.aspx)
-->
<!-- keep by customization: begin -->
- [Indexers Class](https://msdn.microsoft.com/library/azure/microsoft.azure.search.models.indexer.aspx)
- [DataSource Class](https://msdn.microsoft.com/library/azure/microsoft.azure.search.models.datasource.aspx)
<!-- keep by customization: end -->

##.NET SDK 0.9.6-preview
**Released: 2015 March 5**

This is the first public release of the .NET SDK for Azure Search. It includes a client library, Microsoft.Azure.Search.dll, with two namespaces:

<!-- deleted by customization
- [Microsoft.Azure.Search](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.aspx)
- [Microsoft.Azure.Search.Models](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.models.aspx)
-->
<!-- keep by customization: begin -->
- [Microsoft.Azure.Search](https://msdn.microsoft.com/library/azure/microsoft.azure.search.aspx)
- [Microsoft.Azure.Search.Models](https://msdn.microsoft.com/library/azure/microsoft.azure.search.models.aspx)
<!-- keep by customization: end -->

Excludes:

- [Indexers](http://go.microsoft.com/fwlink/p/?LinkId=528173) (this feature is no longer excluded in the 0.10.0-preview version)
<!-- deleted by customization
- [Management REST API](https://msdn.microsoft.com/zh-cn/library/azure/dn832684.aspx)
- [2015-02-28-Preview](/documentation/articles/search-api-2015-02-28-Preview) features (currently, preview-only features consist of Microsoft natural language processors and `moreLikeThis`).
-->
<!-- keep by customization: begin -->
- [Management REST API](https://msdn.microsoft.com/library/azure/dn832684.aspx)
- [2015-02-28-Preview](search-api-2015-02-28-Preview.md) features (currently, preview-only features consist of Microsoft natural language processors and `moreLikeThis`).
<!-- keep by customization: end -->

Visit [How to use Azure Search in .NET](http://go.microsoft.com/fwlink/p/?LinkId=528088) for guidance on installation and usage of the SDK.

##Api-version 2015-02-28-Preview
**Released: 2015 April 22**

- Indexers now support fieldMapping constructs that provide field assignments when actual field names are different between the external database and the Azure Search index. See <!-- deleted by customization [Indexers](/documentation/articles/search-api-indexers-2015-02-28-Preview) --><!-- keep by customization: begin --> [Indexers](search-api-indexers-2015-02-28-Preview.md) <!-- keep by customization: end --> for the `2015-02-28-preview` version of the indexers documentation..

- Also in this preview update, indexers now support field type transformations so that you can map a string field in a SQL table to a string collection field in a search index, assuming the source field represents a JSON array.

**Released: 2015 March 5**

- [Microsoft natural language <!-- deleted by customization processors](/documentation/articles/search-api-2015-02-28-Preview) --><!-- keep by customization: begin --> processors](search-api-2015-02-28-Preview.md) <!-- keep by customization: end --> bring support for more languages and expansive stemming for all the languages supported by Office and Bing.

- <!-- deleted by customization [moreLikeThis=](/documentation/articles/search-api-2015-02-28-Preview) --><!-- keep by customization: begin --> [moreLikeThis=](search-api-2015-02-28-Preview.md) <!-- keep by customization: end --> is a search parameter, mutually exclusive of `search=`, that triggers an alternate query execution path. Instead of full-text search of `search=` based on a search term input, `moreLikeThis=` finds documents that are similar to a given document by comparing their searchable fields.

##Api-version 2015-02-28
**Released: 2015 March 5**

- [Indexers](http://go.microsoft.com/fwlink/p/?LinkID=528210) is a new feature that vastly simplifies indexing from data sources on Azure SQL Database, Azure DocumentDB, and SQL Server on Azure VMs.

- <!-- deleted by customization [Suggesters](https://msdn.microsoft.com/zh-cn/library/azure/dn798936.aspx) --><!-- keep by customization: begin --> [Suggesters](https://msdn.microsoft.com/library/azure/dn798936.aspx) <!-- keep by customization: end --> replaces the more limited, type-ahead query support of the previous implementation (it only matched on prefixes) by adding support for infix matching. This implementation can find matches anywhere in a term, and also supports fuzzy matching.

- [Tag boosting](http://go.microsoft.com/fwlink/p/?LinkId=528212) enables a new scenario for scoring profiles. In particular, it leverages persisted data (such as shopping preferences) so that you can boost search results for individual users, based on personalized information. 

Visit [Azure Search is now Generally Available](http://go.microsoft.com/fwlink/p/?LinkId=528211) for the service announcement on the Azure blog that discusses all of these features.

##Api-version 2014-10-20-Preview
**Released: 2014 November, 2015 January**

- [Lucene language <!-- deleted by customization analyzers](/documentation/articles/search-api-2014-10-20-preview) --><!-- keep by customization: begin --> analyzers](search-api-2014-10-20-preview.md) <!-- keep by customization: end --> was added to provide multi-lingual support for the custom language analyzers distributed with Lucene.

- Tool support was introduced for building indexes, including scoring profiles, in the [Azure management <!-- deleted by customization portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> portal](https://portal.azure.com) <!-- keep by customization: end -->.

##Api-version 2014-07-31-Preview
**Released: 2014 August 21**

This version was the public preview release for Azure Search, providing the following core features:

- REST API for index and document operations. The majority of this API version is intact in 2015-02-28. The documentation for version `2014-07-31-Preview` can be found at [Azure Search Service REST API Version <!-- deleted by customization 2014-07-31](/documentation/articles/search-api-2014-07-31-preview) --><!-- keep by customization: begin --> 2014-07-31](search-api-2014-07-31-preview.md) <!-- keep by customization: end -->.

- Scoring profiles for tuning search results. A scoring profile adds criteria used to compute search scores. The documentation for this feature can be found at [Azure Search Service Scoring Profiles REST API Version <!-- deleted by customization 2014-07-31](/documentation/articles/search-api-scoring-profiles-2014-07-31-preview) --><!-- keep by customization: begin --> 2014-07-31](search-api-scoring-profiles-2014-07-31-preview.md) <!-- keep by customization: end -->.

- Geospatial support has been available from the beginning, provided through the `Edm.GeographyPoint` data type that has been part of Azure Search since its inception.

- Provisioning in the preview version of the [Azure management <!-- deleted by customization portal](https://manage.windowsazure.cn --><!-- keep by customization: begin --> portal](https://portal.azure.com <!-- keep by customization: end --> ). Azure Search was one of the few services that has only been available in the new portal.

##Management api-version 2015-08-19
**Released: 2015 September 11**

[Management REST <!-- deleted by customization API](https://msdn.microsoft.com/zh-cn/library/azure/dn832684.aspx) --><!-- keep by customization: begin --> API](https://msdn.microsoft.com/library/azure/dn832684.aspx) <!-- keep by customization: end --> includes the following updates.

- checkNameAvailability checks whether a given service name is already in use.
- Replica range was previously 1-6 and is now 1-12.
- SKU property was moved from the property bag to the top level of the service payload.
- Response body of the Create Search Service operation was updated to accommodate the relocation of the SKU setting.

##Management api-version 2015-02-28
**Released: 2015 March 5**

[Management REST <!-- deleted by customization API](/documentation/articles/search-management-api-2014-02-28) --><!-- keep by customization: begin --> API](search-management-api-2014-02-28.md) <!-- keep by customization: end --> marks the first version of the management API belonging to the generally available release of Azure Search. There are no feature differences between the earlier preview and this one.

##Management api-version 2014-07-31-Preview
**Released: 2014 October**

The preview release of [Management REST <!-- deleted by customization API](/documentation/articles/search-management-api-2014-07-31-preview) --><!-- keep by customization: begin --> API](search-management-api-2014-07-31-preview.md) <!-- keep by customization: end --> was added to support service administration programmatically. It is versioned independently of the service REST API.


 