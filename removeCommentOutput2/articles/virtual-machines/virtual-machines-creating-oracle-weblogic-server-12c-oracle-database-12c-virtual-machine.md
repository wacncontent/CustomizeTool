<properties
	pageTitle="Oracle WebLogic Server and Database VM | Azure"
	description="Create an Oracle WebLogic Server 12c and Oracle Database 12c Azure image running on Windows Server 2012, using Resource Manager deployment model."
	services="virtual-machines"
	authors="bbenz"
	documentationCenter=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="06/22/2015"
	wacn.date=""/>

#Create an Oracle WebLogic Server 12c and Oracle Database 12c virtual machine in Azure

This article shows how to create a virtual machine based on a Microsoft-provided Oracle WebLogic Server 12c and Oracle Database 12c image running on Windows Server 2012 in Azure.

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)]


##To create an Oracle WebLogic Server 12c and Oracle Database 12c virtual machine in Azure

1. Log in to the [Azure Management Portal](https://manage.windowsazure.cn/).


2. Click **New** > **Compute** > **From Gallery**.

3.	Select the **Windows Server 2012 R2 Datacenter (en-us)** or **Windows Server 2012 R2 Datacenter (zh-cn)** image.  Review the information about this image (such as minimum recommended size), and then click **Next**.

4.	Specify a **Virtual Machine Name** for the VM.

7.	Choose a **Tier** and **Size**. If you need a DS-Series VM, please create is through Azure PowerShell. For more information, see [Create Windows virtual machines with Powershell and the classic deployment model](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms).

5.	Specify a **New User Name** for the VM. Note that this user is for remotely logging into the VM; this is not the Oracle database user name.

6.	Specify and confirm a password for the VM and click next.

8.	Set the optional configuration as needed, with these considerations:
	1. Create a new cloud service or choose an existed cloud service
	2. Choose a **Location**
	1. Leave **Storage Account** as-is to create a new storage account with the VM name.
	2. Leave **Availability Set** as "(None)".
	3. Do not add any **endpoints** at this time. Click **Next**
	

10. Choose whether to install **Configuration extensions** and **Security extensions**, and click **Complete**.


##To create your database hosted in this virtual machine

Follow the instructions in [Create an Oracle Database 12c virtual machine in Azure](/documentation/articles/virtual-machines-creating-oracle-database-virtual-machine), beginning with the **To create your database using the Oracle Database 12c virtual machine in Azure** section.

##To configure your Oracle WebLogic Server 12c hosted in this virtual machine
Follow the instructions in [Create an Oracle WebLogic Server 12c virtual machine in Azure](/documentation/articles/virtual-machines-creating-oracle-webLogic-server-12c-virtual-machine), beginning with the **To configure your Oracle WebLogic Server 12c virtual machine in Azure** section.

##Additional resources
[Miscellaneous considerations for Oracle virtual machine images](/documentation/articles/miscellaneous-considerations-for-oracle-virtual-machine-images-new-article)

[List of Oracle virtual machine images](/documentation/articles/virtual-machines-oracle-list-oracle-virtual-machine-images)

[Connecting to Oracle Database from a Java Application](http://docs.oracle.com/cd/E11882_01/appdev.112/e12137/getconn.htm#TDPJD136)

[Oracle WebLogic Server 12c using Linux on Azure](http://www.oracle.com/technetwork/middleware/weblogic/learnmore/oracle-weblogic-on-azure-wp-2020930.pdf)

[Oracle Database 2 Day DBA 12c Release 1](http://docs.oracle.com/cd/E16655_01/server.121/e17643/toc.htm)
