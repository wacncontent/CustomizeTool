<properties
	pageTitle="Create an Azure Search service in the portal | Windows Azure | Hosted cloud search service"
	description="Add free or standard Azure Search to an existing subscription using the Azure Management Portal. Azure Search is cloud hosted search service for custom apps."
	services="search"
	documentationCenter=""
	authors="HeidiSteen"
	manager="mblythe"
	editor=""
    tags="azure-portal"/>

<tags
	ms.service="search"
	ms.date="11/04/2015"
	wacn.date=""/>

# Create an Azure Search service in the Azure <!-- deleted by customization Management Portal --><!-- keep by customization: begin --> portal <!-- keep by customization: end -->

<!-- deleted by customization Windows --><!-- keep by customization: begin --> Microsoft <!-- keep by customization: end --> Azure Search is a <!-- deleted by customization hosted cloud search --><!-- keep by customization: begin --> new <!-- keep by customization: end --> service that allows you to embed search functionality into custom applications. It provides a search engine and storage of your search data, which you <!-- deleted by customization can --> access and manage <!-- deleted by customization through --><!-- keep by customization: begin --> using <!-- keep by customization: end --> the Azure <!-- deleted by customization Management Portal --><!-- keep by customization: begin --> portal <!-- keep by customization: end -->, a .NET SDK, or a REST API. Key features include auto-complete queries, fuzzy matching, hit-highlighting, faceted navigation, <!-- deleted by customization scoring profiles, --> and multi-language support. For more information about what Azure Search does, see <!-- deleted by customization [What is --><!-- keep by customization: begin --> [Introducing <!-- keep by customization: end --> Azure <!-- deleted by customization Search](/documentation/articles/seach-what-is-search) --><!-- keep by customization: begin --> Search](fundamentals-azure-search-chappell/) <!-- keep by customization: end -->.

## Add Azure Search to your subscription <!-- deleted by customization for free -->

As an administrator, you can add Azure Search to an existing <!-- deleted by customization Azure --> subscription at no cost when choosing the shared service, or at the standard rate when opting in for dedicated resources.

1. Sign in to the [Azure <!-- deleted by customization Management Portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> portal](https://portal.azure.com) <!-- keep by customization: end -->.

2. In the Jumpbar, click **New** > **Data + storage** > **Search**.

     ![][1]

3. Configure the service name, pricing tier, resource group, subscription, and location. These settings are required and cannot be changed once the service is provisioned.

     ![][2]

	- **Service name** must be unique, lowercase, and under 15 characters, with no spaces. This name becomes part of the endpoint of your Azure Search service. See [Naming <!-- deleted by customization Rules](https://msdn.microsoft.com/zh-cn/library/azure/dn857353.aspx) --><!-- keep by customization: begin --> Rules](https://msdn.microsoft.com/library/azure/dn857353.aspx) <!-- keep by customization: end --> for more information about naming conventions.

	- **Pricing Tier** determines capacity and billing. Both tiers provide the same features, but at different resource levels.

		- **Free**  runs on clusters that are shared with other subscribers. It offers enough capacity to try out tutorials and write proof-of-concept code, but is not intended for production applications. Deploying a free service typically only takes a few minutes.
		- **Standard** runs on dedicated resources and is highly scalable. Initially, a standard service is provisioned with one replica and one partition, but you can adjust capacity once the service is created. Deploying a standard service takes longer, usually about 15 minutes.

	- **Resource Groups** are containers for services and resources used for a common purpose. For example, if you're building a custom search application based on Azure Search, the <!-- deleted by customization web sites --><!-- keep by customization: begin --> Web Apps <!-- keep by customization: end --> feature in Azure <!-- deleted by customization Websites --><!-- keep by customization: begin --> App Service <!-- keep by customization: end -->, and Azure Blob storage, you could create a resource group that keeps these services together in the portal management pages.

	- **Subscription** allows you to choose among multiple subscriptions, if you have more than one subscription.

	- **Location** is the datacenter region. Currently, all resources must run in the same datacenter. Distributing resources across multiple datacenters is not supported.

4. Click **Create** to provision the service.

Watch for notifications in the Jumpbar. A notice will appear when the service is ready to use.

<!-- keep by customization: begin -->
<a id="sub-2"></a>
## Find the service name and api-keys of your Azure Search service

After the service is created, you can return to the Azure portal to get the URL or `api-key`. Connections to your Azure Search service requires that you have both the URL and an `api-key` to authenticate the call.

1. In the Jumpbar, click **Home** and then click the Azure Search service to open the service dashboard.

2. On the service dashboard, you'll see tiles for essential information, as well as the key icon for accessing the admin keys.

  	![][3]

3. Copy the service URL and an admin key. You will need them for your next task, [Test service operations](#sub-4).

<!-- keep by customization: end -->
<a id="sub-3"></a>
<!-- deleted by customization
## Add a Standard tier search service to get dedicated resources

Many customers start with the free service, and then switch up to the Standard tier to accommodate larger workloads. Standard tier gives you dedicated resources in an Azure data center that can be used only by you. 

Azure Search operations require both storage and service replicas. In contrast with the free service which has no option for adding resources, Standard tier lets you scale up to add more storage or query support by bumping up whichever resource is the more critical to your scenario.

To use the Standard tier, you have to create a new search service at that pricing level. You can repeat the previous steps in this article to create a new Azure Search service. Note that setting up dedicated resources can take a while, up to 15 minutes or longer.
-->
<!-- keep by customization: begin -->
## Upgrade to the standard tier

Many customers start with the free service, and then upgrade to the standard tier when query performance or storage becomes inadequate for the workloads they need to run. The standard tier gives you dedicated resources in an Azure datacenter that can be used only by you. Azure Search operations require both storage and service replicas. When you sign up for standard search, you can optimize service configuration to use more of whichever resource is the most important to your scenario.

To use the standard tier, repeat the previous steps in this article to create a new Azure Search service, choosing the Standard pricing tier. Note that setting up dedicated resources can take a while, up to 15 minutes or longer.
<!-- keep by customization: end -->

There is no in-place upgrade of the free version. Switching to standard, with its potential for scale, requires a new service. You will need to reload the indexes and documents used by your search application.

An Azure Search service at the standard tier is created with one replica and partition each, but can be easily re-scaled at higher resource levels.

1.	Return to the service dashboard after the service is created.

2.	Click the **Scale** tile.

3.	Use the sliders to add replicas, partitions, or both.

Additional replicas and partitions are billed in terms of search units. The total search units required to support any particular resource configuration are shown on the page, as you add resources.

You can check [Pricing Details](http://go.microsoft.com/fwlink/p/?LinkID=509792) to get the per-unit billing information. See [Limits and <!-- deleted by customization constraints](/documentation/articles/search-limits-quotas-capacity) --><!-- keep by customization: begin --> constraints](search-limits-quotas-capacity.md) <!-- keep by customization: end --> for help in deciding how to configure partition and replica combinations.
<!-- deleted by customization

<a id="sub-2"></a>
## Find the service name and api-keys of your Azure Search service

After the service is created, you can return to the Azure Management Portal to get the URL or `api-key`. Connections to your Azure Search service requires that you have both the URL and an `api-key` to authenticate the call.

1. In the Jumpbar, click **Home** and then click the Azure Search service to open the service dashboard.

2. On the service dashboard, you'll see tiles for essential information, as well as the key icon for accessing the admin keys.

  	![][3]

3. Copy the service URL and an admin key. You will need them for your next task, [Test service operations](#sub-4).

-->

<a id="sub-4"></a>
## Test service operations

Confirming that your service is operational and accessible from a client application is the final step in configuring Azure Search. You can use either of the following links for a code-free approach to verifying service availability.

- [How to use Chrome Postman with Azure <!-- deleted by customization Search](/documentation/articles/search-chrome-postman) --><!-- keep by customization: begin --> Search](search-chrome-postman.md) <!-- keep by customization: end -->
- [How to use Telerik Fiddler with Azure <!-- deleted by customization Search](/documentation/articles/search-fiddler) --><!-- keep by customization: begin --> Search](search-fiddler.md) <!-- keep by customization: end -->

<!--Next steps and links -->
<a id="next-steps"></a>
## Next steps

The following information shows you how to build and manage search applications that use Azure Search.

- [How to use Azure Search in <!-- deleted by customization .NET](/documentation/articles/search-howto-dotnet-sdk) --><!-- keep by customization: begin --> .NET](search-howto-dotnet-sdk.md) <!-- keep by customization: end -->

<!-- deleted by customization
- [Manage your search solution in Windows Azure](/documentation/articles/search-manage)

- [Azure Search on MSDN](http://msdn.microsoft.com/zh-cn/library/dn798933.aspx)
-->
<!-- keep by customization: begin -->
- [Manage your search solution in Microsoft Azure](search-manage.md)

- [Azure Search on MSDN](http://msdn.microsoft.com/library/dn798933.aspx)
<!-- keep by customization: end -->

- [Channel 9 video: Introduction to Azure Search](http://channel9.msdn.com/Shows/Data-Exposed/Introduction-To-Azure-Search)


<!--Anchors-->
[Find the service name and api-keys of your Azure Search service]: #sub-2
[Upgrade to the standard tier]: #sub-3
[Test service operations]: #sub-4
[Next steps]: #next-steps

<!--Image references-->
[1]: ./media/search-create-service-portal/create-search-portal-1.PNG
[2]: ./media/search-create-service-portal/create-search-portal-2.PNG
[3]: ./media/search-create-service-portal/create-search-portal-3.PNG
