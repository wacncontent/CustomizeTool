<properties
 pageTitle="Linux compute VMs in an HPC Pack cluster | Microsoft Azure"
 description="Learn how to create and use an HPC Pack cluster in Azure for Linux high performance computing (HPC) workloads."
 services="virtual-machines-linux"
 documentationCenter=""
 authors="dlepow"
 manager="timlt"
 editor=""
 tags="azure-service-management,azure-resource-manager,hpc-pack"/>
<tags
	ms.service="virtual-machines-linux"
	ms.date="03/21/2016"
	wacn.date=""/>

# Get started with Linux compute nodes in an HPC Pack cluster in Azure

Set up a Microsoft HPC Pack cluster in Azure which contains a head node running Windows Server and several compute nodes running a supported Linux distribution. Explore options to move data among the Linux nodes and the Windows head node of the cluster. Learn how to submit Linux HPC jobs to the cluster.

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)].


At a high level the following diagram shows the HPC Pack cluster you'll create and work with.

![HPC Pack cluster with Linux nodes][scenario]

>[AZURE.TIP]If you are interested in working with Linux nodes in an on-premises HPC Pack cluster, see the [TechNet guidance](https://technet.microsoft.com/en-us/library/mt595803.aspx).

## Deploy an HPC Pack cluster with Linux compute nodes

Following are two recommended ways to create an HPC Pack cluster in Azure with Linux compute nodes:

* **Azure Resource Manager template** - Use a template from the Azure Marketplace, or a template in the commmunity gallery, to automate creation of the cluster in the Resource Manager deployment model. For example, the [HPC Pack cluster for Linux workloads](https://azure.microsoft.com/marketplace/partners/microsofthpc/newclusterlinuxcn/) template in the Azure Marketplace creates a complete HPC Pack cluster, including the Azure virtual network, a head node with local SQL databases, Active Directory Domain forest (with the head node set up as domain controller), and a number of compute nodes running a supported Linux distribution.

* **PowerShell script** - Use the [Microsoft HPC Pack IaaS deployment script](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-powershell-script/) (**New-HpcIaaSCluster.ps1**) to automate the cluster deployment in the classic deployment model. This Azure PowerShell script uses an HPC Pack VM image in the Azure Marketplace for fast deployment and provides a comprehensive set of configuration parameters to make the deployment easy and flexible. The script deploys the Azure virtual network, storage accounts, cloud services, domain controller, optional separate SQL Server database server, cluster head node, compute nodes, broker nodes, Azure PaaS ("burst") nodes, and Linux compute nodes.

For an overview of HPC Pack cluster deployment options, see the [Getting started guide for HPC Pack 2012 R2 and HPC Pack 2012](https://technet.microsoft.com/en-us/library/jj884144.aspx) and [Options to create and manage a high peformance computing (HPC) cluster in Azure with Microsoft HPC Pack](/documentation/articles/virtual-machines-linux-hpcpack-cluster-options/).

### Prerequisites

* **Azure subscription** - You can use a subscription in either the Azure Global or Azure China service. If you don't have an account, you can create a [free account](/pricing/1rmb-trial/) in just a couple of minutes.

* **Cores quota** - You might need to increase the quota of cores, especially if you choose to deploy several cluster nodes with multicore VM sizes. To increase a quota, [open an online customer support request](https://azure.microsoft.com/blog/2014/06/04/azure-limits-quotas-increase-requests/) at no charge.

* **Linux distributions** - Currently HPC Pack supports the following Linux distributions for compute nodes: Ubuntu Server 14.04, CentOS 6.6 or 7.0, Red Hat Enterprise Linux 6.7 or 7.2, and SUSE Linux Enterprise Server 12. You can use Marketplace versions of these distributions where available, or supply your own.

    >[AZURE.TIP]To use the Azure RDMA network with size A8 and A9 compute node VMs, specify the SUSE Linux Enterprise Server 12 - Optimized for High Performance Compute image from the Marketplace. You'll need to install and configure a supported MPI library on the nodes after cluster deployment according to your application needs. For an example, see [Run OpenFOAM with Microsoft HPC Pack on a Linux RDMA cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-openfoam/).

Additional prerequisites if you deploy the cluster by using the HPC Pack IaaS deployment script:

* **Client computer** - You'll need a Windows-based client computer to run the cluster deployment script.

* **Azure PowerShell** - [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) (version 0.8.10 or later) on your client computer.

* **HPC Pack IaaS deployment script** - Download and unpack the latest version of the script from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=44949). You can check the version of the script by running `New-HPCIaaSCluster.ps1 -Version`. This article is based on version 4.4.0 or later of the script.

### Deployment scenario 1. Use a Marketplace template

1. Go to the [HPC Pack cluster for Linux workloads](https://azure.microsoft.com/marketplace/partners/microsofthpc/newclusterlinuxcn/) template in the Azure Marketplace, and click **Deploy**.

2. In the Azure portal, review the information and then click **Create**.

    ![Portal creation][portal]

3. On the **Basics** blade, enter a name for the cluster, which will also name the head node VM. You can choose an existing resource group or create a new group for the deployment.

4. On the **Head node settings** blade, for a first deployment, you can generally accept the default settings. 

    >[AZURE.NOTE]The **Post-configuration script URL** is an optional setting to specify a publicly available Windows PowerShell script that you want to run on the head node VM after it is running. 
    
5. On the **Compute node settings** blade, select a naming pattern for the nodes, the number and size of the nodes, and the image of the Linux distribution to deploy.

6. On the **Infrastructure settings** blade, enter names for the virtual network and Active Directory domain for the cluster, domain and VM administrator credentials, and a naming pattern for the storage accounts needed for the cluster.

    >[AZURE.NOTE]HPC Pack uses the Active Directory domain to authenticate cluster users. 

7. After the validation tests run and you are ready to deploy, click **Create**.


### Deployment scenario 2. Use the IaaS deployment script

The HPC Pack IaaS deployment script uses an XML configuration file as input which describes the infrastructure of the HPC cluster. The following sample configuration file deploys a small cluster consisting of a head node and two size A7 CentOS 7 Linux compute nodes. Modify the file as needed for your environment and desired cluster configuration. For more information about the elements in the configuration file, see the Manual.rtf file in the script folder and [Create an HPC cluster with the HPC Pack IaaS deployment script](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-powershell-script/).

```
<?xml version="1.0" encoding="utf-8" ?>
<IaaSClusterConfig>
  <Subscription>
    <SubscriptionName>Subscription-1</SubscriptionName>
    <StorageAccount>allvhdsje</StorageAccount>
  </Subscription>
  <Location>Japan East</Location>  
  <VNet>
    <VNetName>centos7rdmavnetje</VNetName>
    <SubnetName>CentOS7RDMACluster</SubnetName>
  </VNet>
  <Domain>
    <DCOption>HeadNodeAsDC</DCOption>
    <DomainFQDN>hpc.local</DomainFQDN>
  </Domain>
  <Database>
    <DBOption>LocalDB</DBOption>
  </Database>
  <HeadNode>
    <VMName>CentOS7RDMA-HN</VMName>
    <ServiceName>centos7rdma-je</ServiceName>
  <VMSize>A4</VMSize>
  <EnableRESTAPI />
  <EnableWebPortal />
  </HeadNode>
  <LinuxComputeNodes>
    <VMNamePattern>CentOS7RDMA-LN%1%</VMNamePattern>
    <ServiceName>centos7rdma-je</ServiceName>
    <VMSize>A7</VMSize>
    <NodeCount>2</NodeCount>
    <ImageName>5112500ae3b842c8b9c604889f8753c3__OpenLogic-CentOS-70-20150325</ImageName>
  </LinuxComputeNodes>
</IaaSClusterConfig>
```

**To run the HPC Pack IaaS deployment script**

1. Open the PowerShell console on the client computer as an administrator.

2. Change directory to the script folder (E:\IaaSClusterScript in this example).

    ```
    cd E:\IaaSClusterScript
    ```

3. Run the following command to deploy the HPC Pack cluster. This example assumes that the configuration file is located in E:\HPCDemoConfig.xml.

    ```
    .\New-HpcIaaSCluster.ps1 -ConfigFile E:\HPCDemoConfig.xml -AdminUserName MyAdminName
    ```

    The script generates a log file automatically since  the **-LogFile** parameter isn't specified. The logs aren't written in real time, but are collected at the end of the validation and the deployment. If the PowerShell process is stopped while the script is running, some logs will be lost.

    a. Because the **AdminPassword** is not specified in the above command, you'll be prompted to enter the password for user *MyAdminName*.

    b. The script then starts to validate the configuration file. It takes from tens of seconds to several minutes depending on the network connection.

    ![Validation][validate]

    c. After validations pass, the script lists the resources which will be created for the HPC cluster. Enter *Y* to continue.

    ![Resources][resources]

    d. The script starts to deploy the HPC Pack cluster and completes the configuration without further manual steps. This can take several minutes.

    ![Deploy][deploy]

## Connect to the head node

After the deployment finishes successfully, [connect by Remote Desktop to the head node](/documentation/articles/virtual-machines-windows-connect-logon/) using the domain credentials you provided when you deployed the cluster (for example, *hpc\clusteradmin*). 

On the head node, start HPC Cluster Manager to check the status of the HPC Pack cluster. You can manage and monitor Linux compute nodes the same way you work with Windows compute nodes. For example, you'll see the Linux nodes listed in **Resource Management** (these nodes are deployed with the **LinuxNode** template).

![Node Management][management]

You'll also see the Linux nodes in the **Heat Map** view.

![Heat map][heatmap]

## How to move data in a cluster with Linux nodes

You have several choices to move data among Linux nodes and the Windows head node of the cluster. Here are three common methods.

* **Azure File** - Exposes a managed SMB file share to store data files in Azure storage. Both Windows nodes and the Linux nodes can mount an Azure File share as a drive or folder at the same time even if they are deployed in different virtual networks.

* **Head node SMB share** - Mounts a standard Windows shared folder of the head node on Linux nodes.

* **Head node NFS server**  - Provides a file-sharing solution for a mixed Windows and Linux environment.

### Azure File storage

The [Azure File](/home/features/storage/files/) service exposes file shares using the standard SMB 2.1 protocol. Azure VMs and cloud services can share file data across application components via mounted shares, and on-premises applications can access file data in a share through the File storage API. 

For detailed steps to create an Azure File share and mount it on the head node, see [Get started with Azure File storage on Windows](/documentation/articles/storage-dotnet-how-to-use-files/). To mount the Azure File share on the Linux nodes, see [How to use Azure File Storage with Linux](/documentation/articles/storage-how-to-use-files-linux/). To set up persisting connections, see [Persisting connections to Microsoft Azure Files](http://blogs.msdn.com/b/windowsazurestorage/archive/2014/05/27/persisting-connections-to-microsoft-azure-files.aspx).

In this example, we create an Azure File share named rdma on our storage account allvhdsje. To mount the share on the head node, open a Command Prompt and enter the following commands:

```
> cmdkey /add:allvhdsje.file.core.windows.net /user:allvhdsje /pass:<storageaccountkey>
> net use Z: \\allvhdje.file.core.windows.net\rdma /persistent:yes
```

In this example, allvhdsje is the storage account name, storageaccountkey is the storage account key, and rdma is the Azure File share name. The Azure File share will be mounted onto Z: on your head node.

To mount the Azure File share on Linux nodes, run a **clusrun** command on the head node. **[Clusrun](https://technet.microsoft.com/en-us/library/cc947685.aspx)** is a useful HPC Pack tool to carry out administrative tasks on multiple nodes. (See also [CLusrun for Linux nodes](#CLusrun-for-Linux-nodes) in this article.)

Open a Windows PowerShell window and enter the following commands.

```
PS > clusrun /nodegroup:LinuxNodes mkdir -p /rdma

PS > clusrun /nodegroup:LinuxNodes mount -t cifs //allvhdsje.file.core.windows.net/rdma /rdma -o vers=2.1`,username=allvhdsje`,password=<storageaccountkey>'`,dir_mode=0777`,file_mode=0777
```

The first command creates a folder named /rdma on all nodes in the LinuxNodes group. The second command mounts the Azure File share allvhdsjw.file.core.windows.net/rdma onto the /rdma folder with dir and file mode bits set to 777. In the second command, allvhdsje is your storage account name  and storageaccountkey is your storage account key.

>[AZURE.NOTE]The "\`" symbol in the second command is an escape symbol for PowerShell. "\`," means that the "," (comma character) is a part of the command.

### Head node share

Alternatively, mount a shared folder of the head node on Linux nodes. This is the simplest way to share files, but the head node and all Linux nodes have to be deployed in the same virtual network. Here are the steps.

1. Create a folder on the head node and share it to Everyone with Read/Write permissions. For example, share D:\OpenFOAM on the head node as \\CentOS7RDMA-HN\OpenFOAM. Here CentOS7RDMA-HN is the hostname of the head node.

    ![File share permissions][fileshareperms]

    ![File sharing][filesharing]

2. Open a Windows PowerShell window and run the following commands to mount the shared folder.

```
PS > clusrun /nodegroup:LinuxNodes mkdir -p /openfoam

PS > clusrun /nodegroup:LinuxNodes mount -t cifs //CentOS7RDMA-HN/OpenFOAM /openfoam -o vers=2.1`,username=<username>`,password='<password>'`,dir_mode=0777`,file_mode=0777
```

The first command creates a folder named /openfoam on all nodes in the LinuxNodes group. The second command mounts the shared folder //CentOS7RDMA-HN/OpenFOAM onto the folder with dir and file mode bits set to 777. The username and password in the command should be the username and password of a cluster user on the head node. (See [Add or remove cluster users](https://technet.microsoft.com/en-us/library/ff919330.aspx).)

>[AZURE.NOTE]The "\`" symbol in the second command is an escape symbol for PowerShell. "\`," means that the "," (comma character) is a part of the command.


### NFS server

The NFS service enables you to share and migrate files between computers running the Windows Server 2012 operating system using the SMB protocol and Linux-based computers using the NFS protocol. The NFS server and all other nodes have to be deployed in the same virtual network. It provides better compatibility with Linux nodes compared with an SMB share; for example, it supports file links.

1. To install and set up an NFS server, follow the steps in [Server for Network File System First Share End-to-End](http://blogs.technet.com/b/filecab/archive/2012/10/08/server-for-network-file-system-first-share-end-to-end.aspx).

    For example, create an NFS share named nfs with the following properties.

    ![NFS authorization][nfsauth]

    ![NFS share permissions][nfsshare]

    ![NFS NTFS permissions][nfsperm]

    ![NFS management properties][nfsmanage]

2. Open a Windows PowerShell window and run the following commands to mount the NFS share.

  ```
  PS > clusrun /nodegroup:LinuxNodes mkdir -p /nfsshare
  PS > clusrun /nodegroup:LinuxNodes mount CentOS7RDMA-HN:/nfs /nfsshared
  ```

  The first command creates a folder named /nfsshared on all nodes in the LinuxNodes group. The second command mounts the NFS share CentOS7RDMA-HN:/nfs onto the folder. Here CentOS7RDMA-HN:/nfs is the remote path of your NFS share.

## How to submit jobs
There are several ways to submit jobs to the HPC Pack cluster:

* HPC Cluster Manager or HPC Job Manager GUI

* HPC web portal

* REST API

Job submission to the cluster in Azure via HPC Pack GUI tools and the HPC web portal are the same as for Windows compute nodes. See [HPC Pack Job Manager](https://technet.microsoft.com/en-us/library/ff919691.aspx) and [How to submit jobs from an on-premises client computer](/documentation/articles/virtual-machines-windows-hpcpack-cluster-submit-jobs/).

To submit jobs via the REST API, refer to [Creating and Submitting Jobs by Using the REST API in Microsoft HPC Pack](http://social.technet.microsoft.com/wiki/contents/articles/7737.creating-and-submitting-jobs-by-using-the-rest-api-in-microsoft-hpc-pack-windows-hpc-server.aspx). Also refer to the Python sample in the [HPC Pack SDK](https://www.microsoft.com/download/details.aspx?id=47756) to submit jobs from a Linux client.

## Clusrun for Linux nodes

The HPC Pack **clusrun** tool can be used to execute commands on Linux nodes either through a Command Prompt or HPC Cluster Manager. Following are some basic examples.

* Show current user names on all nodes in the cluster.

    ```
    > clusrun whoami
    ```

* Install the **gdb** debugger tool with **yum** on all nodes in the linuxnodes group and then restart the nodes after 10 minutes.

    ```
    > clusrun /nodegroup:linuxnodes yum install gdb -y; shutdown -r 10
    ```

* Create a shell script displaying each number 1 through 10 for one second on each Linux node in the cluster, run it, and show output from the nodes immediately.

    ```
    > clusrun /interleaved /nodegroup:linuxnodes echo \"for i in {1..10}; do echo \\\"\$i\\\"; sleep 1; done\" ^> script.sh; chmod +x script.sh; ./script.sh
    ```

>[AZURE.NOTE] You might need to use certain escape characters in **clusrun** commands. As shown in this example, use ^ in a Command Prompt to escape the ">" symbol.

## Next steps

* Try scaling up the cluster to a larger number of nodes, or try running a Linux workload on the cluster. For an example, see [Run NAMD with Microsoft HPC Pack on Linux compute nodes in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-namd/).

* Try a cluster with size [A8 or A9](/documentation/articles/virtual-machines-windows-a8-a9-a10-a11-specs/) compute nodes to run MPI workloads. For an example, see [Run OpenFOAM with Microsoft HPC Pack on a Linux RDMA cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-openfoam/).

<!--Image references-->
[scenario]: ./media/virtual-machines-linux-classic-hpcpack-cluster/scenario.png
[portal]: ./media/virtual-machines-linux-classic-hpcpack-cluster/portal.png
[validate]: ./media/virtual-machines-linux-classic-hpcpack-cluster/validate.png
[resources]: ./media/virtual-machines-linux-classic-hpcpack-cluster/resources.png
[deploy]: ./media/virtual-machines-linux-classic-hpcpack-cluster/deploy.png
[management]: ./media/virtual-machines-linux-classic-hpcpack-cluster/management.png
[heatmap]: ./media/virtual-machines-linux-classic-hpcpack-cluster/heatmap.png
[fileshareperms]: ./media/virtual-machines-linux-classic-hpcpack-cluster/fileshare1.png
[filesharing]: ./media/virtual-machines-linux-classic-hpcpack-cluster/fileshare2.png
[nfsauth]: ./media/virtual-machines-linux-classic-hpcpack-cluster/nfsauth.png
[nfsshare]: ./media/virtual-machines-linux-classic-hpcpack-cluster/nfsshare.png
[nfsperm]: ./media/virtual-machines-linux-classic-hpcpack-cluster/nfsperm.png
[nfsmanage]: ./media/virtual-machines-linux-classic-hpcpack-cluster/nfsmanage.png
