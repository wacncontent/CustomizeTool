<!-- Ibiza portal: tested -->


1. Select the VM you wish to redeploy, and click the 'Redeploy' button in the 'Settings' blade:

	![Azure VM blade](./media/virtual-machines-common-redeploy-to-new-node/vmoverview.png)

2. Click the 'Redeploy' button to confirm the operation:

	![Redeploy a VM blade](./media/virtual-machines-common-redeploy-to-new-node/redeployvm.png)

>[AZURE.NOTE] Currently, in Azure China, the Cloud Environment for Microsoft/Compute, Microsoft/Network, and Microsoft/Storage is still using API Version 2015-06-15, while the latest Azure PowerShell is already upgraded to 2016-03-30. Hence, in order to use Microsoft/Compute, Microsoft/Network, and Microsoft/Storage in Azure China, you need to downgrade your Azure PowerShell to 1.2.2. You can download a full installer from [the release page of Azure PowerShell in GitHub](https://github.com/Azure/azure-powershell/releases).


	![VM updating](./media/virtual-machines-common-redeploy-to-new-node/vmupdating.png)

4. The **Status** will then change to *Starting* as the VM boots up on a new Azure host:

	![VM starting](./media/virtual-machines-common-redeploy-to-new-node/vmstarting.png)

5. After the VM finishes the boot process, the **Status** will then return to *Running*, indicating the VM has been successfully redeployed:







	![VM running](./media/virtual-machines-common-redeploy-to-new-node/vmrunning.png)
