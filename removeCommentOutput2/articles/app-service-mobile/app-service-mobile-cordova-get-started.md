<properties
    pageTitle="Create a Cordova app on Azure App Service Mobile Apps | Azure"
    description="Follow this tutorial to get started with using Azure mobile app backends for Apache Cordova development"
    services="app-service\mobile"
    documentationCenter="javascript"
    authors="adrianhall"
    manager="erikre"
    editor=""
    tags=""
    keywords="cordova,javascript,mobile,client" />

<tags
	ms.service="app-service-mobile"
	ms.date="08/11/2016"
	wacn.date=""/>

#Create an Apache Cordova app

[AZURE.INCLUDE [app-service-mobile-selector-get-started](../../includes/app-service-mobile-selector-get-started.md)]

## Overview

This tutorial shows you how to add a cloud-based backend service to an Apache Cordova mobile app by using an Azure mobile app backend.  You will create both a new mobile app backend and a simple _Todo list_ Apache Cordova app that stores app data in Azure.

Completing this tutorial is a prerequisite for all other Apache Cordova tutorials about using the Mobile Apps feature in Azure App Service.

## Prerequisites

To complete this tutorial, you need the following:

* A PC with [Visual Studio Community 2015] or newer.
* [Visual Studio Tools for Apache Cordova].
* An [active Azure account](/pricing/1rmb-trial/).

You may also bypass Visual Studio and use the Apache Cordova command line directly.  This is useful when completing the tutorial on a
Mac computer.  Compiling Apache Cordova client applications using the command line is not covered by this tutorial.

## Create a new Azure mobile app backend

[AZURE.INCLUDE [app-service-mobile-dotnet-backend-create-new-service](../../includes/app-service-mobile-dotnet-backend-create-new-service.md)]

## Configure the server project

[AZURE.INCLUDE [app-service-mobile-configure-new-backend.md](../../includes/app-service-mobile-configure-new-backend.md)]

## Download and run the Apache Cordova app

[AZURE.INCLUDE [app-service-mobile-cordova-run-app](../../includes/app-service-mobile-cordova-run-app.md)]

## Next Steps

Now that you completed this quick start tutorial, move on to one of the following tutorials:

* [Add Authentication] to your Apache Cordova app.
* [Add Push Notifications] to your Apache Cordova app.

Learn more about key concepts with Azure App Service.

* [Authentication]
* [Push Notifications]

Learn how to use the SDKs.

* [Apache Cordova SDK]
* [ASP.NET Server SDK]
* [Node.js Server SDK]

<!-- Images. -->

<!-- URLs -->
[Azure portal]: https://portal.azure.cn/
[Visual Studio Community 2015]: http://www.visualstudio.com/
[Visual Studio Tools for Apache Cordova]: https://www.visualstudio.com/features/cordova-vs.aspx
[Add Authentication]: /documentation/articles/app-service-mobile-cordova-get-started-users/
[Add Push Notifications]: /documentation/articles/app-service-mobile-cordova-get-started-push/
[Authentication]: /documentation/articles/app-service-mobile-auth/
[Push Notifications]: /documentation/articles/notification-hubs-overview/
[Apache Cordova SDK]: /documentation/articles/app-service-mobile-cordova-how-to-use-client-library/
[ASP.NET Server SDK]: /documentation/articles/app-service-mobile-dotnet-backend-how-to-use-server-sdk/
[Node.js Server SDK]: /documentation/articles/app-service-mobile-node-backend-how-to-use-server-sdk/
