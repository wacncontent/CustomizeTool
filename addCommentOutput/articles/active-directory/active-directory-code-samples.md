<properties
   pageTitle="Azure Active Directory Code Samples | Windows Azure"
   description="An index of Azure Active Directory code samples, organized by scenario."
   services="active-directory"
   documentationCenter="dev-center-name"
   authors="msmbaldwin"
   manager="mbaldwin"
   editor=""/>

<tags
	ms.service="active-directory"
	ms.date="09/17/2015"
	wacn.date=""/>

# Azure Active Directory Code Samples

[AZURE.INCLUDE [active-directory-devguide](../includes/active-directory-devguide.md)]

You can use Windows Azure Active Directory (Azure AD) to add authentication and authorization to your web sites and web APIs. This section links you to code samples that show you how it's done and code snippets that you can use in your applications. On the code sample page, you'll find detailed read-me topics that help with requirements, installation and set-up. And the code is commented to help you understand the critical sections.

To understand the basic scenario for each sample type, see Authentication Scenarios for Azure AD.

Contribute to our samples on GitHub: [Windows Azure Active Directory Samples and Documentation](https://github.com/AzureADSamples).

<!-- deleted by customization
## Web Browser to web site
-->
<!-- keep by customization: begin -->
## Web Browser to Web Site 
<!-- keep by customization: end -->

These samples show how to write a web site that directs the userâs browser to sign them in to Azure AD.



| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| C#/.NET | [WebApp-OpenIDConnect-DotNet](http://github.com/AzureADSamples/WebApp-OpenIDConnect-DotNet) | Use OpenID Connect (ASP.Net OpenID Connect OWIN middleware) to authenticate users from an Azure AD tenant.
| C#/.NET | [WebApp-MultiTenant-OpenIdConnect-DotNet](https://github.com/AzureADSamples/WebApp-MultiTenant-OpenIdConnect-DotNet) | A multi-tenant .NET MVC web site that uses OpenID Connect (ASP.Net OpenID Connect OWIN middleware) to authenticate users from multiple Azure AD tenants.
| C#/.NET | [WebApp-WSFederation-DotNet](https://github.com/AzureADSamples/WebApp-WSFederation-DotNet) | Use WS-Federation (ASP.Net WS-Federation OWIN middleware) to authenticate users from an Azure AD tenant.

## Single Page Application (SPA)

This sample shows how to write a single page application secured with Azure AD.  

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| JavaScript, C#/.NET | [SinglePageApp-DotNet](https://github.com/Azure-Samples/active-directory-angularjs-singlepageapp) | Use ADAL for JavaScript and Azure AD to secure an AngularJS-based single page app implemented with an ASP.NET web API back end.


## Native Application to Web API
<!-- deleted by customization
These code samples show how to build native client applications that call web APIs that are secured by Azure AD. They use [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) and [OAuth 2.0 in Azure AD](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx).
-->
<!-- keep by customization: begin -->
 
These code samples show how to build native client applications that call web APIs that are secured by Azure AD. They use [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) and [OAuth 2.0 in Azure AD](https://msdn.microsoft.com/zh-CN/library/azure/dn645545.aspx).
 
<!-- keep by customization: end -->
| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| Javascript | [NativeClient-MultiTarget-Cordova](https://github.com/AzureADSamples/NativeClient-MultiTarget-Cordova) | Use the ADAL plugin for Apache Cordova to build an Apache Cordova app that calls a web API and uses Azure AD for authentication.
| C#/.NET | [NativeClient-DotNet](http://github.com/AzureADSamples/NativeClient-DotNet) | A .NET WPF application that calls a web API that is secured by using Azure AD.
| C#/.NET | [NativeClient-WindowsStore](http://github.com/AzureADSamples/NativeClient-WindowsStore) | A Windows Store application that calls a web API that is secured with Azure AD.
| C#/.NET | [NativeClient-WebAPI-MultiTenant-WindowsStore](https://github.com/AzureADSamples/NativeClient-WebAPI-MultiTenant-WindowsStore) | A Windows Store application calling a multi-tenant web API that is secured with Azure AD.
| C#/.NET | [WebAPI-OnBehalfOf-DotNet](http://github.com/AzureADSamples/WebAPI-OnBehalfOf-DotNet) | A native client application that calls a web API, which gets a token to act on behalf of the original user, and then uses the token to call another web API.
| C#/.NET | [NativeClient-WindowsPhone8.1](https://github.com/AzureADSamples/NativeClient-WindowsPhone8.1) | A Windows Store application for Windows Phone 8.1 that calls a web API that is secured by Azure AD.
| ObjC | [NativeClient-iOS](http://github.com/AzureADSamples/NativeClient-iOS) | An iOS application that calls a web API that requires Azure AD for authentication.
| C#/.NET | [WebAPI-ManuallyValidateJwt-DotNet](https://github.com/AzureADSamples/WebAPI-ManuallyValidateJwt-DotNet) | A native client application that includes logic to process a JWT token in a web API, instead of using OWIN middleware.
| C#/Xamarin | [NativeClient-Xamarin-Android](https://github.com/AzureADSamples/NativeClient-Xamarin-Android) | A Xamarin binding to the native Azure AD Authentication Library (ADAL) for the Android library.
| C#/Xamarin | [NativeClient-Xamarin-iOS](http://github.com/AzureADSamples/NativeClient-Xamarin-iOS) | A Xamarin binding to the native Azure AD Authentication Library (ADAL) for iOS.
| C#/Xamarin | [NativeClient-MultiTarget-DotNet](http://github.com/AzureADSamples/NativeClient-MultiTarget-DotNet) | A Xamarin project that targets five platforms and calls a web API that is secured by Azure AD.
| C#/.NET | [NativeClient-Headless-DotNet](http://github.com/AzureADSamples/NativeClient-Headless-DotNet) | A native application that performs non-interactive authentication and calls a web API that is secured by Azure AD.

<!-- deleted by customization


## web site to Web API

These code samples show how use [OAuth 2.0 in Azure AD](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx) to build web sites that call web APIs that are secured by Azure AD.
-->
<!-- keep by customization: begin -->
   

## Web Site to Web API

These code samples show how use [OAuth 2.0 in Azure AD](https://msdn.microsoft.com/zh-CN/library/azure/dn645545.aspx) to build web sites that call web APIs that are secured by Azure AD.
<!-- keep by customization: end -->

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| C#/.NET | [WebApp-WebAPI-OpenIDConnect-DotNet](http://github.com/AzureADSamples/WebApp-WebAPI-OpenIDConnect-DotNet) | Call a web API with the signed-in user's permissions.
|  C#/.NET | [WebApp-WebAPI-OAuth2-AppIdentity-DotNet](http://github.com/AzureADSamples/WebApp-WebAPI-OAuth2-AppIdentity-DotNet) | Call a web API with the application's permissions.
| C#/.NET | [WebApp-WebAPI-OAuth2-UserIdentity-Dotnet](http://github.com/AzureADSamples/WebApp-WebAPI-OAuth2-UserIdentity-Dotnet) | Add authorization with [OAuth 2.0 in Azure <!-- deleted by customization AD](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx) --><!-- keep by customization: begin --> AD](https://msdn.microsoft.com/zh-CN/library/azure/dn645545.aspx) <!-- keep by customization: end --> to an existing web site so it can call a web API.
| JavaScript | [WebAPI-Nodejs](http://github.com/AzureADSamples/WebAPI-Nodejs) | Set up a REST API service that's integrated with Azure AD for API protection. Includes a Node.js server with a Web API.
| C#/.NET | [WebApp-WebAPI-MultiTenant-OpenIdConnect-DotNet](https://github.com/AzureADSamples/WebApp-WebAPI-MultiTenant-OpenIdConnect-DotNet) |  A multi-tenant MVC web site that uses OpenID Connect (ASP.Net OpenID Connect OWIN middleware) to authenticate users from an Azure AD tenant. Uses an authorization code to invoke the Graph API.

## Server or Daemon Application to Web API

These code samples show how to build a daemon or server application that gets resources from a web API by using [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end --> and [OAuth 2.0 in Azure <!-- deleted by customization AD](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx) --><!-- keep by customization: begin --> AD](https://msdn.microsoft.com/zh-CN/library/azure/dn645545.aspx) <!-- keep by customization: end -->.

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| C#/.NET | [Daemon-DotNet](http://github.com/AzureADSamples/Daemon-DotNet) | A console application calls a web API. The client credential is a password.
| C#/.NET | [Daemon-CertificateCredential-DotNet](http://github.com/AzureADSamples/Daemon-CertificateCredential-DotNet) | A console application that calls a web API. The client credential is a certificate.


## Calling Azure AD Graph API

These code sample show how to build applications that call the Azure AD Graph API to read and write directory data.

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| Java | [WebApp-GraphAPI-Java](http://github.com/AzureADSamples/WebApp-GraphAPI-Java) | A web site that uses the Graph API to access Azure AD directory data.
| PHP | [WebApp-GraphAPI-PHP](http://github.com/AzureADSamples/WebApp-GraphAPI-PHP) | A web site that uses the Graph API to access Azure AD directory data.
| C#/.NET | [WebApp-GraphAPI-DotNet](http://github.com/AzureADSamples/WebApp-GraphAPI-DotNet) | A web site that uses the Graph API to access Azure AD directory data.
| C#/.NET | [ConsoleApp-GraphAPI-DotNet](https://github.com/AzureADSamples/ConsoleApp-GraphAPI-DotNet) | This console app demonstrates common Read and Write calls to the Graph API, and shows how to execute user license assignment and update a user's thumbnail photo and links.
| C#/.NET | [ConsoleApp-GraphAPI-DiffQuery-DotNet](https://github.com/AzureADSamples/ConsoleApp-GraphAPI-DiffQuery-DotNet) | A console application that uses the differential query in the Graph API to get periodic changes to user objects in an Azure AD tenant.
| C#/.NET | [WebApp-GraphAPI-DirectoryExtensions-DotNet](https://github.com/AzureADSamples/WebApp-GraphAPI-DirectoryExtensions-DotNet) | An MVC application uses Graph API queries to generate a simple company organizational chart.
| PHP | [WebApp-GraphAPI-DirectoryExtensions-PHP](https://github.com/AzureADSamples/WebApp-GraphAPI-DirectoryExtensions-PHP) | A PHP application that calls the Graph API to register an extension and then read, update, and delete values in the extension attribute.


## Authorization

These code samples show how to use Azure AD for authorization.

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| C#/.NET | [WebApp-GroupClaims-DotNet](https://github.com/AzureADSamples/WebApp-GroupClaims-DotNet) | Perform role based access control (RBAC) using Azure Active Directory group claims in an application that is integrated with Azure AD.
| C#/.NET | [WebApp-RoleClaims-DotNet](https://github.com/AzureADSamples/WebApp-RoleClaims-DotNet) | Perform role based access control (RBAC) using Azure Active Directory application roles in an application that is integrated with Azure AD.


## Legacy Walkthroughs

These walkthroughs use slightly older technology, but still might be of interest.

| Language/Platform | Sample | Description
| ----------------- | ------ | -----------
| C#/.NET | [Role-Based and ACL-Based Authorization in a Windows Azure AD <!-- deleted by customization Application](https://code.msdn.microsoft.com:443/Role-Based-and-ACL-Based-86ad71a1) --><!-- keep by customization: begin --> Application](http://code.msdn.microsoft.com/Role-Based-and-ACL-Based-86ad71a1) <!-- keep by customization: end --> | Perform role-based authorization (RBAC) and ACL-based authorization in an application that is integrated with Azure AD.
| C#/.NET |  [AAL - Windows Store app to REST service - <!-- deleted by customization Authentication](https://code.msdn.microsoft.com:443/windowsapps/AAL-Windows-Store-app-to-2430e331) --><!-- keep by customization: begin --> Authentication](http://code.msdn.microsoft.com/windowsapps/AAL-Windows-Store-app-to-2430e331) <!-- keep by customization: end --> |  Use [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end --> (formerly AAL) for Windows Store Beta to add user authentication capabilities to a Windows Store app.
| C#/.NET | [ADAL - Native App to REST service - Authentication with AAD via Browser <!-- deleted by customization Dialog](https://code.msdn.microsoft.com:443/AAL-Native-Application-to-fd648dcf) --><!-- keep by customization: begin --> Dialog](http://code.msdn.microsoft.com/AAL-Native-Application-to-fd648dcf) <!-- keep by customization: end --> |  Use [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end --> to add user authentication capabilities to a WPF client.
| C#/.NET | [ADAL - Native App to REST service - Authentication with ACS via Browser Dialog](http://code.msdn.microsoft.com/AAL-Native-App-to-REST-de57f2cc) |  Use [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end --> and [Access Control Service 2.0 <!-- deleted by customization (ACS)](http://msdn.microsoft.com/zh-cn/library/azure/hh147631.aspx) --><!-- keep by customization: begin --> (ACS)](https://msdn.microsoft.com/zh-CN/library/azure/hh147631.aspx) <!-- keep by customization: end --> to add user authentication capabilities to a WPF client.
| C#/.NET | [ADAL - Server to Server <!-- deleted by customization Authentication](https://code.msdn.microsoft.com:443/AAL-Server-to-Server-9aafccc1) --><!-- keep by customization: begin --> Authentication](http://code.msdn.microsoft.com/AAL-Server-to-Server-9aafccc1) <!-- keep by customization: end --> | Use [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end --> to secure service calls from a server side process to an MVC4 Web API REST service.
| C#/.NET | [Adding Sign-On to Your <!-- deleted by customization web site --><!-- keep by customization: begin --> Web Site <!-- keep by customization: end --> Using Azure <!-- deleted by customization AD](https://msdn.microsoft.com/zh-cn/library/azure/dn151790.aspx) --><!-- keep by customization: begin --> AD](https://msdn.microsoft.com/zh-CN/library/azure/dn151790.aspx) <!-- keep by customization: end --> | Configure a .NET application to perform web single sign-on against your Azure AD enterprise directory.
| C#/.NET | [Developing Multi-Tenant <!-- deleted by customization web sites --><!-- keep by customization: begin --> Web Sites <!-- keep by customization: end --> with Azure <!-- deleted by customization AD](https://msdn.microsoft.com/zh-cn/library/azure/dn151789.aspx) --><!-- keep by customization: begin --> AD](https://msdn.microsoft.com/zh-CN/library/azure/dn151789.aspx) <!-- keep by customization: end --> | Use Azure AD to add to the single sign-on and directory access capabilities of one .NET application to work across multiple organizations.
JAVA | [Java Sample App for Azure AD Graph <!-- deleted by customization API](https://code.msdn.microsoft.com:443/Java-Sample-App-for-30d36d54) --><!-- keep by customization: begin --> API](http://code.msdn.microsoft.com/Java-Sample-App-for-30d36d54) <!-- keep by customization: end --> | Use the Graph API to access directory data from Azure AD.
PHP | [PHP Sample App for Azure AD Graph API](http://code.msdn.microsoft.com/PHP-Sample-App-For-Windows-228c6ddb) | Use the Graph API to access directory data from Azure AD.
| C#/.NET | [Sample App for Azure AD Graph <!-- deleted by customization API](https://code.msdn.microsoft.com:443/Write-Sample-App-for-79e55502) --><!-- keep by customization: begin --> API](http://code.msdn.microsoft.com/Write-Sample-App-for-79e55502) <!-- keep by customization: end --> | Use the Graph API to access directory data from Azure AD.
| C#/.NET | [Sample App for Azure AD Graph Differential <!-- deleted by customization Query](https://code.msdn.microsoft.com:443/Sample-App-for-Windows-97eaec90) --><!-- keep by customization: begin --> Query](http://code.msdn.microsoft.com/Sample-App-for-Windows-97eaec90) <!-- keep by customization: end --> | Use the differential query in the Graph API to get periodic changes to user objects in an Azure AD tenant.
| C#/.NET | [Sample App for Integrating Multi-Tenant Cloud Application for Azure <!-- deleted by customization AD](https://code.msdn.microsoft.com:443/Multi-Tenant-Cloud-8015b84b) --><!-- keep by customization: begin --> AD](http://code.msdn.microsoft.com/Multi-Tenant-Cloud-8015b84b) <!-- keep by customization: end --> | Integrate a multi-tenant application into Azure AD.
| C#/.NET | [Securing a Windows Store Application and REST Web Service Using Azure AD <!-- deleted by customization (Preview)](https://msdn.microsoft.com/zh-cn/library/azure/dn169448.aspx) --><!-- keep by customization: begin --> (Preview)](https://msdn.microsoft.com/zh-CN/library/azure/dn169448.aspx) <!-- keep by customization: end --> | Create a simple web API resource and a Windows Store client application using Azure AD and the [Azure AD Authentication Library <!-- deleted by customization (ADAL)](https://msdn.microsoft.com/zh-cn/library/jj573266) --><!-- keep by customization: begin --> (ADAL)](https://msdn.microsoft.com/zh-CN/library/jj573266) <!-- keep by customization: end -->.
| C#/.NET| [Using the Graph API to Query Azure <!-- deleted by customization AD](https://msdn.microsoft.com/zh-cn/library/azure/dn151791.aspx) --><!-- keep by customization: begin --> AD](https://msdn.microsoft.com/zh-CN/library/azure/dn151791.aspx) <!-- keep by customization: end --> | Configure a Microsoft .NET application to use the Azure AD Graph API to access data from an Azure AD tenant directory.

## See also

##### Other Resources

[Azure Active Directory Developer's Guide](/documentation/articles/active-directory-developers-guide)

[Azure AD Graph API Helper Library](http://code.msdn.microsoft.com/Windows-Azure-AD-Graph-API-a8c72e18)

[Developing Modern Applications using OAuth and Active Directory Federation <!-- deleted by customization Services](http://msdn.microsoft.com/zh-cn/library/dn633593.aspx) --><!-- keep by customization: begin --> Services](https://msdn.microsoft.com/zh-CN/library/dn633593.aspx) <!-- keep by customization: end -->
