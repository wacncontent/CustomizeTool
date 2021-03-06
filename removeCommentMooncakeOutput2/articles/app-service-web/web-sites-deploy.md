<properties
	pageTitle="Deploy a web app in Azure Websites"
	description="Learn what methods are available for deploying content to Web Apps."
	services="app-service"
	documentationCenter=""
	authors="tdykstra"
	manager="wpickett"
	editor="mollybos"/>

<tags
	ms.service="app-service"
	ms.date="08/14/2015"
	wacn.date=""/>

#Deploy a web app in Azure Websites

## Overview

This topic provides a brief overview of the options for deploying your own content to [Azure Websites](/documentation/services/web-sites/). 

The best way to deploy a web app is to set up a [continuous delivery workflow](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/continuous-integration-and-continuous-delivery) integrated with your [source control system](http://asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/source-control). Automation not only makes the development process more efficient but also can make your backup and restore processes more manageable and reliable.

For information about deployment from cloud-hosted source control systems, see the following sections later in this article.

* [Visual Studio Online](#vso)
* [Repository websites using Git](#git)
* [Repository websites using Mercurial](#mercurial)
* [Dropbox](#dropbox)

For information about deployment from on-premises source control systems, see the following sections later in this article.

* [Team Foundation Server (TFS)](#tfs)
* [On-premises Git or Mercurial repositories](#onpremises)

You can also automate deployment by using using command-line tools. For information about deployment by using command-line tools, see the following sections later in this article.

* [MSBuild](#msbuild)
* [FTP tools and scripts](#ftp)
* [Windows PowerShell](#powershell)
* [.NET management API](#api)
* [Azure Command-Line Interface (Azure CLI)](#cli)
* [Web Deploy command line](#webdeploy)
 
Sometimes it is more convenient to deploy from your Integrated Development Environment (IDE). For information about deployment from an IDE, see the following sections later in this article.

* [Visual Studio](#vs)
* [WebMatrix](#webmatrix)

Another deployment option is to use a cloud-based service such as [Octopus Deploy](http://en.wikipedia.org/wiki/Octopus_Deploy). For more information, see [Deploy ASP.NET applications to Azure Web Sites](https://octopusdeploy.com/blog/deploy-aspnet-applications-to-azure-websites).

##<a name="vso"></a>Visual Studio Online

[Visual Studio Online](http://www.visualstudio.com/) (formerly Team Foundation Service) is Microsoft's cloud-based solution for source control and team collaboration. The service is free for a team of up to 5 developers. You can do continuous delivery to a web app in Azure Websites, and your repository can use either [Git or TFVC](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/source-control#gittfs).

##<a name="git"></a>Repository websites using Git

[Git](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/source-control#gittfs) is a popular distributed source control system. Azure has built-in features that make it easy to automate deployment to a web app from popular web-based repository sites that store Git repositories, including [GitHub](http://www.github.com), [CodePlex](http://www.codeplex.com/), and [BitBucket](https://bitbucket.org/). An advantage of using Git to deploy is that it's relatively easy to roll back to an earlier deployment if that ever becomes necessary.

For more information, see the following resources:

* [Publishing from Source Control to Web Apps with Git](/documentation/articles/web-sites-publish-source-control). How to use Git to publish directly from your local computer to Web Apps (in Azure, this method of publishing is called Local Git). Also shows how to enable continuous deployment of Git repositories from GitHub, CodePlex, or BitBucket.
* [Deploying to Web Apps with GitHub using Kudu](http://azure.microsoft.com/documentation/videos/deploying-to-azure-from-github/). Video by Scott Hanselman and David Ebbo that shows how to deploy a web app directly from GitHub to Web Apps.
* [Deploy to Azure Button for Web Apps](http://azure.microsoft.com/blog/2014/11/13/deploy-to-azure-button-for-azure-websites-2/). Blog about a method for triggering deployment from a Git repository.
* [Azure Forum for Git, Mercurial, and Dropbox](http://social.msdn.microsoft.com/Forums/zh-cn/home?forum=windowsazurezhchshome?forum=azuregit).

##<a name="mercurial"></a>Repository websites using Mercurial

If you use [Mercurial](http://mercurial.selenic.com/) as your source control system and store your repository in [CodePlex](http://www.codeplex.com/) or [BitBucket](https://bitbucket.org/), you can use built-in features in Azure Websites to automatically deploy your content.

For information about how to deploy using Mercurial, see the following resources:

* [Publishing from Source Control to Web Apps with Git](/documentation/articles/web-sites-publish-source-control). Although this tutorial shows how to publish a Git repository, the process for Mercurial repositories hosted in CodePlex or BitBucket is similar.
* [Azure Forum for Git, Mercurial, and Dropbox](http://social.msdn.microsoft.com/Forums/zh-cn/home?forum=windowsazurezhchshome?forum=azuregit).

##<a name="vs"></a>Visual Studio

For information about how to deploy to Web Apps from Visual Studio, see the following resources:

* [Get started with Azure and ASP.NET](/documentation/articles/web-sites-dotnet-get-started). How to create and deploy a simple ASP.NET MVC web project by using Visual Studio and Web Deploy.
* [How to Deploy Azure WebJobs using Visual Studio](/documentation/articles/websites-dotnet-deploy-webjobs). How to configure Console Application projects so that they deploy as WebJobs.  
* [Deploy a Secure ASP.NET MVC 5 app with Membership, OAuth, and SQL Database to Web Apps](/documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database). How to create and deploy an ASP.NET MVC web project with a SQL database, by using Visual Studio, Web Deploy, and Entity Framework Code First Migrations.
* [Web Deployment Overview for Visual Studio and ASP.NET](http://msdn.microsoft.com/zh-cn/library/dd394698.aspx). A basic introduction to web deployment using Visual Studio. Dated but includes information that is still relevant, including an overview of options for deploying a database along with the web application and a list of additional deployment tasks you might have to do or manually configure Visual Studio to do for you. This topic is about deployment in general, not just about deployment to Web Apps.
* [ASP.NET Web Deployment using Visual Studio](http://www.asp.net/mvc/tutorials/deployment/visual-studio-web-deployment/introduction). A 12-part tutorial series that covers a more complete range of deployment tasks than the others in this list. Some Azure deployment features have been added since the tutorial was written, but notes added later explain what's missing.
* [Deploying an ASP.NET Website to Azure in Visual Studio 2012 from a Git Repository directly](http://www.dotnetcurry.com/ShowArticle.aspx?ID=881). Explains how to deploy an ASP.NET web project in Visual Studio, using the Git plug-in to commit the code to Git and connecting Azure to the Git repository. Starting in Visual Studio 2013, Git support is built-in an doesn't require installation of a plug-in.

For more information, see the following resources:

* [Create a PHP-MySQL web app and deploy using FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp).

##<a name="tfs"></a>Team Foundation Server (TFS)

Team Foundation Server is Microsoft's on-premises solution for source control and team collaboration. You can set up TFS to do continuous delivery to a web app.

For more information, see the following resource:

* [Continuous Delivery for Cloud Services in Azure](/documentation/articles/cloud-services-dotnet-continuous-delivery). This document is for an Azure Cloud Service, but some of its content is relevant to Web Apps.

##<a name="gitmercurial"></a>On-premises Git or Mercurial repositories

In Azure you can enter the URL of any repository that uses Git or Mercurial in order to deploy from that location. You can also directly push from a local Git repository to a web app.

For more information, see the following resources:

* [Publishing from Source Control to Web Apps with Git](/documentation/articles/web-sites-publish-source-control). How to use Git to publish directly from your local computer to a web app (in Azure, this method of publishing is called Local Git). Also shows how to enable continuous deployment of Git repositories from GitHub, CodePlex, or BitBucket.
* [Publishing to Web Apps from any git/hg repo](http://blog.davidebbo.com/2013/04/publishing-to-azure-web-sites-from-any.html). Blog that explains the "External Repository" feature in Web Apps.
* [Azure Forum for Git, Mercurial, and Dropbox](http://social.msdn.microsoft.com/Forums/zh-cn/home?forum=windowsazurezhchshome?forum=azuregit).
* [Deploying TWO websites to Azure from one Git Repository](http://www.hanselman.com/blog/DeployingTWOWebsitesToWindowsAzureFromOneGitRepository.aspx). Blog post by Scott Hanselman.

##<a name="msbuild"></a>MSBuild

If you use the [Visual Studio IDE](#vs) for development, you can use [MSBuild](http://msbuildbook.com/) to automate anything you can do in your IDE. You can configure MSBuild to use either [Web Deploy](#webdeploy) or [FTP/FTPS](#ftp) to copy files. Web Deploy can also automate many other deployment-related tasks, such as deploying databases.

For more information about command-line deployment using MSBuild, see the following resources:

* [ASP.NET Web Deployment using Visual Studio: Command Line Deployment](http://www.asp.net/mvc/tutorials/deployment/visual-studio-web-deployment/command-line-deployment). Tenth in a series of tutorials about deployment to Azure using Visual Studio. Shows how to use the command line to deploy after setting up publish profiles in Visual Studio.
* [Inside the Microsoft Build Engine: Using MSBuild and Team Foundation Build](http://msbuildbook.com/). Hard-copy book that includes chapters on how to use MSBuild for deployment.

##<a name="ftp"></a>FTP tools and scripts

You can deploy content to your App by using [FTP](http://en.wikipedia.org/wiki/File_Transfer_Protocol) to copy files. It's easy to create FTP credentials for a web app, and you can use them in scripts or in applications that work with FTP, including browsers such as Internet Explorer and full-featured free utilities such as [FileZilla](https://filezilla-project.org/). Web Apps also supports the more secure FTPS protocol.

Although it's easy to copy your web app's files to Azure using FTP utilities, they don't automatically take care of or coordinate related deployment tasks such as deploying a database or changing connection strings. Also, many FTP tools don't compare source and destination files in order to skip copying files that haven't changed. For large Apps, always copying all files can result in long deployment times even for minor updates since all files are always copied.

For more information, see the following resource:

* [Using FTP Batch Scripts](http://support.microsoft.com/kb/96269).

##<a name="powershell"></a>Windows PowerShell

You can perform MSBuild or FTP deployment functions from [Windows PowerShell](http://msdn.microsoft.com/zh-cn/library/dd835506.aspx). If you do that, you can also use a collection of Windows PowerShell cmdlets that make the Azure REST management API easy to call.

For more information, see the following resources:
* [Building Real-World Cloud Apps with Azure - Automate Everything](http://asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/automate-everything). E-book chapter that explains how the sample application shown in the e-book uses Windows PowerShell scripts to create an Azure test environment and deploy to it. See the [Resources](http://asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/automate-everything#resources) section for links to additional Azure PowerShell documentation.
* [Using Windows PowerShell Scripts to Publish to Dev and Test Environments](http://msdn.microsoft.com/zh-cn/library/dn642480.aspx). How to use Windows PowerShell deployment scripts that Visual Studio generates.

##<a name="api"></a>.NET management API

You can write C# code to perform MSBuild or FTP functions for deployment. If you do that, you can access the Azure management REST API to perform site management functions.

For more information, see the following resource:

* [Automating everything with the Azure Management Libraries and .NET](http://www.hanselman.com/blog/PennyPinchingInTheCloudAutomatingEverythingWithTheWindowsAzureManagementLibrariesAndNET.aspx). Introduction to the .NET management API and links to more documentation.

##<a name="cli"></a>Azure Command-Line Interface (Azure CLI)

You can use the command line in Windows, Mac or Linux machines to deploy by using FTP. If you do that, you can also access the Azure REST management API using the Azure CLI.

For more information, see the following resource:

* [Azure Command line tools](/downloads/#cmd-line-tools). Portal page in Azure.com for command line tool information.

##<a name="webdeploy"></a>Web Deploy command line

[Web Deploy](http://www.iis.net/downloads/microsoft/web-deploy) is Microsoft software for deployment to IIS that not only provides intelligent file sync features but also can perform or coordinate many other deployment-related tasks that can't be automated when you use FTP. For example, Web Deploy can deploy a new database or database updates along with your web app. Web Deploy can also minimize the time required to update an existing site since it can intelligently copy only changed files. Microsoft WebMatrix, Visual Studio, Visual Studio Online, and Team Foundation Server have support for Web Deploy built-in, but you can also use Web Deploy directly from the command line to automate deployment. Web Deploy commands are very powerful but the learning curve can be steep.

For more information, see the following resource:

* [Simple Web Apps: Deployment](http://azure.microsoft.com/blog/2014/07/28/simple-azure-websites-deployment/). Blog by David Ebbo about a tool he wrote to make it easier to use Web Deploy.
* [Web Deployment Tool](http://technet.microsoft.com/zh-cn/library/dd568996). Official documentation on the Microsoft TechNet site. Dated but still a good place to start.
* [Using Web Deploy](http://www.iis.net/learn/publish/using-web-deploy). Official documentation on the Microsoft IIS.NET site. Also dated but a good place to start.
* [StackOverflow](http://www.stackoverflow.com). The best place to go for more current information about how to use Web Deploy from the command line.
* [ASP.NET Web Deployment using Visual Studio: Command Line Deployment](http://www.asp.net/mvc/tutorials/deployment/visual-studio-web-deployment/command-line-deployment). MSBuild is the build engine used by Visual Studio, and it can also be used from the command line to deploy web applications to Web Apps. This tutorial is part of a series that is mainly about Visual Studio deployment.

##<a name="nextsteps"></a>Next Steps

In some scenarios you might want to be able to easily switch back and forth between a staging and a production version of your web app. For more information, see [Staged Deployment on Web Apps](/documentation/articles/web-sites-staged-publishing).

Having a backup and restore plan in place is an important part of any deployment workflow. For information about the Web Apps backup and restore feature, see [Web Apps Backups](/documentation/articles/web-sites-backup).  

For information about how to use Azure's Role-Based Access Control to manage access to Web Apps deployment, see [RBAC and Web App Publishing](http://azure.microsoft.com/blog/2015/01/05/rbac-and-azure-websites-publishing).

For information about other deployment topics, see the Deploy section in [Web Apps Documentation](/documentation/services/web-sites/).
 
