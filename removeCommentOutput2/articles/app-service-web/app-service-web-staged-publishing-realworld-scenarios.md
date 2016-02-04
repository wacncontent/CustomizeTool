<!-- not suitable for Mooncake -->
<!-- ? -->

<properties
   pageTitle="Use DevOps environments effectively for your web app"
   description="Learn how to use deployment slots to setup and manage multiple development environments for your application"
   services="app-service\web"
   documentationCenter=""
   authors="sunbuild"
   manager="yochayk"
   editor=""/>

<tags
	ms.service="app-service"
	ms.date="12/24/2015"
	wacn.date=""/>

# Use DevOps environments effectively for your web apps

This article shows you how to setup and manage web application deployments  for multiple versions of your application such as development, staging, QA and production. Each version of your application can be considered a development environment for a specific need within your deployment process, for example QA environment can be used by your team of developers to test the quality of the application before you push the changes to production.
Setting up multiple development environments can be a challenging task as you need to track and manage the resources (compute, web app, database, cache etc.) across these environments and deploy content from one environment to another.

## Setting up a non-production environment (stage,dev,QA)
Once you have a production web app up and running, the next step is to create a non-production environment. In order to use deployment slots make sure you are running in the **Standard** App Service plan mode. Deployment slots are actually live web apps with their own hostnames. Web app content and configuration elements can be swapped between two deployment slots, including the production slot. Deploying your application to a deployment slot has the following benefits:

1. You can validate web app changes in a staging deployment slot before swapping it with the production slot.
2. Deploying a web app to a slot first and swapping it into production ensures that all instances of the slot are warmed up before being swapped into production. This eliminates downtime when you deploy your web app. The traffic redirection is seamless, and no requests are dropped due to swap operations. 
3. After a swap, the slot with previously staged web app now has the previous production web app. If the changes swapped into the production slot are not as you expected, you can perform the same swap immediately to get your "last known good web app" back.

To setup a staging deployment slot, see [Set up staging environments for web apps in Azure](/documentation/articles/web-sites-staged-publishing) . Every environment should include its own set of resources, for example if your r web app uses a database then both production web app and staging web app should be using different databases.  Add staging development environment resources such as database, storage or cache for setting up r staging development environment.

## Examples of using multiple development environments

, Any project should follow a source code management with at least two environments, a development and production environment, but when using Content management systems, Application frameworks etc we might run into issues where the application does not support this scenario out of the box. This is true for some of the popular frameworks discussed below. Lots of questions come to mind when working with a CMS/frameworks such as

1. How to break it out into different environments
2. What files can I change and wont impact framework version updates
3. How to manage configuration per environment
4. How to manage modules/plugins version updates,core framework version updates

There are many ways to setup a multiple environment for your project and the examples below are just one such method for the respective applications.

### WordPress
In this section you will learn how to setup a deployment workflow using slots for WordPress. WordPress like most CMS solutions does not support working with multiple development environments out of the box. Azure Web Apps have a few features that make it easier to store configuration settings outside of your code.

Before creating a staging slot, setup your application code to support multiple environments. To support multiple environments in WordPress you need to edit `wp-config.php` on your local development web app add the following code at the beginning of the file. This will allow your application to pick the correct configuration based on the selected environment.

<!
	// Support multiple environments
	// Support multiple environments
	// set the config file based on current environment
	/**/
	if (strpos(filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING),'localhost') !== false) {
	    // local development
	    $config_file = 'config/wp-config.local.php';
	}
	elseif  ((strpos(getenv('WP_ENV'),'stage') !== false) ||  (strpos(getenv('WP_ENV'),'prod' )!== false )){
	      //single file for all azure development environments
	      $config_file = 'config/wp-config.azure.php';
	}
	$path = dirname(__FILE__) . '/';
	if (file_exists($path . $config_file)) {
	    // include the config file if it exists, otherwise WP is going to fail
	    require_once $path . $config_file;
	<!}



Create a folder under web app root called `config` and add two files: `wp-config.azure.php`  and `wp-config.local.php`  representing your azure and local environment respectively.

Copy the following in `wp-config.local.php` :

	<?php
	// MySQL settings
	/** The name of the database for WordPress */
	
	define('DB_NAME', 'yourdatabasename');
	
	/** MySQL database username */
	define('DB_USER', 'yourdbuser');
	
	/** MySQL database password */
	define('DB_PASSWORD', 'yourpassword');
	
	/** MySQL hostname */
	define('DB_HOST', 'localhost');
	/**
	 * For developers: WordPress debugging mode.
	 * * Change this to true to enable the display of notices during development.
	 * It is strongly recommended that plugin and theme developers use WP_DEBUG
	 * in their development environments.
	 */
	define('WP_DEBUG', true);
	
	//Security key settings
	define('AUTH_KEY',         'put your unique phrase here');
	define('SECURE_AUTH_KEY',  'put your unique phrase here');
	define('LOGGED_IN_KEY',    'put your unique phrase here');
	define('NONCE_KEY',        'put your unique phrase here');
	define('AUTH_SALT',        'put your unique phrase here');
	define('SECURE_AUTH_SALT', 'put your unique phrase here');
	define('LOGGED_IN_SALT',   'put your unique phrase here');
	define('NONCE_SALT',       'put your unique phrase here');
	
	/**
	 * WordPress Database Table prefix.
	 *
	 * You can have multiple installations in one database if you give each a unique
	 * prefix. Only numbers, letters, and underscores please!
	 */
	$table_prefix  = 'wp_';

Setting the security keys above can help preventing your web app from being hacked, so use unique values. If you need to generate the string for security keys mentioned above, you can go to the automatic generator to create new keys/values using this [link] (https://api.wordpress.org/secret-key/1.1/salt)

Copy the following code in `wp-config.azure.php`:


	<?php
	// MySQL settings
	/** The name of the database for WordPress */
	
	define('DB_NAME', getenv('DB_NAME'));
	
	/** MySQL database username */
	define('DB_USER', getenv('DB_USER'));
	
	/** MySQL database password */
	define('DB_PASSWORD', getenv('DB_PASSWORD'));
	
	/** MySQL hostname */
	define('DB_HOST', getenv('DB_HOST'));
	
	/**
	* For developers: WordPress debugging mode.
	*
	* Change this to true to enable the display of notices during development.
	* It is strongly recommended that plugin and theme developers use WP_DEBUG
	* in their development environments.
	* Turn on debug logging to investigate issues without displaying to end user. For WP_DEBUG_LOG to
	* do anything, WP_DEBUG must be enabled (true). WP_DEBUG_DISPLAY should be used in conjunction
	* with WP_DEBUG_LOG so that errors are not displayed on the page */
	
	*/
	define('WP_DEBUG', getenv('WP_DEBUG'));
	define('WP_DEBUG_LOG', getenv('TURN_ON_DEBUG_LOG'));
	define('WP_DEBUG_DISPLAY',false);
	
	//Security key settings
	/** If you need to generate the string for security keys mentioned above, you can go the automatic generator to create new keys/values: https://api.wordpress.org/secret-key/1.1/salt **/
	define('AUTH_KEY' ,getenv('DB_AUTH_KEY'));
	define('SECURE_AUTH_KEY',  getenv('DB_SECURE_AUTH_KEY'));
	define('LOGGED_IN_KEY', getenv('DB_LOGGED_IN_KEY'));
	define('NONCE_KEY', getenv('DB_NONCE_KEY'));
	define('AUTH_SALT',  getenv('DB_AUTH_SALT'));
	define('SECURE_AUTH_SALT', getenv('DB_SECURE_AUTH_SALT'));
	define('LOGGED_IN_SALT',   getenv('DB_LOGGED_IN_SALT'));
	define('NONCE_SALT',   getenv('DB_NONCE_SALT'));
	
	/**
	* WordPress Database Table prefix.
	*
	* You can have multiple installations in one database if you give each a unique
	* prefix. Only numbers, letters, and underscores please!
	*/
	$table_prefix  = getenv('DB_PREFIX');

#### Use Relative Paths
One last thing is to allow the WordPress app to use relative paths. WordPress stores URL information in the database. This makes moving content from one environment to another more difficult as you need to update the database every time you move from local to stage or stage to production environments. To reduce the risk of issues that can be caused with deploying a database every time you deploy from one environment to another use the [Relative Root links  plugin](https://wordpress.org/plugins/root-relative-urls/) which can be installed using WordPress administrator dashboard or download it manually from [here](https://downloads.wordpress.org/plugin/root-relative-urls.zip).

Add the following entries to your `wp-config.php` file before the `That's all, stop editing!` comment:


    define('WP_HOME', 'http://' . filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
	define('WP_SITEURL', 'http://' . filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
	define('WP_CONTENT_URL', '/wp-content');
define('DOMAIN_CURRENT_SITE', filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
```

Activate the plugin through the `Plugins` menu in WordPress Administrator dashboard.  Save your permalink settings for WordPress app.

#### The final `wp-config.php` file
Any WordPress Core updates will not affect your `wp-config.php` , `wp-config.azure.php` and `wp-config.local.php` files  . In the end the `wp-config.php` file will look like this

	<?php
	/**
	 * The base configurations of the WordPress.
	 *
	 * This file has the following configurations: MySQL settings, Table Prefix,
	 * Secret Keys, and ABSPATH. You can find more information by visiting
	 *
	 * Codex page. You can get the MySQL settings from your web host.
	 *
	 * This file is used by the wp-config.php creation script during the
	 * installation. You don't have to use the web web app, you can just copy this file
	 * to "wp-config.php" and fill in the values.
	 *
	 * @package WordPress
	 */
	
	// Support multiple environments
	// set the config file based on current environment
	if (strpos($_SERVER['HTTP_HOST'],'localhost') !== false) { // local development
	    $config_file = 'config/wp-config.local.php';
	}
	elseif  ((strpos(getenv('WP_ENV'),'stage') !== false) ||  (strpos(getenv('WP_ENV'),'prod' )!== false )){
	    $config_file = 'config/wp-config.azure.php';
	}
	
	
	$path = dirname(__FILE__) . '/';
	if (file_exists($path . $config_file)) {
	    // include the config file if it exists, otherwise WP is going to fail
	    require_once $path . $config_file;
	}
	
	/** Database Charset to use in creating database tables. */
	define('DB_CHARSET', 'utf8');
	
	/** The Database Collate type. Don't change this if in doubt. */
	define('DB_COLLATE', '');
	
	
	/* That's all, stop editing! Happy blogging. */
	
	define('WP_HOME', 'http://' . filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
	define('WP_SITEURL', 'http://' . filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
	define('WP_CONTENT_URL', '/wp-content');
	define('DOMAIN_CURRENT_SITE', filter_input(INPUT_SERVER, 'HTTP_HOST', FILTER_SANITIZE_STRING));
	
	/** Absolute path to the WordPress directory. */
	if ( !defined('ABSPATH') )
		define('ABSPATH', dirname(__FILE__) . '/');
	
	/** Sets up WordPress vars and included files. */
	require_once(ABSPATH . 'wp-settings.php');

#### Setup a Staging Environment
Assuming you already have a WordPress web app running on Azure Web, login to [Azure Management Portal](http://manage.windowsazure.cn) and go to your WordPress web app. If not you can create one from the marketplace. To learn more, click [here](/documentation/articles/web-sites-php-web-site-gallery).
Click on **Dashboard** -> **quick glance** -> **Add a new deployment slot** with the name stage .A deployment slot is another web site sharing the same resources as the primary web site created above.


Add another MySQL database, say `wordpress-stage-db`.Update the Connection strings for your stage deployment slot to point to newly created database, `wordpress-stage-db`. Note that your production web site , `wordpressapp-group` and staging web site `wordpressprodapp-stage` must point to different databases.

#### Configure environment-specific app settings
Developers can store key-value string pairs in Azure as part of the configuration information associated with a web app called App Settings. At runtime, Azure Web Apps automatically retrieve these values for you and make them available to code running in your web app.  From a security perspective that is a benefit since sensitive information such as database connection strings with passwords should never show up as clear text in a file such as `wp-config.php`.

This process  defined below is useful when you perform updates as it includes both file changes and database changes for WordPress app:

- WordPress version upgrade
- Add new or edit or upgrade Plugins
- Add new or edit or upgrade themes

Configure app settings for:

- database information
- turning on/off  WordPress logging
- WordPress security settings


Make sure you have added the following app settings for your production web app and stage slot. Note that the production web app and Staging web app use different databases.
Uncheck **Slot Setting** checkbox for all the settings parameters except WP_ENV. This will swap the configuration for your web app, along with file content and database. If **Slot Setting** is **Checked**, the web app's app settings and connection string configuration will NOT move across environments when doing a SWAP operation and hence if any database changes are present this will not break your production web app.

Deploy the local development environment web app to stage web app and database using WebMatrix or tool(s) of your choice such as FTP , Git or PhpMyAdmin.

![Web Matrix Publish dialog for WordPress web app](./media/app-service-web-staged-publishing-realworld-scenarios/4wmpublish.png)

Browse and test your staging web app. Considering a scenario where the theme of the web app is to be updated, here is the staging web app.

![Browse staging web app before swapping slots](./media/app-service-web-staged-publishing-realworld-scenarios/5wpstage.png)


If all looks good, use the following PowerShell script to swap you web site slot.


	try{
	    $acct = Get-AzureRmSubscription
	}
	catch{
	    Login-AzureRmAccount -EnvironmentName AzureChinaCloud
	}
	
	# this is the resource group of you web site.
	# If you didn't specify during creation, by default, it's "Default-Web-ChinaEast" or "Default-Web-ChinaNorth"
	$myResourceGroup = '<your resource Group>'
	$mySite = '<your web site name>'
	$stageSlot = '<your source slot>'
	
	
	$props = (Invoke-AzureRmResourceAction -ResourceGroupName $myResourceGroup `
	            -ResourceType Microsoft.Web/sites/Config -Name $mySite/appsettings `
	            -Action list -ApiVersion 2015-08-01 -Force).Properties

	$props_stage = (Invoke-AzureRmResourceAction -ResourceGroupName $myResourceGroup `
	            -ResourceType Microsoft.Web/sites/slots/Config -Name $mySite/$stageSlot/appsettings `
	            -Action list -ApiVersion 2015-08-01 -Force).Properties 
	
	$hash = @{}
	$props | Get-Member -MemberType NoteProperty | % { $hash[$_.Name] = $props.($_.Name) }
	
	$hash_stage = @{}
	$props_stage | Get-Member -MemberType NoteProperty | % { $hash_stage[$_.Name] = $props_stage.($_.Name) }
	
	Set-AzureRMWebAppSlot -ResourceGroupName $myResourceGroup `
	            -Name $mySite -Slot $stageSlot -AppSettings $hash
	
	$ParametersObject = @{targetSlot = 'production'}
	Invoke-AzureRmResourceAction -ResourceGroupName $myResourceGroup `
	            -ResourceType Microsoft.Web/sites/slots `
	            -ResourceName $mySite/$stageSlot `
	            -Action slotsswap `
	            -Parameters $ParametersObject `
	            -ApiVersion 2015-08-01

	Set-AzureRMWebAppSlot -ResourceGroupName $myResourceGroup `
	            -Name $mySite -Slot $stageSlot -AppSettings $hash_stage

> [AZURE.NOTE] The above script is written for Azure PowerShell 1.0.2 or greater. For lower version, please change the commands correspondingly. For more detail, see the blog [Azure PowerShell 1.0.0 or greater in China](http://blogs.msdn.com/b/azchina/archive/2015/12/18/azure-powershell-1.0.0_e54e0a4e48722c6728572d4efd56_azure_7f4f28758476e86c0f618b4e7998_.aspx).

You must use this PowerShell script (or some other similar way, such as Azure CLI) to swap, in order to keep the app settings for each slot. If you swap on Azure Management Portal, the web site's app settings, connection strings configuration will NOT move across environments when doing a SWAP operation and hence if any database changes are present this will not be visible breaking your production web site.


 > [AZURE.NOTE]
 >If you need to swap some of the app settings while keep other app settings, you can manipulate the variables `$hash` and `$hash_stage` in the above script.

Before doing a SWAP, here is the production WordPress web app
![Production web app before swapping slots](./media/app-service-web-staged-publishing-realworld-scenarios/7bfswap.png)

After the SWAP operation, the theme has been updated on your production web app.

![Production web app after swapping slots](./media/app-service-web-staged-publishing-realworld-scenarios/8afswap.png)

In a situation when you need to **rollback**, you can go to the production web app settings and click on the **Swap** button to swap the web app and database from production to staging slot. An important thing to remember is that if database changes are included with a **Swap** operation at any given time, then the next time you re-deploy to your staging web app you need to deploy the database changes to the current database for your staging web app which could be the previous production database or the stage database.

#### Summary
To generalize the process for any application with a database

1. Install application on your local environment
2. Include environment specific configuration (local and Azure Web App )
3. Setup  your environments in Azure Web Apps- Staging , Production
4. If you have a production application already running on Azure, sync your production content (files/code + database) to local and staging environment.
5. Develop your application on your local environment
6. Place your production web app under maintenance or locked mode and sync database content from production to staging and dev environments
7. Deploy to Staging environment and Test
8. Deploy to Production environment
9. Repeat steps 4 through 6

## References
[Agile software development with Azure Web App](/documentation/articles/app-service-agile-software-development)

[Set up staging environments for web apps in Azure](/documentation/articles/web-sites-staged-publishing)

[How to block web access to non-production deployment slots](http://ruslany.net/2014/04/azure-web-sites-block-web-access-to-non-production-deployment-slots/)
