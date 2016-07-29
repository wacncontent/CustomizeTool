<properties
	pageTitle="Different ways to create a Linux VM | Microsoft Azure"
	description="Lists the different ways to create a Linux virtual machine on Azure and links to tools and tutorials for each method"
	services="virtual-machines-linux"
	documentationCenter=""
	authors="iainfoulds"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="06/14/2016"
	wacn.date=""/>

# Different ways to create a Linux virtual machine with Resource Manager

Azure offers different ways to create a VM using the Resource Manager deployment model, to suit different users and purposes. This article summarizes these differences and the choices you can make for creating your Linux virtual machines (VMs).

## Azure CLI 

You can read more about [how to install the Azure CLI](/documentation/articles/xplat-cli-install/) via npm, Docker container, or install script. The following tutorials provide examples on using the Azure CLI:

* [Create a Linux VM from the Azure CLI for dev and test](/documentation/articles/virtual-machines-linux-quick-create-cli/) 

* [Create a secured Linux VM using an Azure template](/documentation/articles/virtual-machines-linux-create-ssh-secured-vm-from-template/)

* [Create a Linux VM from the ground up using the Azure CLI](/documentation/articles/virtual-machines-linux-create-cli-complete/)

## Azure portal

The graphical user interface of the [Azure portal](https://portal.azure.com) is an easy way to try out a VM, especially if you're just starting out with Azure since there is nothing to install on your system. Use the Azure portal to create the VM:

* [Create a virtual machine running Linux using the Azure portal](/documentation/articles/virtual-machines-linux-quick-create-portal/) 

## Operating system and image choices

With both methods, you choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools pre-installed. Or, you you can upload one of your own images.

### Azure images

In all of the above articles, you can easily use an existing Azure image to create a VM and customize it for networking, load balancing, and more. The portal provides the Azure Marketplace for Azure supplied images. You can get similar lists using the command line. For example, in Azure CLI, run `azure vm image list` to get a list of all available images, by location and publisher. See [Navigate and select Azure virtual machine images with the Azure CLI](/documentation/articles/virtual-machines-linux-cli-ps-findimage/) for examples on browsing and using available images.

### Use your own image

If you require specific customizations, you can use an image based on an existing Azure VM by *capturing* that VM, or upload an image of your own, stored in a virtual hard disk (VHD). For more information on supported distros and how to use your own images, see the following articles:

* [Azure endorsed distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)

* [Information for non-endorsed distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)

* [How to capture a Linux virtual machine as a Resource Manager template](/documentation/articles/virtual-machines-linux-capture-image/). 

## Next steps

* Try one of the tutorials to create a Linux VM from the [portal](/documentation/articles/virtual-machines-linux-quick-create-portal/), with the [CLI](/documentation/articles/virtual-machines-linux-quick-create-cli/), or using an Azure Resource Manager [template](/documentation/articles/virtual-machines-linux-cli-deploy-templates/).

* After creating a Linux VM, you can easily [add a data disk](/documentation/articles/virtual-machines-linux-add-disk/).

* Quick steps to [reset a password or SSH keys and manage users](/documentation/articles/virtual-machines-linux-using-vmaccess-extension/)
