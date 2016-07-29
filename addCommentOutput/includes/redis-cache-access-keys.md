
To connect to the cache, your cache clients need the host name, ports, and keys. Some clients may refer to these items by slightly different names. To retrieve these items, [browse](/documentation/articles/cache-configure/#configure-redis-cache-settings) to your cache in the [Azure portal](https://portal.azure.cn) and click **Settings** or **All settings**.

![Redis cache settings](./media/redis-cache-access-keys/redis-cache-settings.png)

### Host name and ports

To access the host name and ports click **Properties**.

![Redis cache properties](./media/redis-cache-access-keys/redis-cache-properties.png)

### Access keys

To retrieve the access keys, click **Access keys**.

![Redis cache access keys](./media/redis-cache-access-keys/redis-cache-access-keys.png)


The cache endpoint and keys can be obtained by the following PowerShell Command:

	Get-AzureRmRedisCacheKey -Name "<your cache name>" -ResourceGroupName "<your resource group name>"

