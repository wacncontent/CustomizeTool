<properties
   pageTitle="ExpressRoute locations | Windows Azure"
   description="This article provides a detailed overview of locations where services are offered and how to connect to Azure regions."
   services="expressroute"
   documentationCenter="na"
   authors="cherylmc"
   manager="carolz"
   editor="" />
<tags
	ms.service="expressroute"
	ms.date="09/22/2015"
	wacn.date=""/>

# ExpressRoute partners and peering locations
<!-- deleted by customization

The tables in this article provide information on ExpressRoute connectivity providers, ExpressRoute geographical coverage, Microsoft cloud services supported over ExpressRoute, and ExpressRoute System Integrators (SIs).
-->
<!-- keep by customization: begin -->
The tables on this page provide information on ExpressRoute connectivity providers (EXPs and NSPs), ExpressRoute geographical coverage, Microsoft cloud services supported over ExpressRoute, and ExpressRoute System Integrators (SIs).
<!-- keep by customization: end -->

## ExpressRoute connectivity providers
<!-- deleted by customization

ExpressRoute is supported across all Azure regions and locations. The following map provides a list of Azure regions and ExpressRoute locations. ExpressRoute locations refer to those where Microsoft peers with several service providers.
![](./media/expressroute-locations/expressroute-locations-map.png)

You will have access to Azure services across all regions within a geopolitical region if you connected to at least one ExpressRoute location within the geopolitical region. The following table  provides a map of Azure regions to ExpressRoute locations within a geopolitical region.

|**Geopolitical region**|**Azure regions**|**ExpressRoute locations**|
-->
<!-- keep by customization: begin -->
ExpressRoute is supported across all Azure regions and locations. The map below provides a list of Azure regions and ExpressRoute locations. ExpressRoute locations refer to those where Microsoft peers with several service providers.
 
![](./media/expressroute-locations/expressroute-locations-map.png)

You will have access to Azure services across all regions within a geopolitical region if you connected to at least one ExpressRoute location within the geopolitical region. The  table below provides a map of Azure regions to ExpressRoute locations within a geopolitical region.

|**Geopolitical Region**|**Azure Regions**|**ExpressRoute Locations**|
<!-- keep by customization: end -->
|---|---|---|
|**US**|All US Regions - China East, China <!-- deleted by customization North, China --><!-- keep by customization: begin --> North,China <!-- keep by customization: end --> East 2, China North, China East, China North|Atlanta, Chicago, Dallas, Los Angeles, New York, Seattle, Silicon Valley, Washington DC|
|**South America**|Brazil South|Sao Paulo|
|**Europe**|China North, West Europe|Amsterdam, London|
<!-- deleted by customization
|**Asia**|East Asia, Southeast Asia|Hong Kong, Singapore|
-->
<!-- keep by customization: begin -->
|**Asia**|East Asia, Southeast Asia, China North, China East|Beijing, Shanghai, Hong Kong, Singapore|  
<!-- keep by customization: end -->
|**Japan**|Japan West, Japan East|Tokyo|
|**Australia**|Australia Southeast, Australia East|Melbourne, Sydney|
|**India**|India West, India Central, India South|Chennai, Mumbai|

<!-- deleted by customization


The table below provides information on regions and geopolitical boundaries for national clouds.

|**Geopolitical region**|**Azure regions**|**ExpressRoute locations**|
|---|---|---|---|
|**US Government cloud**|US Government|Iowa, Virginia|Ashburn, Chicago|


Connectivity across geopolitical regions is not supported on the standard ExpressRoute SKU. You will need to enable the ExpressRoute premium add-on to support global connectivity. Connectivity to national cloud environments is not supported. You can work with your connectivity provider if such a need arises.


## Connectivity provider locations

### Production Azure

| **Service provider**  |**Windows Azure** | **Office 365** | **Locations** |
-->
<!-- keep by customization: begin -->
Connectivity across geopolitical regions is not supported. You can work with your connectivity provider to extend connectivity across geopolitical regions using their network.


## Exchange Provider (EXP) locations

| **Service Provider**  |**Windows Azure** | **Office 365** | **Locations** |
<!-- keep by customization: end -->
|-----------------------|--------------------|----------------|---------------|
| **[Aryaka Networks]( http://www.aryaka.com/)** | Supported | Not Supported | Silicon Valley, Singapore, Washington DC |
<!-- deleted by customization
| **[AT&T NetBond]( https://www.synaptic.att.com/clouduser/html/productdetail/ATT_NetBond.htm)** | Supported | Supported | Amsterdam, London+, Dallas, Silicon Valley, Washington DC |
| **[British Telecom]( http://www.globalservices.bt.com/uk/en/news/bt_to_provide_connectivity_to_microsoft_azure)** | Supported | Supported | Amsterdam, London, Silicon Valley+, Washington DC |
|**China Telecom Global** | Coming Soon | Not Supported | Hong Kong+ |
| **[Colt]( http://www.colt.net/uk/en/news/colt-announces-dedicated-cloud-access-for-microsoft-azure-services-en.htm)**  |  Supported | Not Supported | Amsterdam, London |
-->
<!-- keep by customization: begin -->
| **[Colt Ethernet]( http://www.colt.net/uk/en/news/colt-announces-dedicated-cloud-access-for-microsoft-azure-services-en.htm)** | Supported | Not Supported | Amsterdam, London |
<!-- keep by customization: end -->
| **Comcast** | Supported | Not Supported | Silicon Valley, Washington DC |
| **[Equinix](http://www.equinix.com/partners/microsoft-azure/)** | Supported | <!-- deleted by customization Supported --><!-- keep by customization: begin --> Coming Soon <!-- keep by customization: end --> | Amsterdam, Atlanta, Chicago, Dallas, Hong Kong, London, Los Angeles, Melbourne, New York, Sao Paulo, Seattle, Silicon Valley, Singapore, Sydney, Tokyo, Washington DC |
<!-- deleted by customization
| **[Internet Initiative Japan Inc. - IIJ](http://www.iij.ad.jp/en/news/pressrelease/2013/pdf/Azure_E.pdf)** |  Supported | Not Supported | Tokyo |
-->
| **[InterCloud]( https://www.intercloud.com/)** | Supported | Not Supported | Amsterdam, London, Singapore, Washington DC |
| **Internet Solutions - Cloud Connect** | Supported | Not Supported | Amsterdam, London |
| **Interxion** | Supported | Not Supported | Amsterdam |
| **[Level 3 <!-- deleted by customization Communications]( --><!-- keep by customization: begin --> Communications - Exchange]( <!-- keep by customization: end --> http://your.level3.com/LP=882?WT.tsrc=02192014LP882AzureVanityAzureText)** | Supported | Not Supported | <!-- deleted by customization Amsterdam, --> Chicago, Dallas, London, Seattle, Silicon Valley, Washington DC |
<!-- deleted by customization
| **Megaport** | Supported | Not Supported | Melbourne, Sydney |
| **MTN** | Supported | Not Supported | London |
| **NTT Communications** | Supported | Not Supported | London+, Tokyo |
-->
| **NEXTDC** | Supported | Not Supported | Melbourne, Sydney+ |
<!-- keep by customization: begin -->
| **[TeleCity Group]( http://www.telecitygroup.com/investor-centre/news_details.htm?locid=03100500400b00d&xml)** | Supported | Coming Soon | Amsterdam, London |
| **[Telstra Corporation]( http://www.telstra.com.au/business-enterprise/network-services/networks/cloud-direct-connect/)** | Supported | Not Supported | Melbourne+, Sydney |
| **[Zayo Group]( http://www.zayo.com/)** | Supported | Not Supported | Washington DC |

 **+** denotes coming soon

See [Configure your EXP connection](/documentation/articles/expressroute-configuring-exps) for steps to set up your connection.

## Network Service Provider (NSP) locations


| **Service Provider**  |**Windows Azure** | **Office 365** | **Locations** |
|-----------------------|--------------------|----------------|---------------|
| **[AT&T]( https://www.synaptic.att.com/clouduser/html/productdetail/ATT_NetBond.htm)** | Supported | Coming Soon | Amsterdam+, London+, Dallas, Silicon Valley, Washington DC |
| **[British Telecom]( http://www.globalservices.bt.com/uk/en/news/bt_to_provide_connectivity_to_microsoft_azure)** | Supported | Coming Soon | Amsterdam, London, Silicon Valley+, Washington DC |
|**China Telecom Global** | Coming Soon | Not Supported | Hong Kong+ |
| **[Colt IPVPN]( http://www.colt.net/uk/en/news/colt-announces-dedicated-cloud-access-for-microsoft-azure-services-en.htm)**  |  Supported | Not Supported | Amsterdam, London |
| **[Internet Initiative Japan Inc. - IIJ](http://www.iij.ad.jp/en/news/pressrelease/2013/pdf/Azure_E.pdf)** |  Supported | Not Supported | Tokyo |
| **[Level 3 Communications - IPVPN]( http://your.level3.com/LP=882?WT.tsrc=02192014LP882AzureVanityAzureText)** | Supported | Not Supported | Chicago, Dallas, London, Seattle, Silicon Valley, Washington DC |
| **NTT Communications** | Coming Soon | Not Supported | Tokyo+ | 
<!-- keep by customization: end -->
| **[Orange]( http://www.orange-business.com/)** | Supported | Not Supported | Amsterdam, London, Silicon Valley, Washington DC |
| **PCCW Global Limited** | Supported | Not Supported | Hong Kong |
| **[SingTel]( http://info.singtel.com/about-us/news-releases/singtel-provide-secure-private-access-microsoft-azure-public-cloud)** |  Supported | Not Supported | Singapore |
| **[Tata Communications](http://www.tatacommunications.com/lp/izo/azure/azure_index.html)** | Supported | <!-- deleted by customization Supported --><!-- keep by customization: begin --> Coming Soon <!-- keep by customization: end --> | Amsterdam, Chennai+, Hong Kong, London, Mumbai+, Singapore |
<!-- deleted by customization
| **[TeleCity Group]( http://www.telecitygroup.com/investor-centre/news_details.htm?locid=03100500400b00d&xml)** | Supported | Supported | Amsterdam, London |
-->
| **[Telstra Corporation]( http://www.telstra.com.au/business-enterprise/network-services/networks/cloud-direct-connect/)** | Supported | Not Supported | Melbourne+, Sydney |
| <!-- deleted by customization **[Verizon](http://www.verizonenterprise.com/products/networking/secure-cloud-interconnect/)** --><!-- keep by customization: begin --> **[Verizon](http://news.verizonenterprise.com/2014/04/secure-cloud-interconnect-solutions-enterprise/)** <!-- keep by customization: end --> | Supported | <!-- keep by customization: begin --> Not <!-- keep by customization: end --> Supported | London, Hong Kong, Silicon Valley, <!-- deleted by customization Sydney, Tokyo, --> Washington DC |
<!-- deleted by customization
| **[Zayo Group]( http://www.zayo.com/)** | Supported | Not Supported | Chicago, Silicon Valley, Washington DC |
-->

 **+** denotes coming soon

<!-- deleted by customization
### National cloud environments

#### US Government cloud

| **Service provider**  |**Windows Azure** | **Office 365** | **Locations** |
|-----------------------|--------------------|----------------|---------------|
| **[AT&T NetBond]( https://www.synaptic.att.com/clouduser/html/productdetail/ATT_NetBond.htm)** | Coming Soon | Not Supported | Chicago+, Washington DC+ |
| **[Equinix](http://www.equinix.com/partners/microsoft-azure/)** | Coming Soon | Not Supported | Chicago,  Washington DC |
| **[Level 3 Communications - IPVPN]( http://your.level3.com/LP=882?WT.tsrc=02192014LP882AzureVanityAzureText)** | Coming Soon | Not Supported | Chicago, Washington DC |
| **[Verizon](http://news.verizonenterprise.com/2014/04/secure-cloud-interconnect-solutions-enterprise/)** | Supported | Not Supported | Chicago, Washington DC |

## Connectivity through service providers not listed

If your connectivity provider is not listed in previous sections, you can still create a connection.

- Check with your connectivity provider to see if they are connected to any of the exchanges in the table above. You can check the following links to gather more information about services offered by exchange providers. Several connectivity providers are already connected to Ethernet exchanges.

	- [Equinix Cloud Exchange](http://www.equinix.com/services/interconnection-connectivity/cloud-exchange/)
	- [TeleCity CloudIX](http://www.telecitygroup.com/colocation-services/cloud-ix.htm)
	- [InterXion](http://www.interxion.com/)
	- [NextDC](http://www.nextdc.com/)
	- [CoreSite](http://www.coresite.com/)
- Have your connectivity provider extend your network to the peering location of choice.
	- Ensure that your connectivity provider extends your connectivity in a highly available manner so that there are no single points of failure.
- Order an ExpressRoute circuit with the exchange as your connectivity provider to connect to Microsoft.
	- Follow steps in [Create an ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic) to set up connectivity.

|**Connectivity provider**|**Exchange**|**Peering locations**|
-->
<!-- keep by customization: begin -->
See [Configure your NSP connection](/documentation/articles/expressroute-configuring-nsps) for steps to set up your connection.

## Connectivity through service providers not listed 

If your connectivity provider is not in the list above sections, you can still create a connection.

- Check with your connectivity provider to see if they are connected to any of the Exchange providers in the listed EXP locations. You can check the links below to gather more information on services offered by Exchange Providers. Several connectivity providers are already connected to EXPs' Ethernet exchanges.
	- [Equinix Cloud Exchange](http://www.equinix.com/services/interconnection-connectivity/cloud-exchange/) 
	- [TeleCity CloudIX](http://www.telecitygroup.com/colocation-services/cloud-ix.htm)
- Have your connectivity provider extend your network to the Exchange location of choice.
	- Ensure that your connectivity provider extends your connectivity in a highly available manner so that there are no single points of failure.
	- Connectivity providers (specifically Ethernet providers) may require you to procure a pair of circuits to the Ethernet exchanges to ensure high availability. 
- Order an ExpressRoute circuit through the Exchange provider to connect to Azure.
	- Follow steps in [Configure your EXP connection](/documentation/articles/expressroute-configuring-exps) to set up connectivity.

|**Connectivity Provider**|**Exchange Providers**|**Peering Locations**|
<!-- keep by customization: end -->
|---|---|---|
|**[XO Communications](http://www.xo.com/)**|Equinix|Silicon Valley|

## ExpressRoute system integrators
<!-- deleted by customization

Enabling private connectivity to fit your needs can be challenging, based on the scale of your network. You can work with any of the system integrators listed in the following table to assist you with onboarding to ExpressRoute.

|**System integrator**|**Continent**|
-->
<!-- keep by customization: begin -->
Enabling private connectivity to fit your needs can be challenging, based on the scale of your network. You can work with any of the System Integrators listed in the table below to assist you with onboarding to ExpressRoute. 


|**System Integrator**|**Continent**|
<!-- keep by customization: end -->
|---|---|
|**[Nimbo](http://www.nimbo.com/)**|US||
|**[Dotnet Solutions](http://www.dotnetsolutions.co.uk/)**|EMEA|

<!-- deleted by customization
## Next steps

- For more information about ExpressRoute, see the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs).
- Ensure that all prerequisites are met. See [ExpressRoute prerequisites](/documentation/articles/expressroute-prerequisites).

-->
<!-- keep by customization: begin -->
## Next Steps
- Verify that you meet the [ExpressRoute prerequisites](/documentation/articles/expressroute-prerequisites).
- Visit the [FAQ](/documentation/articles/expressroute-faqs) for more information.
- If you want to configure an ExpressRoute connection, see [Configure your EXP connection](/documentation/articles/expressroute-configuring-exps) or [Configure your NSP connection](/documentation/articles/expressroute-configuring-nsps).
- If you want to configure both a site-to-site VPN connection and ExpressRoute for the same virtual network, see [Configure ExpressRoute and Site-to-Site VPN connections that coexist](/documentation/articles/expressroute-coexist).
 

<!-- keep by customization: end -->