
<properties 
	pageTitle="Redeploy Linux Virtual Machines | Azure" 
	description="Describes how to redeploy Linux virtual machines to mitigate SSH connection issues." 
	services="virtual-machines-linux" 
	documentationCenter="virtual-machines" 
	authors="iainfoulds" 
	manager="timlt"
	tags="azure-resource-manager,top-support-issue" 
/>
	

<tags
	ms.service="virtual-machines-linux"
	ms.date="06/28/2016"
	wacn.date=""/>

# Redeploy virtual machine to new Azure node

If you have been facing difficulties troubleshooting SSH or application access to an Azure virtual machine (VM), redeploying the VM may help. When you redeploy a VM, it moves the VM to a new node within the Azure infrastructure and then powers it back on, retaining all your configuration options and associated resources. This article shows you how to redeploy a VM using Azure CLI or the Azure portal.

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the Resource Manager deployment model, which Azure recommends for most new deployments instead of the classic deployment model.

> [AZURE.NOTE] After you redeploy a VM, the temporary disk will be lost and dynamic IP addresses associated with virtual network interface will be updated. 
## Using Azure CLI
Make sure you have the [latest Azure CLI installed](/documentation/articles/xplat-cli-install/) on your machine and you are in resource manager mode (`azure config mode arm`).
Use the following Azure CLI command to redeploy your virtual machine:
```bash
azure vm redeploy --resourcegroup <resourcegroup> --vm-name <vmname> 
```
You can see the status of the VM change as it goes through the redeploy process. The `PowerState` of the VM will go from 'Running' to 'Updating', then 'Starting', and finally 'Running' as it goes through the process of redeploying to a new host. Check the status of the VMs within a resource group with:
```bash
azure vm list -g <resourcegroup>
```
[AZURE.INCLUDE [virtual-machines-common-redeploy-to-new-node](../includes/virtual-machines-common-redeploy-to-new-node.md)]
## Next steps
You can find specific help on [troubleshooting SSH connections](/documentation/articles/virtual-machines-linux-troubleshoot-ssh-connection/) or [detailed SSH troubleshooting steps](/documentation/articles/virtual-machines-linux-detailed-troubleshoot-ssh-connection/) if you are having issues connecting to your VM. You can also read [application troubleshooting issues](/documentation/articles/virtual-machines-linux-troubleshoot-app-connection/) if you cannot access an application running on your VM.