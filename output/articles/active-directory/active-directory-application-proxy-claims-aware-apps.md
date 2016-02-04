<properties
	pageTitle="Working with Claims Aware Apps in Application Proxy"
	description="Covers how to get up and running with Azure AD Application Proxy."
	services="active-directory"
	documentationCenter=""
	authors="kgremban"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="01/07/2016"
	wacn.date=""/>



# Working with claims aware apps in Application Proxy

> [AZURE.IMPORTANT] Application Proxy is a feature that is available only if you upgraded to the Premium or Basic edition of Azure Active Directory. For more information, see [Azure Active Directory editions](/documentation/articles/active-directory-editions).

Claims aware apps perform a redirection to the Security Token Service (STS), which in turn requests credentials from the user in exchange for a token before redirecting the user to the application. To enable Application Proxy to work with these redirects, the following steps need to be taken.

## Prerequisite

Before performing this procedure, make sure that the STS the claims aware app redirects to is available outside of your on-premises network.


### Azure Management Portal configuration

1. Publish your application according to the instructions described in [Publish applications with Application Proxy](/documentation/articles/active-directory-application-proxy-publish).
2. In the list of applications, select the claims aware app and click **Configure**.
3. If you chose **Passthrough** as your **Preauthentication Method**, make sure to select **HTTPS** as your **External URL** scheme.
4. If you chose **Azure Active Directory** as your **Preauthentication Method**, select **None** as your **Internal Authentication Method**.


### ADFS configuration

1. Open ADFS Management.
2. Go to **Relying Party Trusts**, right click on the app you are publishing with Application Proxy, and choose **Properties**.  
  ![Relying Party Trusts right click on app name - screentshot](./media/active-directory-application-proxy-claims-aware-apps/appproxyrelyingpartytrust.png)  
3. On the **Endpoints** tab, under **Endpoint type**, select **WS-Federation**.
4. Under **Trusted URL** enter the URL you entered in the Application Proxy under **External URL** and click **OK**.  
  ![Add an Endpoint - set Trusted URL value - screenshot](./media/active-directory-application-proxy-claims-aware-apps/appproxyendpointtrustedurl.png)  

## See also
There's a lot more you can do with Application Proxy:

- [Publish applications with Application Proxy](/documentation/articles/active-directory-application-proxy-publish)
- [Publish applications using your own domain name](/documentation/articles/active-directory-application-proxy-custom-domains)
- [Enable single-sign on](/documentation/articles/active-directory-application-proxy-sso-using-kcd)
- [Troubleshoot issues you're having with Application Proxy](/documentation/articles/active-directory-application-proxy-troubleshoot)

## Learn more about Application Proxy
- [Take a look at our online help](/documentation/articles/active-directory-application-proxy-enable)
- [Check out the Application Proxy blog](http://blogs.technet.com/b/applicationproxyblog/)
- [Watch our videos on Channel 9!](http://channel9.msdn.com/events/Ignite/2015/BRK3864)

## Additional Resources

* [Sign up for Azure as an organization](/documentation/articles/sign-up-organization)
* [Azure Identity](/documentation/articles/fundamentals-identity)
