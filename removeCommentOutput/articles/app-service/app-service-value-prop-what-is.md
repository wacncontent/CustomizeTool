<properties
    pageTitle="Azure App Service for web, mobile, and API apps | Azure"
    description="Learn how Azure App Service helps you develop, deploy, and manage web and mobile apps."
    keywords="app service, azure app service, app service cost, scale, scalable, app deployment, azure app deployment, paas, platform-as-a-service, website, web site, web, azure mobile"
    services="app-service"
    documentationcenter=""
    author="omarkmsft"
    manager="erikre"
    editor="cephalin" />
<tags
    ms.assetid="979cafa8-eeb6-4d3b-87cf-764a821c3e4f"
    ms.service="app-service"
    ms.workload="na"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="get-started-article"
    ms.date="10/26/2016"
    wacn.date=""
    ms.author="omark" />

# What is Azure App Service?
*App Service* is a [platform-as-a-service](https://zh.wikipedia.org/wiki/平台即服务) (PaaS) offering of Azure. Create web and mobile apps for any platform or device. Integrate your apps with SaaS solutions, connect with on-premises applications, and automate your business processes. Azure runs your apps on fully managed virtual machines (VMs), with your choice of shared VM resources or dedicated VMs.

App Service includes the web and mobile capabilities that we previously delivered separately as Azure Websites and Azure Mobile Services. It also includes new capabilities for automating business processes and hosting cloud APIs. As a single integrated service, App Service lets you compose various components -- websites, mobile app back ends, RESTful APIs, and business processes -- into a single solution.

The following 4-minute video provides a brief explanation of how App Service relates to earlier Azure offerings and what's new in it.

> [!VIDEO https://channel9.msdn.com/Series/Windows-Azure-Web-Sites-Tutorials/app-service-history-lesson/player]
> 
> 

## Why use App Service?
Here are some key features and capabilities of App Service:

* **Multiple languages and frameworks** - App Service has first-class support for ASP.NET, Node.js, Java, PHP, and Python. You can also run [Windows PowerShell and other scripts or executables](/documentation/articles/web-sites-create-web-jobs/) on App Service VMs.
* **DevOps optimization** - Set up [continuous integration and deployment](/documentation/articles/app-service-continuous-deployment/) with Visual Studio Team Services, GitHub, or BitBucket. Promote updates through [test and staging environments](/documentation/articles/web-sites-staged-publishing/). Perform [A/B testing](/documentation/articles/app-service-web-test-in-production-get-start/). Manage your apps in App Service by using [Azure PowerShell](/documentation/articles/powershell-install-configure/) or the [cross-platform command-line interface (CLI)](/documentation/articles/xplat-cli-install/).
* **Global scale with high availability** - Scale [up](/documentation/articles/web-sites-scale/) or [out](/documentation/articles/insights-how-to-scale/) manually or automatically. Host your apps anywhere in Microsoft's global datacenter infrastructure, and the App Service [SLA](/support/sla/app-service/) promises high availability.
* **Connections to SaaS platforms and on-premises data** - Choose from more than 50 [connectors](/documentation/articles/apis-list/) for enterprise systems (such as SAP, Siebel, and Oracle), SaaS services (such as Salesforce and Office 365), and internet services (such as Facebook and Twitter). Access on-premises data using [Hybrid Connections](/documentation/articles/integration-hybrid-connection-overview/) and [Azure Virtual Networks](/documentation/articles/web-sites-integrate-with-vnet/).
* **Security and compliance** - App Service is [ISO, SOC, and PCI compliant](https://www.microsoft.com/TrustCenter/).
* **Application templates** - Choose from an extensive list of application templates in the [Azure Marketplace](https://azure.microsoft.com/marketplace/) that let you use a wizard to install popular open-source software such as WordPress, Joomla, and Drupal.
* **Visual Studio integration** - Dedicated tools in Visual Studio streamline the work of creating, deploying, and debugging.

## App types in App Service
App Service offers several *app types*, each of which is intended to host a specific kind of workload:

* [**Web Apps**](/documentation/articles/app-service-web-overview/) - For hosting websites and web applications.
* [**Mobile Apps**](/documentation/articles/app-service-mobile-value-prop/) For hosting mobile app back ends.
* [**API Apps**](/documentation/articles/app-service-api-apps-why-best-platform/) - For hosting RESTful APIs.
* [**Logic Apps**](/documentation/articles/app-service-logic-what-are-logic-apps/) - For automating business processes and integrating systems and data across clouds without writing code.

The word *app* here refers to the hosting resources dedicated to running a workload. Taking "web app" as an example, you're probably accustomed to thinking of a web app as both the compute resources and application code that together deliver functionality to a browser. But in App Service a *web app* is the compute resources that Azure provides for hosting your application code. If your application is composed of a web front end and a RESTful API back end, you could deploy both to a web app or you could deploy your front-end code to a web app and your back-end code to an API app. Your application may be composed of multiple App Service apps of different kinds.

## App Service Plans
[App Service Plans](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/) specify the kind of compute resources that your apps run on. If you expect light traffic loads, you can use shared VMs (**Free** and **Shared** pricing tiers). For higher loads, you can choose from several sizes of dedicated VMs (**Basic**, **Standard**, and **Premium** tiers). Multiple App Service apps can share the same plan, and they scale up and down the pricing tiers together in the plan.

If you need more scalability and network isolation, you can run your apps in an [App Service Environment](/documentation/articles/app-service-app-service-environment-intro/).

## Pricing
For information about how much App Service costs, see [App Service Pricing](/pricing/details/app-service/).

## Test-drive App Service
[Create a sample web app, mobile app, or logic app](https://tryappservice.azure.com/) and play with it for 1 hour, with no credit card required, no commitments, no hassles.

Or open a [free Azure account](/pricing/1rmb-trial/), and try one of our getting-started tutorials:

* [Tutorial: Create a web app](/documentation/articles/app-service-web-get-started/)
* [Tutorial: Create a mobile app](/documentation/articles/app-service-mobile-android-get-started/)
* [Tutorial: Create an API app](/documentation/articles/app-service-api-dotnet-get-started/)
* [Tutorial: Create a logic app](/documentation/articles/app-service-logic-create-a-logic-app/)

