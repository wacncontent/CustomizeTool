<properties
	pageTitle="Create a custom virtual machine running Windows | Windows Azure"
	description="Learn to create a custom virtual machine running Windows in Azure."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>


<tags
	ms.service="virtual-machines"
	ms.date="08/11/2015"
	wacn.date=""/>

#Create a custom virtual machine running Windows in Azure
<!-- deleted by customization

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.

-->

A *custom* virtual machine simply means a virtual machine you create using the **From Gallery** option because it gives you more configuration choices than the **Quick Create** option. These choices include:

- Connecting the virtual machine to a virtual network.
- Installing the VM Agent and extensions, such as for antimalware.
- Adding the virtual machine to an existing cloud service.
- Adding the virtual machine to an existing storage account.
- Adding the virtual machine to an availability set.

> [AZURE.IMPORTANT] If you want your virtual machine to use a virtual network so you can connect to it directly by hostname or set up cross-premises connections, make sure you specify the virtual network when you create the virtual machine. A virtual machine can be configured to join a virtual network only when you create the virtual machine. For details on virtual networks, see [Azure Virtual Network Overview](/documentation/articles/virtual-networks-overview).

##To create the virtual machine

[AZURE.INCLUDE [virtual-machines-create-WindowsVM](../includes/virtual-machines-create-windowsvm.md)]
