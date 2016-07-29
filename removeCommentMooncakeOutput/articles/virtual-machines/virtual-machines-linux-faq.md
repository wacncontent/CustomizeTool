<properties
	pageTitle="FAQ for Linux VMs | Azure"
	description="Provides answers to some of the common questions about Linux virtual machines created with the Resource Manager model."
	services="virtual-machines-linux"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-management"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="05/16/2016"
	wacn.date=""/>

# Frequently asked question about Linux Virtual Machines 


This article addresses some common questions users ask about Linux virtual machines created in Azure using the Resource Manager deployment model. For the Windows version of this topic, see [Frequently asked question about Windows Virtual Machines](/documentation/articles/virtual-machines-windows-faq/)

## What can I run on an Azure VM?

All subscribers can run server software on an Azure virtual machine. For more information, see [Linux on Azure-Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)


## How much storage can I use with a virtual machine?

Each data disk can be up to 1 TB. The number of data disks you can use depends on the size of the virtual machine. For details, see [Sizes for Virtual Machines](/documentation/articles/virtual-machines-linux-sizes/).

An Azure storage account provides storage for the operating system disk and any data disks. Each disk is a .vhd file stored as a page blob. For pricing details, see [Storage Pricing Details](/home/features/storage/pricing/).



## How can I access my virtual machine?

You need to establish a remote connection to log on to the virtual machine, using Secure Shell (SSH). See the instructions on how to connect [from Windows](/documentation/articles/virtual-machines-linux-ssh-from-windows/) or 
[from Linux and Mac](/documentation/articles/virtual-machines-linux-ssh-from-linux/). By default, SSH allows a maximum of 10 concurrent connections. You can increase this number by editing the configuration file.


If you're having problems, check out [Troubleshoot Secure Shell (SSH) connections](/documentation/articles/virtual-machines-linux-troubleshoot-ssh-connection/).

## Can I use the temporary disk (/dev/sdb1) to store data?

You shouldn't use the temporary disk (/dev/sdb1) to store data. It is only there for temporary storage, you would risk losing data that can't be recovered. 

## Can I copy or clone an existing Azure VM?

Yes. For instructions, see [How to create a copy of a Linux virtual machine in the Resource Manager deployment model](/documentation/articles/virtual-machines-linux-specialized-image/).
