<!-- Ibiza portal: tested -->


If you have been facing difficulties troubleshooting Remote Desktop (RDP) connection to Windows based Azure virtual machine or in troubleshooting SSH connection to Linux based Azure virtual machine, then this article will help you mitigate them all by yourself, without looping in support and resizing the virtual machine.  Azure will redeploy your virtual machine when you invoke redeploy operation through Azure PowerShell. 

Please note that after this operation is completed, ephemeral disk data will be lost and dynamic IP addresses associated with virtual machine will be updated. 


## Using Azure PowerShell

>[AZURE.NOTE] Currently, in Azure China, the Cloud Environment for Microsoft/Compute, Microsoft/Network, and Microsoft/Storage is still using API Version 2015-06-15, while the latest Azure PowerShell is already upgraded to 2016-03-30. Hence, in order to use Microsoft/Compute, Microsoft/Network, and Microsoft/Storage in Azure China, you need to downgrade your Azure PowerShell to 1.2.2. You can download a full installer from [the release page of Azure PowerShell in GitHub](https://github.com/Azure/azure-powershell/releases).

Make sure you have the latest Azure PowerShell 1.x installed on your machine. Please read [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for more information.

Use this Azure PowerShell command to redeploy your virtual machine:

	Set-AzureRmVM -Redeploy -ResourceGroupName $rgname -Name $vmname 


While this command is running, check your virtual machine in the [Azure portal Preview](https://portal.azure.cn). Notice that the VM's **Status** changes as following:

1. Initial **Status** is *Running*

	![Redeploy initial status](./media/virtual-machines-common-redeploy-to-new-node/statusrunning1.png)

2. **Status** changes to *Updating*

	![Redeploy status Updating](./media/virtual-machines-common-redeploy-to-new-node/statusupdating.png)

3. **Status** changes to *Starting*

	![Redeploy status Starting](./media/virtual-machines-common-redeploy-to-new-node/statusstarting.png)

4. **Status** changes back to *Running*

	![Redeploy final status](./media/virtual-machines-common-redeploy-to-new-node/statusrunning2.png)

When the **Status** is back to *Running*, the VM has successfully redeployed.