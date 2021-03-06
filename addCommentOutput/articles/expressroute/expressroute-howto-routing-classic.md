<properties
   pageTitle="How to configure routing for an ExpressRoute circuit for the classic deployment model using PowerShell | Windows Azure"
   description="This article walks you through the steps for creating and provisioning the private, public and Microsoft peering of an ExpressRoute circuit. This article also shows you how to check the status, update, or delete peerings for your circuit."
   documentationCenter="na"
   services="expressroute"
   authors="cherylmc"
   manager="carolz"
   editor=""
   tags="azure-service-management"/>
<tags
	ms.service="expressroute"
	ms.date="11/05/2015"
	wacn.date=""/>

# Create and modify routing for an ExpressRoute circuit using PowerShell

> [AZURE.SELECTOR]
[PowerShell - Classic](/documentation/articles/expressroute-howto-routing-classic)
[PowerShell - Resource Manager](/documentation/articles/expressroute-howto-routing-arm)

This article walks you through the steps to create and manage routing configuration for an ExpressRoute circuit using PowerShell cmdlets and the classic deployment model.  The steps below will also show you how to check the status, update, or delete and deprovision peerings for an  ExpressRoute circuit.

[AZURE.INCLUDE [vpn-gateway-sm-rm](../includes/vpn-gateway-sm-rm-include.md)] 

## Configuration prerequisites

- You will need the latest version of the Azure PowerShell modules. You can download the latest PowerShell module from the PowerShell section of the [Azure Downloads <!-- deleted by customization page](http://azure.microsoft.com/downloads) --><!-- keep by customization: begin --> page](/downloads/) <!-- keep by customization: end -->. Follow the instructions in the [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure) page for step-by-step guidance on how to configure your computer to use the Azure PowerShell modules.
- Make sure that you have reviewed the [prerequisites](/documentation/articles/expressroute-prerequisites) page, [routing requirements](/documentation/articles/expressroute-routing) page and the [workflows](/documentation/articles/expressroute-workflows) page before you begin configuration.
- You must have an active ExpressRoute circuit. Follow the instructions to [create an ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic) and have the circuit enabled by your connectivity provider before you proceed. The ExpressRoute circuit must be in a provisioned and enabled state for you to be able to run the cmdlets described below.

>[AZURE.IMPORTANT] These instructions only apply for circuits created with service providers offering Layer 2 connectivity services. If you are using a service provider offering managed Layer 3 services (typically an IPVPN, like MPLS), your connectivity provider will configure and manage routing for you. You will not be able to create or manage peerings in such cases. 

You can configure one, two, or all three peerings (Azure private, Azure public and Microsoft) for an ExpressRoute circuit. You can configure peerings in any order you choose. However, you must make sure that you complete the configuration of each peering one at a time. 

## Azure private peering

This section provides instructions on how to create, get, update, and delete the Azure private peering configuration for an ExpressRoute circuit. 

### To create Azure private peering

1. **Import the PowerShell module for ExpressRoute.**
	
	You must import the Azure and ExpressRoute modules into the PowerShell session in order to start using the ExpressRoute cmdlets. Run the following commands to import the Azure and ExpressRoute modules into the PowerShell session.  

	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\Azure.psd1'
	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\ExpressRoute\ExpressRoute.psd1'

2. **Create an ExpressRoute circuit.**
	
	Follow the instructions to create an [ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic) and have it provisioned by the connectivity provider. If your connectivity provider offers managed Layer 3 services, you can request your connectivity provider to enable Azure private peering for you. In that case, you won't need to follow instructions listed in the next sections. However, if your connectivity provider does not manage routing for you, after creating your circuit, follow the instructions below. 

3. **Check the ExpressRoute circuit to ensure it is provisioned.**

	You must first check to see if the ExpressRoute circuit is Provisioned and also Enabled. See the example below.

		PS C:\> Get-AzureDedicatedCircuit -ServiceKey "*********************************"

		Bandwidth                        : 200
		CircuitName                      : MyTestCircuit
		Location                         : Silicon Valley
		ServiceKey                       : *********************************
		ServiceProviderName              : equinix
		ServiceProviderProvisioningState : Provisioned
		Sku                              : Standard
		Status                           : Enabled

	Make sure that the circuit shows as Provisioned and Enabled. If it doesn't, work with your connectivity provider to get your circuit to the required state and status.

		ServiceProviderProvisioningState : Provisioned
		Status                           : Enabled


4. **Configure Azure private peering for the circuit.**

	Make sure that you have the following items before you proceed with the next steps:

	- A /30 subnet for the primary link. This must not be part of any address space reserved for virtual networks.
	- A /30 subnet for the secondary link. This must not be part of any address space reserved for virtual networks.
	- A valid VLAN ID to establish this peering on. Ensure that no other peering in the circuit uses the same VLAN ID.
	- AS number for peering. You can use both 2-byte and 4-byte AS numbers. You can use a private AS number for this peering. Ensure that you are not using 65515.
	- MD5 hash if you choose to use one. **This is optional**.
	
	You can run the following cmdlet to configure Azure private pering for your circuit.

		New-AzureBGPPeering -AccessType Private -ServiceKey "*********************************" -PrimaryPeerSubnet "10.0.0.0/30" -SecondaryPeerSubnet "10.0.0.4/30" -PeerAsn 1234 -VlanId 100

	You can use the cmdlet below if you choose to use an MD5 hash.

		New-AzureBGPPeering -AccessType Private -ServiceKey "*********************************" -PrimaryPeerSubnet "10.0.0.0/30" -SecondaryPeerSubnet "10.0.0.4/30" -PeerAsn 1234 -VlanId 100 -SharedKey "A1B2C3D4"

	>[AZURE.IMPORTANT] Ensure that you specify your AS number as peering ASN, not customer ASN.

### To get Azure private peering details

You can get configuration details using the following cmdlet

	Get-AzureBGPPeering -AccessType Private -ServiceKey "*********************************"
	
	AdvertisedPublicPrefixes       : 
	AdvertisedPublicPrefixesState  : Configured
	AzureAsn                       : 12076
	CustomerAutonomousSystemNumber : 
	PeerAsn                        : 1234
	PrimaryAzurePort               : 
	PrimaryPeerSubnet              : 10.0.0.0/30
	RoutingRegistryName            : 
	SecondaryAzurePort             : 
	SecondaryPeerSubnet            : 10.0.0.4/30
	State                          : Enabled
	VlanId                         : 100


### To update Azure private peering configuration

You can update any part of the configuration using the following cmdlet. In the example below, the VLAN ID of the circuit is being updated from 100 to 500.

	Set-AzureBGPPeering -AccessType Private -ServiceKey "*********************************" -PrimaryPeerSubnet "10.0.0.0/30" -SecondaryPeerSubnet "10.0.0.4/30" -PeerAsn 1234 -VlanId 500 -SharedKey "A1B2C3D4"

### To delete Azure private peering

You can remove your peering configuration by running the following cmdlet.

>[AZURE.WARNING] You must ensure that all virtual networks are unlinked from the ExpressRoute circuit before running this cmdlet. 

	Remove-AzureBGPPeering -AccessType Private -ServiceKey "*********************************"


## Azure public peering

This section provides instructions on how to create, get, update and delete the Azure public peering configuration for an ExpressRoute circuit.

### To create Azure public peering

1. **Import the PowerShell module for ExpressRoute.**
	
	You must import the Azure and ExpressRoute modules into the PowerShell session in order to start using the ExpressRoute cmdlets. Run the following commands to import the Azure and ExpressRoute modules into the PowerShell session. 

	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\Azure.psd1'
	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\ExpressRoute\ExpressRoute.psd1'

2. **Create an ExpressRoute circuit**
	
	Follow the instructions to create an [ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic) and have it provisioned by the connectivity provider. If your connectivity provider offers managed Layer 3 services, you can request your connectivity provider to enable Azure private peering for you. In that case, you won't need to follow instructions listed in the next sections. However, if your connectivity provider does not manage routing for you, after creating your circuit, follow the instructions below.

3. **Check ExpressRoute circuit to ensure it is provisioned**

	You must first check to see if the ExpressRoute circuit is Provisioned and also Enabled. See the example below.

		PS C:\> Get-AzureDedicatedCircuit -ServiceKey "*********************************"

		Bandwidth                        : 200
		CircuitName                      : MyTestCircuit
		Location                         : Silicon Valley
		ServiceKey                       : *********************************
		ServiceProviderName              : equinix
		ServiceProviderProvisioningState : Provisioned
		Sku                              : Standard
		Status                           : Enabled

	Make sure that the circuit shows as Provisioned and Enabled. If it doesn't, work with your connectivity provider to get your circuit to the required state and status.

		ServiceProviderProvisioningState : Provisioned
		Status                           : Enabled

	

4. **Configure Azure public peering for the circuit**

	Ensure that you have the following information before you proceed further.

	- A /30 subnet for the primary link. This must be a valid public IPv4 prefix.
	- A /30 subnet for the secondary link. This must be a valid public IPv4 prefix.
	- A valid VLAN ID to establish this peering on. Ensure that no other peering in the circuit uses the same VLAN ID.
	- AS number for peering. You can use both 2-byte and 4-byte AS numbers. You must use a public AS number for this peering.
	- MD5 hash if you choose to use one. **This is optional**.
	
	You can run the following cmdlet to configure Azure private pering for your circuit

		New-AzureBGPPeering -AccessType Public -ServiceKey "*********************************" -PrimaryPeerSubnet "131.107.0.0/30" -SecondaryPeerSubnet "131.107.0.4/30" -PeerAsn 1234 -VlanId 200

	You can use the cmdlet below if you choose to use an MD5 hash

		New-AzureBGPPeering -AccessType Public -ServiceKey "*********************************" -PrimaryPeerSubnet "131.107.0.0/30" -SecondaryPeerSubnet "131.107.0.4/30" -PeerAsn 1234 -VlanId 200 -SharedKey "A1B2C3D4"

	>[AZURE.IMPORTANT] Ensure that you specify your AS number as peering ASN and not customer ASN.

### To get Azure public peering details

You can get configuration details using the following cmdlet

	Get-AzureBGPPeering -AccessType Public -ServiceKey "*********************************"
	
	AdvertisedPublicPrefixes       : 
	AdvertisedPublicPrefixesState  : Configured
	AzureAsn                       : 12076
	CustomerAutonomousSystemNumber : 
	PeerAsn                        : 1234
	PrimaryAzurePort               : 
	PrimaryPeerSubnet              : 131.107.0.0/30
	RoutingRegistryName            : 
	SecondaryAzurePort             : 
	SecondaryPeerSubnet            : 131.107.0.4/30
	State                          : Enabled
	VlanId                         : 200


### To update Azure public peering configuration

You can update any part of the configuration using the following cmdlet

	Set-AzureBGPPeering -AccessType Public -ServiceKey "*********************************" -PrimaryPeerSubnet "131.107.0.0/30" -SecondaryPeerSubnet "131.107.0.4/30" -PeerAsn 1234 -VlanId 600 -SharedKey "A1B2C3D4"

The VLAN ID of the circuit is being updated from 200 to 600 in the above example.

### To delete Azure public peering

You can remove your peering configuration by running the following cmdlet

	Remove-AzureBGPPeering -AccessType Public -ServiceKey "*********************************"

## Microsoft peering

This section provides instructions on how to create, get, update and delete the Microsoft peering configuration for an ExpressRoute circuit. 

### To create Microsoft peering

1. **Import the PowerShell module for ExpressRoute.**
	
	You must import the Azure and ExpressRoute modules into the PowerShell session in order to start using the ExpressRoute cmdlets. Run the following commands to import the Azure and ExpressRoute modules into the PowerShell session.  

	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\Azure.psd1'
	    Import-Module 'C:\Program Files (x86)\Microsoft SDKs\Azure\PowerShell\ServiceManagement\Azure\ExpressRoute\ExpressRoute.psd1'

2. **Create an ExpressRoute circuit**
	
	Follow the instructions to create an [ExpressRoute circuit](/documentation/articles/expressroute-howto-circuit-classic) and have it provisioned by the connectivity provider. If your connectivity provider offers managed Layer 3 services, you can request your connectivity provider to enable Azure private peering for you. In that case, you won't need to follow instructions listed in the next sections. However, if your connectivity provider does not manage routing for you, after creating your circuit, follow the instructions below.

3. **Check ExpressRoute circuit to ensure it is provisioned**

	You must first check to see if the ExpressRoute circuit is in Provisioned and Enabled state.

		PS C:\> Get-AzureDedicatedCircuit -ServiceKey "*********************************"

		Bandwidth                        : 200
		CircuitName                      : MyTestCircuit
		Location                         : Silicon Valley
		ServiceKey                       : *********************************
		ServiceProviderName              : equinix
		ServiceProviderProvisioningState : Provisioned
		Sku                              : Standard
		Status                           : Enabled

	Make sure that the circuit shows as Provisioned and Enabled. If it doesn't, work with your connectivity provider to get your circuit to the required state and status.

		ServiceProviderProvisioningState : Provisioned
		Status                           : Enabled


4. **Configure Microsoft peering for the circuit**

	Make sure that you have the following information before you proceed.

	- A /30 subnet for the primary link. This must be a valid public IPv4 prefix owned by you and registered in an RIR / IRR.
	- A /30 subnet for the secondary link. This must be a valid public IPv4 prefix owned by you and registered in an RIR / IRR.
	- A valid VLAN ID to establish this peering on. Ensure that no other peering in the circuit uses the same VLAN ID.
	- AS number for peering. You can use both 2-byte and 4-byte AS numbers. You must use public AS numbers only. You must own the AS number.
	- Advertised prefixes: You must provide a list of all prefixes you plan to advertise over the BGP session. Only public IP address prefixes are accepted. You can send a comma separated list if you plan to send a set of prefixes. These prefixes must be registered to you in an RIR / IRR.
	- Customer ASN: If you are advertising prefixes that are not registered to the peering AS number, you can specify the AS number to which they are registered. **This is optional**.
	- Routing Registry Name: You can specify the RIR / IRR against which the AS number and prefixes are registered.
	- A MD5 hash, if you choose to use one. **This is optional.**
	
	You can run the following cmdlet to configure Microsoft pering for your circuit

		New-AzureBGPPeering -AccessType Microsoft -ServiceKey "*********************************" -PrimaryPeerSubnet "131.107.0.0/30" -SecondaryPeerSubnet "131.107.0.4/30" -VlanId 300 -PeerAsn 1234 -CustomerAsn 2245 -AdvertisedPublicPrefixes "123.0.0.0/30" -RoutingRegistryName "ARIN" -SharedKey "A1B2C3D4"


### To get Microsoft peering details

You can get configuration details using the following cmdlet.

	Get-AzureBGPPeering -AccessType Microsoft -ServiceKey "*********************************"
	
	AdvertisedPublicPrefixes       : 123.0.0.0/30
	AdvertisedPublicPrefixesState  : Configured
	AzureAsn                       : 12076
	CustomerAutonomousSystemNumber : 2245
	PeerAsn                        : 1234
	PrimaryAzurePort               : 
	PrimaryPeerSubnet              : 10.0.0.0/30
	RoutingRegistryName            : ARIN
	SecondaryAzurePort             : 
	SecondaryPeerSubnet            : 10.0.0.4/30
	State                          : Enabled
	VlanId                         : 300


### To update Microsoft peering configuration

You can update any part of the configuration using the following cmdlet.

		Set-AzureBGPPeering -AccessType Microsoft -ServiceKey "*********************************" -PrimaryPeerSubnet "131.107.0.0/30" -SecondaryPeerSubnet "131.107.0.4/30" -VlanId 300 -PeerAsn 1234 -CustomerAsn 2245 -AdvertisedPublicPrefixes "123.0.0.0/30" -RoutingRegistryName "ARIN" -SharedKey "A1B2C3D4"

### To delete Microsoft peering

You can remove your peering configuration by running the following cmdlet.

	Remove-AzureBGPPeering -AccessType Microsoft -ServiceKey "*********************************"

## Next steps

Next, [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-classic).
-  For more information about workflows, see [ExpressRoute workflows](/documentation/articles/expressroute-workflows).
-  For more information about circuit peering, see [ExpressRoute circuits and routing domains](/documentation/articles/expressroute-circuit-peerings).

