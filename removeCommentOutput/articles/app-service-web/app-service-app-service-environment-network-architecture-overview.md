<properties 
	pageTitle="Network Architecture Overview of Azure Environments" 
	description="Architectural overview of network topology ofAzure Environments." 
	services="app-service" 
	documentationCenter="" 
	authors="stefsch" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="12/17/2015"
	wacn.date=""/>	

# Network Architecture Overview of Azure Environments

## Introduction ##
Azure Environments are always created within a subnet of a [virtual network][virtualnetwork] - apps running in an Azure Environment can communicate with private endpoints located within the same virtual network topology.  Since customers may lock down parts of their virtual network infrastructure, it is important to understand the types of network communication flows that occur with an Azure Environment.

## General Network Flow ##
 
An Azure Environment always has a public virtual IP address (VIP).  All inbound traffic arrives on that public VIP including HTTP and HTTPS traffic for apps, as well as other traffic for FTP, remote debugging functionality, and Azure management operations.  For a full list of the specific ports (both required and optional) that are available on the public VIP see the article on [controlling inbound traffic][controllinginboundtraffic] to an Azure Environment. 

The diagram below shows an overview of the various inbound and outbound network flows:

![General Network Flows][GeneralNetworkFlows]

An Azure Environment can communicate with a variety of private customer endpoints.  For example, apps running in the Azure Environment can connect to database server(s) running on IaaS virtual machines in the same virtual network topology.

[AZURE.IMPORTANT] Looking at the network diagram, the "Other Computer Resources" are deployed in a different Subnet from the Azure Environment. Deploying resources in the same Subnet with the ASE will block connectivity from ASE to those resources (except for specific intra-ASE routing). Deploy to a different Subnet instead (in the same VNET). The Azure Environment will then be able to connect. No additional configuration is necessary.

Azure Environments also communicate with Sql DB and Azure Storage resources necessary for managing and operating an Azure Environment.  Some of the Sql and Storage resources that an Azure Environment communicates with are located in the same region as the Azure Environment, while others are located in remote Azure regions.  As a result, outbound connectivity to the Internet is always required for an Azure Environment to function properly. 

Since an Azure Environment is deployed in a subnet, network security groups can be used to control inbound traffic to the subnet.  For details on how to control inbound traffic to an Azure Environment, see the following [article][controllinginboundtraffic].

For details on how to allow outbound Internet connectivity from an Azure Environment, see the following article about working with [Express Route][ExpressRoute].  The same approach described in the article applies when working with Site-to-Site connectivity and using forced tunneling.

## Outbound Network Addresses ##
When an Azure Environment makes outbound calls, an IP Address is always associated with the outbound calls.  The specific IP address that is used depends on whether the endpoint being called is located within the virtual network topology, or outside of the virtual network topology.

If the endpoint being called is **outside** of the virtual network topology, then the outbound address (aka the outbound NAT address) that is used is the public VIP of the Azure Environment.  This address can be found in the portal user interface for the Azure Environment in Properties blade.
 
![Outbound IP Address][OutboundIPAddress]

This address can also be determined by creating an app in the Azure Environment, and then performing an *nslookup* on the app's address. The resultant IP address is both the public VIP, as well as the Azure Environment's outbound NAT address.

If the endpoint being called is **inside** of the virtual network topology, the outbound address of the calling app will be the internal IP address of the individual compute resource running the app.  However there is not a persistent mapping of virtual network internal IP addresses to apps.  Apps can move around across different compute resources, and the pool of available compute resources in an Azure Environment can change due to scaling operations.

However, since an Azure Environment is always located within a subnet, you are guaranteed that the internal IP address of a compute resource running an app will always lie within the CIDR range of the subnet.  As a result, when fine-grained ACLs or network security groups are used to secure access to other endpoints within the virtual network, the subnet range containing the Azure Environment needs to be granted access.

The following diagram shows these concepts in more detail:

![Outbound Network Addresses][OutboundNetworkAddresses]

In the above diagram:

- Since the public VIP of the Azure Environment is 192.23.1.2, that is the outbound IP address used when making calls to "Internet" endpoints.
- The CIDR range of the containing subnet for the Azure Environment is 10.0.1.0/26.  Other endpoints within the same virtual network infrastructure will see calls from apps as originating from somewhere within this address range.

## Calls Between Azure Environments ##
A more complex scenario can occur if you deploy multiple Azure Environments in the same virtual network, and make outbound calls from one Azure Environment to another Azure Environment.  These types of cross Azure Environment calls will also be treated as "Internet" calls.

The following diagram shows an example of a layered architecture with apps on one Azure Environment (e.g. "Front door" web apps) calling apps on a second Azure Environment (e.g. internal back-end API apps not intended to be accessible from the Internet). 

![Calls Between Azure Environments][CallsBetweenAppServiceEnvironments] 

In the example above the Azure Environment "ASE One" has an outbound IP address of 192.23.1.2.  If an app running on this Azure Environment makes an outbound call to an app running on a second Azure Environment ("ASE Two") located in the same virtual network, the outbound call will be treated as an "Internet" call.  As a result the network traffic arriving on the second Azure Environment will show as originating from 192.23.1.2 (i.e. not the subnet address range of the first Azure Environment).

Even though calls between different Azure Environments are treated as "Internet" calls, when both Azure Environments are located in the same Azure region the network traffic will remain on the regional Azure network and will not physically flow over the public Internet.  As a result you can use a network security group on the subnet of the second Azure Environment to only allow inbound calls from the first Azure Environment (whose outbound IP address is 192.23.1.2), thus ensuring secure communication between the Azure Environments.

## Additional Links and Information ##
Details on inbound ports used by Azure Environments and using network security groups to control inbound traffic is available [here][controllinginboundtraffic].

Details on using user defined routes to grant outbound Internet access to Azure Environments is available in this [article][ExpressRoute]. 


<!-- LINKS -->
[virtualnetwork]: http://azure.microsoft.com/services/networking/
[controllinginboundtraffic]:  /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[ExpressRoute]:  /documentation/articles/app-service-app-service-environment-network-configuration-expressroute/

<!-- IMAGES -->
[GeneralNetworkFlows]: ./media/app-service-app-service-environment-network-architecture-overview/NetworkOverview-1.png
[OutboundIPAddress]: ./media/app-service-app-service-environment-network-architecture-overview/OutboundIPAddress-1.png
[OutboundNetworkAddresses]: ./media/app-service-app-service-environment-network-architecture-overview/OutboundNetworkAddresses-1.png
[CallsBetweenAppServiceEnvironments]: ./media/app-service-app-service-environment-network-architecture-overview/CallsBetweenEnvironments-1.png

