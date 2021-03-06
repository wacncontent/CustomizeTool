<properties
	pageTitle="Queries in Azure Search | Windows Azure | Hosted cloud search service"
	description="Build a search query in Azure search and use search parameters to filter, sort, and facet search results."
	services="search"
	documentationCenter=""
	authors="HeidiSteen"
	manager="mblythe"
	editor=""
    tags="azure-portal"/>

<tags
	ms.service="search"
	ms.date="11/10/2015"
	wacn.date=""/>

# Queries in Azure Search
> [AZURE.SELECTOR]
- [Overview](/documentation/articles/search-query-overview)
- [Fiddler](/documentation/articles/search-fiddler)
- [.NET](/documentation/articles/search-query-dotnet)
- [REST](/documentation/articles/search-query-rest-api)

Custom solutions using Azure Search for an embedded search experience need to include code that constructs the search query and sends it to a search service for processing.

You can use either the .NET SDK or REST API to write methods for query execution. For preliminary testing or exploration, you can use tools like Fiddler  to send queries to your service.
