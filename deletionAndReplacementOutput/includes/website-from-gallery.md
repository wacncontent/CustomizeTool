deletion:

deleted:

		[webapps]: ./media/website-from-gallery/selectwebapps.png
		[database]: ./media/website-from-gallery/set-db.png
		[resourcegroup]: ./media/website-from-gallery/show-rg.png
		[browse]: ./media/website-from-gallery/browse-web.png
		[marketplace]: ./media/website-from-gallery/marketplace-icon.png
		[groupname]: ./media/website-from-gallery/set-rg.png

reason: ()

replacement:

deleted:

		The Azure Marketplace makes available a wide range of popular web apps developed by Microsoft, third party companies, and open source software initiatives. Web apps created from the Azure Marketplace do not require installation of any software other than the browser used to connect to the [Azure Preview Portal](https://manage.windowsazure.cn/).

replaced by:

		<!-- not suitable for Mooncake -->
		
		The gallery makes available a wide range of popular web applications developed by Microsoft, third party companies, and open source software initiatives. Web applications created from the gallery do not require installation of any software other than the browser used to connect to the Azure Management Portal.

reason: ()

deleted:

		- How to create a new web app through the Azure Marketplace.
		
		- How to deploy the web app through the Azure Preview Portal.

replaced by:

		- How to create a new site through the gallery.
		
		- How to deploy the site through the Azure Management Portal.

reason: ()

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.
		
		## Create a web app in the portal
		
		1. Log in to the Azure Preview Portal.
		
		2. Open the Azure Marketplace either by clicking the **Marketplace** icon:
		
		    ![Marketplace icon][marketplace]
		
		    Or by clicking the **New** icon on the upper right of the dashboard, and selecting **Marketplace** at the bottow of the list.
			
		    ![Create New][5]
			
		3. Select **Web + Mobile**. Search for **WordPress** and click the **WordPress** icon.
		
			![WordPress from list][7]
			
		5. After reading the description of the WordPress app, select **Create**.
		
		6. Click on **Web app**, and provide the required values for configuring your web app.
			
		    ![configure your app][8]
		
		7. Click on **Database**, and provide the required values for configuring your MySQL database. 
		
		    ![configure database][database]
		
		8. Provide a name for a new resource group.
		
		    ![Set resource group][groupname]
		
		8. If necessary, click **SUBSCRIPTION**, and specify the subscription to use. 
		
		7. When you have finished defining the web app, click **Create**, and wait while the new web app is created.
		
		   When the app has been created, you will see the resource group containing web app and database.
		
		   ![show group][resourcegroup]
		
		## Launch and manage your WordPress web app
			
		1. Click on your new web app to see details about your app.
		
		    ![launch dashboard][10]
		
		2. On the **Essentials** page, click either **Browse** or the link under **Url** to open the web app's welcome page.
		
		    ![site URL][browse]
		
		3. If you have not installed WordPress, enter the appropriate configuration information required by WordPress and click **Install WordPress** to finalize configuration and open the web app's login page.
		
		4. Click **Login** and enter your credentials.  
		
		5. You'll have a new WordPress web app that looks similar to the web app below.    
		
			![your WordPress site][13]
		
		
		
		
		
		
		[5]: ./media/website-from-gallery/start-marketplace.png

replaced by:

		<div class="dev-callout"><strong>Note</strong>
		<p>To complete this tutorial, you need an Azure account. You can create a trial account in just a couple of minutes. For details, see <a href="/pricing/1rmb-trial/" target="_blank">Create an Azure account</a>.</p>
		</div>
		<br />
		
		## Create a website in the portal
		
		1. Login to the [Azure Management Portal](http://manage.windowsazure.cn).
		
		2. Click the **New** icon on the bottom left of the dashboard.
			
			![Create New][5]
		
		3. Click the **Website** icon, and click **From Gallery**.
			
			![Create From Gallery][6]
		
		4. Locate and click the WordPress icon in list, and then click **Next**.
			
			![WordPress from list][7]
		
		5. On the **Configure Your App** page, enter or select values for all fields:
			
		- Enter a URL name of your choice	
		- Leave **Create a new MySQL database** selected in the **Database** field
		- Select the region closest to you
		
			![configure your app][8]
		
		6. Then click **Next**.
		
		7. On the **Create New Database** page, you can specify a name for your new MySQL database or use the default name. Select the region closest to you as the hosting location. Select the box at the bottom of the screen to agree to ClearDB's usage terms for your hosted MySQL database. Then click the check to complete the site creation. 
			
			![create database][9]
		
		After you click **Complete** Azure will initiate build and deploy operations. While the website is being built and deployed the status of these operations is displayed at the bottom of the Websites page. After all operations are performed,  A final status message when the site has been successfully deployed.
		
		## Launch and manage your WordPress site
		
		1. Click on your new site from the **Websites** page to open the dashboard for the site.
		
			![launch dashboard][10]
		
		2. On the **Dashboard** management page, scroll down and click the link on the left under **Site Url** to open the site's welcome page.
		
			![site URL][11] 
		
		3. Enter appropriate configuration information required by WordPress and click **Install WordPress** to finalize configuration and open the website's login page.
		
			![login to WordPress][12]
		
		4. Login to the new WordPress website by entering the username and password that you specified on the **Welcome** page.
		
		5. You'll have a new WordPress site that looks similar to the site below.  
		
			![your WordPress site][13]
		
		
		
		
		
		
		[5]: ./media/website-from-gallery/wordpressgallery-01.png

reason: ()

deleted:

		[7]: ./media/website-from-gallery/search-web-app.png
		[8]: ./media/website-from-gallery/set-web-app.png

replaced by:

		[7]: ./media/website-from-gallery/wordpressgallery-03.png
		[8]: ./media/website-from-gallery/wordpressgallery-04.png

reason: ()

deleted:

		[10]: ./media/website-from-gallery/select-web.png

replaced by:

		[10]: ./media/website-from-gallery/wordpressgallery-06.png
		[11]: ./media/website-from-gallery/wordpressgallery-07.png
		[12]: ./media/website-from-gallery/wordpressgallery-08.png

reason: ()

