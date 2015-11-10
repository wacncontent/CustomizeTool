<properties 
   pageTitle="Introduction to ExpressRoute | Windows Azure"
   description="This page provides an overview of the ExpressRoute service, including how an ExpressRoute connection works."
   documentationCenter="na"
   services="expressroute"
   authors="cherylmc"
   manager="carolz"
   editor=""/>
<tags
	ms.service="expressroute"
	ms.date="09/22/2015"
	wacn.date=""/>

# ExpressRoute technical overview

<!-- deleted by customization
Windows Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a dedicated private connection facilitated by a connectivity provider. With ExpressRoute, you can establish connections to Microsoft cloud services, such as Windows Azure, Office 365, and CRM Online. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a connectivity provider at a co-location facility. ExpressRoute connections do not go over the public Internet. This allows ExpressRoute connections to offer more reliability, faster speeds, lower latencies, and higher security than typical connections over the Internet.  

![](./media/expressroute-introduction/expressroute-basic.png)

**Key benefits include:**

- Layer 3 connectivity between your on-premises network and the Microsoft Cloud through a connectivity provider. Connectivity can be from an any-to-any (IPVPN) network, a point-to-point Ethernet connection, or through a virtual cross-connection via an Ethernet exchange.
- Connectivity to Microsoft cloud services across all regions in the geopolitical region.
- Global connectivity to Microsoft services across all regions with ExpressRoute premium add-on.
- Dynamic routing between your network and Microsoft over industry standard protocols (BGP).
- Built-in redundancy in every peering location for higher reliability.
- Connection uptime [SLA](http://azure.microsoft.com/support/legal/sla/).
- QoS and support for multiple classes of service for special applications, such as Skype for Business.

See the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs) for more details.

## How can I connect my network to Microsoft using ExpressRoute?

You can create a connection between your on-premises network and the Microsoft cloud in three different ways

1. **Co-located at a cloud exchange.** If you are co-located in a facility with a cloud exchange, you can order virtual cross-connections to the Microsoft cloud through the co-location provider’s Ethernet exchange. Co-location providers can offer either Layer 2 cross-connections, or managed Layer 3 cross-connections between your infrastructure in the co-location facility and the Microsoft cloud.
2.	**Point-to-point Ethernet connections.** You can connect your on-premises datacenters/offices to the Microsoft cloud through point-to-point Ethernet links. Point-to-point Ethernet providers can offer Layer 2 connections, or managed Layer 3 connections between your site and the Microsoft cloud.
3.	**Any-to-any (IPVPN) networks.** You can integrate your WAN with the Microsoft cloud. IPVPN providers (typically MPLS VPN) offer any-to-any connectivity between your branch offices and datacenters. The Microsoft cloud can be interconnected to your WAN to make it look just like any other branch office. WAN providers typically offer managed Layer 3 connectivity.

![](./media/expressroute-introduction/expressroute-connectivitymodels.png)

ExpressRoute capabilities and features are all identical across all of the above connectivity models. Connectivity providers can offer one or more connectivity models from the above list. You can work with your connectivity provider to pick the model that works best for you.

## ExpressRoute features

ExpressRoute supports the following features and capabilities. 

### Layer 3 connectivity

Microsoft uses industry standard dynamic routing protocol (BGP) to exchange routes between your on-premises network, your instances in Azure, and Microsoft public addresses.  We establish multiple BGP sessions with your network for different traffic profiles. More details can be found in the [ExpressRoute circuit and routing domains](/documentation/articles/expressroute-circuit-peerings) article.

### Redundancy

Each ExpressRoute circuit consists of two connections to two Microsoft Enterprise edge routers (MSEEs) from the connectivity provider / your network edge. Microsoft will require dual BGP connection from the connectivity provider / your side – one to each MSEE. You may choose not to deploy redundant devices / Ethernet circuits at your end. However, connectivity providers use redundant devices to ensure that your connections are handed off to Microsoft in a redundant manner. A redundant Layer 3 connectivity configuration is a requirement for our [SLA](http://azure.microsoft.com/support/legal/sla/) to be valid. 

### Connectivity to Microsoft cloud services

ExpressRoute connections enable access to the following services.

- Windows Azure services
- Microsoft Office 365 services
- Microsoft CRM Online services (coming soon) 
 
You can visit the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs) page for a detailed list of services supported over ExpressRoute.

### Connectivity to all regions within a geopolitical region

You can connect to Microsoft in one of our [peering locations](/documentation/articles/expressroute-locations) and have access to all regions within the geopolitical region. 

For example, if you connected to Microsoft in Amsterdam through ExpressRoute, you will have access to all Microsoft cloud services hosted in Northern Europe and Western Europe. Refer to the [ExpressRoute partners and peering locations](/documentation/articles/expressroute-locations) article for an overview of the geopolitical regions, associated Microsoft cloud regions, and corresponding ExpressRoute peering locations.

### Global connectivity with ExpressRoute premium add-on

You can enable the ExpressRoute premium add-on feature to extend connectivity across geopolitical boundaries. For example, if you are connected to Microsoft in Amsterdam through ExpressRoute, you will have access to all Microsoft cloud services hosted in all regions across the world (national clouds are excluded). You can access services deployed in South America or Australia the same way you access the North and West Europe regions.

### Rich connectivity partner ecosystem

ExpressRoute has a constantly growing ecosystem of connectivity providers and SI partners. You can refer to the [ExpressRoute providers and locations](/documentation/articles/expressroute-locations) article for the latest information.

### Connectivity to national clouds

Microsoft operates isolated cloud environments for special geopolitical regions and customer segments. Refer to the [ExpressRoute providers and locations](/documentation/articles/expressroute-locations) page for a list of national clouds and providers.

### Supported bandwidth options

You can purchase ExpressRoute circuits for a wide range of bandwidths. The list of supported bandwidths are listed below. Be sure to check with your connectivity provider to determine the list of supported bandwidths they provide.

- 50 Mbps
- 100 Mbps
- 200 Mbps
- 500 Mbps
- 1 Gbps
- 2 Gbps
- 5 Gbps
- 10 Gbps

### Dynamic scaling of bandwidth

You have the ability to increase the ExpressRoute circuit bandwidth (on a best effort basis) without having to tear down your connections. 

### Flexible billing models

You can pick a billing model that works best for you. Choose between the billing models listed below. Refer to the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs) page for more details. 

- **Unlimited data**. The ExpressRoute circuit is charged based on a monthly fee, and all inbound and outbound data transfer is included free of charge. 
- **Metered data**. The ExpressRoute circuit is charged based on a monthly fee. All inbound data transfer is free of charge. Outbound data transfer is charged per GB of data transfer. Data transfer rates vary by region.
- **ExpressRoute premium add-on**. The ExpressRoute premium is an add-on over the ExpressRoute circuit. The ExpressRoute premium add-on provides the following capabilities: 
	- Increased route limits for Azure public and Azure private peering from 4,000 routes to 10,000 routes.
	- Global connectivity for services. An ExpressRoute circuit created in any region (excluding national clouds) will have access to resources across any other region in the world. For example, a virtual network created in West Europe can be accessed through an ExpressRoute circuit provisioned in Silicon Valley.
	- Increased number of VNet links per ExpressRoute circuit from 10 to a larger limit, depending on the bandwidth of the circuit.

## Next steps

- Learn about ExpressRoute connections and routing domains. See [ExpressRoute circuits and routing domains](/documentation/articles/expressroute-circuit-peerings).
- Find a service provider. See [ExpressRoute partners and peering locations](/documentation/articles/expressroute-locations).
- Ensure that all prerequisites are met. See [ExpressRoute prerequisites](/documentation/articles/expressroute-prerequisites).
- Refer to the requirements for [Routing](/documentation/articles/expressroute-routing), [NAT](/documentation/articles/expressroute-nat) and [QoS](/documentation/articles/expressroute-qos).
- Configure your ExpressRoute connection.
	- [Create an ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic)
	- [Configure routing](/documentation/articles/expressroute-howto-routing-classic)
	- [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-classic)

-->
<!-- keep by customization: begin -->
Windows Azure ExpressRoute lets you create private connections between Microsoft datacenters and infrastructure that’s on your premises or in a co-location environment. With ExpressRoute, you can establish connections to Microsoft cloud services such as Windows Azure and Office 365 at an ExpressRoute partner co-location facility, or directly connect from your existing WAN network (such as a MPLS VPN provided by a network service provider).
 
ExpressRoute connections offer higher security, more reliability, faster speeds and lower latencies than typical connections over the Internet. In some cases, using ExpressRoute connections to transfer data between your on-premises network and Azure can also yield significant cost benefits. If you already have created a cross-premises connection from your on-premises network to Azure, you can migrate to an ExpressRoute connection while keeping your virtual network intact.

See the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs) for more details.

## How does an ExpressRoute connection work?

In order to connect your WAN to Windows cloud services, you must order a dedicated circuit and have it enabled through a connectivity provider. There are two connectivity provider types to choose from: direct layer 3 through an exchange provider (EXP), or layer 3 through a network service provider (NSP). You can choose to enable one or both types of connectivity between your WAN and the Microsoft cloud.  

## Exchange providers and network service providers
ExpressRoute providers are classified as Network Service Providers (NSPs) and Exchange providers (EXPs).

![](./media/expressroute-introduction/expressroute-nsp-exp.png)


|   |**Exchange Provider**|**Network Service Provider**|
|---|---|---|
|**Typical Connectivity model**| Point-to-point Ethernet links or Connectivity at a cloud exchange | Any-to-any connectivity through a telco VPN |
|**Supported Bandwidths**|200 Mbps, 500 Mbps, 1 Gbps and 10 Gbps|10 Mbps, 50 Mbps, 100 Mbps, 500 Mbps, 1 Gbps|
|**Connectivity Providers**|[Exchange Providers](/documentation/articles/expressroute-locations)|[Network Service Providers](/documentation/articles/expressroute-locations)|
|**Routing**|BGP sessions directly with customer edge routers| BGP sessions with telco|
|**Pricing**|[EXP pricing](/home/features/expressroute/#price)|[NSP pricing](/home/features/expressroute/#price)|

### Exchange providers (EXPs)
We partner with cloud exchange service providers such as Equinix and TeleCity group, and also with point-to-point connectivity service providers such as Cole and Level 3, to offer connectivity between Azure and the customer’s premises. We offer circuit bandwidths from 200 Mbps to 10 Gbps (200 Mbps, 500 Mbps, 1 Gbps and 10 Gbps).

If you want a direct layer 3 connection through an exchange provider, you can do this one of 3 ways:

- You can be co-located with the cloud exchanges such as Equinix's Cloud Exchange or TeleCity's Cloud IX in the locations we offer services in. In such cases you will order redundant connectivity to the cloud exchange. 
- You can work with providers such as Level 3 to have Ethernet circuits setup between your data centers and Microsoft. 
- You can work with your local connectivity provider to acquire redundant connectivity to the closest exchange provider facility and connect to the cloud exchange.

We do require you to have redundant connectivity me meet the requirements for our SLA. We do not support direct connectivity to the Microsoft edge. Dedicated circuits will always be enabled through an Ethernet provider or the local cloud exchange. While this sets up layer 2 connectivity between Microsoft and your network, we will not support extending the layer 2 domain. You must setup redundant routing sessions between your edge routers and the Microsoft edge routers to have layer 3 connectivity.

For more information about configuration and to see real-world examples, you can follow this step by step guidance: [Configure an ExpressRoute connection through an exchange provider](/documentation/articles/expressroute-configuring-exps).


### Network service providers (NSPs)

We partner with Telcos such as AT&T, and British Telecom to offer connectivity between Azure and your WAN. We offer circuit bandwidths from 10 Mbps to 1 Gbps (10 Mbps, 50 Mbps, 100 Mbps, 500 Mbps, 1 Gbps). 

If you use VPN services from any of the network service providers we partner with, they can extend the networks into Azure without having to deploy any new hardware or making major configuration changes to your existing networks.

For more information about configuration and to see real-world examples, you can follow this step by step guidance: [Configure an ExpressRoute connection through a network service provider](/documentation/articles/expressroute-configuring-nsps).

## ExpressRoute peerings
The figure below provides a logical representation of connectivity between your WAN and Microsoft. You must order a *dedicated circuit* to connect your WAN to Microsoft through a connectivity provider (NSP / EXP). A dedicated circuit represents a logical connection between your WAN and Microsoft through the connectivity provider. You may order many dedicated circuits, each of them can be in the same or different regions and can be connected to your WAN through different service providers. 

![](./media/expressroute-introduction/expressroute-basic.png)

A dedicated circuit will have multiple routing domains associated with it – public, private, and Microsoft. Each of the routing domains are configured identically on a pair of routers (in active-active or loadsharing configuration) for high availability. 

![](./media/expressroute-introduction/expressroute-peerings.png)


### Private peering
Azure compute services, namely virtual machines (IaaS) and cloud services (PaaS) deployed within a virtual network can be connected through the private peering domain. The private peering domain is considered to be a trusted extension of your core network into Windows Azure. You can setup bidirectional connectivity between your core network and Azure virtual networks (VNets). This will enable you to connect to virtual machines and cloud services directly on their private IP addresses.  

You can connect more than one virtual network to the private peering domain. Review the [FAQ page](/documentation/articles/expressroute-faqs) for information on limits and limitations. 
  

### Public peering
Services such as Azure Storage, SQL databases and Websites are offered on public IP addresses. You can privately connect to services hosted on public IP addresses, including VIPs of your cloud services, through the public peering routing domain. You can connect the public peering domain to your extranet and connect to all Azure services on their public IP addresses from your WAN without having to connect through the internet. Connectivity is always initiated from your WAN to Windows Azure services. Windows Azure services will not be able to initiate connections into your network through this routing domain. Once public peering is enabled, you will be able to connect to all Azure services. We do not allow you to selectively pick services for which we advertise routes to. You can review the list of prefixes we advertise to you through this peering at [Windows Azure Datacenter IP Ranges](http://www.microsoft.com/download/details.aspx?id=41653) page. You can define custom route filters within your network to consume only the routes you need. 

Review the [FAQ page](/documentation/articles/expressroute-faqs) for more information on services supported through the public peering routing domain. 
 
### Windows peering
Connectivity to all other Windows online services (such as Office 365 services) will be through the Windows peering. We enable bidirectional connectivity between your WAN and Windows cloud services through the Windows peering routing domain. You must connect to Windows cloud services only over public IP addresses that are owned by you or your connectivity provider and must adhere to all the rules we define. Review the [ExpressRoute prerequisites](/documentation/articles/expressroute-prerequisites) page for more information.

Review the [FAQ page](/documentation/articles/expressroute-faqs) for more information on services supported, costs and configuration details. Review the [ExpressRoute Locations](/documentation/articles/expressroute-locations) page for information on the list of connectivity providers offering Windows peering support.


The table below compares the three routing domains.

||**Private Peering**|**Public Peering**|**Windows Peering**|  
|---|---|---|---|
|**Max. # prefixes supported per peering**|4000 by default, 10,000 with ExpressRoute Premium|4000 by default, 10,000 with ExpressRoute Premium|200|
|**IP address ranges supported**|Any valid IPv4 address within your WAN|Public IPv4 addresses owned by you or your connectivity provider|Public IPv4 ddresses owned by you or your connectivity provider|  
|**AS Number Requirements**|Private and public AS numbers . Customer must own public AS number. | Private and public AS numbers. Customer must own public AS number.| Public AS numbers only. AS number must be validated against routing registries to validate ownership.|
|**Routing Interface IP addresses**|RFC1918 and public IP addresses|Public IP addresses registered to customers / NSP in routing registries.| Public IP addresses registered to customers / NSP in routing registries.|
|**MD5 Hash support**| Yes|Yes|Yes|

You can choose to enable one or more of the routing domains as part of their dedicated circuit. You can choose to have all the routing domains put on the same VPN (for NSP case) if they wish to ingest them into a single routing domain. You can also put them on different routing domains similar to the diagram above. The recommended configuration is that private peering is connected directly to the core network, and the public and Windows peering links connected to your extranet.
 
If you choose to have all three peering sessions, you must have three pairs of BGP sessions (one pair for each peering type). The BGP session pairs provide a highly available link. If you are connecting through EXPs, you will be responsible for configuring and managing routing (unless EXP offers to manage routing for you). If you choose to connect through NSPs, you can rely on the NSP to manage routing for you. You can learn more by reviewing the workflows for setting up ExpressRoute


## Next Steps

- Find a service provider. See [ExpressRoute Service Providers and Locations](/documentation/articles/expressroute-locations).
- Configure your ExpressRoute connection. See [Configure an ExpressRoute connection through a network service provider](/documentation/articles/expressroute-configuring-nsps) or [Configure an ExpressRoute connection through an exchange provider](/documentation/articles/expressroute-configuring-exps) for instructions. 
<!-- keep by customization: end -->