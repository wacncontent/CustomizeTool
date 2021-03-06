<properties 
	pageTitle="Configure web apps in Azure" 
	description="How to configure a web app in Azure" 
	services="app-service\web" 
	documentationCenter="" 
	authors="rmcmurray" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="06/02/2016"
	wacn.date=""/>


# Configure web apps in Azure #

This topic explains how to configure a web app using the [Azure Classic Management Portal](https://manage.windowsazure.cn/).

##<a name="howtochangeconfig"></a>How to: Change configuration options for a website

<!-- HOW TO: CHANGE CONFIGURATION OPTIONS FOR A WEBSITE -->

To set configuration options for a website:

1. In the [Classic Management Portal](https://manage.windowsazure.cn/), open the Website's management pages.
1. Click the **Configure** tab.

The **Configure** tab has the following sections:

### General settings

**Framework versions**. Set these options if your app uses any these frameworks: 

- **.NET Framework Version**: Set the .NET framework version.
- **PHP Version**: Set the PHP version, or **OFF** to disable PHP.
- **Java Version**: Select the displayed version to enable Java, or **OFF** to disable Java. 
- **Python Version**: Select the Python version, or **OFF** to disable Python.

For technical reasons, enabling Java for your app disables the .NET, PHP, and Python options.

<a name="platform"></a>
**Platform**. Selects whether your web app runs in a 32-bit or 64-bit environment. The 64-bit environment requires Basic or Standard mode. Free and Shared modes always run in a 32-bit environment.

**Web Sockets**. Set **ON** to enable the WebSocket protocol; for example, if your web app uses [ASP.NET SignalR] or [socket.io].

<a name="alwayson"></a>
**Always On**. By default, web apps are unloaded if they are idle for some period of time. This lets the system conserve resources. In Basic or Standard mode, you can enable **Always On** to keep the app loaded all the time. If your app runs continuous web jobs, you should enable **Always On**, or the web jobs may not run reliably.

**Edit in Visual Studio Online**. Enables live code editing with Visual Studio Online. If enabled, the Dashboard tab will show a link called **Edit in Visual Studio Online**, under the **Quick Glance** section. Click this link to edit your website directly online. If you need to authenticate, you can use your basic deployment credentials.

>[AZURE.NOTE]
> This feature is on preview.

Note: If you enable deployment from source control, it is possible for a deployment to overwrite changes you make in the Visual Studio Online editor. 

### Certificates

In Basic or Standard mode, you can upload SSL certificates for a custom domain. For more information,, see [Enable HTTPS for an Azure website](/documentation/articles/web-sites-configure-ssl-certificate/). 

Your uploaded certificates are listed here. After you upload a certificate, you can assign it to any website in your subscription and region. Wildcard certificates can be used for any site within the domain for which it is valid. A certificate can be deleted only if there are no active bindings for that certificate.

### Domain names

View or add additional domain names for the  Website. For more information, see [Configuring a custom domain name for an Azure Website](/documentation/articles/web-sites-custom-domain-name/).

### SSL Bindings

If you uploaded SSL certificates, you can bind them to custom domain names. For more information,, see [Enable HTTPS for an Azure Website](/documentation/articles/web-sites-configure-ssl-certificate/)

### Deployments

This section appears only if you have enabled deployment from source control. Use these settings to configure deployments.

- **Git URL**. If you have created a Git repository for your Azure website, this is the URL where you push your content.
- **Deployment Trigger URL**. This URL can be set on a GitHub, CodePlex, Bitbucket, or other repository to trigger the deployment when a commit is pushed to the repository.
- **Branch to Deploy**. Specifies the branch that will be deployed when you push content.

To set up deployment from source control, view the **Dashboard** tab, and click **Set up deployment from source control**. 

### Application diagnostics

Options for writing diagnostic logs from a web application that supports logging: 

- <strong>File System</strong>. Writes logs to the website's file system. File system logging lasts for a period of 12 hours. You can access the logs from the FTP share for the website.
- <strong>Table Storage</strong>. Writes logs to Azure table storage. There is no time limit, and logging stays enabled until you disable it. 
- <strong>Blob Storage</strong>. Writes logs to Azure blob storage. There is no time limit, and logging stays enabled until you disable it.

<strong>Logging Level</strong>. When logging is enabled, this option specifies the amount of information that will be recorded (Error, Warning, Information, or Verbose).

**Manage table storage**. When table storage is enabled, click this button to set the storage account and table name.

**Manage blob storage.** When blob storage is enabled, click this button to set the storage account and blob storage name.

### Site diagnostics

Options for gathering diagnostic information for your website.

<strong>Web Server Logging</strong>. Enables web server logging. Logs are saved in the W3C extended log file format. You can save the logs to Azure Storage or to the website's file System.
 
- If you choose <strong>File System</strong>, logs are saved to the FTP site listed under "FTP Diagnostic Logs" on the Dashboard page.
- If you choose **File System**, use the <strong>Quota</strong> box to set the maximum amount of disk space for the log files. The minimum is 25MB and the maximum is 100MB. The default is 35MB. When the quota is reached, the oldest files are successively overwritten by the newest ones. If you need to retain more history 100MB, use Azure Storage, which has a much greater storage capacity.
- Optionally, click <strong>Set Retention</strong> to automatically delete files after a period of time. By default, logs are never deleted.   

<strong>Detailed Error Messages</strong>. If enabled, detailed error messages are saved as .htm files. To view the files, go to the FTP site listed under "FTP Diagnostic Logs" on the Dashboard page. The files are saved under /LogFiles/DetailedErrors in the FTP site.

<strong>Failed Request Tracing</strong>. If enabled, failed requests are logged to XML files. To view the files, go to the FTP site listed under "FTP Diagnostic Logs" on the Dashboard page. The files are saved under /LogFiles/W3SVC*xxx*, where xxx is a unique identifier. This folder contains an XSL file and one or more XML files. Make sure to download the XSL file, because it provides functionality for formatting and filtering the contents of the XML files.

<strong>Remote Debugging</strong> Enables remote debugging. When enabled, you can use the remote debugger in Visual Studio to connect directly to your Azure website. Remote debugging will remain enabled for 48 hours.

**Note**: Remote debugging will not work with a site name or user name that is longer than 20 characters. 

### Developer analytics

Choose <strong>Add-on</strong> to select an analytics add-on from a list (Currently, Azure China does not support Azure Marketplace). Choose <strong>Custom</strong> to select an analytics provider such as New Relic from a list. If you use a custom provider, you must enter the license key in the<strong> Provider Key</strong> box. 

### App settings

This section contains name/value pairs that you web app will load on start up. 

- For .NET apps, these settings are injected into your .NET configuration `AppSettings` at runtime, overriding existing settings. 

- PHP, Python, Java and Node applications can access these settings as environment variables at runtime. For each app setting, two environment variables are created; one with the name specified by the app setting entry, and another with a prefix of APPSETTING_. Both contain the same value.

### Connection strings

Connection strings for linked resources. 

For .NET apps, these connection strings are injected into your .NET configuration `connectionStrings` settings at runtime, overriding existing entries where the key equals the linked database name. 

For PHP, Python, Java and Node applications, these settings will be available as environment variables at runtime, prefixed with the connection type. The environment variable prefixes are as follows: 

- SQL Server: `SQLCONNSTR_`
- MySQL: `MYSQLCONNSTR_`
- SQL Database: `SQLAZURECONNSTR_`
- Custom: `CUSTOMCONNSTR_`

For example, if a MySql connection string were named `connectionstring1`, it would be accessed through the environment variable `MYSQLCONNSTR_connectionString1`.

### Default documents

The default document is the web page that is displayed at the root URL for a website.  The first matching file in the list is used. 

Web apps might use modules that route based on URL, rather than serving static content, in which case there is no default document as such.    

### Handler mappings

Use this area to add custom script processors to handle requests for specific file extensions. 

- **Extension**. The file extension to be handled, such as *.php or handler.fcgi. 
- **Script Processor Path**. The absolute path of the script processor. Requests to files that match the file extension will be processed by the script processor. Use the path `D:\home\site\wwwroot` to refer to your app's root directory.
- **Additional Arguments**. Optional command-line arguments for the script processor 


### Virtual applications and directories 
 
To configure virtual applications and directories, specify each virtual directory and its corresponding physical path relative to the website root. Optionally, you can select the **Application** checkbox to mark a virtual directory as an application.

## Next steps

- [Configure a custom domain name in Azure Web App]
- [Enable HTTPS for an app in Azure Web App]
- [Scale a web app in Azure]
- [Monitoring basics for Web Apps in Azure]

<!-- URL List -->

[ASP.NET SignalR]: http://www.asp.net/signalr
[Azure Portal]: https://portal.azure.cn/
[Configure a custom domain name in Azure Web App]: /documentation/articles/web-sites-custom-domain-name/
[Deploy to Staging Environments for Web Apps in Azure]: /documentation/articles/web-sites-staged-publishing/
[Enable HTTPS for an app in Azure Web App]: /documentation/articles/web-sites-configure-ssl-certificate/
[How to: Monitor web endpoint status]: http://go.microsoft.com/fwLink/?LinkID=279906
[Monitoring basics for Web Apps in Azure]: /documentation/articles/web-sites-monitor/
[pipeline mode]: http://www.iis.net/learn/get-started/introduction-to-iis/introduction-to-iis-architecture#Application
[Scale a web app in Azure]: /documentation/articles/web-sites-scale/
[socket.io]: /documentation/articles/web-sites-nodejs-chat-app-socketio/
[Try Azure Web App]: https://tryappservice.azure.com/
[Using Git to deploy Web Apps in Azure]: /documentation/articles/web-sites-publish-source-control/

<!-- IMG List -->

[configure01]: ./media/web-sites-configure/configure01.png
[configure02]: ./media/web-sites-configure/configure02.png
[configure03]: ./media/web-sites-configure/configure03.png
