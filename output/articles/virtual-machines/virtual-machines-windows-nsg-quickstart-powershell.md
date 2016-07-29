<properties
   pageTitle="Allow external access to a VM using PowerShell | Azure"
   description="Learn how to open a port / create an endpoint that allows external access to your Windows VM using the resource manager deployment mode and Azure PowerShell"
   services="virtual-machines-windows"
   documentationCenter=""
   authors="iainfoulds"
   manager="timlt"
   editor=""/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="05/24/2016"
	wacn.date=""/>

# Allow external access to your VM using PowerShell
[AZURE.INCLUDE [virtual-machines-common-nsg-quickstart](../includes/virtual-machines-common-nsg-quickstart.md)]

## Quick commands
To create a Network Security Group and ACL rules you will need [the latest version of Azure PowerShell installed](/documentation/articles/powershell-install-configure/). You can also [perform these steps using the Azure Portal](/documentation/articles/virtual-machines-windows-nsg-quickstart-portal/).

First, you need to create a rule to allow HTTP traffic on TCP port 80 entering your own name and description:

```
$httprule = New-AzureRmNetworkSecurityRuleConfig -Name http-rule -Description "Allow HTTP" `
    -Access Allow -Protocol Tcp -Direction Inbound -Priority 100 `
    -SourceAddressPrefix Internet -SourcePortRange * `
    -DestinationAddressPrefix * -DestinationPortRange 80
```

Next, create your Network Security group and assign the HTTP rule you just created as follows, entering your own resource group name and location:

```
$nsg = New-AzureRmNetworkSecurityGroup -ResourceGroupName TestRG -Location chinanorth 
    -Name "TestNSG" -SecurityRules $httprule
```

Now let's assign your Network Security Group to a subnet. First, select the virtual network:

```
$vnet = Get-AzureRmVirtualNetwork -ResourceGroupName TestRG -Name TestVNet
```

Associate your Network Security Group with your subnet:

```
Set-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name TestSubnet `
    -NetworkSecurityGroup $nsg
```

Finally, update your virtual network in order for your changes to take effect:

```
Set-AzureRmVirtualNetwork -VirtualNetwork $vnet
```


## More information on Network Security Groups
The quick commands here allow you to get up and running with traffic flowing to your VM. Network Security Groups provide a lot of great features and granularity for controlling access to the your resources. You can read more about [creating a Network Security Group and ACL rules here](/documentation/articles/virtual-networks-create-nsg-arm-ps/).

Network Security Groups and ACL rules can also be defined as part of Azure Resource Manager templates. Read more about [creating Network Security Groups with templates](/documentation/articles/virtual-networks-create-nsg-arm-template/).

If you need to use port-forwarding to map a unique external port to an internal port on your VM, you need to use a load balancer and Network Address Translation (NAT) rules. For example, you may want to expose TCP port 8080 externally and have traffic directed to TCP port 80 on a VM. You can learn about [creating an Internet-facing load balancer](/documentation/articles/load-balancer-get-started-internet-arm-ps/).

## Next steps
In this example, you created a simple rule to allow HTTP traffic. You can find information on creating more detailed environments in the following articles:

- [Azure Resource Manager overview](/documentation/articles/resource-group-overview/)
- [What is a Network Security Group (NSG)?](/documentation/articles/virtual-networks-nsg/)
- [Azure Resource Manager Overview for Load Balancers](/documentation/articles/load-balancer-arm/)