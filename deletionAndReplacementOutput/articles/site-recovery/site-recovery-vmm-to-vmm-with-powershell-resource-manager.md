replacement:

deleted:

		`Add-AzureAccount`

replaced by:

		`Add-AzureAccount -Environment AzureChinaCloud`

reason: (powershell -Environment)

deleted:

		`Add-AzureAccount-Tenant "customer"`

replaced by:

		`Add-AzureAccount -Environment AzureChinaCloud -Tenant "customer"`

reason: (powershell -Environment)

