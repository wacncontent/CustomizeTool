replacement:

deleted:

		[AZURE.INCLUDE [powershell-preview-inline-include](../includes/powershell-preview-inline-include.md)]

replaced by:

		If you have not previously used Azure PowerShell with Resource Manager, see [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager).
		For the purposes of this article, we'll assume you've already added an account and selected a subscription with the resources you want to tag.
		
		Tagging is only available for resources and resource groups available from [Resource Manager](http://msdn.microsoft.com/zh-cn/library/azure/dn790568.aspx), so the next thing we need to do is switch to use Resource Manager.
		
		    Switch-AzureMode AzureResourceManager

reason: ()

deleted:

		centralus

replaced by:

		chinaeast

reason: ()

deleted:

		southcentralus

replaced by:

		chinaeast

reason: ()

deleted:

		southcentralus

replaced by:

		chinaeast

reason: ()

deleted:

		The process is the same for resources, except you'll use the **Get-AzureRmResource** and **Set-AzureRmResource** cmdlets. 
		
		To get resource groups with a specific tag, use **Find-AzureRmResourceGroup** cmdlet with the **-Tag** parameter.
		
		    PS C:\> Find-AzureRmResourceGroup -Tag @{ Name="env"; Value="demo" } | %{ $_.ResourceGroupName }
		    rbacdemo-group
		    tag-demo
		
		For Azure PowerShell versions earlier than 1.0 Preview use the following commands to get resources with a specific tag.

replaced by:

		The process is the same for resources, except you'll use the `Get-AzureResource` and `Set-AzureResource` cmdlets. To get resources or resource groups with a specific tag, use `Get-AzureResource` or `Get-AzureResourceGroup` cmdlet with the `-Tag` parameter.

reason: ()

