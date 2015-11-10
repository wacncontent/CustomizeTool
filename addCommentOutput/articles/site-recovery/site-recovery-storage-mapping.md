<properties
	pageTitle="Site Recovery storage mapping | Windows Azure"
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


# <!-- deleted by customization Azure --> Site Recovery storage mapping


Azure Site Recovery contributes to your business continuity and disaster recovery (BCDR) strategy by orchestrating replication, failover <!-- deleted by customization, --> and recovery of virtual machines and physical servers. Read about possible deployment scenarios in the [Site Recovery <!-- deleted by customization overview](/documentation/articles/site-recovery-overview) --><!-- keep by customization: begin --> Overview](/documentation/articles/hyper-v-recovery-manager-overview) <!-- keep by customization: end -->.


## About this article

Storage mapping is an important element of your Site Recovery deployment. It ensures <!-- deleted by customization you make --><!-- keep by customization: begin --> your making <!-- keep by customization: end --> optimal use of storage. This article describes storage mapping and provides a couple of examples to help you understand how storage mapping works.


Post any questions on the [Azure Recovery Services <!-- deleted by customization Forum](https://social.msdn.microsoft.com/forums/azure/home?forum=hypervrecovmgr) --><!-- keep by customization: begin --> Forum](https://social.msdn.microsoft.com/Forums/zh-CN/home?forum=hypervrecovmgr) <!-- keep by customization: end -->.

## Overview

The way in which you set up storage mapping depends on your Site Recovery deployment scenario.



- **On-premises to on-premises (replicate with Hyper-V Replica)**—Map storage classifications on a source and target VMM servers to do the following:

	- **Identify target storage for replica virtual machines**—Virtual machines will be replicated to a storage target (SMB share or cluster shared volumes (CSVs)) that you choose.
	- **Replica virtual machine placement**—Storage mapping is used to optimally place replica virtual machines on Hyper-V host servers. Replica virtual machines will be placed on hosts that can access the mapped storage classification.
	- **No storage mapping**—If you don’t configure storage mapping <!-- deleted by customization, --> virtual machines will be replicated to the default storage location specified on the Hyper-V host server associated with the replica virtual machine.

- **On-premises to on-premises (replicate with SAN)**—Maps storage arrays pools on a source and target VMM servers to do the following:
	- **Identify target storage pools**—Storage mapping ensures that LUNs in a replication group are replicated <!-- deleted by customization to --> the mapped target storage pool.



## Storage classifications

You map between storage classifications on source and target VMM servers, or on a single VMM server if two sites are managed by the same VMM server. When mapping is configured correctly and replication is enabled, a virtual machine’s virtual hard disk at the primary location will be replicated to storage in <!-- deleted by customization the --> mapped target location. Note that:

- Storage classifications must be available to the host groups located in source and target clouds <!-- deleted by customization. -->
<!-- keep by customization: begin --> - <!-- keep by customization: end --> - Classifications don’t need to have the same type of storage. For example <!-- deleted by customization, --> you can map a source classification that contains SMB shares to a target classification that contains CSVs <!-- deleted by customization. -->
- Read more in [How to create storage classifications in VMM](https://technet.microsoft.com/zh-cn/library/gg610685.aspx).

## Example

If classifications are configured correctly in VMM when you select the source and target VMM server during storage mapping, the source and target classifications will be displayed. Here’s an example of storage files shares and classifications for an organization with two locations in <!-- deleted by customization New York --><!-- keep by customization: begin --> Beijing <!-- keep by customization: end --> and <!-- deleted by customization Chicago --><!-- keep by customization: begin --> Shanghai <!-- keep by customization: end -->.

**Location** | **VMM server** | **File share (source)** | **Classification (source)** | **Mapped to** | **File share (target)**
---|---|--- |---|---|---
<!-- deleted by customization New York --><!-- keep by customization: begin --> Beijing <!-- keep by customization: end --> | VMM_Source| SourceShare1 | GOLD | GOLD_TARGET | TargetShare1
 |  | SourceShare2 | SILVER | SILVER_TARGET | TargetShare2
 | | SourceShare3 | BRONZE | BRONZE_TARGET | TargetShare3
<!-- deleted by customization Chicago --><!-- keep by customization: begin --> Shanghai <!-- keep by customization: end --> | VMM_Target |  | GOLD_TARGET | Not mapped |
| | | SILVER_TARGET | Not mapped |
 | | | BRONZE_TARGET | Not mapped

You'd configure these on the **Server Storage** tab in the **Resources** page of the Site Recovery portal.

![Configure storage mapping](./media/site-recovery-storage-mapping/StorageMapping1.png)

With this example:
- When a a replica virtual machine is created for any virtual machine on GOLD storage (SourceShare1), it will be replicated to a GOLD_TARGET storage (TargetShare1).
- When a replica virtual machine is created for any virtual machine on SILVER storage (SourceShare2), it will be replicated to a SILVER_TARGET (TargetShare2) storage, and so on.

<!-- deleted by customization
The actual file shares and their assigned classifications in VMM appear in the next screen shot.

![Storage classifications in VMM](./media/site-recovery-storage-mapping/StorageMapping2.png)
-->
<!-- keep by customization: begin -->
The actual file shares and their assigned classifications in VMM would be as shown below.

![Storage classifications in VMM](./media/site-recovery-storage-mapping/StorageMapping2.png)
<!-- keep by customization: end -->

## Multiple storage locations

If the target classification is assigned to multiple SMB shares or CSVs <!-- deleted by customization, --> the optimal storage location will be selected automatically when the virtual machine is protected. If no suitable target storage is available with the specified classification, the default storage location specified on the Hyper-V host is used to place the replica virtual hard disks.

The following table show how storage classification and cluster shared volumes are set up in our example.

**Location** | **Classification** | **Associated storage**
---|---|---
<!-- deleted by customization
New York | GOLD | <p>C:\ClusterStorage\SourceVolume1</p><p>\\FileServer\SourceShare1</p>
-->
<!-- keep by customization: begin -->
Beijing | GOLD | <p>C:\ClusterStorage\SourceVolume1</p><p>\\FileServer\SourceShare1</p>
<!-- keep by customization: end -->
 | SILVER | <p>C:\ClusterStorage\SourceVolume2</p><p>\\FileServer\SourceShare2</p>
<!-- deleted by customization
Chicago | GOLD_TARGET | <p>C:\ClusterStorage\TargetVolume1</p><p>\\FileServer\TargetShare1</p>
-->
<!-- keep by customization: begin -->
Shanghai | GOLD_TARGET | <p>C:\ClusterStorage\TargetVolume1</p><p>\\FileServer\TargetShare1</p>
<!-- keep by customization: end -->
 | SILVER_TARGET| <p>C:\ClusterStorage\TargetVolume2</p><p>\\FileServer\TargetShare2</p>

This table summarizes the behavior when you enable protection for virtual machines (VM1 - VM5) in this example environment.

**Virtual machine** | **Source storage** | **Source classification** | **Mapped target storage**
---|---|---|---
VM1 | C:\ClusterStorage\SourceVolume1 | GOLD | <p>C:\ClusterStorage\SourceVolume1</p><p>\\\FileServer\SourceShare1</p><p>Both GOLD_TARGET</p>
VM2 | \\FileServer\SourceShare1 | GOLD | <p>C:\ClusterStorage\SourceVolume1</p><p>\\FileServer\SourceShare1</p> <p>Both GOLD_TARGET</p>
VM3 | C:\ClusterStorage\SourceVolume2 | SILVER | <p>C:\ClusterStorage\SourceVolume2</p><p>\FileServer\SourceShare2</p>
VM4 | \FileServer\SourceShare2 | SILVER |<p>C:\ClusterStorage\SourceVolume2</p><p>\\FileServer\SourceShare2</p><p>Both SILVER_TARGET</p>
<!-- deleted by customization
VM5 | C:\ClusterStorage\SourceVolume3 | N/A | No mapping, so the default storage location of the Hyper-V host is used
-->
<!-- keep by customization: begin -->
VM5 | C:\ClusterStorage\SourceVolume3 | N/A | No mapping so default storage location of the Hyper-V host is used
<!-- keep by customization: end -->

## Next steps

Now that you have a better understanding of storage mapping <!-- deleted by customization, --> start reading the [best practices](/documentation/articles/site-recovery-best-practices) to prepare for deployment.
