<properties
    pageTitle="Debug a Java Web App on Azure in Eclipse | Azure"
    description="This tutorial shows you how to use the Azure Toolkit for Eclipse to debug a Java Web App running on Azure."
    services="app-service\web"
    documentationcenter="java"
    author="selvasingh"
    manager="wpickett"
    editor="" />
<tags
    ms.assetid="321d2d19-9ce0-4165-8555-b6b15e671393"
    ms.service="app-service-web"
    ms.workload="web"
    ms.tgt_pltfrm="na"
    ms.devlang="Java"
    ms.topic="article"
    ms.date="09/20/2016"
    wacn.date=""
    ms.author="asirveda;robmcm" />

# Debug a Java Web App on Azure in Eclipse
This tutorial shows how to debug a Java Web App running on Azure by using the [Azure Toolkit for Eclipse]. For the sake of simplicity, you will use a basic Java Server Page (JSP) example for this tutorial, but the steps would be similar for a Java servlet when you are debugging on Azure.

When you have completed this tutorial, your application will look similar to the following illustration when you are debugging it in Eclipse:

![][01]

## Prerequisites
* A Java Developer Kit (JDK), v 1.8 or later.
* Eclipse IDE for Java EE Developers, Indigo or later. This can be downloaded from <http://www.eclipse.org/downloads/>.
* A distribution of a Java-based web server or application server, such as Apache Tomcat or Jetty.
* An Azure subscription, which can be acquired from <https://azure.microsoft.com/free/> or </pricing/overview/>.
* The Azure Toolkit for Eclipse. For more information, see [Installing the Azure Toolkit for Eclipse].
* A Dynamic Web Project created and deployed to Azure App Service; for example see [Create a Hello World Web App for Azure in Eclipse].

## To Debug a Java Web App on Azure
To complete these steps in this section, you can use an existing Dynamic Web Project which you have already deployed as a Java Web App on Azure, you download a [Sample Dynamic Web Project] and follow steps in [Create a Hello World Web App for Azure in Eclipse] to deploy it on Azure. 

1. Open Eclipse.
2. Configure time-outs for remote debugging:
   
   1. Click the **Windows** menu in Eclipse, and then click **Preferences**.
   2. Expand the **Java** node, then select **Debug**.
   3. Configure both the **Debugger timeout (ms)** and **Launch timeout (ms)** settings to `120000`.
      
       ![][02]
   4. Click **OK** to close the **Preferences** dialog.
3. In  Eclipse's Project Explorer view, right click the Dynamic Web Project which you have deployed to Azure. When the context menu appears, select **Debug As**, and then click **Azure Web App**.
   
    ![][03]
4. If this is the first time you are debugging your Dynamic Web Project, the **Debug Configurations** dialog will open; you can accept the default values which are specified by the Toolkit on the **Connect** tab. On the **Source** tab, click **Add**, then **Java project**, select **Dynamic Web Project**, and then click **OK**. Once you have completed these steps, click **Debug**.
   
    ![][04]
5. When prompted to **Enable remote debugging in the remote Web App now?**, click **OK**.
6. When prompted that **Your web app is now ready for remote debugging**, click **OK**.
   
    ![][05]
7. When the **Debug Configurations** dialog reappears, click **Debug**.
8. A Windows command prompt or Unix shell will open and prepare necessary connection for debugging; you need to wait until the connection to your remote Java Web app is successful before you continue. If you are using Windows, it will look like the following illustration.
   
    ![][06]
9. Insert a break point in your JSP page, then open the URL for your Java Web App in a browser:
   
   1. Open up **Azure Explorer** in Eclipse.
   2. Navigate to **Web Apps** and the Java Web App you want to debug.
   3. Right click on the Web App, and click **Open in Browser**.
   4. Eclipse will now enter into debug mode.

## Next Steps
For more information about using Azure with Java, see the [Azure Java Developer Center].

For additional information about creating Azure Web Apps, see the [Web Apps Overview].

[AZURE.INCLUDE [app-service-web-try-app-service](../../includes/app-service-web-try-app-service.md)]

<!-- URL List -->

[Azure App Service]: /documentation/articles/app-service-changes-existing-services/
[Azure Toolkit for Eclipse]: /documentation/articles/azure-toolkit-for-eclipse/
[Installing the Azure Toolkit for Eclipse]: /documentation/articles/azure-toolkit-for-eclipse-installation/
[Create a Hello World Web App for Azure in Eclipse]: /documentation/articles/app-service-web-eclipse-create-hello-world-web-app/
[Sample Dynamic Web Project]: http://go.microsoft.com/fwlink/?LinkId=817337

[Azure Java Developer Center]: /develop/java/
[Web Apps Overview]: /documentation/articles/app-service-web-overview/

<!-- IMG List -->

[01]: ./media/app-service-web-debug-java-web-app-in-eclipse/01-debug-java-web-app-in-eclipse.png
[02]: ./media/app-service-web-debug-java-web-app-in-eclipse/02-configure-eclipse-remote-debug.png
[03]: ./media/app-service-web-debug-java-web-app-in-eclipse/03-debug-as.png
[04]: ./media/app-service-web-debug-java-web-app-in-eclipse/04-debug-configurations.png
[05]: ./media/app-service-web-debug-java-web-app-in-eclipse/05-ready-for-remote-debugging.png
[06]: ./media/app-service-web-debug-java-web-app-in-eclipse/06-windows-command-prompt-connection-successful-to-remote.png
