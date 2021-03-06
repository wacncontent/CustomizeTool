<properties
   pageTitle="Azure Resource Manager Advanced Template Operations"
   description="Describes how to use nested templates and the copy operation in an Azure Resource Manager template when deploying apps to Azure."
   services="na"
   documentationCenter="na"
   authors="tfitzmac"
   manager="wpickett"
   editor=""/>

<tags
   ms.service="na"
   ms.date="04/28/2015"
   wacn.date=""/>

# Advanced Template Operations

This topic describes the copy operation and nested templates which you can use to perform more advanced tasks when deploying resources to Azure.

## copy

Enables you to use iterate through an array and use each element when deploying a resource.

The following example deploys three web sites named examplecopy-Contoso, examplecopy-Fabrikam, examplecopy-Coho.

    "parameters": {
      "org": {
         "type": "array",
             "defaultValue": [
             "Contoso",
             "Fabrikam",
             "Coho"
          ]
      },
      "count": {
         "type": "int",
         "defaultValue": 3
      }
    },
    "resources": [
      {
          "name": "[concat('examplecopy-', parameters('org')[copyIndex()])]",
          "type": "Microsoft.Web/sites",
          "location": "China East",
          "apiVersion": "2014-06-01",
          "copy": {
             "name": "websitescopy",
             "count": "[parameters('count')]"
          },
          "properties": {}
      }
    ]

## Nested template

At times, you may need to merge two templates together, or you may need to launch a child template from a parent. You can accomplish this through the use of a deployment resource within the master template to deploy a child template. You provide the URI of the nested template, as shown below.

    "variables": {"templatelink":"https://www.contoso.com/ArmTemplates/newStorageAccount.json"},
    "resources": [
      {
         "apiVersion": "2015-01-01",
         "name": "nestedTemplate",
         "type": "Microsoft.Resources/deployments",
         "properties": {
           "mode": "incremental",
           "templateLink": {"uri":"[variables('templatelink')]","contentVersion":"1.0.0.0"},
           "parameters": {
              "StorageAccountName":{"value":"[parameters('StorageAccountName')]"}
           }
         }
      }
    ]

## Next Steps
- [Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates)
- [Azure Resource Manager Template Functions](/documentation/articles/resource-group-template-functions)
- [Deploy an application with Azure Resource Manager Template](/documentation/articles/resource-group-template-deploy)
- [Azure Resource Manager Overview](/documentation/articles/resource-group-overview)
