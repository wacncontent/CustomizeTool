<properties
 pageTitle="Virtual machine sizes | Windows Azure"
 description="Lists the different sizes for virtual machines and their capacities."
 services="virtual-machines"
 documentationCenter=""
 authors="cynthn"
 manager="timlt"
 editor=""
 tags="azure-resource-manager,azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/05/2016"
	wacn.date=""/>

# Sizes for virtual machines

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)]

## Overview

This article describes the available sizes and options for the virtual machine-based compute resources you can use to run your apps and workloads.  It also provides deployment considerations to be aware of when you're planning to use these resources. For information about pricing of the various sizes, see [Virtual Machines Pricing](/home/features/virtual-machines/#price).

To see general limits on Azure VMs, see [Azure subscription and service limits, quotas, and constraints](/documentation/articles/azure-subscription-service-limits).

The standard sizes consist of several series: A and D. Considerations for some of these sizes include:

*   D-series VMs are designed to run applications that demand higher compute power and temporary disk performance. D-series VMs provide faster processors, a higher memory-to-core ratio, and a solid-state drive (SSD) for the temporary disk. For details, see the announcement on the Azure blog, [New D-Series Virtual Machine Sizes](http://azure.microsoft.com/blog/2014/09/22/new-d-series-virtual-machine-sizes/).

The size of the virtual machine affects the pricing. The size also affects the processing, memory, and storage capacity of the virtual machine. Storage costs are calculated separately based on used pages in the storage account. For details, see [Virtual Machines Pricing Details](/home/features/virtual-machines/#price) and [Azure Storage Pricing](/home/features/storage/#price). For more details about storage for VMss, see [About disks and VHDs for virtual machines ](/documentation/articles/virtual-machines-disks-vhds).

The following considerations might help you decide on a size:


*   Some of the physical hosts in Azure data centers may not support larger virtual machine sizes, such as A5 - A11. As a result, you may see the error message **Failed to configure virtual machine <machine name>** or **Failed to create virtual machine <machine name>** when resizing an existing virtual machine to a new size; creating a new virtual machine in a virtual network created before April 16, 2013; or adding a new virtual machine to an existing cloud service. See  [Error: “Failed to configure virtual machine”](https://social.msdn.microsoft.com/Forums/9693f56c-fcd3-4d42-850e-5e3b56c7d6be/error-failed-to-configure-virtual-machine-with-a5-a6-or-a7-vm-size?forum=WAVirtualMachinesforWindows) on the support forum for workarounds for each deployment scenario.  


## Performance considerations

We have created the concept of the Azure Compute Unit (ACU) to provide a way of comparing compute (CPU) performance across Azure SKUs. This will help you easily identify which SKU is most likely to satisfy your performance needs.  ACU is currently standardized on a Small (Standard_A1) VM being 100 and all other SKUs then represent approximately how much faster that SKU can run a standard benchmark. 

>[AZURE.IMPORTANT] The ACU is only a guideline.  The results for your workload may vary. 

<br>

|SKU Family	|ACU/Core |
|---|---|
|[Standard_A0 (Extra Small)](#standard-tier-a-series)	|50 |
|[Standard_A1-4 (Small - Large)] (#standard-tier-a-series)	|100 |
|[Standard_A5-7](#standard-tier-a-series)	|100 |
|[D1-14](#standard-tier-d-series)	|160 |


ACUs marked with a * use Intel® Turbo technology to increase CPU frequency and provide a performance boost.  The amount of the boost can vary based on the VM size, workload, and other workloads running on the same host.



## Size tables

The following tables show the sizes and the capacities they provide.

>[AZURE.NOTE] Storage capacity is represented by using 1024^3 bytes as the unit of measurement for GB. This is sometimes referred to as gibibyte, or base 2 definition. When comparing sizes that use different base systems, remember that base 2 sizes may appear smaller than base 10 but for any specific size (such as 1 GB) a base 2 system provides more capacity than a base 10 system, because 1024^3 is greater than 1000^3.

<br>

## Standard tier: A-series

In the classic deployment model, some VM sizes are slightly different in Powershell and CLI.

* Standard_A0 is ExtraSmall 
* Standard_A1 is Small
* Standard_A2 is Medium
* Standard_A3 is Large
* Standard_A4 is ExtraLarge

<br>

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Max. IOPS (500 per disk)|
|---|---|---|---|---|---|---|
|Standard_A0\ExtraSmall |1|768 MB|1| Temporary = 20 GB |1|1x500|
|Standard_A1\Small|1|1.75 GB|1|Temporary = 70 GB |2|2x500|
|Standard_A2\Medium|2|3.5 GB|1|Temporary = 135 GB |4|4x500|
|Standard_A3\Large|4|7 GB|2|Temporary = 285 GB |8|8x500|
|Standard_A4\ExtraLarge|8|14 GB|4|Temporary = 605 GB |16|16x500|
|Standard_A5|2|14 GB|1|Temporary = 135 GB |4|4X500|
|Standard_A6|4|28 GB|2|Temporary = 285 GB |8|8x500|
|Standard_A7|8|56 GB|4|Temporary = 605 GB |16|16x500|

## Standard tier: D-series

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Max. IOPS (500 per disk)|
|---|---|---|---|---|---|---|
|Standard_D1 |1|3.5 GB|1|Temporary (SSD) =50 GB |2|2x500|
|Standard_D2 |2|7 GB|2|Temporary (SSD) =100 GB |4|4x500|
|Standard_D3 |4|14 GB|4|Temporary (SSD) =200 GB |8|8x500|
|Standard_D4 |8|28 GB|8|Temporary (SSD) =400 GB |16|16x500|
|Standard_D11 |2|14 GB|2|Temporary (SSD) =100 GB |4|4x500|
|Standard_D12 |4|28 GB|4|Temporary (SSD) =200 GB |8|8x500|
|Standard_D13 |8|56 GB|8|Temporary (SSD) =400 GB |16|16x500|
|Standard_D14 |16|112 GB|8|Temporary (SSD) =800 GB |32|32x500|

### See also

[Azure subscription and service limits, quotas, and constraints](/documentation/articles/azure-subscription-service-limits)



