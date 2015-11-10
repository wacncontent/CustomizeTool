<properties
	pageTitle="Get started with data on Android  (JavaScript backend) | Windows Azure"
	description="Learn how to get started using Mobile Services to leverage data in your Android app  (JavaScript backend)."
	services="mobile-services"
	documentationCenter="android"
	authors="RickSaling"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="10/05/2015"
	wacn.date=""/>

# Add Mobile Services to an existing Android app <!-- deleted by customization (JavaScript backend) -->
<!-- keep by customization: begin -->

[AZURE.INCLUDE [mobile-services-selector-get-started-data](../includes/mobile-services-selector-get-started-data.md)]
<!-- keep by customization: end -->

## Summary

<div class="dev-onpage-video-clear clearfix">
<div class="dev-onpage-left-content">

<p>This topic shows you how to use Azure Mobile Services to add persistent data to an Android app. In this tutorial, you will download an app that stores data in memory, create a new mobile service, integrate the app with the mobile service so that it stores and updates data in Azure Mobile Services instead of locally, and then use the Azure Management Portal to view changes to data that were made by running the app.</p>

</div>


<div class="dev-onpage-video-wrapper">
<a href="http://channel9.msdn.com/Series/Windows-Azure-Mobile-Services/Android-Getting-Started-With-Data-Connecting-your-app-to-Windows-Azure-Mobile-Services" target="_blank" class="label">watch the tutorial</a> <a style="background-image: url('/media/devcenter/mobile/videos/mobile-android-get-started-data-180x120.png') !important;" href="http://channel9.msdn.com/Series/Windows-Azure-Mobile-Services/Android-Getting-Started-With-Data-Connecting-your-app-to-Windows-Azure-Mobile-Services" target="_blank" class="dev-onpage-video"><span class="icon">Play Video</span></a><span class="time">15:32</span></div>
</div>


<p>This tutorial helps you understand in more detail how Azure Mobile Services can store and retrieve data from an Android app. So it walks you through many of the steps that are already completed for you in the Mobile Services quickstart tutorial. If this is your first experience with Mobile Services, consider first completing the tutorial <a href="/develop/mobile/tutorials/get-started-android">Get started with Mobile Services</a>.</p>

## Prerequisites

To complete this tutorial, you need the following:

- an Azure account. If you don't have an account, you can create a trial account in just a couple of minutes. For details, see <a <!-- deleted by customization href="/pricing/1rmb-trial/?WT.mc_id=AED8DE357" --><!-- keep by customization: begin --> href="/pricing/1rmb-trial/" <!-- keep by customization: end --> target="_blank">Azure Trial</a>.


- the [Azure Mobile Services Android SDK];
- the <a  href="https://developer.android.com/sdk/index.html" target="_blank">Android Studio integrated development environment</a>, which includes the Android SDK; and Android 4.2 or a later version. The downloaded GetStartedWithData project requires Android 4.2 or a later version. However, the Mobile Services SDK requires only Android 2.2 or a later version.
<!-- deleted by customization

## Sample Code

To see the completed source code, go <a href="https://github.com/Azure/mobile-services-samples/tree/master/GettingStartedWithData/AndroidStudio">here</a>.
-->

## Download the GetStartedWithData project

###Get the sample code

[AZURE.INCLUDE [download-android-sample-code](../includes/download-android-sample-code.md)]

<!-- deleted by customization
### Inspect and run the sample code
-->
<!-- keep by customization: begin -->
###Inspect and run the sample code
<!-- keep by customization: end -->

[AZURE.INCLUDE [mobile-services-android-run-sample-code](../includes/mobile-services-android-run-sample-code.md)]

## Create a new mobile service in the Management Portal

[AZURE.INCLUDE [mobile-services-create-new-service-data](../includes/mobile-services-create-new-service-data.md)]

## Add a new table to the mobile service

[AZURE.INCLUDE [mobile-services-create-new-service-data-2](../includes/mobile-services-create-new-service-data-2.md)]

## Update the app to use the mobile service for data access

[AZURE.INCLUDE [mobile-services-android-getting-started-with-data](../includes/mobile-services-android-getting-started-with-data.md)]


## Test the app against your new mobile service

Now that the app has been updated to use Mobile Services for back end storage, you can test it against Mobile Services, using either the Android emulator or an Android phone.

1. From the **Run** menu, click **Run app** to start the project.

	This executes your app, built with the Android SDK, that uses the client library to send a query that returns items from your mobile service.

<!-- deleted by customization 5 --><!-- keep by customization: begin --> 2 <!-- keep by customization: end -->. As before, type meaningful text, then click **Add**.

   	This sends a new item as an insert to the mobile service.

3. In the [Management Portal], click **Mobile Services**, and then click your mobile service.

4. Click the **Data** tab, then click **Browse**.

   	![][9]
   	Notice that the **TodoItem** table now contains data, with some values generated by Mobile Services, and that columns have been automatically added to the table to match the TodoItem class in the app.

This concludes the **Get started with data** tutorial for Android.

## Troubleshooting

<!-- deleted by customization
### Verify Android SDK Version
-->
<!-- keep by customization: begin -->
###Verify Android SDK Version
<!-- keep by customization: end -->

[AZURE.INCLUDE [Verify SDK](../includes/mobile-services-verify-android-sdk-version.md)]


<!-- keep by customization: begin -->
## Older Code Versions

If you would like to see the Eclipse version of this tutorial, go to 
[Get started with data using Eclipse](/documentation/articles/mobile-services-android-get-started-data-EC).

To see a completed version of the source code in an Eclipse project, go <a href="https://github.com/Azure/mobile-services-samples/tree/master/GettingStartedWithData/Android">here</a>.

If you want to get the sample file used in the preceding version of the Azure Mobile Services Android SDK, you can get it [here](http://go.microsoft.com/fwlink/p/?LinkID=282122).
<!-- keep by customization: end -->

## Next steps

This tutorial demonstrated the basics of enabling an Android app to work with data in Mobile Services.

Next, consider completing one of the following tutorials that is based on the GetStartedWithData app that you created in this tutorial:

* [Validate and modify data with scripts]
  <!-- deleted by customization <br/>Learn --><!-- keep by customization: begin --> Learn <!-- keep by customization: end --> more about using server scripts in Mobile Services to validate and change data sent from your app.

* [Refine queries with paging]
  <!-- deleted by customization <br/>Learn --><!-- keep by customization: begin --> Learn <!-- keep by customization: end --> how to use paging in queries to control the amount of data handled in a single request.

Once you have completed the data series, try these other Android tutorials:

* [Get started with authentication]
	<!-- deleted by customization <br/>Learn --><!-- keep by customization: begin --> Learn <!-- keep by customization: end --> how to authenticate users of your app.

* [Get started with push notifications]
  <!-- deleted by customization <br/>Learn --><!-- keep by customization: begin --> Learn <!-- keep by customization: end --> how to send a very basic push notification to your app with Mobile Services.

<!-- Anchors. -->
[Download the Android app project]: #download-app
[Create the mobile service]: #create-service
[Add a data table for storage]: #add-table
[Update the app to use Mobile Services]: #update-app
[Test the app against Mobile Services]: #test-app
[Next Steps]:#next-steps

<!-- Images. -->
[8]: ./media/mobile-services-android-get-started-data/mobile-dashboard-tab.png
[9]: ./media/mobile-services-android-get-started-data/mobile-todoitem-data-browse.png
[12]: ./media/mobile-services-android-get-started-data/mobile-eclipse-project.png
[13]: ./media/mobile-services-android-get-started-data/mobile-quickstart-startup-android.png
[14]: ./media/mobile-services-android-get-started-data/mobile-services-import-android-workspace.png
[15]: ./media/mobile-services-android-get-started-data/mobile-services-import-android-project.png


<!-- URLs. -->
<!-- deleted by customization
[Validate and modify data with scripts]: /develop/mobile/tutorials/validate-modify-and-augment-data-dotnet
[Refine queries with paging]: /develop/mobile/tutorials/add-paging-to-data-android
[Get started with Mobile Services]: /develop/mobile/tutorials/get-started-android
[Get started with data]: /develop/mobile/tutorials/get-started-with-data-android
[Get started with authentication]: /develop/mobile/tutorials/get-started-with-users-android
[Get started with push notifications]: /develop/mobile/tutorials/get-started-with-push-android
-->
<!-- keep by customization: begin -->
[Validate and modify data with scripts]: /documentation/articles/mobile-services-windows-dotnet-how-to-use-client-library
[Refine queries with paging]: /documentation/articles/mobile-services-android-how-to-use-client-library
[Get started with Mobile Services]: /documentation/articles/mobile-services-android-get-started/
[Get started with data]: /documentation/articles/mobile-services-android-get-started-data
[Get started with data (Eclipse)]: /documentation/articles/mobile-services-android-get-started-data-EC/
[Get started with authentication]: /documentation/articles/mobile-services-android-get-started-users
[Get started with push notifications]: /documentation/articles/mobile-services-javascript-backend-android-get-started-push
<!-- keep by customization: end -->

[Azure Management Portal]: https://manage.windowsazure.cn/
[Management Portal]: https://manage.windowsazure.cn/
[Azure Mobile Services Android SDK]: http://aka.ms/Iajk6q
[GitHub]:  http://go.microsoft.com/fwlink/p/?LinkID=282122
[Android SDK]: http://developer.android.com/sdk/index.html
