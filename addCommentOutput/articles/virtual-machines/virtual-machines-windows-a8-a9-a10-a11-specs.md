<!-- not suitable for Mooncake -->

<properties
 pageTitle="About A8, A9, A10, A11 VM sizes and Windows | Azure"
 description="Get background information and considerations for using the Azure A8, A9, A10, and A11 compute-intensive sizes for Windows VMs and cloud services"
 services="virtual-machines-windows, cloud-services"
 documentationCenter=""
 authors="dlepow"
 manager="timlt"
 editor=""
 tags="azure-resource-manager,azure-service-management"/>
<tags
ms.service="virtual-machines-windows"
 ms.devlang="na"
 ms.topic="article"
 ms.tgt_pltfrm="vm-windows"
 ms.workload="infrastructure-services"
 ms.date="08/04/2016"
 wacn.date=""
 ms.author="danlep"/>

# About the A8, A9, A10, and A11 compute-intensive instances

Here is background information and some considerations for using the Azure A8, A9, A10, and A11 instances, also known as *compute-intensive* instances. This article focuses on using these instances for Windows VMs. This article is also available for [Linux VMs](/documentation/articles/virtual-machines-linux-a8-a9-a10-a11-specs/).

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-both-include.md)]

[AZURE.INCLUDE [virtual-machines-common-a8-a9-a10-a11-specs](../../includes/virtual-machines-common-a8-a9-a10-a11-specs.md)]

## Access to the RDMA network

Within a single cloud service, availability set, or Azure Batch pool, the A8 and A9 instances can access the RDMA network in Azure to run Windows MPI applications that use the Microsoft Network Direct interface to communicate between instances.

Following are prerequisites for MPI applications to access the RDMA network in Windows virtual machines, cloud services, and Azure Batch pools of the A8 or A9 instances. For typical deployment scenarios, see [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/) and [Use multi-instance tasks to run Message Passing Interface (MPI) applications in Azure Batch](/documentation/articles/batch-mpi/).


Prerequisite | Virtual machines | Cloud services or Batch pool 
---------- | ------------ | ------------- 
Operating system | Windows Server 2012 R2 or Windows Server 2012 | Windows Server 2012 R2, Windows Server 2012, or Windows Server 2008 R2 Guest OS family 
MPI | MS-MPI 2012 R2 or later, or Intel MPI Library 5 | MS-MPI 2012 R2 or later, or Intel MPI Library 5 


>[AZURE.NOTE]On size A8 and A9 virtual machines, the HpcVmDrivers extension must be added to the VMs to install Windows network device drivers that are needed for RDMA connectivity. Depending on your deployment method, the HpcVmDrivers extension might be added to a size A8 or A9 VM automatically, or you might need to add it yourself. To add the extension yourself, see [Manage VM extensions](/documentation/articles/virtual-machines-windows-classic-manage-extensions/).

## Considerations for HPC Pack and Windows

HPC Pack is not required for you to use the A8, A9, A10, and A11 instances with Windows Server, but it can be a useful tool to run Windows-based MPI applications that access the RDMA network in Azure. HPC Pack 2012 R2 and later versions include a runtime environment for the Microsoft implementation of the Message Passing Interface (MS-MPI) for Windows that can use the Azure RDMA network when deployed on A8 and A9 instances.

For more information and checklists to use the compute-intensive instances with HPC Pack on Windows Server, see [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/).




## Next steps

* For details about availability and pricing of the A8, A9, A10, and A11 instances, see [Virtual Machines pricing](/pricing/details/virtual-machines/) and [Cloud Services pricing](/pricing/details/cloud-services/).

* For storage capacities and disk details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-linux-sizes/).

* To get started deploying and using A8 and A9 instances with HPC Pack on Windows, see [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/).

* For information about using A8 and A9 instances to run MPI applications with Azure Batch, see [Use multi-instance tasks to run Message Passing Interface (MPI) applications in Azure Batch](/documentation/articles/batch-mpi/).
