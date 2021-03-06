<properties
   pageTitle="Publish-WebApplicationWebSite (Windows PowerShell script) | Windows Azure"
   description="Learn how to publish a web project to an Azure website. This script creates the required resources in your Azure subscription if they don't exist."
   services="visual-studio-online"
   documentationCenter="na"
   authors="TomArcher"
   manager="douge"
   editor="" />
<tags
	ms.service="multiple"
	ms.date="12/17/2015"
	wacn.date=""/>

# Publish-WebApplicationWebSite (Windows PowerShell script)

##Syntax

Publishes a web project to an Azure website. The script creates the required resources in your Azure subscription if they don't exist.

	Publish-WebApplicationWebSite
	âConfiguration <configuration>
	-SubscriptionName <subscriptionName>
	-WebDeployPackage <packageName>
	-DatabaseServerPassword @{Name = "name"; Password = "password"}
	-SendHostMessagesToOutput
	-Verbose


## Configuration

The path to the JSON configuration file that describes the details of the deployment.

|Parameter|Default value|
|---|---|
|Aliases|none|
|Required?|true|
|Position|named|
|Default value|none|
|Accept pipeline input?|false|
|Accept wildcard characters?|false|

## SubscriptionName

The name of the Azure subscription that you want to create the website in.

|Parameter|Default value|
|---|---|
|Aliases|none|
|Required?|false|
|Position|named|
|Default value|none|
|Accept pipeline input?|false|
|Accept wildcard characters?|false|

## WebDeployPackage

<!-- deleted by customization
The path to the web deployment package to publish to the website. You can create this package by using the Publish Web wizard in Visual Studio. For more information, see [Get started with Azure Cloud Services and ASP.NET](/documentation/articles/vs-azure-tools-publish-webapplicationwebsite-windows-powershell-script/).
-->
<!-- keep by customization: begin -->
The path to the web deployment package to publish to the website. You can create this package by using the Publish Web wizard in Visual Studio. See [How to: Create a Web Deployment Package in Visual Studio](/documentation/articles/vs-azure-tools-publish-webapplicationwebsite-windows-powershell-script/).
<!-- keep by customization: end -->

|Parameter|Default value|
|---|---|
|Aliases|none|
|Required?|false|
|Position|named|
|Default value|none|
|Accept pipeline input?|false|
|Accept wildcard characters?|false|

## DatabaseServerPassword

The username and password for the SQL database in Azure.

|Parameter|Default value|
|---|---|
|Aliases|none|
|Required?|false|
|Position|named|
|Default value|none|
|Accept pipeline input?|false|
|Accept wildcard characters?|false|

## SendHostMessagesToOutput

If true, print messages from the script to the output stream.

|Parameter|Default value|
|---|---|
|Aliases|none|
|Required?|false|
|Position|named|
|Default value|false|
|Accept pipeline input?|false|
|Accept wildcard characters?|false|

## Remarks

For a complete explanation of how to use the script to create Dev and Test environments, see [Using Windows PowerShell Scripts to Publish to Dev and Test <!-- deleted by customization Environments](/documentation/articles/vs-azure-tools-publishing-using-powershell-scripts) --><!-- keep by customization: begin --> Environments](https://msdn.microsoft.com/zh-cn/library/azure/dn642480.aspx) <!-- keep by customization: end -->.

The JSON configuration file specifies the details of what is to be deployed. It includes the information that you specified when you created the project, such as the name and username for the website. It also includes the database to provision, if any. The following code shows an example JSON configuration file:

	{
	    "environmentSettings": {
	        "webSite": {
	            "name": "WebApplication10554",
	            "location": "China North"
	        },
	        "databases": [
	            {
	                "connectionStringName": "DefaultConnection",
	                "databaseName": "WebApplication10554_db",
	                "serverName": "iss00brc88",
	                "user": "sqluser2",
	                "password": "",
	                "edition": "",
	                "size": "",
	                "collation": "",
	                "location": "China North"
	            }
	        ]
	    }
	}

You can edit the JSON configuration file to change what is deployed. A webSite section is required, but the database section is optional.

## Next steps

<!-- deleted by customization
For more information, see [Publish-WebApplicationVM (Windows PowerShell script)](/documentation/articles/vs-azure-tools-publish-webapplicationvm)
-->
<!-- keep by customization: begin -->
[Publish-WebApplicationVM (Windows PowerShell script)](https://msdn.microsoft.com/zh-cn/library/azure/dn689112.aspx)
<!-- keep by customization: end -->
