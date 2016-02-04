<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Create an Orchard CMS web site from the Azure Marketplace" 
	description="A tutorial that teaches you how to create a new web site in Azure. Also learn how to launch and manage your web site using the Azure Management Portal." 
	tags="azure-portal"
	services="app-service\web" 
	documentationCenter=".net" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="08/03/2015"
	wacn.date=""/>

# Create an Orchard CMS web site from the Azure Marketplace

## Overview

The Marketplace makes available a wide range of popular web sites developed by Microsoft, third party companies, and open source software initiatives. web sites created from the Marketplace do not require installation of any software other than the browser used to connect to the [Azure preview portal](https://manage.windowsazure.cn/). For more information about the web sites in the Marketplace, see [Azure Marketplace](/marketplace/).

In this tutorial, you'll learn:

- How to create a new web site from the Marketplace

- How to launch and manage your web site from the Azure Management Portal
 
You'll build an Orchard CMS web site that uses a default template. [Orchard](http://www.orchardproject.net/) is a free, open-source, .NET-based CMS application that allows you to create customized, content-driven web sites and websites. Orchard CMS includes an extensibility framework through which you can [download additional modules and themes](http://gallery.orchardproject.net/) to customize your web site. The following illustration shows the Orchard CMS web site in [Azure Websites](/documentation/services/web-sites/) that you will create.

![Orchard blog][13]

[AZURE.INCLUDE [create-account-and-websites-note](../includes/create-account-and-websites-note.md)]

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web site in Azure Websites. No credit cards required; no commitments.

## Create an Orchard web site from the Marketplace

1. Login to the [Azure preview portal](http://manage.windowsazure.cn).

2. Click **New** > **Web + Mobile** > **Azure Marketplace**.
	
	![Create New][1]

3. Click **Web Apps** > **Orchard CMS**. In the next blade, click **Create**.
	
	![Create From Marketplace][2]

4. Configure the web site's URL, App Service plan, resource group, and location. When you're done, click **Create**.
	
	![Configure the app][3]

	Once your web site is created, the **Notifications** button will show a green "SUCCESS" and your web site's blade will be displayed.

## Launch and manage your Orchard web site

1. In your web site's blade, click **Browse** to open your web site's welcome page.

	![browse button][12]

2. Enter the configuration information required by Orchard, and then click **Finish Setup** to complete the configuration and open the web site's home page.

	![login to Orchard][7]

	You'll have a new Orchard web site that looks similar to the screenshot below.  

	![your Orchard web site][13]

3. Follow the details in the [Orchard Documentation](http://docs.orchardproject.net/) to learn more about Orchard and configure your new web site.

## Next steps

* [Create an ASP.NET MVC app with auth and SQL DB and deploy to Azure Websites](/documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database)-- Learn how to create a new web site in Azure Websites from Visual Studio.

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the portal to the preview portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

[1]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-01.png
[2]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-02.png
[3]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-03.png
[4]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-04.png
[5]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-05.png
[7]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-07.png
[12]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-12.png
[13]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-08.png


 
