<properties 
	pageTitle="Provision a Redis Cache | Azure" 
	description="Use Azure Resource Manager template to deploy an Azure Redis Cache." 
	services="app-service" 
	documentationCenter="" 
	authors="steved0x" 
	manager="Erikre" 
	editor=""/>

<tags
	ms.service="cache"
	ms.date="04/22/2016"
	wacn.date=""/>

# Create a Redis Cache using a template

In this topic, you will learn how to create an Azure Resource Manager template that deploys an Azure Redis Cache. You will learn how to define which resources are deployed and
how to define parameters that are specified when the deployment is executed. You can use this template for your own deployments, or customize it to meet your requirements.

For more information about creating templates, see [Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates/).

For the complete template, see [Redis Cache template](https://github.com/Azure/azure-quickstart-templates/blob/master/101-redis-cache/azuredeploy.json).

>[AZURE.NOTE] ARM templates for the new [Premium tier](/documentation/articles/cache-premium-tier-intro/) are available. 
>
>
>To check for the latest templates, see [Azure Quickstart Templates](https://azure.microsoft.com/documentation/templates/) and search for `Redis Cache`.

## What you will deploy

In this template, you will deploy an Azure Redis Cache.

## Parameters

With Azure Resource Manager, you define parameters for values you want to specify when the template is deployed. The template includes a section called Parameters that contains all of the parameter values.
You should define a parameter for those values that will vary based on the project you are deploying or based on the 
environment you are deploying to. Do not define parameters for values that will always stay the same. Each parameter value is used in the template to define the resources that are deploy. 

We will describe each parameter in the template.

[AZURE.INCLUDE [app-service-web-deploy-redis-parameters](../includes/cache-deploy-parameters.md)]

### redisCacheLocation

The location of the Redics Cache. For best perfomance, use the same location as the app to be used with the cache.

    "redisCacheLocation": {
      "type": "string"
    }

### enableNonSslPort

A boolean value that indicates whether to allow access via non-SSL ports.

    "enableNonSslPort": {
      "type": "bool"
    }
    
## Resources to deploy

### Redis Cache

Creates the Azure Redis Cache.

    {
      "apiVersion": "2015-08-01",
      "name": "[parameters('redisCacheName')]",
      "type": "Microsoft.Cache/Redis",
      "location": "[parameters('redisCacheLocation')]",
      "properties": {
        "enableNonSslPort": "[parameters('enableNonSslPort')]",
        "sku": {
          "capacity": "[parameters('redisCacheCapacity')]",
          "family": "[parameters('redisCacheFamily')]",
          "name": "[parameters('redisCacheSKU')]"
        }
      },
        "resources": [
      ]
    }

## Commands to run deployment

[AZURE.INCLUDE [app-service-deploy-commands](../includes/app-service-deploy-commands.md)] 

### PowerShell

    New-AzureRmResourceGroupDeployment -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-redis-cache/azuredeploy.json -ResourceGroupName ExampleDeployGroup -redisCacheName ExampleCache -redisCacheLocation "China North"

### Azure CLI

    azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-redis-cache/azuredeploy.json -g ExampleDeployGroup


