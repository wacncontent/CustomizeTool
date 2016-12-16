<properties
    pageTitle="Control routing and use virtual appliances using PowerShell Azure"
    description="Learn how to control routing in VNets using PowerShell | Classic"
    services="virtual-network"
    documentationcenter="na"
    author="jimdial"
    manager="carmonm"
    editor=""
    tags="azure-service-management" />
<tags
    ms.assetid="d8d07c16-cbe5-4536-acd6-870269346fe3"
    ms.service="virtual-network"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="02/02/2016"
    wacn.date=""
    ms.author="jdial" />

# Control routing and use virtual appliances (classic) using PowerShell

> [!div class="op_single_selector"]
- [PowerShell](/documentation/articles/virtual-network-create-udr-arm-ps/)
- [Azure CLI](/documentation/articles/virtual-network-create-udr-arm-cli/)
- [Template](/documentation/articles/virtual-network-create-udr-arm-template/)
- [PowerShell (Classic)](/documentation/articles/virtual-network-create-udr-classic-ps/)
- [CLI (Classic)](/documentation/articles/virtual-network-create-udr-classic-cli/)

[AZURE.INCLUDE [virtual-network-create-udr-intro-include.md](../../includes/virtual-network-create-udr-intro-include.md)]

> [AZURE.IMPORTANT]
> Before you work with Azure resources, it's important to understand that Azure currently has two deployment models: Azure Resource Manager and classic. Make sure you understand [deployment models and tools](/documentation/articles/resource-manager-deployment-model/) before you work with any Azure resource. You can view the documentation for different tools by selecting an option at the top of this article. This article covers the classic deployment model.
> 

[AZURE.INCLUDE [virtual-network-create-udr-scenario-include.md](../../includes/virtual-network-create-udr-scenario-include.md)]

The sample Azure PowerShell commands below expect a simple environment already created based on the scenario above. If you want to run the commands as they are displayed in this document, create the environment shown in [create a VNet (classic) using PowerShell](/documentation/articles/virtual-networks-create-vnet-classic-netcfg-ps/).

[AZURE.INCLUDE [azure-ps-prerequisites-include.md](../../includes/azure-ps-prerequisites-include.md)]

## Create the UDR for the front end subnet
To create the route table and route needed for the front end subnet based on the scenario above, follow the steps below.

1. Run the following command to create a route table for the front-end subnet:

	```powershell
	New-AzureRouteTable -Name UDR-FrontEnd -Location chinanorth `
	-Label "Route table for front end subnet"
	```

    Output:
   
        Name         Location   Label                          
        ----         --------   -----                          
        UDR-FrontEnd China North    Route table for front end subnet
2. Run the following command to create a route in the route table to send all traffic destined to the back-end subnet (192.168.2.0/24) to the **FW1** VM (192.168.0.4):

	```powershell
	Get-AzureRouteTable UDR-FrontEnd `
	|Set-AzureRoute -RouteName RouteToBackEnd -AddressPrefix 192.168.2.0/24 `
	-NextHopType VirtualAppliance `
	-NextHopIpAddress 192.168.0.4
	```
   
    Output:
   
        Name     : UDR-FrontEnd
        Location : China North
        Label    : Route table for frontend subnet
        Routes   : 
                   Name                 Address Prefix    Next hop type        Next hop IP address
                   ----                 --------------    -------------        -------------------
                   RouteToBackEnd       192.168.2.0/24    VirtualAppliance     192.168.0.4  
3. Run the following command to associate the route table with the **FrontEnd** subnet:

	```powershell
	Set-AzureSubnetRouteTable -VirtualNetworkName TestVNet `
	-SubnetName FrontEnd `
	-RouteTableName UDR-FrontEnd
	```

## Create the UDR for the back-end subnet
To create the route table and route needed for the back end subnet based on the scenario, complete the following steps:

1. Run the following command to create a route table for the back-end subnet:

	```powershell
	New-AzureRouteTable -Name UDR-BackEnd `
	-Location chinanorth `
	-Label "Route table for back end subnet"
	```

2. Run the following command to create a route in the route table to send all traffic destined to the front-end subnet (192.168.1.0/24) to the **FW1** VM (192.168.0.4):

	```powershell
	Get-AzureRouteTable UDR-BackEnd `
	|Set-AzureRoute -RouteName RouteToFrontEnd -AddressPrefix 192.168.1.0/24 `
	-NextHopType VirtualAppliance `
	-NextHopIpAddress 192.168.0.4
	```

3. Run the following command to associate the route table with the **BackEnd** subnet:

	```powershell
	Set-AzureSubnetRouteTable -VirtualNetworkName TestVNet `
	-SubnetName BackEnd `
	-RouteTableName UDR-BackEnd
	```

## Enable IP forwarding on the FW1 VM

To enable IP forwarding in the FW1 VM, complete the following steps:

1. Run the following command to check the status of IP forwarding:

	```powershell
	Get-AzureVM -Name FW1 -ServiceName TestRGFW `
	| Get-AzureIPForwarding
	```

    Output:
   
        Disabled
2. Run the following command to enable IP forwarding for the *FW1* VM:

	```powershell
	Get-AzureVM -Name FW1 -ServiceName TestRGFW `
	| Set-AzureIPForwarding -Enable
	```
