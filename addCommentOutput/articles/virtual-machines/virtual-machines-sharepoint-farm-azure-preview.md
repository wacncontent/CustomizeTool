<properties
	pageTitle="SharePoint Server Farm | Windows Azure"
	description="Quickly create a new basic or highly-available SharePoint Server 2013 farm using SharePoint Server Farm in the Azure Preview portal."
	services="virtual-machines"
	documentationCenter=""
	authors="JoeDavies-MSFT"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/05/2015"
	wacn.date=""/>

<!-- deleted by customization
# SharePoint Server Farm

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.
 

With SharePoint Server Farm, the Windows Azure Preview Portal automatically creates a pre-configured SharePoint Server 2013 farm for you. This can save you a lot of time when you need a basic or high-availability SharePoint farm for a development and testing environment or if you are evaluating SharePoint Server 2013 as a collaboration solution for your organization.
-->
<!-- keep by customization: begin -->
#SharePoint Server Farm#

With SharePoint Server Farm, the Windows Azure Management Portal automatically creates a pre-configured SharePoint Server 2013 farm for you. This can save you a lot of time when you need a basic or high-availability SharePoint farm for a development and testing environment or if you are evaluating SharePoint Server 2013 as a collaboration solution for your organization.
<!-- keep by customization: end -->

The basic SharePoint farm consists of three virtual machines in this configuration.

![sharepointfarm](./media/virtual-machines-sharepoint-farm-azure-preview/SPFarm_Basic.png)

You can use this farm configuration for a simplified setup for SharePoint app development or your first-time evaluation of SharePoint 2013.

The high-availability SharePoint farm consists of nine virtual machines in this configuration.

![sharepointfarm](./media/virtual-machines-sharepoint-farm-azure-preview/SPFarm_HighAvail.png)

You can use this farm configuration to test higher client loads, high availability of the external SharePoint site, and SQL Server AlwaysOn for a SharePoint farm. You can also use this configuration for SharePoint app development in a high-availability environment.
For the configuration details for both of these farms, see [SharePoint Server Farm Configuration Details](/documentation/articles/virtual-machines-sharepoint-farm-config-azure-preview).
<!-- deleted by customization

> [AZURE.NOTE] Microsoft has released the SharePoint Server 2016 IT Preview. To make this preview easy to install and test, you can use an Azure virtual machine gallery image with SharePoint Server 2016 IT Preview and its prerequisites pre-installed. For more information, see [Test the SharePoint Server 2016 IT Preview in Azure](http://azure.microsoft.com/blog/test-sharepoint-server-2016-it-preview-4/).
-->

## Stepping through configuration

To create your SharePoint farm with the SharePoint Server Farm template, do the following:

1. In the [Windows Azure Preview <!-- deleted by customization Portal](https://manage.windowsazure.cn/) --><!-- keep by customization: begin --> Portal](https://manage.windowsazure.cn) <!-- keep by customization: end -->, click  **New** > **Compute** > **SharePoint Server Farm**. If **SharePoint Server Farm** does not appear, click **New** > **Compute** > **Marketplace**, type **SharePoint** in **Search Compute**, and then click **SharePoint Server Farm**. In the **SharePoint Server Farm** pane, click **Create**.
2. In the **Create a SharePoint farm** pane, type the name of a resource group.
3. Type a user name and password for a local administrator account on each virtual machine in your farm. Choose a name and password that is difficult to guess, record it, and store it in a secure location.
4. If you want the high-availability farm, click **Enable high availability**.
5. To configure your domain controllers, click the arrow. You can specify a host name prefix (the default is the resource group name), forest root domain name (default is contoso.com), and the size of your domain controllers (default is A1).
6. To configure your SQL servers, click the arrow. You can specify a host name prefix (the default is the resource group name), the size of your SQL servers (default is A5), a database access account name and password (the default is to use the administrator account), and a SQL server service account name (the default is sqlservice) and password (the default is to use the same password as the administrator account).
7. To configure your SharePoint servers, click the arrow. You can specify a host name prefix (the default is the resource group name), the size of your SharePoint servers (default is A2), a SharePoint user account (the default is sp_setup) and password, a SharePoint farm account name (the default is sp_farm) and password, and a SharePoint farm passphrase. The default is to use the administrator password for the SharePoint user account, farm account, and passphrase.
8. To configure optional configuration settings for the virtual network, storage account, or diagnostics, click the corresponding arrow.
9. To specify the subscription, click the arrow.
<!-- deleted by customization
10. To specify the Azure location, click the arrow.
11. When you are done, click **Create**.
-->
<!-- keep by customization: begin -->
10. When you are done, click **Create**.
<!-- keep by customization: end -->

> [AZURE.NOTE] The domain controller does not have the Active Directory Management tools installed by default. To install them, run the **Install-WindowsFeature AD-Domain-Services -IncludeManagementTools** command from an administrator-level Windows PowerShell command prompt on the domain controller virtual machine.

## Accessing and managing the SharePoint farms

The SharePoint farms have a pre-configured endpoint to allow unauthenticated web traffic (TCP port 80) to the SharePoint web server for an Internet-connected client computer. This endpoint is to a pre-configured team site. To access this team site:

1.	From the Azure Preview Portal, click **Browse**, and then click **Resource Groups**.
2.	In the list of resource groups, click the name of your SharePoint farm resource group.
3.	In the pane for your SharePoint farm resource group, click **Deployment history**.
4.	In the **Deployment history** pane, click **Microsoft.SharePointFarm**.
5.	In the **Microsoft.SharePointFarm** pane, select the URL in the **SHAREPOINTSITEURL** field and copy it.
6.	From your Internet browser, paste the URL into the address field.
7.	When prompted, enter the user account credentials that you specified when you created the farm.

From the Central Administration SharePoint site, you can configure My sites, SharePoint applications, and other functionality. For more information, see [Configure SharePoint 2013](http://technet.microsoft.com/zh-cn/library/ee836142.aspx). To access the Central Administration SharePoint site:

1.	From the Azure Preview Portal, click **Browse**, and then click **Resource Groups**.
2.	In the list of resource groups, click the name of your SharePoint farm resource group.
3.	In the pane for your SharePoint farm resource group, click **Deployment history**.
4.	In the **Deployment history** pane, click **Microsoft.SharePointFarm**.
5.	In the **Microsoft.SharePointFarm** pane, select the URL in the **SHAREPOINTCENTRALADMINURL** field and copy it.
6.	From your Internet browser, paste the URL into the address field.
7.	When prompted, enter the user account credentials that you specified when you created the farm.


Notes:

<!-- keep by customization: begin -->
- The Azure Preview Portal creates these virtual machines within the specified subscription.
<!-- keep by customization: end -->
- The Azure Preview Portal creates both of these farms in a cloud-only virtual network with an Internet-facing web presence. There is no site-to-site VPN or ExpressRoute connection back to your organization network.
<!-- deleted by customization
- You can administer these servers through Remote Desktop connections. For more information, see [Log on to the virtual machine](/documentation/articles/virtual-machines-windows-tutorial#log-on-to-the-virtual-machine).
-->
<!-- keep by customization: begin -->
- You can administer these servers through Remote Desktop connections. For more information, see [How to Log on to a Virtual Machine Running Windows Server](/documentation/articles/virtual-machines-log-on-windows-server).
<!-- keep by customization: end -->

## Azure Resource Manager

The SharePoint Server Farm feature of the Azure Preview Portal creates virtual machines <!-- deleted by customization with the classic deployment model --><!-- keep by customization: begin --> in Service Management <!-- keep by customization: end -->. To create SharePoint Server 2013 farms <!-- deleted by customization with the --><!-- keep by customization: begin --> in <!-- keep by customization: end --> Resource Manager <!-- deleted by customization deployment model -->, see [Deploy SharePoint Farms with Azure Resource Manager Templates](/documentation/articles/virtual-machines-workload-template-sharepoint).

## Additional resources

[SharePoint Server Farm Configuration Details](/documentation/articles/virtual-machines-sharepoint-farm-config-azure-preview)

<!-- keep by customization: begin -->
[SharePoint on Azure Infrastructure Services](http://msdn.microsoft.com/zh-cn/library/azure/dn275955.aspx)

[Set up a SharePoint intranet farm in a hybrid cloud for testing](./documentation/articles/virtual-networks-setup-sharepoint-hybrid-cloud-testing)

<!-- keep by customization: end -->
[SharePoint farms hosted in Azure infrastructure services](/documentation/articles/virtual-machines-sharepoint-infrastructure-services)

<!-- deleted by customization
[Set up a SharePoint intranet farm in a hybrid cloud for testing](/documentation/articles/virtual-networks-setup-sharepoint-hybrid-cloud-testing)

-->