<properties
	pageTitle="Connect a web app in Azure to Redis Cache via the Memcache protocol | Windows Azure"
	description="Connect a web app in Azure App service to Redis Cache using the Memcache protocol"
	services="app-service\web"
	documentationCenter="php"
	authors="SyntaxC4"
	manager="wpickett"
	editor="riande"/>

<tags
	ms.service="app-service-web"
	ms.date="12/24/2015"
	wacn.date=""/>

# Connect a web app in Azure to Redis Cache via the Memcache protocol

In this article, you'll learn how to connect a WordPress web app in [Azure Web App](/documentation/services/web-sites/) to [Azure Redis Cache][12] using the [Memcache][13] protocol. If you have an existing web app that uses a Memcached server for in-memory caching, You can migrate it to Azure and use the first-party caching solution in Windows Azure with little or no change to your application code. Furthermore, you can use your existing Memcache expertise to create highly scalable, distributed apps in Azure with Azure Redis Cache for in-memory caching, while using popular application frameworks such as .NET, PHP, Node.js, Java, and Python.  

Azure Web Apps enables this application scenario with the Web Apps Memcache shim, which is a local Memcached server that acts as a Memcache proxy for caching calls to Azure Redis Cache. This enables any app that communicates using the Memcache protocol to cache data with Redis Cache. This Memcache shim works at the protocol level, so it can be used by any application or application framework as long as it communicates using the Memcache protocol.

## Prerequisites

The Web Apps Memcache shim can be used with any application provided it communicates using the Memcache protocol. For this particular example, the reference application is a Scalable WordPress site which can be provisioned from the Azure gallery.

Follow the steps outlined in these articles:

* [Provision an instance of the Azure Redis Cache Service][0]
* [Deploy a Scalable WordPress site in Azure][1]

Once you have the Scalable WordPress site deployed and a Redis Cache instance provisioned you will be ready to proceed with enabling the Memcache shim in Azure Web Apps.

## Enable the Web Apps Memcache shim

In Windows Azure China, Redis Cache can only be managed by Azure PowerShell or Azure CLI

[AZURE.INCLUDE [azurerm-azurechinacloud-environment-parameter](../includes/azurerm-azurechinacloud-environment-parameter.md)]

### Add REDIS_HOST app setting

The first app setting you need to create is the **REDIS\_HOST** app setting. This setting sets the destination to which the shim forwards the cache information. The value required for the REDIS_HOST app setting can be retrieved from the following PowerShell Command.

	$myRedisCache = Get-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>"; $myRedisCache.HostName

Set the key of the app setting to **REDIS\_HOST** and the value of the app setting to the **hostname** of the Redis Cache instance.

### Add REDIS_KEY app setting

The second app setting you need to create is the **REDIS\_KEY** app setting. This setting provides the authentication token required to securely access the Redis Cache instance. You can retrieve the value required for the REDIS_KEY app setting from the following PowerShell Command.

	Get-AzureRmRedisCacheKey -Name "<your cache name>" -ResourceGroupName "<your resource group name>"

Set the key of the app setting to **REDIS\_KEY** and the value of the app setting to the **Primary Key** of the Redis Cache instance.

### Add MEMCACHESHIM_REDIS_ENABLE app setting

The last app setting is used to enable the Memcache Shim in Web Apps, which uses the REDIS_HOST and REDIS_KEY to connect to the Azure Redis Cache and forward the cache calls. Set the key of the app setting to **MEMCACHESHIM\_REDIS\_ENABLE** and the value to **true**.

Once you are done adding the three (3) app settings, click **Save**.

## Enable Memcache extension for PHP

In order for the application to speak the Memcache protocol, it's necessary to install the Memcache extension to PHP--the language framework for your WordPress site.

### Download the php_memcache Extension

Browse to [PECL][6]. Under the caching category, click [memcache][7]. Under the downloads column click the DLL link.

![PHP PECL Website](./media/web-sites-connect-to-redis-using-memcache-protocol/7-php-pecl-website.png)

Download the Non-Thread Safe (NTS) x86 link for the version of PHP enabled in Web Apps. (Default is PHP 5.4)

![PHP PECL Website Memcache Package](./media/web-sites-connect-to-redis-using-memcache-protocol/8-php-pecl-memcache-package.png)

### Enable the php_memcache extension

After you download the file, unzip and upload the **php\_memcache.dll** into the **d:\\home\\site\\wwwroot\\bin\\ext\\** directory. After the php_memcache.dll is uploaded into the web app, you need to enable the extension to the PHP Runtime. To enable the Memcache extension in the Azure Management Portal, open the **Configure** of your the web app, then add a new app setting with the key of **PHP\_EXTENSIONS** and the value **bin\\ext\\php_memcache.dll**.


> [AZURE.NOTE] If the web site needs to load multiple PHP extensions, the value of PHP_EXTENSIONS should be a comma delimited list of relative paths to DLL files.

Once finished, click **Save**.

## Install Memcache WordPress plugin

> [AZURE.NOTE] You can also download the [Memcached Object Cache Plugin](https://wordpress.org/plugins/memcached/) from WordPress.org.

On the WordPress plugins page, click **Add New**.

![WordPress Plugin Page](./media/web-sites-connect-to-redis-using-memcache-protocol/10-wordpress-plugin.png)

In the search box, type **memcached** and press **Enter**.

![WordPress Add New Plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/11-wordpress-add-new-plugin.png)

Find **Memcached Object Cache** in the list, then click **Install Now**.

![WordPress Install Memcache Plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/12-wordpress-install-memcache-plugin.png)

### Enable the Memcache WordPress plugin

>[AZURE.NOTE] Follow the instructions in this blog on [How to enable a Site Extension in Web Apps][8] to install Visual Studio Team Services.

In the `wp-config.php` file, add the following code above the stop editing comment near the end of the file.

	$memcached_servers = array(
		'default' => array('localhost:' . getenv("MEMCACHESHIM_PORT"))
	);

Once this code has been pasted, monaco will automatically save the document.

The next step is to enable the object-cache plugin. This is done by dragging and dropping **object-cache.php** from **wp-content/plugins/memcached** folder to the **wp-content** folder to enable the Memcache Object Cache functionality.

![Locate the memcache object-cache.php plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/13-locate-memcache-object-cache-plugin.png)

Now that the **object-cache.php** file is in the **wp-content** folder, the Memcached Object Cache is now enabled.

![Enable the memcache object-cache.php plugin](./media/web-sites-connect-to-redis-using-memcache-protocol/14-enable-memcache-object-cache-plugin.png)

## Verify the Memcache Object Cache plugin is functioning

All of the steps to enable the Web Apps Memcache shim are now complete. The only thing left is to verify that the data is populating your Redis Cache instance.

### Enable the non-SSL port support in Azure Redis Cache

>[AZURE.NOTE] At the time of writing this article, the Redis CLI does not support SSL connectivity, thus the following steps are necessary.

You can use the following PowerShell Command to enable NON-SSL port.

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true

### Connect to Azure Redis Cache from redis-cli

>[AZURE.NOTE] This step assumes that redis is installed locally on your development machine. [Install Redis locally using these instructions][9].

Open your command-line console of choice and type the following command:

	redis-cli -h <hostname-for-redis-cache> -a <primary-key-for-redis-cache> -p 6379

Replace the **&lt;hostname-for-redis-cache&gt;** with the actual xxxxx.redis.cache.chinacloudapi.cn hostname and the **&lt;primary-key-for-redis-cache&gt;** with the access key for the cache, then press **Enter**. Once the CLI has connected to the Redis Cache instance, issue any redis command. In the screenshot below, I've chosen to list the keys.

![Connect to Azure Redis Cache from Redis CLI in Terminal](./media/web-sites-connect-to-redis-using-memcache-protocol/19-redis-cli-terminal.png)

The call to list the keys should return a value. If not, try navigating to the web app and trying again.

## Conclusion

Congratulations! The WordPress app now has a centralized in-memory cache to aid in increasing throughput. Remember, the Web Apps Memcache Shim can be used with any Memcache client regardless of programming language or application framework. To provide feedback or to ask questions about the Web Apps Memcache shim, post to [MSDN Forums][10] or [CSDN][11].



[0]: /documentation/articles/cache-dotnet-how-to-use-azure-redis-cache#create-a-cache
[1]: http://bit.ly/1t0KxBQ
[2]: http://manage.windowsazure.cn
[3]: http://manage.windowsazure.cn
[4]: /documentation/articles/powershell-install-configure
[5]: /downloads
[6]: http://pecl.php.net
[7]: http://pecl.php.net/package/memcache
[8]: http://blog.syntaxc4.net/post/2015/02/05/how-to-enable-a-site-extension-in-azure-websites.aspx
[9]: http://redis.io/download#installation
[10]: https://social.msdn.microsoft.com/Forums/home?forum=windowsazurewebsitespreview
[11]: http://azure.csdn.net/
[12]: /services/cache/
[13]: http://memcached.org
