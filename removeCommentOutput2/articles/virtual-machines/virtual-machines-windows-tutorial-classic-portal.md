<properties
	pageTitle="Create a VM running Windows in the Management Portal | Azure"
	description="Create a Windows virtual machine in the Azure Management Portal."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/06/2016"
	wacn.date=""/>

# Create a virtual machine running Windows in the Azure Management Portal

> [AZURE.SELECTOR]
- [Azure Management Portal](/documentation/articles/virtual-machines-windows-tutorial-classic-portal)
- [PowerShell: Classic deployment](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)

<!-- HHTML comment in to break between the selector and the note in the include below-->

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] [Resource Manager deploymen

This tutorial shows you how easy it is to create an Azure virtual machine (VM) running Windows in the Azure Management Portal. We'll use a Windows Server image as an example, but that's just one of the many images Azure offers. Note that your image choice

You can also create VMs using [your own images](/documentation/articles/virtual-machines-create-upload-vhd-windows-server). To learn about this and other methods, see [Different ways to create a Windows virtual machine](/documentation/articles/virtual-machines-windows-choices-create-vm).

[AZURE.INCLUDE [free-trial-note](../includes/free-trial-note.md)]

## <a id="createvirtualmachine"> </a>How to create the virtual machine

This section shows you how to use the **From Gallery** option in the Azure Management Portal to create the virtual machine. This option provides more configuration choices than the **Quick Create** option. For example, if you want to join a virtual machine to a virtual network, you'll need to use the **From Gallery** option.

[AZURE.INCLUDE [virtual-machines-create-WindowsVM](../includes/virtual-machines-create-windowsvm.md)]

## Next steps

- Log on to the virtual machine. For instructions, see [Log on to a virtual machine running Windows Server](/documentation/articles/virtual-machines-log-on-windows-server).

- Attach a disk to store data. You can attach both empty disks and disks that contain data. For instructions, see the [Attach a data disk to a Windows virtual machine created with the classic deployment model](/documentation/articles/storage-windows-attach-disk).
