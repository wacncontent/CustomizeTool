
To enable the non-SSL port, [browse](/documentation/articles/cache-configure/#configure-redis-cache-settings) to your cache in the [Azure portal](https://portal.azure.cn) and click **Settings > Access Ports**. Click **No** to enable the non-SSL port, and click **Save**.

![Redis cache settings](./media/redis-cache-non-ssl-port/redis-cache-non-ssl-port.png)



You can use the following PowerShell command to enable the non-SSL endpoint

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true

