<properties 
	pageTitle="Create NoSQL database account - Trial | Windows Azure" 
	description="Learn how to create database accounts using the online database creator for Azure DocumentDB, a managed NoSQL document database for JSON. Get a trial today."
	keywords="trial, online database creator, create a database, create database, documentdb, azure, Microsoft azure"
	services="documentdb" 
	documentationCenter="" 
	authors="mimig1" 
	manager="jhubbard" 
	editor="monicar"/>

<tags
	ms.service="documentdb"
	ms.date="12/17/2015"
	wacn.date=""/>
<!
# Create a DocumentDB database account using the Azure Management Portal

> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/documentdb-create-account)
- [Azure CLI and ARM](/documentation/articles/documentdb-automation-resource-manager-cli)

To use Windows Azure DocumentDB, you must create a DocumentDB database account using either the Azure Management Portal, Azure Resource Manager templates, or Azure command-line interface (CLI). This article shows how to create a database account using the Azure Management Portal. To create an account using Azure Resource Manager or Azure CLI, see [Automate DocumentDB database account creation](/documentation/articles/documentdb-automation-resource-manager-cli). 

Are you new to DocumentDB? Watch [this](http://azure.microsoft.com/documentation/videos/create-documentdb-on-azure/) four minute video by Scott Hanselman to see how to complete the most common tasks in the online portal.

[AZURE.INCLUDE [documentdb-create-dbaccount](../includes/documentdb-create-dbaccount.md)]

## Next steps

Now that you have a DocumentDB account, the next step is to create a DocumentDB database. You can create a database by using one of the following:

- The C# .NET samples in the [DatabaseManagement](https://github.com/Azure/azure-documentdb-net/tree/master/samples/code-samples/DatabaseManagement) project of the [azure-documentdb-net](https://github.com/Azure/azure-documentdb-net/tree/master/samples/code-samples) repository on GitHub.
- The Azure Management Portal, as described in [Create a DocumentDB database using the Azure Management Portal](/documentation/articles/documentdb-create-database).
- The all-inclusive tutorials: [.NET](/documentation/articles/documentdb-get-started), [.NET MVC](/documentation/articles/documentdb-dotnet-application), [Java](/documentation/articles/documentdb-java-application), [Node.js](/documentation/articles/documentdb-nodejs-application), or [Python](/documentation/articles/documentdb-python-application).
- The [DocumentDB SDKs](/documentation/articles/documentdb-sdk-dotnet). DocumentDB has .NET, Java, Python, Node.js, and JavaScript API SDKs. 


After creating your database, you need to [add one or more collections](/documentation/articles/documentdb-create-collection) to the database, then [add documents](/documentation/articles/documentdb-view-json-document-explorer) to the collections. 

After you have documents in a collection, you can use [DocumentDB SQL](/documentation/articles/documentdb-sql-query) to [execute queries](/documentation/articles/documentdb-sql-query#executing-queries) against your documents by using the [Query Explorer](/documentation/articles/documentdb-query-collections-query-explorer) in the Portal, the [REST API](https://msdn.microsoft.com/zh-cn/library/azure/dn781481.aspx), or one of the [SDKs](/documentation/articles/documentdb-sdk-dotnet).

To learn more about DocumentDB, explore these resources:

-	[Learning path for DocumentDB](https://azure.microsoft.com/documentation/learning-paths/documentdb/)
-	[DocumentDB resource model and concepts](/documentation/articles/documentdb-resources)

 



# Create a DocumentDB database account using the Azure preview portal

To use Microsoft Azure DocumentDB, you must create a DocumentDB database account by using the Azure preview portal. 

Are you new to DocumentDB? Watch [this](http://azure.microsoft.com/documentation/videos/create-documentdb-on-azure/) four minute video by Scott Hanselman to see how to complete the most common tasks in the online portal.

[AZURE.INCLUDE [documentdb-create-dbaccount](../../includes/documentdb-create-dbaccount.md)]

## Next steps

Now that you have a DocumentDB account, the next step is to create a DocumentDB database. You can create a database by using one of the following:

- The C# .NET samples in the [DatabaseManagement](https://github.com/Azure/azure-documentdb-net/tree/master/samples/code-samples/DatabaseManagement) project of the [azure-documentdb-net](https://github.com/Azure/azure-documentdb-net/tree/master/samples/code-samples) repository on GitHub.
- The preview portal, as described in [Create a DocumentDB database using the Azure preview portal](documentdb-create-database.md).
- The all-inclusive tutorials: [.NET](documentdb-get-started.md), [.NET MVC](documentdb-dotnet-application.md), [Java](documentdb-java-application.md), [Node.js](documentdb-nodejs-application.md), or [Python](documentdb-python-application.md).
- The [DocumentDB SDKs](https://msdn.microsoft.com/library/azure/dn781482.aspx). DocumentDB has .NET, Java, Python, Node.js, and JavaScript API SDKs. 


After creating your database, you need to [add one or more collections](documentdb-create-collection.md) to the database, then [add documents](documentdb-view-json-document-explorer.md) to the collections. 

After you have documents in a collection, you can use [DocumentDB SQL](documentdb-sql-query.md) to [execute queries](documentdb-sql-query.md#executing-queries) against your documents by using the [Query Explorer](documentdb-query-collections-query-explorer.md) in the preview portal, the [REST API](https://msdn.microsoft.com/library/azure/dn781481.aspx), or one of the [SDKs](https://msdn.microsoft.com/library/azure/dn781482.aspx).

To learn more about DocumentDB, explore these resources:

-	[Learning path for DocumentDB](https://azure.microsoft.com/documentation/learning-paths/documentdb/)
-	[DocumentDB resource model and concepts](documentdb-resources.md)

 


