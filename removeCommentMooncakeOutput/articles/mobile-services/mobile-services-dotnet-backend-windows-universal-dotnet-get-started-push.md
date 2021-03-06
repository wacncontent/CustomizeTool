<properties 
	pageTitle="Add push notifications to your universal Windows 8.1 app | Windows Azure" 
	description="Learn how to send push notifications to your universal Windows 8.1 app from your .NET backend mobile service using Azure Notification Hubs." 
	services="mobile-services,notification-hubs" 
	documentationCenter="windows" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="11/11/2015" 
	wacn.date=""/>

# Add push notifications to your Mobile Services app

[AZURE.INCLUDE [mobile-service-note-mobile-apps](../includes/mobile-services-note-mobile-apps.md)]
[AZURE.INCLUDE [mobile-services-selector-get-started-push](../includes/mobile-services-selector-get-started-push.md)]

##Overview
This topic shows you how to use Azure Mobile Services with a .NET backend to send push notifications to a universal Windows app. In this tutorial you enable push notifications using Azure Notification Hubs in a universal Windows app project. When complete, your mobile service will send a push notification from the .NET backend to all registered Windows Store and Windows Phone Store apps each time a record is inserted in the TodoList table. The notification hub that you create is free with your mobile service, can be managed independent of the mobile service, and can be used by other applications and services.

To complete this tutorial, you need the following:

* An active [Microsoft Store account](https://dev.windows.com/zh-cn/programs/join).
* <a href="https://www.visualstudio.com/downloads/download-visual-studio-vs" target="_blank">Visual Studio Community 2013</a>. 

##<a id="register"></a>Register your app for push notifications

[AZURE.INCLUDE [mobile-services-create-new-push-vs2013](../includes/mobile-services-create-new-push-vs2013.md)]

&nbsp;&nbsp;6. Browse to the `\Services\MobileServices\your_service_name` project folder, open the generated push.register.cs code file, and inspect the **UploadChannel** method that registers the device's channel URL with the notification hub.
 
&nbsp;&nbsp;7. Open the shared App.xaml.cs code file and notice that a call to the new **UploadChannel** method was added in the **OnLaunched** event handler. This makes sure that registration of the device is attempted whenever the app is launched.

&nbsp;&nbsp;8. Repeat the previous steps to add push notifications to the Windows Phone Store app project, then in the shared App.xaml.cs file, remove the extra call to **UploadChannel** and the remaining `#if...#endif` conditional wrapper. Both projects can now share a single call to **UploadChannel**.

> [AZURE.NOTE] You can also simplify the generated code by unifying the `#if...#endif` wrapped [MobileServiceClient](http://msdn.microsoft.com/zh-cn/library/azure/microsoft.windowsazure.mobileservices.mobileserviceclient.aspx) definitions into a single unwrapped definition used by both versions of the app.

Now that push notifications are enabled in the app, you must update the mobile service to send push notifications. 

##<a id="update-service"></a>Update the service to send push notifications

The following steps update the existing TodoItemController class to send a push notification to all registered devices when a new item is inserted. You can implement similar code in any custom [ApiController](https://msdn.microsoft.com/zh-cn/library/system.web.http.apicontroller.aspx), [TableController](https://msdn.microsoft.com/zh-cn/library/azure/microsoft.windowsazure.mobile.service.tables.tablecontroller.aspx), or anywhere else in your backend services. 

[AZURE.INCLUDE [mobile-services-dotnet-backend-update-server-push](../includes/mobile-services-dotnet-backend-update-server-push.md)]

##<a id="local-testing"></a> Enable push notifications for local testing

[AZURE.INCLUDE [mobile-services-dotnet-backend-configure-local-push-vs2013](../includes/mobile-services-dotnet-backend-configure-local-push-vs2013.md)]

The remaining steps in this section are optional. They allow you to test your app against your mobile service running on a local computer. If you plan to test push notifications using the mobile service running in Azure, you can just skip to the last section. This is because the Add Push Notification wizard already configured your app to connect to your service running in Azure. 

>[AZURE.NOTE]Never use a production mobile service for testing and development work. Always publish your mobile service project to a separate staging service for testing.

&nbsp;&nbsp;5. Open the shared App.xaml.cs project file and locate any the lines of code that create a new instance of the [MobileServiceClient] class to access the mobile service running in Azure.

&nbsp;&nbsp;6. Comment-out this code and add code that creates a new [MobileServiceClient] of the same name but using the URL of the local host in the constructor, similar to the following:

	// This MobileServiceClient has been configured to communicate with your local
	// test project for debugging purposes.
	public static MobileServiceClient todolistClient = new MobileServiceClient(
		"http://localhost:4584"
	);

&nbsp;&nbsp;Using this [MobileServiceClient], the app will connect to the local service instead of the version hosted in Azure. When you want to switch back and run app against the mobile service hosted in Azure, change back to the original [MobileServiceClient] definitions.

##<a id="test"></a> Test push notifications in your app

[AZURE.INCLUDE [mobile-services-dotnet-backend-windows-universal-test-push](../includes/mobile-services-dotnet-backend-windows-universal-test-push.md)]

## <a name="next-steps"> </a>Next steps

This tutorial demonstrated the basics of enabling a Windows Store app to use Mobile Services and Notification Hubs to send push notifications. Next, consider completing the next tutorial, [Send push notifications to authenticated users], which shows how to use tags to send push notifications from a Mobile Service to only an authenticated user.

Learn more about Mobile Services and Notification Hubs in the following topics:

* [Add Mobile Services to an existing app][Get started with data]
  <br/>Learn more about storing and querying data using mobile services.

* [Add authentication to your app][Get started with authentication]
  <br/>Learn how to authenticate users of your app with different account types using mobile services.

* [What are Notification Hubs?]
  <br/>Learn more about how Notification Hubs works to deliver notifications to your apps across all major client platforms.

* [Debug Notification Hubs applications](https://msdn.microsoft.com/zh-cn/library/dn530751.aspx)
  </br>Get guidance troubleshooting and debugging Notification Hubs solutions. 

* [How to use a .NET client for Azure Mobile Services]
  <br/>Learn more about how to use Mobile Services from C# Windows apps.

<!-- Anchors. -->

<!-- Images. -->

<!-- URLs. -->
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253
[Get started with Mobile Services]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started
[Get started with data]: /documentation/articles/mobile-services-dotnet-backend-windows-universal-dotnet-get-started-data
[Get started with authentication]: /documentation/articles/mobile-services-dotnet-backend-windows-universal-dotnet-get-started-users

[Send push notifications to authenticated users]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users

[What are Notification Hubs?]: /documentation/articles/notification-hubs-overview

[How to use a .NET client for Azure Mobile Services]: /documentation/articles/mobile-services-windows-dotnet-how-to-use-client-library
[MobileServiceClient]: http://msdn.microsoft.com/zh-cn/library/azure/microsoft.windowsazure.mobileservices.mobileserviceclient.aspx