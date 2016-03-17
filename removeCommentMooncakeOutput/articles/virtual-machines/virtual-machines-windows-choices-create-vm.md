<properties
	pageTitle="Different ways to create a Windows VM | Azure"
	description="Lists the different ways to create a Windows virtual machine with Resource Manager."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/22/2015"
	wacn.date=""/>

# Different ways to create a Windows virtual machine 

Azure offers different ways to create a virtual machine because virtual machines are suited for different users and purposes. This means that you need to make some choices about the virtual machine and how to create it. This article gives you a summary of these choices and links to instructions.

## Tool choices

### GUI: Azure Management Portal

The graphical user interface of the Azure Management Portal is an easy way to try out a virtual machine, especially if you're just starting out with Azure. Use the Azure Management Portal to create the virtual machine:

[Create a virtual machine running Windows][]

### Command shell: Azure CLI or Azure PowerShell

If you prefer working in a command shell, choose between the Azure command-line interface (CLI) for Mac and Linux users, or Azure PowerShell, which has cmdlets for Azure and a custom console.

For Azure CLI, see:

- [Using the Azure CLI for Mac, Linux, and Windows with Azure Service Management](/documentation/articles/virtual-machines-command-line-tools).
- [Create a multi-VM deployment with the Azure CLI](/documentation/articles/virtual-machines-create-multi-vm-deployment-xplat-cli)

For Azure PowerShell, see:

- [Create a SQL Server Virtual Machine in Azure (PowerShell)](/documentation/articles/virtual-machines-sql-server-create-vm-with-powershell)
- [Manage your virtual machines by using Azure PowerShell](/documentation/articles/virtual-machines-manage-vms-powershell)

## Operating system and image choices

Choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools. Or, use one of your own images. Find the platform image that you need for your application by using the information in: [Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI][].

<!-- LINKS -->

[Create a virtual machine running Windows]: virtual-machines-windows-tutorial-classic-portal

[Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI]: /documentation/articles/resource-groups-vm-searching

