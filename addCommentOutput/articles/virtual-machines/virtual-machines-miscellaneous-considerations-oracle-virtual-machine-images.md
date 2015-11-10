<properties
pageTitle="Considerations for using Oracle VM images | Windows Azure"
description="Learn about supported configurations and limitations for an Oracle VM on Windows Server in Azure before you deploy."
services="virtual-machines"
documentationCenter=""
manager=""
authors="bbenz"
tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="06/22/2015"
	wacn.date=""/>
<!-- deleted by customization

#Miscellaneous considerations for Oracle virtual machine images


[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.


This article covers considerations for Oracle virtual machines in Azure, which are based on Oracle software images provided by Microsoft, with Windows Server as the operating system.  

-  Oracle Database virtual machine images
-  Oracle WebLogic Server virtual machine images
-  Oracle JDK virtual machine images

##Oracle Database virtual machine images
-->
<!-- keep by customization: begin -->
#Miscellaneous Considerations for Oracle Virtual Machine Images
This article covers considerations for Oracle Virtual Machines on Azure, which are based on Oracle software images provided by Microsoft, with Windows Server as the operating system.  

-  Oracle Database Virtual Machine images
-  Oracle WebLogic Server Virtual Machine images
-  Oracle JDK Virtual Machine images

##Oracle Database Virtual Machine images
<!-- keep by customization: end -->
### Clustering (RAC) is not supported

Azure does not currently support Oracle <!-- deleted by customization Real Application Clusters (RAC) of the Oracle --> Database <!-- keep by customization: begin --> clustering <!-- keep by customization: end -->. Only standalone <!-- deleted by customization instances of --> Oracle Database <!-- keep by customization: begin --> instances <!-- keep by customization: end --> are possible. This is because Azure currently does not support virtual disk-sharing in a read/write manner among multiple <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> instances. <!-- deleted by customization Multicast --> UDP <!-- keep by customization: begin --> multicast <!-- keep by customization: end --> is also not supported.

### No static internal IP

Azure assigns each <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> Virtual Machine <!-- keep by customization: end --> an internal IP address. Unless the <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> is part of a virtual network, the IP address of the <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> is dynamic and <!-- deleted by customization might --><!-- keep by customization: begin --> may <!-- keep by customization: end --> change after the <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> restarts. This can cause issues because the Oracle Database expects the IP address to be static. To avoid the issue, consider adding the <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> to an Azure Virtual Network. See [Virtual <!-- deleted by customization Network](/documentation/services/networking/) --><!-- keep by customization: begin --> Network](http://www.windowsazure.cn/home/features/networking/) <!-- keep by customization: end --> and [Create a <!-- deleted by customization virtual network --><!-- keep by customization: begin --> Virtual Network <!-- keep by customization: end --> in Azure](/documentation/articles/create-virtual-network) for more information.

### Attached disk configuration options

<!-- deleted by customization
You can place data files on either the operating system disk of the virtual machine or on attached disks, also known as data disks. Attached disks might offer better performance and size flexibility than the operating system disk. The operating system disk might be preferable only for databases under 10 gigabytes (GB).

Attached disks rely on the Azure Blob storage service. Each disk is capable of a theoretical maximum of approximately 500 input/output operations per second (IOPS). The performance of attached disks might not be optimal initially, and IOPS performance might improve considerably after a “burn-in” period of approximately 60-90 minutes of continuous operation. If a disk subsequently remains idle, IOPS performance might diminish until another burn-in period of continuous operation. In short, the more active a disk, the more likely it is to approach optimal IOPS performance.

Although the simplest approach is to attach a single disk to the virtual machine and put database files on that disk, this approach is also the most limiting in terms of performance. Instead, you can often improve the effective IOPS performance if you use multiple attached disks, spread database data across them, and then use Oracle Automatic Storage Management (ASM). See [Oracle Automatic Storage overview](http://www.oracle.com/technetwork/database/index-100339.html) for more information. Although it is possible to use  striping of multiple disks at the operating system level, that approach is discouraged because it is not known to improve IOPS performance.
-->
<!-- keep by customization: begin -->
You can place data files on either the operating system (OS) disk of the VM or on attached disks, also known as data disks. Attached disks may offer better performance and size flexibility than the OS disk. The OS disk may be preferable only for databases under 10 GB.

Attached disks rely on the Azure Blob Storage service. Each disk is capable of a theoretical maximum of approximately 500 input/output operations per second (IOPS). The performance of attached disks may not be optimal initially, and IOPS performance may improve considerably after a “burn-in” period of approximately 60-90 minutes of continuous operation. If a disk subsequently remains idle, IOPS performance may diminish until another burn-in period of continuous operation. In short, the more active a disk, the more likely it is to approach optimal IOPS performance.

Although the simplest approach is to attach a single disk to the VM and put database files on that disk, this approach is also the most limiting in terms of performance. Instead, you can often improve the effective IOPS performance if you use multiple attached disks, spread database data across them, and then use Oracle Automatic Storage Management (ASM). See [Oracle Automatic Storage Overview](http://www.oracle.com/technetwork/database/index-100339.html) for more information. Although it is possible to use OS-level striping of multiple disks , that approach is discouraged because it is not known to improve IOPS performance.
<!-- keep by customization: end -->

Consider two different approaches for attaching multiple disks based on whether you want to prioritize the performance of read operations or write operations for your database:

- **Oracle ASM on its own** is likely to result in better write operation performance, but worse IOPS for read operations as compared to the approach using Windows Server 2012 storage pools. The following illustration logically depicts this arrangement.  
	![](./media/virtual-machines-miscellaneous-considerations-oracle-virtual-machine-images/image2.png)

- **Oracle ASM with Windows Server 2012 storage pools** is likely to result in better read operation IOPS performance if your database primarily performs read operations, or if you value the performance of read operations over write operations. An image based on the Windows Server 2012 operating system is required. See [Deploy <!-- deleted by customization storage spaces --><!-- keep by customization: begin --> Storage Spaces <!-- keep by customization: end --> on a <!-- deleted by customization stand-alone server](http://technet.microsoft.com/zh-cn/library/jj822938.aspx) --><!-- keep by customization: begin --> Stand-Alone Server](http://technet.microsoft.com/zh-cn/library/jj822938.aspx) <!-- keep by customization: end --> for more information about storage pools. In this arrangement, two equal subsets of attached disks are first “striped” together as physical disks in two storage pool volumes, and then the volumes are added to an ASM disk group. The following illustration logically depicts this arrangement.

	![](./media/virtual-machines-miscellaneous-considerations-oracle-virtual-machine-images/image3.png)  

<!-- deleted by customization
>[AZURE.IMPORTANT] Evaluate the trade-off between write performance and read performance on a case-by-case basis. Your actual results can vary when you use these approaches.

### High availability and disaster recovery considerations

When using Oracle Database in Azure virtual machines, you are responsible for implementing a high availability and disaster recovery solution to avoid any downtime. You are also responsible for backing up your own data and application.

High availability and disaster recovery for Oracle Database Enterprise Edition (without RAC) on Azure can be achieved using [Data Guard, Active Data Guard](http://www.oracle.com/technetwork/articles/oem/dataguardoverview-083155.html), or [Oracle Golden Gate](http://www.oracle.com/technetwork/middleware/goldengate), with two databases in two separate virtual machines. Both virtual machines should be in the same [cloud service](/documentation/articles/cloud-services-connect-virtual-machine) and the same [virtual network](/documentation/services/networking/) to ensure they can access each other over the private persistent IP address.  Additionally, we recommend to place the virtual machines in the same [availability set](/documentation/articles/manage-availability-virtual-machines) to allow Azure to place them into separate fault domains and upgrade domains. Note that only virtual machines in the same cloud service can participate in the same availability set. Each virtual machine must have at least 2 GB of memory and 5 GB of disk space.

With Oracle Data Guard, high availability can be achieved with a primary database in one virtual machine, a secondary (standby) database in another virtual machine, and one-way replication set up between them. The result is read access to the copy of the database. With Oracle GoldenGate, you can configure bi-directional replication between the two databases. To learn how to set up a high-availability solution for your databases using these tools, see [Active Data Guard](http://www.oracle.com/technetwork/database/features/availability/data-guard-documentation-152848.html) and [GoldenGate](http://docs.oracle.com/goldengate/1212/gg-winux/index.html) documentation at the Oracle website. If you need read-write access to the copy of the database, you can use [Oracle Active Data Guard](http://www.oracle.com/uk/products/database/options/active-data-guard/overview/index.html).

##Oracle WebLogic Server virtual machine images
-->
<!-- keep by customization: begin -->
>[AZURE.IMPORTANT] Evaluate the tradeoff between write performance and read performance on a case-by-case basis. Your actual results when using these approaches may vary.

### High Availability and Disaster Recovery Considerations

When using Oracle Database in Azure Virtual Machines, you are responsible for implementing a high availability and disaster recovery solution to avoid any downtime. You are also responsible for backing up your own data and application.

High availability and disaster recovery for Oracle Database Enterprise Edition (without RAC) on Azure can be achieved using [Data Guard, Active Data Guard](http://www.oracle.com/technetwork/articles/oem/dataguardoverview-083155.html), or [Oracle Golden Gate](http://www.oracle.com/technetwork/middleware/goldengate), with two databases in two separate Virtual Machines(VMs). Both Virtual Machines should be in the same [cloud service](/documentation/articles/cloud-services-connect-virtual-machine) and the same [virtual network](http://www.windowsazure.cn/home/features/networking/) to ensure they can access each other over the private persistent IP address.  Additionally, it is recommended to place the VMs in the same [availability set](/documentation/articles/manage-availability-virtual-machines) to allow Azure to place them into separate fault domains and upgrade domains. Note that only VMs in the same cloud service can participate in the same availability set. Each VM must have at least 2 GB of memory and 5 GB of disk space.

With Oracle Data Guard, high availability can be achieved with a primary database in one VM, a secondary (standby) database in another VM, and one-way replication set up between them. The result is read access to the copy of the database. With Oracle GoldenGate, you can configure bi-directional replication between the two databases. To learn how to setup a high availability solution for your databases using these tools, see [Active Data Guard](http://www.oracle.com/technetwork/database/features/availability/data-guard-documentation-152848.html) and [GoldenGate](http://docs.oracle.com/goldengate/1212/gg-winux/index.html) documentation at  Oracle web site. If you need read-write access to the copy of the database, you can use [Oracle Active Data Guard](http://www.oracle.com/uk/products/database/options/active-data-guard/overview/index.html).

##Oracle WebLogic Server Virtual Machine images
<!-- keep by customization: end -->

-  **Clustering is supported on Enterprise Edition only.** If you are using Microsoft-licensed images of WebLogic Server (specifically, those with Windows Server as the operating system), you are licensed to use WebLogic clustering only when using the Enterprise Edition of WebLogic Server. Do not use clustering with WebLogic Server Standard Edition.

-  **Connection timeouts:** If your application relies on connections to public endpoints of another Azure cloud service (for example, a database tier service), Azure <!-- deleted by customization might --><!-- keep by customization: begin --> may <!-- keep by customization: end --> close these open connections after 4 minutes of inactivity. This <!-- deleted by customization might --><!-- keep by customization: begin --> may <!-- keep by customization: end --> affect features and applications relying on connection pools, <!-- deleted by customization because --><!-- keep by customization: begin --> since <!-- keep by customization: end --> connections that are inactive for more than that limit <!-- deleted by customization might --><!-- keep by customization: begin --> may <!-- keep by customization: end --> no longer remain valid. If this affects your application, consider enabling "keep-alive" logic on your connection pools.

	Note that if an endpoint is *internal* to your Azure cloud service deployment (such as a standalone database <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> Virtual Machine <!-- keep by customization: end --> within the *same* cloud service as your WebLogic <!-- deleted by customization virtual machines) --><!-- keep by customization: begin --> Virtual Machines) <!-- keep by customization: end -->, then the connection is direct and does not rely on the Azure load balancer, and therefore is not subject to a connection timeout.

-  **UDP multicast is not supported.** Azure supports UDP unicasting, but neither multicasting nor broadcasting is supported. WebLogic Server is able to rely on <!-- deleted by customization Azure --><!-- keep by customization: begin --> Azure’s <!-- keep by customization: end --> UDP unicast capabilities. For best results relying on UDP unicast, <!-- deleted by customization we recommend --><!-- keep by customization: begin --> it is recommended <!-- keep by customization: end --> that the WebLogic cluster size be kept static, or <!-- deleted by customization be kept --> with no more than 10 managed servers included in the cluster.

-  **WebLogic Server expects public and private ports to be the same for T3 access (for example, when using Enterprise JavaBeans).** Consider a multi-tier scenario where a service layer (EJB) application is running on a WebLogic Server cluster consisting of two or more managed servers, in a cloud service named **SLWLS**. The client tier is in a different cloud service, running a simple Java program trying to call EJB in the service layer. <!-- deleted by customization Because --><!-- keep by customization: begin --> Since <!-- keep by customization: end --> it is necessary to load balance the service layer, a public load-balanced endpoint needs to be created for the Virtual Machines in the WebLogic Server cluster. If the private port <!-- deleted by customization that --> you specify for that endpoint is different from the public port (for example, 7006:7008), an error such as the following <!-- deleted by customization occurs --><!-- keep by customization: begin --> will occur <!-- keep by customization: end -->:

		[java] javax.naming.CommunicationException [Root exception is java.net.ConnectException: t3://example.chinacloudapp.cn:7006:

		Bootstrap to: example.chinacloudapp.cn/138.91.142.178:7006' over: 't3' got an error or timed out]

	This is because for any remote T3 access, WebLogic Server expects the load balancer port and the WebLogic managed server port to be the same. In the above case, the client is accessing port 7006 (the load balancer port) and the managed server is listening on 7008 (the private port). Note that this restriction is applicable only for T3 access, not HTTP.

	To avoid this issue, use one of the following workarounds:

	-  Use the same private and public port numbers for load balanced endpoints dedicated to T3 access.

	-  Include the following JVM parameter when starting WebLogic Server:

			-Dweblogic.rjvm.enableprotocolswitch=true

For related information, see KB article **860340.1** at <http://support.oracle.com>.

-  **Dynamic clustering and load balancing limitations.** Suppose you want to use a dynamic cluster in WebLogic Server and expose it through a single, public <!-- deleted by customization load-balanced --><!-- keep by customization: begin --> load balanced <!-- keep by customization: end --> endpoint in Azure. This can be done as long as you use a fixed port number for each of the managed servers (not dynamically assigned from a range) and do not start more managed servers than there are machines the <!-- deleted by customization administrator --><!-- keep by customization: begin --> admin <!-- keep by customization: end --> is tracking (that is, no more than one managed server per <!-- deleted by customization virtual machine) --><!-- keep by customization: begin --> Virtual Machine) <!-- keep by customization: end -->. If your configuration results in more WebLogic servers being started than there are <!-- deleted by customization virtual machines --><!-- keep by customization: begin --> VMs <!-- keep by customization: end --> (that is, where multiple WebLogic Server instances will share the same <!-- deleted by customization virtual machine) --><!-- keep by customization: begin --> VM) <!-- keep by customization: end -->, then it will not be possible for more than one of those <!-- deleted by customization instances of --> WebLogic Server <!-- keep by customization: begin --> instances <!-- keep by customization: end --> servers to bind to a given port number – the others on that <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end --> will fail.

	On the other hand, if you configure the admin server to automatically assign unique port numbers to its managed servers, then load balancing <!-- deleted by customization is --><!-- keep by customization: begin --> will <!-- keep by customization: end --> not <!-- keep by customization: begin --> be <!-- keep by customization: end --> possible because Azure does not support mapping from a single public port to multiple private ports, as would be required for this configuration.

<!-- deleted by customization
-  **Multiple instances of Weblogic Server on a virtual machine.** Depending on your deployment’s requirements, you might consider the option of running multiple instances of WebLogic Server on the same virtual machine, if the virtual machine is large enough. For example, on a medium size virtual machine, which contains two cores, you could choose to run two instances of WebLogic Server. Note however that we still recommend that you avoid introducing single points of failure into your architecture, which would be the case if you used just one virtual machine that is running multiple instances of WebLogic Server. Using at least two virtual machines could be a better approach, and each of those virtual machines could then run multiple instances of WebLogic Server. Each of these instances of WebLogic Server could still be part of the same cluster. Note, however, it is currently not possible to use Azure to load-balance endpoints that are exposed by such WebLogic Server deployments within the same virtual machine, because Azure load balancer requires the load-balanced servers to be distributed among unique virtual machines.

##Oracle JDK virtual machine images

-  **JDK 6 and 7 latest updates.** While we recommend to use the latest public <!-- deleted by customization, --> supported version of Java (currently Java 8), Azure also makes JDK 6 and 7 images available. This is intended for legacy applications that are not yet ready to be upgraded to JDK 8. While updates to previous JDKimages might no longer be available to the general public, given the Microsoft partnership with Oracle, the JDK 6 and 7 images provided by Azure are intended to contain a more recent non-public update that is normally offered by Oracle to only a select group of Oracle’s supported customers. New versions of the JDK images will be made available over time with updated releases of JDK 6 and 7.

	Note that the JDK available in this JDK 6 and 7 images, and the virtual machines and images derived from them, can only be used within Azure.

-  **64-bit JDK.** The Oracle WebLogic Server virtual machine images and the Oracle JDK virtual machine images provided by Azure contain the 64-bit versions of both Windows Server and the JDK.

##Additional resources
[Oracle virtual machine images for Azure](/documentation/articles/virtual-machines-oracle-list-oracle-virtual-machine-images)

-->
<!-- keep by customization: begin -->
-  **Multiple WebLogic instances on a single VM.** Depending on your deployment’s requirements, you may consider the option of running multiple instances of WebLogic Server on the same Virtual Machine, if the VM is large enough. For example, on a Medium size VM, which contains 2 cores, you could choose to run two instances of WebLogic Server. Note however that it is still recommended that you avoid introducing single points of failure into your architecture, as would be the case if you used just one VM that is running multiple instances of WebLogic Server. Using at least two VMs could be a better approach, and each of those VMs could then run multiple WebLogic Server instances. Each of these WebLogic Server instances could still be part of the same cluster. Note, however, it is currently not possible to use Azure to load balance endpoints exposed by such WebLogic Server deployments within the same VM, as Azure load balancer requires the load balanced servers to be distributed among unique VMs.

##Oracle JDK Virtual Machine images

-  **JDK 6 and 7 latest updates.** While it is recommended to use the latest public <!-- deleted by customization, --> supported version of Java (currently Java 8), Azure also makes JDK 6 and 7 images available. This is intended for legacy applications that are not yet ready to be upgraded to JDK 8. While updates to previous JDKsmay no longer be available to the general public, given Microsoft’s partnership with Oracle, the JDK 6 and 7 images provided by Azure are intended to contain a more recent non-public update that is normally offered by Oracle to only a select group of Oracle’s supported customers. New versions of the JDK images will be made available over time with updated releases of JDK 6 and 7.

	Note that the JDK available in this JDK 6 and 7 images, and the Virtual Machines and images derived from them, may only be used within Azure.

-  **64-bit JDK.** The Oracle WebLogic Server Virtual Machine images and the Oracle JDK Virtual Machine images provided by Azure contain the 64-bit versions of both Windows Server and the JDK.

##Additional Resources
[Oracle Virtual Machine images for Azure](/documentation/articles/virtual-machines-oracle-list-oracle-virtual-machine-images)
<!-- keep by customization: end -->