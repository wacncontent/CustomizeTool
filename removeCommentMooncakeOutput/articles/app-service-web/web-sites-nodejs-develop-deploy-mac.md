<properties
	pageTitle="Create a Node.js web app in Azure | Windows Azure"
	description="Learn how to deploy a Node.js application to a web app in Azure."
	services="app-service\web"
	documentationCenter="nodejs"
	authors="rmcmurray"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="01/09/2016"
	wacn.date=""/>

# Create a Node.js web app in Azure

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows how to create a simple [Node.js](http://nodejs.org) application and deploy it to a [web app](/home/features/web-site) in [Azure Web App](/documentation/services/web-sites) by using [Git](http://git-scm.com). The instructions in this tutorial can be followed on any operating system that is capable of running Node.js.

You'll learn:

* How to create a web app in Azure by using the Azure Management Portal.
* How to deploy a Node.js application to the web app by pushing to the web app's Git repository.

The completed application writes a short "hello world" string to the browser.

![A browser displaying the 'Hello World' message.][helloworld-completed]

For tutorials and sample code with more complex Node.js applications, or for other topics about how to use Node.js in Azure, see the [Node.js Developer Center](/develop/nodejs/).

> [AZURE.NOTE]
> To complete this tutorial, you need a Windows Azure account. If you don't have an account, you can [sign up for a trial](/pricing/1rmb-trial/?WT.mc_id=A261C142F).

## Create a web app and enable Git publishing

Follow these steps to create a web app in Azure and enable Git publishing. 

[Git](http://git-scm.com/) is a distributed version control system that you can use to deploy your Azure Website. You'll store the code you write for your web app in a local Git repository, and you'll deploy your code to Azure by pushing to a remote repository. This method of deployment is a feature of Azure web apps.  

1. Login to the [Azure Management Portal].

2. Click the **+ NEW** icon on the bottom left of the portal

    ![The Azure Management Portal with the +NEW link highlighted.][portal-new-website]

3. Click **WEBSITE**, then **QUICK CREATE**. Enter a value for **URL** and select the datacenter for your website in the **REGION** dropdown. Click the checkmark at the bottom of the dialog.

    ![The Quick Create dialog][portal-quick-create]

4. Once the website status changes to **Running**, click on the name of the website to access the **Dashboard**

	![Open web site dashboard][go-to-dashboard]

6. At the bottom right of the Quickstart page, select **Set up a deployment from source control**.

	![Set up Git publishing][setup-git-publishing]

6. When asked "Where is your source code?" select **Local Git repository**, and then click the arrow.

	![where is your source code][where-is-code]

7. To enable Git publishing, you must provide a user name and password. If you have previously enabled publishing for an Azure Website, you will not be prompted for the user name or password. Instead, a Git repository will be created using the user name and password you previously specified. Make a note of the user name and password, as they will be used for Git publishing to all Azure Websites you create.

	![The dialog prompting for user name and password.][portal-git-username-password]

8. Once the Git repository is ready, you will be presented with instructions on the Git commands to use in order to setup a local repository and then push the files to Azure.

	![Git deployment instructions returned after creating a repository for the website.][git-instructions]

## Build and test your application locally

In this section, you'll create a **server.js** file that contains a slightly modified version of the 'Hello World' example from [nodejs.org]. The code adds process.env.PORT as the port to listen on when running in an Azure web app.

1. Create a directory named *helloworld*.

2. Use a text editor to create a new file named **server.js** in the *helloworld* directory.

2. Copy the following code into the **server.js** file, and then save the file:

        var http = require('http')
        var port = process.env.PORT || 1337;
        http.createServer(function(req, res) {
          res.writeHead(200, { 'Content-Type': 'text/plain' });
          res.end('Hello World\n');
        }).listen(port);

3. Open the command line, and use the following command to start the web app locally.

        node server.js

4. Open your web browser and navigate to http://localhost:1337. 

	A webpage that displays "Hello World" appears, as shown in the following screenshot.

    ![A browser displaying the 'Hello World' message.][helloworld-localhost]

## Publish your application

1. Install Git if you haven't already done so.

	For installation instructions for your platform, see the [Git download page](http://git-scm.com/download).

1. From the command line, change directories to the **helloworld** directory and enter the following command to initialize a local Git repository.

		git init


2. Use the following commands to add files to the repository:

		git add .
		git commit -m "initial commit"

3. Add a Git remote for pushing updates to the web app that you created previously, by using the following command:

		git remote add azure [URL for remote repository]

4. Push your changes to Azure by using the following command:

		git push azure master

	You are prompted for the password that you created earlier. The output is similar to the following example.

		Counting objects: 3, done.
		Delta compression using up to 8 threads.
		Compressing objects: 100% (2/2), done.
		Writing objects: 100% (3/3), 374 bytes, done.
		Total 3 (delta 0), reused 0 (delta 0)
		remote: New deployment received.
		remote: Updating branch 'master'.
		remote: Preparing deployment for commit id '5ebbe250c9'.
		remote: Preparing files for deployment.
		remote: Deploying Web.config to enable Node.js activation.
		remote: Deployment successful.
		To https://user@testsite.scm.chinacloudsites.cn/testsite.git
		 * [new branch]      master -> master

5. To view your app, click the **Browse** button on the **Web App** part in the Azure Management Portal.

## Publish changes to your application

1. Open the **server.js** file in a text editor, and change 'Hello World\n' to 'Hello Azure\n'. 

2. Save the file.

2. From the command line, change directories to the **helloworld** directory and run the following commands:

		git add .
		git commit -m "changing to hello azure"
		git push azure master

	You are prompted for your password again.

3. Refresh the browser window that you navigated to the web app's URL.

	![A web page displaying 'Hello Azure'][helloworld-completed]
4. You can revert to the previous deployment by selecting it in **Deployments**.

## Next steps

You've deployed a Node.js application to a web app in Azure. To learn more about how Azure web apps run Node.js applications, see [Azure Web Apps: Node.js](http://blogs.msdn.com/b/silverlining/archive/2012/06/14/windows-azure-websites-node-js.aspx) and [Specifying a Node.js version in an Azure application](/documentation/articles/nodejs-specify-node-version-azure-apps).

Node.js provides a rich ecosystem of modules that can be used by your applications. To learn how Web Apps works with modules, see [Using Node.js modules with Azure applications](/documentation/articles/nodejs-use-node-modules-azure-apps).

If you encounter problems with your application after it has been deployed to Azure, see [How to debug a Node.js application in Azure Web App](/documentation/articles/web-sites-nodejs-debug) for information on diagnosing the problem.

This article uses the Azure Management Portal to create a web app. You can also use the [Azure Command-Line Interface](/documentation/articles/xplat-cli-install) or [Azure PowerShell](/documentation/articles/powershell-install-configure) to perform the same operations.

For more information about how to develop Node.js applications on Azure, see the [Node.js Developer Center](/develop/nodejs/).

[Azure Management Portal]: http://manage.windowsazure.cn
[Azure Command-Line Tools for Mac and Linux]: /documentation/articles/xplat-cli-install
[Azure PowerShell]: /documentation/articles/powershell-install-configure
[portal-new- Website]: ./media/web-sites-nodejs-develop-deploy-mac/plus-new.png
[portal-git-username-password]: ./media/web-sites-nodejs-develop-deploy-mac/git-deployment-credentials.png
[git-instructions]: ./media/web-sites-nodejs-develop-deploy-mac/git-instructions.png
[git-deployments-first]: ./media/web-sites-nodejs-develop-deploy-mac/git_deployments_first.png
[git-deployments-second]: ./media/web-sites-nodejs-develop-deploy-mac/git_deployments_second.png
[where-is-code]: ./media/web-sites-nodejs-develop-deploy-mac/where_is_code.png
[helloworld-completed]: ./media/web-sites-nodejs-develop-deploy-mac/helloazure.png
[helloworld-localhost]: ./media/web-sites-nodejs-develop-deploy-mac/helloworldlocal.png
[portal-quick-create]: ./media/web-sites-nodejs-develop-deploy-mac/create-quick-website.png
[portal-quick-create2]: ./media/web-sites-nodejs-develop-deploy-mac/create-quick-website2.png
[setup-git-publishing]: ./media/web-sites-nodejs-develop-deploy-mac/setup_git_publishing.png
[go-to-dashboard]: ./media/web-sites-nodejs-develop-deploy-mac/go_to_dashboard.png
[deployment-part]: ./media/web-sites-nodejs-develop-deploy-mac/deployment-part.png
[deployment-credentials]: ./media/web-sites-nodejs-develop-deploy-mac/deployment-credentials.png
[git-url]: ./media/web-sites-nodejs-develop-deploy-mac/git-url.png
