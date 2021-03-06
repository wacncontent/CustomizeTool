<properties
	pageTitle="Set up protection between an on-premises VMM site and Azure"
	description="Azure Site Recovery coordinates the replication, failover and recovery of Hyper-V virtual machines located in on-premises VMM clouds to Azure."
	services="site-recovery"
	documentationCenter=""
	authors="rayne-wiselman"
	manager="jwhit"
	editor="tysonn"/>

<tags
	ms.service="site-recovery"
	ms.date="11/18/2015"
	wacn.date=""/>

#  Set up protection between an on-premises VMM site and Azure

## Overview

Azure Site Recovery contributes to your business continuity and disaster recovery (BCDR) strategy by orchestrating replication, failover and recovery of virtual machines in a number of deployment scenarios. For a full list of deployment scenarios see  [Azure Site Recovery overview](/documentation/articles/site-recovery-overview).

This scenario guide describes how to deploy Site Recovery to orchestrate and automate protection for workloads running on virtual machines on Hyper-V host servers that are located in VMM private clouds. In this scenario virtual machines are replicated from a primary VMM site to Azure using Hyper-V Replica.

The guide includes prerequisites for the scenario and shows you how to set up a Site Recovery vault, get the Azure Site Recovery Provider installed on the source VMM server, register the server in the vault, add an Azure storage account, install the Azure Recovery Services agent on Hyper-V host servers, configure protection settings for VMM clouds that will be applied to all protected virtual machines, and then enable protection for those virtual machines. Finish up by testing the failover to make sure everything's working as expected.

If you run into problems setting up this scenario post your questions on the [Azure Recovery Services Forum](https://social.msdn.microsoft.com/forums/azure/zh-cn/home?forum=hypervrecovmgr).

## Before you start

Make sure you have these prerequisites in place:
### Azure prerequisites

- You'll need a [Windows Azure](http://www.windowsazure.cn) account. If you don't have one, start with a [1rmb trial](http://www.windowsazure.cn/pricing/1rmb-trial/). In addition you can read about [Azure Site Recovery Manager pricing](/home/features/site-recovery/#home_rec_pri).
- You'll need an Azure storage account to store data replicated to Azure. The account needs geo-replication enabled. It should be in the same region as the Azure Site Recovery service, and be associated with the same subscription. To learn more about setting up Azure storage, see [Introduction to Azure Storage](/documentation/articles/storage-introduction).
- You'll need to make sure that virtual machines you want to protect comply with Azure requirements. See [Virtual machine support](https://msdn.microsoft.com/zh-CN/library/azure/dn469078.aspx#BKMK_E2A) for details.

### VMM prerequisites
- You'll need  VMM server running on System Center 2012 R2.
- Any VMM server containing virtual machines you want to protect must be running the Azure Site Recovery Provider. This is installed during the Azure Site Recovery deployment.
- You'll need at least one cloud on the VMM server you want to protect. The cloud should contain:
	- One or more VMM host groups.
	- One or more Hyper-V host servers or clusters in each host group .
	- One or more virtual machines on the source Hyper-V server. The virtual machines should be generation 1.
- Learn more about setting up VMM clouds:
	- Read more about private VMM clouds in [What's New in Private Cloud with System Center 2012 R2 VMM](https://channel9.msdn.com/Events/TechEd/NorthAmerica/2013/MDC-B357) and in [VMM 2012 and the clouds](http://www.server-log.com/blog/2011/8/26/vmm-2012-and-the-clouds.html).
- Learn about [Configuring the VMM cloud fabric](https://msdn.microsoft.com/zh-cn/library/azure/dn469075.aspx#BKMK_Fabric)
	- After your cloud fabric elements are in place learn about creating private clouds in  [Creating a private cloud in VMM](https://technet.microsoft.com/zh-cn/library/jj860425.aspx) and [Walkthrough: Creating private clouds with System Center 2012 SP1 VMM](http://blogs.technet.com/b/keithmayer/archive/2013/04/18/walkthrough-creating-private-clouds-with-system-center-2012-sp1-virtual-machine-manager-build-your-private-cloud-in-a-month.aspx).

### Hyper-V prerequisites

- The host Hyper-V servers must be running at least Windows Server 2012 R2 with Hyper-V role and have the latest updates installed.
- If you're running Hyper-V in a cluster note that cluster broker isn't created automatically if you have a static IP address-based cluster. You'll need to configure the cluster broker manually. For instructions see [Configure Hyper-V Replica Broker](http://social.technet.microsoft.com/wiki/contents/articles/18792.configure-replica-broker-role-cluster-to-cluster-replication.aspx).
- Any Hyper-V host server or cluster for which you want to manage protection must be included in a VMM cloud.

The picture below shows the different communication channels and ports used by Azure Site Recovery for orchestration and replication

![E2A Topology](./media/site-recovery-vmm-to-azure/E2ATopology.png)

### Network mapping prerequisites
When you protect virtual machines in Azure network mapping maps between VM networks on the source VMM server and target Azure networks to enable the following:

- All machines which failover on the same network can connect to each other, irrespective of which recovery plan they are in.
- If a network gateway is setup on the target Azure network, virtual machines can connect to other on-premises virtual machines.
- If you don't configure network mapping only virtual machines that fail over in the same recovery plan will be able to connect to each other after failover to Azure.

If you want to deploy network mapping you'll need the following:

- The virtual machines you want to protect on the source VMM server should be connected to a VM network. That network should be linked to a logical network that is associated with the cloud.
- An Azure network to which replicated virtual machines can connect after failover. You'll select this network at the time of failover. The network should be in the same region as your Azure Site Recovery subscription.
- Learn more about network mapping:
	- [Configuring logical networking in VMM](http://technet.microsoft.com/zh-cn/library/jj721568.aspx)
	- [Configuring VM networks and gateways in VMM](http://technet.microsoft.com/zh-cn/library/jj721575.aspx)
	- [Configure and monitor virtual networks in Windows Azure](/documentation/services/networking)


## Step 1: Create a Site Recovery vault

1. Sign in to the [Management Portal](https://manage.windowsazure.cn) from the VMM server you want to register.


2. Expand
3. *Data Services*, expand *Recovery Services*, and click *Site Recovery Vault*.
3. Click *Create New* and then click *Quick Create*.


4. In *Name*, enter a friendly name to identify the vault.

5. In <b>Region</b>, select the geographic region for the vault. Available geographic regions include China East, China North.
6. Click <b>Create vault</b>. 

	![New Vault](./media/site-recovery-vmm-to-azure/ASRE2AVMM_HvVault.png)

<P>Check the status bar to confirm that the vault was successfully created. The vault will be listed as *Active* on the main Recovery Services page.</P>


## Step 2: Generate a vault registration key

Generate a registration key in the vault. After you download the Azure Site Recovery Provider and install it on the VMM server, you'll use this key to register the VMM server in the vault.

1. In the *Recovery Services* page, click the vault to open the Quick Start page. Quick Start can also be opened at any time using the icon.

	![Quick Start Icon](./media/site-recovery-vmm-to-azure/ASRE2AVMM_QuickStartIcon.png)

2. In the dropdown list, select **Between an on-premises VMM site and Windows Azure**.
3. In **Prepare VMM Servers**, click **Generate registration key** file. The key file is generated automatically and is valid for 5 days after it's generated. If you're not accessing the Azure Management Portal from the VMM server you'll need to copy this file to the server.

	![Registration key](./media/site-recovery-vmm-to-azure/ASRE2AVMM_RegisterKey.png)

## Step 3: Install the Azure Site Recovery Provider

4. On the <b>Quick Start</b> page, in **Prepare VMM servers**, click <b>Download Windows Azure Site Recovery Provider for installation on VMM servers</b> to obtain the latest version of the Provider installation file.

2. Run this file on the source VMM server. If VMM is deployed in a cluster and you're installing the Provider for the first time install it on an active node and finish the installation to register the VMM server in the vault. Then install the Provider on the other nodes. Note that if you're upgrading the Provider you'll need to upgrade on all nodes because they should all be running the same Provider version.


3. The Installer does a few **Pre-requirements Check** and requests permission to stop the VMM service to begin Provider setup. The VMM Service will be restarted automatically when setup finishes. If you're installing on a VMM cluster you'll be prompted to stop the Cluster role.

4. In **Microsoft Update** you can opt in for updates. With this setting enabled Provider updates will be installed according to your Microsoft Update policy.

	![Microsoft Updates](./media/site-recovery-vmm-to-azure/VMMASRInstallMUScreen.png)


1.  The install location is set to **<SystemDrive>\Program Files\Microsoft System Center 2012 R2\Virtual Machine Manager\bin**. Click on the Install button to start installing the Provider.
	![InstallLocation](./media/site-recovery-vmm-to-azure/VMMASRInstallLocationScreen.png)



1. After the Provider is installed click 'Register' button to register the server in the vault.
	![InstallComplete](./media/site-recovery-vmm-to-azure/VMMASRInstallComplete.png)

5. In **Internet Connection** specify how the Provider running on the VMM server connects to the Internet. Select <b>Use default system proxy settings</b> to use the default Internet connection settings configured on the server.

	![Internet Settings](./media/site-recovery-vmm-to-azure/VMMASRRegisterProxyDetailsScreen.png)
	- If you want to use a custom proxy you should set it up before you install the Provider. When you configure custom proxy settings a test will run to check the proxy connection.
	- If you do use a custom proxy, or your default proxy requires authentication you'll need to enter the proxy details, including the proxy address and port.
	- Following urls should be accessible from the VMM Server and the Hyper-v hosts: 
		- *.hypervrecoverymanager.windowsazure.cn
		- *.accesscontrol.chinacloudapi.cn
		- *.backup.windowsazure.cn
		- *.blob.core.chinacloudapi.cn
		- *.store.core.chinacloudapi.cn
	- Allow the IP addresses described in [Azure Datacenter IP Ranges](https://msdn.microsoft.com/zh-cn/library/azure/dn175718.aspx) and HTTPS (443) protocol. You would have to white-list IP ranges of the Azure region that you plan to use and that of China East.

	- If you use a custom proxy a VMM RunAs account (DRAProxyAccount) will be created automatically using the specified proxy credentials. Configure the proxy server so that this account can authenticate successfully. The VMM RunAs account settings can be modified in the VMM console. To do this, open the Settings workspace, expand Security, click Run As Accounts, and then modify the password for DRAProxyAccount. You'll need to restart the VMM service so that this setting takes effect.

6. In **Registration Key**, select that you downloaded from Azure Site Recovery and copied to the VMM server.
7. In **Vault name**, verify the name of the vault in which the server will be registered. Click *Next*.


	![Server registration](./media/site-recovery-vmm-to-azure/VMMASRRegisterVaultCreds.png)

9. You can specify a location to save an SSL certificate that's automatically generated for data encryption. This certificate is used if you enable data encryption for a cloud protected by Azure in the Azure Site Recovery portal. Keep this certificate safe. When you run a failover to Azure you'll select it in order to decrypt encrypted data.

	![Server registration](./media/site-recovery-vmm-to-azure/VMMASRRegisterEncryptionScreen.png)

8. In **Server name**, specify a friendly name to identify the VMM server in the vault. In a cluster configuration specify the VMM cluster role name.

8. In **Initial cloud metadata** sync select whether you want to synchronize metadata for all clouds on the VMM server with the vault. This action only needs to happen once on each server. If you don't want to synchronize all clouds, you can leave this setting unchecked and synchronize each cloud individually in the cloud properties in the VMM console.
	![Server registration](./media/site-recovery-vmm-to-azure/VMMASRRegisterFriendlyName.png)


8. Click *Next* to complete the process. After registration, metadata from the VMM server is retrieved by Azure Site Recovery. The server is displayed on the  *VMM Servers* tab on the **Servers** page in the vault.

>[AZURE.NOTE] The Azure Site Recovery Provider can also be installed using the following command line. This method can be used to install the provider on a Server CORE for Windows Server 2012 R2

1. Download the Provider installation file and registration key to a folder say C:\ASR
1. Stop the System Center Virtual Machine Manager Service
1. Extract the Provider installer by executing the below commands from a command prompt with **Administrator** privileges

    	C:\Windows\System32> CD C:\ASR
    	C:\ASR> AzureSiteRecoveryProvider.exe /x:. /q
1. Install the provider by executing the following command

		C:\ASR> setupdr.exe /i
1. Register the provider by running the following command

    	CD C:\Program Files\Microsoft System Center 2012 R2\Virtual Machine Manager\bin
    	C:\Program Files\Microsoft System Center 2012 R2\Virtual Machine Manager\bin\> DRConfigurator.exe /r  /Friendlyname <friendly name of the server> /Credentials <path of the credentials file> /EncryptionEnabled <full file name to save the encryption certificate>       

  
#### Command line Install Parameter List

 - **/Credentials** : Mandatory parameter that specifies the location in which the registration key file is located  
 - **/FriendlyName** : Mandatory parameter for the name of the Hyper-V host server that appears in the Azure Site Recovery portal.
 - **/EncryptionEnabled** : Optional Parameter that you need to use only in the VMM to Azure Scenario if you need encryption of your virtual machines at at rest in Azure. Please ensure that the name of the file you provide has a **.pfx** extension.
 - **/proxyAddress** : Optional parameter that specifies the address of the proxy server.
 - **/proxyport** : Optional parameter that specifies the port of the proxy server.
 - **/proxyUsername** : Optional parameter that specifies the Proxy user name (if proxy requires authentication).
 - **/proxyPassword** :Optional parameter that specifies the Password for authenticating with the proxy server (if proxy requires authentication).  


## Step 4: Create an Azure storage account

If you don't have an Azure storage account, click **Add an Azure Storage Account**. The account should have geo-replication enabled. It must in the same region as the Azure Site Recovery service, and be associated with the same subscription.


![Storage account](./media/site-recovery-vmm-to-azure/ASRE2AVMM_StorageAgent.png)

## Step 5: Install the Azure Recovery Services Agent

Install the Azure Recovery Services agent on each Hyper-V host server located in the VMM clouds you want to protect.

1. On the Quick Start page, click <b>Download Azure Site Recovery Services Agent and install on hosts</b> to obtain the latest version of the agent installation file.

	![Install Recovery Services Agent](./media/site-recovery-vmm-to-azure/ASRE2AVMM_InstallHyperVAgent.png)

2. Run the installation file on each Hyper-V host server that's located in VMM clouds you want to protect.
3. On the **Prerequisites Check** page click <b>Next</b>. Any missing prerequisites will be automatically installed.

	![Prerequisites Recovery Services Agent](./media/site-recovery-vmm-to-azure/ASRE2AVMM_AgentPrereqs.png)

4. On the **Installation Settings** page, specify where you want to install the Agent and select the cache location in which backup metadata will be installed. Then click <b>Install</b>.

## Step 6: Configure cloud protection settings

After the VMM server is registered, you can configure cloud protection settings. You enabled the option **Synchronize cloud data with the vault** when you installed the Provider so all clouds on the VMM server will appear in the <b>Protected Items</b> tab in the vault.

![Published Cloud](./media/site-recovery-vmm-to-azure/ASRE2AVMM_CloudsList.png)


1. On the Quick Start page, click **Set up protection for VMM clouds**.
2. On the **Protected Items** tab, click on the cloud you want to configure and go to the **Configuration** tab.
3. In <b>Target</b>, select <b>Windows Azure</b>.
4. In <b>Storage Account</b>, select the Azure storage account you want to use to replicate your virtual machines to.
5. Set <b>Encrypt stored data</b> to <b>Off</b>. This setting specifies that data should be encrypted replicated between the on-premises site and Azure.
6. In <b>Copy frequency</b> leave the default setting. This value specifies how frequently data should be synchronized between source and target locations.
7. In <b>Retain recovery points for</b>, leave the default setting. With a default value of zero, only the latest recovery point for a primary virtual machine is stored on a replica host server.
8. In <b>Frequency of application-consistent snapshots</b>, leave the default setting. This value specifies how often to create snapshots. Snapshots use Volume Shadow Copy Service (VSS) to ensure that applications are in a consistent state when the snapshot is taken.  If you do set a value, make sure it's less than the number of additional recovery points you configure.
9. In <b>Replication start time</b>, specify when initial replication of data to Azure should start. The timezone on the Hyper-V host server will be used. We recommend that you schedule the initial replication during off-peak hours.

	![Cloud replication settings](./media/site-recovery-vmm-to-azure/ASRE2AVMM_CloudSettings.png)

After you save the settings a job will be created and can be monitored on the <b>Jobs</b> tab. All Hyper-V host servers in the VMM source cloud will be configured for replication.

After saving, cloud settings can be modified on the <b>Configure</b> tab. To modify the target location or target storage account you'll need to remove the cloud configuration, and then reconfigure the cloud. Note that if you change the storage account the change is only applied for virtual machines that are enabled for protection after the storage account has been modified. Existing virtual machines are not migrated to the new storage account.</p>

## Step 7: Configure network mapping
Before you begin network mapping verify that virtual machines on the source VMM server are connected to a VM network. In addition, create one or more Azure virtual networks. Note that multiple VM networks can be mapped to a single Azure network.

1. On the Quick Start page, click **Map networks**.
2. On the **Networks** tab, in **Source location**, select the source VMM server. In **Target location** select Azure.
3. In **Source** networks a list of VM networks associated with the VMM server are displayed. In **Target** networks the Azure networks associated with the subscription are displayed.
4. Select the source VM network and click **Map**.
5. On the **Select a Target Network** page, select the target Azure network you want to use.
6. Click the check mark to complete the mapping process.

	![Cloud replication settings](./media/site-recovery-vmm-to-azure/ASRE2AVMM_MapNetworks.png)

After you save the settings a job starts to track the mapping progress and it can be monitored on the Jobs tab. Any existing replica virtual machines that correspond to the source VM network will be connected to the target Azure networks. New virtual machines that are connected to the source VM network will be connected to the mapped Azure network after replication. If you modify an existing mapping with a new network, replica virtual machines will be connected using the new settings.

Note that if the target network has multiple subnets and one of those subnets has the same name as subnet on which the source virtual machine is located, then the replica virtual machine will be connected to that target subnet after failover. If there's no target subnet with a matching name, the virtual machine will be connected to the first subnet in the network.

## Step 8: Enable protection for virtual machines

After servers, clouds, and networks are configured correctly, you can enable protection for virtual machines in the cloud. Note the following:

- Virtual machines must meet Azure requirements. Check these in <a href="https://msdn.microsoft.com/zh-CN/library/dn469078.aspx">Prerequisites and support</a> in the Planning guide.
- To enable protection the operating system and operating system disk properties must be set for the virtual machine. When you create a virtual machine in VMM using a virtual machine template you can set the property. You can also set these properties for existing virtual machines on the **General** and **Hardware Configuration** tabs of the virtual machine properties. If you don't set these properties in VMM you'll be able to configure them in the Azure Site Recovery portal.

![Create virtual machine](./media/site-recovery-vmm-to-azure/ASRE2AVMM_EnableNew.png)

![Modify virtual machine properties](./media/site-recovery-vmm-to-azure/ASRE2AVMM_EnableExisting.png)


1. To enable protection, on the <b>Virtual Machines</b> tab in the cloud in which the virtual machine is located, click <b>Enable protection</b> and then select <b>Add virtual machines</b>
2. From the list of virtual machines in the cloud, select the one you want to protect.

	![Enable virtual machine protection](./media/site-recovery-vmm-to-azure/ASRE2AVMM_SelectVM.png)

	Track progress of the Enable Protection action in the **Jobs** tab, including the initial replication. After the Finalize Protection job runs the virtual machine is ready for failover. After protection is enabled and virtual machines are replicated, you'll be able to view them in Azure.


	![Virtual machine protection job](./media/site-recovery-vmm-to-azure/ASRE2AVMM_VMJobs.png)

3. Verify the virtual machine properties and modify as required.

	![Verify virtual machines](./media/site-recovery-vmm-to-azure/VMProperties.png)

4. On the configure tab of the virtual machine properties following network properties could be modified.


	1.  Number of network adapters of target virtual machine - The number of network adapters is dictated by the size you specify for the target virtual machine. Check [virtual machine size specs](/documentation/articles/virtual-machines-size-specs#size-tables) for the number of nics supported by the virtual machine size. 

		When you modify the size for a virtual machine and save the settings, the number of network adapter will change when you open **Configure** page the next time.The number of network adapters of target virtual machines is minimum of the number of network adapters on source virtual machine and maximum number of network adapters supported by the size of the virtual machine chosen. It is explained below:


		- If the number of network adapters on the source machine is less than or equal to the number of adapters allowed for the target machine size, then the target will have the same number of adapters as the source.
		- If the number of adapters for the source virtual machine exceeds the number allowed for the target size then the target size maximum will be used.
		- For example if a source machine has two network adapters and the target machine size supports four, the target machine will have two adapters. If the source machine has two adapters but the supported target size only supports one then the target machine will have only one adapter. 	


	1. Network of the target virtual machine - The network to which the virtual machine connects to is determined by network mapping of the network of source virtual machine. In case source virtual machine has more than one network adapters and source networks are mapped to different networks on target, then the user would have to choose between one of the target networks.

	1. Subnet of each of the network adapters - For each network adapter the user can choose the subnet to which the failed over virtual machine would connect to.

	1. Target IP - If the network adapter of source virtual machine is configured to use static IP then the user can provide the ip for the target virtual machine. User can use this capability to retain the ip of the source virtual machine after a failover. If no IP is provided any available IP would be given to network adapter at the time of failover. In case the target IP provided by user is already used by some other virtual machine that is already running in Azure then the failover would fail.  

		![Modify network properties](./media/site-recovery-vmm-to-azure/MultiNic.png)

>[AZURE.NOTE] Linux virtual machines that use static ip are not supported.

## Test your deployment
To test your deployment you can run a test failover for a single virtual machine, or create a recovery plan consisting of multiple virtual machines and run a test failover for the plan.  Test failover simulates your failover and recovery mechanism in an isolated network. Note that:

- If you want to connect to the virtual machine in Azure using Remote Desktop after the failover, enable Remote Desktop Connection on the virtual machine before you run the test failover.
- After failover you'll use a public IP address to connect to the virtual machine in Azure using Remote Desktop. If you want to do this, ensure you don't have any domain policies that prevent you from connecting to a virtual machine using a public address.

### Create a recovery plan

1. On the **Recovery Plans** tab, add a new plan. Specify a name, **VMM** in **Source type**, and the source VMM server in **Source**, The target will be Azure.

	![Create recovery plan](./media/site-recovery-vmm-to-azure/ASRE2AVMM_RP1.png)

2. In the **Select Virtual Machines** page, select virtual machines to add to the recovery plan. These virtual machines are added to the recovery plan default group—Group 1. A maximum of 100 virtual machines in a single recovery plan have been tested.

	- If you want to verify the virtual machine properties before adding them to the plan, click the virtual machine on the properties page of the cloud in which it's located. You can also configure the virtual machine properties in the VMM console.
	- All of the virtual machines that are displayed have been enabled for protection. The list includes both virtual machines that are enabled for protection and initial replication has completed, and those that are enabled for protection with initial replication pending. Only virtual machines with initial replication completed can fail over as part of a recovery plan. Therefore, verify the initial replication status of virtual machines in the plan before starting recovery plan failover.
	

	![Create recovery plan](./media/site-recovery-vmm-to-azure/ASRE2AVMM_SelectVMRP.png)

After a recovery plan has been created it appears in the **Recovery Plans** tab. You can also add [Azure Automation Runbooks](/documentation/articles/site-recovery-runbook-automation) to the recovery plan to automate failover time actions.

### Run a test failover

There are two ways to run a test failover to Azure.

- Test failover without an Azure network—This type of test failover checks that the virtual machine comes up correctly in Azure. The virtual machine won't be connected to any Azure network after failover.
- Test failover with an Azure network—This type of failover checks that the entire replication environment comes up as expected and that failed over the virtual machines will be connected to the specified target Azure network. For subnet handling, for test failover the subnet of the test virtual machine will be figured out based on the subnet of the replica virtual machine. This is different to regular replication when the subnet of a replica virtual machine is based on the subnet of the source virtual machine.

If you want to run a test failover for a virtual machine enabled for protection to Azure without specifying an Azure target network you don't need to prepare anything. To run a test failover with a target Azure network you'll need to create a new Azure network that's isolated from your Azure production network (default behavior when you create a new network in Azure). Look at how to [run a test failover](/documenatation/articles/site-recovery-failover#run-a-test-failover) for more details.


You will also need to set up the infrastructure for the replicated virtual machine to work as expected. For example, a virtual machine with Domain Controller and DNS can be replicated to Azure using Azure Site Recovery and can be created in the test network using Test Failover. Look at [test failover considerations for active directory](/documentation/articles/site-recovery-active-directory#considerations-for-test-failover) section for more details. 

To run a test failover do the following:

1. On the **Recovery Plans** tab, select the plan and click **Test Failover**.
1. On the **Confirm Test Failover** page select **None** or a specific Azure network.  Note that if you select None the test failover will check that the virtual machine replicated correctly to Azure but doesn't check your replication network configuration.

	![No network](./media/site-recovery-vmm-to-azure/ASRE2AVMM_TestFailoverNoNetwork.png)

1. If data encryption is enabled for the cloud, in **Encryption Key** select the certificate that was issued during installation of the Provider on the VMM server, when you turned on the option to enable data encryption for a cloud.
1. On the **Jobs** tab you can track failover progress. You should also be able to see the virtual machine test replica in the Azure Management Portal. If you're set up to access virtual machines from your on-premises network you can initiate a Remote Desktop connection to the virtual machine.
1. When the failover reaches the **Complete testing** phase , click **Complete Test** to finish up the test failover. You can drill down to the **Job** tab to track failover progress and status, and to perform any actions that are needed.
1. After  failover you'll be able to see the virtual machine test replica in the Azure Management Portal. If you're set up to access virtual machines from your on-premises network you can initiate a Remote Desktop connection to the virtual machine. Note that:

    a. Verify that the virtual machines start successfully.

    b. If you want to connect to the virtual machine in Azure using Remote Desktop after the failover, enable Remote Desktop Connection on the virtual machine before you run the test failover. You will also need to add an RDP endpoint on the virtual machine. You can leverage an [Azure Automation Runbooks](/documentation/articles/site-recovery-runbook-automation) to do that.

    c. After failover, if you use a public IP address to connect to the virtual machine in Azure using Remote Desktop, ensure you don't have any domain policies that prevent you from connecting to a virtual machine using a public address.

1.  After the testing is complete do the following:
	- Click **The test failover is complete**. Clean up the test environment to automatically power off and delete the test virtual machines.
	- Click **Notes** to record and save any observations associated with the test failover.

## <a id="runtest" name="runtest" href="#runtest"></a>Monitor activity
<p>You can use the *Jobs* tab and *Dashboard* to view and monitor the main jobs performed by the Azure Site Recovery vault, including configuring protection for a cloud, enabling and disabling protection for a virtual machine, running a failover (planned, unplanned, or test), and committing an unplanned failover.</p>

<p>From the *Jobs* tab you view jobs, drill down into job details and errors, run job queries to retrieve jobs that match specific criteria, export jobs to Excel, and restart failed jobs.</p>

<p>From the *Dashboard* you can download the latest versions of Provider and Agent installation files, get configuration information for the vault, see the number of virtual machines that have protection managed by the vault, see recent jobs, manage the vault certificate, and resynchronize virtual machines.</p>

<p>For more information about interacting with jobs and the dashboard, see the <a href="/documentation/articles/site-recovery-manage-registration-and-protection">Operations and Monitoring Guide</a>.</p>

##<a id="next" name="next" href="#next"></a>Next steps
<UL>
<LI>To plan and deploy Azure Site Recovery in a full production environment, see <a href="/documentation/articles/site-recovery-best-practices">Planning Guide for Azure Site Recovery</a> and <a href="/documentation/articles/site-recovery-vmm-to-vmm">Deployment Guide for Azure Site Recovery</a>.</LI>


<LI>For questions, visit the <a href="https://social.msdn.microsoft.com/forums/azure/zh-cn/home?forum=hypervrecovmgr">Azure Recovery Services Forum</a>.</LI>
</UL>
