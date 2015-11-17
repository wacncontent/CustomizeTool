deletion:

deleted:

		tool

reason: ()

deleted:

		web app in

reason: ()

replacement:

deleted:

		[Azure Websites](/documentation/services/web-sites/) supports continuous deployment to Web Apps from source code control and repository tools like BitBucket, CodePlex, Dropbox, Git, GitHub, Mercurial, and TFS. You can use these tools to maintain the content and code for your application, and then quickly and easily push changes to your Azure web app when you want.
		
		In this article, you will learn how to use Git to publish directly from your local computer to Web Apps (in Azure, this method of publishing is called **Local Git**). You will also learn how to enable continuous deployment from repository sites like BitBucket, CodePlex, Dropbox, GitHub, or Mercurial. For information about using TFS for continuous deployment, see [Continuous delivery to Azure using Visual Studio Online].
		
		> [AZURE.NOTE] Many of the Git commands described in this article are performed automatically when creating a web app using the [Azure Command-Line Tools for Mac and Linux](/develop/nodejs/how-to-guides/command-line-tools/).
		
		## <a id="Step1"></a>Step 1: Installing Git

replaced by:

		# Publish to Azure Websites with Git
		
		Azure Websites supports continuous deployment  from source code control and repository tools like BitBucket, CodePlex, Dropbox, Git, GitHub, Mercurial, and TFS. You can use these tools to maintain the content and code for your website, and then quickly and easily push changes to your site when you want.
		
		In this article, you will learn how to use Git to publish directly from your local computer to an Azure Website (in Azure, this method of publishing is called **Local Git**). You will also learn how to enable continuous deployment from repository websites like BitBucket, CodePlex, Dropbox, GitHub, or Mercurial. For information about using TFS for continuous deployment, see [Continuous delivery to Azure using Visual Studio Online].
		
		> [AZURE.NOTE] Many of the Git commands described in this article are performed automatically when creating a Website using the [Azure Command-Line Tools for Mac and Linux](/documentation/articles/xplat-cli).
		
		The task includes the following steps:
		
		* [Install Git](#Step1)
		* [Create a local repository](#Step2)
		* [Add a web page](#Step3)
		* [Enable the web site repository](#Step4)
		* [Deploy your project](#Step5)
			* [Pushing local files to Azure (Local Git)](#Step6)
			* [Deploy files from a repository web site like BitBucket, CodePlex, Dropbox, GitHub, or  Mercurial](#Step7)
		* [Troubleshooting](#Step8)
		
		## <a id="Step1"></a>Step 1: Install Git

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		Web Apps supports applications created in a variety of programming languages. For this example, you will use a static .html file.

replaced by:

		Azure Websites support applications created in a variety of programming languages. For this example, you will use a static .html file. For information on publishing websites in other programming languages to Azure, see the [Azure Developer Center].

reason: ()

deleted:

		## <a id="Step4"></a>Enable the web app repository
		
		Perform the following steps to enable a Git repository for your web app.
		
		1. Log in to the [Azure preview portal].
		
		2. In your web app's blade, scroll down to the **Deployment** section and click **Set up continous deployment**. Click **Choose Source**, then click **Local Git Repository**, and then click **OK**.  
		
			![Local Git Repository](./media/publishing-with-git/azure1-local-git.png)
		
		4. If this is your first time setting up a repository in Azure, you need to create login credentials for it. You will use them to log into the Azure repository and push changes from your local Git repository. From your web app's blade, click **Settings > Deployment credentials**, then configure your deployment username and password. When you're done, click **OK**.
		
			![](./media/publishing-with-git/azure2-credentials.png)
		
		## <a id="Step5"></a>Deploy your project

replaced by:

		## <a id="Step4"></a>Step 4: Enable the website repository
		
		Perform the following steps to enable a Git repository for your website by using the Azure Management Portal:
		
		1. Login to the [Azure Management Portal].
		
		2. Click the NEW button to create a new website for which you will enable a repository.
		
		2. Wait until the website creation process is finished in the **Websites** view, and then select the website.
		
			![An image displaying a selected web site][portal-select-website]
		
		3. Select the **DASHBOARD** tab.
		
		4. In the **quick glance** section, select **Set up deployment from source control**.  The following **SET UP DEPLOYMENT** dialog appears.
		
			![git-WhereIsYourSourceCode][git-WhereIsYourSourceCode]
		
		4. Choose **Local Git**, and then click the **Next** arrow.
		
		4. If this is your first time setting up a repository in Azure, you need to create login credentials for it. You will use them to log into the Azure repository and push changes from your local Git repository. 
		
			![](./media/publishing-with-git/git_credentials.png)
			
		5. After a short delay, you should be presented with a message that your repository is ready. 
		
			![git-instructions][git-instructions]
		
		## <a id="Step5"></a>Step 5: Deploy your project

reason: ()

deleted:

		Use the following steps to publish your web app to Azure using Local Git.
		
		1. In your web app's blade, in the Deployment section, click **No deployment found**.
		
			![](./media/publishing-with-git/azure3-repo-details.png)
		
			**Git URL** is the remote reference to deploy to from your local repository. You'll use this URL in the following steps.

replaced by:

		### <a id="Step6"></a>Push local files to Azure (Local Git)
		
		At this point, the portal displays instructions for initializing a local repository and adding files. You have already done this in the previous steps in this topic. However, if you have not set up your deployment credentials, you must go back to the **DASHBOARD** tab in the portal and click **Reset your deployment credentials**.
		
		Use the following steps to publish your website to Azure using Local Git:

reason: ()

deleted:

		2. Use `git remote` to add the remote reference listed in **Git URL** from step 1. Your command will look similar to the following:

replaced by:

		2. Copy git remote add command listed in step 3 of the instructions returned by the portal. It will look similar to the following command:

reason: ()

deleted:

		web app's

replaced by:

		Azure Website

reason: ()

deleted:

		web app

replaced by:

		Azure website

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		2. Go back to your web app's blade in the Azure Management Portal. **No deployment found** should be changed to **Active Deployment** with a log entry of your most recent push. 
		
			![](./media/publishing-with-git/azure4-deployed.png)
		
		2. Click the link under **URL** at the top of the web app blade to verify that the **index.html** has been deployed. A page containing 'Hello Git!' will appear.
		
			![A webpage containing 'Hello Git!'][hello-git]

replaced by:

		2. In the portal, click the **BROWSE** link at the bottom of the portal to verify that the **index.html** has been deployed. A page containing 'Hello Git!' will appear.
		
			![A webpage containing 'Hello Git!'][hello-git]

reason: ()

deleted:

		### <a id="Step7"></a>Deploy files from a repository site like BitBucket, CodePlex, Dropbox, GitHub, or Mercurial
		
		Pushing local files to Azure by using Local Git allows you to manually push updates from a local project to your web app in Azure , while deploying from BitBucket, CodePlex, Dropbox, GitHub, or  Mercurial results in a continuous deployment process where Azure will pull in the most recent updates from your project.
		
		While both methods result in your project being deployed to Web Apps, continuous deployment is useful when you have multiple people working on a project and want to ensure that the latest version is always published regardless of who made the most recent update. Continuous deployment is also useful if you are using one of the above mentioned tools as the central repository for your application.

replaced by:

		![A webpage containing 'Yay!'][yay]
		
		### <a id="Step7"></a>Deploy files from a repository website like BitBucket, CodePlex, Dropbox, GitHub, or Mercurial
		
		Pushing local files to Azure by using Local Git allows you to manually push updates from a local project to your  Azure Website, while deploying from BitBucket, CodePlex, Dropbox, GitHub, or  Mercurial results in a continuous deployment process where Azure will pull in the most recent updates from your project.
		
		While both methods result in your project being deployed to an Azure Website, continuous deployment is useful when you have multiple people working on a project and want to ensure that the latest version is always published regardless of who made the most recent update. Continuous deployment is also useful if you are using one of the above mentioned tools as the central repository for your application.

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		2. In your web app's blade in the portal, scroll down to the **Deployment** section and click **Set up continous deployment**. Click **Choose Source**, then click **GitHub**, for example.  
		
			![](./media/publishing-with-git/azure6-setup-github.png)
			
		2. In the **Continous Deployment** blade, click **Authorization**, then click **Authorize**. The Azure Management Portal will redirect you to the repository site to complete the authorization process. 
		
		4. When you're done, go back to the Azure Management Portal and click **OK** in the **Authorization** blade.
		
		5. In the **Continous Deployment** blade, choose the organization, project, and branch you want to deploy from. When you're done, click **OK**.
		  
			![](./media/publishing-with-git/azure7-setup-github-configure.png)

replaced by:

		2. In the Azure Management Portal for your website,  go to the **DASHBOARD** tab. In the **quick glance** section, select **Set up deployment from source control**.  The **Set Up Deployment dialog** appears that asks **Where is your source code?**. 
		
		2. Choose the source control method that you want to use for continuous deployment.
			
		3. When prompted, enter your credentials for the service you selected.
		
		4. After you have authorized Azure to access your account, you will be prompted with a list of repositories. 
		
			![git-ChooseARepositoryToDeploy][git-ChooseARepositoryToDeploy]
		  
		5. Select the repository that you want to associate with your Azure Website. Click the checkmark to continue.

reason: ()

deleted:

		Azure creates an association with the selected repository, and pulls in the files from the specified branch. After this process completes, the **Deployment** section of your web app's blade will show an **Active Deployment** message that indicates deployment has succeeded.
		
		7. At this point your project has been deployed from your repository of choice to your web app. To verify that the web app is active, Click the **URL** at the top of the portal. The browser should navigate to the web app.
		
		8. To verify that continuous deployment is occurring from the repository of your choice, push a change to the repository. Your web app should update to reflect the changes shortly after the push to the repository completes. You can verify that it has pulled in the update in the **Deployments** blade of your web app.

replaced by:

		6. Azure creates an association with the selected repository, and pulls in the files from the master branch. After this process completes, the **deployment history** on the **Deployments** page will show an **Active Deployment** message like the following:
		
			![git-githubdeployed][git-githubdeployed]
		
		7. At this point your project has been deployed from your repository of choice to your Azure website. To verify that the site is active, click the **Browse** link at the bottom of the portal. The browser should navigate to the website.
		
		8. To verify that continuous deployment is occurring, make a change to your project and then push the update to the repository you have associated with this website. Your website should update to reflect the changes shortly after the push to the repository completes. You can verify that it has pulled in the update on the **Deployments** page of your Website.
		
			![git-GitHubDeployed-Updated][git-GitHubDeployed-Updated]

reason: ()

deleted:

		Web Apps in

replaced by:

		an

reason: ()

deleted:

		Websites

replaced by:

		Website

reason: ()

deleted:

		Web Apps

replaced by:

		Azure Websites

reason: ()

deleted:

		Web Apps

replaced by:

		Azure Website

reason: ()

deleted:

		Web Apps

replaced by:

		an Azure Website

reason: ()

deleted:

		Restore](http://docs.nuget.org/Consume/Package-Restore)

replaced by:

		Restore](http://docs.nuget.org/docs/workflows/using-nuget-without-committing-packages)

reason: ()

deleted:

		## Disable continuous deployment
		
		Continuous deployment can be disabled from the **Deployments** blade. From your web app's blade, in the **Deployment** section, click **Active Deployment**. Then click **Disconnect**.
		
		![git-DisconnectFromGitHub](./media/publishing-with-git/azure5-disconnect.png)	
		
		After answering **Yes** to the confirmation message, you can return to your web app's blade and click **Set up continuous deployment** if you would like to set up publishing from another source.

replaced by:

		<h4>How continuous deployment works</h4>
		Continuous deployment works by providing the **DEPLOYMENT TRIGGER URL** found in the **deployments** section of your site's **Configure** tab.
		
		![git-DeploymentTrigger][git-DeploymentTrigger]
		
		When updates are made to your repository, a POST request is sent to this URL, which notifies your Azure Website that the repository has been updated. At this point it retrieves the update and deploys it to your website.
		
		For more information on the engine behind the Git deployment process for Azure Websites, see [Project Kudu](https://github.com/projectkudu/kudu/wiki).
		
		<h4>Specifying the branch to use</h4>
		
		When you enable continuous deployment, it will default to the **master** branch of the repository. If you want to use a different branch, perform the following steps:
		
		1. In the portal, select your website and then select **CONFIGURE**.
		
		2. In the **deployments** section of the page, enter the branch you wish to use in the **BRANCH TO DEPLOY** field, and then hit enter. Finally, click **SAVE**.
		
			Azure should immediately begin updating based on changes to the new branch.
		
		#### Disabling continuous deployment
		
		Continuous deployment can be disabled from the Azure **Dashboard**. Under the **quick glance** section, choose the option to disconnect from the repository that you are using:
		
		![git-DisconnectFromGitHub][git-DisconnectFromGitHub]	
		
		After answering **Yes** to the confirmation message, you can return to **quick glance** and click **Set up deployment from source control** if you would like to set up publishing from another source.

reason: ()

deleted:

		a web app in

replaced by:

		an

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		web app

replaced by:

		website

reason: ()

deleted:

		**Symptom**: Error - Changes committed to remote repository but your web app not updated.

replaced by:

		**Symptom**: Error - Changes commited to remote repository but your website not updated.

reason: ()

deleted:

		>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.
		
		## What's changed
		* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
		* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)
		
		[Azure Developer Center]: /develop/overview/
		[Azure preview portal]: https://manage.windowsazure.cn

replaced by:

		[Azure Developer Center]: /zh-cn/documentation/
		[Azure Management Portal]: http://manage.windowsazure.cn

reason: ()

deleted:

		/documentation/articles/xplat-cli-install

replaced by:

		/documentation/articles/xplat-cli

reason: ()

deleted:

		/documentation/articles/cloud-services-continuous-delivery-use-vso

replaced by:

		/documentation/articles/cloud-services-continuous-delivery-use-vso/

reason: ()

