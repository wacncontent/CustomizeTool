<properties
    pageTitle="Azure Virtual Machine DotNet Core Tutorial 1 | Azure"
    description="Azure Virtual Machine DotNet Core Tutorial"
    services="virtual-machines-windows"
    documentationcenter="virtual-machines"
    author="neilpeterson"
    manager="timlt"
    editor="tysonn"
    tags="azure-resource-manager" />
<tags
    ms.assetid="14d5f250-1f76-49d4-898f-07b58fd39e7c"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="infrastructure-services"
    ms.date="11/21/2016"
    wacn.date=""
    ms.author="nepeters" />

# Automating application deployments to Azure Virtual Machines
This four-part series details deploying and configuring Azure resource and applications using Azure Resource Manage templates. In this series, a sample template is deployed and the deployment template examined. The goal of this series is to educate on the relationship between Azure resources, and to provide hands on experience deploying fully integrated Azure Resource Manager templates. This document assumes a basic level of knowledge with Azure Resource Manager, before starting this tutorial familiarize yourself with basic Azure Resource Manager concepts.

## Music store application
The sample used in this series is a .Net Core application simulating a Music Store shopping experience. This application can be deployed to either a Linux or Windows virtual system, sample deployments have been created for both. The application includes a web application and a SQL database. Before reading the articles in this series, deploy the application using the deployment button found on this page. When fully deployed, the application / Azure architecture looks like the following diagram. 

The Music Store Resource Manager template can be found here, [Music Store Windows Template](https://github.com/Microsoft/dotnet-core-sample-templates/tree/master/dotnet-core-music-windows)

![Music Store Application](./media/virtual-machines-windows-dotnet-core/music-store.png)

Each of these components, including the associate template JSON is examined in the following four articles.

* [**Application Architecture**](/documentation/articles/virtual-machines-windows-dotnet-core-2-architecture/) - Application components such as web sites and databases need to be hosted on Azure computer resources such as virtual machines and Azure SQL databases. This document walks through mapping compute need, to Azure resources, and deploying these resources with an Azure Resource Manager template. 
* [**Access and Security**](/documentation/articles/virtual-machines-windows-dotnet-core-3-access-security/) - When hosting applications in Azure, it is necessary to consider how the application is accessed, and how different application components access each other. This document details providing and securing internet access to an application and access between application components.
* [**Availability and Scale**](/documentation/articles/virtual-machines-windows-dotnet-core-4-availability-scale/) - Availability and scale refer to the applications ability to stay running during infrastructure downtime, and the ability to scale compute resources to meet application demand. This document details the components needed to deploy a load balanced and highly available application.
* [**Application Deployment**](/documentation/articles/virtual-machines-windows-dotnet-core-5-app-deployment/) - When deploying applications onto Azure Virtual Machines, the method by which the application binaries are installed on the Virtual Machine must be considered. This document details automating application installation using Azure Virtual Machine Custom Script Extensions.

The goal when developing Azure Resource Manager templates is to automate the deployment of Azure Infrastructure, and the installation and configuration of any applications being hosted on this Azure infrastructure. Working through these articles provides an example of this experience.

## Deploy the music store application
The Music Store application can be deployed using this button.

<a href="https://portal.azure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FMicrosoft%2Fdotnet-core-sample-templates%2Fmaster%2Fdotnet-core-music-windows%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

The Azure Resource Manager template requires the following parameter values.

| Parameter Name | Description |
| --- | --- |
| ADMINUSERNAME |Admin user name that is used on the virtual machine and the Azure SQL Database. |
| ADMINPASSWORD |Password that is used on the Azure Virtual Machine and SQL Database. |
| NUMBEROFINSTANCES |The number of virtual machines to be created. Each of these virtual machines host the Music Store web application, and all traffic is load balanced across them. |
| PUBLICIPADDRESSDNSNAME |Globally unique DNS name associated with the Public IP address. |

When the template deployment has completed, browse to the public IP Address using any internet browser. The .Net Core Music site will be presented.

## Next steps
<hr>

[Step 1 - Application Architecture with Azure Resource Manager Templates](/documentation/articles/virtual-machines-windows-dotnet-core-2-architecture/)

[Step 2 - Access and Security in Azure Resource Manager Templates](/documentation/articles/virtual-machines-windows-dotnet-core-3-access-security/)

[Step 3 - Availability and Scale in Azure Resource Manager Templates](/documentation/articles/virtual-machines-windows-dotnet-core-4-availability-scale/)

[Step 4 - Application Deployment with Azure Resource Manager Templates](/documentation/articles/virtual-machines-windows-dotnet-core-5-app-deployment/)

