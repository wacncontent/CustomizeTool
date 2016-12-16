<!-- deleted in Global -->

<properties 
	pageTitle="Create a digital marketing campaign on Azure Web Apps" 
	description="This guide provides a technical overview of how to use Azure Web Apps to create digital marketing campaigns. This includes deployment, social media integration, scaling strategies, and monitoring." 
	editor="jimbe" 
	manager="wpickett" 
	authors="cephalin" 
	services="app-service\web" 
	documentationCenter=""/>

<tags
	ms.service="app-service-web"
	ms.date="02/26/2016"
	wacn.date=""/>

# Create a digital marketing campaign on Azure Web Apps
[Azure Web App](/documentation/services/web-sites/) Web Apps is a great choice for digital marketing campaigns. Digital marketing campaigns are typically short-lived and are meant to drive short-term marketing goals. There are two main scenarios to consider. In the first scenario, a third-party marketing firm creates and manages the campaign for their customer for the duration of the promotion. A second scenario involves the marketing firm creating and then transferring ownership of the digital marketing campaign resources to their customer. The customer then runs and manages the digital marketing campaign on their own. is a good match for both scenarios. 

Below is an example of a global, multi-channel digital marketing campaign using Azure Web Apps. It demonstrates what you can do simply by composing Azure Web Apps together with other services with minimal technical investments. **Click on an element in the topography to read more about it.** 

<object type="image/svg+xml" data="./media/web-sites-digital-marketing-application-solution-overview/digital-marketing-notitle.svg" width="100%" height="100%"></object>

> [AZURE.NOTE]
> This guide presents some of the most common areas and tasks that are aligned with running a digital marketing campaign in Azure Web Apps. However, there are other common solutions that you can implement in Azure Web Apps. To review these solutions, see the other guides on [Global Web Presence](/documentation/articles/web-sites-global-web-presence-solution-overview/) and [Business Applications](/documentation/articles/web-sites-business-application-solution-overview/).

## Create from scratch or bring existing assets

Quickly bring your existing web assets to Azure Web Apps from a variety of languages and frameworks.

You can create a web app using your favorite CMS flavor. You can choose from various database backends to meet your needs, including [Azure SQL Database] and [MySQL].

Your existing web assets can run on Web Apps, whether they are .NET, PHP, Java, Node.js, or Python. You can move them to Web Apps using your familiar [FTP] tools. If you frequently create digital marketing campaigns, it is possible that you have existing web assets in a source control management system. You can deploy to Web Apps directly from popular source control options, such as [Visual Studio], and [Git] - local, GitHub, Mercurial, etc..

## Stay agile

Stay agile by continuously publishing directly from your existing source control and run A/B tests in Azure Web Apps. 

During the planning, prototyping, and early development of a web app, you and your customer can look at real working versions of the campaign app before it goes live by [deploying to a staging slot] of your web app. By integrating source control with Azure Web Apps, you can [continuously publish] to a staging slot, and swap it into production with no downtime when it is ready. 

Also, when planning changes to a live web app, you can easily [run A/B tests] on the proposed updates using the Test in Production feature in and analyze real user behavior to help you make informed decisions on app design.


## Go social

Your digital marketing campaign in Azure Web Apps can integrate with social media by authenticating with popular providers. For an example of this approach with an ASP.NET application, see [Create an ASP.NET MVC app with auth and SQL DB and deploy to Azure Web App]. 

Furthermore, each social media site typically provides information on other ways to integrate with it from .NET and many other frameworks.

## Use rich media and reach all devices

Enrich your digital marketing campaign with other Azure services, such as:

-  Upload and stream videos globally with [Azure Media Services]
-  Establish presence on Windows, iOS, and Android devices with [Mobile Services]
-  Send push notification to millions of devices with [Notification Hub]

## Go global

Go global by serving regional sites with Azure Traffic Manager and delivering content lightning fast with Azure CDN.

To serve global customers in their respective regions, use [Azure Traffic Manager] to route site visitors to a regional site that provides the best performance. Alternatively, you can spread the site load evenly across multiple copies of your web app hosted in multiple regions.

Deliver your static content lightning fast to users globally by [integrating your web app with Azure CDN]. Azure CDN caches static content in the [CDN node] closest to the user, which minimizes latency and connections to your web app.

## Optimize

Optimize your web app by scaling automatically with Autoscale, caching with Azure Redis Cache, running background tasks with WebJobs, and maintaining high availability with Azure Traffic Manager.

The ability of Azure Web Apps to [scale up and out] is perfect for unpredictable workloads, which is the case with digital marketing campaigns. Scale out your web app manually through the [Azure Classic Management Portal](https://manage.windowsazure.cn/), programmatically through the [Service Management API] or [PowerShell scripting], or automatically through the Autoscale feature. In the **Standard** tier, Autoscale enables you to scale out a web app automatically based on CPU utilization. This feature helps you maximize agility and minimize cost at the same time by scaling out the web app only when needed based on user activity. For best practices, see [Troy Hunt]'s [10 things I learned about rapidly scaling web apps with Azure].

Make your web app more responsive with the [Azure Redis Cache]. Use it to cache data from backend databases and other things such as the [ASP.NET session state] and [output cache].

Maintain high availability of your web app using [Azure Traffic Manager]. Using the **Failover** method, Traffic Manager automatically routes traffic to a secondary site if there is a problem on the primary site.

## Monitor and analyze

Stay up-to-date on your web app's performance with Azure or third-party tools. Receive alerts on critical web app events. Gain user insight easily with Application Insight or with web log analytics from HDInsight. 

In the **Standard** tier, monitor app responsiveness receive email notifications whenever your web app becomes unresponsive. For more information, see [How to: Receive Alert Notifications and Manage Alert Rules in Azure].

## More Resources

- [Azure Web Apps Documentation](/home/features/web-site/)
- [Azure Web Blog](/blog/tags/网站/)

[Azure Web App]: /home/features/web-site/

[MySQL]: /documentation/articles/web-sites-php-mysql-deploy-use-git/
[Azure SQL Database]: /documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database/
[FTP]: /documentation/articles/web-sites-deploy/#ftp
[Visual Studio]: /documentation/articles/web-sites-dotnet-get-started/
[Git]: /documentation/articles/web-sites-publish-source-control/

[deploying to a staging slot]: /documentation/articles/web-sites-staged-publishing/
[continuously publish]:http://rickrainey.com/2014/01/21/continuous-deployment-github-with-azure-web-sites-and-staged-publishing/
[run A/B tests]:http://blogs.msdn.com/b/tomholl/archive/2014/11/10/a-b-testing-with-azure-websites.aspx

[Create an ASP.NET MVC app with auth and SQL DB and deploy to Azure Web App]: /documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database/

[Azure Media Services]:http://blogs.technet.com/b/cbernier/archive/2013/09/03/windows-azure-media-services-and-web-sites.aspx
[Mobile Services]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users/
[Notification Hub]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users/

[Azure Traffic Manager]:http://www.hanselman.com/blog/CloudPowerHowToScaleAzureWebsitesGloballyWithTrafficManager.aspx
[integrating your web app with Azure CDN]: /documentation/articles/cdn-websites-with-cdn/
[CDN node]:https://msdn.microsoft.com/zh-cn/library/azure/gg680302.aspx

[scale up and out]:/manage/services/web-sites/how-to-scale-websites/
[Azure Classic Management Portal]:http://manage.windowsazure.cn/
[Service Management API]:http://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx
[PowerShell scripting]:http://msdn.microsoft.com/zh-cn/library/azure/jj152841.aspx
[Troy Hunt]:https://twitter.com/troyhunt
[10 things I learned about rapidly scaling web apps with Azure]:http://www.troyhunt.com/2014/09/10-things-i-learned-about-rapidly.html
[Azure Redis Cache]:/blog/2014/06/05/mvc-movie-app-with-azure-redis-cache-in-15-minutes/
[ASP.NET session state]:https://msdn.microsoft.com/zh-cn/library/azure/dn690522.aspx
[output cache]:https://msdn.microsoft.com/zh-cn/library/azure/dn798898.aspx

[quick glance]:/documentation/articles/web-sites-monitor/
[Azure Application Insights]:http://blogs.msdn.com/b/visualstudioalm/archive/2015/01/07/application-insights-and-azure-websites.aspx
[New Relic]:/develop/net/how-to-guides/new-relic/
[How to: Receive Alert Notifications and Manage Alert Rules in Azure]:http://msdn.microsoft.com/zh-cn/library/azure/dn306638.aspx

  
  [gitstaging]:http://www.bradygaster.com/post/multiple-environments-with-windows-azure-web-sites  
 
