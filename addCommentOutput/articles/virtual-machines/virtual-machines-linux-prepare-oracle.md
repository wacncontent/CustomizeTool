<properties
pageTitle="Prepare an Oracle Linux Virtual Machine for Azure | Azure"
description="Step by Step configuration of an Oracle virtual machine running Linux in Azure."
services="virtual-machines-linux"
authors="bbenz"
manager="timlt"
documentationCenter="virtual-machines"
tags="azure-service-management,azure-resource-manager"
/>

<tags
ms.service="virtual-machines-linux"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="vm-linux"
ms.workload="infrastructure-services"
ms.date="06/22/2015"
wacn.date=""
ms.author="bbenz" />

# Prepare an Oracle Linux virtual machine for Azure

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-both-include.md)]


-   [Prepare an Oracle Linux 6.4+ virtual machine for Azure](/documentation/articles/virtual-machines-linux-oracle-create-upload-vhd/)

-   [Prepare an Oracle Linux 7.0+ virtual machine for Azure](/documentation/articles/virtual-machines-linux-oracle-create-upload-vhd/)

## Prerequisites
This article assumes that you have already installed an Oracle Linux operating system to a virtual hard disk. Multiple tools exist to create .vhd files, for example a virtualization solution such as Hyper-V. For instructions, see [Install Hyper-V and create a virtual machine](http://technet.microsoft.com/zh-cn/library/hh846766.aspx).

**Oracle Linux installation notes**

- Oracle's Red Hat compatible kernel and its UEK3 (Unbreakable Enterprise Kernel) are both supported on Hyper-V and Azure. For best results, be sure to update to the latest kernel while preparing your Oracle Linux VHD.

- Oracle's UEK2 is not supported on Hyper-V and Azure as it does not include the required drivers.

- The newer VHDX format is not supported in Azure. You can convert the disk to VHD format by using Hyper-V Manager or the convert-vhd cmdlet.

- When you're installing the Linux system, we recommend that you use standard partitions rather than LVM (often the default for many installations). This will avoid LVM name conflicts with cloned VMs, particularly if an OS disk ever needs to be attached to another VM for troubleshooting. LVM or [RAID](/documentation/articles/virtual-machines-linux-configure-raid/) may be used on data disks if preferred.

- NUMA is not supported for larger VM sizes due to a bug in Linux kernel versions below 2.6.37. This issue primarily impacts distributions that use the upstream Red Hat 2.6.32 kernel. Manual installation of the Azure Linux agent (waagent) will automatically disable NUMA in the GRUB configuration for the Linux kernel. More information about this can be found in the steps below.

- Do not configure a swap partition on the OS disk. The Linux agent can be configured to create a swap file on the temporary resource disk. More information about this can be found in the steps below.

- All of the VHDs must have sizes that are multiples of 1 MB.

- Make sure that the `Addons` repository is enabled. Choose to edit the file `/etc/yum.repo.d/public-yum-ol6.repo`(Oracle Linux 6) or `/etc/yum.repo.d/public-yum-ol7.repo`(Oracle Linux ), and change the line `enabled=0` to `enabled=1` under **[ol6_addons]** or **[ol7_addons]** in this file.


## Oracle Linux 6.4+
You must complete specific configuration steps in the operating system for the virtual machine to run in Azure.

1. In the center pane of Hyper-V Manager, select the virtual machine.

2. Click **Connect** to open the window for the virtual machine.

3. Uninstall NetworkManager by running the following command:

		# sudo rpm -e --nodeps NetworkManager

	>[AZURE.NOTE] If the package is not already installed, this command will fail with an error message. This is expected.

4. Create a file named **network** in the /etc/sysconfig/ directory that contains the following text:

	`NETWORKING=yes`  
	`HOSTNAME=localhost.localdomain`

5.  Create a file named **ifcfg-eth0** in the /etc/sysconfig/network-scripts/ directory that contains the following text:

		DEVICE=eth0
		ONBOOT=yes
		BOOTPROTO=dhcp
			TYPE=Ethernet
			USERCTL=no
			PEERDNS=yes
		IPV6INIT=no

6.  Move (or remove) udev rules to avoid generating static rules for the Ethernet interface. These rules cause problems when you're cloning a virtual machine in Azure or Hyper-V:

		# sudo mkdir -m 0700 /var/lib/waagent
		# sudo mv /lib/udev/rules.d/75-persistent-net-generator.rules /var/lib/waagent/ 2\>/dev/null
		# sudo mv /etc/udev/rules.d/70-persistent-net.rules /var/lib/waagent/ 2\>/dev/null

7.  Ensure that the network service will start at boot time by running the following command:

		# chkconfig network on

8.  Install python-pyasn1 by running the following command:

		# sudo yum install python-pyasn1

9.  Modify the kernel boot line in your grub configuration to include additional kernel parameters for Azure. To do this, open "/boot/grub/menu.lst" in a text editor and ensure that the default kernel includes the following parameters:

		console=ttyS0 earlyprintk=ttyS0 rootdelay=300 numa=off

	This will also ensure that all console messages are sent to the first serial port, which can assist Azure support with debugging issues. This will disable NUMA due to a bug in Oracle's Red Hat compatible kernel.

	In addition to the above, we recommend that you *remove* the following parameters:

		rhgb quiet crashkernel=auto

	Graphical and quiet boot are not useful in a cloud environment where we want all the logs to be sent to the serial port.

	The `crashkernel` option may be left configured if desired, but note that this parameter will reduce the amount of available memory in the VM by 128 MB or more. This may be problematic on the smaller VM sizes.

10.  Ensure that the SSH server is installed and configured to start at boot time. This is usually the default.

11.  Install the Azure Linux Agent by running the following command:

		# sudo yum install WALinuxAgent

	Note that installing the WALinuxAgent package will remove the NetworkManager and NetworkManager-gnome packages if they were not already removed as described in step 2.

12.  Do not create swap space on the OS disk.

	The Azure Linux Agent can automatically configure swap space by using the local resource disk that is attached to the VM after provisioning on Azure. Note that the local resource disk is a *temporary* disk, and it might be emptied when the VM is deprovisioned. After you install the Azure Linux Agent (see previous step), modify the following parameters in /etc/waagent.conf appropriately:

		ResourceDisk.Format=y

		ResourceDisk.Filesystem=ext4

		ResourceDisk.MountPoint=/mnt/resource

		ResourceDisk.EnableSwap=y

		ResourceDisk.SwapSizeMB=2048 ## NOTE: set this to whatever you need it to be.

13.  Run the following commands to deprovision the virtual machine and prepare it for provisioning on Azure:

		# sudo waagent -force -deprovision
		# export HISTSIZE=0
		# logout

14.  Click **Action -\> Shut Down** in Hyper-V Manager. Your Linux VHD is now ready to be uploaded to Azure.

## Oracle Linux 7.0+
**Changes in Oracle Linux 7**

Preparing an Oracle Linux 7 virtual machine for Azure is very similar to the process for Oracle Linux 6. However, there are several important differences worth noting:

-   Both the Red Hat compatible kernel and Oracle's UEK3 are supported in Azure. We recommend the UEK3 kernel.

-   The NetworkManager package no longer conflicts with the Azure Linux agent. This package is installed by default, and we recommend that it is not removed.

-   GRUB2 is now used as the default bootloader, so the procedure for editing kernel parameters has changed (see below).

-   XFS is now the default file system. The ext4 file system can still be used if desired.

**Configuration steps**

1.  In Hyper-V Manager, select the virtual machine.

2.  Click **Connect** to open a console window for the virtual machine.

3.  Create a file named **network** in the /etc/sysconfig/ directory that contains the following text:

		NETWORKING=yes
		HOSTNAME=localhost.localdomain

4.  Create a file named **ifcfg-eth0** in the /etc/sysconfig/network-scripts/ directory that contains the following text:

		DEVICE=eth0
		ONBOOT=yes
		BOOTPROTO=dhcp
		TYPE=Ethernet
		USERCTL=no
			PEERDNS=yes
		IPV6INIT=no

5.  Move (or remove) udev rules to avoid generating static rules for the Ethernet interface. These rules cause problems when you're cloning a virtual machine in Azure or Hyper-V.

		# sudo mkdir -m 0700 /var/lib/waagent
		# sudo mv /lib/udev/rules.d/75-persistent-net-generator.rules /var/lib/waagent/ 2>/dev/null
		# sudo mv /etc/udev/rules.d/70-persistent-net.rules /var/lib/waagent/ 2>/dev/null

6.  Ensure that the network service will start at boot time by running the following command:

		# sudo chkconfig network on

7.  Install the python-pyasn1 package by running the following command:

		# sudo yum install python-pyasn1

8.  Run the following command to clear the current yum metadata and install any updates:

		# sudo yum clean all
		# sudo yum -y update

9.  Modify the kernel boot line in your grub configuration to include additional kernel parameters for Azure. To do this, open "/etc/default/grub" in a text editor and edit the GRUB\_CMDLINE\_LINUX parameter, for example:

		GRUB\_CMDLINE\_LINUX="rootdelay=300 console=ttyS0 earlyprintk=ttyS0"

	This will also ensure all console messages are sent to the first serial port, which can assist Azure support with debugging issues. In addition to the above, we recommend that you *remove* the following parameters:

		rhgb quiet crashkernel=auto

	Graphical and quiet boot are not useful in a cloud environment where we want all the logs to be sent to the serial port.

	The `crashkernel` option may be left configured if desired, but note that this parameter will reduce the amount of available memory in the VM by 128 MB or more. This may be problematic on the smaller VM sizes.

10.  Once you are done editing "/etc/default/grub", run the following command to rebuild the grub configuration:

		# sudo grub2-mkconfig -o /boot/grub2/grub.cfg

11.  Ensure that the SSH server is installed and configured to start at boot time. This is usually the default.

12.  Install the Azure Linux Agent by running the following command:

		# sudo yum install WALinuxAgent

13.  Do not create swap space on the OS disk.

	The Azure Linux Agent can automatically configure swap space by using the local resource disk that is attached to the VM after provisioning on Azure. Note that the local resource disk is a *temporary* disk, and it might be emptied when the VM is deprovisioned. After you install the Azure Linux Agent (see previous step), modify the following parameters in /etc/waagent.conf appropriately:

		ResourceDisk.Format=y
		ResourceDisk.Filesystem=ext4
		ResourceDisk.MountPoint=/mnt/resource
		ResourceDisk.EnableSwap=y
		ResourceDisk.SwapSizeMB=2048 ## NOTE: Set this to whatever you need it to be.

14.  Run the following commands to deprovision the virtual machine and prepare it for provisioning on Azure:

		# sudo waagent -force -deprovision
		# export HISTSIZE=0
		# logout

15.  Click **Action -\> Shut Down** in Hyper-V Manager. Your Linux VHD is now ready to be uploaded to Azure.
