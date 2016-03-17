<properties
	pageTitle="Create an Azure virtual machine running Linux in the Azure Management Portal | Azure"
	description="Use the Azure Management Portal to create an Azure virtual machine (VM) running Linux with the Azure resource groups."
	services="virtual-machines"
	documentationCenter=""
	authors="squillace"
	manager="timlt"
	editor="tysonn"
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/21/2015"
	wacn.date=""/>

# Create a Virtual Machine Running Linux using the Azure Management Portal

> [AZURE.SELECTOR]
- [Portal - Windows](/documentation/articles/virtual-machines-windows-tutorial-classic-portal)
- [PowerShell](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)
- [Portal - Linux](/documentation/articles/virtual-machines-linux-tutorial-portal-rm)
- [CLI](/documentation/articles/virtual-machines-linux-tutorial)

<br>

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)]

Creating an Azure virtual machine (VM) that runs Linux is easy to do. This tutorial shows you how to use the Azure Management Portal to create one quickly, and uses the `.pem` certificate file to secure your **SSH** connection to the VM. You can also create Linux VMs using [your own images as templates](/documentation/articles/virtual-machines-linux-create-upload-vhd).

[AZURE.INCLUDE [free-trial-note](../includes/free-trial-note.md)]

## Select the image

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn).

2. At the bottom of the portal, click **New** > **Compute** > **Virtual Machine** > **From Gallery**. Select **Ubuntu Server 14.04 LTS** in the image list.

	![choosing a VM image](./media/virtual-machines-linux-tutorial-portal-rm/chooseubuntuvm.png)

## Create the virtual machine

After you select the image, you can use Azure's default settings for most of the configuration and quickly create the VM.

1. On the **Virtual machine configuration**. Enter a **Name** you want for the VM, and a certificate file (in this case the `.pem` file). For more information, see [How to Use SSH with Linux and Mac on Azure](/documentation/articles/virtual-machines-linux-use-ssh-key).

	![](./media/virtual-machines-linux-tutorial-portal-rm/step-1-thebasics.png)

	> [AZURE.NOTE] You may also choose username/password authentication here and enter that information if you do not want to secure your **ssh** session with a public and private key exchange.

2. Choose the pricing **Tier**, and use **Size** drop-down menu to select an appropriate VM size for your needs. Each size specifies the number of compute cores, memory, and other features, such as support for Premium Storage, which will affect the price. Azure recommends certain sizes automatically depending on the image you choose.

	>[AZURE.NOTE] Premium storage is available for DS-series virtual machines, which is not configurable in the portal yet. Howerever, you can use Azure PowerShell to create a DS-series virtual manchine. Premium storage is the best storage option for data intensive workloads such as a database. For details, see [Premium Storage: High-Performance Storage for Azure Virtual Machine Workloads](/documentation/articles/storage-premium-storage-preview-portal).

3. Click **Next** button to see storage and networking settings for the new VM. For a first VM you can generally accept the default settings.

	![](./media/virtual-machines-linux-tutorial-portal-rm/step-3-settings.png)

6. Click **Next** button, and choose to install the VM Agent or not. Notice that the **Configuration Extensions** is not available for Linux yet.

8. Click **Complete** button to create the virtual machine. After the virtual machine is created, you will be able to see it from the virtual machine list.

## Connect to your Azure Linux VM using **ssh**

Now you can connect to your Ubuntu VM using **ssh** in the standard way. You can choose your virtual machine from virtual machine list, and click **Dashboard**. You can find the **Public virtual IP (VIP) address** there.

![summary of successful creation](./media/virtual-machines-linux-tutorial-portal-rm/successresultwithip.png)

Now you can **ssh** into your Azure VM, and you're ready to go.

	ssh ops@23.96.106.1 -p 22
	The authenticity of host '23.96.106.1 (23.96.106.1)' can't be established.
	ECDSA key fingerprint is bc:ee:50:2b:ca:67:b0:1a:24:2f:8a:cb:42:00:42:55.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added '23.96.106.1' (ECDSA) to the list of known hosts.
	Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.16.0-43-generic x86_64)

	 * Documentation:  https://help.ubuntu.com/

	  System information as of Mon Jul 13 21:36:28 UTC 2015

	  System load: 0.31              Memory usage: 5%   Processes:       208
	  Usage of /:  42.1% of 1.94GB   Swap usage:   0%   Users logged in: 0

	  Graph this data and manage this system at:
	    https://landscape.canonical.com/

	  Get cloud support with Ubuntu Advantage Cloud Guest:
	    http://www.ubuntu.com/business/services/cloud

	0 packages can be updated.
	0 updates are security updates.

	The programs included with the Ubuntu system are free software;
	the exact distribution terms for each program are described in the
	individual files in /usr/share/doc/*/copyright.

	Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
	applicable law.

	ops@ubuntuvm:~$

## Next Steps

To learn more about Linux on Azure, see:

- [Linux and Open-Source Computing on Azure](/documentation/articles/virtual-machines-linux-opensource)

- [How to use the Azure Command-Line Tools for Mac and Linux](/documentation/articles/virtual-machines-command-line-tools)

- [Deploy a LAMP app using the Azure CustomScript Extension for Linux](/documentation/articles/virtual-machines-linux-script-lamp)

- [The Docker Virtual Machine Extension for Linux on Azure](/documentation/articles/virtual-machines-docker-vm-extension)
