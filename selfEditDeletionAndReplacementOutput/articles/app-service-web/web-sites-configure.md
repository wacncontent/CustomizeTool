deletion:

deleted:

		**Auto Swap**. If you enable Auto Swap for a deployment slot, Azure Websites will automatically swap the web app into production when you push an update to that slot. For more information, see [Deploy to staging slots for web apps in Azure Websites](/documentation/articles/web-sites-staged-publishing).

reason: (auto swap)

deleted:

		## Enabling diagnostic logs
		
		To enable diagnostic logs:
		
		1. In the blade for your web app, click **All settings**.
		2. Click **Diagnostic logs**. 
		
		Options for writing diagnostic logs from a web application that supports logging: 
		
		- **Application Logging**. Writes application logs to the file system. Logging lasts for a period of 12 hours. 
		
		**Level**. When application logging is enabled, this option specifies the amount of information that will be recorded (Error, Warning, Information, or Verbose).
		
		**Web server logging**. Logs are saved in the W3C extended log file format. 
		
		**Detailed error messages**. Saves detailed error messages .htm files. The files are saved under /LogFiles/DetailedErrors. 
		
		**Failed request tracing**. Logs failed requests to XML files. The files are saved under /LogFiles/W3SVC*xxx*, where xxx is a unique identifier. This folder contains an XSL file and one or more XML files. Make sure to download the XSL file, because it provides functionality for formatting and filtering the contents of the XML files.
		
		To view the log files, you must create FTP credentials, as follows:
		
		1. In the blade for your web app, click **All settings**.
		2. Click **Deployment credentials**.
		3. Enter a user name and password.
		4. Click **Save**.
		
		![](./media/web-sites-configure/configure03.png)
		
		
		The full FTP user name is “app\username” where *app* is the name of your web app. The username is listed in the web app blade, under **Essentials**.  
		
		![](./media/web-sites-configure/configure02.png)

reason: (the new Ibiza portal)

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

reason: (“Try it now”)

deleted:

		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: (terminology: Azure App Service Web, the new Ibiza portal)

replacement:

deleted:

		This topic explains how to configure a web app using the [Azure Management Portal](https://manage.windowsazure.cn/).
		
		[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 
		
		## Application settings
		
		1. In the [Azure Management Portal](https://manage.windowsazure.cn), open the blade for the web app.
		2. Click **Configure**.
		3. Click **Application Settings**.
		
		![](./media/web-sites-configure/configure01.png)
		
		The **Application settings** blade has settings grouped under several categories.

replaced by:

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

reason: (the new Ibiza portal)

deleted:

		To view your uploaded certificates, click **Configure** > **Custom domains and SSL**.

replaced by:

		To view your uploaded certificates, click **Configure** > **SSL Bindings**.

reason: (the new Ibiza portal)

deleted:

		To view your domain names, click **Configure** > **Custom domains and SSL**.

replaced by:

		To view your domain names, click **Configure** > **Domain Names**.

reason: (the new Ibiza portal)

deleted:

		To view your deployment slots, click **Configure** > **Deployment slots**.

replaced by:

		To view your deployment slots, click **Configure** > **Deployment**.

reason: (the new Ibiza portal)

