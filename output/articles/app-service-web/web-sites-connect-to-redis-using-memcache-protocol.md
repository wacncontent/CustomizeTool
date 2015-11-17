<properties
	pageTitle="Connect a web app in Azure Websites to Redis Cache via the Memcache protocol | Windows Azure"
	description="Connect a web app in Azure App service to Redis Cache using the Memcache protocol"
	services="app-service\web"
	documentationCenter="php"
	authors="SyntaxC4"
	manager="wpickett"
	editor="riande"/>

<tags
	ms.service="app-service-web"
	ms.date="09/16/2015"
	wacn.date=""/>

# Connect a web app in Azure Websites to Redis Cache via the Memcache protocol

In this article, <!-- deleted by customization you'll --><!-- keep by customization: begin --> you will <!-- keep by customization: end --> learn how to connect a WordPress web app in [Azure Websites](/documentation/services/web-sites/) to [Azure Redis Cache][12] using the [Memcache][13] protocol. If you have an existing web app that <!-- deleted by customization use --><!-- keep by customization: begin --> leverage <!-- keep by customization: end -->s a Memcached server for in-memory caching, You can migrate it to Azure Websites and use the first-party caching solution in Windows Azure with little or no change to your application code. Furthermore, you can use your existing Memcache expertise to create highly scalable, distributed apps in Azure Websites with Azure Redis Cache for in-memory caching, while using popular application frameworks such as .NET, PHP, Node.js, Java, and Python.

Azure Websites enables this application scenario with the Web Apps Memcache shim, which is a local Memcached server that acts as a Memcache proxy for caching calls to Azure Redis Cache. This enables any app that communicates using the Memcache protocol to cache data with Redis Cache. This Memcache shim works at the protocol level, so it can be used by any application or application framework as long as it communicates using the Memcache protocol.
<!-- deleted by customization

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 
-->

## Prerequisites

The Web Apps Memcache shim can be used with any application provided it communicates using the Memcache protocol. For this particular example, the reference application is a Scalable WordPress site which can be provisioned from the Azure Marketplace.

Follow the steps outlined in these <!-- deleted by customization articles --><!-- keep by customization: begin --> posts <!-- keep by customization: end -->:

<!-- keep by customization: begin -->
* [Deploy a Scalable WordPress site in Azure][0]
<!-- keep by customization: end -->
* [Provision an instance of the Azure Redis Cache Service][1]
* [Deploy a Scalable WordPress site in Azure][0]

Once you have the Scalable WordPress site deployed and a Redis Cache instance provisioned you will be ready to proceed with enabling the Memcache shim in Azure Websites.

## Enable the Web Apps Memcache shim

In order to configure Memcache shim, you must create three app settings. This can be done using a variety of methods including the [Azure Management Portal](https://manage.windowsazure.cn/), the [Management Portal][3], the [Azure PowerShell Cmdlets][5] or the [Azure Command-Line Interface][5]. For the purposes of this post, I’m going to use the [Azure Management Portal][4] to set the app settings. The following values can be retrieved from **Settings** blade of your Redis Cache instance.

![Azure Redis Cache Settings Blade](./media/web-sites-connect-to-redis-using-memcache-protocol/1-azure-redis-cache-settings.png)

<!-- deleted by customization
### Add REDIS_HOST app setting

The first app setting you need to create is the **REDIS\_HOST** app setting. This setting sets the destination to which the shim forwards the cache information. The value required for the REDIS_HOST app setting can be retrieved from the **Properties** blade of your Redis Cache instance.

![Azure Redis Cache Host Name](./media/web-sites-connect-to-redis-using-memcache-protocol/2-azure-redis-cache-hostname.png)

Set the key of the app setting to **REDIS\_HOST** and the value of the app setting to the **hostname** of the Redis Cache instance.

![Web App AppSetting REDIS_HOST](./media/web-sites-connect-to-redis-using-memcache-protocol/3-azure-website-appsettings-redis-host.png)
-->
<!-- keep by customization: begin -->
### Add REDIS_HOST App Setting

The first app setting you need to create is the **REDIS_HOST** app setting. This setting sets the destination to which the shim forwards the cache information. The value required for the REDIS_HOST app setting can be retrieved from the **Properties** blade of your Redis Cache instance.

![Azure Redis Cache Host Name](./media/web-sites-connect-to-redis-using-memcache-protocol/2-azure-redis-cache-hostname.png)

Set the key of the app setting to **REDIS_HOST** and the value of the app setting to the **hostname** of the Redis Cache instance.

![Web App AppSetting REDIS_HOST](./media/web-sites-connect-to-redis-using-memcache-protocol/3-azure-website-appsettings-redis-host.png)
<!-- keep by customization: end -->

### Add REDIS_KEY app setting

The second app setting you need to create is the <!-- deleted by customization **REDIS\_KEY** --><!-- keep by customization: begin --> **REDIS_KEY** <!-- keep by customization: end --> app setting. This setting provides the authentication token required to securely access the Redis Cache instance. <!-- deleted by customization You can retrieve the --><!-- keep by customization: begin --> The <!-- keep by customization: end --> value required for the REDIS_KEY app setting <!-- keep by customization: begin --> can be retrieved <!-- keep by customization: end -->  from the **Access keys** blade of the Redis Cache instance.

![Azure Redis Cache Primary Key](./media/web-sites-connect-to-redis-using-memcache-protocol/4-azure-redis-cache-primarykey.png)

Set the key of the app setting to <!-- deleted by customization **REDIS\_KEY** --><!-- keep by customization: begin --> **REDIS_KEY** <!-- keep by customization: end --> and the value of the app setting to the **Primary Key** of the Redis Cache instance.

![Azure Website AppSetting REDIS_KEY](./media/web-sites-connect-to-redis-using-memcache-protocol/5-azure-website-appsettings-redis-primarykey.png)

### Add MEMCACHESHIM_REDIS_ENABLE app setting

The last app setting is used to enable the Memcache Shim in Web Apps, which <!-- deleted by customization uses --><!-- keep by customization: begin --> will use <!-- keep by customization: end --> the REDIS_HOST and REDIS_KEY to connect to the Azure Redis Cache and forward the cache calls. Set the key of the app setting to <!-- deleted by customization **MEMCACHESHIM\_REDIS\_ENABLE** --><!-- keep by customization: begin --> **MEMCACHESHIM_REDIS_ENABLE** <!-- keep by customization: end --> and the value to **true**.

![Web App AppSetting MEMCACHESHIM_REDIS_ENABLE](./media/web-sites-connect-to-redis-using-memcache-protocol/6-azure-website-appsettings-enable-shim.png)

Once you are done adding the three (3) app settings, click **Save**.

## Enable Memcache extension for PHP

<!-- deleted by customization
In order for the application to speak the Memcache protocol, it's necessary to install the Memcache extension to PHP--the language framework for your WordPress site.
-->
<!-- keep by customization: begin -->
In order for the application to speak the Memcache protocol, it is necessary to install the Memcache extension to PHP, (the language framework for your WordPress site).
<!-- keep by customization: end -->

### Download the php_memcache Extension

Browse to [PECL][6]<!-- deleted by customization. Under --><!-- keep by customization: begin -->, under <!-- keep by customization: end --> the caching category, click <!-- keep by customization: begin --> on <!-- keep by customization: end -->  [memcache][7]. Under the downloads column click <!-- keep by customization: begin --> on <!-- keep by customization: end -->  the DLL link.

![PHP PECL Website](./media/web-sites-connect-to-redis-using-memcache-protocol/7-php-pecl-website.png)

Download the Non-Thread Safe (NTS) x86 link for the version of PHP enabled in Web Apps. (Default is PHP 5.4)

![PHP PECL Website Memcache Package](./media/web-sites-connect-to-redis-using-memcache-protocol/8-php-pecl-memcache-package.png)

### Enable the php_memcache extension

After <!-- deleted by customization you download --><!-- keep by customization: begin --> downloading <!-- keep by customization: end --> the file, unzip and upload the <!-- deleted by customization **php\_memcache.dll** --><!-- keep by customization: begin --> **php_memcache.dll** <!-- keep by customization: end --> into the **d:\\home\\site\\wwwroot\\bin\\ext\\** directory. After the php_memcache.dll <!-- deleted by customization is --><!-- keep by customization: begin --> has been <!-- keep by customization: end --> uploaded into the web app, <!-- deleted by customization you need to enable --> the extension <!-- keep by customization: begin --> needs to be enabled <!-- keep by customization: end -->  to the PHP Runtime. To enable the Memcache extension in the Azure Management Portal, open the **Application Settings** blade for the web app, then add a new app setting with the key of <!-- deleted by customization **PHP\_EXTENSIONS** --><!-- keep by customization: begin --> **PHP_EXTENSIONS** <!-- keep by customization: end --> and the value **bin\\ext\\php_memcache.dll**.


> <!-- deleted by customization [AZURE.NOTE] --> If the web app needs to load multiple PHP extensions, the value of PHP_EXTENSIONS should be a comma delimited list of relative paths to DLL files.

![Web App AppSetting PHP_EXTENSIONS](./media/web-sites-connect-to-redis-using-memcache-protocol/9-azure-website-appsettings-php-extensions.png)

Once finished, click **Save**.

## Install Memcache WordPress plugin

> <!-- deleted by customization [AZURE.NOTE] --> You can also download the [Memcached Object Cache Plugin](https://wordpress.org/plugins/memcached/) from WordPress.org.

On the WordPress plugins page, click <!-- keep by customization: begin --> the <!-- keep by customization: end -->  **Add New** <!-- keep by customization: begin --> button <!-- keep by customization: end --> .

![WordPress Plugin Page](./media/web-sites-connect-to-redis-using-memcache-protocol/10-wordpress-plugin.png)

In the search box, type **memcached** and press <!-- keep by customization: begin --> the <!-- keep by customization: end -->  **Enter** <!-- keep by customization: begin --> key <!-- keep by customization: end --> .

![WordPress Add New Plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/11-wordpress-add-new-plugin.png)

Find **Memcached Object Cache** in the list, then click <!-- keep by customization: begin --> on the <!-- keep by customization: end -->  **Install Now** <!-- keep by customization: begin --> button <!-- keep by customization: end --> .

![WordPress Install Memcache Plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/12-wordpress-install-memcache-plugin.png)

### Enable the Memcache WordPress plugin

>[AZURE.NOTE] Follow the instructions in this blog on [How to enable a Site Extension in Web Apps][8] to install Visual Studio Online.

In the `wp-config.php` file, add the following code <!-- keep by customization: begin --> snippet <!-- keep by customization: end -->  above the stop editing comment near the end of the file.

```php
$memcached_servers = array(
	'default' => array('localhost:' . getenv("MEMCACHESHIM_PORT"))
);
```

Once this code <!-- keep by customization: begin --> snippet <!-- keep by customization: end -->  has been pasted, monaco will automatically save the document.

The next step is to enable the object-cache plugin. This is done by dragging and dropping **object-cache.php** from **wp-content/memcached** folder to the **wp-content** folder to enable the Memcache Object Cache functionality.

![Locate the memcache object-cache.php plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/13-locate-memcache-object-cache-plugin.png)

Now that the **object-cache.php** file is in the **wp-content** folder, the Memcached Object Cache is now enabled.

![Enable the memcache object-cache.php plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/14-enable-memcache-object-cache-plugin.png)

## <!-- deleted by customization Verify --><!-- keep by customization: begin --> Verifying <!-- keep by customization: end --> the Memcache Object Cache plugin is functioning

All of the steps to enable the Web Apps Memcache shim are now complete. The only thing left is to verify that the data is populating your Redis Cache instance.

### Enable the non-SSL port support in Azure Redis Cache

>[AZURE.NOTE] At the time of writing this <!-- deleted by customization article --><!-- keep by customization: begin --> document <!-- keep by customization: end -->, the Redis CLI does not support SSL connectivity, thus the following steps are necessary.

In the Azure <!-- deleted by customization Management Portal --><!-- keep by customization: begin --> Protal <!-- keep by customization: end -->, browse to the Redis Cache instance that you created for this web app. Once the cache's blade is open, click <!-- keep by customization: begin --> on <!-- keep by customization: end -->  the **Settings** icon.

![Azure Redis Cache Settings Button](./media/web-sites-connect-to-redis-using-memcache-protocol/15-azure-redis-cache-settings-button.png)

Select **Access Ports** from the list.

![Azure Redis Cache Access Port](./media/web-sites-connect-to-redis-using-memcache-protocol/16-azure-redis-cache-access-port.png)

Click **No** for **Allow access only via SSL**.

![Azure Redis Cache Access Port SSL Only](./media/web-sites-connect-to-redis-using-memcache-protocol/17-azure-redis-cache-access-port-ssl-only.png)

You will see that the NON-SSL port is now set. Click **Save**.

![Azure Redis Cache Redis Access Portal Non-SSL](./media/web-sites-connect-to-redis-using-memcache-protocol/18-azure-redis-cache-access-port-non-ssl.png)

### Connect to Azure Redis Cache from redis-cli

>[AZURE.NOTE] This step assumes that redis is installed locally on your development machine. [Install Redis locally using these instructions][9].

Open your command-line console of choice and type the following command:

```shell
redis-cli –h <hostname-for-redis-cache> –a <primary-key-for-redis-cache> –p 6379
```

Replace the **<hostname-for-redis-cache>** with the actual xxxxx.redis.cache.chinacloudapi.cn hostname and the **<primary-key-for-redis-cache>** with the access key for the cache, then press **Enter**. Once the CLI has connected to the Redis Cache instance, issue any redis command. In the screenshot below, I’ve chosen to list the keys.

![Connect to Azure Redis Cache from Redis CLI in Terminal](./media/web-sites-connect-to-redis-using-memcache-protocol/19-redis-cli-terminal.png)

The call to list the keys should return a value. If not, try navigating to the web app and trying again.

## Conclusion

Congratulations! The WordPress app now has a centralized in-memory cache to aid in increasing throughput. Remember, the Web Apps Memcache Shim can be used with any Memcache client regardless of programming language or application framework. To provide feedback or to ask questions about the Web Apps Memcache shim, post to [MSDN Forums][10] or [Stackoverflow][11].

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and <!-- deleted by customization its impact --><!-- keep by customization: begin --> Its Impact <!-- keep by customization: end --> on <!-- deleted by customization existing --><!-- keep by customization: begin --> Existing <!-- keep by customization: end --> Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)


[0]: http://bit.ly/1F0m3tw
[1]: http://bit.ly/1t0KxBQ
<!-- deleted by customization
[2]: http://manage.windowsazure.cn
[3]: http://manage.windowsazure.cn
-->
<!-- keep by customization: begin -->
[2]: https://manage.windowsazure.cn
[3]: https://manage.windowsazure.cn
<!-- keep by customization: end -->
[4]: /documentation/articles/powershell-install-configure
<!-- deleted by customization
[5]: /downloads
-->
<!-- keep by customization: begin -->
[5]: #
<!-- keep by customization: end -->
[6]: http://pecl.php.net
[7]: http://pecl.php.net/package/memcache
[8]: http://blog.syntaxc4.net/post/2015/02/05/how-to-enable-a-site-extension-in-azure-websites.aspx
[9]: http://redis.io/download#installation
[10]: https://social.msdn.microsoft.com/Forums/home?forum=windowsazurewebsitespreview
[11]: http://stackoverflow.com/questions/tagged/azure-web-sites
<!-- deleted by customization
[12]: /services/cache/
-->
<!-- keep by customization: begin -->
[12]: /documentation/services/cache
<!-- keep by customization: end -->
[13]: http://memcached.org
