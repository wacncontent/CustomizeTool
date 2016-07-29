
To create a premium cache, sign-in to the [Azure Portal](https://portal.azure.cn) and click **New** > **DATA SERVICE** > **Redis Cache**.

![Create cache](./media/redis-cache-premium-create/redis-cache-new-cache-menu.png)

>[AZURE.NOTE] In addition to creating caches in the Azure Portal, you can also create them using ARM templates, PowerShell, or Azure CLI. For more information, see [Create a cache](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache/#create-a-cache).
To configure premium features, first select one of the premium pricing tiers in the **Choose your pricing tier** blade.

![Choose your pricing tier](./media/redis-cache-premium-create/redis-cache-premium-pricing-tier.png)





Use the following PowerShell Script to create a cache:

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-ChinaNorth"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 6GB -Sku Premium -ShardCount 2

