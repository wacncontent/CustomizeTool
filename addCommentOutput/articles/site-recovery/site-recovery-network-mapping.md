<properties
	pageTitle="Azure Site Recovery network mapping | Windows Azure"
	description="Azure Site Recovery coordinates the replication, failover, and recovery of virtual machines and physical servers located on-premises to Azure or to a secondary on-premises site."
	services="site-recovery"
	documentationCenter=""
	authors="rayne-wiselman"
	manager="jwhit"
	editor=""/>

<tags
	ms.service="site-recovery"
	ms.date="10/07/2015"
	wacn.date=""/>


# Azure Site Recovery network mapping


Azure Site Recovery contributes to your business continuity and disaster recovery (BCDR) strategy by orchestrating replication, failover <!-- deleted by customization, --> and recovery of virtual machines and physical servers. Read about possible deployment scenarios in the [Site Recovery <!-- deleted by customization overview](/documentation/articles/site-recovery-overview) --><!-- keep by customization: begin --> Overview](/documentation/articles/site-recovery-overview) <!-- keep by customization: end -->.


## About this article

Network mapping is an important element when you deploy VMM and Site Recovery. It optimally places replicated virtual machines on target Hyper-V host servers, and ensures your replicated virtual machines are connected to appropriate networks after failover. This article describes network mapping and provides a couple of examples to help you understand how network mapping works.


Post any questions on the [Azure Recovery Services <!-- deleted by customization Forum](https://social.msdn.microsoft.com/forums/azure/home?forum=hypervrecovmgr) --><!-- keep by customization: begin --> Forum](https://social.msdn.microsoft.com/Forums/zh-CN/home?forum=hypervrecovmgr) <!-- keep by customization: end -->.

## Overview

The way in which you set up network mapping depends on your Site Recovery deployment scenario.



- **On-premises to on-premises VMM servers**—Network mapping maps between VM networks on a source VMM server and VM networks on a target VMM server to do the following:

	- **Connect virtual machines after failover**—Ensures that virtual machines will be connected to appropriate networks after failover. The replica virtual machine will be connected to the target network that is mapped to the source network.
	- **Place replica virtual machines on host servers**—Optimally place replica virtual machines on Hyper-V host servers. Replica virtual machines will be placed on hosts that can access the mapped VM networks.
	- **No network mapping**—If you don’t configure network mapping, replicated virtual machines won’t be connected to any VM networks after failover.

- **On-premises VMM server to Azure**—Network mapping maps between VM networks on the source VMM server and target Azure networks to do the following:
	- **Connect virtual machines after failover**—All machines which failover on the same network can connect to each other, irrespective of which recovery plan they are in.
	- **Network gateway**—If a network gateway is set up on the target Azure network, virtual machines can connect to other on-premises virtual machines.
	- **No network mapping**—If you don’t configure network mapping, only virtual machines that failover in the same recovery plan will be able to connect to each other after fail over to Azure.

## VM networks

A VMM logical network provides an abstract view of the physical network infrastructure. VM networks provide a network interface so that virtual machines can connect to logical networks. A logical network needs at least one VM network. When you place a virtual machine in a cloud for protection, it must be connected to a VM network that links to a logical network associated with the cloud. Learn more at:

- [Logical Networks (Part 1)](http://blogs.technet.com/b/scvmm/archive/2013/02/14/networking-in-vmm-2012-sp1-logical-networks-part-i.aspx)
- [Virtual Networking in VMM 2012 SP1](http://blogs.technet.com/b/scvmm/archive/2013/01/08/virtual-networking-in-vmm-2012-sp1.aspx)

## Example

Network mapping can be configured between VM networks on two VMM servers, or on a single VMM server if two sites are managed by the same server. When mapping is configured correctly and replication is enabled, a virtual machine at the primary location will be connected to a network, and its replica at the target location will be connected to its mapped network.

If networks have been set up correctly in VMM, when you select a target VM network during network mapping, the VMM source clouds that use the source VM network will be displayed, along with the available target VM networks on the target clouds that are used for protection.

Here’s an example to illustrate this mechanism. Let’s take an organization with two locations in <!-- deleted by customization New York --><!-- keep by customization: begin --> Beijing <!-- keep by customization: end --> and <!-- deleted by customization Chicago --><!-- keep by customization: begin --> Shanghai <!-- keep by customization: end -->.

**Location** | **VMM server** | **VM networks** | **Mapped to**
---|---|---|---
<!-- deleted by customization
New York | VMM-NewYork| VMNetwork1-NewYork | Mapped to VMNetwork1-Chicago
 |  | VMNetwork2-NewYork | Not mapped
Chicago | VMM-Chicago| VMNetwork1-Chicago | Mapped to VMNetwork1-NewYork
 | | VMNetwork1-Chicago | Not mapped
-->
<!-- keep by customization: begin -->
Beijing | VMM-Beijing| VMNetwork1-Beijing | Mapped to VMNetwork1-Shanghai
 |  | VMNetwork2-Beijing | Not mapped
Shanghai | VMM-Shanghai| VMNetwork1-Shanghai | Mapped to VMNetwork1-Beijing
 | | VMNetwork1-Shanghai | Not mapped
<!-- keep by customization: end -->

With this example:

- When a replica virtual machine is created for any virtual machine that is connected to <!-- deleted by customization VMNetwork1-NewYork --><!-- keep by customization: begin --> VMNetwork1-Beijing <!-- keep by customization: end -->, it will be connected to <!-- deleted by customization VMNetwork1-Chicago --><!-- keep by customization: begin --> VMNetwork1-Shanghai <!-- keep by customization: end -->.
- When a replica virtual machine is created for <!-- deleted by customization VMNetwork2-NewYork --><!-- keep by customization: begin --> VMNetwork2-Beijing <!-- keep by customization: end --> or <!-- deleted by customization VMNetwork2-Chicago --><!-- keep by customization: begin --> VMNetwork2-Shanghai <!-- keep by customization: end -->, it will not be connected to any network.

Here's how VMM clouds are set up in our example organization, and the logical networks associated with the clouds.

### Cloud protection settings

**Protected cloud** | **Protecting cloud** | **Logical network <!-- deleted by customization (New York)** --><!-- keep by customization: begin --> (Beijing)** <!-- keep by customization: end -->
---|---|---
GoldCloud1 | GoldCloud2 |
SilverCloud1| SilverCloud2 |
<!-- deleted by customization
GoldCloud2 | <p>NA</p><p></p> | <p>LogicalNetwork1-NewYork</p><p>LogicalNetwork1-Chicago</p>
SilverCloud2 | <p>NA</p><p></p> | <p>LogicalNetwork1-NewYork</p><p>LogicalNetwork1-Chicago</p>
-->
<!-- keep by customization: begin -->
GoldCloud2 | <p>NA</p><p></p> | <p>LogicalNetwork1-Beijing</p><p>LogicalNetwork1-Shanghai</p>
SilverCloud2 | <p>NA</p><p></p> | <p>LogicalNetwork1-Beijing</p><p>LogicalNetwork1-Shanghai</p>
<!-- keep by customization: end -->

### Logical and VM network settings

**Location** | **Logical network** | **Associated VM network**
---|---|---
<!-- deleted by customization
New York | LogicalNetwork1-NewYork | VMNetwork1-NewYork
Chicago | LogicalNetwork1-Chicago | VMNetwork1-Chicago
 | LogicalNetwork2Chicago | VMNetwork2-Chicago
-->
<!-- keep by customization: begin -->
Beijing | LogicalNetwork1-Beijing | VMNetwork1-Beijing
Shanghai | LogicalNetwork1-Shanghai | VMNetwork1-Shanghai
 | LogicalNetwork2Shanghai | VMNetwork2-Shanghai
<!-- keep by customization: end -->

### Target networks

Based on these settings, when you select the target VM network, the following table shows the choices that will be available.

**Select** | **Protected cloud** | **Protecting cloud** | **Target network available**
---|---|---|---
<!-- deleted by customization
VMNetwork1-Chicago | SilverCloud1 | SilverCloud2 | Available
-->
<!-- keep by customization: begin -->
VMNetwork1-Shanghai | SilverCloud1 | SilverCloud2 | Available
<!-- keep by customization: end -->
 | GoldCloud1 | GoldCloud2 | Available
<!-- deleted by customization VMNetwork2-Chicago --><!-- keep by customization: begin --> VMNetwork2-Shanghai <!-- keep by customization: end --> | SilverCloud1 | SilverCloud2 | Not available
 | GoldCloud1 | GoldCloud2 | Available



## Multiple subnets

If the target network has multiple subnets and one of those subnets has the same name as the subnet on which the source virtual machine is located, then the replica virtual machine will be connected to that target subnet after failover. If there’s no target subnet with a matching name, the virtual machine will be connected to the first subnet in the network.


### Failback

To see what happens in the case of failback (reverse replication), let’s assume that <!-- deleted by customization VMNetwork1-NewYork --><!-- keep by customization: begin --> VMNetwork1-Beijing <!-- keep by customization: end --> is mapped to <!-- deleted by customization VMNetwork1-Chicago --><!-- keep by customization: begin --> VMNetwork1-Shanghai <!-- keep by customization: end -->, with the following settings.


**Virtual machine** | **Connected to VM network**
---|---
VM1 | VMNetwork1-Network
<!-- deleted by customization
VM2 (replica of VM1) | VMNetwork1-Chicago
-->
<!-- keep by customization: begin -->
VM2 (replica of VM1) | VMNetwork1-Shanghai
<!-- keep by customization: end -->

With these settings, let's review what happens in a couple of possible scenarios.

**Scenario** | **Outcome**
---|---
No change in the network properties of VM-2 after failover <!-- deleted by customization. --> | VM-1 remains connected to the source network.
<!-- deleted by customization
Network properties of VM-2 are changed after failover and is disconnected. | VM-1 is disconnected.
Network properties of VM-2 are changed after failover and is connected to VMNetwork2-Chicago. | If VMNetwork2-Chicago isn’t mapped, VM-1 will be disconnected.
Network mapping of VMNetwork1-Chicago is changed. | VM-1 will be connected to the network now mapped to VMNetwork1-Chicago.
-->
<!-- keep by customization: begin -->
Network properties of VM-2 are changed after failover and is disconnected | VM-1 is disconnected
Network properties of VM-2 are changed after failover and is connected to VMNetwork2-Shanghai | If VMNetwork2-Shanghai isn’t mapped, VM-1 will be disconnected
Network mapping of VMNetwork1-Shanghai is changed | VM-1 will be connected to the network now mapped to VMNetwork1-Shanghai
<!-- keep by customization: end -->


## Next steps

Now that you have a better understanding of network mapping <!-- deleted by customization, --> start reading the [best practices](/documentation/articles/site-recovery-best-practices) to prepare for deployment.
