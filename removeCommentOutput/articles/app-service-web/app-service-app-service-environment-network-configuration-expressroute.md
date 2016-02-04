<properties 
	pageTitle="Network Configuration Details for Working with Express Route" 
	description="Network configuration details for running Azure Websites Environments in a Virtual Networks connected to an ExpressRoute Circuit." 
	services="app-service" 
	documentationCenter="" 
	authors="stefsch" 
	manager="nirma" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="10/23/2015"
	wacn.date=""/>	

# Network Configuration Details for Azure Websites Environments with ExpressRoute 

## Overview ##
Customers can connect an [Azure ExpressRoute][ExpressRoute] circuit to their virtual network infrastructure, thus extending their on-premises network to Azure.  An Azure Websites Environment can  be created in a subnet of this [virtual network][virtualnetwork] infrastructure.  Apps running on the Azure Websites Environment can then establish secure connections to back-end resources accessible only over the ExpressRoute connection.  

**Note:**  An Azure Websites Environment cannot be created in a "v2" virtual network.  Azure Websites Environments are currently only supported in classic "v1" virtual networks.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Required Network Connectivity ##
There are network connectivity requirements for Azure Websites Environments that may not be initially met in a virtual network connected to an ExpressRoute.  Azure Websites Environments require all of the following in order to function properly:


-  Outbound network connectivity to Azure Storage endpoints worldwide.  This includes endpoints located in the same region as the Azure Websites Environment, as well as storage endpoints located in **other** Azure regions.  Azure Storage endpoints resolve under the following DNS domains: *table.core.chinacloudapi.cn*, *blob.core.chinacloudapi.cn*, *queue.core.chinacloudapi.cn* and *file.core.chinacloudapi.cn*.  
-  Outbound network connectivity to Sql DB endpoints located in the same region as the Azure Websites Environment.  SQl DB endpoints resolve under the following domain:  *database.chinacloudapi.cn*.
-  Outbound network connectivity to the Azure management plane endpoints (both ASM and ARM endpoints).  This includes outbound connectivity to both *management.core.chinacloudapi.cn* and *management.azure.com*. 
-  Outbound network connectivity to *ocsp.msocsp.com*.  This is needed to support SSL functionality.
-  The DNS configuration for the virtual network must be capable of resolving all of the endpoints and domains mentioned in the earlier points.  If these endpoints cannot be resolved, Azure Websites Environment creation attempts will fail, and existing Azure Websites Environments will be marked as unhealthy.
-  If a custom DNS server exists on the other end of a VPN gateway, the DNS server must be reachable from the subnet containing the Azure Websites Environment. 
-  The outbound network path cannot travel through internal corporate proxies, nor can it be force tunneled to on-premises.  Doing so changes the effective NAT address of outbound network traffic from the Azure Websites Environment.  Changing the NAT address of an Azure Websites Environment's outbound network traffic will cause connectivity failures to many of the endpoints listed above.  This results in failed Azure Websites Environment creation attempts, as well as previously healthy Azure Websites Environments being marked as unhealthy.  
-  Inbound network access to required ports for Azure Websites Environments must be allowed as described in this [article][requiredports].

The DNS requirements can be met by ensuring a valid DNS infrastructure is configured and maintained for the virtual network.  If for any reason the DNS configuration is changed after an Azure Websites Environment has been created, developers can force an Azure Websites Environment to pick up the new DNS configuration.  Triggering a rolling environment reboot using the "Restart" icon located at the top of the Azure Websites Environment management blade in the [Azure Management Portal][NewPortal] will cause the environment to pick up the new DNS configuration.

The inbound network access requirements can be met by configuring a [network security group][NetworkSecurityGroups] on the Azure Websites Environment's subnet to allow the required access as described in this [article][requiredports].

## Enabling Outbound Network Connectivity for an Azure Websites Environment##
By default, a newly created ExpressRoute circuit advertises a default route that allows outbound Internet connectivity.  With this configuration an Azure Websites Environment will be able to connect to other Azure endpoints.

However a common customer configuration is to define their own default route (0.0.0.0/0) which forces outbound Internet traffic to instead flow on-premises.  This traffic flow invariably breaks Azure Websites Environments because the outbound traffic is either blocked on-premises, or NAT'd to an unrecognizable set of addresses that no longer work with various Azure endpoints.

The solution is to define one (or more) user defined routes (UDRs) on the subnet that contains the Azure Websites Environment.  A UDR defines subnet-specific routes that will be honored instead of the default route.

If possible, it is recommended to use the following configuration:

- The ExpressRoute configuration advertises 0.0.0.0/0 and by default force tunnels all outbound traffic on-premises.
- The UDR applied to the subnet containing the Azure Websites Environment defines 0.0.0.0/0 with a next hop type of Internet (an example of this is farther down in this article).

The combined effect of these steps is that the subnet level UDR will take precedence over the ExpressRoute forced tunneling, thus ensuring outbound Internet access from the Azure Websites Environment.

**IMPORTANT:**  The routes defined in a UDR **must** be specific enough to  take precedence over any routes advertised by the ExpressRoute configuration.  The example below uses the broad 0.0.0.0/0 address range, and as such can potentially be accidentally overridden by route advertisements using more specific address ranges.

**VERY IMPORTANT:**  Azure Websites Environments are not supported with ExpressRoute configurations that **incorrectly cross-advertise routes from the public peering path to the private peering path**.  ExpressRoute configurations that have public peering configured, will receive route advertisements from Microsoft for a large set of Windows Azure IP address ranges.  If these address ranges are incorrectly cross-advertised on the private peering path, the end result is that all outbound network packets from the Azure Websites Environment's subnet will be incorrectly force-tunneled to a customer's on-premises network infrastructure.  This network flow will break Azure Websites Environments.  The solution to this problem is to stop cross-advertising routes from the public peering path to the private peering path.

Background information on user defined routes is available in this [overview][UDROverview].  

Details on creating and configuring user defined routes is available in this [How To Guide][UDRHowTo].

## Example UDR Configuration for an Azure Websites Environment ##

**Pre-requisites**

1. Install the very latest Azure Powershell from the [Azure Downloads page][AzureDownloads] (dated June 2015 or later).  Under "Command-line tools" there is an "Install" link under "Windows Powershell" that will install the latest Powershell cmdlets.

2. It is recommended that a unique subnet is created for exclusive use by an Azure Websites Environment.  This ensures that the UDRs applied to the subnet will only open outbound traffic for the Azure Websites Environment.
3. **Important**:  do not deploy the Azure Websites Environment until **after** the following configuration steps are followed.  This ensures that outbound network connectivity is available before attempting to deploy an Azure Websites Environment.

**Step 1:  Create a named route table**

The following snippet creates a route table called "DirectInternetRouteTable" in the China North Azure region:

    New-AzureRouteTable -Name 'DirectInternetRouteTable' -Location uswest

**Step 2:  Create one or more routes in the route table**

You will need to add one or more routes to the route table in order to enable outbound Internet access.  

The recommended approach for configuring outbound access to the Internet is to define a route for 0.0.0.0/0 as shown below.
  
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 0' -AddressPrefix 0.0.0.0/0 -NextHopType Internet

Remember that 0.0.0.0/0 is a broad address range, and as such will be overriden by more specific address ranges advertised by the ExpressRoute.  To re-iterate the earlier recommendation, a UDR with a 0.0.0.0/0 route should be used in conjunction with an ExressRoute configuration that only advertises 0.0.0.0/0 as well. 

As an alternative, you can download a comprehensive and updated list of CIDR ranges in use by Azure.  The Xml file containing all of the Azure IP address ranges is available from the [Microsoft Download Center][DownloadCenterAddressRanges].  

Note though that these ranges change over time, thus necessitating periodic manual updates to a UDR to keep in sync.  Also, since there is an upper limit of 100 routes in a single UDR, you will need to "summarize" the Azure IP address ranges to fit within the 100 route limit, keeping in mind that UDR defined routes need to be more specific than the routes advertised by your ExpressRoute.   


**Step 3:  Associate the route table to the subnet containing the Azure Websites Environment**

The last  configuration step is to associate the route table to the subnet where the Azure Websites Environment will be deployed.  The following command associates the "DirectInternetRouteTable" to the "ASESubnet" that will eventually contain an Azure Websites Environment.

    Set-AzureSubnetRouteTable -VirtualNetworkName 'YourVirtualNetworkNameHere' -SubnetName 'ASESubnet' -RouteTableName 'DirectInternetRouteTable'


**Step 4:  Final Steps**

Once the route table is bound to the subnet, it is recommended to first test and confirm the intended effect.  For example, deploy a virtual machine into the subnet and confirm that:


- Outbound traffic to both Azure and non-Azure endpoints mentioned earlier in this article is **not** flowing down the ExpressRoute circuit.  It is very important to verify this behavior, since if outbound traffic from the subnet is still being forced tunneled on-premises, Azure Websites Environment creation will always fail. 
- DNS lookups for the endpoints mentioned earlier are all resolving properly. 

Once the above steps are confirmed, you will need to delete the virtual machine because the subnet needs to be "empty" at the time the Azure Websites Environment is created.
 
Then proceed with creating an Azure Websites Environment!

## Getting started

To get started with Azure Websites Environments, see [Introduction to Azure Websites Environment][IntroToAppServiceEnvironment]

For more information about the Azure Websites platform, see [Azure Websites][AzureAppService].

<!-- LINKS -->
[virtualnetwork]: http://azure.microsoft.com/services/networking/
[ExpressRoute]: http://azure.microsoft.com/services/expressroute/
[requiredports]: /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[UDROverview]: /documentation/articles/virtual-networks-udr-overview/
[UDRHowTo]: /documentation/articles/virtual-networks-udr-how-to/
[HowToCreateAnAppServiceEnvironment]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[AzureDownloads]: /downloads/ 
[DownloadCenterAddressRanges]: http://www.microsoft.com/download/details.aspx?id=41653  
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[AzureAppService]: /documentation/articles/app-service-value-prop-what-is/
[IntroToAppServiceEnvironment]:  /documentation/articles/app-service-app-service-environment-intro/
[NewPortal]:  https://manage.windowsazure.cn
 

<!-- IMAGES -->
