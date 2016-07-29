<properties
	pageTitle="About disks and VHDs for Windows VMs | Azure"
	description="Learn about the basics of disks and VHDs for Windows virtual machines in Azure."
	services="virtual-machines-windows"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor="tysonn"
	tags="azure-resource-manager,azure-service-management"/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="06/16/2016"
	wacn.date=""/>

# About disks and VHDs for Azure virtual machines

Just like any other computer, virtual machines in Azure use disks as a place to store an operating system, applications, and data. All Azure virtual machines have at least two disks - a Windows operating system disk (in the case of a Windows VM) and a temporary disk. The operating system disk is created from an image, and both the operating system disk and the image are actually virtual hard disks (VHDs) stored in an Azure storage account. Virtual machines also can have one or more data disks, that are also stored as VHDs. This article is also available for [Linux virtual machines](/documentation/articles/virtual-machines-linux-about-disks-vhds/).

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)]

[AZURE.INCLUDE [virtual-machines-common-about-disks-vhds](../includes/virtual-machines-common-about-disks-vhds.md)]

## Next steps
-  [Capture a Windows virtual machine](/documentation/articles/virtual-machines-windows-capture-image/) so you can scale-out your VM deployment.
-  [Upload a Windows VM image to Azure](/documentation/articles/virtual-machines-windows-upload-image/) to use when creating a new VM.
-  [Change the drive letter of the Windows temporary disk](/documentation/articles/virtual-machines-windows-classic-change-drive-letter/) so your application can use the D: drive for data.
