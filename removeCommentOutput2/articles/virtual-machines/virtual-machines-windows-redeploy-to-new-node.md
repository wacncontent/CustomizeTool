
<properties 
	pageTitle="Redeploy Windows virtual machines | Azure" 
	description="Describes how to redeploy Windows virtual machines to mitigate RDP connection issues." 
	services="virtual-machines-windows" 
	documentationCenter="virtual-machines" 
	authors="iainfoulds" 
	manager="timlt"
	tags="azure-resource-manager,top-support-issue" 
/>
	

<tags
	ms.service="virtual-machines-windows"
	ms.date="06/28/2016"
	wacn.date=""/>


# Redeploy virtual machine to new Azure node

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the Resource Manager deployment model, which Azure recommends for most new deployments instead of the classic deployment model.

If you have been facing difficulties troubleshooting Remote Desktop (RDP) connection or application access to Windows-based Azure virtual machine (VM), redeploying the VM may help. When you redeploy a VM, it moves the VM to a new node within the Azure infrastructure and then powers it back on, retaining all your configuration options and associated resources. This article shows you how to redeploy a VM using Azure PowerShell or the Azure portal.
> [AZURE.NOTE] After you redeploy a VM, the temporary disk will be lost and dynamic IP addresses associated with virtual network interface will be updated. 
## Using Azure PowerShell
Make sure you have the latest Azure PowerShell 1.x installed on your machine. Please read [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for more information.
Use this Azure PowerShell command to redeploy your virtual machine:
	Set-AzureRmVM -Redeploy -ResourceGroupName $rgname -Name $vmname 
[AZURE.INCLUDE [virtual-machines-common-redeploy-to-new-node](../includes/virtual-machines-common-redeploy-to-new-node.md)]
## Next steps
You can find specific help on [troubleshooting RDP connections](/documentation/articles/virtual-machines-windows-troubleshoot-rdp-connection/) or [detailed RDP troubleshooting steps](/documentation/articles/virtual-machines-windows-detailed-troubleshoot-rdp/) if you are having issues connecting to your VM. You can also read [application troubleshooting issues](/documentation/articles/virtual-machines-windows-troubleshoot-app-connection/) if you cannot access an application running on your VM.