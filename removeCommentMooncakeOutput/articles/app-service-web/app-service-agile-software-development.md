<properties
	pageTitle="Agile software development with Azure Web App"
	description="Learn how to create high-scale complex applications with Azure in a way that supports agile software development."
	services="app-service"
	documentationCenter=""
	authors="cephalin"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="01/07/2016"
	wacn.date=""/>


# Agile software development with Azure #

In this tutorial, you will learn how to create high-scale complex applications with [Azure Web App](/home/features/web-site/) in a way that supports [agile software development](https://en.wikipedia.org/wiki/Agile_software_development).

Limitations in technical processes can often stand in the way of successful implementation of agile methodologies. Azure with features such as [continuous publishing](/documentation/articles/web-sites-publish-source-control/), [staging environments](/documentation/articles/web-sites-staged-publishing/) (slots), and [monitoring](/documentation/articles/web-sites-monitor/), when coupled wisely with the orchestration and management of deployment in [Azure Resource Manager](/documentation/articles/resource-group-overview/), can be part of a great solution for developers who embrace agile software development.

The following table is a short list of requirements associated with agile development, and how Azure services enables each of them.

| Requirement | How Azure enables |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - Make builds self-testing | Load tests, web tests, etc., can be deployed with the Azure Resource Manager template.|
| - Perform tests in a clone of production environment | Azure Resource Manager templates can be used to create clones of the Azure production environment (including app settings, connection string templates, scaling, etc.) for testing quickly and predictably.|

## What you will do ##

You will walk through a typical dev-test-stage-production workflow in order to publish new changes to the [ToDoApp](https://github.com/azure-appservice-samples/ToDoApp) sample application, which consists of two [web apps](/home/features/web-site/), one being a frontend (FE) and the other being a Web API backend (BE), and a [SQL database](/home/features/sql-database/). You will work with the deployment architecture shown below:

![](./media/app-service-agile-software-development/what-1-architecture.png)

To put the picture into words :

-	The deployment architecture is separated into three distinct environments (or [resource groups](/documentation/articles/resource-group-overview/) in Azure), each with its own App Service plan, [scaling](/documentation/articles/web-sites-scale/) settings, and SQL database.
-	Each environment can be managed separately. They can even exist in different subscriptions.
-	Staging and production are implemented as two slots of the same Azure Web App.
-	When a commit to master branch is verified on the staging slot (with production data), the verified staging app is swapped into the production slot [with no downtime](/documentation/articles/web-sites-staged-publishing/).

The production and staging environment is defined by the template at [*&lt;repository_root>*/ARMTemplates/ProdandStage.json](https://github.com/azure-appservice-samples/ToDoApp/blob/master/ARMTemplates/ProdAndStage.json).

The dev and test environments are defined by the template at [*&lt;repository_root>*/ARMTemplates/Dev.json](https://github.com/azure-appservice-samples/ToDoApp/blob/master/ARMTemplates/Dev.json).

You will also use the typical branching strategy, with code moving from the dev branch up to the test branch, then to the master branch (moving up in quality, so to speak).

![](./media/app-service-agile-software-development/what-2-branches.png) 

## What you will need ##

-	An Azure account
-	A [GitHub](https://github.com/) account
-	Git Shell (installed with [GitHub for Windows](https://windows.github.com/)) - this enables you to run both the Git and PowerShell commands in the same session 
-	Latest [Azure PowerShell](https://github.com/Azure/azure-powershell/releases/download/0.9.4-June2015/azure-powershell.0.9.4.msi) bits
	
	>[AZURE.NOTE] If you are using Auzre PowerShell 1.0 or greater, you need to do a lot of modification to "deploy.ps1".
	> <p>1. You need to delete all `Switch-AzureMode` command.
	> <p>2. Replace `Get-AzureResource` by `Get-AzureRmResource`, and delete the `-OutputObjectFormat` parameter
	> <p>3. Decomposite `New-AzureResourceGroup` into `New-AzureRmResourceGroup` and `New-AzureRmResourceGroupDeployment`, i.e. `New-AzureRmResourceGroup -Name $RG_Name -Location $RG_Location` and `New-AzureRmResourceGroupDeployment -Verbose -name $RG_Name -ResourceGroupName $RG_Name -TemplateFile ".\$TemplateFile" -TemplateParameterFile ".\temp.json" -ErrorAction Stop`

-	Basic understanding of the following:
	-	[Azure Resource Manager](/documentation/articles/resource-group-overview/) template deployment
	-	[Git](http://git-scm.com/documentation)
	-	[PowerShell](https://technet.microsoft.com/zh-cn/library/bb978526.aspx)

> [AZURE.NOTE] You need an Azure account to complete this tutorial:
> + You can [open an trial Azure account](/pricing/1rmb-trial/) - You get credits you can use to try out paid Azure services, and even after they're used up you can keep the account and use free Azure services, such as Web Apps.

## Set up your production environment ##

In a typical DevOps scenario, you have an application that's running live in Azure, and you want to make changes to it. In this scenario, you have a template that you developed, tested, and used to deploy the production environment. You will set it up in this section.

1.	Create your own fork of the [ToDoApp](https://github.com/azure-appservice-samples/ToDoApp) repository. For information on creating your fork, see [Fork a Repo](https://help.github.com/articles/fork-a-repo/). Once your fork is created, you can see it in your browser.
 
	![](./media/app-service-agile-software-development/production-1-private-repo.png)

2.	Open a Git Shell session. If you don't have Git Shell yet, install [GitHub for Windows](https://windows.github.com/) now.

3.	Create a local clone of your fork by executing the following command:

		git clone https://github.com/<your_fork>/ToDoApp.git 

4.	Once you have your local clone, navigate to *&lt;repository_root>*\ARMTemplates, and run the deploy.ps1 script as follows:

		.\deploy.ps1 -RepoUrl https://github.com/<your_fork>/todoapp.git

	>[AZURE.NOTE] Before you can use these templates, you need to do the following edition, in order to fit in the Azure China Cloud environment:
	> <p>1. Open file "ProdAndStage.json", and search for "sourcecontrols".
	> <p>2. Inside the block and fater `"branch": "[parameters('branch')]"`, add `"IsManualIntegration": true`
	> <p>3. Replace "China North" or "China East" by "China East" or "China North" in both "ProdAndStage.json", and "deploy.ps1"
	> <p>Since, Azure Web App is not manageable by Ibiza Portal in Azure China yet, it's not possible for us to setup GitHub credentials.

4.	When prompted, type in the desired username and password for database access.

	You should see the provisioning progress of various Azure resources. When deployment completes, the script will launch the application in the browser and give you a friendly beep.

	![](./media/app-service-agile-software-development/production-2-app-in-browser.png)
 
	>[AZURE.TIP] Take a look at *&lt;repository_root>*\ARMTemplates\Deploy.ps1, to see how it generates resources with unique IDs. You can use the same approach to create clones of the same deployment without worrying about conflicting resource names.
 
6.	Back in your Git Shell session, run:

		.\swap -Name ToDoApp<unique_string>master

	![](./media/app-service-agile-software-development/production-4-swap.png)

	>[AZURE.NOTE] For Azure PowerShell 1.0 and greater, delete all `Switch-AzureMode` command in "swap.ps1".

7.	When the script finishes, go back to browse to the frontend's address (http://ToDoApp*&lt;unique_string>*master.chinacloudsites.cn/) to see the application running in production.
 
5.	Log into the [Azure Classic Management Portal](https://manage.windowsazure.cn/) and take a look at what's created.

	You should be able to see two web apps, one with the `Api` suffix in the name. you will also see the SQL Database and server, the App Service plan, and the staging slots for the web apps. Browse through the different resources and compare them with *&lt;repository_root>*\ARMTemplates\ProdAndStage.json to see how they are configured in the template.

You have now set up the production environment. Next, you will kick off a new update to the application.

## Create dev and test branches ##

Now that you have a complex application running in production in Azure, you will make an update to your application in accordance with agile methodology. In this section, you will create the dev and test branches that you will need to make the required updates.

1.	Create the test environment first. In your Git Shell session, run the following commands to create the environment for a new branch called **NewUpdate**. 

		git checkout -b NewUpdate
		git push origin NewUpdate 
		.\deploy.ps1 -TemplateFile .\Dev.json -RepoUrl https://github.com/<your_fork>/ToDoApp.git -Branch NewUpdate

	>[AZURE.NOTE] You should do the same modification to "Dev.json" as what you have done to "ProdAndStage.json" 

1.	When prompted, type in the desired username and password for database access. 

	When deployment completes, the script will launch the application in the browser and give you a friendly beep. And just like that, you now have a new branch with its own test environment. Take a moment to review a few things about this test environment:

	-	You can create it in any Azure subscription. That means the production environment can be managed separately from your test environment.
	-	Your test environment is running live in Azure.
	-	Your test environment is identical to the production environment, except for the staging slots and the scaling settings. You can know this because these are the only differences between ProdandStage.json and Dev.json.
	-	You can manage your test environment in its own App Service plan, with a different price tier (such as **Free**).
	-	Deleting this test environment will be as simple as deleting the resource group. You will find out how to do this [later](#delete).

2.	Go on to create a dev branch by running the following commands:

		git checkout -b Dev
		git push origin Dev
		.\deploy.ps1 -TemplateFile .\Dev.json -RepoUrl https://github.com/<your_fork>/ToDoApp.git -Branch Dev

3.	When prompted, type in the desired username and password for database access. 

	Take a moment to review a few things about this dev environment: 

	-	Your dev environment has a configuration identical to the test environment because it's deployed using the same template.
	-	Each dev environment can be created in the developer's own Azure subscription, leaving the test environment to be separately managed.
	-	Your dev environment is running live in Azure.
	-	Deleting the dev environment is as simple as deleting the resource group. You will find out how to do this [later](#delete).

>[AZURE.NOTE] When you have multiple developers working on the new update, each of them can easily create a branch and dedicated dev environment by doing the following:
><p>1.	Create their own fork of the repository in GitHub (see [Fork a Repo](https://help.github.com/articles/fork-a-repo/)).
><p>2.	Clone the fork on their local machine
><p>3.	Run the same commands to create their own dev branch and environment.

When you're done, your GitHub fork should have three branches:

![](./media/app-service-agile-software-development/test-1-github-view.png)

And you should have six web sites (three sets of two) in [Azure Classic Management Portal](https://manage.windowsazure.cn):
 
>[AZURE.NOTE] Note that ProdandStage.json specifies the production environment to use the **Standard** pricing tier, which is appropriate for scalability of the production application.


## Merge code into test environment ##

When you're ready to push your code from Dev branch up to NewUpdate branch, it's the standard git process:

1.	Merge any new commits to NewUpdate into the Dev branch in GitHub, such as commits created by other developers. Any new commit on GitHub will trigger a code push and build in the dev environment. You can then make sure your code in Dev branch still works with the latest bits from NewUpdate branch.

2.	Merge all your new commits from Dev branch into NewUpdate branch on GitHub. This action triggers a code push and build in the test environment. 

Now, let's push your code to **NewUpdate** branch. In Git Shell, run the following commands:

	git checkout NewUpdate
	git pull origin NewUpdate
	git merge Dev
	git push origin NewUpdate

That's it! 

Go to the web app blade for your test environment to see your new commit (merged into NewUpdate branch) now pushed to the test environment. Then, click **Browse** to see that the style change is now running live in Azure.

## Deploy update to production ##

Pushing code to the staging and production environment should feel no different than what you've already done when you pushed code to the test environment. It's really that simple. 

In Git Shell, run the following commands:

	git checkout master
	git pull origin master
	git merge NewUpdate
	git push origin master

Remember that based on the way the staging and production environment is setup in ProdandStage.json, your new code is pushed to the **Staging** slot and is running there. So if you navigate to the staging slot's URL, you'll see the new code running there. To do this, run the `Show-AzureWebsite` cmdlet in Git Shell.

	Show-AzureWebsite -Name ToDoApp<unique_string>master -Slot Staging
 
And now, after you've verified the update in the staging slot, the only thing left to do is to swap it into production. In Git Shell, just run the following commands:

	cd <repository_root>\ARMTemplates
	.\swap.ps1 -Name ToDoApp<unique_string>master

Congratulations! You've successfully published a new update to your production web application. What's more is that you've just done it by easily creating dev and test environments, and building and testing every commit. These are crucial building blocks for agile software development.

<a name="delete"></a>
## Delete dev and test enviroments ##

Because you have purposely architected your dev and test environments to be self-contained resource groups, it is very easy to delete them. To delete the ones you created in this tutorial, both the GitHub branches and Azure artifacts, just run the following commands in Git Shell:

	git branch -d Dev
	git push origin :Dev
	git branch -d NewUpdate
	git push origin :NewUpdate
	Remove-AzureRmResourceGroup -Name ToDoApp<unique_string>dev-group -Force -Verbose
	Remove-AzureRmResourceGroup -Name ToDoApp<unique_string>newupdate-group -Force -Verbose

## Summary ##

Agile software development is a must-have for many companies who want to adopt Azure as their application platform. In this tutorial, you have learned how to create and tear down exact replicas or near replicas of the production environment with ease, even for complex applications. You have also learned how to leverage this ability to create a development process that can build and test every single commit in Azure. This tutorial has hopefully shown you how you can best use Azure and Azure Resource Manager together to create a DevOps solution that caters to agile methodologies. Next, you can build on this scenario by performing advanced DevOps techniques such as [testing in production](/documentation/articles/app-service-web-test-in-production-get-start/). For a common testing-in-production scenario, see [Flighting deployment (beta testing) in Azure Web App](/documentation/articles/app-service-web-test-in-production-controlled-test-flight/).

## More resources ##

-	[Agile Development in Practice: Tips and Tricks for Modernized Development Cycle](http://channel9.msdn.com/Events/Ignite/2015/BRK3707)
-	[Advanced deployment strategies for Azure Web Apps using Resource Manager templates](http://channel9.msdn.com/Events/Build/2015/2-620)
-	[Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates/)
-	[JSONLint - The JSON Validator](http://jsonlint.com/)
-	[ARMClient - Set up GitHub publishing to site](https://github.com/projectKudu/ARMClient/wiki/Setup-GitHub-publishing-to-Site)
-	[Git Branching - Basic Branching and Merging](http://www.git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
-	[David Ebbo's Blog](http://blog.davidebbo.com/)
-	[Azure PowerShell](/documentation/articles/powershell-install-configure/)
-	[Azure Cross-Platform Command-Line Tools](/documentation/articles/xplat-cli-install/)
-	[Create or edit users in Azure AD](https://msdn.microsoft.com/zh-cn/library/azure/hh967632.aspx#BKMK_1)
