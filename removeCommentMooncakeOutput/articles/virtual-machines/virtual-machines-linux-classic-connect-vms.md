<properties
	pageTitle="Connect Linux VMs in a cloud service | Azure"
	description="Connect Linux virtual machines created with the classic deployment model to an Azure cloud service or virtual network."
	services="virtual-machines-linux"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="03/24/2016"
	wacn.date=""/>

# Connect Linux virtual machines created with the classic deployment model with a virtual network or cloud service

> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the Resource Manager model.

Linux virtual machines created with the classic deployment model are always placed in a cloud service. The cloud service acts as a container and provides a unique public DNS name, a public IP address, and a set of endpoints to access the virtual machine over the Internet. The cloud service can be in a virtual network, but that's not a requirement. You can also [connect Windows virtual machines with a virtual network or cloud service](/documentation/articles/virtual-machines-windows-classic-connect-vms/).

If a cloud service isn't in a virtual network, it's called a *standalone* cloud service. The virtual machines in a standalone cloud service can only communicate with other virtual machines by using the other virtual machines' public DNS names, and the traffic travels over the Internet. If a cloud service is in a virtual network, the virtual machines in that cloud service can communicate with all other virtual machines in the virtual network without sending any traffic over the Internet.

If you place your virtual machines in the same standalone cloud service, you can still use load balancing and availability sets. For details, see [Load balancing virtual machines](/documentation/articles/virtual-machines-linux-load-balance/) and [Manage the availability of virtual machines](/documentation/articles/virtual-machines-linux-manage-availability/). However, you can't organize the virtual machines on subnets or connect a standalone cloud service to your on-premises network. Here's an example:

[AZURE.INCLUDE [virtual-machines-common-classic-connect-vms](../includes/virtual-machines-common-classic-connect-vms.md)]

## Next steps

After you create a virtual machine, it's a good idea to [add a data disk](/documentation/articles/virtual-machines-linux-classic-attach-disk/) so your services and workloads have a location to store data. 



