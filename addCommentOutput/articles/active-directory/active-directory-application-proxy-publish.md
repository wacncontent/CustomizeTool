<properties
	pageTitle="Publishing Apps with Azure AD Application Proxy | Windows Azure"
	description="Covers how to publish on-premises applications using Azure AD Application Proxy."
	services="active-directory"
	documentationCenter=""
	authors="kgremban"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/02/2015"
	wacn.date=""/>


# Publish applications using Azure AD Application Proxy

> [AZURE.NOTE] Application Proxy is a feature that is available only if you upgraded to the Premium or Basic edition of Azure Active Directory. For more information, see [Azure Active Directory <!-- deleted by customization editions](/documentation/articles/active-directory-editions) --><!-- keep by customization: begin --> editions](https://msdn.microsoft.com/zh-cn/library/azure/dn532272.aspx) <!-- keep by customization: end -->.

After you enable <!-- deleted by customization Windows --> Azure AD Application Proxy, you can publish applications to make them accessible <!-- deleted by customization to --><!-- keep by customization: begin --> for <!-- keep by customization: end --> your users outside your private network.

This <!-- deleted by customization article --><!-- keep by customization: begin --> section <!-- keep by customization: end --> walks you through the steps <!-- keep by customization: begin --> necessary <!-- keep by customization: end --> to publish applications that are running on your local network for which you want to enable secure remote access from outside your network.

> [AZURE.NOTE] To verify that the Connector is running properly, the first application you publish should be any website accessible from within your private network to assure users can access it from the Internet, before publishing an actual application.

## Publish an app using the wizard

1. Open a browser of your choice and go to the Azure Management Portal.
2. In the left pane of the Azure Management Portal, click the Active Directory tab.
3. Click the directory in which you enabled Application Proxy and for which you want to publish an application (for example, Wingtip Toys).
4. Click the **Applications** tab, and then click the **Add** button at the bottom of the screen
<!-- deleted by customization
	![Add application](./media/active-directory-application-proxy-publish/aad_appproxy_selectdirectory.png)
-->
<!-- keep by customization: begin -->
	![Add application](http://i.imgur.com/wEeZ7IR.png)
<!-- keep by customization: end -->
5. In the What do you want to do? dialog box, click **Publish an application that will be accessible outside your network**.
	![New application that will be accessible from outside your <!-- deleted by customization network](./media/active-directory-application-proxy-publish/aad_appproxy_addapp.png) --><!-- keep by customization: begin --> network](http://i.imgur.com/Wj3vkyD.png) <!-- keep by customization: end -->

6. Follow the instructions on the screen to provide the following information about your application:
<!-- deleted by customization
	![Application properties](./media/active-directory-application-proxy-publish/aad_appproxy_appproperties.png)
-->
<!-- keep by customization: begin -->
	![Application properties](http://i.imgur.com/MkPNc93.png)
<!-- keep by customization: end -->

**Setting** | **Details**
---|---
External URL | This is the URL of the cloud service that is used to access the application from outside your private network. The URL is automatically generated based on the name you provided, with the suffix msappproxy.net.
Preauthentication <!-- deleted by customization method --><!-- keep by customization: begin --> Method <!-- keep by customization: end --> | <p>Set the type of preauthentication method you want the application to use:</p><p>a. Windows Azure Active Directory (Windows Azure AD) - <!-- keep by customization: begin --> sets the preauthentication method to Windows Azure Active Directory (Windows Azure AD). <!-- keep by customization: end --> When a user tries to access an application, Application Proxy will redirect the user to log in with Azure AD which will authenticate the user, ensuring that the user has the necessary permissions for the directory and the application.</p> <p>b. Pass through <!-- deleted by customization - preauthentication --><!-- keep by customization: begin --> -preauthentication <!-- keep by customization: end --> is not performed.</p>
<!-- deleted by customization
External URL Protocol | <p>By default, applications are published by using the HTTPS protocol. The service will automatically redirect users who type the URL with http.</p> <p>To enable HTTP for an internal application, you have to set the preauthentication method to Passthrough and then you are able to change the External URL protocol from HTTPS to HTTP. Note that publishing applications by using HTTP may create security issues for your application and your users.</p> <p>You can insert a custom domain rather than using the default suffix msappproxy.net. For more information, see [Working with custom domains](/documentation/articles/active-directory-application-proxy-custom-domains).</p>
Internal URL | <p>This is the internal URL that the Application Proxy connector uses to access the application internally. This should be the URL of the published application that is used to access the application from inside your private network. This is a valid URL with no spaces or symbols.</p> <p>You can specify a specific path on the backend server to publish, while the rest of the server is not published. This allows you to publish, for example, different sites located on the same SharePoint server with different names and access rules.</p> <p>The path is specified in the internal URL field and will be visible in the external URL. The internal and external paths must be identical.</p>
-->
<!-- keep by customization: begin -->
External URL Protocol | <p>By default, applications are published by using the HTTPS protocol.</p> <p>To enable HTTP for an internal application, you have to set Preauthentication to Passthrough and then you are able to change the External URL protocol from HTTPS to HTTP.</p> <p>Note that publishing applications by using HTTP may create security issues for your application and your users.</p> <p>You can insert a custom domain rather than using the default of msappproxy.net. For more information, see below.</p>
Internal URL | This is the internal URL that the Application Proxy connector uses to access the application internally. This should be the URL of the published application that is used to access the application from inside your private network. This is a valid URL with no path and no spaces or symbols.
<!-- keep by customization: end -->

To finish the wizard, click the check mark at the bottom of the screen. The application is now defined in Azure AD.


## Assign users and groups to the application

1. For apps that are preauthenticated, you must assign users and groups that will have access to the app. <p>For apps that are passthrough, access is available for all users. However, in order for a user to see the app in their application list, you must assign the app to that user.
2. After finishing the Add App wizard, the App Proxy Quick Start page is displayed. To assign users, click **Assign users**.
<!-- deleted by customization
	![Application Proxy quick start screen](./media/active-directory-application-proxy-publish/quickstart.png)
-->
<!-- keep by customization: begin -->
	![Application Proxy quick start screen](http://i.imgur.com/OmuWElV.png)
<!-- keep by customization: end -->
3. Select each user or group you want to assign to this app and click **Assign**.

> [AZURE.NOTE] For Integrated Windows Authentication apps, you can assign only users and groups that are synced from your on-prem Active Directory. Users logging in using a Microsoft account and guests cannot be assigned for apps published with Azure Active Directory Application Proxy. Make sure the users you assign log in with their credentials that are part of the same domain as the app you are publishing.

## Advanced configuration

1. You can modify published apps or configure advanced options, such as SSO to on-prem applications, from the <!-- deleted by customization Configure --><!-- keep by customization: begin --> **Configure** <!-- keep by customization: end --> page.
<!-- deleted by customization
	![Advanced configuration](./media/active-directory-application-proxy-publish/advancedconfig.png)
-->
<!-- keep by customization: begin -->
	![Advanced configuration](http://i.imgur.com/FhbRvoq.png)
<!-- keep by customization: end -->

2. Select the app and click **Configure**. The following options are available:

**Setting** | **Details**
---|---
Name | Provide a descriptive name for your application
External URL | This is the URL of the cloud service that is used to access the application from outside your private network. The URL is automatically generated based on the name you provided, with the suffix <!-- deleted by customization msappproxy.net. --><!-- keep by customization: begin --> **msappproxy.net.** <!-- keep by customization: end -->
<!-- deleted by customization
Preauthentication method | <p>Set the type of preauthentication method you want the application to use:</p><p>a. Windows Azure Active Directory (Windows Azure AD) - When a user tries to access an application, Application Proxy will redirect the user to log in with Azure AD which will authenticate the user, ensuring that the user has the necessary permissions for the directory and the application.</p> <p>b. Pass through - preauthentication is not performed.</p>
External URL Protocol | <p>By default, applications are published by using the HTTPS protocol. The service will automatically redirect users who type the URL with http.</p> <p>To enable HTTP for an internal application, you have to set the preauthentication method to Passthrough and then you are able to change the External URL protocol from HTTPS to HTTP. Note that publishing applications by using HTTP may create security issues for your application and your users.</p> <p>You can insert a custom domain rather than using the default suffix msappproxy.net. For more information, see [Working with custom domains](/documentation/articles/active-directory-application-proxy-custom-domains).</p>
Internal URL | <p>This is the internal URL that the Application Proxy connector uses to access the application internally. This should be the URL of the published application that is used to access the application from inside your private network. This is a valid URL with no spaces or symbols.</p> <p>You can specify a specific path on the backend server to publish, while the rest of the server is not published. This allows you to publish, for example, different sites located on the same SharePoint server with different names and access rules.</p> <p>The path is specified in the internal URL field and will be visible in the external URL. The internal and external paths must be identical.</p>
Translate URL in headers | For applications (such as some SharePoint configurations) that necessitate that the HTTP host headers are not translated, set this to **No**. This will disable header translation for both request and response headers.
Internal authentication method | <p>If you use Application Proxy for preauthentication, you can set an internal authentication method to enable your users to benefit from single sign-on (SSO) to this application.</p> <p> Select **Integrated Windows Authentication (IWA)** if your application uses IWA and you can configure Kerberos Constrained Delegation (KCD) to enable SSO for this application. Applications that use IWA must be configured using KCD, otherwise Application Proxy will not be able to publish these applications.</p> <p>Select **None** if your application does not use IWA.</p> <p>For more information, see [Single sign-on with App Proxy](/documentation/articles/active-directory-application-proxy-sso-using-kcd).</p>
Internal Application SPN | <!-- deleted by customization <p>This --> is the Service-Principal-Name (SPN) of the internal application as configured in the on-prem Application Proxy. The SPN is used by the Application Proxy Connector to fetch Kerberos tokens for the application using Kerberos Constrained Delegation <!-- deleted by customization (KCD).</p> <p>For --><!-- keep by customization: begin --> (KCD). <p> For <!-- keep by customization: end --> more information, see <!-- deleted by customization [Enable single-sign on](/documentation/articles/active-directory-application-proxy-sso-using-kcd).</p> -->
-->
<!-- keep by customization: begin -->
Preauthentication Method | Set the type of preauthentication method you want the application to use:<p>Active directory - sets the preauthentication method to Active Directory. When a user tries to access an application, Application Proxy will redirect the user to log in with Application Proxy which will authenticate the user, ensuring that the user has the necessary permissions for the directory and the application.</p><p> Pass through -preauthentication is not performed.</p>
External URL | By default, applications are published by using the HTTPS protocol. To enable HTTP for an internal application, you have to set Preauthentication to Passthrough and then you are able to change the External URL protocol from HTTPS to HTTP. Note that publishing applications by using HTTP may create security issues for your application and your users. You can set a custom domain rather than using the default domain provided (msappproxy.net). For more information, see Working with Custom Domains.
Internal URL | This is the internal URL that the Application Proxy Connector uses to access the application internally. This should be the URL of the published application that is used to access the application from inside your private network. This is a valid URL with no path and no spaces or symbols.
Translate URL in Headers | For applications (such as some SharePoint configurations) that necessitate that the HTTP host headers are not translated, set this to No. This will disable header translation for both request and response headers.
Internal Authentication Method | If you use Application Proxy for preauthentication, you can set an internal authentication method to enable your users to benefit from single-sign on (SSO) to this application. <p> Select **Integrated Windows Authentication (IWA)** if your application uses IWA and you can configure Kerberos Constrained Delegation (KCD) to enable SSO for this application. <p> Select **None** if your application does not use IWA. <p> Applications that use IWA must be configured using KCD, otherwise Application Proxy will not be able to publish these applications. <p> For more information, see SSO for On Prem IWA Apps Using KCD with App Proxy
Internal Application SPN | <!-- deleted by customization <p>This -->This is the Service-Principal-Name (SPN) of the internal application as configured in the on-prem Application Proxy. The SPN is used by the Application Proxy Connector to fetch Kerberos tokens for the application using Kerberos Constrained Delegation <!-- deleted by customization (KCD).</p> <p>For --><!-- keep by customization: begin --> (KCD). <p> For <!-- keep by customization: end --> more information, see <!-- deleted by customization [Enable single-sign on](/documentation/articles/active-directory-application-proxy-sso-using-kcd).</p> -->SSO for On Prem IWA Apps Using KCD with App Proxy
<!-- keep by customization: end -->

After you publish applications using Azure Active Directory Application Proxy, they appear in the Applications list in Azure AD, and you can manage them there.
If you disable Application Proxy services after you have published applications, the applications are not deleted, but will no longer be accessible from outside your private network.
To view an application and make sure it is accessible, double-click the name of the application. If the Application Proxy service is disabled and the application is not available, a warning message appears at the top of the screen.
<!-- deleted by customization

To delete an application, select an application in the list and then click **Delete**.

## See also
There's a lot more you can do with Application Proxy:

- [Enable Application Proxy](/documentation/articles/active-directory-application-proxy-enable)
- [Publish applications using your own domain name](/documentation/articles/active-directory-application-proxy-custom-domains)
- [Enable single-sign on](/documentation/articles/active-directory-application-proxy-sso-using-kcd)
- [Enable conditional access](/documentation/articles/active-directory-application-proxy-conditional-access)
- [Working with claims aware applications](/documentation/articles/active-directory-application-proxy-claims-aware-apps)
- [Troubleshoot issues you're having with Application Proxy](/documentation/articles/active-directory-application-proxy-troubleshoot)

## Learn more about Application Proxy
- [Take a look here at our online help](/documentation/articles/active-directory-application-proxy-enable)
- [Check out the Application Proxy blog](http://blogs.technet.com/b/applicationproxyblog/)
- [Watch our videos on Channel 9!](http://channel9.msdn.com/events/Ignite/2015/BRK3864)
-->
<!-- keep by customization: begin -->
To delete an application, select an application in the list, and then click **Delete**.
<!-- keep by customization: end -->

## Additional resources

* [About Kerberos constrained delegation](http://technet.microsoft.com/zh-cn/library/cc995228.aspx)
