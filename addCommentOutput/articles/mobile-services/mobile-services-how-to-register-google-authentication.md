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
	ms.date="08/27/2015"
	wacn.date=""/>

# Register your apps for Google login with Mobile Services

[AZURE.INCLUDE [mobile-services-selector-register-identity-provider](../includes/mobile-services-selector-register-identity-provider.md)]

This topic shows you how to register your apps to be able to use Google to authenticate with Azure Mobile Services.

>[AZURE.NOTE] This tutorial is about [Azure Mobile <!-- deleted by customization Services](/home/features/mobile-services/) --><!-- keep by customization: begin --> Services](/home/features/identity/) <!-- keep by customization: end -->, a solution to help you build scalable mobile applications for any platform. Mobile Services makes it easy to sync data, authenticate users, and send push notifications. This page supports the [Get Started with Authentication](/documentation/articles/mobile-services-ios-get-started-users) tutorial, which shows how to sign in users to your app.
<br/>If this is your first experience with Mobile Services, please complete the tutorial [Get Started with Mobile Services](/documentation/articles/mobile-services-ios-get-started).

To complete the procedure in this topic, you must have a Google account that has a verified email address. To create a new Google account, go to <a href="https://accounts.google.com/SignUp" target="_blank">accounts.google.com</a>.

<!-- deleted by customization 3 --><!-- keep by customization: begin --> 1 <!-- keep by customization: end -->. Navigate to the <!-- deleted by customization [Google apis](https://accounts.google.com/ServiceLogin?osid=1&passive=true&continue=https://console.developers.google.com/dcredirect/) --><!-- keep by customization: begin --> <a href="https://accounts.google.com/ServiceLogin?osid=1&passive=true&continue=https://console.developers.google.com/dcredirect/" <!-- keep by customization: end --><!-- keep by customization: begin --> target="_blank">Google apis</a> <!-- keep by customization: end --> website, sign-in with your Google account credentials, click **Create Project**, provide a **Project name**, then click **Create**.

<!-- deleted by customization
4. In the left navigation bar, click **API & Auth**, then under **Social APIs** click **Google+ API** > **Enable API**.

5. Click **API & Auth** > **Credentials** > **OAuth consent screen**, then select your **Email address**,  enter a **Product Name**, and click **Save**.

6. In the **Credentials** tab, click **Add credentials** > **OAuth 2.0 client ID**, then select **Web application**.

7. Type your mobile service URL in **Authorized JavaScript Origins**, replace the generated URL in **Authorized Redirect URI** with the URL of your mobile service appended with the path `/login/google`, and then click **Create client ID**.
-->
<!-- keep by customization: begin -->
   	![Google API new project](./media/mobile-services-how-to-register-google-authentication/mobile-services-google-new-project.png)

2. Click **Consent screen**, select your **Email Address**, enter a **Product Name**, then click **Save**. 

3. Click **API & Auth** > **Credentials** > **Create new Client ID**.

   	![Create new client ID](./media/mobile-services-how-to-register-google-authentication/mobile-services-google-create-client.png)

4. Select **Web application**, type your mobile service URL in **Authorized JavaScript Origins**, replace the generated URL in **Authorized Redirect URI** with the URL of your mobile service appended with the path `/login/google`, and then click **Create client ID**.
<!-- keep by customization: end -->

	>[AZURE.NOTE] For a .NET backend mobile service published to Azure by using Visual Studio, the redirect URL is the URL of your mobile service appended with the path _signin-google_ your mobile service as a .NET service, such as `https://todolist.azure-mobile.cn/signin-google`. 
	&nbsp;
<!-- deleted by customization
	
8. On the next screen, make a note of the values of the client ID and client secret.

    > [AZURE.IMPORTANT] The client secret is an important security credential. Do not share this secret with anyone or distribute it within a client application.
-->
<!-- keep by customization: begin -->

   	![](./media/mobile-services-how-to-register-google-authentication/mobile-services-google-create-client2.png)

5. Under **Client ID for web applications**, make a note of the values of **Client ID** and **Client secret**. 

   	![Client credentials](./media/mobile-services-how-to-register-google-authentication/mobile-services-google-create-client3.png)

    >[AZURE.IMPORTANT] The client secret is an important security credential. Do not share this secret with anyone or distribute it with your app.
<!-- keep by customization: end -->

You are now ready to configure your mobile service to use Google sign-in for authentication in your app.

<!-- Anchors. -->

<!-- Images. -->

<!-- URLs. -->

[Google apis]: https://accounts.google.com/ServiceLogin?osid=1&passive=true&continue=https://console.developers.google.com/dcredirect/
<!-- deleted by customization
[Get started with authentication]: /develop/mobile/tutorials/get-started-with-users-dotnet/
-->
<!-- keep by customization: begin -->
[Get started with authentication]: /documentation/articles/mobile-services-windows-store-dotnet-get-started-users/
<!-- keep by customization: end -->

[Azure Management Portal]: https://manage.windowsazure.cn/
