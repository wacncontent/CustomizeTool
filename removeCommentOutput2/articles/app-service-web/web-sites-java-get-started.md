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
	ms.date="10/20/2015"
	wacn.date=""/>

# Create a Java web app in Azure Websites

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows how to create a Java [web app in Azure Websites](/documentation/services/web-sites/) by using the [Azure preview portal](https://manage.windowsazure.cn/). The Azure preview portal is a web interface that you can use to manage Azure resources.

> [AZURE.NOTE] To complete this tutorial, you need a Windows Azure account. If you don't have an account, you can [activate your MSDN subscriber benefits][] or [sign up for a trial][].
>
> If you want to get started with Azure Websites before you sign up for an Azure account, go to [Try Azure Websites][]. There, you can immediately create a short-lived starter web app in Azure Websites—no credit card required, and no commitments.

## Java application options

10. Click **Application settings**.

11. Choose the desired **Java version**. 
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

	![](./media/web-sites-java-get-started/versions.png)

13. Click **Save**.

	Within a few moments, your web app will become Java-based and configured to use the web container you selected.

14. Click **Web apps > {your new web app}**.

15. Click the **URL** to browse to the new site.

	The web page confirms that you have created a Java-based web app.

## Next steps

At this point, you have a Java application server running in your web app in Azure Websites. To deploy your own code to the web app, see [Add an application or webpage to your Java web app](/documentation/articles/web-sites-java-add-app).

<!-- External Links -->
[activate your MSDN subscriber benefits]: /pricing/1rmb-trial/
[sign up for a trial]: /pricing/1rmb-trial/

[Try Azure Websites]: https://tryappservice.azure.com/
