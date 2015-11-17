<properties 
	pageTitle="Line of business application in Azure | Windows Azure" 
	description="Learn the value of a line of business application in Azure, set up a test environment, and deploy a high-availability configuration." 
	services="virtual-machines" 
	documentationCenter="" 
	authors="JoeDavies-MSFT" 
	manager="timlt" 
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="11/09/2015"
	wacn.date=""/>

# Azure Infrastructure Services Workload: High-availability line of business application
<!-- deleted by customization

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] classic deployment model.

-->

Set up your first or next web-based, intranet-only line of business application in Windows Azure and take advantage of ease of configuration and the ability to quickly expand the application to include new capacity.
 
With the Virtual Machines and Virtual Network features of Azure infrastructure services, you can quickly deploy and run a line of business application that is accessible by your organization's users. For example, you can set this up.

![](./media/virtual-machines-workload-high-availability-LOB-application/workload-lobapp-phase4.png)
 
Because the Azure Virtual Network is an extension of your on-premises network with all of the correct naming and traffic routing in place, your users will access the servers of the line of business application in the same way as if it were located in an on-premises datacenter.

This configuration allows you to easily expand the capacity of the application by adding new Azure virtual machines in which the ongoing costs of both hardware and maintenance are lower than running the equivalent in your datacenter.

Your next step is to set up a dev/test line of business application hosted in Azure.

## Create a dev/test line of business application hosted in Azure

A cross-premises virtual network is connected to an on-premises network with a site-to-site VPN or ExpressRoute connection. If you want to create a dev/test environment that mimics the final configuration and experiment with accessing the application and performing remote administration over a VPN connection, see [Set up a web-based LOB application in a hybrid cloud for testing](/documentation/articles/virtual-networks-setup-lobapp-hybrid-cloud-testing). 

![](./media/virtual-machines-workload-high-availability-LOB-application/CreateLOBAppHybridCloud_3.png)
 
You can create this dev/test environment for free with your [MSDN subscription](/pricing/member-offers/msdn-benefits/) or an [Azure Trial Subscription](/pricing/1rmb-trial/).

Your next step is to create a high-availability line of business application in Azure.

## Deploy a line of business application hosted in Azure

The baseline, representative configuration for a high-availability line of business application in Azure looks like this.

![](./media/virtual-machines-workload-high-availability-LOB-application/workload-lobapp-phase4.png)
 
This consists of:

- An intranet-only line of business application with two servers at the web and database tiers.
- A SQL Server AlwaysOn configuration with two virtual machines running SQL Server and a majority node computer in a cluster.
- Active Directory Domain Services in the virtual network with two replica domain controllers.

For an overview of line of business applications, see the [Line of Business Applications architecture blueprint](http://msdn.microsoft.com/dn630664).

### Bill of materials

This baseline configuration requires the following set of Azure services and components:

- Seven virtual machines
- Four extra data disks for the domain controllers and virtual machines running SQL Server
- Three availability sets
- One cross-premises virtual network
- Two storage accounts

Here are the virtual machines and thier default sizes for this configuration.

Item | Virtual machine description | Gallery image | Default size 
--- | --- | --- | --- 
1. | First domain controller | Windows Server 2012 R2 Datacenter | D1
2. | Second domain controller | Windows Server 2012 R2 Datacenter | D1
3. | Primary database server | Microsoft SQL Server 2014 Enterprise – Windows Server 2012 R2 | D4
4. | Secondary database server | Microsoft SQL Server 2014 Enterprise – Windows Server 2012 R2 | D4
5. | Majority node for the cluster | Windows Server 2012 R2 Datacenter | D1
6. | First web server | Windows Server 2012 R2 Datacenter | D3
7. | Second web server | Windows Server 2012 R2 Datacenter | D3

To compute the estimated costs for this configuration, see the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/). 

1. In **Modules**, click **Compute**, and then click **Virtual Machines** enough times to create a list of seven virtual machines.
2. For each virtual machine, select:
	- Your intended region
	- **Windows** for the type
	- **Standard** for the pricing tier
	- The default size in the previous table or your intended size for the **Instance size**

> [AZURE.NOTE] The Azure Pricing Calculator does not include the additional costs for the SQL Server license for the two virtual machines running SQL Server 2014 Enterprise. See [Virtual Machines Pricing-SQL](/home/features/virtual-machines/#price) for more information.

### Deployment phases

To deploy this configuration, use the following process:

- Phase 1: Configure Azure 

	Use Azure PowerShell to create the storage accounts, availability sets, and a cross-premises virtual network. For the detailed configuration steps, see [Phase 1](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-phase1).

- Phase 2: Configure the domain controllers 

	Configure two Active Directory replica domain controllers and DNS settings for the virtual network. For the detailed configuration steps, see [Phase 2](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-phase2).

- Phase 3: Configure the SQL Server infrastructure.  

	Create the virtual machines running SQL Server and the cluster. For the detailed configuration steps, see [Phase 3](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-phase3).

- Phase 4: Configure the web servers.

	Create the web server virtual machines and add your line of business application to it. For the detailed configuration, see [Phase 4](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-phase4).

- Phase 5: Configure a SQL Server AlwaysOn Availability Group.

	Prepare the application databases, create a SQL Server AlwaysOn Availability Group, and then add the application databases to it. For the detailed configuration steps, see [Phase 5](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-phase5).

Once configured, you can easily expand this line of business application by adding more web servers or virtual machines running SQL Servers to the cluster.

## Additional resources

[Deploy a high-availability line of business application in Azure](/documentation/articles/virtual-machines-workload-high-availability-LOB-application-overview)

[Line of Business Applications architecture blueprint](http://msdn.microsoft.com/dn630664)

[Set up a web-based LOB application in a hybrid cloud for testing](/documentation/articles/virtual-networks-setup-lobapp-hybrid-cloud-testing)

[Azure infrastructure services implementation guidelines](/documentation/articles/virtual-machines-infrastructure-services-implementation-guidelines)

[Azure Infrastructure Services Workload: SharePoint Server 2013 farm](/documentation/articles/virtual-machines-workload-intranet-sharepoint-farm)
