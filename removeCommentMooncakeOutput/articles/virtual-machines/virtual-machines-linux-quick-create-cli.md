<!-- ARM: tested -->

<properties
   pageTitle="Create a Linux VM on Azure using the CLI | Azure"
   description="Create a Linux VM on Azure using the CLI."
   services="virtual-machines-linux"
   documentationCenter=""
   authors="vlivech"
   manager="timlt"
   editor=""/>

<tags
	ms.service="virtual-machines-linux"
	ms.date="05/03/2016"
	wacn.date=""/>


# Create a Linux VM on Azure using the CLI

[AZURE.INCLUDE [arm-api-version-cli](../includes/arm-api-version-cli.md)]

This article shows how to quickly deploy a Linux Virtual Machine on Azure using the Azure CLI's `azure vm quick-create` command. The `quick-create` command deploys a VM with a basic infrastructure surrounding it that you can use to prototype or test a concept very rapidly (you can think of it as the quickest way to a Linux bash shel)l.  The article requires an Azure account ([get a trial](/pricing/1rmb-trial/)), and [the Azure CLI](/documentation/articles/xplat-cli-install/) logged in (`azure login -e AzureChinaCloud`) and in resource manager mode (`azure config mode arm`).  You can also quickly deploy a Linux VM using the [Azure Portal](/documentation/articles/virtual-machines-linux-quick-create-portal/).

## Quick Command Summary

One command to deploy a CoreOS VM and attach your SSH key:

```bash
azure vm quick-create -M ~/.ssh/azure_id_rsa.pub -Q OpenLogic:Centos:7.2:latest
```

## Deploy the Linux VM

Using the same command from above, the following shows each prompt along with the output you should expect to see.  

## Use an ImageUR

The following table lists the distribution Linux (as of Azure CLI version 0.9).

| Publisher | Offer        | SKU         | Version |
|:----------|:-------------|:------------|:--------|
| OpenLogic | Centos       | 7.2         | latest  |
| SUSE      | openSUSE     | 13.2        | latest  |
| Canonical | UbuntuServer | 14.04.3-LTS | latest  |



For the **ImageURN** option (`-Q`) we will use `Canonical:UbuntuServer:14.04.3-LTS:latest` to deploy a Canonical Ubuntu 14.04.3-LTS. (These 3 images represent a tiny portion of the available OS on Azure; find more images in the marketplace by [searching for an image](/documentation/articles/virtual-machines-linux-cli-ps-findimage/), or you can [upload your own custom image](/documentation/articles/virtual-machines-linux-create-upload-generic/).)

In the following command walk through, please replace the prompts with values from your own environment, we are using "example" values.  

Follow the prompts and enter your own names

```bash
azure vm quick-create -M ~/.ssh/id_rsa.pub -Q Canonical:UbuntuServer:14.04.3-LTS:latest
```

The output should look like the following output block.

```bash
info:    Executing command vm quick-create
Resource group name: rhel-quick
Virtual machine name: rhel
Location name: chinanorth
Operating system Type [Windows, Linux]: linux
User name: ops
+ Listing virtual machine sizes available in the location "chinanorth"
+ Looking up the VM "rhel"
info:    Verifying the public key SSH file: /Users/ops/.ssh/id_rsa.pub
info:    Using the VM Size "Standard_D1"
info:    The [OS, Data] Disk or image configuration requires storage account
+ Looking up the storage account cli1630678171193501687
info:    Could not find the storage account "cli1630678171193501687", trying to create new one
+ Creating storage account "cli1630678171193501687" in "chinanorth"
+ Looking up the storage account cli1630678171193501687
+ Looking up the NIC "rhel-china-1630678171-nic"
info:    An nic with given name "rhel-china-1630678171-nic" not found, creating a new one
+ Looking up the virtual network "rhel-china-1630678171-vnet"
info:    Preparing to create new virtual network and subnet
+ Creating a new virtual network "rhel-china-1630678171-vnet" [address prefix: "10.0.0.0/16"] with subnet "rhel-china-1630678171-snet" [address prefix: "10.0.1.0/24"]
+ Looking up the virtual network "rhel-china-1630678171-vnet"
+ Looking up the subnet "rhel-china-1630678171-snet" under the virtual network "rhel-china-1630678171-vnet"
info:    Found public ip parameters, trying to setup PublicIP profile
+ Looking up the public ip "rhel-china-1630678171-pip"
info:    PublicIP with given name "rhel-china-1630678171-pip" not found, creating a new one
+ Creating public ip "rhel-china-1630678171-pip"
+ Looking up the public ip "rhel-china-1630678171-pip"
+ Creating NIC "rhel-china-1630678171-nic"
+ Looking up the NIC "rhel-china-1630678171-nic"
+ Looking up the storage account clisto909893658rhel
+ Creating VM "rhel"
+ Looking up the VM "rhel"
+ Looking up the NIC "rhel-china-1630678171-nic"
+ Looking up the public ip "rhel-china-1630678171-pip"
data:    Id                              :/subscriptions/<guid>/resourceGroups/rhel-quick/providers/Microsoft.Compute/virtualMachines/rhel
data:    ProvisioningState               :Succeeded
data:    Name                            :rhel
data:    Location                        :chinanorth
data:    Type                            :Microsoft.Compute/virtualMachines
data:
data:    Hardware Profile:
data:      Size                          :Standard_D1
data:
data:    Storage Profile:
data:      Image reference:
data:        Publisher                   :Canonical
data:        Offer                       :UbuntuServer
data:        Sku                         :14.04.3-LTS
data:        Version                     :latest
data:
data:      OS Disk:
data:        OSType                      :Linux
data:        Name                        :clic5abbc145c0242c1-os-1462425492101
data:        Caching                     :ReadWrite
data:        CreateOption                :FromImage
data:        Vhd:
data:          Uri                       :https://cli1630678171193501687.blob.core.chinacloudapi.cn/vhds/clic5abbc145c0242c1-os-1462425492101.vhd
data:
data:    OS Profile:
data:      Computer Name                 :rhel
data:      User Name                     :ops
data:      Linux Configuration:
data:        Disable Password Auth       :true
data:
data:    Network Profile:
data:      Network Interfaces:
data:        Network Interface #1:
data:          Primary                   :true
data:          MAC Address               :00-0D-3A-32-0F-DD
data:          Provisioning State        :Succeeded
data:          Name                      :rhel-china-1630678171-nic
data:          Location                  :chinanorth
data:            Public IP address       :104.42.236.196
data:            FQDN                    :rhel-china-1630678171-pip.chinanorth.chinacloudapp.cn
data:
data:    Diagnostics Profile:
data:      BootDiagnostics Enabled       :true
data:      BootDiagnostics StorageUri    :https://clisto909893658rhel.blob.core.chinacloudapi.cn/
data:
data:      Diagnostics Instance View:
info:    vm quick-create command OK
```

You can now SSH into your VM on the default SSH port 22 and the fully qualified domain name (FQDN) listed in the output above. (You can also use the IP address listed.)

```bash
ssh ops@rhel-china-1630678171-pip.chinanorth.chinacloudapp.cn
```
The login process should look something like the following:

```bash
The authenticity of host 'rhel-china-1630678171-pip.chinanorth.chinacloudapp.cn (104.42.236.196)' can't be established.
RSA key fingerprint is 0e:81:c4:36:2d:eb:3c:5a:dc:7e:65:8a:3f:3e:b0:cb.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'rhel-china-1630678171-pip.chinanorth.chinacloudapp.cn,104.42.236.196' (RSA) to the list of known hosts.
[ops@rhel ~]$ ls -a
.  ..  .bash_logout  .bash_profile  .bashrc  .cache  .config  .ssh
```

## Next Steps

The `azure vm quick-create` is the way to quickly deploy a VM so you can log in  to a bash shell and get working. Using `vm quick-create` does not give you the additional benefits of a complex environment.  To deploy a Linux VM customized for your infrastructure you can follow any of the articles below.

- [Use an Azure resource manager template to create a specific deployment](/documentation/articles/virtual-machines-linux-cli-deploy-templates/)
- [Create your own custom environment for a Linux VM using Azure CLI commands directly](/documentation/articles/virtual-machines-linux-create-cli-complete/).
- [Create a SSH Secured Linux VM on Azure using Templates](/documentation/articles/virtual-machines-linux-create-ssh-secured-vm-from-template/)

Those articles will get you started in building an Azure infrastructure as well as any number of proprietary and open-source infrastructure deployment, configuration, and orchestration tools.
