<properties
    pageTitle="Connect Azure VNets with VPN Gateway and PowerShell | Azure"
    description="This article walks you through connecting virtual networks together by using Azure Resource Manager and PowerShell."
    services="vpn-gateway"
    documentationcenter="na"
    author="cherylmc"
    manager="carmonm"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="0683c664-9c03-40a4-b198-a6529bf1ce8b"
    ms.service="vpn-gateway"
    ms.devlang="na"
    ms.topic="get-started-article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="08/31/2016"
    wacn.date=""
    ms.author="cherylmc" />

# Configure a VNet-to-VNet connection for Resource Manager using PowerShell
> [AZURE.SELECTOR]
- [Resource Manager - Azure Portal](/documentation/articles/vpn-gateway-howto-vnet-vnet-resource-manager-portal/)
- [Resource Manager - PowerShell](/documentation/articles/vpn-gateway-vnet-vnet-rm-ps/)
- [Classic - Classic Management Portal](/documentation/articles/virtual-networks-configure-vnet-to-vnet-connection/)

This article walks you through the steps to create a connection between VNets in the Resource Manager deployment model by using VPN Gateway. The virtual networks can be in the same or different regions, and from the same or different subscriptions.

![v2v diagram](./media/vpn-gateway-vnet-vnet-rm-ps/v2vrmps.png)

### Deployment models and methods for VNet-to-VNet connections
[AZURE.INCLUDE [deployment models](../../includes/vpn-gateway-deployment-models-include.md)]

The following table shows the currently available deployment models and methods for VNet-to-VNet configurations. When an article with configuration steps is available, we link directly to it from this table.

[AZURE.INCLUDE [vpn-gateway-table-vnet-vnet](../../includes/vpn-gateway-table-vnet-to-vnet-include.md)]

**VNet peering**

[AZURE.INCLUDE [vpn-gateway-vnetpeeringlink](../../includes/vpn-gateway-vnetpeeringlink-include.md)]

## About VNet-to-VNet connections
Connecting a virtual network to another virtual network (VNet-to-VNet) is similar to connecting a VNet to an on-premises site location. Both connectivity types use an Azure VPN gateway to provide a secure tunnel using IPsec/IKE. The VNets you connect can be in different regions. Or in different subscriptions. You can even combine VNet-to-VNet communication with multi-site configurations. This lets you establish network topologies that combine cross-premises connectivity with inter-virtual network connectivity, as shown in the following diagram:

![About connections](./media/vpn-gateway-vnet-vnet-rm-ps/aboutconnections.png)

### Why connect virtual networks?
You may want to connect virtual networks for the following reasons:

* **Cross region geo-redundancy and geo-presence**
  
  * You can set up your own geo-replication or synchronization with secure connectivity without going over Internet-facing endpoints.
  * With Azure Traffic Manager and Load Balancer, you can set up highly available workload with geo-redundancy across multiple Azure regions. One important example is to set up SQL Always On with Availability Groups spreading across multiple Azure regions.
* **Regional multi-tier applications with isolation or administrative boundary**
  
  * Within the same region, you can set up multi-tier applications with multiple virtual networks connected together due to isolation or administrative requirements.

### VNet-to-VNet FAQ
[AZURE.INCLUDE [vpn-gateway-vnet-vnet-faq](../../includes/vpn-gateway-vnet-vnet-faq-include.md)]

## Which set of steps should I use?
In this article, you see two different sets of steps. One set of steps for [VNets that reside in the same subscription](#samesub), and another for [VNets that reside in different subscriptions](#difsub). The key difference between the sets is whether you can create and configure all virtual network and gateway resources within the same PowerShell session.

The steps in this article use variables that are declared at the beginning of each section. If you already are working with existing VNets, modify the variables to reflect the settings in your own environment. 

![Both connections](./media/vpn-gateway-vnet-vnet-rm-ps/differentsubscription.png)

## <a name="samesub"></a>How to connect VNets that are in the same subscription
![v2v diagram](./media/vpn-gateway-vnet-vnet-rm-ps/v2vrmps.png)

### Before you begin
Before beginning, you need to install the Azure Resource Manager PowerShell cmdlets. See [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for more information about installing the PowerShell cmdlets.

### <a name="Step1"></a>Step 1 - Plan your IP address ranges
In the following steps, we create two virtual networks along with their respective gateway subnets and configurations. We then create a VPN connection between the two VNets. It's important to plan the IP address ranges for your network configuration. Keep in mind that you must make sure that none of your VNet ranges or local network ranges overlap in any way.

We use the following values in the examples:

**Values for TestVNet1:**

* VNet Name: TestVNet1
* Resource Group: TestRG1
* Location: China East
* TestVNet1: 10.11.0.0/16 & 10.12.0.0/16
* FrontEnd: 10.11.0.0/24
* BackEnd: 10.12.0.0/24
* GatewaySubnet: 10.12.255.0/27
* DNS Server: 8.8.8.8
* GatewayName: VNet1GW
* Public IP: VNet1GWIP
* VPNType: RouteBased
* Connection(1to4): VNet1toVNet4
* Connection(1to5): VNet1toVNet5
* ConnectionType: VNet2VNet

**Values for TestVNet4:**

* VNet Name: TestVNet4
* TestVNet2: 10.41.0.0/16 & 10.42.0.0/16
* FrontEnd: 10.41.0.0/24
* BackEnd: 10.42.0.0/24
* GatewaySubnet: 10.42.255.0/27
* Resource Group: TestRG4
* Location: China North
* DNS Server: 8.8.8.8
* GatewayName: VNet4GW
* Public IP: VNet4GWIP
* VPNType: RouteBased
* Connection: VNet4toVNet1
* ConnectionType: VNet2VNet

### <a name="Step2"></a>Step 2 - Create and configure TestVNet1
1. Declare your variables
   
    Start by declaring variables. This example declares the variables using the values for this exercise. In most cases, you should replace the values with your own. However, you can use these variables if you are running through the steps to become familiar with this type of configuration. Modify the variables if needed, then copy and paste them into your PowerShell console.
   
        $Sub1 = "Replace_With_Your_Subcription_Name"
        $RG1 = "TestRG1"
        $Location1 = "China East"
        $VNetName1 = "TestVNet1"
        $FESubName1 = "FrontEnd"
        $BESubName1 = "Backend"
        $GWSubName1 = "GatewaySubnet"
        $VNetPrefix11 = "10.11.0.0/16"
        $VNetPrefix12 = "10.12.0.0/16"
        $FESubPrefix1 = "10.11.0.0/24"
        $BESubPrefix1 = "10.12.0.0/24"
        $GWSubPrefix1 = "10.12.255.0/27"
        $DNS1 = "8.8.8.8"
        $GWName1 = "VNet1GW"
        $GWIPName1 = "VNet1GWIP"
        $GWIPconfName1 = "gwipconf1"
        $Connection14 = "VNet1toVNet4"
        $Connection15 = "VNet1toVNet5"
2. Connect to your subscription
   
    Switch to PowerShell mode to use the Resource Manager cmdlets. Open your PowerShell console and connect to your account. Use the following example to help you connect:
   
        Login-AzureRmAccount
   
    Check the subscriptions for the account.
   
        Get-AzureRmSubscription 
   
    Specify the subscription that you want to use.
   
        Select-AzureRmSubscription -SubscriptionName $Sub1
3. Create a new resource group
   
        New-AzureRmResourceGroup -Name $RG1 -Location $Location1
4. Create the subnet configurations for TestVNet1
   
    This example creates a virtual network named TestVNet1 and three subnets, one called GatewaySubnet, one called FrontEnd, and one called Backend. When substituting values, it's important that you always name your gateway subnet specifically GatewaySubnet. If you name it something else, your gateway creation will fail. 
   
    The following example uses the variables that you set earlier. In this example, the gateway subnet is using a /27. While it is possible to create a gateway subnet as small as /29, we recommend that you create a larger subnet that includes more addresses by selecting at least /28 or /27. This will allow for enough addresses to accommodate possible additional configurations that you may want in the future. 
   
        $fesub1 = New-AzureRmVirtualNetworkSubnetConfig -Name $FESubName1 -AddressPrefix $FESubPrefix1
        $besub1 = New-AzureRmVirtualNetworkSubnetConfig -Name $BESubName1 -AddressPrefix $BESubPrefix1
        $gwsub1 = New-AzureRmVirtualNetworkSubnetConfig -Name $GWSubName1 -AddressPrefix $GWSubPrefix1
5. Create TestVNet1
   
        New-AzureRmVirtualNetwork -Name $VNetName1 -ResourceGroupName $RG1 `
        -Location $Location1 -AddressPrefix $VNetPrefix11,$VNetPrefix12 -Subnet $fesub1,$besub1,$gwsub1
6. Request a public IP address
   
    Request a public IP address to be allocated to the gateway you will create for your VNet. Notice that the AllocationMethod is Dynamic. You cannot specify the IP address that you want to use. It's dynamically allocated to your gateway. 
   
        $gwpip1 = New-AzureRmPublicIpAddress -Name $GWIPName1 -ResourceGroupName $RG1 `
        -Location $Location1 -AllocationMethod Dynamic
7. Create the gateway configuration
   
    The gateway configuration defines the subnet and the public IP address to use. Use the example to create your gateway configuration. 
   
        $vnet1 = Get-AzureRmVirtualNetwork -Name $VNetName1 -ResourceGroupName $RG1
        $subnet1 = Get-AzureRmVirtualNetworkSubnetConfig -Name "GatewaySubnet" -VirtualNetwork $vnet1
        $gwipconf1 = New-AzureRmVirtualNetworkGatewayIpConfig -Name $GWIPconfName1 `
        -Subnet $subnet1 -PublicIpAddress $gwpip1
8. Create the gateway for TestVNet1
   
    In this step, you create the virtual network gateway for your TestVNet1. VNet-to-VNet configurations require a RouteBased VpnType. Creating a gateway can take a while (45 minutes or more to complete).
   
        New-AzureRmVirtualNetworkGateway -Name $GWName1 -ResourceGroupName $RG1 `
        -Location $Location1 -IpConfigurations $gwipconf1 -GatewayType Vpn `
        -VpnType RouteBased -GatewaySku Standard

### Step 3 - Create and configure TestVNet4
Once you've configured TestVNet1, create TestVNet4. Follow the steps below, replacing the values with your own when needed. This step can be done within the same PowerShell session because it is in the same subscription.

1. Declare your variables
   
    Be sure to replace the values with the ones that you want to use for your configuration.
   
        $RG4 = "TestRG4"
        $Location4 = "China North"
        $VnetName4 = "TestVNet4"
        $FESubName4 = "FrontEnd"
        $BESubName4 = "Backend"
        $GWSubName4 = "GatewaySubnet"
        $VnetPrefix41 = "10.41.0.0/16"
        $VnetPrefix42 = "10.42.0.0/16"
        $FESubPrefix4 = "10.41.0.0/24"
        $BESubPrefix4 = "10.42.0.0/24"
        $GWSubPrefix4 = "10.42.255.0/27"
        $DNS4 = "8.8.8.8"
        $GWName4 = "VNet4GW"
        $GWIPName4 = "VNet4GWIP"
        $GWIPconfName4 = "gwipconf4"
        $Connection41 = "VNet4toVNet1"
   
    Before you continue, make sure you are still connected to Subscription 1.
2. Create a new resource group
   
        New-AzureRmResourceGroup -Name $RG4 -Location $Location4
3. Create the subnet configurations for TestVNet4
   
        $fesub4 = New-AzureRmVirtualNetworkSubnetConfig -Name $FESubName4 -AddressPrefix $FESubPrefix4
        $besub4 = New-AzureRmVirtualNetworkSubnetConfig -Name $BESubName4 -AddressPrefix $BESubPrefix4
        $gwsub4 = New-AzureRmVirtualNetworkSubnetConfig -Name $GWSubName4 -AddressPrefix $GWSubPrefix4
4. Create TestVNet4
   
        New-AzureRmVirtualNetwork -Name $VnetName4 -ResourceGroupName $RG4 `
        -Location $Location4 -AddressPrefix $VnetPrefix41,$VnetPrefix42 -Subnet $fesub4,$besub4,$gwsub4
5. Request a public IP address
   
        $gwpip4 = New-AzureRmPublicIpAddress -Name $GWIPName4 -ResourceGroupName $RG4 `
        -Location $Location4 -AllocationMethod Dynamic
6. Create the gateway configuration
   
        $vnet4 = Get-AzureRmVirtualNetwork -Name $VnetName4 -ResourceGroupName $RG4
        $subnet4 = Get-AzureRmVirtualNetworkSubnetConfig -Name "GatewaySubnet" -VirtualNetwork $vnet4
        $gwipconf4 = New-AzureRmVirtualNetworkGatewayIpConfig -Name $GWIPconfName4 -Subnet $subnet4 -PublicIpAddress $gwpip4
7. Create the TestVNet4 gateway
   
        New-AzureRmVirtualNetworkGateway -Name $GWName4 -ResourceGroupName $RG4 `
        -Location $Location4 -IpConfigurations $gwipconf4 -GatewayType Vpn `
        -VpnType RouteBased -GatewaySku Standard

### Step 4 - Connect the gateways
1. Get both virtual network gateways
   
    In this example, because both gateways are in the same subscription, this step can be completed in the same PowerShell session.
   
        $vnet1gw = Get-AzureRmVirtualNetworkGateway -Name $GWName1 -ResourceGroupName $RG1
        $vnet4gw = Get-AzureRmVirtualNetworkGateway -Name $GWName4 -ResourceGroupName $RG4
2. Create the TestVNet1 to TestVNet4 connection
   
    In this step, you create the connection from TestVNet1 to TestVNet4. You'll see a shared key referenced in the examples. You can use your own values for the shared key. The important thing is that the shared key must match for both connections. Creating a connection can take a short while to complete.
   
        New-AzureRmVirtualNetworkGatewayConnection -Name $Connection14 -ResourceGroupName $RG1 `
        -VirtualNetworkGateway1 $vnet1gw -VirtualNetworkGateway2 $vnet4gw -Location $Location1 `
        -ConnectionType Vnet2Vnet -SharedKey 'AzureA1b2C3'
3. Create the TestVNet4 to TestVNet1 connection
   
    This step is similar to the one above, except you are creating the connection from TestVNet4 to TestVNet1. Make sure the shared keys match.
   
        New-AzureRmVirtualNetworkGatewayConnection -Name $Connection41 -ResourceGroupName $RG4 `
        -VirtualNetworkGateway1 $vnet4gw -VirtualNetworkGateway2 $vnet1gw -Location $Location4 `
        -ConnectionType Vnet2Vnet -SharedKey 'AzureA1b2C3'
   
    The connection should be established after a few minutes.
4. Verify your connection. See the section [How to verify your connection](#verify).

## <a name="difsub"></a>How to connect VNets that are in different subscriptions
![v2v diagram](./media/vpn-gateway-vnet-vnet-rm-ps/v2vdiffsub.png)

In this scenario, we connect TestVNet1 and TestVNet5. TestVNet1 and TestVNet5 reside in a different subscription. The steps for this configuration add an additional VNet-to-VNet connection in order to connect TestVNet1 to TestVNet5. 

The difference here is that some of the configuration steps need to be performed in a separate PowerShell session in the context of the second subscription. Especially when the two subscriptions belong to different organizations. 

The instructions continue from the previous steps listed above. You must complete [Step 1](#Step1) and [Step 2](#Step2) to create and configure TestVNet1, and the VPN Gateway for TestVNet1. Once you complete Step 1 and Step 2, continue with Step 5 to create TestVNet5.

### Step 5 - Verify the additional IP address ranges
It is important to make sure that the IP address space of the new virtual network, TestVNet5, does not overlap with any of your VNet ranges or local network gateway ranges. 

In this example, the virtual networks may belong to different organizations. For this exercise, you can use the following values for the TestVNet5:

**Values for TestVNet5:**

* VNet Name: TestVNet5
* Resource Group: TestRG5
* Location: China East
* TestVNet5: 10.51.0.0/16 & 10.52.0.0/16
* FrontEnd: 10.51.0.0/24
* BackEnd: 10.52.0.0/24
* GatewaySubnet: 10.52.255.0.0/27
* DNS Server: 8.8.8.8
* GatewayName: VNet5GW
* Public IP: VNet5GWIP
* VPNType: RouteBased
* Connection: VNet5toVNet1
* ConnectionType: VNet2VNet

**Additional Values for TestVNet1:**

* Connection: VNet1toVNet5

### Step 6 - Create and configure TestVNet5
This step must be done in the context of the new subscription. This part may be performed by the administrator in a different organization that owns the subscription.

1. Declare your variables
   
    Be sure to replace the values with the ones that you want to use for your configuration.
   
        $Sub5 = "Replace_With_the_New_Subcription_Name"
        $RG5 = "TestRG5"
        $Location5 = "China East"
        $VnetName5 = "TestVNet5"
        $FESubName5 = "FrontEnd"
        $BESubName5 = "Backend"
        $GWSubName5 = "GatewaySubnet"
        $VnetPrefix51 = "10.51.0.0/16"
        $VnetPrefix52 = "10.52.0.0/16"
        $FESubPrefix5 = "10.51.0.0/24"
        $BESubPrefix5 = "10.52.0.0/24"
        $GWSubPrefix5 = "10.52.255.0/27"
        $DNS5 = "8.8.8.8"
        $GWName5 = "VNet5GW"
        $GWIPName5 = "VNet5GWIP"
        $GWIPconfName5 = "gwipconf5"
        $Connection51 = "VNet5toVNet1"
2. Connect to subscription 5
   
    Open your PowerShell console and connect to your account. Use the following sample to help you connect:
   
        Login-AzureRmAccount
   
    Check the subscriptions for the account.
   
        Get-AzureRmSubscription 
   
    Specify the subscription that you want to use.
   
        Select-AzureRmSubscription -SubscriptionName $Sub5
3. Create a new resource group
   
        New-AzureRmResourceGroup -Name $RG5 -Location $Location5
4. Create the subnet configurations for TestVNet4
   
        $fesub5 = New-AzureRmVirtualNetworkSubnetConfig -Name $FESubName5 -AddressPrefix $FESubPrefix5
        $besub5 = New-AzureRmVirtualNetworkSubnetConfig -Name $BESubName5 -AddressPrefix $BESubPrefix5
        $gwsub5 = New-AzureRmVirtualNetworkSubnetConfig -Name $GWSubName5 -AddressPrefix $GWSubPrefix5
5. Create TestVNet5
   
        New-AzureRmVirtualNetwork -Name $VnetName5 -ResourceGroupName $RG5 -Location $Location5 `
        -AddressPrefix $VnetPrefix51,$VnetPrefix52 -Subnet $fesub5,$besub5,$gwsub5
6. Request a public IP address
   
        $gwpip5 = New-AzureRmPublicIpAddress -Name $GWIPName5 -ResourceGroupName $RG5 `
        -Location $Location5 -AllocationMethod Dynamic
7. Create the gateway configuration
   
        $vnet5 = Get-AzureRmVirtualNetwork -Name $VnetName5 -ResourceGroupName $RG5
        $subnet5  = Get-AzureRmVirtualNetworkSubnetConfig -Name "GatewaySubnet" -VirtualNetwork $vnet5
        $gwipconf5 = New-AzureRmVirtualNetworkGatewayIpConfig -Name $GWIPconfName5 -Subnet $subnet5 -PublicIpAddress $gwpip5
8. Create the TestVNet5 gateway
   
        New-AzureRmVirtualNetworkGateway -Name $GWName5 -ResourceGroupName $RG5 -Location $Location5 `
        -IpConfigurations $gwipconf5 -GatewayType Vpn -VpnType RouteBased -GatewaySku Standard

### Step 7 - Connecting the gateways
In this example, because the gateways are in the different subscriptions, we've split this step into two PowerShell sessions marked as [Subscription 1] and [Subscription 5].

1. **[Subscription 1]** Get the virtual network gateway for Subscription 1
   
    Make sure you log in and connect to Subscription 1.
   
        $vnet1gw = Get-AzureRmVirtualNetworkGateway -Name $GWName1 -ResourceGroupName $RG1
   
    Copy the output of the following elements and send these to the administrator of Subscription 5 via email or another method.
   
        $vnet1gw.Name
        $vnet1gw.Id
   
    These two elements will have values similar to the following example output:
   
        PS D:\> $vnet1gw.Name
        VNet1GW
        PS D:\> $vnet1gw.Id
        /subscriptions/b636ca99-6f88-4df4-a7c3-2f8dc4545509/resourceGroupsTestRG1/providers/Microsoft.Network/virtualNetworkGateways/VNet1GW
2. **[Subscription 5]** Get the virtual network gateway for Subscription 5
   
    Make sure you log in and connect to Subscription 5.
   
        $vnet5gw = Get-AzureRmVirtualNetworkGateway -Name $GWName5 -ResourceGroupName $RG5
   
    Copy the output of the following elements and send these to the administrator of Subscription 1 via email or another method.
   
        $vnet5gw.Name
        $vnet5gw.Id
   
    These two elements will have values similar to the following example output:
   
        PS C:\> $vnet5gw.Name
        VNet5GW
        PS C:\> $vnet5gw.Id
        /subscriptions/66c8e4f1-ecd6-47ed-9de7-7e530de23994/resourceGroups/TestRG5/providers/Microsoft.Network/virtualNetworkGateways/VNet5GW
3. **[Subscription 1]** Create the TestVNet1 to TestVNet5 connection
   
    In this step, you create the connection from TestVNet1 to TestVNet5. The difference here is that $vnet5gw cannot be obtained directly because it is in a different subscription. You will need to create a new PowerShell object with the values communicated from Subscription 1 in the steps above. Use the example below. Replace the Name, Id, and shared key with your own values. The important thing is that the shared key must match for both connections. Creating a connection can take a short while to complete.
   
    Make sure you connect to Subscription 1. 
   
        $vnet5gw = New-Object Microsoft.Azure.Commands.Network.Models.PSVirtualNetworkGateway
        $vnet5gw.Name = "VNet5GW"
        $vnet5gw.Id   = "/subscriptions/66c8e4f1-ecd6-47ed-9de7-7e530de23994/resourceGroups/TestRG5/providers/Microsoft.Network/virtualNetworkGateways/VNet5GW"
        $Connection15 = "VNet1toVNet5"
        New-AzureRmVirtualNetworkGatewayConnection -Name $Connection15 -ResourceGroupName $RG1 -VirtualNetworkGateway1 $vnet1gw -VirtualNetworkGateway2 $vnet5gw -Location $Location1 -ConnectionType Vnet2Vnet -SharedKey 'AzureA1b2C3'
4. **[Subscription 5]** Create the TestVNet5 to TestVNet1 connection
   
    This step is similar to the one above, except you are creating the connection from TestVNet5 to TestVNet1. The same process of creating a PowerShell object based on the values obtained from Subscription 1 applies here as well. In this step, be sure that the shared keys match.
   
    Make sure you connect to Subscription 5.
   
        $vnet1gw = New-Object Microsoft.Azure.Commands.Network.Models.PSVirtualNetworkGateway
        $vnet1gw.Name = "VNet1GW"
        $vnet1gw.Id = "/subscriptions/b636ca99-6f88-4df4-a7c3-2f8dc4545509/resourceGroups/TestRG1/providers/Microsoft.Network/virtualNetworkGateways/VNet1GW "
        New-AzureRmVirtualNetworkGatewayConnection -Name $Connection51 -ResourceGroupName $RG5 -VirtualNetworkGateway1 $vnet5gw -VirtualNetworkGateway2 $vnet1gw -Location $Location5 -ConnectionType Vnet2Vnet -SharedKey 'AzureA1b2C3'

## <a name="verify"></a>How to verify a connection
[AZURE.INCLUDE [vpn-gateway-no-nsg-include](../../includes/vpn-gateway-no-nsg-include.md)]

[AZURE.INCLUDE [verify connection powershell](../../includes/vpn-gateway-verify-connection-ps-rm-include.md)]

## Next steps

* Once your connection is complete, you can add virtual machines to your virtual networks. See the [Virtual Machines documentation](https://docs.microsoft.com/azure/#pivot=services&panel=Compute) for more information.
* For information about BGP, see the [BGP Overview](/documentation/articles/vpn-gateway-bgp-overview/) and [How to configure BGP](/documentation/articles/vpn-gateway-bgp-resource-manager-ps/). 

