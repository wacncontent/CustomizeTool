<properties
    pageTitle="How to create a web app with App Service on Linux | Azure"
    description="Web app creation workflow for App Service on Linux."
    keywords="azure app service, web app, linux, oss"
    services="app-service"
    documentationcenter=""
    author="naziml"
    manager="wpickett"
    editor="" />
<tags
    ms.assetid="3a71d10a-a0fe-4d28-af95-03b2860057d5"
    ms.service="app-service"
    ms.workload="na"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/10/2016"
    wacn.date=""
    ms.author="naziml" />

# Create a web app with App Service on Linux
## Use the Azure portal to create your web app
You can start creating your web app on Linux from the [Azure portal](https://portal.azure.cn) as shown in the following image:

![Start creating a web app on the Azure portal][1]

Next, the **Create blade** opens as shown in the following image:

![The Create blade][2]

1. Give your web app a name.
2. Choose an existing resource group or create a new one. (See available regions in the [limitations section](/documentation/articles/app-service-linux-intro/).)
3. Choose an existing Azure App Service plan or create a new one. (See App Service plan notes in the [limitations section](/documentation/articles/app-service-linux-intro/).)
4. Choose the application stack that you intend to use. You can choose between several versions of Node.js and PHP.

Once you have created the app, you can change the application stack from the application settings as shown in the following image:

![Application settings][3]

## Deploy your web app
Choosing **deployment options** from the management portal gives you the option to use local a Git or GitHub repository to deploy your application. The rest of the instructions are similar to those for a non-Linux web app, and you can follow these instructions in either our [local Git deployment](/documentation/articles/app-service-deploy-local-git/) or our [continuous deployment](/documentation/articles/app-service-continuous-deployment/) article for GitHub.

You can also use FTP to upload your application to your site. You can get the FTP endpoint for your web app from the diagnostics logs section as shown in the following image:

![Diagnostics logs][4]

## Next steps
* [What is App Service on Linux?](/documentation/articles/app-service-linux-intro/)
* [Using PM2 Configuration for Node.js in Web Apps on Linux](/documentation/articles/app-service-linux-using-nodejs-pm2/)

<!--Image references-->
[1]: ./media/app-service-linux-how-to-create-a-web-app/top-level-create.png
[2]: ./media/app-service-linux-how-to-create-a-web-app/create-blade.png
[3]: ./media/app-service-linux-how-to-create-a-web-app/application-settings-change-stack.png
[4]: ./media/app-service-linux-how-to-create-a-web-app/diagnostic-logs-ftp.png
