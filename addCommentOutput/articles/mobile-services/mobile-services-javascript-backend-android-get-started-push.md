
<properties
	pageTitle="Get started with push notifications (Android JavaScript) | Windows Azure"
	description="Learn how to use Azure Mobile Services to send push notifications to your Android JavaScript app."
	services="mobile-services, notification-hubs"
	documentationCenter="android"
	authors="RickSaling"
	writer="ricksal"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="10/06/2015"
	wacn.date=""/>


# Add push notifications to your Mobile Services Android app

[AZURE.INCLUDE [mobile-services-selector-get-started-push](../includes/mobile-services-selector-get-started-push.md)]

## Summary

This topic shows how to use Azure Mobile Services to send push notifications to your Android app using Google Cloud Messaging ("GCM"). You will add push notifications to the quickstart project that is a prerequisite for this tutorial. Push notifications are enabled by using the Azure Notification Hub that is included in your mobile service. When complete, your mobile service will send a push notification each time a record is inserted.

<!-- deleted by customization
## Prerequisites
-->
<!-- keep by customization: begin -->



##Prerequisites
<!-- keep by customization: end -->

[AZURE.INCLUDE [mobile-services-android-prerequisites](../includes/mobile-services-android-prerequisites.md)]

<!-- deleted by customization
## Sample code
To see the completed source code go [here](https://github.com/Azure/mobile-services-samples/tree/master/GettingStartedWithPush).

## Enable Google Cloud Messaging
-->
<!-- keep by customization: begin -->
##<a id="register"></a>Enable Google Cloud Messaging
<!-- keep by customization: end -->

[AZURE.INCLUDE [mobile-services-enable-Google-cloud-messaging](../includes/mobile-services-enable-google-cloud-messaging.md)]

<!-- deleted by customization
## Configure Mobile Services to send push requests
-->
<!-- keep by customization: begin -->
##<a id="configure"></a>Configure Mobile Services to send push requests
<!-- keep by customization: end -->

[AZURE.INCLUDE [mobile-services-android-configure-push](../includes/mobile-services-android-configure-push.md)]

<!-- deleted by customization
## Add push notifications to your app
-->
<!-- keep by customization: begin -->
##<a id="add-push"></a>Add push notifications to your app
<!-- keep by customization: end -->



Your next step is to install Google Play services. Google Cloud Messaging has some minimum API level requirements for development and testing, which the **minSdkVersion** property in the Manifest must conform to.

If you will be testing with an older device, then consult [Set Up Google Play Services SDK] to determine how low you can set this value, and set it appropriately.

###Add Google Play Services to the project

[AZURE.INCLUDE [Add Play Services](../includes/mobile-services-add-google-play-services.md)]

###Add code

[AZURE.INCLUDE [mobile-services-android-getting-started-with-push](../includes/mobile-services-android-getting-started-with-push.md)]


<!-- deleted by customization
## Update the registered insert script in the Management Portal
-->
<!-- keep by customization: begin -->
##<a id="update-scripts"></a>Update the registered insert script in the Management Portal
<!-- keep by customization: end -->

[AZURE.INCLUDE [mobile-services-javascript-backend-android-push-insert-script](../includes/mobile-services-javascript-backend-android-push-insert-script.md)]


<!-- deleted by customization
## Test push notifications in your app
-->
<!-- keep by customization: begin -->
##<a id="test"></a>Test push notifications in your app
   
<!-- keep by customization: end -->
You can test the app by directly attaching an Android phone with a USB cable, or by using a virtual device in the emulator.

###Setting up the Android emulator for testing

When you run this app in the emulator, make sure that you use an Android Virtual Device (AVD) that supports Google APIs.

1. From the right end of the toolbar, select the Android Virtual Device Manager, select your device, click the edit icon on the right.

	![](./media/mobile-services-javascript-backend-android-get-started-push/mobile-services-android-virtual-device-manager.png)

2. Select **Change** on the device description line, select **Google APIs**,  then click OK.

   	![](./media/mobile-services-javascript-backend-android-get-started-push/mobile-services-android-virtual-device-manager-edit.png)

	This targets the AVD to use Google APIs.

###Running the test

1. From the **Run** menu item, click **Run app** to start the app.

2. In the app, type meaningful text, such as _A new Mobile Services task_ and then click the **Add** button.

  	![](./media/mobile-services-javascript-backend-android-get-started-push/mobile-quickstart-push1-android.png)

3. Swipe down from the top of the screen to open the device's Notification Drawer to see the notification.


You have successfully completed this tutorial.

## Troubleshooting

### Verify Android SDK Version

[AZURE.INCLUDE [Verify SDK](../includes/mobile-services-verify-android-sdk-version.md)]

<!-- deleted by customization ## Next steps -->
<!-- keep by customization: begin -->
## Older Code Versions

If you would like to see the Eclipse version of this tutorial, go to [Get started with push notifications (Eclipse)].




## <a name="next-steps"> </a>Next steps
<!-- keep by customization: end -->

<!---This tutorial demonstrated the basics of enabling an Android app to use Mobile Services and Notification Hubs to send push notifications. Next, consider completing the next tutorial, [Send push notifications to authenticated users], which shows how to use tags to send push notifications from a Mobile Service to only an authenticated user.
<!-- keep by customization: begin -->

+ [Send push notifications to authenticated users]
	<br/>Learn how to use tags to send push notifications from a Mobile Service to only an authenticated user.
<!-- keep by customization: end -->

+ [Send broadcast notifications to subscribers]
	<br/>Learn how users can register and receive push notifications for categories they're interested in.

+ [Send template-based notifications to subscribers]
	<br/>Learn how to use templates to send push notifications from a Mobile Service, without having to craft platform-specific payloads in your back-end.
-->

Learn more about Mobile Services and Notification Hubs in the following topics:

<!-- keep by customization: begin -->
* [Get started with data]
  <br/>Learn more about storing and querying data using mobile services.

<!-- keep by customization: end -->
* [Get started with authentication]
  <br/>Learn how to authenticate users of your app with different account types using mobile services.

* [What are Notification Hubs?]
  <br/>Learn more about how Notification Hubs works to deliver notifications to your apps across all major client platforms.

* [Debug Notification Hubs applications](https://msdn.microsoft.com/zh-cn/library/dn530751.aspx)
  </br>Get guidance troubleshooting and debugging Notification Hubs solutions.

* [How to use the Android client library for Mobile Services]
  <br/>Learn more about how to use Mobile Services with Android.

* [Mobile Services server script reference]
  <br/>Learn more about how to implement business logic in your mobile service.


<!-- Anchors. -->
[Register your app for push notifications and configure Mobile Services]: #register
[Update the generated push notification code]: #update-scripts
[Insert data to receive notifications]: #test
[Next Steps]:#next-steps

<!-- Images. -->
[13]: ./media/mobile-services-windows-store-javascript-get-started-push/mobile-quickstart-push1.png
[14]: ./media/mobile-services-windows-store-javascript-get-started-push/mobile-quickstart-push2.png


<!-- URLs. -->
<!-- keep by customization: begin -->
[Get started with push notifications (Eclipse)]: /documentation/articles/mobile-services-javascript-backend-android-get-started-push-ec
<!-- keep by customization: end -->
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Get started with Mobile Services]: /documentation/articles/mobile-services-android-get-started
<!-- keep by customization: begin -->
[Get started with data]: /documentation/articles/mobile-services-android-get-started-data
<!-- keep by customization: end -->
[Get started with authentication]: /documentation/articles/mobile-services-android-get-started-users
<!-- deleted by customization
[Get started with push notifications]: /develop/mobile/tutorials/get-started-with-push-js
[Push notifications to app users]: /develop/mobile/tutorials/push-notifications-to-users-js
[Authorize users with scripts]: /develop/mobile/tutorials/authorize-users-in-scripts-js
[JavaScript and HTML]: /develop/mobile/tutorials/get-started-with-push-js
-->
<!-- keep by customization: begin -->
[Get started with push notifications]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-push-js
[Push notifications to app users]: /documentation/articles/mobile-services-javascript-backend-windows-store-javascript-get-started-push
[Authorize users with scripts]: /documentation/articles/mobile-services-windows-store-javascript-authorize-users-in-scripts
[JavaScript and HTML]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-push-js
<!-- keep by customization: end -->
[Set Up Google Play Services SDK]: http://go.microsoft.com/fwlink/?LinkId=389801
<!-- deleted by customization
[Azure Management Portal]: https://manage.windowsazure.cn/
-->
<!-- keep by customization: begin -->
[Windows Azure Management Portal]: https://manage.windowsazure.cn/
<!-- keep by customization: end -->
[How to use the Android client library for Mobile Services]: /documentation/articles/mobile-services-android-how-to-use-client-library
[gcm object]: https://msdn.microsoft.com/zh-cn/library/dn126137.aspx

<!-- deleted by customization
[Mobile Services server script reference]: http://go.microsoft.com/fwlink/?LinkId=262293
-->
<!-- keep by customization: begin -->
[Mobile Services server script reference]: /documentation/articles/mobile-services-how-to-use-server-scripts
[Send push notifications to authenticated users]: /documentation/articles/mobile-services-javascript-backend-android-push-notifications-app-users

<!-- keep by customization: end -->
[What are Notification Hubs?]: /documentation/articles/notification-hubs-overview
[Send broadcast notifications to subscribers]: /documentation/articles/notification-hubs-android-send-breaking-news
[Send template-based notifications to subscribers]: /documentation/articles/notification-hubs-android-send-localized-breaking-news