
To see general limits on Azure VMs, see [Azure subscription and service limits, quotas, and constraints](/documentation/articles/azure-subscription-service-limits/).

The standard sizes consist of several series: A, D and DS . Considerations for some of these sizes include:

*   D-series VMs are designed to run applications that demand higher compute power and temporary disk performance. D-series VMs provide faster processors, a higher memory-to-core ratio, and a solid-state drive (SSD) for the temporary disk.

*   Dv2-series, a follow-on to the original D-series, features a more powerful CPU. The Dv2-series CPU is about 35% faster than the D-series CPU. It is based on the latest generation 2.4 GHz Intel Xeon® E5-2673 v3 (Haswell) processor, and with the Intel Turbo Boost Technology 2.0, can go up to 3.1 GHz. The Dv2-series has the same memory and disk configurations as the D-series.

*   DS-series and DSv2-series VMs can use Premium Storage, which provides high-performance, low-latency storage for I/O intensive workloads. These VMs use solid-state drives (SSDs) to host a virtual machine's disks and also provide a local SSD disk cache. Premium Storage is available in certain regions. For details, see [Premium Storage: High-performance storage for Azure virtual machine workloads](/documentation/articles/storage-premium-storage/).

	>[AZURE.NOTE] Currently, DS-series can not be created directly through the Portal. However, you can create a DS Virtual Machine through PowerShell. For details, see [Premium Storage: High-performance storage for Azure virtual machine workloads](/documentation/articles/storage-premium-storage/).

*   The A-series VMs can be deployed on a variety of hardware types and processors. The size is throttled, based upon the hardware, to offer consistent processor performance for the running instance, regardless of the hardware it is deployed on. To determine the physical hardware on which this size is deployed, query the virtual hardware from within the Virtual Machine.

*   The A0 size is over-subscribed on the physical hardware. For this specific size only, other customer deployments may impact the performance of your running workload. The relative performance is outlined below as the expected baseline, subject to an approximate variability of 15 percent.


The size of the virtual machine affects the pricing. The size also affects the processing, memory, and storage capacity of the virtual machine. Storage costs are calculated separately based on used pages in the storage account. For details, see [Virtual Machines Pricing Details](/home/features/virtual-machines/pricing/) and [Azure Storage Pricing](/home/features/storage/pricing/). 


The following considerations might help you decide on a size:


*	Dv2-series, D-series, and the DS counterparts  are ideal for applications that demand faster CPUs, better local disk performance, or have higher memory demands.  They offer a powerful combination for many enterprise-grade applications.

*   Some of the physical hosts in Azure data centers may not support larger virtual machine sizes, such as A5 - A7. As a result, you may see the error message **Failed to configure virtual machine <machine name>** or **Failed to create virtual machine <machine name>** when resizing an existing virtual machine to a new size; creating a new virtual machine in a virtual network created before April 16, 2013; or adding a new virtual machine to an existing cloud service. See  [Error: "Failed to configure virtual machine"](https://social.msdn.microsoft.com/Forums/9693f56c-fcd3-4d42-850e-5e3b56c7d6be/error-failed-to-configure-virtual-machine-with-a5-a6-or-a7-vm-size?forum=WAVirtualMachinesforWindows) on the support forum for workarounds for each deployment scenario.


## Performance considerations

We have created the concept of the Azure Compute Unit (ACU) to provide a way of comparing compute (CPU) performance across Azure SKUs. This will help you easily identify which SKU is most likely to satisfy your performance needs.  ACU is currently standardized on a Small (Standard_A1) VM being 100 and all other SKUs then represent approximately how much faster that SKU can run a standard benchmark. 

>[AZURE.IMPORTANT] The ACU is only a guideline.  The results for your workload may vary. 

<br>

|SKU Family	|ACU/Core |
|---|---|
|[Standard_A0](#a-series)	|50 |
|[Standard_A1-4](#a-series)	|100 |
|[Standard_A5-7](#a-series)	|100 |
|[D1-14](#d-series)	|160 |
|[D1-14v2](#dv2-series)	|210 - 250*|
|[DS1-14](#ds-series)	|160 |

ACUs marked with a * use Intel® Turbo technology to increase CPU frequency and provide a performance boost.  The amount of the boost can vary based on the VM size, workload, and other workloads running on the same host.

## Size tables

The following tables show the sizes and the capacities they provide.

* Storage capacity is represented by using 1024^3 bytes as the unit of measurement for GB. This is sometimes referred to as gibibyte, or base 2 definition. When comparing sizes that use different base systems, remember that base 2 sizes may appear smaller than base 10 but for any specific size (such as 1 GB) a base 2 system provides more capacity than a base 10 system, because 1024^3 is greater than 1000^3.

* Maximum network bandwidth is the maximum aggregated bandwidth allocated and assigned per VM type. The maximum bandwidth provides guidance for selecting the right VM type to ensure adequate network capacity is available. When moving between Low, Moderate, High and Very High, the throughput will increase accordingly. Actual network performance will depend on many factors including network and application loads, and application network settings.


##<a name="a-series"></a> A-series

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Max. IOPS (500 per disk)| Max network bandwidth |
|---|---|---|---|---|---|---|---|
|Standard_A0 |1|768 MB|1| Temporary = 20 GB |1|1x500| low |
|Standard_A1 |1|1.75 GB|1|Temporary = 70 GB |2|2x500| moderate |
|Standard_A2 |2|3.5 GB|1|Temporary = 135 GB |4|4x500| moderate |
|Standard_A3 |4|7 GB|2|Temporary = 285 GB |8|8x500| high |
|Standard_A4 |8|14 GB|4|Temporary = 605 GB |16|16x500| high |
|Standard_A5 |2|14 GB|1|Temporary = 135 GB |4|4X500| moderate |
|Standard_A6 |4|28 GB|2|Temporary = 285 GB |8|8x500| high |
|Standard_A7 |8|56 GB|4|Temporary = 605 GB |16|16x500| high |

##<a name="d-series"></a> D-series

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Max. IOPS (500 per disk)| Max network bandwidth |
|---|---|---|---|---|---|---|---|
|Standard_D1 |1|3.5 GB|1|Temporary (SSD) =50 GB |2|2x500| moderate |
|Standard_D2 |2|7 GB|2|Temporary (SSD) =100 GB |4|4x500| high |
|Standard_D3 |4|14 GB|4|Temporary (SSD) =200 GB |8|8x500| high |
|Standard_D4 |8|28 GB|8|Temporary (SSD) =400 GB |16|16x500| high |
|Standard_D11 |2|14 GB|2|Temporary (SSD) =100 GB |4|4x500| high |
|Standard_D12 |4|28 GB|4|Temporary (SSD) =200 GB |8|8x500| high |
|Standard_D13 |8|56 GB|8|Temporary (SSD) =400 GB |16|16x500| high |
|Standard_D14 |16|112 GB|8|Temporary (SSD) =800 GB |32|32x500| very high |

##<a name="dv2-series"></a> Dv2-series

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Max. IOPS (500 per disk)| Max network bandwidth |
|---|---|---|---|---|---|---|---|
|Standard_D1_v2 |1|3.5 GB|1|Temporary (SSD) =50 GB |2|2x500| moderate |
|Standard_D2_v2 |2|7 GB|2|Temporary (SSD) =100 GB |4|4x500| high |
|Standard_D3_v2 |4|14 GB|4|Temporary (SSD) =200 GB |8|8x500| high |
|Standard_D4_v2 |8|28 GB|8|Temporary (SSD) =400 GB |16|16x500| high |
|Standard_D5_v2 |16|56 GB|8|Temporary (SSD) =800 GB |32|32x500| extremely high |
|Standard_D11_v2 |2|14 GB|2|Temporary (SSD) =100 GB |4|4x500| high |
|Standard_D12_v2 |4|28 GB|4|Temporary (SSD) =200 GB |8|8x500| high |
|Standard_D13_v2 |8|56 GB|8|Temporary (SSD) =400 GB |16|16x500| high |
|Standard_D14_v2 |16|112 GB|8|Temporary (SSD) =800 GB |32|32x500| extremely high |
|Standard_D15_v2 |20|140 GB|10|Temporary (SSD) =1 TB |40|40x500| extremely high |

##<a name="ds-series"></a> DS-series*

|Size |CPU cores|Memory|NICs (Max)|Max. disk size|Max. data disks (1023 GB each)|Cache size (GB)|Max. disk IOPS &amp; bandwidth| Max network bandwidth |
|---|---|---|---|---|---|---|---|---|
|Standard_DS1 |1|3.5|1|Local SSD disk = 7 GB |2|43| 3,200  32 MB per second | moderate |
|Standard_DS2 |2|7|2|Local SSD disk = 14 GB |4|86| 6,400  64 MB per second | high |
|Standard_DS3 |4|14|4|Local SSD disk = 28 GB |8|172| 12,800  128 MB per second | high |
|Standard_DS4 |8|28|8|Local SSD disk = 56 GB |16|344| 25,600  256 MB per second | high |
|Standard_DS11 |2|14|2|Local SSD disk = 28 GB |4|72| 6,400  64 MB per second | high |
|Standard_DS12 |4|28|4|Local SSD disk = 56 GB |8|144| 12,800  128 MB per second | high |
|Standard_DS13 |8|56|8|Local SSD disk = 112 GB |16|288| 25,600  256 MB per second | high |
|Standard_DS14 |16|112|8|Local SSD disk = 224 GB |32|576| 51,200  512 MB per second | very high |

*The maximum input/output operations per second (IOPS) and throughput (bandwidth) possible with a DS series VM is affected by the size of the disk. For details, see [Premium Storage: High-performance storage for Azure virtual machine workloads](/documentation/articles/storage-premium-storage/).

## Notes: Standard A0 - A4 using CLI and PowerShell 


In the classic deployment model, some VM size names are slightly different in CLI and PowerShell:

* Standard_A0 is ExtraSmall 
* Standard_A1 is Small
* Standard_A2 is Medium
* Standard_A3 is Large
* Standard_A4 is ExtraLarge


## Next steps

- Learn about [azure subscription and service limits, quotas, and constraints](/documentation/articles/azure-subscription-service-limits/).



