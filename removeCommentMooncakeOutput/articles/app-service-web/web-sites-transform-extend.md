<properties
	pageTitle="Azure Websites advanced config and extensions"
	description="Use XML Document Transformation(XDT) declarations to transform the ApplicationHost.config file in your Azure Websites and to add private extensions to enable custom administration actions."
	authors="cephalin"
	writer="cephalin"
	editor="mollybos"
	manager="wpickett"
	services="app-service"
	documentationCenter=""/>

<tags
	ms.service="app-service"
	ms.date="12/09/2015"
	wacn.date=""/>

# Azure Websites advanced config and extensions

By using [XML Document Transformation](http://msdn.microsoft.com/zh-cn/library/dd465326.aspx) (XDT) declarations, you can transform the [ApplicationHost.config](http://www.iis.net/learn/get-started/planning-your-iis-architecture/introduction-to-applicationhostconfig) file in your web site in Azure Websites. You can also use XDT declarations to add private extensions to enable custom web site administration actions. This article includes a sample PHP Manager web site extension that enables management of PHP settings through a web interface.

##<a id="transform"></a>Advanced configuration through ApplicationHost.config
The Azure Websites platform provides flexibility and control for web site configuration. Although the standard IIS ApplicationHost.config configuration file is not available for direct editing in Azure Websites, the platform supports a declarative ApplicationHost.config transform model based on XML Document Transformation (XDT).

To leverage this transform functionality, you create an ApplicationHost.xdt file with XDT content and place under the site root (d:\home\site) in the [Kudu Console](https://github.com/projectkudu/kudu/wiki/Kudu-console). You may need to restart the web site for changes to take effect.

The following applicationHost.xdt sample shows how to add a new custom environment variable to a web site that uses PHP 5.4.

	<?xml version="1.0"?>
	<configuration xmlns:xdt="http://schemas.microsoft.com/XML-Document-Transform">
  		<system.webServer>
    			<fastCgi>
      				<application>
         				<environmentVariables>
            					<environmentVariable name="CONFIGTEST" value="TEST" xdt:Transform="Insert" xdt:Locator="XPath(/configuration/system.webServer/fastCgi/application[contains(@fullPath,'5.4')]/environmentVariables)" />
         				</environmentVariables>
      				</application>
    			</fastCgi>
  		</system.webServer>
	</configuration>


A log file with transform status and details is available from the FTP root under LogFiles\Transform.

For additional samples, see [https://github.com/projectkudu/kudu/wiki/Xdt-transform-samples](https://github.com/projectkudu/kudu/wiki/Xdt-transform-samples).

**Note**<br />
Elements from the list of modules under `system.webServer` cannot be removed or reordered, but additions to the list are possible.


##<a id="extend"></a> Extend your web site

###<a id="overview"></a> Overview of private web site extensions

Azure Websites supports web site extensions as an extensibility point for administrative actions. In fact, some Azure Websites platform features are implemented as pre-installed extensions. While the pre-installed platform extensions cannot be modified, you can create and configure private extensions for your own web site. This functionality also relies on XDT declarations. The key steps for creating a private web site extension are the following:

1. web site extension **content**: create any web site supported by Azure Websites
2. web site extension **declaration**: create an ApplicationHost.xdt file
3. web site extension **deployment**: place content in the SiteExtensions folder under `root`

Internal links for the web site should point to a path relative to the application path specified in the ApplicationHost.xdt file. Any change to the ApplicationHost.xdt file requires a web site recycle.

**Note**: Additional information for these key elements is available at [https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions).

A detailed example is included to illustrate the steps for creating and enabling a private web site extension. The source code for the PHP Manager example that follows can be downloaded from [https://github.com/projectkudu/PHPManager](https://github.com/projectkudu/PHPManager).

###<a id="SiteSample"></a> web site extension example: PHP Manager

PHP Manager is a web site extension that allows web site administrators to easily view and configure their PHP settings using a web interface instead of having to modify PHP .ini files directly. Common configuration files for PHP include the php.ini file located under Program Files and the .user.ini file located in the root folder of your web site. Since the php.ini file is not directly editable on the Azure Websites platform, the PHP Manager extension uses the .user.ini file to apply setting changes.

####<a id="PHPwebapp"></a> The PHP Manager web site

The following is the home page of the PHP Manager deployment:

![TransformSitePHPUI][TransformSitePHPUI]

As you can see, a web site extension is just like a regular web site, but with an additional ApplicationHost.xdt file placed in the root folder of the web site (more details about the ApplicationHost.xdt file are available in the next section of this article).

The PHP Manager extension was created using the Visual Studio ASP.NET MVC 4 web site template. The following view from Solution Explorer shows the structure of the PHP Manager extension.

![TransformSiteSolEx][TransformSiteSolEx]

The only special logic needed for file I/O is to indicate where the wwwroot directory of the web site is located. As the following code example shows, the environment variable "HOME" indicates the web site's root path, and the wwwroot path can be constructed by appending "site\wwwroot":

	/// <summary>
	/// Gives the location of the .user.ini file, even if one doesn't exist yet
	/// </summary>
	private static string GetUserSettingsFilePath()
	{
    		var rootPath = Environment.GetEnvironmentVariable("HOME"); // For use on Azure Websites
    		if (rootPath == null)
    		{
        		rootPath = System.IO.Path.GetTempPath(); // For testing purposes
    		};
    		var userSettingsFile = Path.Combine(rootPath, @"site\wwwroot\.user.ini");
    		return userSettingsFile;
	}


After you have the directory path, you can use regular file I/O operations to read and write to files.

One point of caution with web site extensions regards the handling of internal links.  If you have any links in your HTML files that give absolute paths to internal links on your web site, you must ensure those links are prepended with your extension name as your root. This is needed because the root for your extension is now "/`[your-extension-name]`/" rather than being just "/", so any internal links must be updated accordingly. For example, suppose your code includes a link to the following:

`"<a href="/Home/Settings">PHP Settings</a>"`

When the link is part of a web site extension, the link must be in the following form:

`"<a href="/[your-site-name]/Home/Settings">Settings</a>"`

You can work around this requirement by either using only relative paths within your web site, or in the case of ASP.NET applications, by using the `@Html.ActionLink` method which creates the appropriate links for you.

####<a id="XDT"></a> The applicationHost.xdt file

The code for your web site extension goes under %HOME%\SiteExtensions\[your-extension-name]. We'll call this the extension root.  

To register your web site extension with the applicationHost.config file, you need to place a file called ApplicationHost.xdt in the extension root. The content of the ApplicationHost.xdt file should be as follows:

	<?xml version="1.0"?>
	<configuration xmlns:xdt="http://schemas.microsoft.com/XML-Document-Transform">
  		<system.applicationHost>
    			<sites>
      				<site name="%XDT_SCMSITENAME%" xdt:Locator="Match(name)">
						<!-- NOTE: Add your extension name in the application paths below -->
        				<application path="/[your-extension-name]" xdt:Locator="Match(path)" xdt:Transform="Remove" />
        				<application path="/[your-extension-name]" applicationPool="%XDT_APPPOOLNAME%" xdt:Transform="Insert">
          					<virtualDirectory path="/" physicalPath="%XDT_EXTENSIONPATH%" />
        				</application>
      				</site>
    			</sites>
  		</system.applicationHost>
	</configuration>

The name you select as your extension name should have the same name as your extension root folder.

This has the effect of adding a new application path to the `system.applicationHost` sites list under the SCM site. The SCM site is a site administration end point with specific access credentials. It has the URL `https://[your-site-name].scm.chinacloudsites.cn`.  

	<system.applicationHost>
  		...
  		<site name="~1[your-website]" id="1716402716">
      			<bindings>
        			<binding protocol="http" bindingInformation="*:80: [your-website].scm.chinacloudsites.cn" />
        			<binding protocol="https" bindingInformation="*:443: [your-website].scm.chinacloudsites.cn" />
      			</bindings>
      			<traceFailedRequestsLogging enabled="false" directory="C:\DWASFiles\Sites\[your-website]\VirtualDirectory0\LogFiles" />
      			<detailedErrorLogging enabled="false" directory="C:\DWASFiles\Sites\[your-website]\VirtualDirectory0\LogFiles\DetailedErrors" />
      			<logFile logSiteId="false" />
      			<application path="/" applicationPool="[your-website]">
        			<virtualDirectory path="/" physicalPath="D:\Program Files (x86)\SiteExtensions\Kudu\1.24.20926.5" />
      			</application>
				<!-- Note the custom changes that go here -->
      			<application path="/[your-extension-name]" applicationPool="[your-website]">
        			<virtualDirectory path="/" physicalPath="C:\DWASFiles\Sites\[your-website]\VirtualDirectory0\SiteExtensions\[your-extension-name]" />
      			</application>
    		</site>
  	</sites>
	  ...
	</system.applicationHost>

###<a id="deploy"></a> web site extension deployment

To install your web site extension, you can use FTP to copy all the files of your web site to the `\SiteExtensions\[your-extension-name]` folder of the web site on which you want to install the extension.  Be sure to copy the ApplicationHost.xdt file to this location as well. Restart your web site to enable the extension.

You should be able to see your web site extension at:

`https://[your-site-name].scm.chinacloudsites.cn/[your-extension-name]`

Note that the URL looks just like the URL for your web site, except that it uses HTTPS and contains ".scm".

It is possible to disable all private (not pre-installed) extensions for your web site during development and investigations by adding an app settings with the key `WEBSITE_PRIVATE_EXTENSIONS` and a value of `0`.

<!-- IMAGES -->
[TransformSitePHPUI]: ./media/web-sites-transform-extend/TransformSitePHPUI.png
[TransformSiteSolEx]: ./media/web-sites-transform-extend/TransformSiteSolEx.png
 
