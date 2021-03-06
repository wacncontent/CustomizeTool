deletion:

deleted:

		- `webSpaceName` should be one of the values defined in the [WebSpaceNames][] class.
		- `appServicePlanName` should be specified as shown above.

reason: ()

deleted:

		[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]
		
		[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

reason: ()

replacement:

deleted:

		To obtain FTP connection information from the web app's blade in the [Azure Management Portal][]:
		
		1. Under **Essentials**, find and copy the **FTP hostname**. This is a URI similar to `ftp://waws-prod-bay-NNN.ftp.azurewebsites.chinacloudapi.cn`.
		
		2. Under **Essentials**, find and copy **FTP/Deployment username**. This will have the form *webappname\deployment-username*; for example `WebDemoWebApp\deployer77`.
		
		To obtain FTP connection information from the  publish profile:
		
		1. In the web app's blade, click **Get publish profile**. This will download a .publishsettings file to your local drive.

replaced by:

		To obtain FTP connection information from the website's **Dashboard** page:
		
		1. Under **Quick Glance**, find and copy the **FTP host name**. This is a URI similar to `ftp://cnws-prod-sha-001.ftp.chinacloudsites.chinacloudapi.cn`.
		
		2. Under **Quick Glance**, find and copy **Deployment / FTP user**. This will have the form *WebsiteName\DeploymentUsername*; for example `WebDemoWebsite\deployer77`.
		
		To obtain FTP connection information from the website's publish profile:
		
		1. In the website's **Dashboard**, under **Quick Glance**, click **Download the publish profile**. This will download a .publishsettings file to your local drive.

reason: ()

deleted:

		http://msdn.microsoft.com/zh-cn/library/azure/gg551722.aspx

replaced by:

		/documentation/articles/cloud-services-certs-create/

reason: ()

deleted:

		[WebSiteManagementClient]: http://dl.windowsazure.com/javadoc/com/microsoft/windowsazure/management/websites/WebSiteManagementClient.html
		[WebSpaceNames]: http://dl.windowsazure.com/javadoc/com/microsoft/windowsazure/management/websites/models/WebSpaceNames.html

replaced by:

		[WebSiteManagementClient]: http://azure.github.io/azure-sdk-for-java/com/microsoft/windowsazure/management/websites/WebSiteManagementClient.html
		[WebSpaceNames]: http://azure.github.io/azure-sdk-for-java/com/microsoft/windowsazure/management/websites/models/WebSpaceNames.html

reason: ()

