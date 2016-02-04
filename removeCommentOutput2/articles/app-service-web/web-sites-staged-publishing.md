<properties
	pageTitle="Set up staging environments for web apps in Azure"
	description="Learn how to use staged publishing for web apps in Azure."
	services="app-service"
	documentationCenter=""
	authors="cephalin"
	writer="cephalin"
	manager="wpickett"
	editor="mollybos"/>

<tags
	ms.service="app-service"
	ms.date="01/12/2016"
	wacn.date=""/>

# Set up staging environments for web apps in Azure
<a name="Overview"></a>

When you deploy your web app to [Azure Web App](/documentation/services/web-sites/), you can deploy to a separate deployment slot instead of the default production slot when running in the **Standard** App Service plan mode. Deployment slots are actually live web apps with their own hostnames. Web app content and configurations elements can be swapped between two deployment slots, including the production slot. Deploying your application to a deployment slot has the following benefits:

- You can validate web app changes in a staging deployment slot before swapping it with the production slot.

- Deploying a web app to a slot first and swapping it into production ensures that all instances of the slot are warmed up before being swapped into production. This eliminates downtime when you deploy your web app. The traffic redirection is seamless, and no requests are dropped as a result of swap operations. This entire workflow can be automated by configuring [Auto Swap](#configure-auto-swap-for-your-web-app) when pre-swap validation is not needed.

- After a swap, the slot with previously staged web app now has the previous production web app. If the changes swapped into the production slot are not as you expected, you can perform the same swap immediately to get your "last known good site" back.

Only the **Standard** App Service plan mode supports staging deployment. To scale you website, see [scale your website in Azure Websites](/documentation/articles/web-sites-scale).

- When your web app has multiple slots, you cannot change the mode.

- Scaling is not available for non-production slots.

- Linked resource management is not supported for non-production slots. In the [Azure Management Portal](https://manage.windowsazure.cn/) only, you can avoid this potential impact on a production slot by temporarily moving the non-production slot to a different App Service plan mode. Note that the non-production slot must once again share the same mode with the production slot before you can swap the two slots.


<a name="Add"></a>
## Add a deployment slot to a web app ##

The web app must be running in the **Standard** mode in order for you to enable multiple deployment slots.

1. On the Quick Start page, or in the Quick Glance section of the Dashboard page for your website, click **Add a new deployment slot**. 
	
	![Add a new deployment slot][QGAddNewDeploymentSlot]
	
	> [AZURE.NOTE]
	> If the website is not already in **Standard** mode, you will receive the message **You must be in the standard mode to enable staged publishing**. At this point, you have the option to select **Upgrade** and navigate to the **Scale** tab of your website before continuing.
	
2. In the **Add New Deployment Slot** dialog, give the slot a name, and select whether to clone website configuration from another existing deployment slot. Click the check mark to continue.
	
	![Configuration Source][ConfigurationSource1]
	
	The first time you create a slot, you will only have two choices: clone configuration from the default slot in production or not at all.
	
	After you have created several slots, you will be able to clone configuration from a slot other than the one in production:
	
	![Configuration sources][MultipleConfigurationSources]

3. In the list of websites, expand the mark to the left of your website name to reveal the deployment slot. It will have the website name followed by the deployment slot name. 
	
	![Site List with Deployment Slot][SiteListWithStagedSite]
	
4. When you click the name of the deployment site slot, a page will open with a set of tabs just like any other website. <strong><i>your-website-name</i>(<i>deployment-slot-name</i>)</strong> will appear at the top of the portal page to remind you that you are viewing the deployment site slot.
	
	![Deployment Slot Title][StagingTitle]
	
5. Click the site URL in the dashboard view. Notice the the deployment slot has its own hostname and is also a live site. To limit public access to the deployment slot, see [Azure Web Sites - block web access to non-production deployment slots](http://ruslany.net/2014/04/azure-web-sites-block-web-access-to-non-production-deployment-slots/).

There is no content after deployment slot creation. You can deploy to the slot from a different repository branch, or an altogether different repository. You can also change the slot's configuration. Use the publish profile or deployment credentials associated with the deployment slot for content updates.  For example, you can [publish to this slot with git](/documentation/articles/web-sites-publish-source-control).

<a name="AboutConfiguration"></a>
## Configuration for deployment slots ##
When you clone configuration from another deployment slot, the cloned configuration is editable. Furthermore, some configuration elements will follow the content across a swap (not slot specific) while other configuration elements will stay in the same slot after a swap (slot specific). The following lists show the configuration that will change when you swap slots.

**Settings that are swapped**:

- General settings - such as framework version, 32/64-bit, Web sockets
- App settings (can be configured to stick to a slot)
- Connection strings (can be configured to stick to a slot)
- Handler mappings
- Monitoring and diagnostic settings
- WebJobs content

**Settings that are not swapped**:

- Publishing endpoints
- Custom Domain Names
- SSL certificates and bindings
- Scale settings
- WebJobs schedulers


<a name="Swap"></a>
## To swap deployment slots ##

>[AZURE.IMPORTANT] Before you swap a web app from a deployment slot into production, make sure that all non-slot specific settings are configured exactly as you want to have it in the swap target.

1. To swap deployment slots, click the **Swap** button in the command bar of the web app or in the command bar of a deployment slot. Make sure that the swap source and swap target are set properly. Usually, the swap target would be the production slot.  

	![Swap Button][SwapButtonBar]

3. Click **OK** to complete the operation. When the operation finishes, the deployment slots have been swapped.

<a name="Multi-Phase"></a>
## Use multi-phase swap for your web app ##

Multi-phase swap is available to simplify validation in the context of configuration elements designed to stick to a slot such as connection strings. In these cases, it may be useful to apply such configuration elements from the swap target to the swap source and validate before swap actually takes effect. Once swap target configuration elements are applied to the swap source the actions available are either completing the swap or reverting to original configuration for the swap source which also has the effect of canceling the swap. Samples for the Azure PowerShell cmdlets available for multi-phase swap are included in the Azure PowerShell cmdlets for deployment slots section.

<a name="Rollback"></a>
## To rollback a production app after swap ##
If any errors are identified in production after a slot swap, roll the slots back to their pre-swap states by swapping the same two slots immediately.

<a name="Delete"></a>
## To delete a deployment slot##

In the blade for a deployment slot, click **Delete** in the command bar.  

![Delete a Deployment Slot][DeleteStagingSiteButton]

<!-- ======== AZURE POWERSHELL CMDLETS =========== -->

<a name="PowerShell"></a>
## Azure PowerShell cmdlets for deployment slots

[AZURE.INCLUDE [AzureRm PowerShell with Azure China Cloud](../includes/azurerm-azurechinacloud-environment-parameter.md)]

Azure PowerShell is a module that provides cmdlets to manage Azure through Windows PowerShell, including support for managing web app deployment slots in Azure Web App.

- For information on installing and configuring Azure PowerShell, and on authenticating Azure PowerShell with your Azure subscription, see [How to install and configure Windows Azure PowerShell](/documentation/articles/powershell-install-configure).  

- In order to use the new Azure Resource Manager mode for PowerShell cmdlets start with the following: `Switch-AzureMode -Name AzureResourceManager`.

----------

### Create web app

`New-AzureWebApp -ResourceGroupName [resource group name] -Name [web app name] -Location [location] -AppServicePlan [app service plan name]`

----------

### Create a deployment slot for a web app

`New-AzureWebApp -ResourceGroupName [resource group name] -Name [web app name] -SlotName [deployment slot name] -Location [location] -AppServicePlan [app service plan name]`

----------

### Initiate multi-phase swap and apply target slot configuration to source slot

`$ParametersObject = @{targetSlot  = "[slot name - e.g. “production”]"}`
`Invoke-AzureResourceAction -ResourceGroupName [resource group name] -ResourceType Microsoft.Web/sites/slots -ResourceName [web app name]/[slot name] -Action applySlotConfig -Parameters $ParametersObject -ApiVersion 2015-07-01`

----------

### Revert the first phase of multi-phase swap and restore source slot configuration

`Invoke-AzureResourceAction -ResourceGroupName [resource group name] -ResourceType Microsoft.Web/sites/slots -ResourceName [web app name]/[slot name] -Action resetSlotConfig -ApiVersion 2015-07-01`

----------

### Swap deployment slots

`$ParametersObject = @{targetSlot  = "[slot name - e.g. “production”]"}`
`Invoke-AzureResourceAction -ResourceGroupName [resource group name] -ResourceType Microsoft.Web/sites/slots -ResourceName [web app name]/[slot name] -Action slotsswap -Parameters $ParametersObject -ApiVersion 2015-07-01`

----------

### Delete deployment slot

`Remove-AzureResource -ResourceGroupName [resource group name] -ResourceType Microsoft.Web/sites/slots -Name [web app name]/[slot name] -ApiVersion 2015-07-01`

----------

<!-- ======== Azure CLI =========== -->

<a name="CLI"></a>
## Azure Command-Line Interface (Azure CLI) commands for Deployment Slots

[AZURE.INCLUDE [Azure CLI with Azure China Cloud](../includes/azure-cli-azurechinacloud-environment-parameter.md)]

The Azure CLI provides cross-platform commands for working with Azure, including support for managing Web App deployment slots.

- For instructions on installing and configuring the Azure CLI, including information on how to connect Azure CLI to your Azure subscription, see [Install and Configure the Azure CLI](/documentation/articles/xplat-cli-install).

-  To list the commands available for Azure in the Azure CLI, call `azure site -h`.

----------
### azure site list
For information about the web apps in the current subscription, call **azure site list**, as in the following example.

`azure site list webappslotstest`

----------
### azure site create
To create a deployment slot, call **azure site create** and specify the name of an existing web app and the name of the slot to create, as in the following example.

`azure site create webappslotstest --slot staging`

To enable source control for the new slot, use the **--git** option, as in the following example.

`azure site create --git webappslotstest --slot staging`

----------
### azure site swap
To make the updated deployment slot the production app, use the **azure site swap** command to perform a swap operation, as in the following example. The production app will not experience any down time, nor will it undergo a cold start.

`azure site swap webappslotstest`

----------
### azure site delete
To delete a deployment slot that is no longer needed, use the **azure site delete** command, as in the following example.

`azure site delete webappslotstest --slot staging`

----------

## Next Steps ##
[Azure Web App - block web access to non-production deployment slots](http://ruslany.net/2014/04/azure-web-sites-block-web-access-to-non-production-deployment-slots/)

[Windows Azure Trial](/pricing/1rmb-trial/)

<!-- IMAGES -->
[QGAddNewDeploymentSlot]:  ./media/web-sites-staged-publishing/QGAddNewDeploymentSlot.png
[AddNewDeploymentSlotDialog]: ./media/web-sites-staged-publishing/AddNewDeploymentSlotDialog.png
[ConfigurationSource1]: ./media/web-sites-staged-publishing/ConfigurationSource1.png
[MultipleConfigurationSources]: ./media/web-sites-staged-publishing/MultipleConfigurationSources.png
[SiteListWithStagedSite]: ./media/web-sites-staged-publishing/SiteListWithStagedSite.png
[StagingTitle]: ./media/web-sites-staged-publishing/StagingTitle.png
[SwapButtonBar]: ./media/web-sites-staged-publishing/SwapButtonBar.png
[SwapConfirmationDialog]:  ./media/web-sites-staged-publishing/SwapConfirmationDialog.png
[DeleteStagingSiteButton]: ./media/web-sites-staged-publishing/DeleteStagingSiteButton.png
[SwapDeploymentsDialog]: ./media/web-sites-staged-publishing/SwapDeploymentsDialog.png
[Autoswap1]: ./media/web-sites-staged-publishing/AutoSwap01.png
[Autoswap2]: ./media/web-sites-staged-publishing/AutoSwap02.png
[SlotSettings]: ./media/web-sites-staged-publishing/SlotSetting.png
 
