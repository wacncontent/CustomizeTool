<properties
	pageTitle="Get Started with Mobile Services for Xamarin Android apps | Windows Azure"
	description="Follow this tutorial to get started using Azure Mobile Services for Xamarin Android development"
	services="mobile-services"
	documentationCenter="xamarin"
	authors="lindydonna"
	manager="dwrede"
	editor="mollybos"/>

<tags
	ms.service="mobile-services"
	ms.date="10/12/2015"
	wacn.date=""/>

# <a name="getting-started"> </a>Get started with Mobile Services

[AZURE.INCLUDE [mobile-service-note-mobile-apps](../includes/mobile-services-note-mobile-apps.md)]

&nbsp;
[AZURE.INCLUDE [mobile-services-selector-get-started](../includes/mobile-services-selector-get-started.md)]
&nbsp;

>[AZURE.TIP] If you are new to mobile development using Windows Azure, [get started with Azure Mobile Apps](/documentation/articles/app-service-mobile-dotnet-backend-xamarin-android-get-started-preview) instead of Azure Mobile Services; Mobile Apps gives you [additional advantages](/documentation/articles/app-service-mobile-value-prop-migration-from-mobile-services-preview).

This tutorial shows you how to add a cloud-based backend service to a Xamarin Android app using Azure Mobile Services. In this tutorial, you will create both a new mobile service and a simple _To do list_ app that stores app data in the new mobile service. The mobile service that you will create uses the supported .NET languages using Visual Studio for server-side business logic and to manage the mobile service. To create a mobile service that lets you write your server-side business logic in JavaScript, see the [JavaScript backend version] of this topic.

>[AZURE.NOTE]This topic shows you how to create a new mobile service project by using the Azure Management Portal. By using Visual Studio 2013 Update 2, you can also add a new mobile service project to an existing Visual Studio solution. For more information, see [Quickstart: Add a mobile service (.NET backend)](http://msdn.microsoft.com/zh-cn/library/windows/apps/dn629482.aspx)

A screenshot from the completed app is below:

![][0]

Completing this tutorial is a prerequisite for all other Mobile Services tutorials for Xamarin Android apps.

<!-- deleted by customization
>[AZURE.NOTE]To complete this tutorial, you need an Azure account. If you don't have an account, you can sign up for an Azure trial and get up to 10 free mobile services that you can keep using even after your trial ends. For details, see [Azure Trial](/pricing/1rmb-trial/?WT.mc_id=A0E0E5C02&amp;returnurl=http%3A%2F%2Fazure.microsoft.com%2Fen-us%2Fdocumentation%2Farticles%2Fmobile-services-dotnet-backend-xamarin-android-get-started).
>This tutorial requires [Visual Studio Professional 2013](https://www.visualstudio.com/downloads/download-visual-studio-vs). A trial version is available.
-->
<!-- keep by customization: begin -->
>[AZURE.NOTE]To complete this tutorial, you need an Azure account. If you don't have an account, you can sign up for an Azure trial and get up to 10 free mobile services that you can keep using even after your trial ends. For details, see <a href="/pricing/1rmb-trial">Azure Trial</a>.<br />This tutorial requires <a href="https://www.visualstudio.com/downloads/download-visual-studio-vs" target="_blank">Visual Studio Professional 2013</a>. A trial version is available.
<!-- keep by customization: end -->

## Create a new mobile service

[AZURE.INCLUDE [mobile-services-dotnet-backend-create-new-service](../includes/mobile-services-dotnet-backend-create-new-service.md)]

## Create a new Xamarin Android app

Once you have created your mobile service, you can follow an easy quickstart in the Azure Management Portal to either create a new app or modify an existing app to connect to your mobile service.

In this section you will download a new Xamarin Android app and a service project for your mobile service.

1. In the [Azure Management Portal], click **Mobile Services**, and then click the mobile service that you just created.

2. In the quickstart tab, click **Xamarin** under **Choose platform** and expand **Create a new Xamarin app**.

   	![][6]

   	This displays the three easy steps to create a Xamarin Android app connected to your mobile service.

  	![][7]

3. If you haven't already done so, download and install [Visual Studio Professional 2013](https://www.visualstudio.com/downloads/download-visual-studio-vs) on your local computer or virtual machine.

4. If you haven't already done so, download and install [Xamarin Studio] or Xamarin for Visual Studio.

5. Under **Download and publish your service to the cloud**, select **Android** and click **Download**.

  	This downloads a solution contains projects for both the mobile service and for the sample _To do list_ application that is connected to your mobile service. Save the compressed project file to your local computer, and make a note of where you save it.

6. Download your publish profile, save the downloaded file to your local computer, and make a note of where you save it.

## Test the mobile service

[AZURE.INCLUDE [mobile-services-dotnet-backend-test-local-service](../includes/mobile-services-dotnet-backend-test-local-service.md)]

## Publish your mobile service

[AZURE.INCLUDE [mobile-services-dotnet-backend-publish-service](../includes/mobile-services-dotnet-backend-publish-service.md)]

## Run the Xamarin Android app

The final stage of this tutorial is to build and run your new app.

1. Navigate to the client project within the mobile service solution, in either Visual Studio or Xamarin Studio.

2. Press the **Run** button to build the project and start the app. You will be asked to select an emulator or a connected USB device.

	> [AZURE.NOTE] To be able to run the project in the Android emulator, you must define a least one Android Virtual Device (AVD). Use the AVD Manager to create and manage these devices.

3. In the app, type meaningful text, such as _Complete the tutorial_ and then click the plus (**+**) icon.

	![][10]

	This sends a POST request to the new mobile service hosted in Azure. Data from the request is inserted into the TodoItem table. Items stored in the table are returned by the mobile service, and the data is displayed in the list.

	> [AZURE.NOTE]
   	> You can review the code that accesses your mobile service to query and insert data, which is found in the ToDoActivity.cs C# file.
## Next Steps
Now that you have completed the quickstart, learn how to perform additional important tasks in Mobile Services:

* [Get started with offline data sync]
  <br/>Learn how the quickstart uses offline data sync to make the app responsive and robust.

* [Get started with authentication]
  <br/>Learn how to authenticate users of your app with an identity provider.

* [Get started with push notifications]
  <br/>Learn how to send a very basic push notification to your app.

* [Troubleshoot a Mobile Services .NET backend]
  <br/> Learn how to diagnose and fix issues that can arise with a Mobile Services .NET backend.

[AZURE.INCLUDE [app-service-disqus-feedback-slug](../includes/app-service-disqus-feedback-slug.md)]

<!-- Anchors. -->
[Getting started with Mobile Services]:#getting-started
[Create a new mobile service]:#create-new-service
[Next Steps]:#next-steps



<!-- Images. -->
[0]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-quickstart-completed-android.png
[6]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-portal-quickstart-xamarin.png
[7]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-quickstart-steps-xamarin-android.png
[8]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-xamarin-project-android-vs.png
[9]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-xamarin-project-android-xs.png
[10]: ./media/mobile-services-dotnet-backend-xamarin-android-get-started/mobile-quickstart-startup-android.png

<!-- URLs. -->
[Get started with offline data sync]: <!-- deleted by customization mobile-services-xamarin-android-get-started-offline-data.md --><!-- keep by customization: begin --> /documentation/articles/mobile-services-xamarin-android-get-started-offline-data <!-- keep by customization: end -->
<!-- deleted by customization
[Get started with authentication]: mobile-services-dotnet-backend-xamarin-android-get-started-users.md
[Get started with push notifications]: mobile-services-dotnet-backend-xamarin-android-get-started-push.md
-->
<!-- keep by customization: begin -->
[Get started with authentication]: /documentation/articles/mobile-services-dotnet-backend-xamarin-android-get-started-users
[Get started with push notifications]: /documentation/articles/mobile-services-dotnet-backend-xamarin-android-get-started-push
<!-- keep by customization: end -->
[Visual Studio Professional 2013]: https://www.visualstudio.com/downloads/download-visual-studio-vs
[Mobile Services SDK]: http://go.microsoft.com/fwlink/?LinkId=257545
<!-- deleted by customization
[JavaScript and HTML]: mobile-services-win8-javascript/
-->
<!-- keep by customization: begin -->
[JavaScript and HTML]: /documentation/articles/mobile-services-win8-javascript
<!-- keep by customization: end -->
[Azure Management Portal]: https://manage.windowsazure.cn/
<!-- deleted by customization
[JavaScript backend version]: mobile-services-android-get-started.md
[Troubleshoot a Mobile Services .NET backend]: mobile-services-dotnet-backend-how-to-troubleshoot.md
-->
<!-- keep by customization: begin -->
[JavaScript backend version]: /documentation/articles/mobile-services-android-get-started
[Troubleshoot a Mobile Services .NET backend]: /documentation/articles/mobile-services-dotnet-backend-how-to-troubleshoot
<!-- keep by customization: end -->


[Xamarin Studio]: http://xamarin.com/download
[Xcode]: https://go.microsoft.com/fwLink/?LinkID=266532&clcid=0x409
[Xamarin for Windows]: https://go.microsoft.com/fwLink/?LinkID=330242&clcid=0x409
