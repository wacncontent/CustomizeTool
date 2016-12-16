<properties
    pageTitle="Create a virtual network using PowerShell | Azure"
    description="Learn how to create a virtual network using PowerShell | Resource Manager."
    services="virtual-network"
    documentationcenter=""
    author="jimdial"
    manager="carmonm"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="a31f4f12-54ee-4339-b968-1a8097ca77d3"
    ms.service="virtual-network"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="03/15/2016"
    wacn.date=""
    ms.author="jdial" />

# Create a virtual network using PowerShell

[AZURE.INCLUDE [virtual-networks-create-vnet-intro](../../includes/virtual-networks-create-vnet-intro-include.md)]

Azure has two deployment models: Azure Resource Manager and classic. Azure recommends creating resources through the Resource Manager deployment model. To learn more about the differences between the two models, read the [Understand Azure deployment models](/documentation/articles/resource-manager-deployment-model/) article.
 
This article explains how to create a VNet through the Resource Manager deployment model using PowerShell. You can also create a VNet through Resource Manager using other tools or create a VNet through the classic deployment model by selecting a different option from the following list:

> [!div class="op_single_selector"]
- [Portal](/documentation/articles/virtual-networks-create-vnet-arm-pportal/)
- [PowerShell](/documentation/articles/virtual-networks-create-vnet-arm-ps/)
- [CLI](/documentation/articles/virtual-networks-create-vnet-arm-cli/)
- [Template](/documentation/articles/virtual-networks-create-vnet-arm-template-click/)
- [Portal (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-pportal/)
- [PowerShell (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-netcfg-ps/)
- [CLI (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-cli/)

[AZURE.INCLUDE [virtual-networks-create-vnet-scenario-include](../../includes/virtual-networks-create-vnet-scenario-include.md)]

## Create a virtual network

To create a virtual network using PowerShell, complete the following steps:

1. Install and configure Azure PowerShell, by following the steps in the [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure/) article.

2. If necessary, create a new resource group, as shown below. For this scenario, create a resource group named *TestRG*. For more information about resource groups, visit [Azure Resource Manager Overview](/documentation/articles/resource-group-overview/).

	```powershell   
	New-AzureRmResourceGroup -Name TestRG -Location chinaeast
	```

    Expected output:

        ResourceGroupName : TestRG
        Location          : chinaeast
        ProvisioningState : Succeeded
        Tags              :
        ResourceId        : /subscriptions/[Subscription Id]/resourceGroups/TestRG    
3. Create a new VNet named *TestVNet*:

	```powershell
	New-AzureRmVirtualNetwork -ResourceGroupName TestRG -Name TestVNet `
	-AddressPrefix 192.168.0.0/16 -Location chinaeast
	```

    Expected output:

        Name                  : TestVNet
        ResourceGroupName     : TestRG
        Location              : chinaeast
        Id                    : /subscriptions/[Subscription Id]/resourceGroups/TestRG/providers/Microsoft.Network/virtualNetworks/TestVNet
        Etag                   : W/"[Id]"
        ProvisioningState          : Succeeded
        Tags                       : 
        AddressSpace               : {
                                   "AddressPrefixes": [
                                     "192.168.0.0/16"
                                   ]
                                  }
        DhcpOptions                : {}
        Subnets                    : []
        VirtualNetworkPeerings     : []
4. Store the virtual network object in a variable:

	```powershell
	$vnet = Get-AzureRmVirtualNetwork -ResourceGroupName TestRG -Name TestVNet
	```

   > [AZURE.TIP]
   > You can combine steps 3 and 4 by running `$vnet = New-AzureRmVirtualNetwork -ResourceGroupName TestRG -Name TestVNet -AddressPrefix 192.168.0.0/16 -Location chinaeast`.
   > 

5. Add a subnet to the new VNet variable:

	```powershell
	Add-AzureRmVirtualNetworkSubnetConfig -Name FrontEnd `
	-VirtualNetwork $vnet -AddressPrefix 192.168.1.0/24
	```

    Expected output:
   
        Name                  : TestVNet
        ResourceGroupName     : TestRG
        Location              : chinaeast
        Id                    : /subscriptions/[Subscription Id]/resourceGroups/TestRG/providers/Microsoft.Network/virtualNetworks/TestVNet
        Etag                  : W/"[Id]"
        ProvisioningState     : Succeeded
        Tags                  :
        AddressSpace          : {
                                  "AddressPrefixes": [
                                    "192.168.0.0/16"
                                  ]
                                }
        DhcpOptions           : {}
        Subnets             : [
                                  {
                                    "Name": "FrontEnd",
                                    "AddressPrefix": "192.168.1.0/24"
                                  }
                                ]
        VirtualNetworkPeerings     : []

6. Repeat step 5 above for each subnet you want to create. The following command creates the *BackEnd* subnet for the scenario:

	```powershell
	Add-AzureRmVirtualNetworkSubnetConfig -Name BackEnd `
	-VirtualNetwork $vnet -AddressPrefix 192.168.2.0/24
	```

7. Although you create subnets, they currently only exist in the local variable used to retrieve the VNet you create in step 4 above. To save the changes to Azure, run the following command:

	```powershell
	Set-AzureRmVirtualNetwork -VirtualNetwork $vnet
	```
   
    Expected output:
   
        Name                  : TestVNet
        ResourceGroupName     : TestRG
        Location              : chinaeast
        Id                    : /subscriptions/[Subscription Id]/resourceGroups/TestRG/providers/Microsoft.Network/virtualNetworks/TestVNet
        Etag                  : W/"[Id]"
        ProvisioningState     : Succeeded
        Tags                  :
        AddressSpace          : {
                                  "AddressPrefixes": [
                                    "192.168.0.0/16"
                                  ]
                                }
        DhcpOptions           : {
                                  "DnsServers": []
                                }
        Subnets               : [
                                  {
                                    "Name": "FrontEnd",
                                    "Etag": "W/\"[Id]\"",
                                    "Id": "/subscriptions/[Subscription Id]/resourceGroups/TestRG/providers/Microsoft.Network/virtualNetworks/TestVNet/subnets/FrontEnd",
                                    "AddressPrefix": "192.168.1.0/24",
                                    "IpConfigurations": [],
                                    "ProvisioningState": "Succeeded"
                                  },
                                  {
                                    "Name": "BackEnd",
                                    "Etag": "W/\"[Id]\"",
                                    "Id": "/subscriptions/[Subscription Id]/resourceGroups/TestRG/providers/Microsoft.Network/virtualNetworks/TestVNet/subnets/BackEnd",
                                    "AddressPrefix": "192.168.2.0/24",
                                    "IpConfigurations": [],
                                    "ProvisioningState": "Succeeded"
                                  }
                                ]
        VirtualNetworkPeerings : []

## Next steps

Learn how to connect:

- A virtual machine (VM) to a virtual network by reading the [Create a Windows VM](/documentation/articles/virtual-machines-windows-ps-create/) article. Instead of creating a VNet and subnet in the steps of the articles, you can select an existing VNet and subnet to connect a VM to.
- The virtual network to other virtual networks by reading the [Connect VNets](/documentation/articles/vpn-gateway-vnet-vnet-rm-ps/) article.
- The virtual network to an on-premises network using a site-to-site virtual private network (VPN) or ExpressRoute circuit. Learn how by reading the [Connect a VNet to an on-premises network using a site-to-site VPN](/documentation/articles/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/) and [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-arm/) articles.