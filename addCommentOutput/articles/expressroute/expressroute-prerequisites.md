<properties
   pageTitle="Prerequisites for ExpressRoute adoption | Windows Azure"
   description="This page provides a list of requirements to be met before you can order an Azure ExpressRoute circuit."
   documentationCenter="na"
   services="expressroute"
   authors="cherylmc"
   manager="carolz"
   editor=""/>
<tags
	ms.service="expressroute"
	ms.date="09/21/2015"
	wacn.date=""/>


<!-- deleted by customization
# ExpressRoute prerequisites   

To connect to Microsoft cloud services using ExpressRoute, you’ll need to verify that the following requirements listed in the sections below have been met <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

## Account requirements

- A valid and active Windows Azure account. This is required to setup the ExpressRoute circuit. ExpressRoute circuits are resources within Azure subscriptions. An Azure subscription is a requirement even if connectivity is limited to non-Azure Microsoft cloud services, such as Office 365 services and CRM online.
- An active Office 365 subscription (if using Office 365 services). See the [Office 365 specific requirements](#office-365-specific-requirements) section of this article for more information.

## Connectivity provider relationship

- A relationship with a connectivity provider from the supported list through whom connectivity needs to be facilitated. You must have an existing business relationship with your connectivity provider. You will need to make sure that the service you have with the connectivity provider is compatible with ExpressRoute.
- If the you want to use a connectivity provider that is not in the supported list, you can still create a connection to Microsoft cloud services through an exchange.
	- Check with your connectivity provider to see if they are present in any of the exchange locations appearing in supported list.
	- Have the connectivity provider extend your network to the exchange location of choice.
	- Order an ExpressRoute circuit with the exchange as the connectivity provider.

## Physical connectivity between your network and the connectivity provider

Refer to the connectivity models section for details on connectivity models. Customers must ensure that their on-premises infrastructure is physically connected to the service provider infrastructure through one of the models described. 

## Redundancy requirements for connectivity

There are no redundancy requirements on physical connectivity between the customer infrastructure and the service provider infrastructure. 
Microsoft does require redundancy in Layer 3. Microsoft does require redundant routing to be setup between Microsoft’s edge and the customer’s network through the service provider for each of the peerings to be enabled. If routing sessions are not configured in a redundant manner, the service availability SLA will be void.

## IP addresses and routing considerations

Customers/Connectivity Providers are responsible for setting up redundant BGP sessions with the Microsoft edge infrastructure.  Customers choosing to connect through IP VPN providers will typically rely on the connectivity providers to manage routing configurations. Customers co-located with an exchange or connecting to Microsoft through a point-to-point Ethernet provider will have to configure redundant BGP sessions per peering to meet availability SLA requirements. Connectivity providers may offer this as a value added service. 
Refer to the routing domains table in the [ExpressRoute circuits and routing domains](/documentation/articles/expressroute-circuit-peerings) article for more information on limits.

## Security and firewalling

Please refer to this document, [Microsoft Cloud Services and Network Security](/documentation/articles/best-practices-network-security), for security and firewalling information.

## NAT configuration for Azure public and Microsoft peerings

Refer to [ExpressRoute NAT requirements](/documentation/articles/expressroute-nat) for detailed guidance about requirements and configurations. Check with your connectivity provider to see if they will manage NAT setup and management for you. Typically, Layer 3 connectivity providers will manage NAT for you.

## Office 365 specific requirements

Review the following resources for more information about Office 365 requirements.

- [Network planning and performance tuning for Office 365](https://support.office.com/zh-cn/article/Network-planning-and-performance-tuning-for-Office-365-e5f1228c-da3c-4654-bf16-d163daee8848)
- [Office 365 network traffic management](https://msft.spoppe.com/teams/cpub/teams/IW_Admin/modsquad/_layouts/15/WopiFrame.aspx?sourcedoc=%7b23f09224-0668-4476-8627-aaff30931439%7d&action=edit&source=https%3A%2F%2Fmsft%2Espoppe%2Ecom%2Fteams%2Fcpub%2Fteams%2FIW%5FAdmin%2Fmodsquad%2FSitePages%2FHome%2Easpx)
- Refer to the [ExpressRoute Quality of Service (QoS) requirements](/documentation/articles/expressroute-qos) article for detailed guidance on QoS requirements and configurations. Check with your connectivity provider to see if they offer multiple classes of service for your VPN. 

## Next steps
-->
<!-- keep by customization: begin -->
# ExpressRoute Prerequisites  

To connect to Microsoft cloud services using ExpressRoute, you’ll need to verify that the following prerequisites have been met <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

## Prerequisites for Connectivity

- A valid and active Windows Azure Account
- A relationship with a network service provider (NSP) or an exchange provider (EXP) from the [supported list](/documentation/articles/expressroute-locations) through whom connectivity needs to be facilitated. You must have an existing business relationship with the network service provider or exchange provider. You’ll need to make sure that the service you use is compatible with ExpressRoute. 
- If you want to use a network service provider and your network service provider is not in the list above, you can still create a connection to Azure.
	- Check with your network provider to see if they are present in any of the Exchange locations listed above.
	- Have your network provider extend your network to the Exchange location of choice.
	- Order an ExpressRoute circuit through the Exchange provider to connect to Azure.
- Connectivity to the service provider's infrastructure. You must meet the criteria for at least one of the following items listed:
	- You are a VPN customer of the network service provider and have at least one on-premises site connected to the network service provider’s VPN infrastructure. Check with your network service provider to see if your VPN service meets the requirements for ExpressRoute
	- Your infrastructure is co-located in the exchange provider’s datacenter.
	- You have Ethernet connectivity to the exchange provider’s Ethernet exchange infrastructure.
- IP addresses and AS numbers for routing configuration.
	- You can use private AS numbers to connect to Azure private peering routing domain. If you choose to do so, it must be > 65000. For more information about AS numbers, see [Autonomous System (AS) Numbers](http://www.iana.org/assignments/as-numbers/as-numbers.xhtml).
	- IP addresses to configure routes. A /28 subnet is required. This must not overlap with any IP address ranges used in your on-premises or in Azure.
	- You must use your own public AS numbers for configuring BGP sessions with Azure public services.

## Next Steps
<!-- keep by customization: end -->

- For more information about ExpressRoute, see the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs).
<!-- deleted by customization
- Find a service provider. See [ExpressRoute partners and peering locations](/documentation/articles/expressroute-locations).
- Refer to requirements for [Routing](/documentation/articles/expressroute-routing), [NAT](/documentation/articles/expressroute-nat) and [QoS](/documentation/articles/expressroute-qos).
- Configure your ExpressRoute connection.
	- [Create an ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic)
	- [Configure routing](/documentation/articles/expressroute-howto-routing-classic)
	- [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-classic)


-->
<!-- keep by customization: begin -->
- For information about how to configure your ExpressRoute connection, see:
	- [Configure an ExpressRoute Connection through a Network Service Provider](/documentation/articles/expressroute-configuring-nsps)
	- [Configure an ExpressRoute Connection through an Exchange Provider](/documentation/articles/expressroute-configuring-exps)
 

<!-- keep by customization: end -->