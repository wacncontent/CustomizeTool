<properties
	pageTitle="Create a Java web app in Azure | Windows Azure"
	description="This tutorial shows you how to deploy a Java web app to Azure."
	services="app-service\web"
	documentationCenter="java"
	authors="rmcmurray"
	manager="wpickett"
	editor=""/>
<tags
	ms.service="app-service-web"
	ms.date="01/09/2016"
	wacn.date=""/>

# Create a Java web app in Azure

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows how to create a Java [web app in Azure](/documentation/services/web-sites/) by using the [Azure Management Portal](https://manage.windowsazure.cn/). 

> [AZURE.NOTE] To complete this tutorial, you need a Windows Azure account. If you don't have an account, you can [sign up for a trial][].
>

## Java application options

There are several ways you can set up a Java application in an Azure web app. 

1. Create an app and then use the Azure configuration UI.

	Azure Websites provides several Tomcat and Jetty versions, with default configuration. If the application that you will be hosting will work with one of the built-in versions, this method of setting up a web container is the easiest but it lacks the configuration capabilities in other methods. For this method, you create an app in the Azure Management Portal, and then go to the app's **Configure** blade to choose your version of Java along with the desired Java web container. When you use this method the app runs from the local hard drive that is used by the worker to host the app, which does not take disk space away from the tenant. When you use this model, you don't have access to edit files in this part of the file system, which means you can't do things like configure the *server.xml* file or place library files in the */lib* folder.  For more information, see the [Create and configure a Java web site](#appsettings) section later in this tutorial.  
  
3. Create an app and then manually copy and edit configuration files 

	You might want to host a custom Java application that does not deploy in any of the web containers provided by Azure Web App.  For example, here are some reasons for doing this:
	
	* Your Java application requires a version of Tomcat or Jetty that isn't directly supported by Azure or provided in the gallery.
	* Your Java application takes HTTP requests and does not deploy as a WAR into a pre-existing web container.
	* You want to configure the web container from scratch yourself. 
	* You want to use a version of Java that isn't supported in Azure and want to upload it yourself.

	For cases like these, you can create an app using the Azure Management Portal, and then provide the appropriate runtime files manually. In this case the files will be counted against your storage space quotas for your App Service plan. For more information, see [Upload a custom Java web app to Azure](/documentation/articles/web-sites-java-custom-upload/).

## <a name="portal"></a> Create and configure a Java web app

This information shows how to use the Azure configuration UI to select a Java application container, either Apache Tomcat or Jetty, for your web site.

1. Log in to the Windows [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **New**, click **Compute**, click **Website**, and then click **Quick Create**.
3. Specify the URL name.
4. Select a region. For example, **China East**.
5. Click **Complete**. Within a few moments, your website will be created. To view the website, within the Azure Management Portal, in the **Websites** view, wait for the status to show as **Running** and then click the URL for the website.
6. Still within the Azure Management Portal, in the **Websites** view, click the name of your website to open the 
dashboard.
7. Click **Configure**.
8. In the **General** section, enable **Java** by clicking the available version.
9. The options for the web container are displayed, for example, Tomcat and Jetty. Select the web container that you want to use. 
10. Click **Save**. 

Within a few moments, your web site will become Java-based. To confirm that it is Java-based, click its URL. Note that the page will provide text stating that the new web site is a Java-based web site.

Now that you've created the web site with an app container, see the **Next steps** section for information about uploading your application to the web site.

## Next steps

At this point, you have a Java application server running in your web app in Azure. To deploy your own code to the web app, see [Add an application or webpage to your Java web app](/documentation/articles/web-sites-java-add-app).

For more information about developing Java applications in Azure, see the [Java Developer Center](/develop/java/).

<!-- External Links -->
[activate your Visual Studio subscriber benefits]: /pricing/1rmb-trial/
[sign up for a trial]: /pricing/1rmb-trial/

[Try Azure Web App]: https://tryappservice.azure.com/
