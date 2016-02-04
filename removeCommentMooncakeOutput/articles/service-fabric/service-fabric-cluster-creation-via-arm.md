<properties
   pageTitle="Setting up a Service Fabric Cluster using an ARM Template | Windows Azure"
   description="Setting up a Service Fabric Cluster using an ARM Template."
   services="service-fabric"
   documentationCenter=".net"
   authors="ChackDan"
   manager="timlt"
   editor=""/>

<tags
	ms.service="service-fabric"
	ms.date="11/19/2015"
	wacn.date=""/>

# Setting up a Service Fabric Cluster using an ARM Template

This page helps you with setting up of a Service Fabric Cluster using an ARM template. It is assumed that your subscription has enough cores to deploy the IaaS VMs that will make up this cluster

## Prerequisites

- If you want to set up a secure cluster, make sure to have uploaded an X509 certificate to your key vault. you will need the Source Vault URL, Certificate URL and the Certificate thumbprint.
-  Refer to [Service Fabric Cluster security](/documentation/articles/service-fabric-cluster-security) for more details on how to.

## Acquiring a sample ARM template

1. Sample ARM templates are available at [Azure quick start template Gallery on github ](https://github.com/Azure/azure-quickstart-templates). All the service fabric templates start with the name "service-fabric.." . you can either search the repository for "fabric" or just scroll down to the set of sample templates.
2. In order to help quickly find what you may be looking for, the templates have been named as follows
	1. [service-fabric-unsecure-cluster-5-node-1-nodetype](http://go.microsoft.com/fwlink/?LinkId=716923) to indicate a 5 node single node unsecure cluster template. 
	3. [service-fabric-secure-cluster-5-node-1-nodetype-wad](http://go.microsoft.com/fwlink/?LinkID=716924) to indicate a 5 node single node secure cluster template that is WAD enabled. 
	4. [service-fabric-secure-cluster-10-node-2-nodetype-wad](http://go.microsoft.com/fwlink/?LinkId=716925) to indicate a 10 node two node secure cluster template that is WAD enabled. 
	

## Creating a custom ARM template

2. You have two choices here 
	1. You can acquire a sample template from [Azure quick start template Gallery on github ](https://github.com/Azure/azure-quickstart-templates) and make changes to it.
	2. Log into the Azure Management Portal and use the service fabric portal pages to generate the template for you to customize. The process to do so is described below.
3. Log on to the Azure Management Portal [http://aka.ms/servicefabricportal](http://aka.ms/servicefabricportal).
2. Go through the process of creating the cluster as described in [Creating Service Fabric Cluster via portal](/documentation/articles/service-fabric-cluster-creation-via-portal) , but do not click on ***create**, instead go to Summary and download the template.

 ![DownloadTemplate][DownloadTemplate]

## Deploying the ARM template to Azure using Azure PS

Refer to [Deploying ARM templates using PS ](/documentation/articles/resource-group-template-deploy) for detailed guidance on how to deploy the template using PowerShell.

<!--Every topic should have next steps and links to the next logical set of content to keep the customer engaged-->
## Next steps
- [Service Fabric Cluster security](/documentation/articles/service-fabric-cluster-security) 
- [Managing your Service Fabric applications in Visual Studio](/documentation/articles/service-fabric-manage-application-in-visual-studio).
- [Service Fabric Health model introduction](/documentation/articles/service-fabric-health-introduction)

<!--Image references-->
[DownloadTemplate]: ./media/service-fabric-cluster-creation-via-arm/DownloadTemplate.png

