<properties
	pageTitle="Create a Linux virtual machine | Azure"
	description="Learn to create a Linux virtual machine or Ubuntu virtual machine by using an image from Azure and the Azure Command-Line Interface."
	keywords="linux virtual machine,virtual machine linux,ubuntu virtual machine" 
	services="virtual-machines"
	documentationCenter=""
	authors="squillace"
	manager="timlt"
	editor="tysonn"
	tags="azure-resource-manager" />

<tags
	ms.service="virtual-machines"
	ms.date="10/21/2015"
	wacn.date=""/>

# Create a Linux virtual machine

> [AZURE.SELECTOR]
- [Portal - Windows](/documentation/articles/virtual-machines-windows-tutorial-classic-portal)

- [PowerShell](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)
- [Portal - Linux](/documentation/articles/virtual-machines-linux-tutorial-portal-rm)
- [CLI](/documentation/articles/virtual-machines-linux-tutorial)

Creating a Linux virtual machine (VM) is easy to do from the command line or from the portal. This tutorial shows you how to use the Azure Command-Line Interface (CLI) for Mac, Linux, and Windows to quickly create an Ubuntu Server VM running in Azure, connect to it using **ssh**, and create and mount a new disk. This topic uses an Ubuntu Server VM, but you can also create Linux virtual machine using [your own images as templates](/documentation/articles/virtual-machines-linux-create-upload-vhd).


[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)]

[AZURE.INCLUDE [free-trial-note](../includes/free-trial-note.md)]

## Install the Azure CLI

The first step is to [install the Azure CLI](/documentation/articles/xplat-cli-install).


Good. Now make sure you're in the Service Manager mode by typing `azure config mode asm`.

Even better. Now [log in with your work or school id](/documentation/articles/xplat-cli-connect#use-the-log-in-method) by typing `azure login -e AzureChinaCloud -u <your account>` and following the prompts for an interactive login experience to your Azure account.

## Create the Linux virtual machine


You can use `azure vm create-from <your-vm-name> example.json` to create a new virtual machine. If you are creating a new cloud service for your virtual machine, you need to use `-l` parameter to specify the location of your cloud service. For Example, `azure vm create-from <your-vm-name> example.json -l "China East"`. The following is a sample json file for the virtual machine creation.

	{
	    "configurationSets": [
	        {
	            "inputEndpoints": [
	                {
	                    "localPort": 22,
	                    "name": "SSH",
	                    "port": 22,
	                    "protocol": "tcp",
	                    "virtualIPAddress": "",
	                    "enableDirectServerReturn": false
	                }
	            ],
	            "networkInterfaces": [],
	            "publicIPs": [],
	            "storedCertificateSettings": [],
	            "subnetNames": [],
	            "configurationSetType": "NetworkConfiguration"
	        },
	        {
	            "configurationSetType":"LinuxProvisioningConfiguration",
	            "hostName": "myubuntu",
	            "userName": "<adminName>",
	            "userPassword": "<adminPass>",
                "disableSshPasswordAuthentication": "false",
                "sSh":{
                    "publicKeys": [
                        {
                            "fingerprint": "",
                            "path": ""
                        }
                    ],
                    "keyPairs": [
                        {
                            "fingerprint": "",
                            "path": ""
                        }
                    ]
                },
                "customData": ""
	        }
	    ],
	    "dataVirtualHardDisks": [],
	    "resourceExtensionReferences": [],
	    "roleName": "myubuntu",
	    "oSVersion": "",
	    "roleType": "PersistentVMRole",
	    "oSVirtualHardDisk": {
	        "hostCaching": "ReadWrite",
	        "mediaLink": "https://<storageaccountname>.blob.core.chinacloudapi.cn/vhds/myubuntu-myubuntu-2016-02-19.vhd",
	        "sourceImageName":"b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140416.1-en-us-30GB",
	        "operatingSystem": "Linux"
	    },
	    "roleSize": "Basic_A0",
	    "provisionGuestAgent": true
	}

- configurationSets: Contains a collection of configuration sets that define system and application settings.

	* NetworkConfiguration: You can optionally specify a NetworkConfiguration set that contains the metadata required to create the virtual network configuration for a Virtual Machine.
	* LinuxProvisioningConfiguration: You can configure Your VM host name, user name, password and SSH Public keys, and so on.

- dataVirtualHardDisks: Specify VHDs that are attached to your VM. If you are using Premium Storage, "roleSize" must be in DS-Series.
- oSVirtualHardDisk: Specify a OS VHD for your vm.

	* mediaLink: Specify the location of the VHD file that is created.
	* sourceImageName: Specify the name of the image to use to create the Virtual Machine. You can get the image name by `azure vm image list`. For more information about image searching, see [Navigate and select VM images](/documentation/articles/resource-groups-vm-searching).

- roleSize: Specify the size of the Virtual Machine. You can use `azure vm location list --json` to view the available "virtualMachinesRoleSizes".

For more information about each field, Check the request body of the REST API for [Create Virtual Machine Deployment](https://msdn.microsoft.com/zh-cn/library/azure/jj157194.aspx). The structure of the json file is exactly the same as the request body, except that the request body is xml, and each field name starts with a uppercase letter, while `azure vm create-from` use a json file, and each field name starts with a lowercase letter.

After a while you will see the following output:

		info:    Executing command vm create-from
	+ Looking up cloud service
	info:    cloud service myubuntu not found.
	+ Creating cloud service
	+ Creating VM
	info:    vm create-from command OK

You can use `azure vm show <you-vm-name>` to get the status of your virtual machine. You will get output that looks like this:

	info:    Executing command vm show
	+ Getting virtual machines
	data:    DNSName "myubuntu.chinacloudapp.cn"
	data:    Location "China East"
	data:    VMName "myubuntu"
	data:    IPAddress "<private ip>"
	data:    InstanceStatus "ReadyRole"
	data:    InstanceSize "Basic_A0"
	data:    Image "b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140416.1-en-us-30GB"
	data:    OSDisk hostCaching "ReadWrite"
	data:    OSDisk name "myubuntu-myubuntu-0-201601070618550344"
	data:    OSDisk mediaLink "https://<storageaccountname>.blob.core.chinacloudapi.cn/vhds/myubuntu-myubuntu-2016-02-19.vhd"
	data:    OSDisk sourceImageName "b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140416.1-en-us-30GB"
	data:    OSDisk operatingSystem "Linux"
	data:    OSDisk iOType "Standard"
	data:    ReservedIPName ""
	data:    VirtualIPAddresses 0 address "<public ip>"
	data:    VirtualIPAddresses 0 name "myubuntuContractContract"
	data:    VirtualIPAddresses 0 isDnsProgrammed true
	data:    Network Endpoints 0 localPort 22
	data:    Network Endpoints 0 name "SSH"
	data:    Network Endpoints 0 port 22
	data:    Network Endpoints 0 protocol "tcp"
	data:    Network Endpoints 0 virtualIPAddress "<public ip>"
	data:    Network Endpoints 0 enableDirectServerReturn false

If you see `InstanceStatus "ReadyRole"`, your VM is up and running and waiting for you to connect.

## Connect to the Linux virtual machine

With Linux virtual machines, you typically connect using **ssh**. 

> [AZURE.NOTE] This topic connects to a VM using usernames and passwords; to use public and private key pairs to communicate with your VM, see [How to Use SSH with Linux on Azure](/documentation/articles/virtual-machines-linux-use-ssh-key). You can modify the **SSH**

If you're not familiar with connecting with **ssh**, the command takes the form `ssh <username>@<publicdnsaddress> -p <the ssh port>`. In this case, we use the username and password from the previous step and port 22, which is the default **ssh** port.

	ssh ops@myuni-westu-1432328437727-pip.chinanorth.chinacloudapp.cn -p 22
	The authenticity of host 'myuni-westu-1432328437727-pip.chinanorth.chinacloudapp.cn (191.239.51.1)' can't be established.
	ECDSA key fingerprint is bx:xx:xx:xx:xx:xx:xx:xx:xx:x:x:x:x:x:x:xx.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added 'myuni-westu-1432328437727-pip.chinanorth.chinacloudapp.cn,191.239.51.1' (ECDSA) to the list of known hosts.
	ops@myuni-westu-1432328437727-pip.chinanorth.chinacloudapp.cn's password:
	Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.16.0-37-generic x86_64)

	 * Documentation:  https://help.ubuntu.com/

	  System information as of Fri May 22 21:02:32 UTC 2015

	  System load: 0.37              Memory usage: 2%   Processes:       207
	  Usage of /:  41.4% of 1.94GB   Swap usage:   0%   Users logged in: 0

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

	ops@myuniquevmname:~$

Now that you're connected to your VM, you're ready to attach a disk.

## Attach and mount a disk

Attaching a new disk is quick. Just type `azure vm disk attach-new <myuniquegroupname> <myuniqto create and attach [blob-url]` to create and att  a new GB disk for your VM. It should look something like this:


	azure vm disk attach-new <you-vm-name> 5 https://<storageAccoutName>.blob.core.chinacloudapi.cn/vhds/temp.vhd
	info:    Executing command vm disk attach-new

	+ Getting virtual machines
	+ Adding Data-Disk
	info:    vm disk attach-new command OK


Now let's find the disk, using `dmesg | grep SCSI` (the method you use to discover your new disk may vary). In this case, it looks something like:

	dmesg | grep SCSI
	[    0.294784] SCSI subsystem initialized
	[    0.573458] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
	[    7.110271] sd 2:0:0:0: [sda] Attached SCSI disk
	[    8.079653] sd 3:0:1:0: [sdb] Attached SCSI disk
	[ 1828.162306] sd 5:0:0:0: [sdc] Attached SCSI disk

and in the case of this topic, the `sdc` disk is the one that we want. Now partition the disk with `sudo fdisk /dev/sdc` -- assuming that in your case the disk was `sdc`, and make it a primary disk on partition 1, and accept the other defaults.

	sudo fdisk /dev/sdc
	Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel
	Building a new DOS disklabel with disk identifier 0x2a59b123.
	Changes will remain in memory only, until you decide to write them.
	After that, of course, the previous content won't be recoverable.

	Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite)

	Command (m for help): n
	Partition type:
	   p   primary (0 primary, 0 extended, 4 free)
	   e   extended
	Select (default p): p
	Partition number (1-4, default 1): 1
	First sector (2048-10485759, default 2048):
	Using default value 2048
	Last sector, +sectors or +size{K,M,G} (2048-10485759, default 10485759):
	Using default value 10485759

Create the partition by typing `p` at the prompt:

	Command (m for help): p

	Disk /dev/sdc: 5368 MB, 5368709120 bytes
	255 heads, 63 sectors/track, 652 cylinders, total 10485760 sectors
	Units = sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disk identifier: 0x2a59b123

	   Device Boot      Start         End      Blocks   Id  System
	/dev/sdc1            2048    10485759     5241856   83  Linux

	Command (m for help): w
	The partition table has been altered!

	Calling ioctl() to re-read partition table.
	Syncing disks.

And write a file system to the partition by using the **mkfs** command, specifying your filesystem type and the device name. In this topic, we're using `ext4` and `/dev/sdc1` from above:

	sudo mkfs -t ext4 /dev/sdc1
	mke2fs 1.42.9 (4-Feb-2014)
	Discarding device blocks: done
	Filesystem label=
	OS type: Linux
	Block size=4096 (log=2)
	Fragment size=4096 (log=2)
	Stride=0 blocks, Stripe width=0 blocks
	327680 inodes, 1310464 blocks
	65523 blocks (5.00%) reserved for the super user
	First data block=0
	Maximum filesystem blocks=1342177280
	40 block groups
	32768 blocks per group, 32768 fragments per group
	8192 inodes per group
	Superblock backups stored on blocks:
		32768, 98304, 163840, 229376, 294912, 819200, 884736

	Allocating group tables: done
	Writing inode tables: done
	Creating journal (32768 blocks): done
	Writing superblocks and filesystem accounting information: done

Now we create a directory to mount the file system using `mkdir`:

	sudo mkdir /datadrive

And you mount the directory using `mount`:

	sudo mount /dev/sdc1 /datadrive

The data disk is now ready to use as `/datadrive`.

	ls
	bin   datadrive  etc   initrd.img  lib64       media  opt   root  sbin  sys  usr  vmlinuz
	boot  dev        home  lib         lost+found  mnt    proc  run   srv   tmp  var

> [AZURE.NOTE] You can also connect to your Linux virtual machine using an SSH key for identification. For details, see [How to Use SSH with Linux on Azure](/documentation/articles/virtual-machines-linux-use-ssh-key).

## Next Steps

Remember, that your new disk will not typically be available to the VM if it reboots unless you write that information to your [fstab](http://en.wikipedia.org/wiki/Fstab) file. If you want, you can add several more disks and [configure RAID](/documentation/articles/virtual-machines-linux-configure-raid). 

To learn more about Linux on Azure, see:

- [Linux and Open-Source Computing on Azure](/documentation/articles/virtual-machines-linux-opensource)

- [How to use the Azure Command-Line Interface](/documentation/articles/virtual-machines-command-line-tools)

- [Deploy a LAMP app using the Azure CustomScript Extension for Linux](/documentation/articles/virtual-machines-linux-script-lamp)

- [The Docker Virtual Machine Extension for Linux on Azure](/documentation/articles/virtual-machines-docker-vm-extension)
