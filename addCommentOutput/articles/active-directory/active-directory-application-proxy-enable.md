<properties
	pageTitle="Enabling Azure AD Application Proxy | Windows Azure"
	description="Covers how to get up and running with Azure AD Application Proxy."
	services="active-directory"
	documentationCenter=""
	authors="kgremban"
	manager="StevenPo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/02/2015"
	wacn.date=""/>

# Enabling Azure AD Application Proxy
> [AZURE.NOTE] Application Proxy is a feature that is available only if you upgraded to the Premium or Basic edition of Azure Active Directory. For more information, see [Azure Active Directory <!-- deleted by customization editions](/documentation/articles/active-directory-editions) --><!-- keep by customization: begin --> editions](https://msdn.microsoft.com/zh-cn/library/azure/dn532272.aspx) <!-- keep by customization: end -->.

Windows Azure <!-- deleted by customization Active Directory --><!-- keep by customization: begin --> AD <!-- keep by customization: end --> Application Proxy lets you publish applications, such as SharePoint sites, Outlook Web Access <!-- deleted by customization, --> and IIS-based apps <!-- keep by customization: begin -->, <!-- keep by customization: end --> inside your private network and provides secure access to users outside your network. Employees can log into your apps from home <!-- keep by customization: begin -->, <!-- keep by customization: end --> on their own devices and authenticate through this cloud-based proxy <!-- deleted by customization. -->

<!-- deleted by customization
Application Proxy works by installing a slim Windows service called a Connector inside your network. The Connector maintains an outbound connection from within your network to the proxy service. When users access a published application, they proxy uses this connection to provide access to the application.

This article walks you through enabling Windows Azure AD Application Proxy for your cloud directory in Azure AD, installing the Application Proxy Connector on your private network, and registering the Connector with your Windows Azure AD tenant subscription.
-->
<!-- keep by customization: begin -->
This section walks you through enabling Windows Azure AD Application Proxy for your cloud directory in Azure AD, installing the Application Proxy Connector on your private network, registering the Connector with your Windows Azure AD tenant subscription.
<!-- keep by customization: end -->

##Application Proxy prerequisites
Before you can enable and use Application Proxy services, you need to have:

<!-- deleted by customization
- A Windows Azure AD [basic or premium subscription](/documentation/articles/active-directory-editions) and an Azure AD directory for which you are a global administrator.
-->
<!-- keep by customization: begin -->
- An Windows Azure administrator account. If you donâtâ have one, you can get one here.
<!-- keep by customization: end -->
- A server running Windows Server 2012 R2 or Windows 8.1 or higher on which you can install the Application Proxy Connector. The server must be able to send HTTPS requests to the Application Proxy services in the cloud, and it must have an HTTPS connection to the applications that you intend to publish.
- If a firewall is placed in the path, make sure the firewall is open to allow HTTPS (TCP) requests that originate from the Connector to the Application Proxy. The Connector uses these ports together with subdomains that are part of the high level domain: msappproxy.net. Make sure to open **all** the following ports to **outbound** traffic:

Port Number | Description
--- | ---
80 | To enable outbound HTTP traffic for security validation.
443 | To enable user authentication against Azure AD (required only for the Connector registration process)
10100 - 10120 | To enable LOB HTTP responses sent back to the proxy
9352, 5671 | To enable communication between the Connector toward the Azure service for incoming requests.
<!-- deleted by customization
9350 | Optional, to enable better performance for incoming requests
8080 | To enable the Connector bootstrap sequence and  Connector automatic update
-->
<!-- keep by customization: begin -->
9350 | Optional. To enable better performance for incoming requests.
8080 | To enable the Connector bootstrap sequence and to enable Connector automatic update
<!-- keep by customization: end -->
9090 | To enable Connector registration (required only for the Connector registration process)
9091 | To enable Connector trust certificate automatic renewal
If your firewall enforces traffic according to originating users, open these ports for traffic coming from Windows services running as a Network Service. Also, make sure to enable port 8080 for NT Authority\System.


##Step 1: Enable Application Proxy in Azure AD
1. Sign in as an administrator in the Azure Management Portal.
2. Go to Active Directory and select the directory in which you want to enable Application Proxy.
3. Click <!-- deleted by customization **Configure** --><!-- keep by customization: begin --> Configure <!-- keep by customization: end -->, scroll down to Application Proxy and toggle Enable Application Proxy Services for this Directory to <!-- deleted by customization **Enabled** --><!-- keep by customization: begin --> Enabled <!-- keep by customization: end -->.

<!-- deleted by customization
	![Enable Application Proxy](./media/active-directory-application-proxy-enable/app_proxy_enable.png) <p>
4. Click **Download now** at the bottom of the screen. This will take you to the download page. Read and accept the license terms and click **Download** to save the Windows Installer file (.exe) for the Application Proxy Connector.
-->
<!-- keep by customization: begin -->
	![Enable Application Proxy](http://i.imgur.com/87woFzq.png) <p>
4. Click Download now at the bottom of the screen. This will take you to the download page. Read and accept the license terms and click Download to save the Windows Installer file (.exe) for the Application Proxy Connector.
<!-- keep by customization: end -->

##Step 2: Install and register the Connector
<!-- deleted by customization
1. Run `AADApplicationProxyConnectorInstaller.exe` on the server you prepared (see Application Proxy prerequisites above).
-->
<!-- keep by customization: begin -->
1. Run AADApplicationProxyConnectorInstaller.exe on the server you prepared (see Application Proxy prerequisites).
<!-- keep by customization: end -->
2. Follow the instructions in the wizard to install.
<!-- deleted by customization
3. During installation you will be prompted to register the Connector with the Application Proxy of your Azure AD tenant.
<p>- Provide your Azure AD global administrator credentials.
<!-- deleted by customization <p>- --> Make sure the admin who registers the Connector is in the same directory where you enabled the Application Proxy service, for example if the tenant domain is contoso.com, the admin should be admin@contoso.com or any other alias on that domain. And that you are a global administrator of the Azure AD tenant. Your global administrator tenant may be different from your Windows Azure credentials.
<!-- deleted by customization <p>- --> If IE Enhanced Security Configuration is set to **On** on the server where you are installing the Azure AD Connector, the registration screen might be blocked. If this happens, follow the instructions in the error message to allow access. Make sure that Internet Explorer Enhanced Security is off.
<p>- If Connector registration does not succeed, see [Troubleshoot Application Proxy](/documentation/articles/active-directory-application-proxy-troubleshoot).
-->
<!-- keep by customization: begin -->
3. During installation you will be prompted to register the Connector with your active Application Proxy account.
<p>Provide your Azure AD global administrator credentials.
<!-- deleted by customization <p>- -->- Make sure the admin who registers the Connector is in the same directory where you enabled the Application Proxy service, for example if the tenant domain is contoso.com, the admin should be admin@contoso.com or any other alias on that domain. And that you are a global administrator of the Azure AD tenant. Your global administrator tenant may be different from your Windows Azure credentials.
<!-- deleted by customization <p>- -->- If IE Enhanced Security Configuration is set to On on the server where you are installing the Azure AD Connector, the registration screen might be blocked. If this happens, follow the instructions in the error message to allow access. Make sure that Internet Explorer Enhanced Security is off.
- If Connector registration does not succeed, see Troubleshoot Application Proxy.
<!-- keep by customization: end -->

4. When the installation completes, two new services are added to your server, as shown below. These are the Connector service, which enables connectivity, and an automated update service, which periodically checks for new versions of the Connector and updates the Connector as needed. Click Finish in the installation window to complete installation
<!-- deleted by customization
	![Application Proxy Connector Service!](./media/active-directory-application-proxy-enable/app_proxy_services.png) <p>
-->
<!-- keep by customization: begin -->
	![Application Proxy Connector Service](http://i.imgur.com/zsVJKOz.png) <p>
<!-- keep by customization: end -->
5. You are now ready to Publish applications with Application Proxy.

<!-- deleted by customization
For<!-- keep by customization: begin --> <p>For <!-- keep by customization: end --> high availability purposes, you must deploy at least one additional Connector. To deploy an additional Connector, repeat steps 2 and 3, above. Each Connector must be registered separately.

If you want to uninstall the Connector, uninstall both the Connector service and the Updater service and then make sure to restart your computer to fully remove the service.


## See also
There's a lot more you can do with Application Proxy:

- [Publish applications with Application Proxy](/documentation/articles/active-directory-application-proxy-publish)
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
If you want to uninstall the Connector, after uninstalling the Connector service and the Updater service, make sure to restart your computer to fully remove the service.
<!-- keep by customization: begin --> <p>For <!-- keep by customization: end --> high availability purposes, you must deploy at least one additional Connector. To deploy an additional Connector, repeat steps 2 and 3, above. Each Connector must be registered separately.


<!-- keep by customization: end -->

## Additional resources
* [Sign up for Azure as an organization](/documentation/articles/sign-up-organization)
* [Azure Identity](/documentation/articles/fundamentals-identity)
<!-- deleted by customization
* [Publish Applications with Application Proxy](/documentation/articles/active-directory-application-proxy-publish)
-->
