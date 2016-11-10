<properties
	pageTitle="Set up Key Vault for virtual machines in Azure Resource Manager | Azure"
	description="How to set up Key Vault for use with an Azure Resource Manager virtual machine."
	services="virtual-machines-windows"
	documentationCenter=""
	authors="singhkays"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-windows"
	ms.workload="infrastructure-services"
	ms.tgt_pltfrm="vm-windows"
	ms.devlang="na"
	ms.topic="article"
	ms.date="05/31/2016"
	wacn.date=""
	ms.author="singhkay"/>

# Set up Key Vault for virtual machines in Azure Resource Manager

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-rm-include.md)] classic deployment model

In Azure Resource Manager stack, secrets/certificates are modeled as resources that are provided by the resource provider of Key Vault. To learn more about Key Vault, see [What is Azure Key Vault?](/documentation/articles/key-vault-whatis/)

>[AZURE.NOTE] 
>
>1. In order for Key Vault to be used with Azure Resource Manager virtual machines, the **EnabledForDeployment** property on Key Vault must be set to true. You can do this in various clients.
>
>2. The Key Vault needs to be created in the same subscription and location as the Virtual Machine.

## Use PowerShell to set up Key Vault
To create a key vault by using PowerShell, see [Get started with Azure Key Vault](/documentation/articles/key-vault-get-started/#vault).

For new key vaults, you can use this PowerShell cmdlet:

	New-AzureRmKeyVault -VaultName 'ContosoKeyVault' -ResourceGroupName 'ContosoResourceGroup' -Location 'China East' -EnabledForDeployment

For existing key vaults, you can use this PowerShell cmdlet:

	Set-AzureRmKeyVaultAccessPolicy -VaultName 'ContosoKeyVault' -EnabledForDeployment

## Us CLI to set up Key Vault
To create a key vault by using the command-line interface (CLI), see [Manage Key Vault using CLI](/documentation/articles/key-vault-manage-with-cli/#create-a-key-vault).

For CLI, you have to create the key vault before you assign the deployment policy. You can do this by using the following command:

	azure keyvault set-policy ContosoKeyVault -enabled-for-deployment true

## Use templates to set up Key Vault
While you use a template, you need to set the `enabledForDeployment` property to `true` for the Key Vault resource.

	{
      "type": "Microsoft.KeyVault/vaults",
      "name": "ContosoKeyVault",
      "apiVersion": "2015-06-01",
      "location": "<location-of-key-vault>",
      "properties": {
        "enabledForDeployment": "true",
        ....
        ....
      }
    }

For other options that you can configure when you create a key vault by using templates, see [Create a key vault](https://github.com/Azure/azure-quickstart-templates/tree/master/101-key-vault-create/).