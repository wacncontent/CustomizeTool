<properties
	pageTitle="Create a VM running Windows in the Classic Management Portal | Azure"
	description="Create a Windows virtual machine in the Azure Classic Management Portal."
	services="virtual-machines-windows"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines-windows"
	ms.workload="infrastructure-services"
	ms.tgt_pltfrm="vm-windows"
	ms.devlang="na"
	ms.topic="article"
	ms.date="09/27/2016"
	wacn.date=""
	ms.author="cynthn"/>

# Create a virtual machine running Windows in the Azure Classic Management Portal

> [AZURE.SELECTOR]
- [Azure Classic Management Portal](/documentation/articles/virtual-machines-windows-classic-tutorial/)
- [PowerShell: Classic deployment](/documentation/articles/virtual-machines-windows-classic-create-powershell/)

<br>

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)] Learn how to [perform these steps using the Resource Manager deployment model](/documentation/articles/virtual-machines-windows-hero-tutorial/). If you want to use the new Azure portal, see [Create your first Windows virtual machine in the Azure portal](/documentation/articles/virtual-machines-windows-hero-tutorial/).

This tutorial shows you how easy it is to create an Azure virtual machine (VM) running Windows in the Azure Classic Management Portal. We'll use a Windows Server image as an example, but that's just one of the many images Azure offers. Note that your image choices depend on your subscription. For example, Windows desktop images may be available to MSDN subscribers.

This section shows you how to use the **From Gallery** option in the Azure Classic Management Portal to create the virtual machine. This option provides more configuration choices than the **Quick Create** option. For example, if you want to join a virtual machine to a virtual network, you'll need to use the **From Gallery** option.

You can also create VMs using [your own images](/documentation/articles/virtual-machines-windows-classic-createupload-vhd/). To learn about this and other methods, see [Different ways to create a Windows virtual machine](/documentation/articles/virtual-machines-windows-creation-choices/).
## <a id="createvirtualmachine"> </a>Create the virtual machine

[AZURE.INCLUDE [virtual-machines-create-WindowsVM](../../includes/virtual-machines-create-windowsvm.md)]

## Next steps

- Log on to the virtual machine. For instructions, see [Log on to a virtual machine running Windows Server](/documentation/articles/virtual-machines-windows-classic-connect-logon/).

- Attach a disk to store data. You can attach both empty disks and disks that contain data. For instructions, see the [Attach a data disk to a Windows virtual machine created with the classic deployment model](/documentation/articles/virtual-machines-windows-classic-attach-disk/).
