<properties
	pageTitle="Create a Java web app in Azure | Azure"
	description="This tutorial shows you how to deploy a Java web app to Azure."
	services="app-service\web"
	documentationCenter="java"
	authors="rmcmurray"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="06/01/2016"
	wacn.date=""/>

# Create a Java web app in Azure

[AZURE.INCLUDE [tabs](../includes/app-service-web-get-started-nav-tabs.md)]

This tutorial shows how to create a Java [web app in Azure](/documentation/services/web-sites/) by using the [Azure Classic Management Portal](https://manage.windowsazure.cn/). The Azure Classic Management Portal is a web interface that you can use to manage your Azure resources.

> [AZURE.NOTE] To complete this tutorial, you need a Azure account. If you don't have an account, you can [sign up for a trial].
>

## Java application options

There are several ways you can set up a Java application in an Azure web app. 

1. Create an app and then use the Azure configuration UI.

	Azure Websites provides several Tomcat and Jetty versions, with default configuration. If the application that you will be hosting will work with one of the built-in versions, this method of setting up a web container is the easiest but it lacks the configuration capabilities in other methods. For this method, you create an app in the Azure Classic Management Portal, and then go to the app's **Configure** blade to choose your version of Java along with the desired Java web container. When you use this method the app runs from    the local hard drive that is used by the worker to host the app, which does not take disk space away from the tenant.  When you use this model, you don't have access to edit files in this part of the file system, which means you can't do things like configure the *server.xml* file or place library files in the */lib* folder.
  
3. Create an app and then manually copy and edit configuration files 

	You might want to host a custom Java application that does not deploy in any of the web containers provided by Azure Web App. For example:
	
	* Your Java application requires a version of Tomcat or Jetty that isn't directly supported by Azure or provided in the gallery.
	* Your Java application takes HTTP requests and does not deploy as a WAR into a pre-existing web container.
	* You want to configure the web container from scratch yourself. 
	* You want to use a version of Java that isn't supported in Azure and want to upload it yourself.

	For cases like these, you can create an app using the Azure Classic Management Portal and then provide the appropriate runtime files manually. In this case, the files will be counted against your storage space quotas for your App Service plan. For more information, see [Upload a custom Java web app to Azure](/documentation/articles/web-sites-java-custom-upload/).

## <a name="portal"></a> Create and configure a Java web app

This information shows how to use the Azure configuration UI to select a Java application container, either Apache Tomcat or Jetty, for your web app.

1. Log in to the Windows [Azure Classic Management Portal](https://manage.windowsazure.cn/).
2. Click **New**, click **Compute**, click **Website**, and then click **Quick Create**.
3. Specify the URL name.
4. Select a region. For example, **China East**.
5. Click **Complete**. Within a few moments, your website will be created. To view the website, within the Azure Classic Management Portal, in the **Websites** view, wait for the status to show as **Running** and then click the URL for the website.
6. Still within the Azure Classic Management Portal, in the **Websites** view, click the name of your website to open the 
dashboard.
7. Click **Configure**.
8. In the **General** section, enable **Java** by clicking the available version.
9. The options for the web container are displayed, for example, Tomcat and Jetty. Select the web container that you want to use. 
10. Click **Save**. 

Within a few moments, your web app will become Java-based. To confirm that it is Java-based, click its URL. Note that the page will provide text stating that the new web app is a Java-based web app.

Now that you've created the web app with an app container, see the [Next steps](#next-steps) section for information about how to upload your application to the web app.

##<a name="next-steps"></a> Next steps

At this point, you have a Java application server running in your web app in Azure. To deploy your own code to the web app, see [Add an application or webpage to your Java web app](/documentation/articles/web-sites-java-add-app/).

For more information about developing Java applications in Azure, see the [Java Developer Center](/develop/java/).

<!-- URL List -->

[Add an application or webpage to your Java web app]: /documentation/articles/web-sites-java-add-app/
[Azure App Service plans overview]: /documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/
[Azure Portal Preview]: https://portal.azure.cn/
[activate your Visual Studio subscriber benefits]: /pricing/1rmb-trial/
[sign up for a trial]: /pricing/1rmb-trial/
[Try Azure Web App]: https://tryappservice.azure.com/
[web app in Azure]: /documentation/services/web-sites/
[Java Developer Center]: /develop/java/
[Using the Azure Portal Preview to manage your Azure resources]: /documentation/articles/resource-group-portal/
[Upload a custom Java web app to Azure]: /documentation/articles/web-sites-java-custom-upload/

<!-- IMG List -->

[newwebapp]: ./media/web-sites-java-get-started/newwebapp.png
[newwebapp2]: ./media/web-sites-java-get-started/newwebapp2.png
[selectwebapp]: ./media/web-sites-java-get-started/selectwebapp.png
[versions]: ./media/web-sites-java-get-started/versions.png
[newmarketplace]: ./media/web-sites-java-get-started/newmarketplace.png
[webmobilejetty]: ./media/web-sites-java-get-started/webmobilejetty.png
[jettyblade]: ./media/web-sites-java-get-started/jettyblade.png
[jettyportalcreate2]: ./media/web-sites-java-get-started/jettyportalcreate2.png
[jettyurl]: ./media/web-sites-java-get-started/jettyurl.png
[tomcat]: ./media/web-sites-java-get-started/tomcat.png
[jetty]: ./media/web-sites-java-get-started/jetty.png
