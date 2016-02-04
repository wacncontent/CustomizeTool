<properties 
	pageTitle="Controlling Azure web site traffic with Azure Traffic Manager" 
	description="This article provides summary information for  Azure Traffic Manager as it relates to Azure web sites." 
	services="app-service\web" 
	documentationCenter="" 
	authors="cephalin" 
	writer="cephalin" 
	manager="wpickett" 
	editor="mollybos"/>

<tags
	ms.service="app-service-web"
	ms.date="12/10/2015"
	wacn.date=""/>

# Controlling Azure web site traffic with Azure Traffic Manager

> [AZURE.NOTE] This article provides summary information for Windows Azure Traffic Manager as it relates to Azure Websites. More information about Azure Traffic Manager itself can be found by visiting the links at the end of this article.

## Introduction
You can use Azure Traffic Manager to control how requests from web clients are distributed to web sites in Azure Websites. When web site endpoints are added to a Azure Traffic Manager profile, Azure Traffic Manager keeps track of the status of your web sites (running, stopped or deleted) so that it can decide which of those endpoints should receive traffic.

## Load Balancing Methods
Azure Traffic Manager uses three different load balancing methods. These are described  in the following list as they pertain to Azure web sites. 

* **Failover**: If you have web site clones in different regions, you can use this method to configure one web site to service all web client traffic, and configure another web site in a different region to service that traffic in case the first web site becomes unavailable. 
	
* **Round Robin**: If you have web site clones in different regions, you can use this method to distribute traffic equally across the web sites in different regions. 
	
* **Performance**: The Performance method distributes traffic based on the shortest round trip time to clients. The Performance method can be used for web sites within the same region or in different regions. 

For detailed information about load balancing in Azure Traffic Manager, see [About Traffic Manager Load Balancing Methods](/documentation/articles/traffic-manager-load-balancing-methods).

##web sites and Traffic Manager Profiles 
To configure the control of web site traffic, you create a profile in Azure Traffic Manager that uses one of the three load balancing methods described previously, and then add the endpoints (in this case, web sites) for which you want to control traffic to the profile. Your web site status (running, stopped or deleted) is regularly communicated to the profile so that Azure Traffic Manager can direct traffic accordingly.

When using Azure Traffic Manager with Azure, keep in mind the following points:

* For web site only deployments within the same region, web sites already provides failover and round-robin functionality without regard to web site mode.

* For deployments in the same region that use web sites in conjunction with another Azure cloud service, you can combine both types of endpoints to enable hybrid scenarios.

* You can only specify one web site endpoint per region in a profile. When you select a web site as an endpoint for one region, the remaining web sites in that region become unavailable for selection for that profile.

* The web site endpoints that you specify in a Azure Traffic Manager profile will appear under the **Domain Names** section on the Configure page for the web site in the profile, but will not be configurable there.

* After you add a web site to a profile, the **Site URL** on the Dashboard of the web site's portal page will display the custom domain URL of the web site if you have set one up. Otherwise, it will display the Traffic Manager profile URL (for example, `contoso.trafficmgr.com`). Both the direct domain name of the web site and the Traffic Manager URL will be visible on the web site's Configure page under the **Domain Names** section.

* Your custom domain names will work as expected, but in addition to adding them to your web sites, you must also configure your DNS map to point to the Traffic Manager URL. For information on how to set up a custom domain for a Azure web site,  see [Configuring a custom domain name for an Azure web site](/documentation/articles/web-sites-custom-domain-name).

* You can only add web sites that are in standard mode to a Azure Traffic Manager profile.

## Next Steps

For a conceptual and technical overview of Azure Traffic Manager, see [Traffic Manager Overview](/documentation/articles/traffic-manager-overview). 

For detailed information about load balancing in Azure Traffic Manager, see [About Traffic Manager Load Balancing Methods](/documentation/articles/traffic-manager-load-balancing-methods).

For more information about using Traffic Manager with web sites, see the blog posts 
[Using Azure Traffic Manager with Azure Web Sites](http://blogs.msdn.com/b/waws/archive/2014/03/18/using-windows-azure-traffic-manager-with-waws.aspx) and [Azure Traffic Manager can now integrate with Azure Web Sites](http://azure.microsoft.com/blog/2014/03/27/azure-traffic-manager-can-now-integrate-with-azure-web-sites/).
 
