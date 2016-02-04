<properties 
	pageTitle="Use Azure preview portal to manage Azure resources | Windows Azure" 
	description="Group multiple resources as a logical group that becomes the lifecycle boundary for resources contained within it." 
	services="azure-resource-manager,azure-portal" 
	documentationCenter="" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="azure-resource-manager"
	ms.date="11/11/2015"
	wacn.date=""/>


# Using the Azure <!-- deleted by customization Preview --><!-- keep by customization: begin --> Management <!-- keep by customization: end --> Portal to manage your Azure resources

## Introduction

<!-- deleted by customization
Historically, managing a resource (such as a database server, database, or web site) in Windows Azure required you to perform operations against one resource at a time. If you had a complex application made up of multiple resources, you had to manually coordinate changes to the application infrastructure. In the Azure preview portal, you can utilize Azure Resource Manager to create resource groups to deploy and manage all the resources in an application together.

Typically, a resource group contains resources related to a specific application. For example, a group may contain a web site that hosts your public website, a SQL Database that stores relational data used by the site, and a Storage account that stores non-relational assets. Every resource in a resource group should share the same lifecycle. For more information about Resource Manager, see [Resource Manager overview](/documentation/articles/resource-group-overview).

This topic provides an overview of how to use resource groups within the Azure preview portal. Currently, not every service supports the preview portal or Resource Manager. For those services, you will need to use the [portal](https://manage.windowsazure.cn). For the status of each service, see [Resource Manager support for services, regions, and API versions](/documentation/articles/resource-manager-supported-services)

## Create resource group and resources

If you need to create an empty resource group, you can select **New**, **Management**, and **Resource Group**.

![create empty resource group](./media/resource-group-portal/create-empty-group.png)

You give it a name and location, and, if necessary, select a subscription.

![set group values](./media/resource-group-portal/set-group-properties.png)

However, you do not need to explicitly create an empty resource group. When creating a new resource, you can choose to either create a new resource group or use an existing resource group. The following image shows how to create a new web site with the option of selecting an existing resource group or creating a new one. 

![create resource group](./media/resource-group-portal/select-existing-group.png)

## Browse resource groups

You can browse all resource groups by clicking the **Browse All** and **Resource groups**. 

![browse resource groups](./media/resource-group-portal/browse-groups.png)

When you select a particular resource group, you see a resource group blade that gives you information about that resource group, including a list of all of the resources in the group.

![resource group summary](./media/resource-group-portal/group-summary.png)

The resource group blade also gives you a unified view of your billing and monitoring information for all the resources in the resource group.

![monitoring and billing](./media/resource-group-portal/monitoring-billing.png)

## Customizing the interface

For quick access to the resource group summary, you can pin the blade to your Startboard.

![pin resource group](./media/resource-group-portal/pin-group.png)

Or, you can pin a section of the blade to your Startboard by selecting the ellipsis (...) above the section. You can also customize the size the section in the blade or remove it completely. The following image shows how to pin, customize, or remove the Events section.

![pin section](./media/resource-group-portal/pin-section.png)

After pinning the Events section to the Startboard, you will see a summary of events on the Startboard.

![events startboard](./media/resource-group-portal/events-startboard.png)

And, selecting it immediately takes you to more details about the events.

## Viewing past deployments

From within the resource group blade, you can see the date and status of the last deployment for this resource group. Selecting the link, displays a history of deployments for the group.

![last deployment](./media/resource-group-portal/last-deployment.png)

Selecting any deployment from the history shows details about that deployment.

![deployment summary](./media/resource-group-portal/deployment-summary.png)

You can see the individual operations that were executed during the deployment. The following image shows one operation that succeeded and one that failed.

![operation details](./media/resource-group-portal/operation-details.png) 

Selecting any of the operations shows more details about the operation. This can be especially helpful when an operation has failed, as shown below. It can help you troubleshoot why a deployment failed. In the following image, you can see that the web site was not deployed because the name was not unique.

![operation message](./media/resource-group-portal/operation-message.png)

## Viewing audit logs

The audit log contains not just deployment operations, but all management operations taken on resources in your subscription. For example, you can see in the audit logs when someone in your organization stopped an app. To see the audit logs, select **Browse All** and **Audit Logs**.

![browse audit logs](./media/resource-group-portal/browse-audit-logs.png)

In the operations section, you can see the individual operations that have been performed across your subscription.

![view audit log](./media/resource-group-portal/view-audit-log.png)

By selecting any of the operations, you can see greater details, including which user executed the operation.

You can filter what is shown in the audit log, by selecting **Filter**.

![filter log](./media/resource-group-portal/filter-logs.png)

You can select what type of operations to show, such belonging to a resource group or resource, within a specified time span, initiated by a particular caller, or the levels of operation.

![filter options](./media/resource-group-portal/filter-options.png)  
-->
<!-- keep by customization: begin -->
Historically, managing a resource (a user-managed entity such as a database server, database, or website) in Windows Azure required you to perform operations against one resource at a time. If you had a complex application made up of multiple resources, management of this application became a complex task. In the Azure Management Portal you can create resource groups to manage all your resources in an application together. Resource group is a new concept in Azure that serves as the lifecycle boundary for every resource contained within it.

Resource groups enable you to manage all your resources in an application together. Resource groups are enabled by the new management functionality, Azure Resource Manager. Azure Resource Manager allows you to group multiple resources as a logical group which serves as the lifecycle boundary for every resource contained within it. Typically a group will contain resources related to a specific application. For example, a group may contain a Website resource that hosts your public website, a SQL Database that stores relational data used by the site, and a Storage Account that stores non-relational assets.

Here is a concise overview of how to use Resource groups within the Azure Management Portal.

## Creating resource groups

Whenever a resource is created in the portal, it is always created within a resource group. You can choose to create a new resource group or use an existing resource group in the create flow. <br><br />

![create resource group](./media/resource-group-portal/1_createWebsite.png)

When you create an application that consists of a few resources working together (e.g. Website + Database) it is always created in its own resource group, so you can manage the lifecycle of all related assets using the resource group. You can add or remove additional resources from the resource group as your application evolves.

![create resource group](./media/resource-group-portal/2_createWSandDB.png)

## Browsing resource groups

You can browse all resource groups by clicking the Jumpbar on the left side of your screen. A resource group has a blade that gives you all the information on a particular resource group. The Resource group blade will also give you a unified view of your billing and monitoring information for all the resources in the Resource group.

The summary section shows a visual resource map of all the resources in the resource group, it also shows resources in other resource groups that are linked to the resource group. The resource map also shows the status of each resource.
![resource group summary](./media/resource-group-portal/3_1BrowseRGs.png)

The resource map part can be customized to show in a larger size which will display all the resources that are contained within the resource group and resources in other resource groups that are linked. This part can be pinned to the Starboard, which will copy the part to the Startboard.

![pin](./media/resource-group-portal/3_2BrowseRGs.png)

Clicking on the resource map launches the list view of all the resources on the resource map. This view will list all the resources within a resource group or linked to it. Clicking on these resources will launch their blades.

![see resources](./media/resource-group-portal/3_3BrowseRGs.png)
<!-- keep by customization: end -->

## Adding resources to resource groups

You can add resources to a resource group using the **Add** command on the resource group blade. <!-- keep by customization: begin --> Following the steps in the flow will allow you to add other resources to the resource group. <!-- keep by customization: end -->

<!-- deleted by customization
![add resource](./media/resource-group-portal/add-resource.png)

You can select the resource you want from the available list.
-->
<!-- keep by customization: begin -->
![add resource](./media/resource-group-portal/4_AddResource.png)

Note: It is not advisable to put team project in the same resource group as other Azure resources. If you create a Team Project in a new account and group, then create a Website, the site group will default to the last group used (VSO group) and you will end up with runtime/developer resources in the same group.
<!-- keep by customization: end -->

## Deleting resource groups

Since resource groups allow you to manage the lifecycle of all the contained resources, deleting a resource group will delete all the resources contained within it. You can also delete individual resources within a resource group. You want to exercise caution when you are deleting a resource group since there might be other resources linked to it. You can see the linked resources in the resource map and take the necessary steps to avoid any unintentional consequences when you delete resource groups. <!-- deleted by customization The linked resources will not be deleted but they may not operate as expected. -->
<!-- deleted by customization

![delete group](./media/resource-group-portal/delete-group.png)

## Tagging resources

You can apply tags to resource groups and resources to logically organize your assets. For information about working with tags through the preview portal, see [Using tags to organize your Azure resources](/documentation/articles/resource-group-using-tags).

## Deploying a custom template

If you want to execute a deployment but not use any of the templates in the Marketplace, you can create customized template that defines the infrastructure for your solution. For more information about templates, see [Authoring Azure Resource Manager templates](/documentation/articles/resource-group-authoring-templates).

To deploy a customized template through the preview portal, select **New**, **Marketplace**, and **Everything**.

![find template deployment](./media/resource-group-portal/launch-template.png)

Search for **Template Deployment**, and select it from the returned list.

![search template deployment](./media/resource-group-portal/search-template.png)

After launching the template deployment, you can create the custom template and set values for the deployment.

![create template](./media/resource-group-portal/show-custom-template.png)
-->

## Next Steps
Getting Started  

- For an introduction to the concepts in Resource Manager, see [Azure Resource Manager Overview](/documentation/articles/resource-group-overview) <!-- deleted by customization. -->
- For an introduction to using Azure PowerShell when deploying resources, see [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager) <!-- deleted by customization. -->
- For an introduction to using Azure CLI when deploying resources, see [Using the Azure CLI for Mac, Linux, and Windows with Azure Resource Management](/documentation/articles/xplat-cli-azure-resource-manager) <!-- deleted by customization. -->
<!-- keep by customization: begin -->

- To learn about logically organizing your resources, see [Using tags to organize your Azure resources](/documentation/articles/resource-group-using-tags).
<!-- keep by customization: end -->
