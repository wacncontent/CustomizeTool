<properties
   pageTitle="Create FQDN for a VM in Azure portal | Azure"
   description="Learn how to create a Fully Qualified Domain Name or FQDN for a Resource Manager based virtual machine in the Azure portal."
   services="virtual-machines-windows"
   documentationCenter=""
   authors="iainfoulds"
   manager="timlt"
   editor="tysonn"
   tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="06/07/2016"
	wacn.date=""/>

# Create a Fully Qualified Domain Name in the Azure portal  Preview 
When you create a virtual machine (VM) in the [Azure  portal](https://portal.azure.cn)  portal Preview](https://portal.azure.cn)  using the Resource Manager deployment model, a public IP resource for the virtual machine is automatically created. You can use this IP address to remotely access the VM. Although the portal does not create a [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name), or FQDN, by default, it is extremely easy to create one once the VM is created. This article demonstrates the steps to create a DNS name or FQDN.

[AZURE.INCLUDE [virtual-machines-common-portal-create-fqdn](../includes/virtual-machines-common-portal-create-fqdn.md)]

You can now connect remotely to the VM using this DNS name such as for Remote Desktop Protocol (RDP).

## Next steps
Now that your VM has a public IP and DNS name, you can deploy common application frameworks or services such as IIS, SQL, SharePoint, , etc.

You can also read more about [using Resource Manager](/documentation/articles/resource-group-overview/) for tips on building your Azure deployments.