<properties
	pageTitle="Common network PowerShell commands for VMs | Azure"
	description="Common PowerShell commands to get you started creating a virtual network and its associated resources for VMs."
	services="virtual-machines-windows"
	documentationCenter=""
	authors="davidmu1"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="06/07/2016"
	wacn.date=""/>

# Common network Azure PowerShell commands for VMs

If you want to create a virtual machine, you need to create a [virtual network](/documentation/articles/virtual-networks-overview/) or know about an existing virtual network in which the VM can be added. Typically, when you create a VM, you also need to consider creating the resources described in this article.

## Create resources using Azure Powershell

See [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for information about how to install the latest version of Azure PowerShell, select the subscription that you want to use, and sign in to your Azure account.

Resource | Command 
-------------- | -------------------------
Subnet | $internetSubnet = [New-AzureRmVirtualNetworkSubnetConfig](https://msdn.microsoft.com/zh-cn/library/mt619412.aspx) -Name internetSubnet -AddressPrefix 10.0.1.0/24<BR>$internalSubnet = New-AzureRmVirtualNetworkSubnetConfig -Name internalSubnet -AddressPrefix 10.0.2.0/24<BR><BR>A typical network might have a subnet for a internet facing load balancer and a separate subnet for an internal load balancer. |
Virtual network | Create a virtual network:<BR><BR>$rgName = "[resource-group-name](/documentation/articles/powershell-azure-resource-manager/)"<BR>$locName = "[location-name](https://msdn.microsoft.com/zh-cn/library/azure/dn495177.aspx)"<BR>$vnetName = "virtual-network-name"<BR>$vnet = [New-AzureRmVirtualNetwork](https://msdn.microsoft.com/zh-cn/library/mt603657.aspx) -Name $vnetName -ResourceGroupName $rgName -Location $locName -AddressPrefix 10.0.0.0/16 -Subnet $internetSubnet,$internalSubnet<BR><BR>Get a list of virtual networks:<BR><BR>[Get-AzureRmVirtualNetwork](https://msdn.microsoft.com/zh-cn/library/mt603515.aspx) -ResourceGroupName $rgName &#124; Sort Name &#124; Select Name<BR><BR>List the subnets in a virtual network:<BR><BR>Get-AzureRmVirtualNetwork -Name $vnetName -ResourceGroupName $rgName &#124; Select Subnets<BR><BR>You should see something like this that shows the list of subnets:<BR><BR>Subnets<BR>-------<BR>{internetSubnet, internalSubnet}<BR><BR>The subnet index for the internetSubnet is 0 and the subnet index for the internalSubnet is 1.
Domain name label | $domName = "domain-name"<BR>[Test-AzureRmDnsAvailability](https://msdn.microsoft.com/zh-cn/library/mt619419.aspx) -DomainQualifiedName $domName -Location $locName<BR><BR>You can specify a DNS domain name label for a [public IP resource](/documentation/articles/virtual-network-ip-addresses-overview-arm/), which creates a mapping for domainnamelabel.location.chinacloudapp.cn to the public IP address in the Azure-managed DNS servers. The label can contain only letters, numbers, and hyphens. The first and last character must be a letter or number and the domain name label must be unique within its Azure location. You should always test whether your domain name label is globally unique. If **True** is returned, your proposed name is globally unique.
Public IP address | $ipName = "public-ip-address-name"<BR>$pip = [New-AzureRmPublicIpAddress](https://msdn.microsoft.com/zh-cn/library/mt603620.aspx) -Name $ipName -ResourceGroupName $rgName -DomainNameLabel $domName -Location $locName -AllocationMethod Dynamic<BR><BR>The public IP address uses the domain name label that you previously created and is used by the frontend configuration of the load balancer.
Frontend IP configuration | $feConfigName = "frontend-ip-config-name"<BR>$frontendIP = [New-AzureRmLoadBalancerFrontendIpConfig](https://msdn.microsoft.com/zh-cn/library/mt603510.aspx) -Name $feConfigName -PublicIpAddress $pip<BR><BR>The frontend configuration includes the public IP address that you previously created for incoming network traffic.
Backend address pool | $bePoolName = "back-end-pool-name"<BR>$beAddressPool = [New-AzureRmLoadBalancerBackendAddressPoolConfig](https://msdn.microsoft.com/zh-cn/library/mt603791.aspx) -Name $bePoolName<BR><BR>Provides internal addresses for the backend of the load balancer that are accessed through a network interface.
Probe | $probeName = "health-probe-name"<BR>$healthProbe = [New-AzureRmLoadBalancerProbeConfig](https://msdn.microsoft.com/zh-cn/library/mt603847.aspx) -Name $probeName -RequestPath 'HealthProbe.aspx' -Protocol http -Port 80 -IntervalInSeconds 15 -ProbeCount 2<BR><BR>Contains health probes used to check availability of virtual machines instances in the backend address pool.
Load balancing rule | $lbRule = [New-AzureRmLoadBalancerRuleConfig](https://msdn.microsoft.com/zh-cn/library/mt619391.aspx) -Name HTTP -FrontendIpConfiguration $frontendIP -BackendAddressPool  $beAddressPool -Probe $healthProbe -Protocol Tcp -FrontendPort 80 -BackendPort 80<BR><BR>Contains rules mapping a public port on the load balancer to a port in the backend address pool.
Inbound NAT rule | $ruleName = "NAT-rule-name"<BR>$inboundNATRule = [New-AzureRmLoadBalancerInboundNatRuleConfig](https://msdn.microsoft.com/zh-cn/library/mt603606.aspx) -Name $ruleName -FrontendIpConfiguration $frontendIP -Protocol TCP -FrontendPort 3441 -BackendPort 3389<BR><BR>Contains rules mapping a public port on the load balancer to a port for a specific virtual machine in the backend address pool.
Load balancer | $lbName = "load-balancer-name"<BR>$loadBalancer = [New-AzureRmLoadBalancer](https://msdn.microsoft.com/zh-cn/library/mt619450.aspx) -ResourceGroupName $rgName -Name $lbName -Location $locName -FrontendIpConfiguration $frontendIP -InboundNatRule $inboundNATRule -LoadBalancingRule $lbRule -BackendAddressPool $beAddressPool -Probe $healthProbe
Network interface | $vnet = [Get-AzureRmVirtualNetwork](https://msdn.microsoft.com/zh-cn/library/mt603515.aspx) -Name $vnetName -ResourceGroupName $rgName<BR>$internalSubnet = [Get-AzureRmVirtualNetworkSubnetConfig](https://msdn.microsoft.com/zh-cn/library/mt603817.aspx) -Name "internalSubnet" -VirtualNetwork $vnet<BR>$nicName = "network-interface-name"<BR>$nic1= [New-AzureRmNetworkInterface](https://msdn.microsoft.com/zh-cn/library/mt619370.aspx) -ResourceGroupName $rgName -Name $nicName -Location $locName -PrivateIpAddress 10.0.2.6 -Subnet $internalSubnet -LoadBalancerBackendAddressPool $loadBalancer.BackendAddressPools[0] -LoadBalancerInboundNatRule $loadBalancer.InboundNatRules[0]<BR><BR>Create a network interface using the public IP address and virtual network subnet that you previously created.
	
## Next Steps

- Use the network interface that you just created when you [create a VM](/documentation/articles/virtual-machines-windows-ps-create/).
- Learn about how you can [create a VM with multiple network interfaces](/documentation/articles/virtual-networks-multiple-nics/).