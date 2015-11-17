<properties 
	pageTitle="Register for Google authentication | Windows Azure" 
	description="Learn how to register your apps to use Google to authenticate with Azure Mobile Services." 
	services="mobile-services" 
	documentationCenter="android" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="11/15/2015"
	wacn.date=""/>

# Register your apps for Google login with Mobile Services

[AZURE.INCLUDE [mobile-services-selector-register-identity-provider](../includes/mobile-services-selector-register-identity-provider.md)]

This topic shows you how to register your apps to be able to use Google to authenticate with Azure Mobile Services.

>[AZURE.NOTE] This tutorial is about [Azure Mobile Services](/home/features/mobile-services/), a solution to help you build scalable mobile applications for any platform. Mobile Services makes it easy to sync data, authenticate users, and send push notifications. This page supports the [Get Started with Authentication](/documentation/articles/mobile-services-ios-get-started-users) tutorial, which shows how to sign in users to your app. 
<br/>If this is your first experience with Mobile Services, please complete the tutorial [Get Started with Mobile Services](/documentation/articles/mobile-services-ios-get-started).

To complete the procedure in this topic, you must have a Google account that has a verified email address. To create a new Google account, go to <a href="https://accounts.google.com/SignUp" target="_blank">accounts.google.com</a>.

3. Navigate to the [Google apis](https://accounts.google.com/ServiceLogin?osid=1&passive=true&continue=https://console.developers.google.com/dcredirect/) website, sign-in with your Google account credentials, click **Create Project**, provide a **Project name**, then click **Create**.

4. In the left navigation bar, click **API & Auth**, then under **Social APIs** click **Google+ API** > **Enable API**.

5. Click **API & Auth** > **Credentials** > **OAuth consent screen**, then select your **Email address**,  enter a **Product Name**, and click **Save**.

6. In the **Credentials** tab, click **Add credentials** > **OAuth 2.0 client ID**, then select **Web application**.

7. Type your mobile service URL in **Authorized JavaScript Origins**, replace the generated URL in **Authorized Redirect URI** with one of the following URL formats, and then click **Create client ID**:
 
	+ **.NET backend**: `https://<mobile_service>.azure-mobile.cn/signin-google`
	+ **JavaScript backend**: `https://<mobile_service>.azure-mobile.cn/login/google` 

	 >[AZURE.NOTE]Make sure that you use the correct redirect URL path format for your type of Mobile Services backend. When this is incorrect, authentication will not succeed. 

8. On the next screen, make a note of the values of the client ID and client secret.

    > [AZURE.IMPORTANT] The client secret is an important security credential. Do not share this secret with anyone or distribute it within a client application.

You are now ready to configure your mobile service to use Google sign-in for authentication in your app.

<!-- Anchors. -->

<!-- Images. -->

<!-- URLs. -->

[Google apis]: https://accounts.google.com/ServiceLogin?osid=1&passive=true&continue=https://console.developers.google.com/dcredirect/
[Get started with authentication]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-dotnet/

[Azure Management Portal]: https://manage.windowsazure.cn/
 
