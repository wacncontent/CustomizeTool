<properties
    pageTitle="App Service Environment | Azure"
    description="What is an Azure App Service Environment? An introduction to App Service Environment."
    keywords="azure app service environment, virtual network, secure networking"
    services="app-service"
    documentationcenter=""
    author="stefsch"
    manager="wpickett"
    editor="" />
<tags
    ms.assetid="1db5c057-3c56-4537-b580-cdd21fe3f3a7"
    ms.service="app-service"
    ms.workload="na"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/04/2016"
    wacn.date=""
    ms.author="stefsch" />

# App Service Environment Documentation
An App Service Environment is a [Premium][PremiumTier] service plan option of Azure App Service that provides a fully isolated and dedicated environment for securely running Azure App Service apps at high scale, including [Web Apps][WebApps], [Mobile Apps][MobileApps], and [API Apps][APIApps].  

App Service Environments are ideal for application workloads requiring:

* Very high scale
* Isolation and secure network access

Customers can create multiple App Service Environments within a single Azure region, as well as across multiple Azure regions.  This makes App Service Environments ideal for horizontally scaling state-less application tiers in support of high RPS workloads.

App Service Environments are isolated to running only a single customer's applications, and are always deployed into a virtual network.  Customers have fine-grained control over both inbound and outbound application network traffic using [network security groups][NetworkSecurityGroups].  Applications can also establish high-speed secure connections over virtual networks to on-premises corporate resources.

Apps frequently need to access corporate resources such as internal databases and web services.  Apps running on App Service Environments can access resources reachable via [Site-to-Site][SiteToSite] VPN and [Azure ExpressRoute][ExpressRoute] connections.

* [What is an App Service Environment?](/documentation/articles/app-service-app-service-environment-intro/)
* [Creating an App Service Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment/)
* [Creating Apps in an App Service Environment](/documentation/articles/app-service-web-how-to-create-a-web-app-in-an-ase/)
* [Creating and Using an Internal Load Balancer with App Service Environments](/documentation/articles/app-service-environment-with-internal-load-balancer/)
* [Configuring an App Service Environment](/documentation/articles/app-service-web-configure-an-app-service-environment/) 
* [Scaling Apps in an App Service Environment](/documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment/)
* [Network Security and Architecture](/documentation/articles/app-service-app-service-environment-network-architecture-overview/)

## How To's
[AZURE.INCLUDE [app-service-blueprint-app-service-environment](../../includes/app-service-blueprint-app-service-environment.md)]

## Videos
[!VIDEO https://channel9.msdn.com/Events/Microsoft-Azure/AzureCon-2015/ACON325/player]


[!VIDEO https://channel9.msdn.com/Events/Ignite/2015/BRK3715/player]



<!-- LINKS -->
[PremiumTier]: /pricing/overview/app-service/
[WebApps]: /documentation/articles/app-service-web-overview/
[MobileApps]: /documentation/articles/app-service-mobile-value-prop-preview/
[APIApps]: /documentation/articles/app-service-api-apps-why-best-platform/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[SiteToSite]: /documentation/articles/vpn-gateway-site-to-site-create/
[ExpressRoute]: http://azure.microsoft.com/services/expressroute/
