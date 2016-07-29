<!-- not suitable for Mooncake -->

<properties
	pageTitle="Web Apps overview | Azure"
	description="Learn how Azure helps you develop and host web applications"
	services="app-service\web"
	documentationCenter=""
	authors="jaime-espinosa"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="05/25/2016"
	wacn.date=""/>

# Web Apps overview

*Azure Web Apps* is a fully managed compute platform that is optimized for hosting websites and web applications. This [platform-as-a-service](https://en.wikipedia.org/wiki/Platform_as_a_service) (PaaS) offering of Azure lets you focus on your business logic while Azure takes care of the infrastructure to run and scale your apps.

The following 5-minute video introduces Azure Web Apps.

[AZURE.VIDEO azure-app-service-web-apps-with-yochay-kiriaty]

## What is a web app in Azure?

In Azure Web App, a *web app* is the compute resources that Azure provides for hosting a website or web application.  

The compute resources may be on shared or dedicated virtual machines (VMs), depending on the pricing tier that you choose. Your application code runs in a managed VM that is isolated from other customers.

Your code can be in any language or framework that is supported by [Azure Web App](/documentation/services/web-sites/), such as ASP.NET, Node.js, Java, PHP, or Python. You can also run scripts that use [PowerShell and other scripting languages](/documentation/articles/web-sites-create-web-jobs/#acceptablefiles) in a web app.

For examples of typical application scenarios that you can use Web Apps for, see [Web app scenarios](https://azure.microsoft.com/documentation/scenarios/web-app/) and the **Scenarios and recommendations** section of [Azure Web App, Virtual Machines, Service Fabric, and Cloud Services comparison](/documentation/articles/choose-web-site-cloud-service-vm/#scenarios).

## Why use Web Apps?

Here are some key features of Azure that apply to Web Apps:

- **Multiple languages and frameworks** - Azure has first-class support for ASP.NET, Node.js, Java, PHP, and Python. You can also run [PowerShell and other scripts or executables](/documentation/articles/web-sites-create-web-jobs/) on Azure VMs.

- **DevOps optimization** - Set up [continuous integration and deployment](/documentation/articles/app-service-continous-deployment/) with Visual Studio Team Services, GitHub, or BitBucket. Promote updates through [test and staging environments](/documentation/articles/web-sites-staged-publishing/). Perform [A/B testing](/documentation/articles/app-service-web-test-in-production-get-start/). Manage your apps in Azure by using [Azure PowerShell](/documentation/articles/powershell-install-configure/) or the [cross-platform command-line interface (CLI)](/documentation/articles/xplat-cli-install/).
 
- **Global scale with high availability** - Scale [up](/documentation/articles/web-sites-scale/) or [out](/documentation/articles/insights-how-to-scale/) manually or automatically. Host your apps anywhere in Microsoft's global datacenter infrastructure, and the Azure [SLA](https://azure.microsoft.com/support/legal/sla/app-service/) promises high availability.

- **Connections to SaaS platforms and on-premises data** - Choose from more than 50 [connectors](/documentation/articles/apis-list/) for enterprise systems (such as SAP, Siebel, and Oracle), SaaS services (such as Salesforce and Office 365), and internet services (such as Facebook and Twitter). Access on-premises data using [Hybrid Connections](/documentation/articles/integration-hybrid-connection-overview/) and [Azure Virtual Networks](/documentation/articles/web-sites-integrate-with-vnet/).

- **Security and compliance** - Azure is [ISO, SOC, and PCI compliant](https://www.microsoft.com/TrustCenter/).

- **Application templates** - Choose from an extensive list of application templates in the [Azure Marketplace](https://azure.microsoft.com/marketplace/) that let you use a wizard to install popular open-source software such as WordPress, Joomla, and Drupal.

- **Visual Studio integration** - Dedicated tools in Visual Studio streamline the work of creating, deploying, and debugging.

In addition, a web app can take advantage of features offered by [API Apps](/documentation/articles/app-service-api-apps-why-best-platform/) (such as CORS support) and [Mobile Apps](/documentation/articles/app-service-mobile-value-prop/) (such as push notifications). For more information about app types in Azure Web App, see [Azure overview](/documentation/services/web-sites/).

Besides Web Apps in Azure, Azure offers other services that can be used for hosting websites and web applications. For most scenarios, Web Apps is the best choice.  For microservice architecture, consider [Service Fabric](/documentation/services/service-fabric), and if you need more control over the VMs that your code runs on, consider [Azure Virtual Machines](/documentation/services/virtual-machines/). For more information about how to choose between these Azure services, see [Azure Web App, Virtual Machines, Service Fabric, and Cloud Services comparison](/documentation/articles/choose-web-site-cloud-service-vm/).

## Getting started

To get started by deploying sample code to a new web app in Azure, follow the [Deploy your first web app to Azure in 5 minutes](/documentation/articles/app-service-web-get-started/) tutorial. You'll need a free Azure account.

If you want to get started with Azure before signing up for an Azure account, go to [Try Azure Web App](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure. No credit cards required; no commitments.
