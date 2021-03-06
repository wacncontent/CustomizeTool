<properties
	pageTitle="Create and manage a Windows VM using Azure PowerShell | Windows Azure"
	description="Create and manage a Windows virtual machine with Azure Powershell using the classic deployment model."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="07/09/2015"
	wacn.date=""/>

# Create and manage a Windows virtual machine using Azure PowerShell

This article describes how to create and manage Windows virtual machines using Azure PowerShell.

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] [Resource Manager model](/documentation/articles/virtual-machines-deploy-rmtemplates-powershell).
-->
<!-- keep by customization: begin -->
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-include.md)] This article covers creating a Windows VM with the classic deployment model. You can also create a Windows VM with the [Resource Manager deployment model](/documentation/articles/virtual-machines-deploy-rmtemplates-powershell).
<!-- keep by customization: end -->



## Set up Azure PowerShell

If you have already installed Azure PowerShell, you must have Azure PowerShell version 0.8.0 or later. You can check the version of Azure PowerShell that you have installed by using this command at the Azure PowerShell command prompt:

	Get-Module azure | format-table version

If you haven't done so already, use the instructions in [How to install and configure Azure PowerShell](/documentation/articles/install-configure-powershell) to install Azure PowerShell on your local computer. Then, open an Azure PowerShell command prompt.

First, you must sign in to Azure by using this command:

	Add-AzureAccount

Specify the email address of your Azure account and its password in the Windows Azure sign-in dialog.

Next, if you have multiple Azure subscriptions, you need to set your Azure subscription. To see a list of your current subscriptions, run this command:

	Get-AzureSubscription | sort SubscriptionName | Select SubscriptionName

Now, replace everything within the quotes, including the < and > characters, with the correct subscription name and run these commands:

	$subscrName="<subscription name>"
	Select-AzureSubscription -SubscriptionName $subscrName –Current

## Create a virtual machine

First, you need a Storage account. You can display your current list of Storage accounts by using this command:

	Get-AzureStorageAccount | sort Label | Select Label

If you do not already have one, create a new Storage account. You must pick a unique name that contains only lowercase letters and numbers. You can test for the uniqueness of the Storage account name by using this command:

	Test-AzureName -Storage <Proposed Storage account name>

If this command returns "False", your proposed name is unique.

You will need to specify the location of an Azure datacenter when creating a Storage account. To get a list of Azure datacenters, run this command:

	Get-AzureLocation | sort Name | Select Name

Now, create and set the Storage account by using the following commands. Fill in the names of the storage account and replace everything within the quotes, including the < and > characters.

	$stAccount="<chosen Storage account name>"
	$locName="<Azure location>"
	New-AzureStorageAccount -StorageAccountName $stAccount -Location $locName
	Set-AzureStorageAccount -StorageAccountName $stAccount
	Set-AzureSubscription -SubscriptionName $subscrName -CurrentStorageAccountName $stAccount

Next, you need a cloud service. If you do not have an existing cloud service, you must create one. You must pick a unique name that contains only letters, numbers, and hyphens. The first and last character in the field must be a letter or number.

For example, you could name it TestCS-*UniqueSequence*, in which *UniqueSequence* is an abbreviation of your organization. For example, if your organization is named Tailspin Toys, you could name the cloud service TestCS-Tailspin.

You can test for the uniqueness of the name by using this Azure PowerShell command:

	Test-AzureName -Service <Proposed cloud service name>

If this command returns "False", your proposed name is unique. Create the cloud service by using these commands:

	$csName="<cloud service name>"
	$locName="<Azure location>"
	New-AzureService -Service $csName -Location $locName

Next, copy this set of Azure PowerShell commands to a text editor, such as Notepad:

	$vmName="<machine name>"
	$csName="<cloud service name>"
	$locName="<Azure location>"
	$image=Get-AzureVMImage | where { $_.ImageFamily -eq "Windows Server 2012 R2 Datacenter" } | sort PublishedDate -Descending | select -ExpandProperty ImageName -First 1
	$vm=New-AzureVMConfig -Name $vmName -InstanceSize Medium -ImageName $image
	$cred=Get-Credential -Message "Type the name and password of the local administrator account."
	$vm | Add-AzureProvisioningConfig -Windows -AdminUsername $cred.GetNetworkCredential().Username -Password $cred.GetNetworkCredential().Password
	New-AzureVM –ServiceName $csName –Location $locName -VMs $vm

In your text editor, fill in the name of the virtual machine, the cloud service name, and the location.

Finally, copy the command set to the Clipboard and then right-click your open Azure PowerShell command prompt. This will issue the command set as a series of Azure PowerShell commands, prompt you for the name and password of the local administrator account, and create your Azure virtual machine.
Here is an example of what running the command set looks like:

	PS C:\> $vmName="PSTest"
	PS C:\> $csName=" TestCS-Tailspin"
	PS C:\> $locName="China North"
	PS C:\> $image=Get-AzureVMImage | where { $_.ImageFamily -eq "Windows Server 2012 R2 Datacenter" } | sort PublishedDate -Descending | select -ExpandProperty ImageName -First 1
	VERBOSE: 3:01:17 PM - Begin Operation: Get-AzureVMImage
	VERBOSE: 3:01:22 PM - Completed Operation: Get-AzureVMImage
	VERBOSE: 3:01:22 PM - Begin Operation: Get-AzureVMImage
	VERBOSE: 3:01:23 PM - Completed Operation: Get-AzureVMImage
	PS C:\> $vm=New-AzureVMConfig -Name $vmName -InstanceSize Medium -ImageName $image
	PS C:\> $cred=Get-Credential -Message "Type the name and password of the local administrator account."
	PS C:\> $vm | Add-AzureProvisioningConfig -Windows -AdminUsername $cred.GetNetworkCredential().Username -Password $cred.
	GetNetworkCredential().Password


	AvailabilitySetName               :
	ConfigurationSets                 : PSTest,Microsoft.WindowsAzure.Commands.ServiceManagement.Model.NetworkConfigurationSet}
	DataVirtualHardDisks              : {}
	Label                             : PSTest
	OSVirtualHardDisk                 : Microsoft.WindowsAzure.Commands.ServiceManagement.Model.OSVirtualHardDisk
	RoleName                          : PSTest
	RoleSize                          : Medium
	RoleType                          : PersistentVMRole
	WinRMCertificate                  :
	X509Certificates                  : {}
	NoExportPrivateKey                : False
	NoRDPEndpoint                     : False
	NoSSHEndpoint                     : False
	DefaultWinRmCertificateThumbprint :
	ProvisionGuestAgent               : True
	ResourceExtensionReferences       : {BGInfo}
	DataVirtualHardDisksToBeDeleted   :
	VMImageInput                      :

	PS C:\> New-AzureVM -ServiceName $csName -Location $locName -VMs $vm
	VERBOSE: 3:01:46 PM - Begin Operation: New-AzureVM - Create Deployment with VM PSTest
	VERBOSE: 3:02:49 PM - Completed Operation: New-AzureVM - Create Deployment with VM PSTest

	OperationDescription                    OperationId                            OperationStatus
	--------------------                    -----------                            --------------
	New-AzureVM                             8072cbd1-4abe-9278-9de2-8826b56e9221   Succeeded

## Display information about a virtual machine
This is a basic task you'll use often. Use it to get information about a VM, perform tasks on a VM, or get output to store in a variable.

To get info about the VM, run this command, replacing everything in the quotes, including the < and > characters:

     Get-AzureVM -ServiceName "<cloud service name>" -Name "<virtual machine name>"

To store the output in a $vm variable, run:

    $vm = Get-AzureVM -ServiceName "<cloud service name>" -Name "<virtual machine name>"

## Log on to a Windows-based virtual machine

Run these commands:

	$svcName="<cloud service name>"
	$vmName="<virtual machine name>"
	$localPath="<drive and folder location to store the downloaded RDP file, example: c:\temp >"
	$localFile=$localPath + "\" + $vmname + ".rdp"
	Get-AzureRemoteDesktopFile -ServiceName $svcName -Name $vmName -LocalPath $localFile -Launch

>[AZURE.NOTE] You can get the virtual machine and cloud service name from the display of the **Get-AzureVM** command.

## Stop a VM

Run this command:

    Stop-AzureVM -ServiceName "<cloud service name>" -Name "<virtual machine name>"

>[AZURE.IMPORTANT] Use the **StayProvisioned** parameter to keep the virtual IP (VIP) of the cloud service in case it's the last VM in that cloud service. If you use this parameter, you'll still be billed for the VM.

## Start a VM

Run this command:

    Start-AzureVM -ServiceName "<cloud service name>" -Name "<virtual machine name>"

## Attach a data disk
This task requires a few steps. First, you use the **Add-AzureDataDisk** cmdlet to add the disk to the $vm object. Then you use Update-AzureVM cmdlet to update the configuration of the VM.

You'll also need to decide whether to attach a new disk or one that contains data. For a new disk, the command creates the .vhd file and attaches it in the same command.

To attach a new disk, run this command:

    Add-AzureDataDisk -CreateNew -DiskSizeInGB <disk size> -DiskLabel "<label name>" -LUN <LUN number> -VM $vm | Update-AzureVM

To attach an existing data disk, run this command:

    Add-AzureDataDisk -Import -DiskName "<existing disk name>" -LUN <LUN number> | Update-AzureVM

To attach data disks from an existing .vhd file in blob storage, run this command:

    $diskLoc="https://mystorage.blob.core.chinacloudapi.cn/mycontainer/" + "<existing disk name>" + ".vhd"
	Add-AzureDataDisk -ImportFrom -MediaLocation  $diskLoc -DiskLabel "<label name>" -LUN <LUN number> | Update-AzureVM

## Additional resources

[Create a Windows virtual machine with Resource Manager and Azure PowerShell](/documentation/articles/virtual-machines-create-windows-powershell-resource-manager)

[Create a Windows virtual machine with a Resource Manager template and Azure PowerShell](/documentation/articles/virtual-machines-create-windows-powershell-resource-manager-template-simple)

[Virtual Machines documentation](/documentation/services/virtual-machines/)

[How to install and configure Azure PowerShell](/documentation/articles/install-configure-powershell)

[Use Azure PowerShell to create and preconfigure Windows-based virtual machines](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)
