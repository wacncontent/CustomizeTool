<properties 
	pageTitle="How to configure Virtual Network support for a Premium Azure Redis Cache" 
	description="Learn how to create and manage Virtual Network support for your Premium tier Azure Redis Cache instances" 
	services="redis-cache" 
	documentationCenter="" 
	authors="steved0x" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="cache"
	ms.date="02/04/2016"
	wacn.date=""/>

# How to configure Virtual Network Support for a Premium Azure Redis Cache
Azure Redis Cache has different cache offerings which provide flexibility in the choice of cache size and features, including the new Premium tier.

The Azure Redis Cache premium tier includes clustering, persistence, and virtual network (VNET) support. A VNET is a representation of your own network in the cloud. When an Azure Redis Cache instance is configured with a VNET, it is not publicly addressable and can only be accessed from clients within the VNET. This article describes how to configure Virtual Network Support for a premium Azure Redis Cache instance.

For information on other premium cache features, see [How to configure persistence for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-persistence) and [How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering).

## Why VNET?
[Azure Virtual Network (VNET)](/home/features/networking/) deployment provides enhanced security and isolation for your Azure Redis Cache, as well as subnets, access control policies, and other features to further restrict access to Azure Redis Cache.

## Virtual network support

Virtual Network (VNET) support is configured on the **New Redis Cache** blade during cache creation. To create a cache, sign-in to the [Azure Management Portal](https://manage.windowsazure.cn) and click **New** > **DATA SERVICE** > **Redis Cache**.

![Create a Redis Cache][redis-cache-new-cache-menu]

To configure VNET support, first select one of the **Premium** caches in the **Choose your pricing tier** blade.

![Choose your pricing tier][redis-cache-premium-pricing-tier]

Azure Redis Cache VNET integration is configured in the **Virtual Network (classic)** blade. From here you can select an existing classic VNET. To use a new VNET, follow the steps in [Create a virtual network (classic) by using the Azure Management Portal](/documentation/articles/virtual-networks-create-vnet-classic-pportal) and then return to the **Redis Cache Virtual Network** blade to select it.

>[AZURE.NOTE] Azure Redis Cache works with classic VNETs. For information on creating a classic VNET, see [Create a virtual network (classic) by using the Azure Management Portal](/documentation/articles/virtual-networks-create-vnet-classic-pportal). For information on connecting classic VNETs to ARM VNETS, see [Connecting classic VNets to new VNets](/documentation/articles/virtual-networks-arm-asm-s2s).

Click **Virtual Network (classic)** on the **New Redis Cache** blade, and select the desired VNET from the drop-down list to select and configure your VNET.

![Virtual network][redis-cache-vnet]

Select the desired subnet from the **Subnet** drop-down list.

![Virtual network][redis-cache-vnet-ip]

The **Static IP address** field is optional. If none is specified here, one will be chosen from the selected subnet. If a specific static IP is desired, type the desired **Static IP address** and click **OK** to save the VNET configuration. If the selected static IP is already use, an error message is displayed.

Once the cache is created, you can view the IP address and other information about the VNET by clicking **Virtual Network** from the **Settings** blade.

![Virtual network][redis-cache-vnet-info]



In Azure China, Redis Cache can only be managed by Azure PowerShell or Azure CLI


[AZURE.INCLUDE [azurerm-azurechinacloud-environment-parameter](../includes/azurerm-azurechinacloud-environment-parameter.md)]


Use the following PowerShell Script to create a cache:

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-ChinaNorth"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 6GB -Sku Premium -VirtualNetwork /subscriptions/{subid}/Microsoft.ClassicNetwork/VirtualNetworks/vnet1 -Subnet Front -StaticIP 10.10.1.5

The **-StaticIP** Parameter is optional. If the selected static IP is already use, an error message is displayed. If none is specified here, one will be chosen from the selected subnet.

Once the cache is created, it can be accessed only by clients within the same VNET.


>[AZURE.IMPORTANT] To access your Azure Redis cache instance when using a VNET, pass the static IP address of the cache in the VNET as the first parameter, and pass in an `sslhost` parameter with the endpoint of your cache. In the following example the static IP address is `172.160.0.99` and the cache endpoint is `contoso5.redis.cache.chinacloudapi.cn`.

	private static Lazy<ConnectionMultiplexer> lazyConnection = new Lazy<ConnectionMultiplexer>(() =>
	{
	    return ConnectionMultiplexer.Connect("172.160.0.99,sslhost=contoso5.redis.cache.chinacloudapi.cn,abortConnect=false,ssl=true,password=password");
	});
	
	public static ConnectionMultiplexer Connection
	{
	    get
	    {
	        return lazyConnection.Value;
	    }
	}

## Azure Redis Cache VNET FAQ

The following list contains answers to commonly asked questions about the Azure Redis Cache scaling.

## What are some common misconfiguration issues with Azure Redis Cache and VNETs?

When Azure Redis Cache is hosted in a VNET, the ports in the following table are used. If these ports are blocked, the cache may not function correctly. Having one or more of these ports blocked is the most common misconfiguration issue when using Azure Redis Cache in a VNET.

| Port(s)     | Direction        | Transport Protocol | Purpose                                                                           | Remote IP                           |
|-------------|------------------|--------------------|-----------------------------------------------------------------------------------|-------------------------------------|
| 80, 443     | Outbound         | TCP                | Redis dependencies on Azure Storage/PKI (Internet)                                | *                                   |
| 53          | Outbound         | TCP/UDP            | Redis dependencies on DNS (Internet/VNet)                                         | *                                   |
| 6379, 6380  | Inbound          | TCP                | Client communication to Redis, Azure Load Balancing                               | VIRTUAL_NETWORK, AZURE_LOADBALANCER |
| 8443        | Inbound/Outbound | TCP                | Implementation Detail for Redis                                                   | VIRTUAL_NETWORK                     |
| 8500        | Inbound          | TCP/UDP            | Azure Load Balancing                                                              | AZURE_LOADBALANCER                  |
| 10221-10231 | Inbound/Outbound | TCP                | Implementation Detail for Redis (can restrict remote endpoint to VIRTUAL_NETWORK) | VIRTUAL_NETWORK, AZURE_LOADBALANCER |
| 13000-13999 | Inbound          | TCP                | Client communication to Redis Clusters, Azure Load Balancing                      | VIRTUAL_NETWORK, AZURE_LOADBALANCER |
| 15000-15999 | Inbound          | TCP                | Client communication to Redis Clusters, Azure Load Balancing                      | VIRTUAL_NETWORK, AZURE_LOADBALANCER |
| 16001       | Inbound          | TCP/UDP            | Azure Load Balancing                                                              | AZURE_LOADBALANCER                  |
| 20226       | Inbound+Outbound | TCP                | Implementation Detail for Redis Clusters                                          | VIRTUAL_NETWORK                     |




## Can I use VNETs with a standard or basic cache?

VNETs can only be used with premium caches.

## Next steps
Learn how to use more premium cache features.

-	[How to configure persistence for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-persistence)
-	[How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering)





  
<!-- IMAGES -->

[redis-cache-new-cache-menu]: ./media/cache-how-to-premium-vnet/redis-cache-new-cache-menu.png

[redis-cache-premium-pricing-tier]: ./media/cache-how-to-premium-vnet/redis-cache-premium-pricing-tier.png

[redis-cache-vnet]: ./media/cache-how-to-premium-vnet/redis-cache-vnet.png

[redis-cache-vnet-ip]: ./media/cache-how-to-premium-vnet/redis-cache-vnet-ip.png

[redis-cache-vnet-info]: ./media/cache-how-to-premium-vnet/redis-cache-vnet-info.png

