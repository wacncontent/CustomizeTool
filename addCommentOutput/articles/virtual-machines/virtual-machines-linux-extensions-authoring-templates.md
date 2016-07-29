<properties
   pageTitle="Authoring templates with Linux VM extensions | Azure"
   description="Learn about authoring Azure Resource Manager templates with extensions for Linux VMs"
   services="virtual-machines-linux"
   documentationCenter=""
   authors="kundanap"
   manager="timlt"
   editor=""
   tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="03/29/2016"
	wacn.date=""/>

# Authoring Azure Resource Manager templates with Linux VM extensions


[AZURE.INCLUDE [arm-api-version-cli](../includes/arm-api-version-cli.md)]

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the Resource Manager deployment model, which Azure recommends for most new deployments instead of the classic deployment model.
 


[AZURE.INCLUDE [virtual-machines-common-extensions-authoring-templates](../includes/virtual-machines-common-extensions-authoring-templates.md)]

From Azure CLI, run the following commnad:

      Azure VM extension list

This command returns the publisher name, extension name and version as following:

      Publisher                   : Microsoft.Azure.Extensions  
      ExtensionName               : DockerExtension
      Version                     : 1.0

These three properties map to "publisher", "type", and "typeHandlerVersion" respectively in the above template snippet.

>[AZURE.NOTE]It's always recommended to use the latest extension version to get the most updated functionality.

## Identifying the schema for the extension configuration parameters

The next step with authoring an extension template is to identify the format for providing configuration parameters. Each extension supports its own set of parameters.

To look at sample configurations for Linux extensions, click the documentation for see [Linux eExtensions samples](/documentation/articles/virtual-machines-linux-extensions-configuration-samples/).

Please refer to the following to get a fully complete template with VM Extensions.

[Custom script extension on a Linux VM](https://github.com/Azure/azure-quickstart-templates/blob/b1908e74259da56a92800cace97350af1f1fc32b/mongodb-on-ubuntu/azuredeploy.json/)

After authoring the template, you can deploy it using the Azure CLI.
