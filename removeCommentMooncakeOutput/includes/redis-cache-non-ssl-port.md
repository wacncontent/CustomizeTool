You can use the following PowerShell command to enable the non-SSL endpoint

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true
