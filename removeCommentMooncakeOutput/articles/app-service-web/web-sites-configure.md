<properties 
	pageTitle="Configure web sites in Azure Websites" 
	description="How to configure a web site in Azure Websitess" 
	services="app-service" 
	documentationCenter="" 
	authors="erikre" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="12/08/2015"
	wacn.date=""/>


# Configure web sites in Azure Websites #
In the Azure Management Portal, you can change the configuration options for websites and link to other Azure resources, such as a database.

## Table of Contents ##
- [How to: Change configuration options for a web site](#howtochangeconfig)
- [How to: Configure a web site to use a SQL database](#howtoconfigSQL)
- [How to: Configure a web site to use a MySQL database](#howtoconfigMySQL)
- [How to: Configure a custom domain name](#howtodomain)
- [How to: Configure a web site to use SSL](#howtoconfigSSL)
- [Next steps](#next)


##<a name="howtochangeconfig"></a>How to: Change configuration options for a website

<!-- HOW TO: CHANGE CONFIGURATION OPTIONS FOR A WEBSITE -->

To set configuration options for a website:

1. In the [Management Portal](https://manage.windowsazure.cn/), open the Website's management pages.
1. Click the <strong>Configure</strong> tab.

The **Configure** tab has the following sections:
### General settings

**Framework versions**. Set these options if your app uses any these frameworks: 

- **.NET Framework**: Set the .NET framework version. 
- **PHP**: Set the PHP version, or **OFF **to disable PHP. 
- **Java**: Select the Java version or **OFF** to disable Java. Use the **Web Container** option to choose between Tomcat and Jetty versions.
- **Python**: Select the Python version, or **OFF** to disable Python.

For technical reasons, enabling Java for your app disables the .NET, PHP, and Python options.

<a name="platform"></a>
**Platform**. Selects whether your web site runs in a 32-bit or 64-bit environment. The 64-bit environment requires Basic or Standard mode. Free and Shared modes always run in a 32-bit environment.

**Web Sockets**. Set **ON** to enable the WebSocket protocol; for example, if your web site uses [ASP.NET SignalR](http://www.asp.net/signalr) or [socket.io](/documentation/articles/web-sites-nodejs-chat-app-socketio).

<a name="alwayson"></a>
**Always On**. By default, web sites are unloaded if they are idle for some period of time. This lets the system conserve resources. In Basic or Standard mode, you can enable **Always On** to keep the app loaded all the time. If your app runs continuous web jobs, you should enable **Always On**, or the web jobs may not run reliably.

**Managed Pipeline Version**. Sets the IIS [pipeline mode](http://www.iis.net/learn/get-started/introduction-to-iis/introduction-to-iis-architecture#Application). Leave this set to Integrated (the default) unless you have a legacy app that requires an older version of IIS.


### Debugging

**Remote Debugging**. Enables remote debugging. When enabled, you can use the remote debugger in Visual Studio to connect directly to your web site. Remote debugging will remain enabled for 48 hours. 


### App settings

This section contains name/value pairs that you web site will load on start up. 

- For .NET apps, these settings are injected into your .NET configuration `AppSettings` at runtime, overriding existing settings. 

- PHP, Python, Java and Node applications can access these settings as environment variables at runtime. For each app setting, two environment variables are created; one with the name specified by the app setting entry, and another with a prefix of APPSETTING_. Both contain the same value.

### Connection strings

Connection strings for linked resources. 

For .NET apps, these connection strings are be injected into your .NET configuration `connectionStrings` settings at runtime, overriding existing entries where the key equals the linked database name. 

For PHP, Python, Java and Node applications, these settings will be available as environment variables at runtime, prefixed with the connection type. The environment variable prefixes are as follows: 

- SQL Server: SQLCONNSTR_
- MySQL: MYSQLCONNSTR_
- SQL Database: SQLAZURECONNSTR_
- Custom: CUSTOMCONNSTR_

For example, if a MySql connection string were named `connectionstring1`, it would be accessed through the environment variable `MYSQLCONNSTR_connectionString1`.

### Default documents

The default document is the web page that is displayed at the root URL for a website.  The first matching file in the list is used. 

web sites might use modules that route based on URL, rather than serving static content, in which case there is no default document as such.    

### Handler mappings

Use this area to add custom script processors to handle requests for specific file extensions. 

- **Extension**. The file extension to be handled, such as *.php or handler.fcgi. 
- **Script Processor Path**. The absolute path of the script processor. Requests to files that match the file extension will be processed by the script processor. Use the path `D:\home\site\wwwroot` to refer to your app's root directory.
- **Additional Arguments**. Optional command-line arguments for the script processor 


### Virtual applications and directories 
 
To configure virtual applications and directories, specify each virtual directory and its corresponding physical path relative to the website root. Optionally, you can select the **Application** checkbox to mark a virtual directory as an application.

## Other configuration tasks

### SSL 

In Basic or Standard mode, you can upload SSL certificates for a custom domain. For more information, see [Enable HTTPS for a web site](/documentation/articles/web-sites-configure-ssl-certificate). 

To view your uploaded certificates, click **Configure** > **SSL Bindings**.

### Domain names

Add custom domain names for your web site. For more information, see [Configure a custom domain name for a web site in Azure Websites](/documentation/articles/web-sites-custom-domain-name).

To view your domain names, click **Configure** > **Domain Names**.

### Deployments

- Set up continuous deployment. See [Using Git to deploy web sites in Azure Websites](/documentation/articles/web-sites-publish-source-control)
- Deployment slots. See [Deploy to Staging Environments for web sites in Azure Websites](/documentation/articles/web-sites-staged-publishing)

To view your deployment slots, click **Configure** > **Deployment**.


### Monitoring

In Basic or Standard mode, you can  test the availability of HTTP or HTTPS endpoints, from up to three geo-distributed locations. A monitoring test fails if the HTTP response code is an error (4xx or 5xx) or the response takes more than 30 seconds. An endpoint is considered available if the monitoring tests succeed from all the specified locations. 

For more information, see [How to: Monitor web endpoint status](/documentation/articles/web-sites-monitor/).

## Next steps

- [Configure a custom domain name](/documentation/articles/web-sites-custom-domain-name)
- [Enable HTTPS](/documentation/articles/web-sites-configure-ssl-certificate)
- [Scale a web site in Azure Websites](/documentation/articles/web-sites-scale)
- [Monitoring basics for web sites in Azure Websites](/documentation/articles/web-sites-monitor)
 
