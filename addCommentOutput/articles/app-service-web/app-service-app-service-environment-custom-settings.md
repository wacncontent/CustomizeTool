<!-- not suitable for Mooncake -->

<properties
	pageTitle="Custom settings for Azure Environments"
	description="Custom configuration settings for Azure Environments"
	services="app-service"
	documentationCenter=""
	authors="stefsch"
	manager="nirma"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="06/01/2016"
	wacn.date=""/>

# Custom configuration settings for Azure Environments

## Overview ##
Because Azure Environments are isolated to a single customer, there are certain configuration settings that can be applied exclusively to Azure Environments. This article documents the various specific customizations that are available for Azure Environments.

You can store Azure Environment customizations by using an array in the new **clusterSettings** attribute. This attribute is found in the "Properties" dictionary of the *hostingEnvironments* Azure Resource Manager entity.

The following abbreviated Resource Manager template snippet shows the **clusterSettings** attribute:


    "resources": [
    {
       "apiVersion": "2015-08-01",
       "type": "Microsoft.Web/hostingEnvironments",
       "name": ...,
       "location": ...,
       "properties": {
          "clusterSettings": [
             {
                 "name": "nameOfCustomSetting",
                 "value": "valueOfCustomSetting"
             }
          ],
          "workerPools": [ ...],
          etc...
       }
    }

The **clusterSettings** attribute can be included in a Resource Manager template to update the Azure Environment.

## Use Azure Resource Explorer to update an Azure Environment
Alternatively, you can update the Azure Environment by using [Azure Resource Explorer](https://resources.azure.com).  

1. In Resource Explorer, go to the node for the Azure Environment (**subscriptions** > **resourceGroups** > **providers** > **Micrososft.Web** > **hostingEnvironments**). Then click the specific Azure Environment that you want to update.

2. In the right pane, click **Read/Write** in the upper toolbar to allow interactive editing in Resource Explorer.  

3. Click the blue **Edit** button to make the Resource Manager template editable.

4. Scroll to the bottom of the right pane. The **clusterSettings** attribute is at the very bottom, where you can enter or update its value.

5. Type (or copy and paste) the array of configuration values you want in the **clusterSettings** attribute.  

6. Click the green **PUT** button that's located at the top of the right pane to commit the change to the Azure Environment.

However you submit the change, it takes roughly 30 minutes multiplied by the number of front ends in the Azure Environment for the change to take effect.
For example, if an Azure Environment has four front ends, it will take roughly two hours for the configuration update to finish. While the configuration change is being rolled out, no other scaling operations or configuration change operations can take place in the Azure Environment.

## Disable TLS 1.0 ##
A recurring question from customers, especially customers who are dealing with PCI compliance audits, is how to explicitly disable TLS 1.0 for their apps.

TLS 1.0 can be disabled through the following **clusterSettings** entry:

        "clusterSettings": [
            {
                "name": "DisableTls1.0",
                "value": "1"
            }
        ],

## Change TLS cipher suite order ##
Another question from customers is if they can modify the list of ciphers negotiated by their server and this can be achieved by modifying the **clusterSettings** as shown below. The list of cipher suites available can be retrieved from [this MSDN article](https://msdn.microsoft.com/zh-cn/library/windows/desktop/aa374757(v=vs.85).aspx).

        "clusterSettings": [
            {
                "name": "FrontEndSSLCipherSuiteOrder",
                "value": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384_P256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P256"
            }
        ],

> [AZURE.WARNING]  If incorrect values are set for the cipher suite that SChannel cannot understand, all TLS communication to your server might stop functioning. In such a case, you will need to remove the *FrontEndSSLCipherSuiteOrder* entry from **clusterSettings** and submit the updated ARM template to revert back to the default cipher suite settings.  Please use this functionality with caution.

## Get started
The Azure Quickstart Resource Manager template site includes a template with the base definition for [creating an Azure Environment](https://azure.microsoft.com/documentation/templates/201-web-app-ase-create/).


<!-- LINKS -->

<!-- IMAGES -->
