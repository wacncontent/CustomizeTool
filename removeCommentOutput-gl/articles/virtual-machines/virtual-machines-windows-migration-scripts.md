<properties
	pageTitle="Clone a classic Virtual Machine to Azure Resource Manager using PowerShell Scripts"
	description="This article shows you how to clone a single classic Virtual Machine to Azure Resource Manager using PowerShell scripts"
	services="virtual-machines-windows"
	documentationCenter=""
	authors="singhkay"
	manager="drewm"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="05/03/2016"
	wacn.date=""/>

# Clone a classic Virtual Machine to Azure Resource Manager using PowerShell Scripts

This article will show you how to use the scripts located at [Azure/classic-iaas-resourcemanager-migration](https://github.com/Azure/classic-iaas-resourcemanager-migration) to clone a **single** classic Virtual Machine to the Azure Resource Manager deployment model.

>[AZURE.IMPORTANT]Cloning with these scripts will cause downtime for your classic Virtual Machine. If you're looking for platform supported migration, please visit 
- [Platform supported migration of IaaS resources from Classic to Azure Resource Manager stack](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager/)
- [Technical Deep Dive on Platform supported migration from Classic to Azure Resource Manager](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager-deep-dive/)
- [Migrate IaaS resources from Classic to Azure Resource Manager using Azure PowerShell](/documentation/articles/virtual-machines-windows-ps-migration-classic-resource-manager/)

## Getting the scripts

>[AZURE.NOTE]The PowerShell scripts are not officially supported by Microsoft Support. Therefore they are open sourced on Github and we're happy to accept PRs for fixes or additional scenarios.

You can either get the scripts by downloading the zip file from the above specified repo or clone the repo using the **either** of the commands below

```
git clone https://github.com/Azure/classic-iaas-resourcemanager-migration.git
```

**OR**

```
git clone git@github.com:Azure/classic-iaas-resourcemanager-migration.git
```

## Import the migration module

The next step is to import the module into your PowerShell session. This can be done with the below command

```
Import-Module .\asm2arm.psd1
```

## Authenticate with the Classic Deployment Model and Azure Resource Manager subscriptions

Before you can clone your classic Virtual Machine, you need to authenticate your PowerShell session to both the Classic Deployment Model and Azure Resource Manager stacks. This can be done with the following cmdlets

```
Add-AzureAccount
Login-AzureRmAccount
```

>[AZURE.IMPORTANT]Make sure default subscriptions are selected using `Select-AzureSubscription` for the Classic Deployment Model and Set-AzureRmContext for Azure Resource Manager

## Using the scripts

### The cmdlets

Importing the module will add the below two cmdlets to your session.

```
Add-AzureSMVmToRM
New-AzureSmToRMDeployment
```

These cmdlets accomplish the below specified functionality.

#### Add-AzureSMVmToRM
- Generates a set of Azure Resource Manager templates and imperative PowerShell scripts (to copy the disk blobs and if the VM has VM Agent Extensions), given a Virtual Machine

>[AZURE.IMPORTANT]If the `-Deploy` switch is specified, this cmdlet calls the `New-AzureSmToRMDeployment` cmdlet to deploy the above generated Azure Resource Manager templates and imperative PowerShell Scripts.

#### New-AzureSmToRMDeployment
- Deploys the templates and imperative PowerShell scripts generated by the `Add-AzureSMVmToRM` cmdlet to start the migration.

### Identify the classic Virtual Machine to clone

This can be done by either storing the classic Virtual Machine state in a variable and passing that on to the `Add-AzureSMVmToRM` cmdlet or using the `ServiceName` and VM `Name` parmaeters directly. Once you identify the classic Virtual Machine, you can use the `Add-AzureSMVmToRM` cmdlet to clone it.

```
$vm = Get-AzureVm -ServiceName acloudservice -Name atestvm
Add-AzureSMVmToRM -VM $vm -ResourceGroupName aresourcegroupname -DiskAction CopyDisks -OutputFileFolder D:\myarmtemplates -AppendTimeStampForFiles -Deploy
```

**OR**

```
Add-AzureSMVmToRM -ServiceName acloudservice -Name atestvm -ResourceGroupName aresourcegroupname -DiskAction CopyDisks -OutputFileFolder D:\myarmtemplates -AppendTimeStampForFiles -Deploy
```

>[AZURE.IMPORTANT]In the above examples since we are using the `-Deploy` switch, use of `New-AzureSmToRMDeployment` cmdlet is not needed.

## How does the migration work with these scripts?

The cmdlets go through steps for cloning the classVM, and generate resources as custom PowerShell hash tables for Storage, Network and Compute resource providers.
Those hash tables representing the resources are appended to an array, later turned into a template by serializing to JSON, and written to a file.

The template creates files depending on the existence of classic Virtual Machine agent extensions and DiskAction option value. Those are all placed in the directory specified by OutputFileFolder parameter. The files are:

1. `<ServiceName>-<VMName>-setup<optional timestamp>.json`: This file represents the resources that are needed to be prepared before the classic Virtual Machine is cloned, and potentially be the same for any subsequent VMs (we do not maintain state between subsequent runs, but since a storage account needs to be provisioned before a blob copy operation happens, which is done imperatively, it was only logical to group like resources into one)

2.  `<ServiceName>-<VMName>-deploy<optional timestamp>.json`: Contains the template for the Resource Manager Virtual Machine
3.  `<ServiceName>-<VMName>-parameters<optional timestamp>.json`: Contains the actual parameters passed to the templates
4.  `<ServiceName>-<VMName>-setextensions<optional timestamp>.json`: a set of PowerShell cmdlets to be run for setting the Virtual Machine agent extensions.
4.  `<ServiceName>-<VMName>-copydisks<optional timestamp>.json`: a set of PowerShell cmdlets to be run for copying disk blobs, if CopyDisks option is specified.

If the -Deploy flag is set, after generating the files, the cmdlet then deploys the <ServiceName>-<VMName>-setup.json template, copies the source Virtual Machine disk blobs if the DiskAction parameter is set to CopyDisks and then deploys the <ServiceName>-<VMName>-deploy.json template, using the <ServiceName>-<VMName>-parameters.json file for parameters. Once the deployment of the Virtual Machine is done, if there is an imperative script (for Virtual Machine agent extensions), or a script for copying the disks, they are executed.

### Network details
The cmdlet's intent is not to clone the classic network settings to Resource Manager. It utilizes the networking facilities in a way that is the most convenient for cloning the Virtual Machine itself. Here is what happens on different conditions:

1.  No virtual network on the target resource group
    - Source Virtual Machine is not on a subnet: A default virtual network with 10.0.0.0/16 is created along with a subnet, with 10.0.0.0/22 address space.
    - Source Virtual Machine is on a subnet: The virtual network the Virtual Machine is on is discovered, the specification of the virtual network, along with the subnets are copied over
2.  Target resource group has a virtual network with a name `<VM virtual network>arm` (the string 'arm' is appended)
    - If the virtual network has a subnet with the same name and address space, use it
    - If no suitable subnet is found, find an address block out of the existing subnets with 22 bits mask and use that one.

## Cloning vs Platform migration

There are a few differences between the current cloning approach versus the platform supported migration. 

### Cloning


| Pros                                                   |                               Cons                               |
|--------------------------------------------------------|:----------------------------------------------------------------:|
| Clone any Virtual Machine within a cloud service       |    Downtime incurred for the VMs as they need to be shutdown     |
| Clone any Virtual Machine in a VNET or outside a VNET  | Long delays in scenario where copying of disk blobs is required  |
|                                                        | Change in network configuration for the VM - Internal IPs, VIPs. |


### Platform migration


| Pros                             |                     Cons                    |
|----------------------------------|:-------------------------------------------:|
| Majority of the VM configurations inside a Virtual Network will not incur downtime. | Either All VMs in a Cloud Service or the VNET with all the resources deployed in it has to be migrated together. |
 
 
## Unsupported scenarios

**Following are not in the scope of the cloning scripts**

 1. Stop a running Virtual Machine 
 2. Change your data/disks
 3. Clone running VMs
 4. Clone multiple VMs in a complex scenario automagically
 5. Clone the entire ASM network configuration
 6. Creates load balanced VMs. We assume this is a configuration the Azure expert needs to handle explicitly
 
 
## Tested configurations

The _Add-AzureSMVmToRM_ cmdlet was validated using the following test cases:

| # | Description |
|:---|:---|
| 1	| Windows Virtual Machine with an existing OS disk |
| 2	| Linux Virtual Machine with an existing OS disk |
| 3	| Windows Virtual Machine with existing OS and data disks |
| 4	| Linux Virtual Machine with existing OS and data disks |
| 5	| Windows Virtual Machine with a new OS disk matched from Image Gallery |
| 6	| Linux Virtual Machine with a new OS disk matched from Image Gallery |
| 7	| Windows Virtual Machine with a new OS disk and empty data disks |
| 8	| Linux Virtual Machine with a new OS disk and empty data disks |
| 9 | Windows Virtual Machine with public endpoints |
| 10 | Linux Virtual Machine with public endpoints |
| 11 | Windows Virtual Machine with a WinRM certificate |
| 12 | Windows Virtual Machine in a Vnet and subnet |
| 13 | Linux Virtual Machine in a Vnet and subnet |
| 14 | Windows Virtual Machine with custom extensions |
| 15 | Windows Virtual Machine in an availability set |
| 16 | Windows Virtual Machine in an availability set, with multiple data disks, public endpoints, in a vnet and subnet, and with custom extensions |
| 17 | Linux Virtual Machine in an availability set, with multiple data disks, public endpoints, in a vnet and subnet, and with custom extensions |

## Notes
1. If multiple VMs are cloned one after the other with short time intervals in between them, there might be DNS name conflicts for the public IP addresses, due to the DNS cache refresh time.
