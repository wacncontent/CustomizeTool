<properties
	pageTitle="Create an Azure Search index using .NET | Windows Azure | Hosted cloud search service"
	description="Create an index in code using the Azure Search .NET SDK or library."
	services="search"
	documentationCenter=""
	authors="HeidiSteen"
	manager="mblythe"
	editor=""
    tags="azure-portal"/>

<tags
	ms.service="search"
	ms.date="11/09/2015"
	wacn.date=""/>

# Create an Azure Search index using .NET
> [AZURE.SELECTOR]
- [Overview](/documentation/articles/search-what-is-an-index)
- [Portal](/documentation/articles/search-create-index-portal)
- [.NET](/documentation/articles/search-create-index-dotnet)
- [REST](/documentation/articles/search-create-index-rest-api)

This article shows you how to create an index using the [Azure Search .NET SDK](https://msdn.microsoft.com/zh-cn/library/azure/dn951165.aspx). The content below is a subset of the [How to use Azure Search from a .NET Application](/documentation/articles/search-howto-dotnet-sdk). Refer to the parent article for end-to-end steps.

Prerequisites to creating an index include having previously established a connection to your search service, typically done via a `SearchServiceClient`. A best practice for ensuring a friction-free redeployment is to delete an existing index of the same name, if it already exists. 

Assuming an index named 'hotels', you can construct a method for this as follows:

    private static void DeleteHotelsIndexIfExists(SearchServiceClient serviceClient)
    {
        if (serviceClient.Indexes.Exists("hotels"))
        {
            serviceClient.Indexes.Delete("hotels");
        }
    }

This method uses the given `SearchServiceClient` to check if the index exists, and if so, delete it.

To create a new "hotels" index, construct a method similar to the following:

    private static void CreateHotelsIndex(SearchServiceClient serviceClient)
    {
        var definition = new Index()
        {
            Name = "hotels",
            Fields = new[]
            {
                new Field("hotelId", DataType.String)                       { IsKey = true },
                new Field("hotelName", DataType.String)                     { IsSearchable = true, IsFilterable = true },
                new Field("baseRate", DataType.Double)                      { IsFilterable = true, IsSortable = true },
                new Field("category", DataType.String)                      { IsSearchable = true, IsFilterable = true, IsSortable = true, IsFacetable = true },
                new Field("tags", DataType.Collection(DataType.String))     { IsSearchable = true, IsFilterable = true, IsFacetable = true },
                new Field("parkingIncluded", DataType.Boolean)              { IsFilterable = true, IsFacetable = true },
                new Field("lastRenovationDate", DataType.DateTimeOffset)    { IsFilterable = true, IsSortable = true, IsFacetable = true },
                new Field("rating", DataType.Int32)                         { IsFilterable = true, IsSortable = true, IsFacetable = true },
                new Field("location", DataType.GeographyPoint)              { IsFilterable = true, IsSortable = true }
            }
        };

        serviceClient.Indexes.Create(definition);
    }

This method creates a new `Index` object with a list of `Field` objects that defines the schema of the new index. Each field has a name, data type, and several attributes that define its search behavior. In addition to fields, you can also add scoring profiles, suggesters, or CORS options to the Index (these are omitted from the sample for brevity). You can find more information about the Index object and its constituent parts in the SDK reference on [MSDN](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.models.index_members.aspx), as well as in the [Azure Search REST API reference](https://msdn.microsoft.com/zh-cn/library/azure/dn798935.aspx).