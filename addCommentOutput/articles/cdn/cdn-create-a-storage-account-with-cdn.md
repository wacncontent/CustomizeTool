<properties 
	pageTitle="How to use CDN | Windows Azure" 
	description="Learn how to use the Azure Content Delivery Network (CDN) to deliver high-bandwidth content by caching blobs and static content." 
	services="cdn" 
	documentationCenter=".net" 
	authors="camsoper" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="cdn"
	ms.date="12/02/2015"
	wacn.date=""/>


# Integrate a Storage Account with CDN

CDN can be enabled to cache content from your Azure storage. It offers developers a global solution for delivering high-bandwidth content by caching blobs and static content of compute instances at physical nodes in the United States, Europe, Asia, Australia and South America.


## Step 1: Create a storage account

Use the following procedure to create a new storage account for a
Azure subscription. A storage account gives access to 
Azure storage services. The storage account represents the highest level
of the namespace for accessing each of the Azure storage service
components: Blob services, Queue services, and Table services. For more <!-- deleted by customization information, refer to the [Introduction to Windows Azure Storage](/documentation/articles/storage-introduction). -->
<!-- keep by customization: begin -->
information about the Azure storage services, see [Using the
Azure Storage Services](http://msdn.microsoft.com/zh-cn/library/azure/gg433040.aspx).
<!-- keep by customization: end -->

To create a storage account, you must be either the service
administrator or a co-administrator for the associated subscription.

<!-- deleted by customization
> [AZURE.NOTE] There are several methods you can use to create a storage account, including the Azure Management Portal and Powershell.  For this tutorial, we'll be using the Azure Management Portal.  
-->
<!-- keep by customization: begin -->
> [AZURE.NOTE] For information about performing this operation by using the
Azure Service Management API, see the [Create Storage Account](http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx) reference topic.
<!-- keep by customization: end -->

**To create a storage account for an Azure subscription**

1.  Sign in to the [Azure Management <!-- deleted by customization Portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> Portal] <!-- keep by customization: end -->.
<!-- deleted by customization
2.  In the upper left corner, select **New**. In the **New** Dialog, select **Data  + Storage**, then click **Storage account**. Leave **Classic** selected as the deployment model, then click **Create**.

    The **Storage account** blade appears.

    ![Create Storage Account][create-new-storage-account]

4. In the **Storage** field, type a subdomain name. This entry can contain  3-24 lowercase letters and numbers.
-->
<!-- keep by customization: begin -->
2.  In the lower left corner, select **New**. In the **New** Dialog, select **Data Services**, then click **Storage**, then **Quick Create**.

    The **Create Storage Account** dialog appears.

    ![Create Storage Account][create-new-storage-account]

3. In the **URL** field, type a subdomain name. This entry can contain from 3-24 lowercase letters and numbers.
<!-- keep by customization: end -->

    This value becomes the host name within the URI that is used to
    address Blob, Queue, or Table resources for the subscription. To
    address a container resource in the Blob service, you would use a
    URI in the following format, where *&lt;StorageAccountLabel&gt;* refers
    to the value you typed in **Enter a URL**:

    http://*&lt;StorageAcountLabel&gt;*.blob.core.chinacloudapi.cn/*&lt;mycontainer&gt;*

    **Important:** The URL label forms the subdomain of the storage
    account URI and must be unique among all hosted services in 
    Azure.

	This value is also used as the name of this storage account in the portal, or when accessing this account programmatically.

<!-- deleted by customization
5.  Select a **Pricing tier** or use the default.  For more information on pricing tiers, see [Azure Storage Pricing](../../home/features/storage/#price).

6.  Select or create a **Resource Group**.  For more information on Resource Groups, see [Azure Resource Manager overview](/documentation/articles/resource-group-overview#resource-groups). 

7. Select the **Subscription** that the storage account will be used with.

8.  Click **Create**. The process of creating the storage account might take several minutes to complete.

9.  To verify that the storage account was created successfully, verify that the account appears in the items listed for **Storage** with a status of **Online**.


## Step 2: Create a new CDN profile

A CDN profile is a collection of CDN endpoints.  Each profile contains one or more CDN endpoints.  You may wish to use multiple profiles to organize your CDN endpoints by internet domain, web site, or some other criteria.

> [AZURE.TIP] If you already have a CDN profile that you want to use for this tutorial, proceed to [Step 3](#step-3-create-a-new-cdn-endpoint).

**To create a new CDN profile**

1. In the [Azure Management Portal](https://manage.windowsazure.cn), in the upper left, click **New**.  In the **New** blade, select **Media + CDN**, then **CDN**.

    The new CDN profile blade appears.
    
    ![New CDN Profile][new-cdn-profile]

2. Enter a name for your CDN profile. 

3. Select a **Pricing tier** or use the default.

4. Select or create a **Resource Group**.  It is not necessary that this is the same Resource Group as your storage account.

5. Select the **Subscription** for this CDN profile.  This will need to be the same subscription as the storage account for the purposes of this tutorial.

6. Select a **Location**.  This is the Azure location where your CDN profile information will be stored.  It has no impact on CDN endpoint locations.  It does not need to be the same location as the storage account.

7. Click the **Create** button to create the new profile.

## Step 3: Create a new CDN endpoint
-->
<!-- keep by customization: begin -->
4.  From the **Region/Affinity Group** drop-down list, select a region or affinity group for the storage account. Select an affinity group instead of a region if you want your storage services to be in the same data center with other Windows Azure services that you are using. This can improve performance, and no charges are incurred for egress.  

    **Note:** To create an affinity group, open the **Settings** area of the Management Portal, click **Affinity Groups**, and then click either **Add an affinity group** or **Add**. You can also create and manage affinity groups using the Windows Azure Service Management API. For more information, see [Operations on Affinity Groups].

5. From the **Subscription** drop-down list, select the subscription that the storage account will be used with.
6.  Click **Create Storage Account**. The process of creating the storage account might take several minutes to complete.
7.  To verify that the storage account was created successfully, verify that the account appears in the items listed for **Storage** with a status of **Online**.


## Step 2: Create a new CDN endpoint for your storage account

Once you enable CDN access to a storage account or hosted service, all
publicly available objects are eligible for CDN edge caching. If you
modify an object that is currently cached in the CDN, the new content
will not be available via the CDN until the CDN refreshes its content
when the cached content time-to-live period expires.
<!-- keep by customization: end -->

**To create a new CDN endpoint for your storage account**

<!-- deleted by customization
1. In the [Azure Management Portal](https://manage.windowsazure.cn), navigate to your CDN profile.  You may have pinned it to the dashboard in the previous step.  If you not, you can find it by clicking **Browse**, then **CDN profiles**, and clicking on the profile you plan to add your endpoint to.

    The CDN profile blade appears.
    
    ![CDN profile][cdn-profile-settings]
    
2. Click the **Add Endpoint** button.

    ![Add endpoint button][cdn-new-endpoint-button]

    The **Add an endpoint** blade appears.
    
    ![Add endpoint blade][cdn-add-endpoint]

3. Enter a **Name** for this CDN endpoint.  This name will be used to access your cached resources at the domain `<EndpointName>.azureedge.net`.

4. In the **Origin type** dropdown, select *Storage*.  

5. In the **Origin hostname** dropdown, select your storage account.

6. Leave the defaults for **Origin path**, **Origin host header**, and **Protocol/Origin port**.  You must specify at least one protocol (HTTP or HTTPS). 

    > [AZURE.NOTE] This configuration enables all of your publicly visible containers in your storage account for caching in the CDN.  If you want to limit the scope to a single container, use **Origin path**.  Note the container must have its visibility set to public.

7. Click the **Add** button to create the new endpoint.

8. Once the endpoint is created, it appears in a list of endpoints for the profile. The list view shows the URL to use to access cached content, as well as the origin domain.

    ![CDN endpoint][cdn-endpoint-success]

    > [AZURE.NOTE] The endpoint will not immediately be available for use.  It can take up to 90 minutes for the registration to propagate through the CDN network. Users who try to use the CDN domain name immediately may receive status code 404 until the content is available via the CDN.


## Step 4: Access CDN content
-->
<!-- keep by customization: begin -->
1. In the [Azure Management Portal], in the navigation pane, click **CDN**.

2. On the ribbon, click **New**. In the **New** dialog, select **Azure Websitess**, then **CDN**, then **Quick Create**.

3. In the **Origin Domain** dropdown, select the storage account you created in the previous section from the list of your available storage accounts. 

4. Click the **Create** button to create the new endpoint.

5. Once the endpoint is created, it appears in a list of endpoints for the subscription. The list view shows the URL to use to access cached content, as well as the origin domain. 

	The origin domain is the location from which the CDN caches
    content. The origin domain can be either a storage account or a cloud service; a storage account is used for the purposes of this example. Storage content is cached to edge servers according either to a cache-control setting that you specify, or to the default heuristics of the caching network. See [How to Manage Expiration of Blob Content](http://msdn.microsoft.com/zh-cn/library/gg680306.aspx) for more information. 


    > [AZURE.NOTE] The configuration created for the endpoint will not
    immediately be available; it can take up to 60 minutes for the
    registration to propagate through the CDN network. Users who try to
    use the CDN domain name immediately may receive status code 400
    (Bad Request) until the content is available via the CDN.


## Step 3: Access CDN content
<!-- keep by customization: end -->

To access cached content on the CDN, use the CDN URL provided in the portal. The address for a cached blob will be similar to the following:

<!-- deleted by customization
http://<*EndpointName*\>.azureedge.net/<*myPublicContainer*\>/<*BlobName*\>

> [AZURE.NOTE] Once you enable CDN access to a storage account or hosted service, all publicly available objects are eligible for CDN edge caching. If you modify an object that is currently cached in the CDN, the new content will not be available via the CDN until the CDN refreshes its content when the cached content time-to-live period expires.

## Step 5: Remove content from the CDN
-->
<!-- keep by customization: begin -->
http://<*CDNNamespace*\>.vo.msecnd.net/<*myPublicContainer*\>/<*BlobName*\>


## Step 4: Remove content from the CDN
<!-- keep by customization: end -->

If you no longer wish to cache an object in the Azure Content
Delivery Network (CDN), you can take one of the following steps:

<!-- deleted by customization
-   You can make the container private instead of public. See [Manage anonymous read access to containers and blobs](/documentation/articles/storage-manage-access-to-resources) for more information.
-   You can disable or delete the CDN endpoint using the Management Portal.
-   You can modify your hosted service to no longer respond to requests for the object.

An object already cached in the CDN will remain cached until the time-to-live period for the object expires or until the endpoint is purged. When the time-to-live period expires, the CDN will check to see whether the CDN endpoint is still valid and the object still anonymously accessible. If it is not, then the object will no longer be cached.

-->
<!-- keep by customization: begin -->
-   You can make the container private instead of public. See [Restrict Access to Containers and Blobs](http://msdn.microsoft.com/zh-cn/library/dd179354.aspx) for more information.
-   You can disable or delete the CDN endpoint using the Management 
    Portal.
-   You can modify your hosted service to no longer respond to requests for the 
    object.

An object already cached in the CDN will remain cached until the 
time-to-live period for the object expires. When the time-to-live period
expires, the CDN will check to see whether the CDN endpoint is still
valid and the object still anonymously accessible. If it is not, then
the object will no longer be cached.

The ability to immediately purge content is currently not supported on Azure Management Portal. Please contact [Azure support](/support/contact/)  if you need to immediately purge content. 
<!-- keep by customization: end -->

## Additional resources

<!-- deleted by customization
-   [How to Map CDN Content to a Custom Domain](/documentation/articles/cdn-map-content-to-custom-domain)
-->
<!-- keep by customization: begin -->
-   [How to Create an Affinity Group in Azure]
-   [How to: Manage Storage Accounts for an Azure Subscription]
-   [How to Map CDN Content to a Custom Domain]

[Create Storage Account]: http://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx
[Azure CDN Node Locations]: /documentation/articles/cdn-pop-locations
[Azure Management Portal]: https://manage.windowsazure.cn/
[billing plan]: /pricing/calculator/?scenario=full
[How to Register a Custom Subdomain Name for Accessing Blobs in Azure]: /documentation/articles/storage-custom-domain-name
[How to Create an Affinity Group in Azure]: http://msdn.microsoft.com/zh-cn/library/azure/ee460798.aspx
[Overview of the Azure CDN]: /documentation/articles/cdn-overview
[How to: Manage Storage Accounts for an Azure Subscription]: https://msdn.microsoft.com/zh-cn/library/azure/hh531793.aspx
[How to Map CDN Content to a Custom Domain]: /documentation/articles/cdn-map-content-to-custom-domain

<!-- keep by customization: end -->

[create-new-storage-account]: ./media/cdn-create-a-storage-account-with-cdn/CDN_CreateNewStorageAcct.png

<!-- deleted by customization
[new-cdn-profile]: ./media/cdn-create-a-storage-account-with-cdn/cdn-new-profile.png
[cdn-profile-settings]: ./media/cdn-create-a-storage-account-with-cdn/cdn-profile-settings.png
[cdn-new-endpoint-button]: ./media/cdn-create-a-storage-account-with-cdn/cdn-new-endpoint-button.png
[cdn-add-endpoint]: ./media/cdn-create-a-storage-account-with-cdn/cdn-add-endpoint.png
[cdn-endpoint-success]: ./media/cdn-create-a-storage-account-with-cdn/cdn-endpoint-success.png

-->
