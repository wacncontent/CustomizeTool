deletion:

deleted:

		from the Azure Marketplace

reason: ()

deleted:

		For more information, see the [Python Developer Center](/develop/python/).
		
		
		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

reason: ()

replacement:

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

replaced by:

		+ [Prerequisites](#prerequisites)
		+ [Website Creation on Portal](#website-creation-on-portal)
		+ [Application Overview](#application-overview)
		+ Website Development
		  + [Windows - Python Tools for Visual Studio](#website-development-windows-ptvs)
		  + [Windows - Command Line](#website-development-windows-command-line)
		  + [Mac/Linux - Command Line](#website-development-mac-linux-command-line)
		+ [Troubleshooting - Deployment](#troubleshooting-deployment)
		+ [Troubleshooting - Package Installation](#troubleshooting-package-installation)
		+ [Troubleshooting - Virtual Environment](#troubleshooting-virtual-environment)
		+ [Troubleshooting - Static Files](#troubleshooting-static-files)
		+ [Troubleshooting - Settings](#troubleshooting-settings)
		+ [Using a Database](#using-a-database)
		+ [Django Admin Interface](#django-admin-interface)
		+ [Next steps](#next-steps)

reason: ()

deleted:

		The first step in creating your app is to create the web app via the [Azure Management Portal](https://manage.windowsazure.cn).
		
		1. Log into the Azure Management Portal and click the **NEW** button in the bottom left corner.
		2. Click **Web + Mobile** > **Azure Marketplace** > **Web Apps**.
		3. In the search box, type "python".
		4. In the search results, select **Django**, then click **Create**.
		5. Configure the new Django app, such as creating a new App Service plan and a new resource group for it. Then, click **Create**.
		6. Configure Git publishing for your newly created web app by following the instructions at [Continuous deployment using GIT in Azure Websites](/documentation/articles/web-sites-publish-source-control).

replaced by:

		The first step in creating your app is to create the web site via the Azure Management Portal.  To do this, you will need to login to the portal and click the NEW button in the bottom left corner. A window will appear. Click **Quick Create**, enter a URL, and select **Create Web Site**.
		
		![](./media/web-sites-python-create-deploy-django-app/django-ws-003.png)
		
		The site will be quickly set up.  Next, you will add support for publishing via Git.  This can be done by choosing **Set up deployment from source control**.
		
		![](./media/web-sites-python-create-deploy-django-app/django-ws-004.png)
		
		From the **Set up deployment** dialog, scroll down and select the **Local Git** option. Click the right arrow to continue.
		
		![](./media/web-sites-python-create-deploy-django-app/django-ws-005.png)
		
		After setting up Git publishing, you will momentarily see a page informing you the repo is being created. When the repo is ready, you will be taken to the deployments tab. The deployments tab includes instructions on how to connect.  
		
		![](./media/web-sites-python-create-deploy-django-app/django-ws-006.png)

reason: ()

deleted:

		the **Application Settings** blade of your web app in the Azure Management Portal

replaced by:

		the site configuration page

reason: ()

deleted:

		the Application Settings blade of your web app in the Azure Management Portal

replaced by:

		the site configuration page

reason: ()

deleted:

		the Application Settings blade of your web app in the Azure Management Portal

replaced by:

		the site configuration page

reason: ()

