<!-- not suitable for Mooncake -->

<properties 
   pageTitle="How to create NSGs in ARM mode using a template| Windows Azure"
   description="Learn how to create and deploy NSGs in ARM using a template"
   services="virtual-network"
   documentationCenter="na"
   authors="telmosampaio"
   manager="carmonm"
   editor="tysonn"
   tags="azure-resource-manager"
/>
<tags
	ms.service="virtual-network"
	ms.date="02/02/2016"
	wacn.date=""/>

# How to create NSGs using a template

[AZURE.INCLUDE [virtual-networks-create-nsg-selectors-arm-include](../includes/virtual-networks-create-nsg-selectors-arm-include.md)]

[AZURE.INCLUDE [virtual-networks-create-nsg-intro-include](../includes/virtual-networks-create-nsg-intro-include.md)]

[AZURE.INCLUDE [azure-arm-classic-important-include](../includes/azure-arm-classic-important-include.md)] This article covers the Resource Manager deployment model. You can also [create NSGs in the classic deployment model](/documentation/articles/virtual-networks-create-nsg-classic-ps).

[AZURE.INCLUDE [virtual-networks-create-nsg-scenario-include](../includes/virtual-networks-create-nsg-scenario-include.md)]

## NSG resources in a template file

You can view and download the [sample template](https://raw.githubusercontent.com/telmosampaio/azure-templates/master/201-IaaS-WebFrontEnd-SQLBackEnd/NSGs.json).

The section below shows the definition of the front end NSG, based on the scenario above.

      "apiVersion": "2015-06-15",
      "type": "Microsoft.Network/networkSecurityGroups",
      "name": "[parameters('frontEndNSGName')]",
      "location": "[resourceGroup().location]",
      "tags": {
        "displayName": "NSG - Front End"
      },
      "properties": {
        "securityRules": [
          {
            "name": "rdp-rule",
            "properties": {
              "description": "Allow RDP",
              "protocol": "Tcp",
              "sourcePortRange": "*",
              "destinationPortRange": "3389",
              "sourceAddressPrefix": "Internet",
              "destinationAddressPrefix": "*",
              "access": "Allow",
              "priority": 100,
              "direction": "Inbound"
            }
          },
          {
            "name": "web-rule",
            "properties": {
              "description": "Allow WEB",
              "protocol": "Tcp",
              "sourcePortRange": "*",
              "destinationPortRange": "80",
              "sourceAddressPrefix": "Internet",
              "destinationAddressPrefix": "*",
              "access": "Allow",
              "priority": 101,
              "direction": "Inbound"
            }
          }
        ]
      }

To associate the NSG to the front end subnet, you have to change the subnet definition in the template, and use the reference id for the NSG.

        "subnets": [
          {
            "name": "[parameters('frontEndSubnetName')]",
            "properties": {
              "addressPrefix": "[parameters('frontEndSubnetPrefix')]",
              "networkSecurityGroup": {
                "id": "[resourceId('Microsoft.Network/networkSecurityGroups', parameters('frontEndNSGName'))]"
              }
            }
          }, ...

Notice the same being done for the back end NSG and the back end subnet in the template.

## Deploy the ARM template by using click to deploy

The sample template available in the public repository uses a parameter file containing the default values used to generate the scenario described above. To deploy this template using click to deploy, follow [this link](http://github.com/telmosampaio/azure-templates/tree/master/201-IaaS-WebFrontEnd-SQLBackEnd-NSG), click **Deploy to Azure**, replace the default parameter values if necessary, and follow the instructions in the portal.

## Deploy the ARM template by using PowerShell

To deploy the ARM template you downloaded by using PowerShell, follow the steps below.

[AZURE.INCLUDE [powershell-preview-include.md](../includes/powershell-preview-include.md)]

1. If you have never used Azure PowerShell, see [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure) and follow the instructions all the way to the end to sign into Azure and select your subscription.

3. Run the **`New-AzureRmResourceGroup`** cmdlet to create a resource group using the template.

		New-AzureRmResourceGroup -Name TestRG -Location uswest `
		    -TemplateFile 'https://raw.githubusercontent.com/telmosampaio/azure-templates/master/201-IaaS-WebFrontEnd-SQLBackEnd/azuredeploy.json' `
		    -TemplateParameterFile 'https://raw.githubusercontent.com/telmosampaio/azure-templates/master/201-IaaS-WebFrontEnd-SQLBackEnd/azuredeploy.parameters.json'	

	Expected output:

		ResourceGroupName : TestRG
		Location          : chinanorth
		ProvisioningState : Succeeded
		Tags              : 
		Permissions       : 
		                    Actions  NotActions
		                    =======  ==========
		                    *                  
		                    
		Resources         : 
		                    Name                Type                                     Location
		                    ==================  =======================================  ========
		                    sqlAvSet            Microsoft.Compute/availabilitySets       chinanorth  
		                    webAvSet            Microsoft.Compute/availabilitySets       chinanorth  
		                    SQL1                Microsoft.Compute/virtualMachines        chinanorth  
		                    SQL2                Microsoft.Compute/virtualMachines        chinanorth  
		                    Web1                Microsoft.Compute/virtualMachines        chinanorth  
		                    Web2                Microsoft.Compute/virtualMachines        chinanorth  
		                    TestNICSQL1         Microsoft.Network/networkInterfaces      chinanorth  
		                    TestNICSQL2         Microsoft.Network/networkInterfaces      chinanorth  
		                    TestNICWeb1         Microsoft.Network/networkInterfaces      chinanorth  
		                    TestNICWeb2         Microsoft.Network/networkInterfaces      chinanorth  
		                    NSG-BackEnd         Microsoft.Network/networkSecurityGroups  chinanorth  
		                    NSG-FrontEnd        Microsoft.Network/networkSecurityGroups  chinanorth  
		                    TestPIPSQL1         Microsoft.Network/publicIPAddresses      chinanorth  
		                    TestPIPSQL2         Microsoft.Network/publicIPAddresses      chinanorth  
		                    TestPIPWeb1         Microsoft.Network/publicIPAddresses      chinanorth  
		                    TestPIPWeb2         Microsoft.Network/publicIPAddresses      chinanorth  
		                    TestVNet            Microsoft.Network/virtualNetworks        chinanorth  
		                    testvnetstorageprm  Microsoft.Storage/storageAccounts        chinanorth  
		                    testvnetstoragestd  Microsoft.Storage/storageAccounts        chinanorth  
		                    
		ResourceId        : /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/TestRG

## Deploy the ARM template by using the Azure CLI

To deploy the ARM template by using the Azure CLI, follow the steps below.

1. If you have never used Azure CLI, see [Install and Configure the Azure CLI](/documentation/articles/xplat-cli-install) and follow the instructions up to the point where you select your Azure account and subscription.
2. Run the **`azure config mode`** command to switch to Resource Manager mode, as shown below.

		azure config mode arm

	Here is the expected output for the command above:

		info:    New mode is arm

4. Run the **`azure group deployment create`** cmdlet to deploy the new VNet by using the template and parameter files you downloaded and modified above. The list shown after the output explains the parameters used.

		azure group create -n TestRG -l chinanorth -f 'https://raw.githubusercontent.com/telmosampaio/azure-templates/master/201-IaaS-WebFrontEnd-SQLBackEnd/azuredeploy.json' -e 'https://raw.githubusercontent.com/telmosampaio/azure-templates/master/201-IaaS-WebFrontEnd-SQLBackEnd/azuredeploy.parameters.json'

	Expected output:

		info:    Executing command group create
		info:    Getting resource group TestRG
		info:    Creating resource group TestRG
		info:    Created resource group TestRG
		info:    Initializing template configurations and parameters
		info:    Creating a deployment
		info:    Created template deployment "azuredeploy"
		data:    Id:                  /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/TestRG
		data:    Name:                TestRG
		data:    Location:            chinanorth
		data:    Provisioning State:  Succeeded
		data:    Tags: null
		data:    
		info:    group create command OK

	- **-n (or --name)**. Name of the resource group to be created.
	- **-l (or --location)**. Azure region where the resource group will be created.
	- **-f (or --template-file)**. Path to your ARM template file.
	- **-e (or --parameters-file)**. Path to your ARM parameters file.

