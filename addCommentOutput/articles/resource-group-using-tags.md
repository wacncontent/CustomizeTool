<properties
	pageTitle="Using tags to organize your Azure resources"
	description="Shows how to apply tags to organize resources for billing and managing."
	services="azure-resource-manager"
	documentationCenter=""
	authors="tfitzmac"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="azure-resource-manager"
	ms.date="10/14/2015"
	wacn.date=""/>


# Using tags to organize your Azure resources

Resource Manager enables you to logically organize resources by applying tags. The tags consist of key/value pairs that identify resources with properties that you define. To mark resources as belonging to the same category, apply the same tag to those resources.

When you view resources with a particular tag, you see resources from all of your resource groups. You are not limited to only resources in the same resource group which enables you to organize your resources in a way that is independent of the deployment relationships. Tags can be particularly helpful when you need to organize resources for billing or management.

Each tag you add to a resource or resource group is automatically added to the subscription-wide taxonomy. You can also prepopulate the taxonomy for your subscription with tag names and values you'd like to use as resources are tagged in the future.

> [AZURE.NOTE] You can only apply tags to resources that support Resource Manager operations. If you created a Virtual Machine, Virtual Network, or Storage through the classic deployment model (such as through the Azure Management Portal or [Service Management <!-- deleted by customization API](/home/features/api-management/)) --><!-- keep by customization: begin --> API](https://msdn.microsoft.com/zh-cn/library/azure/dn948465.aspx)) <!-- keep by customization: end -->, you cannot apply a tag to that resource. You must re-deploy these resources through Resource Manager to support tagging. All other resources support tagging.


## Tags in the preview portal

Tagging resources and resource groups in the preview portal is easy. Use the Browse hub to navigate to the resource or resource group you’d like to tag and click the Tags part in the Overview section at the top of the blade.

![Tags part on resource and resource group blades](./media/resource-group-using-tags/tag-icon.png)

This will open a blade with the list of tags that have already been applied. If this is your first tag, the list will be empty. To add a tag, simply specify a name and value and press Enter. After you've added a few tags, you'll notice autocomplete options based on pre-existing tag names and values to better ensure a consistent taxonomy across your resources and to avoid common mistakes, like misspellings.

![Tag resources with name/value pairs](./media/resource-group-using-tags/tag-resources.png)

To view your taxonomy of tags in the portal, use the Browse hub to view Everything and then select Tags.

![Find tags via the Browse hub](./media/resource-group-using-tags/browse-tags.png)

Pin the most important tags to your Startboard for quick access and you're ready to go. Have fun!

![Pin tags to the Startboard](./media/resource-group-using-tags/pin-tags.png)

## Tagging with PowerShell

<!-- deleted by customization
[AZURE.INCLUDE [powershell-preview-inline-include](../includes/powershell-preview-inline-include.md)]

Tags exist directly on resources and resource groups, so to see what tags are already applied, we can simply get a resource or resource group with **Get-AzureRmResource** or **Get-AzureRmResourceGroup**. Let's start with a resource group.

    PS C:\> Get-AzureRmResourceGroup tag-demo
-->
<!-- keep by customization: begin -->
If you have not previously used Azure PowerShell with Resource Manager, see [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager).
For the purposes of this article, we'll assume you've already added an account and selected a subscription with the resources you want to tag.

Tagging is only available for resources and resource groups available from [Resource Manager](http://msdn.microsoft.com/zh-cn/library/azure/dn790568.aspx), so the next thing we need to do is switch to use Resource Manager.

    Switch-AzureMode AzureResourceManager

Tags exist directly on resources and resource groups, so to see what tags are already applied, we can simply get a resource or resource group with `Get-AzureResource` or `Get-AzureResourceGroup`, respectively. Let's start with a resource group.

    PS C:\> Get-AzureResourceGroup tag-demo
<!-- keep by customization: end -->

    ResourceGroupName : tag-demo
    Location          : southcentralus
    ProvisioningState : Succeeded
    Tags              :
    Permissions       :
                    Actions  NotActions
                    =======  ==========
                    *

    Resources         :
                    Name                             Type                                  Location
                    ===============================  ====================================  ==============
                    CPUHigh ExamplePlan              microsoft.insights/alertrules         <!-- deleted by customization eastus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    ForbiddenRequests tag-demo-site  microsoft.insights/alertrules         <!-- deleted by customization eastus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    LongHttpQueue ExamplePlan        microsoft.insights/alertrules         <!-- deleted by customization eastus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    ServerErrors tag-demo-site       microsoft.insights/alertrules         <!-- deleted by customization eastus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    ExamplePlan-tag-demo             microsoft.insights/autoscalesettings  <!-- deleted by customization eastus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    tag-demo-site                    microsoft.insights/components         <!-- deleted by customization centralus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    ExamplePlan                      Microsoft.Web/serverFarms             <!-- deleted by customization southcentralus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->
                    tag-demo-site                    Microsoft.Web/sites                   <!-- deleted by customization southcentralus --><!-- keep by customization: begin --> chinaeast <!-- keep by customization: end -->


This cmdlet returns several bits of metadata on the resource group including what tags have been applied, if any. To tag a resource group, simply use the <!-- deleted by customization **Set-AzureRmResourceGroup** --><!-- keep by customization: begin --> `Set-AzureResourceGroup` <!-- keep by customization: end --> command and specify a tag name and value.

    PS C:\> <!-- deleted by customization Set-AzureRmResourceGroup --><!-- keep by customization: begin --> Set-AzureResourceGroup <!-- keep by customization: end --> tag-demo -Tag @( @{ Name="project"; Value="tags" }, @{ Name="env"; Value="demo"} )

    ResourceGroupName : tag-demo
    Location          : southcentralus
    ProvisioningState : Succeeded
    Tags              :
                    Name     Value
                    =======  =====
                    project  tags
                    env      demo

Tags are updated as a whole, so if you are adding one tag to a resource that's already been tagged, you'll need to use an array with all the tags you want to keep. To do this, you can first select the existing tags and add a new one.

<!-- deleted by customization
    PS C:\> $tags = (Get-AzureRmResourceGroup -Name tag-demo).Tags
-->
<!-- keep by customization: begin -->
    PS C:\> $tags = (Get-AzureResourceGroup -Name tag-demo).Tags
<!-- keep by customization: end -->
    PS C:\> $tags += @{Name="status";Value="approved"}
<!-- deleted by customization
    PS C:\> Set-AzureRmResourceGroup tag-demo -Tag $tags
-->
<!-- keep by customization: begin -->
    PS C:\> Set-AzureResourceGroup tag-demo -Tag $tags
<!-- keep by customization: end -->

    ResourceGroupName : tag-demo
    Location          : southcentralus
    ProvisioningState : Succeeded
    Tags              :
                    Name     Value
                    =======  ========
                    project  tags
                    env      demo
                    status   approved


To remove one or more tags, simply save the array without the ones you want to remove.

<!-- deleted by customization
The process is the same for resources, except you'll use the **Get-AzureRmResource** and **Set-AzureRmResource** cmdlets. 

To get resource groups with a specific tag, use **Find-AzureRmResourceGroup** cmdlet with the **-Tag** parameter.

    PS C:\> Find-AzureRmResourceGroup -Tag @{ Name="env"; Value="demo" } | %{ $_.ResourceGroupName }
    rbacdemo-group
    tag-demo

For Azure PowerShell versions earlier than 1.0 Preview use the following commands to get resources with a specific tag.
-->
<!-- keep by customization: begin -->
The process is the same for resources, except you'll use the `Get-AzureResource` and `Set-AzureResource` cmdlets. To get resources or resource groups with a specific tag, use `Get-AzureResource` or `Get-AzureResourceGroup` cmdlet with the `-Tag` parameter.
<!-- keep by customization: end -->

    PS C:\> Get-AzureResourceGroup -Tag @{ Name="env"; Value="demo" } | %{ $_.ResourceGroupName }
    rbacdemo-group
    tag-demo
    PS C:\> Get-AzureResource -Tag @{ Name="env"; Value="demo" } | %{ $_.Name }
    rbacdemo-web
    rbacdemo-docdb
    ...    

To get a list of all tags within a subscription using PowerShell, use the <!-- deleted by customization **Get-AzureRmTag** --><!-- keep by customization: begin --> `Get-AzureTag` <!-- keep by customization: end --> cmdlet.

<!-- deleted by customization
    PS C:/> Get-AzureRmTag
-->
<!-- keep by customization: begin -->
    PS C:/> Get-AzureTag
<!-- keep by customization: end -->
    Name                      Count
    ----                      ------
    env                       8
    project                   1

You may see tags that start with "hidden-" and "link:". These are internal tags, which you should ignore and avoid changing.

Use the <!-- deleted by customization **New-AzureRmTag** --><!-- keep by customization: begin --> `New-AzureTag` <!-- keep by customization: end --> cmdlet to add new tags to the taxonomy. These tags will be included in the autocomplete even though they haven't been applied to any resources or resource groups, yet. To remove a tag name/value, first remove the tag from any resources it may be used with and then use the <!-- deleted by customization **Remove-AzureRmTag** --><!-- keep by customization: begin --> `Remove-AzureTag` <!-- keep by customization: end --> cmdlet to remove it from the taxonomy.

## Tagging with REST API

The portal and PowerShell both use the [Resource Manager REST API](http://msdn.microsoft.com/zh-cn/library/azure/dn790568.aspx) behind the scenes. If you need to integrate tagging into another environment, you can get tags with a GET on the resource id and update the set of tags with a PATCH call.


## Tagging and billing

For supported services, you can use tags to group your billing data. For example, [Virtual Machines integrated with Azure Resource <!-- deleted by customization Manager](/virtual-machines/virtual-machines-azurerm-versus-azuresm.md) --><!-- keep by customization: begin --> Manager](/documentation/articles/virtual-machines-azurerm-versus-azuresm) <!-- keep by customization: end --> enable
you to define and apply tags to organize the billing usage for virtual machines. If you are running multiple VMs for different organizations, you can use the tags to group usage by cost center.  
You can also use tags to categorize costs by runtime environment; such as, the billing usage for VMs running in production environment.

You can retrieve information about tags through the [Azure Resource Usage and RateCard APIs](/documentation/articles/billing-usage-rate-card-overview) or the usage comma-separated values (CSV) file that you can download from
the [Azure accounts portal](https://account.windowsazure.cn/) or [EA portal](https://ea.azure.com). For more information about programmatic access to billing information, see [Gain insights into your Windows Azure resource consumption](/documentation/articles/billing-usage-rate-card-overview). For REST API operations, see [Azure Billing REST API Reference](https://msdn.microsoft.com/zh-cn/library/azure/1ea5b323-54bb-423d-916f-190de96c6a3c).

When you download the usage CSV for services that support tags with billing, the tags will appear in the **Tags** column. For more details, see [Understand your bill for Windows Azure](/documentation/articles/billing-understand-your-bill).

![See tags in billing](./media/resource-group-using-tags/billing_csv.png)

## Next Steps

- For an introduction to using Azure PowerShell when deploying resources, see [Using Azure PowerShell with Azure Resource <!-- deleted by customization Manager](./powershell-azure-resource-manager.md) --><!-- keep by customization: begin --> Manager](/documentation/articles/powershell-azure-resource-manager) <!-- keep by customization: end -->.
- For an introduction to using Azure CLI when deploying resources, see [Using the Azure CLI for Mac, Linux, and Windows with Azure Resource <!-- deleted by customization Management](./xplat-cli-azure-resource-manager.md) --><!-- keep by customization: begin --> Management](/documentation/articles/xplat-cli-azure-resource-manager) <!-- keep by customization: end -->.
- For an introduction to using the preview portal, see [Using the Azure preview portal to manage your Azure <!-- deleted by customization resources](./resource-group-portal.md) --><!-- keep by customization: begin --> resources](/documentation/articles/resource-group-portal) <!-- keep by customization: end -->