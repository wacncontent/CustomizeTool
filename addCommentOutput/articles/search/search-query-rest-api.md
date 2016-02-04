<properties
	pageTitle="Build queries in Azure Search using REST calls | Windows Azure | Hosted cloud search service"
	description="Build a search query in Azure search and use search parameters to filter, sort, and facet search result using the .NET library or SDK."
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

#Build queries in Azure Search using REST calls 
> [AZURE.SELECTOR]
- [Overview](/documentation/articles/search-query-overview)
- [Fiddler](/documentation/articles/search-fiddler)
- [Postman](/documentation/articles/search-chrome-postman)
- [.NET](/documentation/articles/search-query-dotnet)
- [REST](/documentation/articles/search-query-rest-api)

This article shows you how to construct a query against an index using the [Azure Search REST API](https://msdn.microsoft.com/zh-cn/library/azure/dn798935.aspx). Some of the content below is from [Search Documents (Azure Search REST API)](https://msdn.microsoft.com/zh-cn/library/azure/dn798927.aspx). Refer to the parent article for more context.

Prerequisites to importing include having an existing index already in place, loaded with documents that provide searchable data.

When using the REST API, queries are based on a GET HTTP request. Code snippets are from the [scoring profiles sample](/documentation/articles/search-get-started-scoring-profiles).

        static JObject ExecuteRequest(string action, string query = "")
        {
            // original:  string url = serviceUrl + indexName + "/" + action + "?" + ApiVersion; 
            string url = serviceUrl + indexName + "/docs?" + action ;
            if (!String.IsNullOrEmpty(query))
            {
                url += query + "&" + ApiVersion;
            }

            string response = ExecuteGetRequest(url);
            return JObject.Parse(response);

        }

        static string ExecuteGetRequest(string requestUri)
        {
            //This will execute a get request and return the response
            using (HttpClient client = new HttpClient())
            {
                client.DefaultRequestHeaders.Add("api-key", primaryKey);
                HttpResponseMessage response = client.GetAsync(requestUri).Result;        // Searches are done over port 80 using Get
                return response.Content.ReadAsStringAsync().Result;
            }

        }