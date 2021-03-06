<properties
	pageTitle="Create a Java web app in Azure Websites | Windows Azure"
	description="This tutorial shows you how to deploy a Java web app to Azure Websites."
	services="app-service\web"
	documentationCenter="java"
	authors="rmcmurray"
	manager="wpickett"
	editor="jimbe"/>
<tags
	ms.service="app-service-web"
	ms.date="08/31/2015"
	wacn.date=""/>

# Create a Java web app in Azure Websites

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows how to create a web app on Windows Azure by using Java, through either the Azure Marketplace or the configuration UI in the [Web Apps feature in Azure Websites][].

If you don't want to use either of those techniques—for example, if you want to customize your application container—see [Upload a custom Java web app to Azure](/documentation/articles/web-sites-java-custom-upload).

> [AZURE.NOTE] To complete this tutorial, you need a Windows Azure account. If you don't have an account, you can [sign up for a trial][].

## Create a Java web app by using the Azure configuration UI

This information shows how to use the Azure configuration UI to select a Java application container, either Apache Tomcat or Jetty, for your web app.
1. Log in to the Windows Azure Management Portal.
2. Click **New**, click **Compute**, click **Website**, and then click **Quick Create**.
3. Specify the URL name.
4. Select a region. For example, **Chian East**.
5. Click **Complete**. Within a few moments, your website will be created. To view the website, within the Azure Management Portal, in the **Websites** view, wait for the status to show as **Running** and then click the URL for the website.
6. Still within the Azure Management Portal, in the **Websites** view, click the name of your website to open the 
dashboard.
7. Click **Configure**.
8. In the **General** section, enable **Java** by clicking the available version.
9. The options for the web container are displayed, for example, Tomcat and Jetty. Select the web container that you want to use. 
10. Click **Save**. 
Within a few moments, your web app will become Java-based. To confirm that it is Java-based, click its URL. Note that the page will provide text stating that the new web app is a Java-based web app.

Now that you've created the web app with an app container, see the **Next steps** section for information about uploading your application to the web app.

## Next steps

At this point, you have a Java application server running as your Java web app on Azure. To add in your own application or webpage, see [Add an application or webpage to your Java web app](/documentation/articles/web-sites-java-add-app).

<!-- External Links -->
[activate your MSDN subscriber benefits]: /pricing/1rmb-trial/
[sign up for a trial]: /pricing/1rmb-trial/
[Web Apps feature in Azure Websites]: /documentation/services/web-sites/
[Try Azure Websites]: https://tryappservice.azure.com/
[Azure Websites and existing Azure services]: /documentation/services/web-sites/
[Reference for navigating the Azure Management Portal]: https://manage.windowsazure.cn/
