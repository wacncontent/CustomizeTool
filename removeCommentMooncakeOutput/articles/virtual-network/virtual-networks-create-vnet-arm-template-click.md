<!-- Ibiza portal: not suitable for Mooncake -->

<properties
   pageTitle="Create a virtual network using an ARM template | Azure"
   description="Learn how to create a virtual network using an ARM template | Resource Manager."
   services="virtual-network"
   documentationCenter=""
   authors="telmosampaio"
   manager="carmonm"
   editor="tysonn"
   tags="azure-resource-manager"/>

<tags
	ms.service="virtual-network"
	ms.date="03/15/2016"
	wacn.date=""/>

# Create a virtual network by using an ARM template

[AZURE.INCLUDE [virtual-networks-create-vnet-selectors-arm-include](../includes/virtual-networks-create-vnet-selectors-arm-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-intro](../includes/virtual-networks-create-vnet-intro-include.md)]

>[AZURE.IMPORTANT]Before you work with Azure resources, it's important to understand that Azure currently has two deployment models: Resource Manager, and classic. Make sure you understand [deployment models and tools](/documentation/articles/azure-classic-rm/) before working with any Azure resource. You can view the documentation for different tools by clicking the tabs at the top of this article. This document covers creating a VNet by using the Resource Manager deployment model. You can also [create a virtual network in the classic deployment model](/documentation/articles/virtual-networks-create-vnet-classic-pportal/).

You will learn how to download and modify and existing ARM template from GitHub, and deploy the template from GitHub, PowerShell, and the Azure CLI.

If you are simply deploying the ARM template directly from GitHub, without any changes, skip to [deploy a template from github](#deploy-the-arm-template-by-using-click-to-deploy).

[AZURE.INCLUDE [virtual-networks-create-vnet-scenario-include](../includes/virtual-networks-create-vnet-scenario-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-include](../includes/virtual-networks-create-vnet-arm-template-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-ps-include](../includes/virtual-networks-create-vnet-arm-template-ps-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-cli-include](../includes/virtual-networks-create-vnet-arm-template-cli-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-click-include](../includes/virtual-networks-create-vnet-arm-template-click-include.md)]