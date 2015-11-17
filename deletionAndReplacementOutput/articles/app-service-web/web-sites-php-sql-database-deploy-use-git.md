deletion:

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

reason: ()

replacement:

deleted:

		preview portal](https://manage.windowsazure.cn/)

replaced by:

		Management Portal](https://manage.windowsazure.cn/)

reason: ()

deleted:

		1. Log in to the [Azure preview portal](https://manage.windowsazure.cn/).
		
		2. Open the Azure Marketplace either by clicking the **Marketplace** icon, or by clicking the **New** icon on the bottom left of the dashboard, selecting **Web + mobile** and then **Azure Marketplace** at the bottom.
			
		3. In the Marketplace, select **Web Apps**.
		
		4. Click the **Web app + SQL** icon.
		
		5. After reading the description of the Web app + SQL app, select **Create**.
		
		6. Click on each part (**Resource Group**, **Web App**, **Database**, and **Subscription**) and enter or select values for the required fields:
			
			- Enter a URL name of your choice	
			- Configure database server credentials
			- Select the region closest to you
		
			![configure your app](./media/web-sites-php-sql-database-deploy-use-git/configure-db-settings.png)
		
		7. When finished defining the web app, click **Create**.
		
			When the web app has been created, the **Notifications** button will flash a green **SUCCESS** and the resource group blade open to show both the web app and the SQL database in the group.
		
		4. Click the web app's icon in the resource group blade to open the web app's blade.
		
			![web app's resource group](./media/web-sites-php-sql-database-deploy-use-git/resource-group-blade.png)
		
		5. Click **Set up continuous deployment** > **Choose Source**. Select **Local Git Repository** and click **OK**.
		
			![where is your source code](./media/web-sites-php-sql-database-deploy-use-git/setup-local-git.png)
		
			If you have not set up a Git repository before, you must provide a user name and password. To do this, click **Set deployment credentials** in the web app's blade.
		
			![](./media/web-sites-php-sql-database-deploy-use-git/deployment-credentials.png)
		
		6. **Set up continous deployment** becomes **No deployment found**. Click it to see the Git remote URL you need to use to deploy your PHP app later.
		
		##Get SQL Database connection information
		
		To connect to the SQL Database instance that is linked to your web app, your will need the connection information, which you specified when you created the database. To get the SQL Database connection information, follow these steps:
		
		1. Back in the resource group's blade, click the SQL database's icon.
		
		2. In the SQL database's blade, click **Properties**, then click **Show database connection strings**. 
		
			![View database properties](./media/web-sites-php-sql-database-deploy-use-git/view-database-properties.png)
			
		3. From the **PHP** section of the resulting dialog, make note of the values for `Server`, `SQL Database`, and `User Name`. You will use these values later when publishing your PHP web app to Azure Websites.

replaced by:

		1. Login to the [Azure Management Portal][management-portal].
		2. Click the **New** icon on the bottom left of the portal.
		![Create New Azure  Website][new- Website]
		
		3. Click ** Website**, then **Custom Create**.
		
			![Custom Create a new  Website][custom-create]
		
			Enter a value for **URL**, select **Create a New SQL Database** from the **Database** dropdown,  and select **Publish from source control**. Click the arrow at the bottom of the dialog.
		
			![Fill in  Website details][ Website-details-sqlazure]
		
		4. Enter a value for the **Name** of your database, select **NEW SQL Database server**, provide login credentials, and select a region. Click the arrow at the bottom of the dialog.
		
			![Fill in SQL Database settings][database-settings]
		
		5. Select **Local Git repository** for your source code.
		
			![where is your source code][where-is-code]
		
			If you have not set up a Git repository before, you must provide a user name and password.
		
		6. After the web site has been created, open the site's dashboard, and select **View deployments**.
		
			![Web site dashboard][go-to-dashboard]
		
		9. You will see instructions for pushing your application files to the repository. Make note of these instructions - you will need them later.
		
			![Git instructions][git-instructions]
		##Get SQL Database connection information
		
		To connect to the SQL Database instance that is linked to your web app, your will need the connection information, which you specified when you created the database. To get the SQL Database connection information, follow these steps:
		1. From the Azure Management Portal, click **Linked Resources**, then click the database name.
		
			![Linked Resources][linked-resources]
		
		2. Click **View connection strings**.
		
			![Connection string][connection-string]
			
		3. From the **PHP** section of the resulting dialog, make note of the values for `SERVER`, `DATABASE`, and `USERNAME`.

reason: ()

deleted:

		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the portal to the preview portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

replaced by:

		[running-app]: ./media/web-sites-php-sql-database-deploy-use-git/running_app_3.png
		[new- Website]: ./media/web-sites-php-sql-database-deploy-use-git/new_Website.jpg
		[custom-create]: ./media/web-sites-php-sql-database-deploy-use-git/custom_create.png
		[website-details-sqlazure]: ./media/web-sites-php-sql-database-deploy-use-git/createphpgitsite.png
		[database-settings]: ./media/web-sites-php-sql-database-deploy-use-git/setupdb.png
		[create-server]: ./media/web-sites-php-sql-database-deploy-use-git/create_server.jpg
		[go-to-dashboard]: ./media/web-sites-php-sql-database-deploy-use-git/viewdeploy.png
		[setup-git-publishing]: ./media/web-sites-php-sql-database-deploy-use-git/setup_git_publishing.png
		[credentials]: ./media/web-sites-php-sql-database-deploy-use-git/git-deployment-credentials.png
		[git-instructions]: ./media/web-sites-php-sql-database-deploy-use-git/gitsettings.png
		[linked-resources]: ./media/web-sites-php-sql-database-deploy-use-git/linked_resources.jpg
		[connection-string]: ./media/web-sites-php-sql-database-deploy-use-git/connection_string.jpg
		[management-portal]: https://manage.windowsazure.cn/
		[sql-database-editions]: http://msdn.microsoft.com/zh-cn/library/azure/ee621788.aspx
		[where-is-code]: ./media/web-sites-php-sql-database-deploy-use-git/setupgit.png

reason: ()

