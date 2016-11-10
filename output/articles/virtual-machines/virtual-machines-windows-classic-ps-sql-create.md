<properties
	pageTitle="Create a SQL Server Virtual Machine in Azure PowerShell (Classic) | Azure"
	description="Provides steps and PowerShell scripts for creating an Azure VM with SQL Server virtual machine gallery images. This topic uses the classic deployment mode."
	services="virtual-machines-windows"
	documentationCenter="na"
	authors="rothja"
	manager="jhubbard"
	editor=""
	tags="azure-service-management" />
<tags
	ms.service="virtual-machines-windows"
	ms.devlang="na"
	ms.topic="article"
	ms.tgt_pltfrm="vm-windows-sql-server"
	ms.workload="infrastructure-services"
	ms.date="10/07/2016"
	wacn.date=""
	ms.author="jroth" />

# Provision a SQL Server virtual machine using Azure PowerShell (Classic)

## Overview

This article provides steps for how to create a SQL Server virtual machine in Azure by using the PowerShell cmdlets.

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)] For the Resource Manager version of this topic, see [Provision a SQL Server virtual machine using Azure PowerShell Resource Manager](/documentation/articles/virtual-machines-windows-ps-sql-create/).

### Install and configure PowerShell:

1. If you do not have an Azure account, visit [Azure trial](/pricing/1rmb-trial/).

2. [Download and install the latest Azure PowerShell commands](/documentation/articles/powershell-install-configure/).

3. Start Windows PowerShell, and connect it to your Azure subscription with the **Add-AzureAccount** command.

		Add-AzureAccount

## Determine your target Azure region

Your SQL Server Virtual Machine will be hosted in a cloud service that resides a specific Azure region. The following steps help you to determine your region, storage account, and cloud service that will be used for the rest of the tutorial.

1. Determine the data center that you want to use to host your SQL Server VM. The following PowerShell commands will display the available regions in detail with a summary list at the end.

		Get-AzureLocation
		(Get-AzureLocation).Name

2.  Once you've identified your preferred location, set a variable named **$dcLocation** to that region.

		$dcLocation = "<region name>"

## Set your subscription and storage account

1. Determine the Azure subscription you will use for the new virtual machine.

		(Get-AzureSubscription).SubscriptionName

1. Assign your target Azure subscription to the **$subscr** variable. Then set this as your current Azure subscription.

		$subscr="<subscription name>"
		Select-AzureSubscription -SubscriptionName $subscr -Current

1. Then check for existing storage accounts. The following script displays all storage accounts that exist in your chosen region:

		(Get-AzureStorageAccount | where { $_.GeoPrimaryLocation -eq $dcLocation }).StorageAccountName

	>[AZURE.NOTE] If you require a new storage account, first create an all-lower-case storage account name with the New-AzureStorageAccount command as in the following example: **New-AzureStorageAccount -StorageAccountName "<storage account name>" -Location $dcLocation**

1. Assign the target storage account name to the **$staccount**. Then use **Set-AzureSubscription** to set the subscription and current storage account.

		$staccount="<storage account name>"
		Set-AzureSubscription -SubscriptionName $subscr -CurrentStorageAccountName $staccount

## Select a SQL Server virtual machine image

1. Find out the list of available SQL Server virtual machines images from the gallery. These images all have an **ImageFamily** property that starts with "SQL". The following query displays the image family available to you that have SQL Server preinstalled.

		Get-AzureVMImage | where { $_.ImageFamily -like "SQL*" } | select ImageFamily -Unique | Sort-Object -Property ImageFamily

1. When you find the  virtual machine image family, there could be multiple published images in this family. Use the following script to find the latest published virtual machine image name for your selected image family (such as **SQL Server 2016 RTM Enterprise on Windows Server 2012 R2**):

		$family="<ImageFamily value>"
		$image=Get-AzureVMImage | where { $_.ImageFamily -eq $family } | sort PublishedDate -Descending | select -ExpandProperty ImageName -First 1

		echo "Selected SQL Server image name:"
		echo "   $image"

## Create the virtual machine

Finally, create the virtual machine with PowerShell:

1. Create a cloud service to host the new VM. Note that it is also possible to use an existing cloud service instead. Create a new variable **$svcname** with the short name of the cloud service.

		$svcname = "<cloud service name>"
		New-AzureService -ServiceName $svcname -Label $svcname -Location $dcLocation

2. Specify the virtual machine name and a size. For more information about virtual machine sizes, see [Virtual Machine Sizes for Azure](/documentation/articles/virtual-machines-windows-sizes/).

		$vmname="<machine name>"
		$vmsize="<Specify one: Large, ExtraLarge, A5, A6, A7, A8, A9, or see the link to the other VM sizes>"
		$vm1=New-AzureVMConfig -Name $vmname -InstanceSize $vmsize -ImageName $image

3. Specify the local administrator account and password.

		$cred=Get-Credential -Message "Type the name and password of the local administrator account."
		$vm1 | Add-AzureProvisioningConfig -Windows -AdminUsername $cred.GetNetworkCredential().Username -Password $cred.GetNetworkCredential().Password

4. Run the following script to create the virtual machine.

		New-AzureVM -ServiceName $svcname -VMs $vm1

>[AZURE.NOTE] For additional explanation and configuration options, see the **Build your command set** section in [Use Azure PowerShell to create and preconfigure Windows-based Virtual Machines](/documentation/articles/virtual-machines-windows-classic-create-powershell/).

## Example PowerShell script

The following script provides and example of a complete script that creates a **SQL Server 2016 RTM Enterprise on Windows Server 2012 R2** virtual machine. If you use this script, you must customize the initial variables based on the previous steps in this topic.

	# Customize these variables based on your settings and requirements:
	$dcLocation = "China East"
	$subscr="mysubscription"
	$staccount="mystorageaccount"
	$family="SQL Server 2016 RTM Enterprise on Windows Server 2012 R2"
	$svcname = "mycloudservice"
	$vmname="myvirtualmachine"
	$vmsize="A5"

	# Set the current subscription and storage account
	# Comment out the New-AzureStorageAccount line if the account already exists
	Select-AzureSubscription -SubscriptionName $subscr -Current
	New-AzureStorageAccount -StorageAccountName $staccount -Location $dcLocation
	Set-AzureSubscription -SubscriptionName $subscr -CurrentStorageAccountName $staccount

	# Select the most recent VM image in this image family:
	$image=Get-AzureVMImage | where { $_.ImageFamily -eq $family } | sort PublishedDate -Descending | select -ExpandProperty ImageName -First 1

	# Create the new cloud service; comment out this line if cloud service exists already:
	New-AzureService -ServiceName $svcname -Label $svcname -Location $dcLocation

	# Create the VM config:
	$vm1=New-AzureVMConfig -Name $vmname -InstanceSize $vmsize -ImageName $image

	# Set administrator credentials:
	$cred=Get-Credential -Message "Type the name and password of the local administrator account."
	$vm1 | Add-AzureProvisioningConfig -Windows -AdminUsername $cred.GetNetworkCredential().Username -Password $cred.GetNetworkCredential().Password

	# Create the SQL Server VM:
	New-AzureVM -ServiceName $svcname -VMs $vm1


## Connect with remote desktop

1. Create the .RDP files in the current user's document folder to launch these virtual machines to complete setup:

		$documentspath = [environment]::getfolderpath("mydocuments")
		Get-AzureRemoteDesktopFile -ServiceName $svcname -Name $vmname -LocalPath "$documentspath\vm1.rdp"

1. In the documents directory, launch the RDP file. Connect with the administrator user name and password provided earlier (for example, if your user name was VMAdmin, specify "\VMAdmin" as the user and provide the password).

		cd $documentspath
		.\vm1.rdp

## Complete the configuration of the SQL Server Machine for remote access

After logging onto the machine with remote desktop, configure SQL Server based on the instructions in [Steps for configuring SQL Server connectivity in an Azure VM](/documentation/articles/virtual-machines-windows-classic-sql-connect/#steps-for-configuring-sql-server-connectivity-in-an-azure-vm).

## Next steps

You can find additional instructions for provisioning virtual machines with PowerShell in the [virtual machines documentation](/documentation/articles/virtual-machines-windows-classic-create-powershell/). For additional scripts related to SQL Server and Premium Storage, see [Use Azure Premium Storage with SQL Server on Virtual Machines](/documentation/articles/virtual-machines-windows-classic-sql-server-premium-storage/).

In many cases, the next step is to migrate your databases to this new SQL Server VM. For database migration guidance, see [Migrating a Database to SQL Server on an Azure VM](/documentation/articles/virtual-machines-windows-migrate-sql/).

If you're also interested in using the Azure portal to create SQL Virtual Machines, see [Provisioning a SQL Server Virtual Machine on Azure](/documentation/articles/virtual-machines-windows-portal-sql-server-provision/). Note that the tutorial that walks you through the portal creates VMs using the recommended Resource Manager model, rather than the classic model used in this PowerShell topic.

In addition to these resources, we recommend that you review [other topics related to running SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-server-iaas-overview/).