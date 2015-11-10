<properties
    pageTitle="What happened to my cloud service project? | Windows Azure | Visual Studio connected services"
	description="Describes what happens in a cloud services project after connecting to an Azure storage account using Visual Studio connected services"
    services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags
	ms.service="storage"
	ms.date="09/03/2015"
	wacn.date=""/>
# What happened to my cloud services project (Visual Studio Azure Storage connected service)?

> [AZURE.SELECTOR]
> - [Getting started](/documentation/articles/vs-storage-cloud-services-getting-started-blobs)
> - [What happened](/documentation/articles/vs-storage-cloud-services-what-happened)


<!-- deleted by customization ## --><!-- keep by customization: begin --> ###### <!-- keep by customization: end --> References added

The Azure Storage NuGet package was added to your Visual Studio project.  
This package adds the following .NET references:

<!-- deleted by customization
- **Microsoft.Data.Edm**
- **Microsoft.Data.OData**
- **Microsoft.Data.Services.Client**
- **Microsoft.WindowsAzure.Configuration**
- **Microsoft.WindowsAzure.Storage**
- **Newtonsoft.Json**
- **System.Data**
- **System.Spatial**

## Connection string for Azure Storage added
-->
<!-- keep by customization: begin -->
- `Microsoft.Data.Edm`
- `Microsoft.Data.OData`
- `Microsoft.Data.Services.Client`
- `Microsoft.WindowsAzure.Configuration`
- `Microsoft.WindowsAzure.Storage`
- `Newtonsoft.Json`
- `System.Data`
- `System.Spatial`

######Connection string for Azure Storage added
<!-- keep by customization: end -->
Elements were created with the selected storage account's connection string and key. Modifications were made to the following files:

<!-- deleted by customization
- **ServiceDefinition.csdef**
- **ServiceConfiguration.Cloud.cscfg**
- **ServiceConfiguration.Local.cscfg**
-->
<!-- keep by customization: begin -->
- `ServiceDefinition.csdef`
- `ServiceConfiguration.Cloud.cscfg`
- `ServiceConfiguration.Local.cscfg`
<!-- keep by customization: end -->
