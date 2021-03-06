<properties
	pageTitle="Set up endpoints on a classic Linux VM | Microsoft Azure"
	description="Learn to set up endpoints in the Azure classic portal to allow communication with a Linux virtual machine in Azure"
	services="virtual-machines-linux"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="04/19/2016"
	wacn.date=""/>

# How to set up endpoints on a classic virtual machine in Azure

All Linux virtual machines that you create in Azure using the classic deployment model can automatically communicate over a private network channel with other virtual machines in the same cloud service or virtual network. However, computers on the Internet or other virtual networks require endpoints to direct the inbound network traffic to a virtual machine. This article is also available for [Windows virtual machines](/documentation/articles/virtual-machines-windows-classic-setup-endpoints/).


[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.


> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the Resource Manager model. 


When you create a Linux virtual machine in the Azure  classic  Classic   portal  Management Portal , an endpoint for Secure Shell (SSH) is typically created for you automatically. You can configure additional endpoints while creating the virtual machine or afterwards as needed.
 

[AZURE.INCLUDE [virtual-machines-common-classic-setup-endpoints](../includes/virtual-machines-common-classic-setup-endpoints.md)]

## Next steps

* You can also create a VM endpoint by using the [Azure Command-Line Interface](/documentation/articles/virtual-machines-command-line-tools/). Run the **azure vm endpoint create** command.

* If you created a virtual machine in the Resource Manager deployment model, you can use the Azure CLI in Resource Manager mode to [create network security groups](/documentation/articles/virtual-networks-create-nsg-arm-cli/) to control traffic to the VM.