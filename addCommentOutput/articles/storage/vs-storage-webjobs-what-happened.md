<properties
	pageTitle="What happened to my WebJob project (Visual Studio Azure Storage connected service)? | Windows Azure"
	description="Describes what happened in a Azure WebJob project after connecting to a storage account using Visual Studio connected services" 
	services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags
	ms.service="storage"
	ms.date="09/03/2015"
	wacn.date=""/>
# What happened to my WebJob project (Visual Studio Azure Storage connected service)?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-storage-webjobs-getting-started-blobs)
> - [What Happened](/documentation/articles/vs-storage-webjobs-what-happened)


<!-- deleted by customization ## --><!-- keep by customization: begin --> ##### <!-- keep by customization: end --> References Added

The Azure Storage NuGet package was added to or updated in your Visual Studio project.  
This package adds the following .NET references:

<!-- deleted by customization
- **Microsoft.Data.Edm**
- **Microsoft.Data.OData**
- **Microsoft.Data.Services.Client**
- **Microsoft.WindowsAzure.ConfigurationManager**
- **Microsoft.WindowsAzure.Storage**
- **Newtonsoft.Json**
- **System.Data**
- **System.Spatial**
-->
<!-- keep by customization: begin -->
- `Microsoft.Data.Edm`
- `Microsoft.Data.OData`
- `Microsoft.Data.Services.Client`
- `Microsoft.WindowsAzure.ConfigurationManager`
- `Microsoft.WindowsAzure.Storage`
- `Newtonsoft.Json`
- `System.Data`
- `System.Spatial`
<!-- keep by customization: end -->

## Connection string for Azure Storage added
In the App.config file of your project, the **AzureWebJobsStorage** and **AzureWebJobsDashboard** entries were updated with the selected storage account's connection string and key.

For more information, see [Azure WebJobs Recommended <!-- deleted by customization Resources](/documentation/articles/websites-webjobs-resources/) --><!-- keep by customization: begin --> Resources](http://www.windowsazure.cn/documentation/articles/websites-webjobs-resources/) <!-- keep by customization: end -->.