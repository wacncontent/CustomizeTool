<properties
	pageTitle="Create and upload a Linux VHD | Microsoft Azure"
	description="Create and upload an Azure virtual hard disk (VHD) with the classic deployment model that contains the Linux operating system."
	services="virtual-machines-linux"
	documentationCenter=""
	authors="iainfoulds"
	manager="timlt"
	editor="tysonn"
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="06/14/2016"
	wacn.date=""/>

# Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.

This article shows you how to create and upload a virtual hard disk (VHD) so you can use it as your own image to create virtual machines in Azure. You'll learn how to prepare the operating system so you can use it to create multiple virtual machines based on that image.

**Important**: The Azure platform SLA applies to virtual machines running the Linux OS only when one of the endorsed distributions is used with the configuration details as specified under 'Supported Versions' in [Linux on Azure-Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/). All Linux distributions in the Azure image gallery are endorsed distributions with the required configuration.


## Prerequisites
This article assumes that you have the following items:

- **Linux operating system installed in a .vhd file**  - You have installed an [Azure-endorsed Linux distribution](/documentation/articles/virtual-machines-linux-endorsed-distros/) (or see [information for non-endorsed distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)) to a virtual disk in the VHD format. Multiple tools exist to create .vhd files - for example you can use a virtualization solution such as Hyper-V to create the .vhd file and install the operating system. For instructions, see [Install the Hyper-V Role and Configure a Virtual Machine](http://technet.microsoft.com/en-us/library/hh846766.aspx).

	> [AZURE.NOTE] The newer VHDX format is not supported in Azure. You can convert a VHDX to VHD format using Hyper-V Manager or the `Convert-VHD` cmdlet. Further, Azure does not support uploading dynamic VHDs, so you need to convert such disks to static VHDs before uploading. You can use tools such as [Azure VHD Utilities for GO](https://github.com/Microsoft/azure-vhd-utils-for-go) to convert dynamic disks.

- **Azure Command-line Interface** - Install the latest [Azure Command-Line Interface](/documentation/articles/virtual-machines-command-line-tools/) to upload the VHD.

<a id="prepimage"> </a>
## Step 1: Prepare the image to be uploaded

Azure supports a variety of Linux distributions (see [Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)). The following articles will guide you through how to prepare the various Linux distributions that are supported on Azure. After following the steps in the guides below, come back here and you should have a VHD file that is ready to upload to Azure:

- **[CentOS-based Distributions](/documentation/articles/virtual-machines-linux-create-upload-centos/)**
- **[Debian Linux](/documentation/articles/virtual-machines-linux-debian-create-upload-vhd/)**
- **[Oracle Linux](/documentation/articles/virtual-machines-linux-oracle-create-upload-vhd/)**
- **[Red Hat Enterprise Linux](/documentation/articles/virtual-machines-linux-redhat-create-upload-vhd/)**
- **[SLES & openSUSE](/documentation/articles/virtual-machines-linux-suse-create-upload-vhd/)**
- **[Ubuntu](/documentation/articles/virtual-machines-linux-create-upload-ubuntu/)**
- **[Other - Non-Endorsed Distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)**

Also see the **[Linux Installation Notes](/documentation/articles/virtual-machines-linux-create-upload-generic/#general-linux-installation-notes)** for more general tips on preparing Linux images for Azure.


<a id="connect"> </a>
## Step 2: Prepare the connection to Azure

Make sure you are using the Azure CLI in the classic deployment model (`azure config mode asm`), then log in to your account:

```
azure login
```


<a id="upload"> </a>
## Step 3: Upload the image to Azure

You will need a storage account to upload your VHD file to. You can either pick an existing one or [create a new one](/documentation/articles/storage-create-storage-account/).

Use the Azure CLI to upload the image by using the following command:

		azure vm image create <ImageName> --blob-url <BlobStorageURL>/<YourImagesFolder>/<VHDName> --os Linux <PathToVHDFile>

In the previous example:

- **BlobStorageURL** is the URL for the storage account you plan to use
- **YourImagesFolder** is the container within blob storage where you want to store your images
- **VHDName** is the label that appears in portal to identify the virtual hard disk.
- **PathToVHDFile** is the full path and name of the .vhd file on your machine.

For more information, see [Azure CLI reference for Azure Service Management](/documentation/articles/virtual-machines-command-line-tools/).

[Step 1: Prepare the image to be uploaded]: #prepimage
[Step 2: Prepare the connection to Azure]: #connect
[Step 3: Upload the image to Azure]: #upload
