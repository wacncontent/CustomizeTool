<properties
	pageTitle="Different ways to create a Linux VM | Azure"
	description="Learn the different ways to create a Linux virtual machine on Azure, including links to tools and tutorials for each method."
	services="virtual-machines-linux"
	documentationCenter=""
	authors="iainfoulds"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-linux"
	ms.devlang="na"
	ms.topic="get-started-article"
	ms.tgt_pltfrm="vm-linux"
	ms.workload="infrastructure-services"
	ms.date="09/27/2016"
	wacn.date=""
	ms.author="iainfou"/>

# Different ways to create a Linux virtual machine in Azure

You have the flexibility in Azure to create a Linux virtual machine (VM) using tools and workflows comfortable to you. This article summarizes these differences and examples for creating your Linux VMs.

## Azure CLI 

The Azure CLI is available across platforms via an npm package, distro-provided packages, or Docker container. You can read more about [how to install and configure the Azure CLI](/documentation/articles/xplat-cli-install/). The following tutorials provide examples on using the Azure CLI. Read each article for more details on the CLI quick-start commands shown:

- [Create a Linux VM from the Azure CLI for dev and test](/documentation/articles/virtual-machines-linux-quick-create-cli/)
	- The following example creates a CoreOS VM using a public key named `azure_id_rsa.pub`:

		azure vm quick-create -M ~/.ssh/azure_id_rsa.pub -Q CoreOS

- [Create a secured Linux VM using an Azure template](/documentation/articles/virtual-machines-linux-create-ssh-secured-vm-from-template/)
	- The following example creates a VM using a template stored on GitHub:

		azure group create --name TestRG --location ChinaNorth 
			--template-file /path/to/101-vm-sshkey/azuredeploy.json

- [Create a complete Linux environment using the Azure CLI](/documentation/articles/virtual-machines-linux-create-cli-complete/)
	- Includes creating a load balancer and multiple VMs in an availability set.

- [Add a disk to a Linux VM](/documentation/articles/virtual-machines-linux-add-disk/)
	- The following example adds a 5Gb disk to an existing VM named `TestVM`:

		azure vm disk attach-new --resource-group TestRG --vm-name TestVM <size-in-GB>

## Azure portal Preview

The graphical user interface of the [Azure portal Preview](https://portal.azure.cn) is an easy way to try out a VM, especially if you're just starting out with Azure since there is nothing to install on your system. Use the Azure portal Preview to create the VM:

* [Create a Linux VM using the Azure portal Preview](/documentation/articles/virtual-machines-linux-quick-create-portal/) 
* [Attach a disk using the Azure portal Preview](/documentation/articles/virtual-machines-linux-attach-disk-portal/)

## Operating system and image choices
When creating a VM, you choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools pre-installed. Or, upload one of your own images (see [the following section](#use-your-own-image)).

### Azure images
Use the `azure vm image` CLI commands to see what's available by publisher, distro release, and builds.

List available publishers as follows:

	azure vm image list-publishers --location ChinaNorth

List available products (offers) for a given publisher as follows:

	azure vm image list-offers --location ChinaNorth --publisher Canonical

List available SKUs (distro releases) of a given offer as follows:

	azure vm image list-skus --location ChinaNorth --publisher Canonical --offer UbuntuServer

List all available images for a given release follows:

	azure vm image list --location ChinaNorth --publisher Canonical --offer UbuntuServer --sku 16.04.0-LTS

For more examples on browsing and using available images, see [Navigate and select Azure virtual machine images with the Azure CLI](/documentation/articles/virtual-machines-linux-cli-ps-findimage/).

The `azure vm quick-create` and `azure vm create` commands have aliases you can use to quickly access the more common distros and their latest releases. Using aliases is often quicker than specifying the publisher, offer, SKU, and version each time you create a VM:

| Alias     | Publisher | Offer        | SKU         | Version |
|:----------|:----------|:-------------|:------------|:--------|
| CentOS    | OpenLogic | Centos       | 7.2         | latest  |
| openSUSE  | SUSE      | openSUSE     | 13.2        | latest  |
| SUSE | SLES      | SLES         | 12-SP1      | latest  |
| UbuntuLTS | Canonical | UbuntuServer | 14.04.3-LTS | latest  |

### Use your own image

If you require specific customizations, you can use an image based on an existing Azure VM by *capturing* that VM. You can also upload an image created on-premises. For more information on supported distros and how to use your own images, see the following articles:

- [Azure endorsed distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)

- [Information for non-endorsed distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)

- [How to capture a Linux virtual machine as a Resource Manager template](/documentation/articles/virtual-machines-linux-capture-image/).
	- Quick-start example commands to capture an existing VM:

		azure vm deallocate --resource-group TestRG --vm-name TestVM
		azure vm generalize --resource-group TestRG --vm-name TestVM
		azure vm capture --resource-group TestRG --vm-name TestVM --vhd-name-prefix CapturedVM

## Next steps

- Create a Linux VM from the [portal](/documentation/articles/virtual-machines-linux-quick-create-portal/), with the [CLI](/documentation/articles/virtual-machines-linux-quick-create-cli/), or using an [Azure Resource Manager template](/documentation/articles/virtual-machines-linux-cli-deploy-templates/).

- After creating a Linux VM, [add a data disk](/documentation/articles/virtual-machines-linux-add-disk/).

- Quick steps to [reset a password or SSH keys and manage users](/documentation/articles/virtual-machines-linux-using-vmaccess-extension/)
