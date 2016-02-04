<properties
	pageTitle="How to silently install the Azure AD Application Proxy Connector | Windows Azure"
	description="Covers how to perform a silent installation of Azure AD Application Proxy Connector to provide secure remote access to your on-premises apps."
	services="active-directory"
	documentationCenter=""
	authors="kgremban"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="10/19/2015"
	wacn.date=""/>

# How to silently install the Azure AD Application Proxy Connector

You want to be able to send an installation script to multiple <!-- deleted by customization Windows --> servers or to Windows Servers that don't have user interface enabled. This topic explains how to create a Windows PowerShell script that enables unattended installation and installs and registers your Azure AD Application Proxy Connector.

## Enabling Access
Application Proxy works by installing a slim Windows Server service called the Connector inside your network. For the Application Proxy Connector to work it has to be registered with your Azure AD directory using a global administrator and password. Ordinarily this is entered during Connector installation in a pop up dialog box. Instead, you can use Windows PowerShell to create a credential object <!-- keep by customization: begin --> and use the token it creates <!-- keep by customization: end -->  to enter your registration information, or you can create your own token <!-- deleted by customization and --><!-- keep by customization: begin --> to <!-- keep by customization: end --> use <!-- deleted by customization it --> to enter your registration information.

## Step 1:  Install the Connector without registration


Install the Connector MSIs without registering the Connector as follows:


1. Open a command prompt.
2. Run the following command in which the /q means <!-- deleted by customization quiet --><!-- keep by customization: begin --> quite <!-- keep by customization: end --> installation - the installation will not prompt you to accept the End User License Agreement.

        AADApplicationProxyConnectorInstaller.exe REGISTERCONNECTOR="false" /q

## Step 2: Register the Connector with Azure Active Directory
This can be accomplished using either of the following methods:


- Register the Connector using a Windows PowerShell credential object
- Register the Connector using a token created offline

### Register the Connector using a Windows PowerShell credential object


1. Create the Windows PowerShell Credentials object, by running the following, where <!-- deleted by customization "username" --><!-- keep by customization: begin --> <username> <!-- keep by customization: end --> and <!-- deleted by customization "password" --><!-- keep by customization: begin --> <password> <!-- keep by customization: end --> should be replaced with the username and password for your directory:

        $User = "<username>"
        $PlainPassword = '<password>'
        $SecurePassword = $PlainPassword | ConvertTo-SecureString -AsPlainText -Force
<!-- deleted by customization
        $cred = New-Object âTypeName System.Management.Automation.PSCredential âArgumentList $User, $SecurePassword

2. Go to **C:\Program Files\Microsoft AAD App Proxy Connector** and run the script using the PowerShell credentials object you created: where $cred is the name of the PowerShell credentials object you created:
-->
<!-- keep by customization: begin -->
        $cred = New-Object –TypeName System.Management.Automation.PSCredential –ArgumentList $User, $SecurePassword 
    
2. 	Go to **C:\Program Files\Microsoft AAD App Proxy Connector** and run the file **Register Connector.PS1** in Windows PowerShell.
3. Use the PowerShell credentials object you created to input your Connector registration username and password in your script, by running the following, where $cred is the name of the PowerShell credentials object you created:
<!-- keep by customization: end -->

        RegisterConnector.ps1 -modulePath "C:\Program Files\Microsoft AAD App Proxy Connector\Modules\" -moduleName "AppProxyPSModule" -Authenticationmode Credentials -Usercredentials $cred


### Register the Connector using a token created offline

<!-- deleted by customization
1. Create an offline token using the AuthenticationContext class using the values in the code snippet:


        using System;
        using System.Diagnostics;
        using Microsoft.IdentityModel.Clients.ActiveDirectory;

        class Program
        {
        #region constants
        /// <summary>
        /// The AAD authentication endpoint uri
        /// </summary>
        static readonly Uri AadAuthenticationEndpoint = new Uri("https://login.chinacloudapi.cn/common/oauth2/token?api-version=1.0");

-->
<!-- keep by customization: begin -->
1. Create an offline token using the AuthenticationContext class, for example:

        #region constants /// /// The AAD authentication endpoint uri /// static readonly Uri AadAuthenticationEndpoint = new Uri("https://login.chinacloudapi.cn/common/oauth2/token?api-version=1.0");
<!-- keep by customization: end -->
        /// <summary>
        /// The application ID of the connector in AAD
        /// </summary>
        static readonly string ConnectorAppId = "55747057-9b5d-4bd4-b387-abf52a8bd489";

        /// <summary>
        /// The reply address of the connector application in AAD
        /// </summary>
        static readonly Uri ConnectorRedirectAddress = new Uri("urn:ietf:wg:oauth:2.0:oob");
<!-- deleted by customization

        /// <summary>
        /// The AppIdUri of the registration service in AAD
        /// </summary>
        static readonly Uri RegistrationServiceAppIdUri = new Uri("https://proxy.cloudwebappproxy.net/registerapp");

        #endregion

        #region private members
        private string token;
        private string tenantID;
        #endregion

        public void GetAuthenticationToken()
-->
<!-- keep by customization: begin -->
		
		/// <summary>
		/// The AppIdUri of the registration service in AAD
		/// </summary>
		static readonly Uri RegistrationServiceAppIdUri = new Uri("https://proxy.cloudwebappproxy.net/registerapp");

		#endregion


		public static void GetAuthenticationToken()
<!-- keep by customization: end -->
        {
            AuthenticationContext authContext = new AuthenticationContext(AadAuthenticationEndpoint.AbsoluteUri);
<!-- deleted by customization

            AuthenticationResult authResult = authContext.AcquireToken(RegistrationServiceAppIdUri.AbsoluteUri,
-->
<!-- keep by customization: begin -->
	    AuthenticationResult authResult = authContext.AcquireToken(RegistrationServiceAppIdUri.AbsoluteUri,
<!-- keep by customization: end -->
                ConnectorAppId,
                ConnectorRedirectAddress,
                PromptBehavior.Always);

<!-- deleted by customization
            if (authResult == null || string.IsNullOrEmpty(authResult.AccessToken) || string.IsNullOrEmpty(authResult.TenantId))
            {
                Trace.TraceError("Authentication result, token or tenant id returned are null");
                throw new InvalidOperationException("Authentication result, token or tenant id returned are null");
            }

            token = authResult.AccessToken;
            tenantID = authResult.TenantId;
        }




-->
<!-- keep by customization: begin -->

	        if (authResult == null || string.IsNullOrEmpty(authResult.AccessToken) || string.IsNullOrEmpty(authResult.TenantId))
    	    {
          Trace.TraceError("Authentication result, token or tenant id returned are null");
          throw new InvalidOperationException("Authentication result, token or tenant id returned are null");
    	}

    	string token = authResult.AccessToken;
    	string tenantID = authResult.TenantId;
		}
<!-- keep by customization: end -->

2. Once you have the token create a SecureString using the token: <br>
`$SecureToken = $Token | ConvertTo-SecureString -AsPlainText -Force`
3. Run the following Windows PowerShell command, where SecureToken is the name of the token you created above <!-- deleted by customization and tenantID is your tenant's GUID -->: <br>
`RegisterConnector.ps1 -modulePath "C:\Program Files\Microsoft AAD App Proxy Connector\Modules\" -moduleName "AppProxyPSModule" -Authenticationmode Token -Token $SecureToken -TenantId <tenant GUID>`



## What's next?
There's a lot more you can do with Application Proxy:


- [Publish applications using your own domain name](/documentation/articles/active-directory-application-proxy-custom-domains)
- [Enable single-sign on](/documentation/articles/active-directory-application-proxy-sso-using-kcd)
- [Working with claims aware applications](/documentation/articles/active-directory-application-proxy-claims-aware-apps)
- [Enable conditional access](/documentation/articles/active-directory-application-proxy-conditional-access)


### Learn more about Application Proxy
- [Take a look here at our online help](/documentation/articles/active-directory-application-proxy-enable)
- [Check out the Application Proxy blog](http://blogs.technet.com/b/applicationproxyblog/)
- [Watch our videos on Channel 9!](http://channel9.msdn.com/events/Ignite/2015/BRK3864)

## Additional resources
* [Sign up for Azure as an organization](/documentation/articles/sign-up-organization)
* [Azure Identity](/documentation/articles/fundamentals-identity)
