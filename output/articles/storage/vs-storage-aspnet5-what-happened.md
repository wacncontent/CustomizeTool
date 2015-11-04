<properties
	pageTitle="What happened to my ASP.NET 5 project (Visual Studio connected services) | Windows Azure Storage"
	description="Describes what happens after connecting to an Azure storage account in a Visual Studio ASP.NET 5 project using Visual Studio connected services"
	services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags
	ms.service="storage"
	ms.date="09/03/2015"
	wacn.date=""/>

# What happened to my ASP.NET 5 project (Visual Studio Azure Storage connected services)?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-storage-aspnet5-getting-started-blobs)
> - [What Happened](/documentation/articles/vs-storage-aspnet5-what-happened)

> [AZURE.SELECTOR]
> - [Blobs](/documentation/articles/vs-storage-aspnet5-getting-started-blobs)
> - [Queues](/documentation/articles/vs-storage-aspnet5-getting-started-queues)
> - [Tables](/documentation/articles/vs-storage-aspnet5-getting-started-tables)

## References added

The Azure Storage NuGet package was added to your Visual Studio project.  
This package adds the following .NET references:

- **Microsoft.Data.Edm**
- **Microsoft.Data.OData**
- **Microsoft.Data.Services.Client**
- **Microsoft.WindowsAzure.Configuration**
- **Microsoft.WindowsAzure.Storage**
- **Newtonsoft.Json**
- **System.Data**
- **System.Spatial**

Also, the NuGet package **Microsoft.Framework.Configuration.Json** was added.

## Connection string for Azure Storage added
In the config.json file of your project, an element was created with the selected storage account's connection string and key.

For more information, see [ASP.NET 5](http://www.asp.net/vnext).
