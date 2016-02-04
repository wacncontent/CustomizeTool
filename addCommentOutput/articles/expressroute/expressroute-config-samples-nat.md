<properties
   pageTitle="ExpressRoute customer router configuration samples | Windows Azure"
   description="This page provides router configuration samples for Cisco and Juniper routers."
   documentationCenter="na"
   services="expressroute"
   authors="cherylmc"
   manager="carolz"
   editor="" />
<tags
	ms.service="expressroute"
	ms.date="10/12/2015"
	wacn.date=""/>

# Router configuration samples to setup and manage NAT

This page provides NAT configuration samples for Cisco ASA and Juniper MX series routers. These are intended to be samples for guidance only and must not be used as is. You can work with your vendor to come up with appropriate configurations for your network. 

>[AZURE.IMPORTANT] Samples in this page are intended to be purely for guidance. You must work with your vendor's sales / technical team and your networking team to come up with appropriate configurations to meet your needs. Microsoft will not support issues related to configurations listed in this page. You must contact your device vendor for support issues.

Router configuration samples below apply to Azure Public and Microsoft peerings. You must not configure NAT for Azure private peering. Review [ExpressRoute peerings](/documentation/articles/expressroute-circuit-peerings) and [ExpressRoute NAT requirements](/documentation/articles/expressroute-nat) for more details.

**Note:** You MUST use separate NAT IP pools for connectivity to the internet and ExpressRoute. Using the same NAT IP pool across the internet and ExpressRoute will result in asymmetric routing and loss of connectivity.

## Cisco ASA firewalls

### PAT configuration for traffic from customer network to Microsoft

    object network MSFT-PAT
      range <SNAT-START-IP> <SNAT-END-IP>
    
    
    object-group network MSFT-Range
      network-object <IP> <Subnet_Mask>
    
    object-group network on-prem-range-1
<!-- deleted by customization
      network-object <IP> <Subnet-Mask>
-->
<!-- keep by customization: begin -->
      network-object <IP> <Subnet_Mask>
<!-- keep by customization: end -->
    
    object-group network on-prem-range-2
<!-- deleted by customization
      network-object <IP> <Subnet-Mask>
-->
<!-- keep by customization: begin -->
      network-object <IP> <Subnet_Mask>
<!-- keep by customization: end -->
    
    object-group network on-prem
      network-object object on-prem-range-1
      network-object object on-prem-range-2
    
    nat (outside,inside) source dynamic on-prem pat-pool MSFT-PAT destination static MSFT-Range MSFT-Range

<!-- deleted by customization
### PAT configuration for traffic from Microsoft to customer network

#### Interfaces and Direction:
	Source Interface (where the traffic enters the ASA): inside
	Destination Interface (where the traffic exits the ASA): outside

#### Configuration:
NAT Pool:

	object network outbound-PAT
		host <NAT-IP>

Target Server:

	object network Customer-Network
		network-object <IP> <Subnet-Mask>

Object Group for Customer IP Addresses

	object-group network MSFT-Network-1
		network-object <MSFT-IP> <Subnet-Mask>
	
	object-group network MSFT-PAT-Networks
		network-object object MSFT-Network-1

NAT Commands:

	nat (inside,outside) source dynamic MSFT-PAT-Networks pat-pool outbound-PAT destination static Customer-Network Customer-Network
-->


## Juniper MX series routers 

### 1. Create redundant Ethernet interfaces for the cluster

	interfaces {
	    reth0 {
	        description "To Internal Network";
	        vlan-tagging;
	        redundant-ether-options {
	            redundancy-group 1;
	        }
	        unit 100 {
	            vlan-id 100;
	            family inet {
<!-- deleted by customization
	                address <IP-Address/Subnet-mask>;
-->
<!-- keep by customization: begin -->
	                address <IP_Address/Subnet_mask>;
<!-- keep by customization: end -->
	            }
	        }
	    }
	    reth1 {
	        description "To Microsoft via Edge Router";
	        vlan-tagging;
	        redundant-ether-options {
	            redundancy-group 2;
	        }
	        unit 100 {
	            description "To Microsoft via Edge Router";
	            vlan-id 100;
	            family inet {
<!-- deleted by customization
	                address <IP-Address/Subnet-mask>;
-->
<!-- keep by customization: begin -->
	                address <IP_Address/Subnet_mask>;
<!-- keep by customization: end -->
	            }
	        }
	    }
	}


### 2. Create two security zones

 - Trust Zone for internal network and Untrust Zone for external network facing Edge Routers
 - Assign appropriate interfaces to the zones
 - Allow services on the interfaces


	security {   
	 zones {
	        security-zone Trust {
	            host-inbound-traffic {
	                system-services {
	                    ping;
	                }
	                protocols {
	                    bgp;
	                }
	            }
	            interfaces {
	                reth0.100;
	            }
	        }
	        security-zone Untrust {
	            host-inbound-traffic {
	                system-services {
	                    ping;
	                }
	                protocols {
	                    bgp;
	                }
	            }
	            interfaces {
	                reth1.100;
	            }
	        }
	    }
	}


### 3. Create security policies between zones
 
	security {
	    policies {
	        from-zone Trust to-zone Untrust {
	            policy allow-any {
	                match {
	                    source-address any;
	                    destination-address any;
	                    application any;
	                }
	                then {
	                    permit;
	                }
	            }
	        }
	        from-zone Untrust to-zone Trust {
	            policy allow-any {
	                match {
	                    source-address any;
	                    destination-address any;
	                    application any;
	                }
	                then {
	                    permit;
	                }
	            }
	        }
	    }
	}


### 4. Configure NAT policies
 - Create two NAT pools. One will be used to NAT traffic outbound to Microsoft and other from Microsoft to the customer.
 - Create rules to NAT the respective traffic

		security {
		    nat {
		        source {
<!-- deleted by customization
		            pool SNAT-To-ExpressRoute {
-->
<!-- keep by customization: begin -->
		            pool SNAT_To_ExpressRoute {
<!-- keep by customization: end -->
		                routing-instance {
<!-- deleted by customization
		                    External-ExpressRoute;
-->
<!-- keep by customization: begin -->
		                    External_ExpressRoute;
<!-- keep by customization: end -->
		                }
		                address {
<!-- deleted by customization
		                    <NAT-IP-address/Subnet-mask>;
-->
<!-- keep by customization: begin -->
		                    <NAT_IP_address/Subnet_mask>;
<!-- keep by customization: end -->
		                }
		            }
<!-- deleted by customization
		            pool SNAT-From-ExpressRoute {
-->
<!-- keep by customization: begin -->
		            pool SNAT_From_ExpressRoute {
<!-- keep by customization: end -->
		                routing-instance {
		                    Internal;
		                }
		                address {
<!-- deleted by customization
		                    <NAT-IP-address/Subnet-mask>;
-->
<!-- keep by customization: begin -->
		                    <NAT_IP_address/Subnet_mask>;
<!-- keep by customization: end -->
		                }
		            }
		            rule-set Outbound_NAT {
		                from routing-instance Internal;
<!-- deleted by customization
		                to routing-instance External-ExpressRoute;
		                rule SNAT-Out {
-->
<!-- keep by customization: begin -->
		                to routing-instance External_ExpressRoute;
		                rule SNAT_Out {
<!-- keep by customization: end -->
		                    match {
		                        source-address 0.0.0.0/0;
		                    }
		                    then {
		                        source-nat {
		                            pool {
<!-- deleted by customization
		                                SNAT-To-ExpressRoute;
-->
<!-- keep by customization: begin -->
		                                SNAT_To_ExpressRoute;
<!-- keep by customization: end -->
		                            }
		                        }
		                    }
		                }
		            }
<!-- deleted by customization
		            rule-set Inbound-NAT {
		                from routing-instance External-ExpressRoute;
-->
<!-- keep by customization: begin -->
		            rule-set Inbound_NAT {
		                from routing-instance External_ExpressRoute;
<!-- keep by customization: end -->
		                to routing-instance Internal;
<!-- deleted by customization
		                rule SNAT-In {
-->
<!-- keep by customization: begin -->
		                rule SNAT_In {
<!-- keep by customization: end -->
		                    match {
		                        source-address 0.0.0.0/0;
		                    }
		                    then {
		                        source-nat {
		                            pool {
<!-- deleted by customization
		                                SNAT-From-ExpressRoute;
-->
<!-- keep by customization: begin -->
		                                SNAT_From_ExpressRoute;
<!-- keep by customization: end -->
		                            }
		                        }
		                    }
		                }
		            }
		        }
		    }
		}


### 5. Configure BGP to advertise selective prefixes in each direction

Refer to samples in [Routing configuration samples ](/documentation/articles/expressroute-config-samples-routing) page.

### 6. Create policies

	routing-options {
<!-- deleted by customization
	    	      autonomous-system <Customer-ASN>;
-->
<!-- keep by customization: begin -->
	    	      autonomous-system <Customer_ASN>;
<!-- keep by customization: end -->
	}
	policy-options {
<!-- deleted by customization
	    prefix-list Microsoft-Prefixes {
	        <IP-Address/Subnet-Mask;
	        <IP-Address/Subnet-Mask;
-->
<!-- keep by customization: begin -->
	    prefix-list Microsoft_Prefixes {
	        <IP_Address/Subnet_Mask;
	        <IP_Address/Subnet_Mask;
<!-- keep by customization: end -->
	    }
	    prefix-list private-ranges {
	        10.0.0.0/8;
	        172.16.0.0/12;
	        192.168.0.0/16;
	        100.64.0.0/10;
	    }
<!-- deleted by customization
	    policy-statement Advertise-NAT-Pools {
-->
<!-- keep by customization: begin -->
	    policy-statement Advertise_NAT_Pools {
<!-- keep by customization: end -->
	        from {
	            protocol static;
<!-- deleted by customization
	            route-filter <NAT-Pool-Address/Subnet-mask> prefix-length-range /32-/32;
-->
<!-- keep by customization: begin -->
	            route-filter <NAT_Pool_Address/Subnet_mask> prefix-length-range /32-/32;
<!-- keep by customization: end -->
	        }
	        then accept;
	    }
<!-- deleted by customization
	    policy-statement Accept-from-Microsoft {
-->
<!-- keep by customization: begin -->
	    policy-statement Accept_from_Microsoft {
<!-- keep by customization: end -->
	        term 1 {
	            from {
<!-- deleted by customization
	                instance External-ExpressRoute;
	                prefix-list-filter Microsoft-Prefixes orlonger;
-->
<!-- keep by customization: begin -->
	                instance External_ExpressRoute;
	                prefix-list-filter Microsoft_Prefixes orlonger;
<!-- keep by customization: end -->
	            }
	            then accept;
	        }
	        term deny {
	            then reject;
	        }
	    }
<!-- deleted by customization
	    policy-statement Accept-from-Internal {
-->
<!-- keep by customization: begin -->
	    policy-statement Accept_from_Internal {
<!-- keep by customization: end -->
	        term no-private {
	            from {
	                instance Internal;
	                prefix-list-filter private-ranges orlonger;
	            }
	            then reject;
	        }
	        term bgp {
	            from {
	                instance Internal;
	                protocol bgp;
	            }
	            then accept;
	        }
	        term deny {
	            then reject;
	        }
	    }
	}
	routing-instances {
	    Internal {
	        instance-type virtual-router;
	        interface reth0.100;
	        routing-options {
	            static {
<!-- deleted by customization
	                route <NAT-Pool-IP-Address/Subnet-mask> discard;
-->
<!-- keep by customization: begin -->
	                route <NAT_Pool_IP_Address/Subnet_mask> discard;
<!-- keep by customization: end -->
	            }
<!-- deleted by customization
	            instance-import Accept-from-Microsoft;
-->
<!-- keep by customization: begin -->
	            instance-import Accept_from_Microsoft;
<!-- keep by customization: end -->
	        }
	        protocols {
	            bgp {
	                group customer {
<!-- deleted by customization
	                    export <Advertise-NAT-Pools>;
	                    peer-as <Customer-ASN-1>;
	                    neighbor <BGP-Neighbor-IP-Address>;
	                }
	            }
-->
<!-- keep by customization: begin -->
	                    export <Advertise_NAT_Pools>;
	                    peer-as <Customer_ASN_1>;
	                    neighbor <BGP_Neighbor_IP_Address>;
	                }
<!-- keep by customization: end -->
	        }
	    }
<!-- deleted by customization
	    External-ExpressRoute {
-->
<!-- keep by customization: begin -->
	    }
	    External_ExpressRoute {
<!-- keep by customization: end -->
	        instance-type virtual-router;
	        interface reth1.100;
	        routing-options {
	            static {
<!-- deleted by customization
	                route <NAT-Pool-IP-Address/Subnet-mask> discard;
-->
<!-- keep by customization: begin -->
	                route <NAT_Pool_IP_Address/Subnet_mask> discard;
<!-- keep by customization: end -->
	            }
<!-- deleted by customization
	            instance-import Accept-from-Internal;
-->
<!-- keep by customization: begin -->
	            instance-import Accept_from_Internal;
<!-- keep by customization: end -->
	        }
	        protocols {
	            bgp {
<!-- deleted by customization
	                group edge-router {
	                    export <Advertise-NAT-Pools>;
	                    peer-as <Customer-Public-ASN>;
	                    neighbor <BGP-Neighbor-IP-Address>;
-->
<!-- keep by customization: begin -->
	                group edge_router {
	                    export <Advertise_NAT_Pools>;
	                    peer-as <Customer_Public_ASN>;
	                    neighbor <BGP_Neighbor_IP_Address>;
<!-- keep by customization: end -->
	                }
	            }
	        }
	    }
	}

## Next steps

See the [ExpressRoute FAQ](/documentation/articles/expressroute-faqs) for more details.
