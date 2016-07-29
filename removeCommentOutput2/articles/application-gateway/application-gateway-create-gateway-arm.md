<properties
   pageTitle="Create, start, or delete an application gateway by using Azure Resource Manager | Azure"
   description="This page provides instructions to create, configure, start, and delete an Azure application gateway by using Azure Resource Manager"
   documentationCenter="na"
   services="application-gateway"
   authors="joaoma"
   manager="carmonm"
   editor="tysonn"/>
<tags
	ms.service="application-gateway"
	ms.date="04/05/2016"
	wacn.date=""/>


# Create, start, or delete an application gateway by using Azure Resource Manager

Azure Application Gateway is a layer-7 load balancer. It provides failover, performance-routing HTTP requests between different servers, whether they are on the cloud or on-premises. Application Gateway has the following application delivery features: HTTP load balancing, cookie-based session affinity, and Secure Sockets Layer (SSL) offload.


> [AZURE.SELECTOR]
- [Azure Classic PowerShell steps](/documentation/articles/application-gateway-create-gateway/)
- [Azure Resource Manager PowerShell](/documentation/articles/application-gateway-create-gateway-arm/)
- [Azure Resource Manager template ](/documentation/articles/application-gateway-create-gateway-arm-template/)


<BR>


This article walks you through the steps to create, configure, start, and delete an application gateway.


>[AZURE.IMPORTANT] Before you work with Azure resources, it's important to understand that Azure currently has two deployment models: Resource Manager and classic. Make sure that you understand [deployment models and tools](/documentation/articles/azure-classic-rm/) before working with any Azure resource. You can view the documentation for different tools by clicking the tabs at the top of this article. This document will cover creating an application gateway by using Azure Resource Manager. To use the classic version, go to [Create an application gateway classic deployment by using PowerShell](/documentation/articles/application-gateway-create-gateway/).



## Before you begin

1. Install the latest version of the Azure PowerShell cmdlets by using the Web Platform Installer. You can download and install the latest version from the **Windows PowerShell** section of the [Downloads page](/downloads/).
2. If you have an existing virtual network, either select an existing empty subnet or create a new subnet in your existing virtual network solely for use by the application gateway. You cannot deploy the application gateway to a different virtual network than the resources you intend to deploy behind the application gateway. 
3. The servers that you will configure to use the application gateway must exist or have their endpoints created either in the virtual network or with a public IP/VIP assigned.

## What is required to create an application gateway?


- **Back-end server pool:** The list of IP addresses of the back-end servers. The IP addresses listed should either belong to the virtual network subnet or should be a public IP/VIP.
- **Back-end server pool settings:** Every pool has settings like port, protocol, and cookie-based affinity. These settings are tied to a pool and are applied to all servers within the pool.
- **Front-end port:** This port is the public port that is opened on the application gateway. Traffic hits this port, and then gets redirected to one of the back-end servers.
- **Listener:** The listener has a front-end port, a protocol (Http or Https, these are case-sensitive), and the SSL certificate name (if configuring SSL offload).
- **Rule:** The rule binds the listener, the back-end server pool and defines which back-end server pool the traffic should be directed to when it hits a particular listener. 



## Create a new application gateway

The difference between using Azure Classic and Azure Resource Manager is the order in which you will create the application gateway and the items that need to be configured.

With Resource Manager, all items that will make an application gateway will be configured individually and then put together to create the application gateway resource.


Here are the steps that are needed to create an application gateway:

1. Create a resource group for Resource Manager.
2. Create a virtual network, subnet, and public IP for the application gateway.
3. Create an application gateway configuration object.
4. Create an application gateway resource.


## Create a resource group for Resource Manager

Make sure that you are using the latest version of Azure PowerShell. More info is available at [Using Windows PowerShell with Resource Manager](/documentation/articles/powershell-azure-resource-manager/).

### Step 1
Login to Azure
		[AZURE.ACOM]{
		Login-AzureRmAccount
		[AZURE.ACOM]}
		
		[AZURE.ACN]{
		Login-AzureRmAccount -EnvironmentName AzureChinaCloud
		[AZURE.ACN]}

You will be prompted to authenticate with your credentials.<BR>
### Step 2
Check the subscriptions for the account.

		Get-AzureRmSubscription

### Step 3
Choose which of your Azure subscriptions to use. <BR>

		Select-AzureRmSubscription -Subscriptionid "GUID of subscription"

### Step 4
Create a new resource group (skip this step if you're using an existing resource group).

    [AZURE.ACOM]{
    New-AzureRmResourceGroup -Name appgw-rg -location "West US"
    [AZURE.ACOM]}

    [AZURE.ACN]{
    New-AzureRmResourceGroup -Name appgw-rg -location "China North"
    [AZURE.ACN]}

Azure Resource Manager requires that all resource groups specify a location. This is used as the default location for resources in that resource group. Make sure that all commands to create an application gateway will use the same resource group.

[AZURE.ACOM]{
In the example above, we created a resource group called "appgw-RG" and location "West US".
[AZURE.ACOM]}

[AZURE.ACN]{
In the example above, we created a resource group called "appgw-RG" and location "China North".
[AZURE.ACN]}

>[AZURE.NOTE] If you need to configure a custom probe for your application gateway, see [Create an application gateway with custom probes by using PowerShell](/documentation/articles/application-gateway-create-probe-ps/). Check out [custom probes and health monitoring](/documentation/articles/application-gateway-probe-overview/) for more information.



## Create a virtual network and a subnet for the application gateway

The following example shows how to create a virtual network by using Resource Manager.

### Step 1

Assign the address range 10.0.0.0/24 to the subnet variable to be used to create a virtual network.

	$subnet = New-AzureRmVirtualNetworkSubnetConfig -Name subnet01 -AddressPrefix 10.0.0.0/24


### Step 2

[AZURE.ACOM]{
Create a virtual network named "appgwvnet" in resource group "appgw-rg" for the West US region using the prefix 10.0.0.0/16 with subnet 10.0.0.0/24.

	$vnet = New-AzureRmVirtualNetwork -Name appgwvnet -ResourceGroupName appgw-rg -Location "West US" -AddressPrefix 10.0.0.0/16 -Subnet $subnet
[AZURE.ACOM]}

[AZURE.ACN]{
Create a virtual network named "appgwvnet" in resource group "appgw-rg" for the China North region using the prefix 10.0.0.0/16 with subnet 10.0.0.0/24.

	$vnet = New-AzureRmVirtualNetwork -Name appgwvnet -ResourceGroupName appgw-rg -Location "China North" -AddressPrefix 10.0.0.0/16 -Subnet $subnet
[AZURE.ACN]}


### Step 3

Assign a subnet variable for the next steps, which create an application gateway.

	$subnet=$vnet.Subnets[0]

## Create a public IP address for the front-end configuration

[AZURE.ACOM]{
Create a public IP resource "publicIP01" in resource group "appgw-rg" for the West US region.

	$publicip = New-AzureRmPublicIpAddress -ResourceGroupName appgw-rg -name publicIP01 -location "West US" -AllocationMethod Dynamic
[AZURE.ACOM]}

[AZURE.ACN]{
Create a public IP resource "publicIP01" in resource group "appgw-rg" for the China North region.

	$publicip = New-AzureRmPublicIpAddress -ResourceGroupName appgw-rg -name publicIP01 -location "China North" -AllocationMethod Dynamic
[AZURE.ACN]}


## Create an application gateway configuration object

You need to set up all configuration items before creating the application gateway. The following steps create the configuration items that are needed for an application gateway resource.

### Step 1

Create an application gateway IP configuration named "gatewayIP01". When Application Gateway starts, it will pick up an IP address from the subnet configured and route network traffic to the IP addresses in the back-end IP pool. Keep in mind that each instance will take one IP address.


	$gipconfig = New-AzureRmApplicationGatewayIPConfiguration -Name gatewayIP01 -Subnet $subnet


### Step 2

Configure the back-end IP address pool named "pool01" with IP addresses "134.170.185.46, 134.170.188.221,134.170.185.50". Those will be the IP addresses that receive the network traffic that comes from the front-end IP endpoint. You will replace the IP addresses above to add your own application IP address endpoints.

	$pool = New-AzureRmApplicationGatewayBackendAddressPool -Name pool01 -BackendIPAddresses 134.170.185.46, 134.170.188.221,134.170.185.50



### Step 3

Configure application gateway setting "poolsetting01" for the load-balanced network traffic in the back-end pool.

	$poolSetting = New-AzureRmApplicationGatewayBackendHttpSettings -Name poolsetting01 -Port 80 -Protocol Http -CookieBasedAffinity Disabled


### Step 4

Configure the front-end IP port named "frontendport01" for the public IP endpoint.

	$fp = New-AzureRmApplicationGatewayFrontendPort -Name frontendport01  -Port 80

### Step 5

Create the front-end IP configuration named "fipconfig01" and associate the public IP address with the front-end IP configuration.

	$fipconfig = New-AzureRmApplicationGatewayFrontendIPConfig -Name fipconfig01 -PublicIPAddress $publicip


### Step 6

Create the listener name "listener01" and associate the front-end port to the front-end IP configuration.

	$listener = New-AzureRmApplicationGatewayHttpListener -Name listener01  -Protocol Http -FrontendIPConfiguration $fipconfig -FrontendPort $fp

### Step 7

Create the load balancer routing rule named "rule01" that configures the load balancer behavior.

	$rule = New-AzureRmApplicationGatewayRequestRoutingRule -Name rule01 -RuleType Basic -BackendHttpSettings $poolSetting -HttpListener $listener -BackendAddressPool $pool

### Step 8

Configure the instance size of the application gateway.

	$sku = New-AzureRmApplicationGatewaySku -Name Standard_Small -Tier Standard -Capacity 2

>[AZURE.NOTE]  The default value for *InstanceCount* is 2, with a maximum value of 10. The default value for *GatewaySize* is Medium. You can choose between Standard_Small, Standard_Medium, and Standard_Large.

## Create an application gateway by using New-AzureRmApplicationGateway

Create an application gateway with all configuration items from the steps above. In this example, the application gateway is called "appgwtest".

	[AZURE.ACOM]{
	$appgw = New-AzureRmApplicationGateway -Name appgwtest -ResourceGroupName appgw-rg -Location "West US" -BackendAddressPools $pool -BackendHttpSettingsCollection $poolSetting -FrontendIpConfigurations $fipconfig  -GatewayIpConfigurations $gipconfig -FrontendPorts $fp -HttpListeners $listener -RequestRoutingRules $rule -Sku $sku
	[AZURE.ACOM]}

	[AZURE.ACN]{
	$appgw = New-AzureRmApplicationGateway -Name appgwtest -ResourceGroupName appgw-rg -Location "China North" -BackendAddressPools $pool -BackendHttpSettingsCollection $poolSetting -FrontendIpConfigurations $fipconfig  -GatewayIpConfigurations $gipconfig -FrontendPorts $fp -HttpListeners $listener -RequestRoutingRules $rule -Sku $sku
	[AZURE.ACN]}

### Step 9
Retrieve DNS and VIP details of the application gateway from the public IP resource attached to the application gateway.
	Get-AzureRmPublicIpAddress -Name publicIP01 -ResourceGroupName appgw-rg  
	Name                     : publicIP01
	ResourceGroupName        : appgwtest 
	Location                 : chinanorth
	Id                       : /subscriptions/<sub_id>/resourceGroups/appgw-rg/providers/Microsoft.Network/publicIPAddresses/publicIP01
	Etag                     : W/"12302060-78d6-4a33-942b-a494d6323767"
	ResourceGuid             : ee9gd76a-3gf6-4236-aca4-gc1f4gf14171
	ProvisioningState        : Succeeded
	Tags                     : 
	PublicIpAllocationMethod : Dynamic
	IpAddress                : 137.116.26.16
	IdleTimeoutInMinutes     : 4
	IpConfiguration          : {
	                             "Id": "/subscriptions/<sub_id>/resourceGroups/appgw-rg/providers/Microsoft.Network/applicationGateways/appgwtest/frontendIPConfigurations/fipconfig01"
	                           }
	DnsSettings              : {
	                             "Fqdn": "ee7aca47-4344-4810-a999-2c631b73e3cd.chinacloudapp.cn"
	                           } 

## Delete an application gateway

To delete an application gateway, follow these steps:

1. Use the **Stop-AzureRmApplicationGateway** cmdlet to stop the gateway.
2. Use the **Remove-AzureRmApplicationGateway** cmdlet to remove the gateway.
3. Verify that the gateway has been removed by using the **Get-AzureRmApplicationGateway** cmdlet.

### Step 1

Get the application gateway object and associate it to a variable "$getgw".

	$getgw =  Get-AzureRmApplicationGateway -Name appgwtest -ResourceGroupName appgw-rg

### Step 2

Use **Stop-AzureRmApplicationGateway** to stop the application gateway.

	Stop-AzureRmApplicationGateway -ApplicationGateway $getgw  


Once the application gateway is in a stopped state, use the **Remove-AzureRmApplicationGateway** cmdlet to remove the service.


	Remove-AzureRmApplicationGateway -Name $appgwtest -ResourceGroupName appgw-rg -Force



>[AZURE.NOTE] The **-force** switch can be used to suppress the remove confirmation message.


To verify that the service has been removed, you can use the **Get-AzureRmApplicationGateway** cmdlet. This step is not required.


	Get-AzureRmApplicationGateway -Name appgwtest -ResourceGroupName appgw-rg


## Next steps

If you want to configure SSL offload, see [Configure an application gateway for SSL offload](/documentation/articles/application-gateway-ssl/).

If you want to configure an application gateway to use with an internal load balancer, see [Create an application gateway with an internal load balancer (ILB)](/documentation/articles/application-gateway-ilb/).

If you want more information about load balancing options in general, see:

[AZURE.ACOM]{
- [Azure Load Balancer](/documentation/services/load-balancer/)
[AZURE.ACOM]}
- [Azure Traffic Manager](/documentation/services/traffic-manager/)
