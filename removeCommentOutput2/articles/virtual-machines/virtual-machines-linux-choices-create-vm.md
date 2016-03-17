<properties
	pageTitle="Different ways to create a Linux VM | Azure"
	description="Lists the different ways to create a Linux virtual machine on Azure and gives links to further instructions."
	services="virtual-machines"
	documentationCenter=""
	authors="dsk-2015"
	manager="timlt"
	editor=""
	tags="azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/20/2016"
	wacn.date=""/>

# Different Ways to Create a Linux Virtual Machine

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)]

Azure offers different ways to create a VM, to suit different users and purposes. This article summarizes these differences and the choices you can make for creating your Linux virtual machines.

## Tool choices

### GUI: The Azure Management Portal

The graphical user interface of the Azure Management Portal is an easy way to try out a virtual machine, especially if you're just starting out with Azure. Use the [Azure Management Portal](https://manage.windowsazure.cn) to create the VM. For general instructions, see [Create a Custom Virtual Machine][] and select any Linux image from the **Gallery**.

### Command Shell: Azure CLI or Azure PowerShell

If you prefer working in a command shell, choose between the Azure command-line interface (CLI) for Mac, Linux and Windows users, or the Azure PowerShell, which has Windows PowerShell cmdlets for Azure and a custom console.

For classic deployment model, see [Create a custom Linux virtual machine using Azure CLI](/documentation/articles/virtual-machines-linux-create-custom) and
[Use Azure PowerShell to create and preconfigure Linux-based Virtual Machines][].


### Development Environment: Visual Studio


Visual Studio also supports creating Azure virtual machines. For classic deployment model, read [Creating a virtual machine for a website with Visual Studio][].

## Operating System and Image Choices

Choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools. Or, use one of your own images.


### Azure Images

In all of the above articles, you can easily use an existing Azure image to create a virtual machine and customize it for networking, load balancing, and more. The portals provide a gallery or image list for Azure supplied images. You can get similar lists using the command line. For example, in Azure CLI, run `azure vm image list` to get a list of all available images, by location and publisher.


### Use Your Own Image

Use an image based on an existing Azure virtual machine by *capturing* that VM, or upload an image of your own, stored in a virtual hard disk (VHD). For classic deployment model, see [How to Capture a Linux Virtual Machine to Use as a Template with the CLI][] and [Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System][].

## Next Steps

[Log On to the Virtual Machine][]

[Attach a Data Disk][]

## Additional resources

[Base Configuration Test Environment][]

[Azure hybrid cloud test environments][]


<!-- LINKS -->
[overview]: /documentation/articles/resource-group-overview

[Create a Virtual Machine Running Windows]: /documentation/articles/virtual-machines-windows-tutorial-classic-portal
[Create a Virtual Machine Running Linux]: /documentation/articles/virtual-machines-linux-tutorial

[Equivalent Resource Manager and Service Management Commands for VM Operations with the Azure CLI for Mac, Linux, and Windows]:/documentation/articles/xplat-cli-azure-manage-vm-asm-arm
[Deploy and Manage Virtual Machines using Azure Resource Manager Templates and the Azure CLI]: /documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli
[Deploy and Manage Virtual Machines using Azure Resource Manager Templates and PowerShell]:  /documentation/articles/virtual-machines-deploy-rmtemplates-powershell
[Use Azure PowerShell to create and preconfigure Linux-based Virtual Machines]: /documentation/articles/virtual-machines-ps-create-preconfigure-linux-vms

[How to Create a Custom Virtual Machine Running Linux in Azure]: /documentation/articles/virtual-machines-linux-create-custom
[How to Capture a Linux Virtual Machine to Use as a Template with the CLI]: /documentation/articles/virtual-machines-linux-capture-image

[Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System]: /documentation/articles/virtual-machines-linux-create-upload-vhd

[Creating a virtual machine for a website with Visual Studio]: /documentation/articles/virtual-machines-dotnet-create-visual-studio-powershell
[Deploy Azure Resources Using the Compute, Network, and Storage .NET Libraries]: /documentation/articles/virtual-machines-arm-deployment

[Log On to the Virtual Machine]: /documentation/articles/virtual-machines-linux-how-to-log-on

[Attach a Data Disk]: /documentation/articles/virtual-machines-linux-how-to-attach-disk

[Base Configuration Test Environment]: /documentation/articles/virtual-machines-base-configuration-test-environment
[Azure hybrid cloud test environments]: /documentation/articles/virtual-machines-hybrid-cloud-test-environments

[Create a Virtual Machine Running Linux]: /documentation/articles/virtual-machines-linux-tutorial
[Create a Custom Virtual Machine]: /documentation/articles/virtual-machines-create-custom
