<properties
	pageTitle="FAQ for Windows VMs | Azure"
	description="Provides answers to some of the common questions about Windows virtual machines created with the Resource Manager model."
	services="virtual-machines-windows"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-management"/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="05/16/2016"
	wacn.date=""/>

# Frequently asked question about Windows Virtual Machines 


This article addresses some common questions users ask about Windows virtual machines created in Azure using the Resource Manager deployment model. For the Linux version of this topic, see [Frequently asked question about Linux Virtual Machines](/documentation/articles/virtual-machines-linux-faq/)

## What can I run on an Azure VM?

All subscribers can run server software on an Azure virtual machine. For information about the support policy for running Microsoft server software in Azure, see [Microsoft server software support for Azure Virtual Machines](https://support.microsoft.com/kb/2721672)

## How much storage can I use with a virtual machine?

Each data disk can be up to 1 TB. The number of data disks you can use depends on the size of the virtual machine. For details, see [Sizes for Virtual Machines](/documentation/articles/virtual-machines-windows-sizes/).

An Azure storage account provides storage for the operating system disk and any data disks. Each disk is a .vhd file stored as a page blob. For pricing details, see [Storage Pricing Details](/home/features/storage/pricing/).


## How can I access my virtual machine?

You need to establish a remote connection using Remote Desktop Connection (RDP) for a Windows VM. For instructions, see [How to connect and log on to an Azure virtual machine running Windows](/documentation/articles/virtual-machines-windows-connect-logon/). A maximum of 2 concurrent connections are supported, unless the server is configured as a Remote Desktop Services session host.  


If you're having problems with Remote Desktop, see [Troubleshoot Remote Desktop connections to a Windows-based Azure Virtual Machine](/documentation/articles/virtual-machines-windows-troubleshoot-rdp-connection/). 

If you're familiar with Hyper-V, you might be looking for a tool similar to VMConnect. Azure doesn't offer a similar tool because console access to a virtual machine isn't supported.

## Can I use the temporary disk (the D: drive by default) to store data?

You shouldn't use the temporary disk to store data. It is only temporary storage, so you would risk losing data that can't be recovered. This can occur when the virtual machine moves to a different host. Resizing a virtual machine, updating the host, or a hardware failure on the host are some of the reasons a virtual machine might move.

If you have an application that needs to use the D: drive letter, you can reassign drive letters so that the temporary disk uses soemthing other than D:. For instructions, see [Change the drive letter of the Windows temporary disk](/documentation/articles/virtual-machines-windows-classic-change-drive-letter/).

## How can I change the drive letter of the temporary disk?

On a Windows virtual machine, you can change the drive letter by moving the page file and reassigning drive letters, but you'll need to make sure you do the steps in a specific order. For instructions, see [Change the drive letter of the Windows temporary disk](/documentation/articles/virtual-machines-windows-classic-change-drive-letter/).

## Can I add an existing VM to an availability set?

No. If you want your VM to be part of an availability set, you need to create the VM within the set. There currently isn't a way to add a VM to an availability set after it has been created.

## Can I upload a virtual machine to Azure?

Yes. For instructions, see [Upload a Windows VM image to Azure ](/documentation/articles/virtual-machines-windows-upload-image/)

## Can I resize the OS disk?

Yes. For instructions, see [How to expand the OS drive of a Virtual Machine in an Azure Resource Group](/documentation/articles/virtual-machines-windows-expand-os-disk/).

## Can I copy or clone an existing Azure VM?

Yes. For instructions, see [How to create a copy of a Windows virtual machine in the Resource Manager deployment model](/documentation/articles/virtual-machines-windows-specialized-image/).

## Does Azure support Linux VMs?

Yes. To quickly create a Linux VM to try out, see [Create a Linux VM on Azure using the Portal](/documentation/articles/virtual-machines-linux-quick-create-portal/).

