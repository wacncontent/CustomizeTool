<properties 
	pageTitle="Add a Java application to Azure Websites" 
	description="This tutorial shows you how to add a page or application to your instance of Azure Websites that is already configured to use Java." 
	services="app-service\web" 
	documentationCenter="java" 
	authors="rmcmurray" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service-web"
	ms.date="11/19/2015"
	wacn.date=""/>

# Add a Java application to Azure Websites

Once you have initialized your Java web site in [Azure Websites][] as documented at [Create a Java web site in Azure Websites](/documentation/articles/web-sites-java-get-started), you can upload your application by placing your WAR in the **webapps** folder.

The navigation path to the **webapps** folder differs based on how you set up your web sites instance.

- If you set up your web site by using the Azure Marketplace, the path to the **webapps** folder is in the form **d:\home\site\wwwroot\bin\application\_server\webapps**, where **application\_server** is the name of the application server in effect for your web sites instance. 
- If you set up your web site by using the Azure configuration UI, the path to the **webapps** folder is in the form **d:\home\site\wwwroot\webapps**. 

Note that you can use source control to upload your application or web pages, including continuous integration scenarios. Instructions for using source control with your web site are available at [Continuous deployment using GIT in Azure Websites](/documentation/articles/web-sites-publish-source-control). FTP is also an option for uploading your application or web pages.

Note for Tomcat web sites: Once you've uploaded your WAR file to the **webapps** folder, the Tomcat application server will detect that you've added it and will automatically load it. Note that if you copy files (other than WAR files) to the ROOT directory, the application server will need to be restarted before those files are used. The autoload functionality for the Tomcat Java web sites running on Azure is based on a new WAR file being added, or new files or directories added to the **webapps** folder. 

## Next steps

For more information, see the [Java Developer Center](/develop/java/).

[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

<!-- External Links -->
[Azure Websites]: /documentation/services/web-sites/
