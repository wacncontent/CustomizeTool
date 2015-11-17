<properties
   pageTitle="Create a multi-VM deployment with the Azure CLI | Windows Azure"
   description="Learn how to create a multi-VM deployment using the classic deployment model and the Azure CLI."
   services="virtual-machines"
   documentationCenter="nodejs"
   authors="AlanSt"
   manager="timlt"
   editor=""
   tags="azure-service-management"/>

   <tags
	ms.service="virtual-machines"
	ms.date="02/20/2015"
	wacn.date=""/>

# Create a multi-VM deployment with the Azure CLI

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.
 
-->
<!-- keep by customization: begin -->
> [AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-include.md)] This article covers creating resources with the classic deployment model. 
<!-- keep by customization: end -->

The following script will show you how to configure a multi-VM multi-cloud service deployment in a VNET using Azure Command-Line Interface (Azure CLI).

The image below explains how your deployment will look after the script completes:

![](./media/virtual-machines-create-multi-vm-deployment-xplat-cli/multi-vm-xplat-cli.png)

The script creates one VM (**servervm**) in cloud service **servercs** with two data disks attached and two VMs (**clientvm1, clientvm2**) in the cloud service **workercs**. Both the cloud services are placed in the VNET **samplevnet**. The **servercs** cloud service also has an endpoint configured for external connectivity.

## CLI script to make it happen
The code to set this up is relatively straightforward:

>[AZURE.NOTE] You will likely need to change the cloud service names servercs and workercs to be unique cloud service names

    azure network vnet create samplevnet -l "China North"
    azure vm create -l "China North" -w samplevnet -e 10000 -z Small -n servervm servercs b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_10-amd64-server-20150202-en-us-30GB azureuser Password@1
    azure vm create -l "China North" -w samplevnet -e 10001 -z Small –n clientvm1 clientcs b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_10-amd64-server-20150202-en-us-30GB azureuser Password@1
    azure vm create -l "China North" -w samplevnet -e 10002 -c -z Small -n clientvm2 clientcs b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_10-amd64-server-20150202-en-us-30GB azureuser Password@1
    azure vm disk attach-new servervm 100
    azure vm disk attach-new servervm 500
    azure vm endpoint create servervm 443 443 -n https -o tcp

As is the code to tear it down:

    azure vm delete -b -q servervm
    azure vm delete -b -q clientvm1
    azure vm delete -b -q clientvm2
    azure network vnet delete -q samplevnet

*The –q option suppresses the interactive confirmation for deleting objects, -b cleans up the disks / blobs associated with the VM.*

## Generic forms of the commands used

While you can find more information by using the –help option on any of the Azure CLI commands, the generic form of each command as used above is:

    azure network vnet create -l <Region> <VNet_name>
    azure network vnet delete -q <VNet_name>

    azure vm create -l <Region> -w <Vnet_name> -e <SSH_port> -z <VM_size> -n <VM_name> <Cloud_service_name> <VM_image> <Username> <Password>
    azure vm delete -b -q <VM_name>
    azure vm disk attach-new <VM_name>
    azure vm endpoint create <VM_name> <External_port> <Internal_port> -n <Endpoint_name> -o <TCP/UDP>

## Next steps


* [Linux and open-source computing on Azure](/documentation/articles/virtual-machines-linux-opensource)
* [How to log on to a virtual machine running Linux](/documentation/articles/virtual-machines-linux-how-to-log-on)
 