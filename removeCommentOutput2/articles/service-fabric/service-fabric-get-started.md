<properties
   pageTitle="Set up your development environment | Windows Azure"
   description="Install the runtime, SDK, and tools and create a local development cluster. After completing this setup, you will be ready to build applications."
   services="service-fabric"
   documentationCenter=".net"
   authors="seanmck"
   manager="timlt"
   editor=""/>

<tags
	ms.service="service-fabric"
	ms.date="11/17/2015"
	wacn.date=""/>

# Set up your Service Fabric development environment
 This article covers everything you need to start building [Service Fabric][1] apps, including installing the runtime, SDK, tools, and setting up a local cluster.

 > [AZURE.NOTE] These instructions are intended for setting up new PCs. If you have installed a previous version of Service Fabric on your PC, please follow the [instructions to update your development environment ](/documentation/articles/service-fabric-update-your-development-environment).

## Prerequisites
### Supported Operating System versions
The following operating system versions are supported:

- Windows 8/8.1
- Windows Server 2012 R2
- Windows 10

### Visual Studio 2015

The tools for Service Fabric depend on Visual Studio 2015, which you can find [here][2].

> [AZURE.NOTE] If you aren't running one of the supported OS versions or would prefer not to install Visual Studio 2015 on your PC, you can set up an Azure virtual machine with Windows Server 2012 R2 and Visual Studio 2015 pre-installed using an image from the VM Gallery.

## Install the runtime, SDK, and tools

Installation of the Service Fabric components is done by the Web Platform Installer. Follow these instructions to install:

1. [Download the SDK][3] using the Web Platform Installer.

2. Click **Install** to begin the install process.

3. Review and accept the EULA.

Installation will proceed automatically.

## Enable PowerShell script execution

Service Fabric uses Windows PowerShell scripts for creating a local development cluster and for deploying applications from Visual Studio. By default, Windows will block these scripts from running. To enable them, you must modify your PowerShell execution policy. Open PowerShell as an administrator and enter the following command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force -Scope CurrentUser
```

## Next steps
Now that your development environment is set up, you can start building and running apps.

- [Create your first Service Fabric application in Visual Studio](/documentation/articles/service-fabric-create-your-first-application-in-visual-studio)
- [Learn how to deploy and manage applications on your local cluster](/documentation/articles/service-fabric-get-started-with-a-local-cluster)
- [Learn about the programming models: Reliable Actors and Reliable Services](/documentation/articles/service-fabric-choose-framework)
- [Check out the Service Fabric samples on GitHub](https://aka.ms/servicefabricsamples)
- [Visualize your cluster using Service Fabric Explorer](/documentation/articles/service-fabric-visualizing-your-cluster)

[1]: http://azure.microsoft.com/campaigns/service-fabric/ "Service Fabric campaign page"
[2]: http://go.microsoft.com/fwlink/?LinkId=517106 "VS RC"
[3]:http://www.microsoft.com/web/handlers/webpi.ashx?command=getinstallerredirect&appid=MicrosoftAzure-ServiceFabric "WebPI link"
