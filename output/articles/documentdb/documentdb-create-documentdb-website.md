<properties 
	pageTitle="Deploy DocumentDB and Azure Websites using an Azure Resource Manager Template | Windows Azure" 
	description="Learn how to deploy a DocumentDB account, Azure Websites, and a sample web site using an Azure Resource Manager template." 
	services="documentdb, app-service\web" 
	authors="ryancrawcour" 
	manager="jhubbard" 
	editor="monicar" 
	documentationCenter=""/>

<tags
	ms.service="documentdb"
	ms.date="10/16/2015"
	wacn.date=""/>

# Deploy DocumentDB and Azure Websites using an Azure Resource Manager Template #

This tutorial shows you how to use an Azure Resource Manager template to deploy and integrate [Windows Azure DocumentDB](/home/features/documentdb/), an [Azure Websites](/documentation/services/web-sites/) web site, and a sample web site.

After completing this tutorial, you'll be able to answer the following questions:  

-	How can I use an Azure Resource Manager template to deploy and integrate a DocumentDB account and a web site in Azure Websites?
-	How can I use an Azure Resource Manager template to deploy and integrate a DocumentDB account, a web site in Azure Websites, and a Webdeploy application?

<a id="Prerequisites"></a>
## Prerequisites ##
> [AZURE.TIP] While this tutorial does not assume prior experience with Azure Resource Manager templates, JSON, or Azure PowerShell, should you wish to modify the referenced templates or deployment options, then knowledge of each of these areas will be required.

Before following the instructions in this tutorial, ensure that you have the following:

- An Azure subscription. Azure is a subscription-based platform.  For more information about obtaining a subscription, see [Purchase Options](/pricing/overview/), [Member Offers](/pricing/member-offers/), or [Trial](/pricing/1rmb-trial/).
- An Azure Storage Account. For instructions, see [About Azure Storage Accounts](/documentation/articles/storage-whatis-account).
- A workstation with Azure PowerShell 0.9.8. For instructions, see [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure). This tutorial has not yet been updated for Azure PowerShell 1.0 Preview. 

##<a id="CreateDB"></a>Step 1: Download and extract the sample files ##
Let's start by downloading the sample files we will use in this tutorial.

1. Download the [Create a DocumentDB account, web sites, and deploy a demo application sample](https://portalcontent.blob.core.chinacloudapi.cn/samples/CreateDocDBWebsiteTodo.zip) to a local folder (e.g. C:\DocumentDBTemplates) and extract the files.  This sample will deploy a DocumentDB account, an Azure Websites, and a web site.  It will also automatically configure the web site to connect to the DocumentDB account.

2. Download the [Create a DocumentDB account and web sites sample](https://portalcontent.blob.core.chinacloudapi.cn/samples/CreateDocDBWebSite.zip) to a local folder (e.g. C:\DocumentDBTemplates) and extract the files.  This sample will deploy a DocumentDB account, an Azure Websites, and will modify the web site's configuration to easily surface DocumentDB connection information, but does not include a web site.  

> [AZURE.TIP] Note that depending on the security settings of your computer, you may need to unblock the extracted files by right-clicking, clicking **Properties**, and clicking **Unblock**.

![Screenshot of the Properties window with the Unblock button highlighted](./media/documentdb-create-documentdb-website/image1.png)

<a id="Build"></a>
##Step 2: Deploy the Document account, Azure Websites and demo application sample ##

Now let's deploy our first template.

> [AZURE.TIP] The template does not validate that the web site name and DocumentDB account name entered below are a) valid and b) available.  It is highly recommended that you verify the availability of the names you plan to supply prior to running the PowerShell deployment script.

1. Open Windows Azure PowerShell and navigate to the folder in which you downloaded and extracted the [Create a DocumentDB account, Azure Websites, and deploy a demo application sample](https://portalcontent.blob.core.chinacloudapi.cn/samples/CreateDocDBWebsiteTodo.zip) (e.g. C:\DocumentDBTemplates\CreateDocDBWebsiteTodo).


2. We're going to run the CreateDocDBWebsiteTodo.ps1 PowerShell script.  The script takes the following mandatory parameters:
	- WebsiteName: Specifies the Azure Websites name and is used to construct the URL that you will use to access the web site (e.g. if you specify "mydemodocdbwebapp", then the URL by which you will access the web site will be mydemodocdbwebapp.chinacloudsites.cn).

	- ResourceGroupName: Specifies the name of the Azure Resource Group to deploy. If the specified Resource Group doesn't exist, it will be created.

	- docDBAccountName: Specifies the name of the DocumentDB account to create.

	- location: Specifies the Azure location in which to create the DocumentDB and web site resources.  Valid values are China East, China North, China East, China North, China North, West Europe (note that the location value provided is case sensitive).


3. Here is an example command to run the script:

    	PS C:\DocumentDBTemplates\CreateDocDBWebAppTodo> .\CreateDocDBWebsiteTodo.ps1 -WebSiteName "mydemodocdbwebapp" -ResourceGroupName "myDemoResourceGroup" -docDBAccountName "mydemodocdbaccount" -location "China North"

	> [AZURE.TIP] Note that you will be prompted to enter your Azure account username and password as part of running the script.  The full deployment will take between 10 and 15 minutes to complete.  	

4. And here is an example of the resulting output: 

		VERBOSE: 1:06:00 PM - Created resource group 'myDemoResourceGroup' in location chinanorth'
		VERBOSE: 1:06:01 PM - Template is valid.
		VERBOSE: 1:06:01 PM - Create template deployment 'Microsoft.DocumentDBWebSiteTodo'.
		VERBOSE: 1:06:08 PM - Resource Microsoft.DocumentDb/databaseAccounts 'mydemodocdbaccount' provisioning status is running
		VERBOSE: 1:06:10 PM - Resource Microsoft.Web/serverFarms 'mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:14 PM - Resource microsoft.insights/alertrules 'CPUHigh mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:16 PM - Resource microsoft.insights/autoscalesettings 'mydemodocdbwebapp-myDemoResourceGroup' provisioning status is succeeded
		VERBOSE: 1:06:16 PM - Resource microsoft.insights/alertrules 'LongHttpQueue mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:21 PM - Resource Microsoft.Web/Sites 'mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:23 PM - Resource microsoft.insights/alertrules 'ForbiddenRequests mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:25 PM - Resource microsoft.insights/alertrules 'ServerErrors mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:06:25 PM - Resource microsoft.insights/components 'mydemodocdbwebapp' provisioning status is succeeded
		VERBOSE: 1:16:22 PM - Resource Microsoft.DocumentDb/databaseAccounts 'mydemodocdbaccount' provisioning status is succeeded
		VERBOSE: 1:16:22 PM - Resource Microsoft.DocumentDb/databaseAccounts 'mydemodocdbaccount' provisioning status is succeeded
		VERBOSE: 1:16:24 PM - Resource Microsoft.Web/Sites/config 'mydemodocdbwebapp/web' provisioning status is succeeded
		VERBOSE: 1:16:27 PM - Resource Microsoft.Web/Sites/Extensions 'mydemodocdbwebapp/MSDeploy' provisioning status is running
		VERBOSE: 1:16:35 PM - Resource Microsoft.Web/Sites/Extensions 'mydemodocdbwebapp/MSDeploy' provisioning status is succeeded

		ResourceGroupName : myDemoResourceGroup
		Location          : chinanorth
		Resources         : {mydemodocdbaccount, CPUHigh mydemodocdbwebapp, ForbiddenRequests mydemodocdbwebapp, LongHttpQueue mydemodocdbwebapp...}
		ResourcesTable    :
                    Name                                    Type                                   Location
                    ======================================  =====================================  =========
                    mydemodocdbaccount                      Microsoft.DocumentDb/databaseAccounts  chinanorth
                    CPUHigh mydemodocdbwebapp              microsoft.insights/alertrules          chinaeast
                    ForbiddenRequests mydemodocdbwebapp    microsoft.insights/alertrules          chinaeast
                    LongHttpQueue mydemodocdbwebapp        microsoft.insights/alertrules          chinaeast
                    ServerErrors mydemodocdbwebapp         microsoft.insights/alertrules          chinaeast
                    mydemodocdbwebapp-myDemoResourceGroup  microsoft.insights/autoscalesettings   chinaeast
                    mydemodocdbwebapp                      microsoft.insights/components          centralus
                    mydemodocdbwebapp                      Microsoft.Web/serverFarms              chinanorth
                    mydemodocdbwebapp                      Microsoft.Web/sites                    chinanorth

		ProvisioningState : Succeeded


5. Before we look at our sample application, let's understand what the template deployment accomplished:

	- An Azure Websites was created.

	- A DocumentDB account was created.

	- A Web Deploy package was deployed to the Azure Websites

	- The web site configuration was modified such that the DocumentDB endpoint and primary master key were surfaced as application settings.

	- A series of default monitoring rules were created.

	
6. In order to use the application, simply navigate to the web site URL (in the example above, the URL would be http://mydemodocdbwebapp.chinacloudsites.cn).  You'll see the following web site:

	![Sample Todo application](./media/documentdb-create-documentdb-website/image2.png)

7. Go ahead and create a couple of tasks and then let's open the [Windows Azure Management Portal](https://manage.windowsazure.cn).

8. Choose to browse Resource Groups and select the Resource Group we created during the deployment (in the sample above, myDemoResourceGroup).

	![Screenshot of the Azure Management Portal with the myDemoResourceGroup highlighted](./media/documentdb-create-documentdb-website/image3.png)
9.  Notice how the resource map in the Summary lens shows all of our related resources (DocumentDB account, Azure Websites, Monitoring).

	![Screenshot of the Summary lens](./media/documentdb-create-documentdb-website/image4.png)
10.  Click your DocumentDB account, and launch Query Explorer (near the bottom of the account blade).

	![Screenshot of the Resource Group and Account blades with the Query Explorer tile highlighted](./media/documentdb-create-documentdb-website/image8.png)

11. Run the default query, "SELECT * FROM c" and inspect the results.  Notice that the query has retrieved the JSON representation of the todo items you created in step 7 above.  Feel free to experiment with queries; for example, try running SELECT * FROM c WHERE c.isComplete = true to return all todo items which have been marked as complete.


	![Screenshot of the Query Explorer and Results blades showing the query results](./media/documentdb-create-documentdb-website/image5.png)
12. Feel free to explore the DocumentDB portal experience or modify the sample Todo application.  When you're ready, let's deploy another template.
	
<a id="Build"></a> 
## Step 3: Deploy the Document account and web site sample ##

Now let's deploy our second template.

> [AZURE.TIP] The template does not validate that the web site name and DocumentDB account name entered below are a) valid and b) available.  It is highly recommended that you verify the availability of the names you plan to supply prior to running the PowerShell deployment script.

1. Open Windows Azure PowerShell and navigate to the folder in which you downloaded and extracted the [Create a DocumentDB account and web site sample](https://portalcontent.blob.core.chinacloudapi.cn/samples/CreateDocDBWebSite.zip) (e.g. C:\DocumentDBTemplates\CreateDocDBWebsite).


2. We're going to run the CreateDocDBWebsite.ps1 PowerShell script.  The script takes the same parameters as the first template we deployed, namely:
	- WebsiteName: Specifies the Azure Websites name and is used to construct the URL that you will use to access the web site (e.g. if you specify "myotherdocumentdbwebapp", then the URL by which you will access the web site will be myotherdocumentdbwebapp.chinacloudsites.cn).

	- ResourceGroupName: Specifies the name of the Azure Resource Group to deploy.  If the specified Resource Group doesn't exist, it will be created.

	- docDBAccountName: Specifies the name of the DocumentDB account to create.

	- 	location: Specifies the Azure location in which to create the DocumentDB and web site resources.  Valid values are China East, China North, China East, China North, China North, West Europe (note that the location value provided is case sensitive).

3. Here is an example command to run the script:

    	PS C:\DocumentDBTemplates\CreateDocDBWebSite> .\CreateDocDBWebSite.ps1 -WebSiteName "myotherdocumentdbwebapp" -ResourceGroupName "myOtherDemoResourceGroup" -docDBAccountName "myotherdocumentdbdemoaccount" -location "China East"

	> [AZURE.TIP] Note that you will be prompted to enter your Azure account username and password as part of running the script.  The full deployment will take between 10 and 15 minutes to complete.  	

4. The deployment output will be very similar to the first template example. 
5. Before we open the Azure Management Portal, let's understand what this template deployment accomplished:

	- An Azure Websites was created.

	- A DocumentDB account was created.

	- 	The web site configuration was modified such that the Azure DocumentDB endpoint, primary master key, and secondary master key were surfaced as application settings.

	- 	A series of default monitoring rules were created.

6. Let's open the [Azure Management Portal](https://manage.windowsazure.cn), choose to browse Resource Groups and select the Resource Group we created during the deployment (in the sample above, myOtherDemoResourceGroup).
7. In the Summary lens, click the web site which was just deployed.

	![Screenshot of the Summary lens with the myotherdocumentdbwebapp web site highlighted](./media/documentdb-create-documentdb-website/image6.png)
8. On the web site's blade, click **All settings**, then **Application Settings** and note how there are application settings present for the DocumentDB endpoint and each of the DocumentDB master keys.

	![Screenshot of the web site, Settings, and application settings blades](./media/documentdb-create-documentdb-website/image7.png)
9. Feel free to continue exploring the Azure Management Portal, or follow one of our DocumentDB [samples](http://go.microsoft.com/fwlink/?LinkID=402386) to create your own DocumentDB application.

	
	
<a name="NextSteps"></a>
## Next steps

Congratulations! You've deployed DocumentDB, Azure Websites and a sample web site using Azure Resource Manager templates.

- To learn more about DocumentDB, click [here](http://azure.com/docdb).
- To learn more about Azure Websites, click [here](http://go.microsoft.com/fwlink/?LinkId=325362).
- To learn more about Azure Resource Manager templates, click [here](https://msdn.microsoft.com/zh-cn/library/azure/dn790549.aspx).


## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the Azure Management Portal](https://manage.windowsazure.cn/)

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](https://tryappservice.azure.com/), where you can immediately create a short-lived starter web site in Azure Websites. No credit cards required; no commitments.
 
