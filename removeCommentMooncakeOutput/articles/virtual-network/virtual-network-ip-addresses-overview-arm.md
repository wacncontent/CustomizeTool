<!-- not suitable for Mooncake -->

<properties
   pageTitle="Public and private IP addressing in Azure Resource Manager | Windows Azure"
   description="Learn about public and private IP addressing in Azure Resource Manager"
   services="virtual-network"
   documentationCenter="na"
   authors="telmosampaio"
   manager="carmonm"
   editor="tysonn"
   tags="azure-resource-manager" />
<tags
	ms.service="virtual-network"
	ms.date="01/12/2015"
	wacn.date=""/>

# IP addresses in Azure
You can assign IP addresses to Azure resources to communicate with other Azure resources, your on-premises network, and the Internet. There are two types of IP addresses you can use in Azure: public and private.

Public IP addresses are used for communication with the Internet, including Azure public-facing services.

Private IP addresses are used for communication within an Azure virtual network (VNet), and your on-premises network when you use ExpressRoute circuit to extend your network to Azure.

[AZURE.INCLUDE [azure-arm-classic-important-include](../includes/learn-about-deployment-models-rm-include.md)] [classic deployment model](/documentation/articles/virtual-network-ip-addresses-overview-classic).

If you are familiar with the classic deployment model, check the [differences in IP addressing between classic and Resource Manager](/documentation/articles/virtual-network-ip-addresses-overview-classic#Differences-between-Resource-Manager-and-classic-deployments).

## Public IP addresses
Public IP addresses allow Azure resources to communicate with Internet and Azure public-facing services such as [Azure Redis Cache](/home/features/cache), [Azure Event Hubs](/home/features/event-hubs), [SQL databases](/documentation/articles/sql-database-technical-overview), and [Azure storage](/documentation/articles/storage-introduction).

In Azure Resource Manager, a [public IP](/documentation/articles/resource-groups-networking#public-ip-address) address is a resource that has its own properties. You can associate a public IP address resource with any of the following resources:

- VMs
- Application gateways

### Allocation method
There are two methods in which an IP address is allocated to a *public IP resource* - *dynamic* or *static*. The default allocation method is *dynamic*, where an IP address is **not** allocated at the time of its creation. Instead, the public IP address is allocated when you start (or create) the associated resource (like VM or Load balancer). The IP address is released when you stop (or delete) the resource. This causes the IP address to change when you stop and start a resource.

To ensure the IP address for the associated resource remains the same, you can set the allocation method explicitly to *static*. In this case an IP address is assigned immediately. It is released only when you delete the resource or change its allocation method to *dynamic*.

>[AZURE.NOTE] Even when you set the allocation method to *static*, you cannot specify the actual IP address assigned to the *public IP resource*. Instead, it gets allocated from a pool of available IP addresses in the Azure location the resource is created.

Static public IP addresses are commonly used in the following scenarios:

- end-users need to update firewall rules to communicate with your Azure resources.
- DNS name resolution, where a change in IP address would require updating A records.
- your Azure resources communicate with other apps or services that use an IP address based security model.
- you use SSL certificates linked to an IP address.

>[AZURE.NOTE] The list of IP ranges from which public IP addresses (dynamic/static) are allocated to Azure resources is published at [Azure Datacenter IP ranges](https://www.microsoft.com/download/details.aspx?id=41653).

### DNS hostname resolution
You can specify a DNS domain name label for a public IP resource, which creates a mapping for *domainnamelabel*.*location*.chinacloudapp.cn to the public IP address in the Azure-managed DNS servers. For instance, if you create a public IP resource with **contoso** as a *domainnamelabel* in the **China North** Azure *location*, the fully-qualified domain name (FQDN) **contoso.chinanorth.chinacloudapp.cn** will resolve to the public IP address of the resource. You can use this FQDN to create a custom domain CNAME record pointing to the public IP address in Azure.

>[AZURE.IMPORTANT] Each domain name label created must be unique within its Azure location.  

### VMs
You can associate a Public IP address with a [Virtual machine](/documentation/articles/virtual-machines-about) (VM) by assigning it to its **network interface card** (NIC). In case of a multi-NIC VM, you can assign it to the *primary* NIC only. You can assign either a dynamic or a static public IP address to a VM.

### Internet facing load balancers
You can associate a public IP address with an [Azure Load Balancer](/documentation/articles/load-balancer-overview), by assigning it to the load balancer **front end** configuration. This public IP address serves as a load-balanced virtual IP address (VIP). You can assign either a dynamic or a static public IP address to a load balancer front end. You can also assign multiple public IP addresses to a load balancer front end, which enables [multi-vip](/documentation/articles/load-balancer-multivip) scenarios like a multi-tenant environment with SSL-based websites.


### Application gateways
You can associate a public IP address with an Azure [Application gateway](/documentation/articles/application-gateway-introduction), by assigning it to gateway's **front end** configuration. This public IP address serves as a load-balanced VIP. Currently, you can only assign a *dynamic* public IP address to an application gateway front end configuration. You can also assign multiple public IP addresses, which enables multi-vip scenarios.

### At-a-glance
The table below shows each resource type with the possible allocation methods (dynamic/static), and ability to assign multiple public IP addresses.

|Resource|Dynamic|Static|Multiple IP addresses|
|---|---|---|---|
|Application gateway front end|Yes|No|No|

## Private IP addresses
Private IP addresses allow Azure resources to communicate with other resources in a [virtual network](/documentation/articles/virtual-networks-overview)(VNet), or in on-premises network through ExpressRoute circuit, without using an Internet-reachable IP address.

In Azure Resource Manager deployment model, a private IP address is associated to various Azure resources.

- VMs
- Internal load balancers (ILBs)
- Application gateways

### Allocation method
A private IP address is allocated from the address range of the subnet to which the resource is attached. The address range of the subnet itself is a part of the VNet's address range.

There are two methods in which a private IP address is allocated: *dynamic* or *static*. The default allocation method is *dynamic*, where the IP address is automatically allocated from the resource's subnet (using DHCP). This IP address can change when you stop and start the resource.

You can set the allocation method to *static* to ensure the IP address remains the same. In this case, you also need to provide a valid IP address that is part of the resource's subnet.

Static private IP addresses are commonly used for:

- VMs that act as domain controllers or DNS servers.
- Resources that require firewall rules using IP addresses.
- Resources accessed by other apps/resources through an IP address.

### VMs
A private IP address is assigned to the **network interface card** (NIC) of a [Virtual machine](/documentation/articles/virtual-machines-about). In case of a multi-nic VM, each NIC gets a private IP address assigned. You can specify the allocation method either as a dynamic or static for a NIC.

#### Internal DNS hostname resolution (for VMs)
All Azure VMs are configured with [Azure-managed DNS servers](/documentation/articles/virtual-networks-name-resolution-for-vms-and-role-instances#azure-provided-name-resolution) by default, unless you explicitly configure custom DNS servers. These DNS servers provide internal name resolution for VMs that reside within the same VNet.

When you create a VM, a mapping for the hostname to its private IP address is added to the Azure-managed DNS servers. In case of a multi-NIC VM, the hostname is mapped to the private IP address of the primary NIC.

VMs configured with Azure-managed DNS servers will be able to resolve the hostnames of all VMs within their VNet to their private IP addresses.

### Internal load balancers (ILB) & Application gateways
You can assign a private IP address to the **front end** configuration of an [Azure Internal Load Balancer](/documentation/articles/load-balancer-internal-overview) (ILB) or an [Azure Application Gateway](/documentation/articles/application-gateway-introduction). This private IP address serves as an internal endpoint, accessible only to the resources within its virtual network (VNet) and the remote networks connected to the VNet. You can assign either a dynamic or static private IP address to the front end configuration. You can also assign multiple private IP addresses to enable multi-vip scenarios.

### At-a-glance
The table below shows each resource type with the possible allocation methods (dynamic/static), and ability to assign multiple private IP addresses.

|Resource|Static|Dynamic|Multiple IP addresses|
|---|---|---|---|
|Virtual Machine (VM)/Network Interface Card (NIC)|Yes|Yes|Yes|
|Internal Load balancer front end|Yes|Yes|Yes|
|Application gateway front end|Yes|Yes|Yes|

## Limits

The table below shows the limits imposed on IP addressing in Azure per region, per subscription. You can [contact support](https://manage.windowsazure.cn/#blade/Microsoft_Azure_Support/HelpAndSupportBlade) to increase the default limits up to the maximum limits based on your business needs.

||Default limit|Maximum limit|
|---|---|---|
|Public IP addresses (dynamic)|60|contact support|
|Public IP addresses (static)|20|contact support|
|Public front end IP per load balancer|5|contact support|
|Private front end IP per load balancer|1|contact support|

Make sure you read the full set of [limits for Networking](/documentation/articles/azure-subscription-service-limits#networking-limits) in Azure.

## Pricing

In most cases, public IP addresses are free. There is a nominal charge to use additional and/or static public IP addresses. Make sure you understand the [pricing structure for public IPs](/home/features/ip-addresses/#price).

In summary, the following pricing structure applies to public IP resources:

- VPN gateways and application gateways use only one dynamic public IP, which is free of cost.
- VMs use only one public IP, which is free as long as it is a dynamic IP address. If a VM uses a static public IP, it gets counted towards Static (Reserved) Public IP usage.
- Each load balancer can use multiple public IPs. The first public IP is free of cost. Additional dynamic IPs are charged at $0.004/hr. Static public IPs get counted towards Static (Reserved) Public IP usage.
- Static (Reserved) Public IP usage: 
	- First 5 (in-use) are free. Additional static public IPs are charged at $0.004/hr. 
	- Static public IPs not assigned to any resource are charged at $0.004/hr.
	- Usage is calculated based on the total number of static public IPs in the subscription.

## Next steps
- [Deploy a VM with a static public IP](/documentation/articles/virtual-network-deploy-static-pip-arm-portal) using the Azure Management Portal.
- Learn how to [deploy a VM with a static public IP using a template](/documentation/articles/virtual-network-deploy-static-pip-arm-template).
- [Deploy a VM with a static private IP address](/documentation/articles/virtual-networks-static-private-ip-arm-pportal) using the Azure Management Portal.
