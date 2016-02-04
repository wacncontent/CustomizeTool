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


# Using CDN for Azure

The Azure Content Delivery Network (CDN) is the fundamental building block to scale any HTTP application in Azure. It offers Azure customers a global solution by caching and delivering content close to end users. As a result, instead of hitting origin every single time, user requests get intelligently routed to the best performed CDN edge POP. This significantly increases the performance and user experience. For a current list of
<!-- deleted by customization
CDN node locations, see [Azure Content Delivery Network (CDN) POP Locations](/documentation/articles/cdn-pop-locations).
-->
<!-- keep by customization: begin -->
CDN node locations, see [Azure CDN Node Locations].
<!-- keep by customization: end -->

The benefits of using CDN to cache Azure data include:

-Better performance and user experience for end users who are far from a content source <!-- keep by customization: begin -->, <!-- keep by customization: end --> and are using applications where many <!-- deleted by customization HTTP requests --><!-- keep by customization: begin --> 'internet trips' <!-- keep by customization: end --> are required to load content <!-- deleted by customization. -->
-Large distributed scale to better handle instantaneous high load, say, at the start of an event such as a product launch <!-- deleted by customization. -->
-By distributing user requests and serving content from global edge POPs, less traffic is sent to <!-- keep by customization: begin --> origin thus offload <!-- keep by customization: end --> the origin.

<!-- deleted by customization
>[AZURE.TIP] Azure CDN can distrubute content from a variety of origins.  Integrated origins within Azure include Azure Websites, Cloud Services, blob storage, and Media Service.  You can also define a custom origin using any publicly accessible web address.

##How to enable CDN

1. Create a CDN profile with endpoint(s) pointing to your origin

	A CDN profile is a collection of CDN endpoints.  Each profile contains one or more CDN endpoints.  Once you have created a CDN profile, you can create a new CDN endpoint using the origin you have chosen.
	
	>[AZURE.NOTE] A single Azure subscription is limited to four CDN profiles.  Each CDN profile is limited to four CDN endpoints.
	>
	> CDN pricing is applied at the CDN profile level.  If you wish to use a mix of Standard and Premium CDN features, you will need multiple CDN profiles.
	
	For a detailed tutorial on creating CDN profiles and endpoints, see [How to Enable the Content Delivery Network for Azure](/documentation/articles/cdn-create-new-endpoint).   
	
2. Set up your CDN configuration 

	You can enable a number of features for your CDN endpoint, such as [caching policy](/documentation/articles/cdn-caching-policy), [query string caching](/documentation/articles/cdn-query-string), [rules engine](/documentation/articles/cdn-rules-engine), and more.  For details, see the **Manage** menu on the left.  

3. Access CDN content

	To access cached content on the CDN, use the CDN URL provided in the portal. For example, the address for a cached blob will be similar to the following: `http://<identifier>.azureedge.net/<myPublicContainer>/<BlobName>`

## Caching content from Azure storage

Once the CDN is enabled on a Azure storage account, any blobs that are in public containers and are available for anonymous access will be cached via the CDN. Only blobs that are publicly available can be cached with the Azure CDN. To make a blob publicly available for anonymous access, you must denote its container as public. Once you do so, all blobs within that container will be available for anonymous read access. You have the option of making container data public as well, or restricting access only to the blobs within it. See [Manage Access to Azure Storage Resources](/documentation/articles/storage-manage-access-to-resources) for information on managing access control for containers and blobs.

For best performance, use CDN edge caching for delivering blobs less than 10 GB in size.

When you enable CDN access for a storage account, the Management Portal provides you with a CDN domain name in the following format: `http://<identifier>.azureedge.net/`. This domain name can be used to access blobs in a public container. For example, given a public container named music in a storage account named myaccount, users can access the blobs in that container using either of the following two URLs:

- **Azure Blob service URL**: `http://myAccount.blob.core.chinacloudapi.cn/music/` 
- **Azure CDN URL**: `http://<identifier>.azureedge.net/music/` 

## Caching content from Azure websites

You can enable CDN from your websites to cache your web contents, such as images, scripts, and stylesheets. See [Integrate an Azure Website with Azure CDN](/documentation/articles/cdn-websites-with-cdn).

When you enable CDN access for a website, the Management Portal provides you with a CDN domain name in the following format: `http://<identifier>.azureedge.net/`. This domain name can be used to retrieve objects from a website. For example, given a public container named cdn and an image file called music.png, users can access the object using either of the following two URLs:

- **Azure Website URL**: `http://mySiteName.chinacloudsites.cn/cdn/music.png` 
- **Azure CDN URL**: `http://<identifier>.azureedge.net/cdn/music.png`
 
## Caching content from Azure cloud services

You can cache objects to the CDN that are provided by a Azure cloud service. 

Caching for cloud services has the following constraints: 


- The CDN should be used to cache static content only.

	>[AZURE.WARNING] Caching of highly volatile or truly dynamic content may adversely affect your performance or cause content problems, all at increased cost.
- Your cloud service must be deployed to in a production deployment.
- Your cloud service must provide the object on port 80 using HTTP.
- The cloud service must place the content to be cached in, or delivered from, the /cdn folder on the cloud service.

When you enable CDN access for on a cloud service, the Management Portal provides you with a CDN domain name in the following format: `http://<identifier>.azureedge.net/`. This domain name can be used to retrieve objects from a cloud service. For example, given a cloud service named myHostedService and an ASP.NET web page called music.aspx that delivers content, users can access the object using either of the following two URLs:


- **Azure cloud service URL**: `http://myHostedService.chinacloudapp.cn/music.aspx` 
- **Azure CDN URL**: `http://<identifier>.azureedge.net/music.aspx` 

## Caching content from custom origins

You can cache objects to the CDN that are provided by any publicly accessible web site. 

Caching for custom origins has the following constraints: 

- The CDN should be used to cache static content only.

	>[AZURE.WARNING] Caching of highly volatile or truly dynamic content may adversely affect your performance or cause content problems, all at increased cost.
- The content on the custom origin must be hosted on a server with a public IP address.  CDN edge nodes are incapable of retrieving assets from intranet servers behind a firewall.

When you enable CDN access for on a custom origin, the Azure Management Portal provides you with a CDN domain name in the following format: `http://<identifier>.azureedge.net/`. This domain name can be used to retrieve objects from the custom origin. For example, given a site located at www.contoso.com and an ASP.NET web page called music.aspx that delivers content, users can access the object using either of the following two URLs:


- **Custom origin URL**: `http://www.contoso.com/music.aspx` 
- **Azure CDN URL**: `http://<identifier>.azureedge.net/music.aspx` 

## Caching specific content with query strings

You can use query strings to differentiate objects retrieved from an origin. For example, if the origin displays a chart that can vary you can pass a query string to retrieve the specific chart required. For example: 

`http://<identifier>.azureedge.net/chart.aspx?item=1`

Query strings are passed as string literals. If you have a service that takes two parameters, such as `?area=2&item=1` and make subsequent calls to the origin using `?item=1&area=2`, you will cache two copies of the same object.

For more information on query string caching, see [Controlling caching behavior of CDN requests with query strings](/documentation/articles/cdn-query-string).

## Accessing cached content over HTTPS

Azure allows you to retrieve content from the CDN using HTTPS calls. This allows you to incorporate content cached in the CDN into secure web pages without receiving warnings about mixed security content types.

Accessing CDN content using HTTPS has the following constraints:


- You must use the certificate provided by the CDN. Third party certificates are not supported.
- You must use the CDN domain to access content. HTTPS support is not available for custom domain names (CNAMEs) since the CDN does not support custom certificates at this time.

For more information on enabling HTTPS for CDN content, see [How to Enable the Content Delivery Network (CDN) for Azure](/documentation/articles/cdn-create-new-endpoint).


## Accessing cached content with custom domains

You can map the CDN HTTP endpoint to a custom domain name and use that name to request objects from the CDN.

For more information on mapping a custom domain, see [How to Map Content Delivery Network (CDN) Content to a Custom Domain](/documentation/articles/cdn-map-content-to-custom-domain).

## Managing CDN programmatically

Windows Azure CDN can be managed programmatically using the [CDN Resource Provider REST API](https://msdn.microsoft.com/zh-cn/library/mt634456.aspx). 
-->
<!-- keep by customization: begin -->
Existing CDN customers can now use the Azure CDN in the [Azure Management Portal]. The CDN is an add-on feature to your subscription and has a separate [billing plan].

##Step 1: Create a CDN origin in Azure

CDN origin is the location from which CDN fetch content and cache at the edge POPs. The integrated Azure origin includes Azure Apps, Cloud Services, Storage and Media services. 

## Step 2: Create a CDN endpoint pointing to your Azure origin

Once your origin is set up, it will be available in the origin list when you [create a new CDN endpoint](/documentation/articles/cdn-create-new-endpoint).  

> [AZURE.NOTE] The configuration created for the endpoint will not immediately be available; it can take up to 60 minutes for the registration to propagate through the CDN network. Users who try to use the CDN domain name immediately may receive status code 400 (Bad Request) until the content is available via the CDN.

## Step 3: Set up your CDN configuration 

You can enable a number of features for your CDN endpoint, such as caching policy, query string caching, etc.  

## Step 4: Access CDN content

To access cached content on the CDN, use the CDN URL provided in the portal. For example, the address for a cached blob will be similar to the following: http://<*CDNNamespace*\>.vo.msecnd.net/<*myPublicContainer*\>/<*BlobName*\>

<!-- keep by customization: end -->


## See also

<!-- deleted by customization
- [How to Enable the Content Delivery Network for Azure](/documentation/articles/cdn-create-new-endpoint)
- [Overview of the Azure Content Delivery Network (CDN)](/documentation/articles/cdn-overview)
- [Purge an Azure CDN Endpoint](/documentation/articles/cdn-purge-endpoint)
- [CDN Resource Provider REST API](https://msdn.microsoft.com/zh-cn/library/mt634456.aspx)

-->
<!-- keep by customization: begin -->
[Overview of the Azure Content Delivery Network (CDN)](/documentation/articles/cdn-overview)
 
<!-- keep by customization: end -->
