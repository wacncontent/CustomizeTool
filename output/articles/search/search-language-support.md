<properties
   pageTitle="Create an index for documents in multiple languages in Azure Search | Windows Azure | Hosted cloud search service"
   description=" Azure Search supports 56 languages, leveraging language analyzers from Lucene and Natural Language Processing technology from Microsoft."
   services="search"
   documentationCenter=""
   authors="yahnoosh"
   manager="pablocas"
   editor=""/>

<tags
	ms.service="search"
	ms.date="10/19/2015"
	wacn.date=""/>

# Create an index for documents in multiple languages in Azure Search
> [AZURE.SELECTOR]
- [Portal](/documentation/articles/search-language-support)
- [REST](https://msdn.microsoft.com/zh-cn/library/azure/dn879793.aspx)
- [.NET](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.azure.search.models.analyzername.aspx)

Unleashing the power of language analyzers is as easy as setting one property on a searchable field in the index definition. Now you can do this step in the portal.

Below are screenshots of the Azure Management Portal blades for Azure Search that allow users to define an index schema. From this blade, users can create all of the fields and set the analyzer property for each of them.

> [AZURE.NOTE] You can only set a language analyzer during field definition, as in when creating a new index from the ground up, or when adding a new field to an existing index. Make sure you fully specify all attributes, including the analyzer, while creating the field. You won't be able to edit the attributes or change the analyzer type once the field is defined.

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn) and open the service blade of your search service.
2. Click **Add an Index** at the top of the service dashboard to start a new index, or open an existing index to set an analyzer on new fields you're adding to an existing index.
3. The Fields blade appears, giving you options for defining the schema of the index, including the Analyzer tab used for choosing a language analyzer.
4. In Fields, start a field definition by providing a name, choosing the data type, and setting  attributes to mark the field as full text searchable, retrievable in search results, usable in facet navigation structures, sortable, and so forth. 
5. Before moving on to the next field, open the **Analyzer** tab. 
6. Scroll to find the field you are defining. 
7. If you haven't marked the field as search, click the checkbox now to mark it as Searchable.
8. Click the Analyzer area to display the list of available analyzers.
9. Choose the analyzer you want to use.

![][1]
*To select an analyzer, click the Analyzer tab on the Fields blade*

![][2]
*Select one of the supported analyzers for each field*

By default, all searchable fields use the [Standard Lucene analyzer](http://lucene.apache.org/core/4_10_0/analyzers-common/org/apache/lucene/analysis/standard/StandardAnalyzer.html) which is language agnostic. To view the full list of supported analyzers, see [Language Support in Azure Search](https://msdn.microsoft.com/zh-cn/library/azure/dn879793.aspx).

Once the language analyzer is selected for a field, it will be used with each indexing and search request for that field. When a query is issued against multiple fields using different analyzers, the query will be processed independently by the right analyzers for each field.

Many web and mobile applications serve users around the globe using different languages. Itâs possible to define an index for a scenario like this by creating a field for each language supported.

![][3]
*Index definition with a description field for each language supported*

If the language of the agent issuing a query is known, a search request can be scoped to a specific field using the **searchFields** query parameter. The following query will be issued only against the description in Polish:

`https://[service name].search.chinacloudapi.cn/indexes/[index name]/docs?search=darmowy&searchFields=description_pl&api-version=2015-02-28`

Sometimes the language of the agent issuing a query is not known, in which case the query can be issued against all fields simultaneously. If needed, preference for results in a certain language can be defined using [scoring profiles](https://msdn.microsoft.com/zh-cn/library/azure/dn798928.aspx). In the example below, matches found in the description in English will be scored higher relative to matches in Polish and French:

    "scoringProfiles": [
      {
        "name": "englishFirst",
        "text": {
          "weights": { "description_en": 2 }
        }
      }
    ]

`https://[service name].search.chinacloudapi.cn/indexes/[index name]/docs?search=Microsoft&scoringProfile=englishFirst&api-version=2015-02-28`

If you're a .NET developer, note that you can configure language analyzers using the [Azure Search .NET SDK](http://www.nuget.org/packages/Microsoft.Azure.Search/0.13.0-preview). The latest release includes support for the Microsoft language analyzers as well.

<!-- Image References -->
[1]: ./media/search-language-support/AnalyzerTab.png
[2]: ./media/search-language-support/SelectAnalyzer.png
[3]: ./media/search-language-support/IndexDefinition.png