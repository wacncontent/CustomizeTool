<properties
	pageTitle="Azure AD Windows Phone Getting Started | Windows Azure"
	description="How to build a Windows Phone application that integrates with Azure AD for sign in and calls Azure AD protected APIs using OAuth."
	services="active-directory"
	documentationCenter="windows"
	authors="dstrockis"
	manager="mbaldwin"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="10/13/2015"
	wacn.date=""/>



# Integrate Azure AD with a Windows Phone App
<!-- deleted by customization

[AZURE.INCLUDE [active-directory-devquickstarts-switcher](../includes/active-directory-devquickstarts-switcher.md)]
-->

[AZURE.INCLUDE [active-directory-devguide](../includes/active-directory-devguide.md)]

If you're developing a windows phone app, Azure AD makes it simple and straightforward for you to authenticate your users with their Active Directory accounts.  It also enables your application to securely consume any web API protected by Azure AD, such as the Office 365 APIs or the Azure API.

For .NET native clients that need to access protected resources, Azure AD provides the Active Directory Authentication Library, or ADAL.  ADAL's sole purpose in life is to make it easy for your app to get access tokens.  To demonstrate just how easy it is, here we'll build a "Directory Searcher" Windows Phone 8.1 app that:

-	Gets access tokens for calling the Azure AD Graph API using the [OAuth 2.0 authentication protocol](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx).
-	Searches a directory for users with a given UPN.
-	Signs users out.

To build the complete working application, you'll need to:

2. Register your application with Azure AD.
3. Install & Configure ADAL.
5. Use ADAL to get tokens from Azure AD.

To get started, [download a skeleton project](https://github.com/AzureADQuickStarts/NativeClient-WindowsPhone/archive/skeleton.zip) or [download the completed sample](https://github.com/AzureADQuickStarts/NativeClient-WindowsPhone/archive/complete.zip).  Each is a Visual Studio 2013 solution.  You'll also need an Azure AD tenant in which you can create users and register an application.  If you don't already have a tenant, [learn how to get one](/documentation/articles/active-directory-howto-tenant).

## *1. Register the Directory Searcher Application*
To enable your app to get tokens, you'll first need to register it in your Azure AD tenant and grant it permission to access the Azure AD Graph API:

-	Sign into the [Azure Management Portal](https://manage.windowsazure.cn)
-	In the left hand nav, click on **Active Directory**
-	Select a tenant in which to register the application.
-	Click the **Applications** tab, and click **Add** in the bottom drawer.
-	Follow the prompts and create a new **Native Client Application**.
    -	The **Name** of the application will describe your application to end-users
    -	The **Redirect Uri** is a scheme and string combination that Azure AD will use to return token responses.  Enter a placeholder value for now, e.g. `http://DirectorySearcher`.  We'll replace this value later.
-	Once you've completed registration, AAD will assign your app a unique client identifier.  You'll need this value in the next sections, so copy it from the **Configure** tab.
- Also in **Configure** tab, locate the "Permissions to Other Applications" section.  For the "Azure Active Directory" application, add the **Access Your Organization's Directory** permission under **Delegated Permissions**.  This will enable your application to query the Graph API for users.

## *2. Install & Configure ADAL*
Now that you have an application in Azure AD, you can install ADAL and write your identity-related code.  In order for ADAL to be able to communicate with Azure AD, you need to provide it with some information about your app registration.
-	Begin by adding ADAL to the DirectorySearcher project using the Package Manager Console.

<!-- deleted by customization ``` -->
PM> Install-Package Microsoft.IdentityModel.Clients.ActiveDirectory
<!-- deleted by customization
```
-->

-	In the DirectorySearcher project, open `MainPage.xaml.cs`.  Replace the values in the `Config Values` region to reflect the values you input into the Azure Management Portal.  Your code will reference these values whenever it uses ADAL.
    -	The `tenant` is the domain of your Azure AD tenant, e.g. contoso.partner.onmschina.cn
    -	The `clientId` is the clientId of your application you copied from the portal.
-	You now need to discover the callback uri for your Windows Phone app.  Set a breakpoint on this line in the `MainPage` method:

<!-- deleted by customization
```
redirectURI = Windows.Security.Authentication.Web.WebAuthenticationBroker.GetCurrentApplicationCallbackUri();
```
-->
<!-- keep by customization: begin -->
		redirectURI = Windows.Security.Authentication.Web.WebAuthenticationBroker.  
		GetCurrentApplicationCallbackUri();

<!-- keep by customization: end -->
- Run the app, and copy aside the value of `redirectUri` when the breakpoint is hit.  It should look something like

<!-- deleted by customization
```
ms-app://s-1-15-2-1352796503-54529114-405753024-3540103335-3203256200-511895534-1429095407/
```
-->
<!-- keep by customization: begin -->
		ms-app://s-1-15-2-1352796503-54529114-405753024-3540103335-3203256200-  
		511895534-1429095407/
<!-- keep by customization: end -->

- Back on the **Configure** tab of your application in the Azure Management Portal, replace the value of the **RedirectUri** with this value.  

## *3.	Use ADAL to Get Tokens from AAD*
The basic principle behind ADAL is that whenever your app needs an access token, it simply calls `authContext.AcquireToken(…)`, and ADAL does the rest.  

-	The first step is to initialize your app's `AuthenticationContext` - ADAL's primary class.  This is where you pass ADAL the coordinates it needs to communicate with Azure AD and tell it how to cache tokens.

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
public MainPage()
{
    ...

    // ADAL for Windows Phone 8.1 builds AuthenticationContext instances <!-- deleted by customization through a factory -->
<!-- keep by customization: begin -->
    		//through a factory
<!-- keep by customization: end -->
    authContext = AuthenticationContext.CreateAsync(authority).GetResults();
<!-- deleted by customization
}
```
-->
<!-- keep by customization: begin -->
		}

<!-- keep by customization: end -->

- Now locate the `Search(...)` method, which will be invoked when the user cliks the "Search" button in the app's UI.  This method makes a GET request to the Azure AD Graph API to query for users whose UPN begins with the given search term.  But in order to query the Graph API, you need to include an access_token in the `Authorization` header of the request - this is where ADAL comes in.

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
private async void Search(object sender, RoutedEventArgs e)
{
    ...

    // Try to get a token without triggering any user prompt.
    // ADAL will check whether the requested token is in ADAL's token cache <!-- deleted by customization or can otherwise be obtained without user interaction. -->
<!-- deleted by customization
    AuthenticationResult result = await authContext.AcquireTokenSilentAsync(graphResourceId, clientId);
-->
<!-- keep by customization: begin -->
    		// or can otherwise be obtained without user interaction.
    AuthenticationResult result = await authContext.AcquireTokenSilentAsync(
    		graphResourceId, clientId);
<!-- keep by customization: end -->
    if (result != null && result.Status == AuthenticationStatus.Success)
    {
        // A token was successfully retrieved.
        QueryGraph(result);
    }
    else
    {
        // Acquiring a token without user interaction was not possible.
        // Trigger an authentication experience and specify that once a token <!-- deleted by customization has been obtained the QueryGraph method should be called -->
<!-- deleted by customization
        authContext.AcquireTokenAndContinue(graphResourceId, clientId, redirectURI, QueryGraph);
-->
<!-- keep by customization: begin -->
        		// has been obtained the QueryGraph method should be called  	
        authContext.AcquireTokenAndContinue(graphResourceId, clientId, 
				redirectURI, QueryGraph);
<!-- keep by customization: end -->
    }
<!-- deleted by customization
}
```
-->
<!-- keep by customization: begin -->
		}

<!-- keep by customization: end -->
- If interactive authentication is necessary, ADAL will use Windows Phone's Web Authentication Broker (WAB) and [continuation model](http://www.cloudidentity.com/blog/2014/06/16/adal-for-windows-phone-8-1-deep-dive/) to display the Azure AD sign in page.  When the user signs in, your app needs to pass ADAL the results of the WAB interaction.  This is as simple as implementing the `ContinueWebAuthentication` interface:

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
// This method is automatically invoked when the application
// is reactivated after an authentication interaction through <!-- deleted by customization WebAuthenticationBroker. -->
<!-- deleted by customization
public async void ContinueWebAuthentication(WebAuthenticationBrokerContinuationEventArgs args)
-->
<!-- keep by customization: begin -->
		// WebAuthenticationBroker.
		public async void ContinueWebAuthentication(  
		WebAuthenticationBrokerContinuationEventArgs args)
<!-- keep by customization: end -->
{
    // pass the authentication interaction results to ADAL, which will
    // conclude the token acquisition operation and invoke the callback <!-- deleted by customization specified in AcquireTokenAndContinue. -->
<!-- keep by customization: begin -->
    		// specified in AcquireTokenAndContinue.
<!-- keep by customization: end -->
    await authContext.ContinueAcquireTokenAsync(args);
}
<!-- deleted by customization
```
-->

- Now it's time to use the `AuthenticationResult` that ADAL returned to your app.  In the `QueryGraph(...)` callback, attach the access_token you acquired to the GET request in the Authorization header:

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
private async void QueryGraph(AuthenticationResult result)
{
    if (result.Status != AuthenticationStatus.Success)
    {
        MessageDialog dialog = new MessageDialog(string.Format("If the <!-- deleted by customization error continues, please contact your administrator.\n\nError: {0}\n\nError Description:\n\n{1}", result.Error, result.ErrorDescription), "Sorry, an error occurred while signing you in."); -->
<!-- keep by customization: begin -->
        		error continues, please contact your administrator.  
        		\n\nError: {0}\n\nError Description:\n\n{1}", result.Error,  
        		result.ErrorDescription), "Sorry, an error occurred while signing you  
        		in.");
<!-- keep by customization: end -->
        await dialog.ShowAsync();
    }

    // Add the access token to the Authorization Header of the call to <!-- deleted by customization the Graph API, and call the Graph API. -->
<!-- deleted by customization
    httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", result.AccessToken);
-->
<!-- keep by customization: begin -->
    		// the Graph API, and call the Graph API.
    		httpClient.DefaultRequestHeaders.Authorization = new  
    		AuthenticationHeaderValue("Bearer", result.AccessToken);
<!-- keep by customization: end -->

    ...
<!-- deleted by customization
}
```
-->
<!-- keep by customization: begin -->
		}  

<!-- keep by customization: end -->
- You can also use the `AuthenticationResult` object to display information about the user in your app. In the `QueryGraph(...)` method, use the result to show the user's id on the page:

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
// Update the Page UI to represent the signed in user
ActiveUser.Text = result.UserInfo.DisplayableId;
<!-- deleted by customization ``` -->
- Finally, you can use ADAL to sign the user out of hte application as well.  When the user clicks the "Sign Out" button, we want to ensure that the next call to `AcquireTokenSilentAsync(...)` will fail.  With ADAL, this is as easy as clearing the token cache:

<!-- deleted by customization ```C# --><!-- keep by customization: begin --> C# <!-- keep by customization: end -->
private void SignOut()
{
    // Clear session state from the token cache.
    authContext.TokenCache.Clear();

    ...
<!-- deleted by customization
}
```
-->
<!-- keep by customization: begin -->
		}

<!-- keep by customization: end -->

Congratulations! You now have a working Windows Phone app that has the ability to authenticate users, securely call Web APIs using OAuth 2.0, and get basic information about the user.  If you haven't already, now is the time to populate your tenant with some users.  Run your DirectorySearcher app, and sign in with one of those users.  Search for other users based on their UPN.  Close the app, and re-run it.  Notice how the user's session remains intact.  Sign out, and sign back in as another user.

ADAL makes it easy to incorporate all of these common identity features into your application.  It takes care of all the dirty work for you - cache management, OAuth protocol support, presenting the user with a login UI, refreshing expired tokens, and more.  All you really need to know is a single API call, `authContext.AcquireToken*(…)`.

For reference, the completed sample (without your configuration values) is provided [here](https://github.com/AzureADQuickStarts/NativeClient-WindowsPhone/archive/complete.zip).  You can now move on to additional identity scenarios.  You may want to try:

[Secure a .NET Web API with Azure AD >>](/documentation/articles/active-directory-devquickstarts-webapi-dotnet)

<!-- deleted by customization
[AZURE.INCLUDE [active-directory-devquickstarts-additional-resources](../includes/active-directory-devquickstarts-additional-resources.md)]
 
-->
<!-- keep by customization: begin -->
For additional resources, check out:  

- [AzureADSamples on GitHub >>](https://github.com/AzureAdSamples)
- [CloudIdentity.com >>](https://cloudidentity.com)
- Azure AD documentation on [www.windowsazure.cn >>](/documentation/services/identity/)

<!-- keep by customization: end -->