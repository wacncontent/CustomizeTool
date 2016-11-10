<!-- not suitable for Mooncake -->

<properties
	pageTitle="Create a web app in an App Service Environment"
	description="Learn how to create web apps and app service plans in an App Service Environment"
	services="app-service"
	documentationCenter=""
	authors="ccompy"
	manager="stefsch"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="04/04/2016"
	wacn.date=""/>

# Create a web app in an  App Service  Azure  Environment

## Overview

This tutorial shows how to create web apps and App Service plans in an  [App Service  [Azure  Environment](/documentation/articles/app-service-app-service-environment-intro/) (ASE).

> [AZURE.NOTE] If you want to learn how to create a web app but don't need to do it in an  App Service  Azure  Environment, see [Create a .NET web app](/documentation/articles/web-sites-dotnet-get-started/) or one of the related tutorials for other languages and frameworks.

## Prerequisites

This tutorial assumes you have created an  App Service  Azure  Environment. If you haven't done that yet, see [Create an  App Service  Azure  Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment/).

## Create a web app

1. In the [Azure  Portal](https://portal.azure.com/)  Portal](https://portal.azure.cn/) , click **New > Web + Mobile > Web App**.

	![][1]

2. Select your subscription.  

	If you have multiple subscriptions be aware that to create an app in your  App Service  Azure  Environment, you need to use the same subscription that you used when creating the environment.

3. Select or create a resource group.

	*Resource groups* enable you to manage related Azure resources as a unit and are useful when establishing *role-based access control* (RBAC) rules for your apps. For more information, see [Managing your Azure resources][ResourceGroups]. 

4. Select or create an App Service plan.

	*App Service plans* are managed sets of web apps.  When you select pricing, the price charged is applied to the App Service plan rather than to the individual apps. To scale up the number of instances of a web app you scale up the instances of your App Service plan and it affects all of the web apps in that plan.  Some features such as site slots or VNET Integration also have quantity restrictions within the plan.  For more information, see [Azure App Service plans overview](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/)

	You can identify the App Service plans in your ASE by looking at the location that is noted under the plan name.  

	![][5]

	If you want to use an App Service plan that already exists in your  App Service  Azure  Environment, select that plan. If you want to create a new App Service plan, see the following section of this tutorial, [Create an App Service plan in an  App Service  Azure  Environment](#createplan).

5. Enter the name for your web app, and then click **Create**. 

	Your web app name needs to be unique in Azure  Web  App  Service .  This means if you want to create a web app named "thisismywebapp" then there currently cannot be any other web app named "thisismywebapp" in Azure  Web  App  Service .

	The URL of a web app in an ASE is:


	[*sitename*].[*name of your App Service Environment*].p.azurewebsites.net


	[*sitename*].[*name of your Azure Environment*].p.chinacloudsites.cn


	instead of


	[*sitename*].azurewebsites.net


	[*sitename*].chinacloudsites.cn


## <a name="createplan"></a> Create an App Service plan

When you create an App Service plan in  an App Service Environment  an Azure Environment , your worker choices are different as there are no shared workers in an ASE.  The workers you have to use are the ones that have been allocated to the ASE by the admin.  This means that to create a new plan, you need to have more workers allocated to your ASE worker pool than the total number of instances across all of your plans already in that worker pool.  If you don't have enough workers in your ASE worker pool to create your plan, you need to work with your ASE admin to get them added.

Another difference with App Service plans hosted by an  App Service  Azure  Environment is the lack of pricing selection.  When you have an  App Service  Azure  Environment you are paying for compute resources used by the system and do not have added charges for the plans in that environment.  Normally when you create an App Service plan you select a pricing plan which determines your billing.  An  App Service  Azure  Environment is essentially a private location where you can create content.  You pay for the environment and not to host your content.

The following instructions show how to create an App Service plan while you are creating a web app as explained in the previous section of the tutorial.

1. Click **Create New** in the plan selection UI and provide a name for your plan just as you normally would outside of an ASE.

2. Select the ASE that you want to use from your location picker.

	Because an  App Service  Azure  Environment is essentially a private deployment location, it shows under Location.

	![][2]

	After selection of an ASE in the location picker, the App Service plan creation UI updates.  The location now shows the name of the ASE system and the region it is in, and the pricing plan picker is replaced with a worker pool picker.  

	![][3]

### Selecting a worker pool

Normally in Azure  App Service  and outside of an  App Service  Azure  Environment, there are 3 compute sizes that are available with the selection of a dedicated price plan.  In a similar fashion, for an ASE you can define up to 3 pools of workers and specify the compute size that is used for that worker pool.  What that means for tenants of the ASE is that instead of selecting a pricing plan with compute size for your App Service plan, you select what is called a *worker pool*.

The worker pool selection UI shows the compute size used for that worker pool below the name.  The quantity available refers to how many compute instances are available for use in that pool.  The total pool may actually have more instances than this number but this value refers to simply how many are not in use.  If you need to adjust your  App Service  Azure  Environment to add more compute resources see [Configuring your  App Service  Azure  Environment](/documentation/articles/app-service-web-configure-an-app-service-environment/).

![][4]

In this example you see only two worker pools available. That is because the ASE administrator only allocated hosts into those two worker pools.  The third would show up when there are VMs allocated into it.  

## After web app creation

There are a few considerations for running web apps and managing App Service plans in an ASE that need to be taken into account.  

As noted earlier, the owner of the ASE is responsible for the size of the system and as a result they are also responsible for ensuring that there is sufficient capacity to host the desired App Service plans. If there are no available workers, you will not be able to create your App Service plan.  This is also true to scaling up your web app.  If you need more instances then you would have to get  your App Service Environment  your Azure Environment  admin to add more workers.

After creating your web app and App Service plan it is a good idea to scale it up.  In an ASE you always need to have at least 2 instances of your App Service plan to provide fault tolerance for your apps.  Scaling an App Service plan in an ASE is the same as normal through the App Service plan UI.  For more information about scaling, [How to scale a web app in  an App Service  an Azure  Environment](/documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment/)

<!--Image references-->
[1]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspnewwebapp.png
[2]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createasplocation.png
[3]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspselected.png
[4]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspworkerpool.png
[5]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/selectaspinase.png

<!--Links-->
[WhatisASE]: /documentation/articles/app-service-app-service-environment-intro/
[Appserviceplans]: /documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/
[HowtoCreateASE]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[HowtoScale]:  /documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment  /documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment/ 
[HowtoConfigureASE]:  /documentation/articles/app-service-web-configure-an-app-service-environment  /documentation/articles/app-service-web-configure-an-app-service-environment/ 
[ResourceGroups]: /documentation/articles/resource-group-portal/
[AzurePowershell]: /documentation/articles/powershell-install-configure/