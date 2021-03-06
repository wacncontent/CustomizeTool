<!-- not suitable for Mooncake -->

<properties 
	pageTitle="How To Control Inbound Traffic to an Azure Websites Environment" 
	description="Learn about how to configure network security rules to control inbound traffic to an Azure Websites Environment." 
	services="app-service" 
	documentationCenter="" 
	authors="ccompy" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/11/2015"
	wacn.date=""/>	

# How To Control Inbound Traffic to an Azure Websites Environment

## Overview ##
An Azure Websites Environment is always created in a subnet of a regional classic "v1" [virtual network][virtualnetwork].  A new regional classic "v1" virtual network and new subnet can be defined at the time an Azure Websites Environment is created.  Alternatively, an Azure Websites Environment can be created in a pre-existing regional classic "v1" virtual network and pre-existing subnet.  For more details on creating an Azure Websites Environment see [How To Create an Azure Websites Environment][HowToCreateAnAppServiceEnvironment].

An Azure Websites Environment must always be created within a subnet because a subnet provides a network boundary which can be used to lock down inbound traffic behind upstream devices and services such that HTTP and HTTPS traffic is only accepted from specific upstream IP addresses.

Inbound and outbound network traffic on a subnet is controlled using a [network security group][NetworkSecurityGroups].  Controlling inbound traffic requires creating network security rules in a network security group, and then assigning the network security group the subnet containing the Azure Websites Environment.

Once a network security group is assigned to a subnet, inbound traffic to apps in the Azure Websites Environment is allowed/blocked based on the allow and deny rules defined in the network security group.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Network Ports Used in an Azure Websites Environment ##
Before locking down inbound network traffic with a network security group, it is important to know the set of required and optional network ports used by an Azure Websites Environment.  Accidentally closing off traffic to some ports can result in loss of functionality in an Azure Websites Environment.

The following is a list of ports used by an Azure Websites Environment:

- 454:  **Required port** used by Azure infrastructure for managing and maintaining Azure Websites Environments.  Do not block traffic to this port.
- 455:  **Required port** used by Azure infrastructure for managing and maintaining Azure Websites Environments.  Do not block traffic to this port.
- 80:  Default port for inbound HTTP traffic to apps running in App Service Plans in an Azure Websites Environment
- 443: Default port for inbound SSL traffic to apps running in App Service Plans in an Azure Websites Environment
- 21:  Control channel for FTP.  This port can be safely blocked if FTP is not being used.
- 10001-10020: Data channels for FTP.  As with the control channel, these ports can be safely blocked if FTP is not being used   (**Note:** the FTP data channels may change during preview.)
- 4016: Used for remote debugging with Visual Studio 2012.  This port can be safely blocked if the feature is not being used.
- 4018: Used for remote debugging with Visual Studio 2013.  This port can be safely blocked if the feature is not being used.
- 4020: Used for remote debugging with Visual Studio 2015.  This port can be safely blocked if the feature is not being used.

## Outbound Connectivity and DNS Requirements ##
Note that for an Azure Websites Environment to function properly, it also requires outbound access to Azure Storage worldwide as well as Sql Database in the same Azure region.  If outbound Internet access is blocked in the virtual network, Azure Websites Environments will not be able to access these Azure endpoints.

Customer may also have custom DNS servers configured in the virtual network.  Azure Websites Environments need to be able to resolve Azure endpoints under *.database.chinacloudapi.cn, *.file.core.chinacloudapi.cn and *.blob.core.chinacloudapi.cn.  

It is also recommended that any custom DNS servers on the vnet be setup ahead of time prior to creating an Azure Websites Environment.  If a virtual network's DNS configuration is changed while an Azure Websites Environment is being created, that will result in the Azure Websites Environment creation process failing.  In a similar vein, if a custom DNS server exists on the other end of a VPN gateway, and the DNS server is unreachable or unavailable, the Azure Websites Environment creation process will also fail.

## Creating a Network Security Group ##
For full details on how network security groups work see the following [information][NetworkSecurityGroups].  The details below touch on highlights of network security groups, with a focus on configuring and applying a network security group to a subnet that contains an Azure Websites Environment.

**Note:** Network security groups can only be configured using the Powershell cmdlets described below.  Network security groups cannot be configured graphically using the new portal (portal.azure.com) because the new portal only allows graphical configuration of NSGs associated with "v2" virtual networks.  However, Azure Websites Environments currently only work with classic "v1" virtual networks.  As a result only Powershell cmdlets can be used to configure network security groups associated with "v1" virtual networks.

Network security groups are first created as a standalone entity associated with a subscription. Since network security groups are created in an Azure region, ensure that the network security group is created in the same region as the Azure Websites Environment.

The following demonstrates creating a network security group:

    New-AzureNetworkSecurityGroup -Name "testNSGexample" -Location "China East" -Label "Example network security group for an app service environment"

Once a network security group is created, one or more network security rules are added to it.  Since the set of rules may change over time, it is recommended to space out the numbering scheme used for rule priorities to make it easy to insert additional rules over time.

The example below shows a rule that explicitly grants access to the management ports needed by the Azure infrastructure to manage and maintain an Azure Websites Environment.  Note that all management traffic flows over SSL and is secured by client certificates, so even though the ports are opened they are inaccessible by any entity other than Azure management infrastructure.


    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "ALLOW AzureMngmt" -Type Inbound -Priority 100 -Action Allow -SourceAddressPrefix 'INTERNET'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '454-455' -Protocol TCP
    

When locking down access to port 80 and 443 to "hide" an Azure Websites Environment behind upstream devices or services, you will need to know the upstream IP address.  For example, if you are using a web application firewall (WAF), the WAF will have its own IP address (or addresses) which it uses when proxying traffic to a downstream Azure Websites Environment.  You will need to use this IP address in the *SourceAddressPrefix* parameter of a network security rule.

In the example below, inbound traffic from a specific upstream IP address is explicitly allowed.  The address *1.2.3.4* is used as a placeholder for the IP address of an upstream WAF.  Change the value to match the address used by your upstream device or service.

    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT HTTP" -Type Inbound -Priority 200 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '80' -Protocol TCP
    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT HTTPS" -Type Inbound -Priority 300 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '443' -Protocol TCP
    
If FTP support is desired, the following rules can be used as a template to grant access to the FTP control port and data channel ports.  Since FTP is a stateful protocol, you may not be able to route FTP traffic through a traditional HTTP/HTTPS firewall or proxy device.  In this case you will need to set the *SourceAddressPrefix* to a different value - for example the IP address range of developer or deployment machines on which FTP clients are running. 

    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT FTPCtrl" -Type Inbound -Priority 400 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '21' -Protocol TCP
    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT FTPDataRange" -Type Inbound -Priority 500 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '10001-10020' -Protocol TCP

(**Note:**  the data channel port range may change during the preview period.)

If remote debugging with Visual Studio is used, the following rules demonstrate how to grant access.  There is a separate rule for each supported version of Visual Studio since each version uses a different port for remote debugging.  As with FTP access, remote debugging traffic may not flow properly through a traditional WAF or proxy device.  The *SourceAddressPrefix* can instead be set to the IP address range of developer machines running Visual Studio.

    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT RemoteDebuggingVS2012" -Type Inbound -Priority 600 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '4016' -Protocol TCP
    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT RemoteDebuggingVS2013" -Type Inbound -Priority 700 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '4018' -Protocol TCP
    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityRule -Name "RESTRICT RemoteDebuggingVS2015" -Type Inbound -Priority 800 -Action Allow -SourceAddressPrefix '1.2.3.4/32'  -SourcePortRange '*' -DestinationAddressPrefix '*' -DestinationPortRange '4020' -Protocol TCP

## Assigning a Network Security Group to a Subnet ##
A network security group has a default security rule which denies access to all external traffic.  The result from combining the network security rules described above, and the default security rule blocking inbound traffic, is that only traffic from source address ranges associated with an *Allow* action will be able to send traffic to apps running in an Azure Websites Environment.

After a network security group is populated with security rules, it needs to be assigned to the subnet containing the Azure Websites Environment.  The assignment command references both the name of the virtual network where the Azure Websites Environment resides, as well as the name of the subnet where the Azure Websites Environment was created.  

The example below shows a network security group being assigned to a subnet and virtual network:


    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Set-AzureNetworkSecurityGroupToSubnet -VirtualNetworkName 'testVNet' -SubnetName 'Subnet-test'

Once the network security group assignment succeeds (the assignment is a long-running operations and can take a few minutes to complete), only inbound traffic matching *Allow* rules will successfully reach apps in the Azure Websites Environment.

For completeness the following example shows how to remove and thus dis-associate the network security group from the subnet:


    Get-AzureNetworkSecurityGroup -Name "testNSGexample" | Remove-AzureNetworkSecurityGroupFromSubnet -VirtualNetworkName 'testVNet' -SubnetName 'Subnet-test'

## Special Considerations for Explicit IP-SSL ##
If an app is configured with an explicit IP address, instead of the default IP address of the Azure Websites Environment, both HTTP and HTTPS traffic flows into the subnet over a different set of ports other than ports 80 and 443.

The individual pair of ports used for each IP-SSL address can be found by clicking through "All settings" --> "IP Addresses" from an Azure Websites Environment's user interface blade.  The "IP Addresses" blade shows a table of all explicitly configured IP-SSL addresses for the Azure Websites Environment, along with the special port pair that is used to route HTTP and HTTPS traffic associated with each IP-SSL address.  It is this port pair that needs to be used for the DestinationPortRange parameters when configuring rules in a network security group.

## Getting started

To get started with Azure Websites Environments, see [Introduction to Azure Websites Environment][IntroToAppServiceEnvironment]

For details around apps securely connecting to backend resource from an Azure Websites Environment, see [Securely connecting to Backend resources from an Azure Websites Environment][SecurelyConnecttoBackend]

For more information about the Azure Websites platform, see [Azure Websites][AzureAppService].

[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

<!-- LINKS -->
[virtualnetwork]: /documentation/articles/virtual-networks-faq/
[HowToCreateAnAppServiceEnvironment]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[AzureAppService]: /documentation/services/web-sites/
[IntroToAppServiceEnvironment]:  /documentation/articles/app-service-app-service-environment-intro/
[SecurelyConnecttoBackend]:  /documentation/articles/app-service-app-service-environment-securely-connecting-to-backend-resources/ 

<!-- IMAGES -->
 
