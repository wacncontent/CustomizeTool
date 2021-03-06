<properties
	pageTitle="Authenticate your app with Active Directory Authentication Library Single Sign-On (iOS) | Windows Azure"
	description="Learn how to authentication users for single sign-on with ADAL in your iOS application."
	documentationCenter="ios"
	authors="mattchenderson"
	manager="dwrede"
	editor=""
	services="mobile-services"/>

<tags
	ms.service="mobile-services"
	ms.date="12/15/2015"
	wacn.date=""/>

# Authenticate your app with Active Directory Authentication Library Single Sign-On

[AZURE.INCLUDE [mobile-service-note-mobile-apps](../includes/mobile-services-note-mobile-apps.md)]

&nbsp;
[AZURE.INCLUDE [mobile-services-selector-adal-sso](../includes/mobile-services-selector-adal-sso.md)]

##Overview

In this tutorial, you add authentication to the quickstart project using the Active Directory Authentication Library.

To be able to authenticate users, you must register your application with the Azure Active Directory (AAD). This is done in two steps. First, you must register your mobile service and expose permissions on it. Second, you must register your iOS app and grant it access to those permissions


>[AZURE.NOTE] This tutorial is intended to help you better understand how Mobile Services enables you to do single sign-on Azure Active Directory authentication for iOS apps. If this is your first experience with Mobile Services, complete the tutorial [Get started with Mobile Services].


##Prerequisites


This tutorial requires the following:

* XCode 4.5 and iOS 6.0 (or later versions)
* Completion of the [Get started with Mobile Services] tutorial.
* Completion of the [Register your apps to use an Azure Active Directory Account login]
* Windows Azure Mobile Services SDK
* The [Active Directory Authentication Library for iOS]

[AZURE.INCLUDE [mobile-services-dotnet-adal-register-client](../includes/mobile-services-dotnet-adal-register-client.md)]

##Configure the mobile service to require authentication

[AZURE.INCLUDE [mobile-services-restrict-permissions-dotnet-backend](../includes/mobile-services-restrict-permissions-dotnet-backend.md)]

##Add authentication code to the client app

1. Download the [Active Directory Authentication Library for iOS] and include it in your project. Be sure to also add the storyboards from the ADAL source.

2. In the QSTodoListViewController, include ADAL with the following:

        #import "ADALiOS/ADAuthenticationContext.h"

2. Then add the following method:

        - (void) loginAndGetData
        {
            MSClient *client = self.todoService.client;
            if (client.currentUser != nil) {
                return;
            }

            NSString *authority = @"<INSERT-AUTHORITY-HERE>";
            NSString *resourceURI = @"<INSERT-RESOURCE-URI-HERE>";
            NSString *clientID = @"<INSERT-CLIENT-ID-HERE>";
            NSString *redirectURI = @"<INSERT-REDIRECT-URI-HERE>";

            ADAuthenticationError *error;
            ADAuthenticationContext *authContext = [ADAuthenticationContext authenticationContextWithAuthority:authority error:&error];
            NSURL *redirectUri = [[NSURL alloc]initWithString:redirectURI];

            [authContext acquireTokenWithResource:resourceURI clientId:clientID redirectUri:redirectUri completionBlock:^(ADAuthenticationResult *result) {
                if (result.tokenCacheStoreItem == nil)
                {
                    return;
                }
                else
                {
                    NSDictionary *payload = @{
                        @"access_token" : result.tokenCacheStoreItem.accessToken
                    };
                    [client loginWithProvider:@"windowsazureactivedirectory" token:payload completion:^(MSUser *user, NSError *error) {
                        [self refresh];
                    }];
                }
            }];
        }


6. In the code for the `loginAndGetData` method above, replace **INSERT-AUTHORITY-HERE** with the name of the tenant in which you provisioned your application, the format should be https://login.chinacloudapi.cn/tenant-name.partner.onmschina.cn. This value can be copied out of the Domain tab in your Azure Active Directory in the [Azure Management Portal].

7. In the code for the `loginAndGetData` method above, replace **INSERT-RESOURCE-URI-HERE** with the **App ID URI** for your mobile service. If you followed the [How to Register with the Azure Active Directory] topic your App ID URI should be similar to https://todolist.azure-mobile.cn/login/aad.

8. In the code for the `loginAndGetData` method above, replace **INSERT-CLIENT-ID-HERE** with the client ID you copied from the native client application.

9. In the code for the `loginAndGetData` method above, replace **INSERT-REDIRECT-URI-HERE** with the /login/done endpoint for your mobile service. This should be similar to https://todolist.azure-mobile.cn/login/done.


3. In the QSTodoListViewController, modify `ViewDidLoad` by replacing `[self refresh]` with the following:

        [self loginAndGetData];

##Test the client using authentication

1. From the Product menu, click Run to start the app
2. You will receive a prompt to login against your Azure Active Directory.
3. The app authenticates and returns the todo items.

   ![](./media/mobile-services-dotnet-backend-ios-adal-sso-authentication/mobile-services-app-run.png)



<!-- URLs. -->
<!-- deleted by customization
[Get started with Mobile Services]: mobile-services-dotnet-backend-ios-get-started.md
[Register your apps to use an Azure Active Directory Account login]:mobile-services-how-to-register-active-directory-authentication.md
[How to Register with the Azure Active Directory]: mobile-services-how-to-register-active-directory-authentication.md
-->
<!-- keep by customization: begin -->
[Get started with Mobile Services]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started
[Register your apps to use an Azure Active Directory Account login]:/documentation/articles/mobile-services-how-to-register-active-directory-authentication
[How to Register with the Azure Active Directory]: /documentation/articles/mobile-services-how-to-register-active-directory-authentication
<!-- keep by customization: end -->
[Azure Management Portal]: https://manage.windowsazure.cn/
[Active Directory Authentication Library for iOS]: https://github.com/MSOpenTech/azure-activedirectory-library-for-ios
