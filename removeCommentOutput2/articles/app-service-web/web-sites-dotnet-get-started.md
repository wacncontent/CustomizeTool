<properties
	pageTitle="Create an ASP.NET web app in Azure | Azure"
	description="This tutorial shows you how to create an ASP.NET web project in Visual Studio 2013 and deploy it to a web app in Azure."
	services="app-service\web"
	documentationCenter=".net"
	authors="tdykstra"
	manager="wpickett"
	editor="jimbe"/>

<tags
	ms.service="app-service-web"
	ms.date="12/07/2015"
	wacn.date=""/>

# Create an ASP.NET web app in Azure

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

## Overview

This tutorial shows how to deploy an ASP.NET web application to a [web app in Azure](/home/features/web-site) by using Visual Studio 2015 or Visual Studio 2013. The tutorial assumes that you are an ASP.NET developer who has no prior experience with using Azure. On completing the tutorial, you'll have a simple web application up and running in the cloud.

The following illustration shows the completed application:

![Web app home page](./media/web-sites-dotnet-get-started/deployedandazure.png)

You'll learn:

* How to prepare your machine for Azure development by installing the [Azure SDK for .NET](/documentation/articles/dotnet-sdk).
* How to set up Visual Studio to create a new Azure web app while it creates an ASP.NET MVC 5 web project.
* How to deploy a web project to an Azure web app by using Visual Studio.
* How to use Visual Studio **Server Explorer** to open remote files and start a remote debug session. 
* How to use the [Azure Management Portal](https://manage.windowsazure.cn) to monitor and manage your web app.

> [AZURE.NOTE] This tutorial is about using ASP.NET with Azure Web App; it doesn't teach how to develop an ASP.NET web application. For an introduction to ASP.NET MVC 5, see [Getting Started with ASP.NET MVC 5](http://www.asp.net/mvc/overview/getting-started/introduction/getting-started) on the [ASP.NET](http://asp.net/) site. For links to other articles that go into more depth about how to use Azure Web App, see the [Next steps](#next-steps) section.

##<a name="video"></a>Sign up for Azure

You need an Azure account to complete this tutorial. You can:

* [Open an Azure account for free](/pricing/1rmb-trial/?WT.mc_id=A261C142F). You get credits that can be used to try out paid Azure services. Even after the credits are used up, you can keep the account and use free Azure services and features, such as the Web Apps feature in Azure Web App.


<a name="set-up-the-development-environment"></a>
[AZURE.INCLUDE [install-sdk-2015-2013](../includes/install-sdk-2015-2013.md)]


##<a name="create-an-aspnet-web-application"></a> Create a project and a web app

Your first step is to create a web project in Visual Studio and a web app in Azure. When that's done, you'll deploy the project to the web app to make it available on the Internet. 

The diagram illustrates what you're doing in the create and deploy steps.

![Create and deploy](./media/web-sites-dotnet-get-started/Create_App.png)

1. Open Visual Studio 2015 or Visual Studio 2013.

	If you use Visual Studio 2013, the screens will be slightly different from the screenshots, but the procedures are essentially the same.

2. From the **File** menu, click **New > Project**.

3. In the **New Project** dialog box, click **C# > Web > ASP.NET Web Application**. If you prefer, you can choose **Visual Basic**.

3. Make sure that **.NET Framework 4.5.2** is selected as the target framework.

4. Name the application **MyExample**.

5. Click **OK**.

	![New Project dialog box](./media/web-sites-dotnet-get-started/GS13newprojdb.png)

5. In the **New ASP.NET Project** dialog box, select the **MVC** template.

	[MVC](http://www.asp.net/mvc) is an ASP.NET framework for developing web apps.


5. In the **New ASP.NET Project** dialog box, make sure that the **Host in the cloud** is unchecked, and then click **OK**.

	![New ASP.NET Project dialog box](./media/web-sites-dotnet-get-started/GS13newaspnetprojdb.png)

	Azure China currently does not support create or manage websits in Visual Studio. Hence, you need to go to the [Management Portal](https://manage.windowsazure.cn/) to create a new Azure website

	The **Solution Explorer** window shows the files and folders in the new project.

	![Solution Explorer](./media/web-sites-dotnet-get-started/solutionexplorer.png)



##<a name="deploy-the-application-to-azure"></a> Deploy the project to the web site

In this section you deploy web project to the web app, as illustrated in step 2 of the diagram.

![Create and deploy](./media/web-sites-dotnet-get-started/Create_App.png)


1. In the [Management Portal](https://manage.windowsazure.cn/), create a new website or choose an exited website.

2. Click the **Dashboard** of the website. Under the **quick glance**, click **Download publish profile**.

3. In Visual Studio, right click you project and choose **Publish**

	![choose "publish"](./media/web-sites-dotnet-get-started/choosepublish.png)

	In a few seconds, the **Publish Web** wizard appears.

4. In **Publish Profile**, click **Import**, and choose the publish profile downloaded above.

	Settings that Visual Studio needs to deploy your project to Azure have been imported. You can use the wizard to review and change those settings.

8. On the **Connection** tab of the **Publish Web** wizard, click **Next**.

	![Successfully validated connection](./media/web-sites-dotnet-get-started/GS13ValidateConnection.png)

10. On the **Settings** tab, click **Next**.

	You can accept the default values for **Configuration** and **File Publish Options**.

	You can use the **Configuration** drop-down to deploy a Debug build for remote debugging. The [Next steps](#next-steps) section links to a tutorial that shows how to run Visual Studio in debug mode remotely.

	![Settings tab](./media/web-sites-dotnet-get-started/GS13SettingsTab.png)

11. On the **Preview** tab, click **Publish**.

	If you want to see what files will be copied to Azure, you can click **Start Preview** before clicking **Publish**.

	![](./media/web-sites-dotnet-get-started/GS13previewoutput.png)

	When you click **Publish** Visual Studio begins the process of copying the files to the Azure server.

	The **Output** and **Azure Activity** windows show what deployment actions were taken and report successful completion of the deployment.

	![Output window reporting successful deployment](./media/web-sites-dotnet-get-started/PublishOutput.png)

	Upon successful deployment, the default browser automatically opens to the URL of the deployed web app, and the application that you created is now running in the cloud. The URL in the browser address bar shows that the web app is loaded from the Internet.

	![Web app running in Azure](./media/web-sites-dotnet-get-started/GS13deployedsite.png)

13. Keep this browser window open for use in the next section.

**Tip:** You can enable the **Web One Click Publish** toolbar for quick deployment. Click **View > Toolbars**, and then select **Web One Click Publish**. You can use the toolbar to select a profile, click a button to publish, or click a button to open the **Publish Web** wizard.

![Web One Click Publish Toolbar](./media/web-sites-dotnet-get-started/weboneclickpublish.png)


##<a name="open-remote-files-in-server-explorer"></a> Open remote files in Server Explorer

When you're testing and debugging a web app, you can do quick temporary changes on the remote site by opening and editing files in **Server Explorer**.

1.  In **Server Explorer**, navigate to **Azure > Azure > MyExampleGroup**, and then expand the node for your web app.

2. Expand **Files > Views > Home**, and then double-click the *Index.cshtml* file.

	![](./media/web-sites-dotnet-get-started/indexfileinse.png)

3. Change `<h1>ASP.NET</h1>` to `<h1>Azure Web App</h1>`.

4. Save the file.

5. Refresh the browser window that has the site running in Azure. 

	![](./media/web-sites-dotnet-get-started/afterindexedit.png)

This change is now in the deployed site but not the local project. If you redeploy the project, the site will revert to the way it was before you made this change.

This feature is handy for [temporarily turning off customErrors in the Web.config file in order to get a detailed error message](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

In **Server Explorer** you can also right-click the Azure node and get access to web app settings in a Visual Studio window, start a remote debugging session, and view application logs in real time as the application writes them.

![](./media/web-sites-dotnet-get-started/sewebappmenu.png)

For more information, see [Troubleshooting Azure web apps in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

## Monitor and manage the web app in the Azure Management Portal

The [Azure Management Portal](/home/features/management-portal/) is a web interface that you can use to manage and monitor your Azure services, such as the web app that you just created. In this section of the tutorial, you look at some of what you can do in the Portal.

1. In your browser, go to [https://manage.windowsazure.cn](https://manage.windowsazure.cn), and sign in with your Azure credentials.


	The portal displays a list of your Azure services.

2. Click the name of your website.

	![Portal home page with new web site called out](./media/web-sites-dotnet-get-started-vs2013/portalhome.png)
  
3. Click the **Dashboard** tab.

	The **Dashboard** tab displays an overview of usage statistics and link for a number of commonly used site management functions. Under **Quick Glance** you'll also find a link to your application's home page.

	![Portal web site dashboard tab](./media/web-sites-dotnet-get-started-vs2013/portaldashboard.png)
  
	At this point your site hasn't had much traffic and may not show anything in the graph. If you browse to your application, refresh the page a few times, and then refresh the portal **Dashboard** page, you'll see some statistics show up. You can click the **Monitor** tab for more details.

4. Click the **Configure** tab.

	The [Configure](/documentation/articles/web-sites-configure//) tab enables you to control the .NET version used for the site, enable features such as [WebSockets](http://www.windowsazure.cn/blog/2013/11/14/introduction-to-websockets-on-windows-azure-web-sites/) and [diagnostic logging](/documentation/articles/web-sites-enable-diagnostic-log), set [connection string values](http://azure.microsoft.com/blog/2013/07/17/windows-azure-web-sites-how-application-strings-and-connection-strings-work/), and more. 

	![Portal web site configure tab](./media/web-sites-dotnet-get-started-vs2013/portalconfigure.png)
  
5. Click the **Scale** tab.

	For the paid tiers of the  Websites service, the [Scale](/documentation/articles/web-sites-scale) tab enables you to control the size and number of machines that service your web site in order to handle variations in traffic.

	You can scale manually or configure criteria or schedules for automatic scaling.

	![Portal website scale tab](./media/web-sites-dotnet-get-started-vs2013/portalscale.png)

These are just a few of the Portal's features. You can create new web apps, delete existing web apps, stop and restart web apps, and manage other kinds of Azure services, such as databases and virtual machines.  


##<a name="next-steps"></a> Next steps

In this tutorial, you've seen how to create a simple web application and deploy it to an Azure web app. Here are some related topics and resources for learning more about web apps in Azure:

* How to add database and authorization functionality

	For a tutorial that shows how to access a database and restrict some application functions to authorized users, see [Deploy a secure ASP.NET MVC app with membership, OAuth, and SQL Database to an Azure web app](/documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database/). That tutorial assumes some knowledge of MVC 5; if you are new to MVC 5, see [Getting Started with ASP.NET MVC 5](http://www.asp.net/mvc/overview/getting-started/introduction/getting-started).

* Other ways to deploy a web project

	For information about other ways to deploy web projects to web apps, by using Visual Studio or by [automating deployment](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/continuous-integration-and-continuous-delivery) from a [source control system](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/source-control), see [How to deploy an Azure web app](/documentation/articles/web-sites-deploy).

	Visual Studio can also generate Windows PowerShell scripts that you can use to automate deployment. For more information, see [Automate Everything (Building Real-World Cloud Apps with Azure)](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/automate-everything).

* How to troubleshoot a web app

	Visual Studio provides features that make it easy to view Azure logs as they are generated in real time. You can also run in debug mode remotely in Azure. For more information, see [Troubleshooting Azure web apps in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

* How to add a custom domain name and SSL

	For information about how to use SSL and your own domain (for example, www.contoso.com instead of contoso.chinacloudsites.cn), see the following resources:

	* [Configure a custom domain name in Azure Web App](/documentation/articles/web-sites-custom-domain-name)
	* [Enable HTTPS for an Azure website](/documentation/articles/web-sites-configure-ssl-certificate)

* How to add real-time features such as chat

	If your web app will include real-time features (such as a chat service, a game, or a stock ticker), you can get the best performance by using [ASP.NET SignalR](http://www.asp.net/signalr) with the [WebSockets](/blog/2013/11/transport method. For more information, see [Using SignalR with Azure web apps](http://www.asp.net/signalr/overview/signalr-20/getting-started-with-signalr-20/using-signalr-with-windows-azure-web-sites).

* How to choose between Azure Web App, Azure Cloud Services, and Azure Virtual Machines for web applications

	In Azure, you can run web applications in Azure Web Apps as shown in this tutorial, or in Cloud Services or in Virtual Machines. For more information, see [Azure web apps, cloud services, and VMs: When to use which?](/documentation/articles/choose-web-site-cloud-service-vm/).

* [How to choose or create an App Service plan](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview)

