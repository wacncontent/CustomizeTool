<properties
	pageTitle="Create and configure a VM | Windows Azure"
	description="Create and configure an Azure virtual machine with the Powershell and the Resource Manager deployment model."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/08/2015"
	wacn.date=""/>

# Create and <!-- deleted by customization configure --><!-- keep by customization: begin --> preconfigure <!-- keep by customization: end --> a Windows Virtual Machine with Resource Manager and Azure PowerShell

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] [classic deployment model](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms).

These steps show you how to construct a set of Azure PowerShell commands to create and configure an Azure virtual machine. You can use this building block process to quickly create a command set for a new Windows-based virtual machine and expand an existing deployment. You can also use it to create multiple command sets that quickly build out a custom dev/test or IT pro environment.
-->
<!-- keep by customization: begin -->
These steps show you how to construct a set of commands in the Resource Manager mode of Azure PowerShell that create and pre-configure a Windows-based Azure virtual machine. You can use this building block process to quickly create a command set for a new Windows-based virtual machine and expand an existing deployment. You can also use it to create multiple command sets that quickly build out a custom dev/test or IT pro environment.
<!-- keep by customization: end -->

These steps follow a fill-in-the-blanks approach for creating Azure PowerShell command sets. This approach can be useful if you are new to PowerShell or you just want to know what values to specify for successful configuration. If you are an advanced PowerShell user, you can take the commands and substitute your own values for the variables (the lines beginning with "$")

<!-- keep by customization: begin -->
[AZURE.INCLUDE [resource-manager-pointer-to-service-management](../includes/resource-manager-pointer-to-service-management.md)]

- [Use Azure PowerShell to create and preconfigure Windows-based Virtual Machines](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)

<!-- keep by customization: end -->
## Step 1: Install Azure PowerShell

You must also have Azure PowerShell version <!-- deleted by customization 1.0.0 --><!-- keep by customization: begin --> 0.9.0 <!-- keep by customization: end --> or later. If you have not installed and configured Azure PowerShell, click [here](/documentation/articles/powershell-install-configure) for instructions.

You can check the version of Azure PowerShell that you have installed with this command at the Azure PowerShell prompt.

	Get-Module azure | format-table version

Here is an example.

	Version
	-------
<!-- deleted by customization
	1.0.0

If you do not have Version 1.0.0 or later, you must remove Azure PowerShell using  Programs and Features from the Control Panel and then install the latest version. See [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure) for more information.
-->
<!-- keep by customization: begin -->
	0.9.0

If you do not have Version 0.9.0 or later, you must remove Azure PowerShell using the Programs and Features  Control Panel and then install the latest version. See [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure) for more information.
<!-- keep by customization: end -->

## Step 2: Set your subscription

First, <!-- deleted by customization start --><!-- keep by customization: begin --> run <!-- keep by customization: end --> an Azure PowerShell prompt.

<!-- deleted by customization
Login to your account.
	
	Login-AzureRmAccount

Get your subscription name using the following command.

	Get-AzureSubscription | Sort SubscriptionName | Select SubscriptionName

Set your Azure subscription. Replace everything within the quotes, including the < and > characters, with the correct names.
-->
<!-- keep by customization: begin -->
Next, set your Azure subscription by running these commands at the Azure PowerShell prompt. Replace everything within the quotes, including the < and > characters, with the correct names.
<!-- keep by customization: end -->

	$subscr="<subscription name>"
	Select-AzureSubscription -SubscriptionName $subscr –Current

<!-- deleted by customization

## Step 3: Create  resources

In this section we will show you how to create each resource for your new virtual machine.

### Resource group


VMs created using the Resource Manager deployment model require a resource group. If needed, create a new resource group for your new virtual machine. Replace everything within the quotes, including the < and > characters, with the correct names.
-->
<!-- keep by customization: begin -->
You can get the correct subscription name from the display of this command.

	Get-AzureSubscription | Sort SubscriptionName | Select SubscriptionName

Next, switch Azure PowerShell into Resource Manager mode.

	Switch-AzureMode AzureResourceManager

## Step 3: Create the required resources

Resource Manager-based virtual machines require a resource group. If needed, create a new resource group for your new virtual machine with these commands. Replace everything within the quotes, including the < and > characters, with the correct names.
<!-- keep by customization: end -->

	$rgName="<resource group name>"
	$locName="<location name, such as China North>"
<!-- deleted by customization
	New-AzureRmResourceGroup -Name $rgName -Location $locName

You can use this command to list your existing resource groups.

	Get-AzureRmResourceGroup | Sort ResourceGroupName | Select ResourceGroupName

To see a list of the Azure locations where you can create Resource Manager-based virtual machines.

	$loc=Get-AzureRmLocation | where { $_.Name –eq "Microsoft.Compute/virtualMachines" }
-->
<!-- keep by customization: begin -->
	New-AzureResourceGroup -Name $rgName -Location $locName

To determine a unique resource group name, use this command to list your existing resource groups.

	Get-AzureResourceGroup | Sort ResourceGroupName | Select ResourceGroupName

To list the Azure locations where you can create Resource Manager-based virtual machines, use these commands.

	$loc=Get-AzureLocation | where { $_.Name –eq "Microsoft.Compute/virtualMachines" }
<!-- keep by customization: end -->
	$loc.Locations

<!-- deleted by customization
### Storage account


VMs created with the Resource Manager deployment model require a Resource Manager-based storage account. If needed, create a new storage account for your new virtual machine with these commands.
-->
<!-- keep by customization: begin -->
Resource Manager-based virtual machines require a Resource Manager-based storage account. If needed, create a new storage account for your new virtual machine with these commands.
<!-- keep by customization: end -->

	$rgName="<resource group name>"
	$locName="<location name, such as China North>"
	$saName="<storage account name>"
	$saType="<storage account type, specify one: Standard_LRS, Standard_GRS, Standard_RAGRS, or Premium_LRS>"
	<!-- deleted by customization New-AzureRmStorageAccount --><!-- keep by customization: begin --> New-AzureStorageAccount <!-- keep by customization: end --> -Name $saName -ResourceGroupName $rgName –Type $saType -Location $locName

You must pick a globally unique name for your storage account that contains only lowercase letters and numbers. You can use this command to list the existing storage accounts.

<!-- deleted by customization
	Get-AzureRmStorageAccount | Sort Name | Select Name

To test whether a chosen storage account name is globally unique, you need to run the **Test-AzureName** command . 

-->
<!-- keep by customization: begin -->
	Get-AzureStorageAccount | Sort Name | Select Name

To test whether a chosen storage account name is globally unique, you need to run the **Test-AzureName** command in the Azure Service Management mode of PowerShell. Use these commands.

	Switch-AzureMode AzureServiceManagement
<!-- keep by customization: end -->
	Test-AzureName -Storage <Proposed storage account name>

If the Test-AzureName command displays "False", your proposed name is unique. <!-- keep by customization: begin -->  When you have determined a unique name, switch Azure PowerShell back to Resource Manager mode with this command. <!-- keep by customization: end -->

<!-- deleted by customization

### Public domain name label


VMs created with the Resource Manager deployment model can use a public domain name label. The label can contain only letters, numbers, and hyphens. The first and last character must be a letter or number.  
-->
<!-- keep by customization: begin -->
	Switch-AzureMode AzureResourceManager

Resource Manager-based virtual machines can use a public domain name label, which can contain only letters, numbers, and hyphens. The first and last character in the field must be a letter or number.  
<!-- keep by customization: end -->

To test whether a chosen domain name label is globally unique, use these commands.

	$domName="<domain name label to test>"
	$loc="<short name of an Azure location, for example, for China North, the short name is westus>"
<!-- deleted by customization
	Test-AzureRmDnsAvailability -DomainQualifiedName $domName -Location $loc
-->
<!-- keep by customization: begin -->
	Get-AzureCheckDnsAvailability -DomainQualifiedName $domName -Location $loc
<!-- keep by customization: end -->

If DNSNameAvailability is "True", your proposed name is globally unique.

<!-- deleted by customization
### Availability set


If needed, create a new availability set for the new virtual machine with these commands.
-->
<!-- keep by customization: begin -->
Resource Manager-based virtual machines can be placed in a Resource Manager-based availability set. If needed, create a new availability set for the new virtual machine with these commands.
<!-- keep by customization: end -->

	$avName="<availability set name>"
	$rgName="<resource group name>"
	$locName="<location name, such as China North>"
<!-- deleted by customization
	New-AzureRmAvailabilitySet –Name $avName –ResourceGroupName $rgName -Location $locName
-->
<!-- keep by customization: begin -->
	New-AzureAvailabilitySet –Name $avName –ResourceGroupName $rgName -Location $locName
<!-- keep by customization: end -->

Use this command to list the existing availability sets.

	<!-- deleted by customization Get-AzureRmAvailabilitySet --><!-- keep by customization: begin --> Get-AzureAvailabilitySet <!-- keep by customization: end --> –ResourceGroupName $rgName | Sort Name | Select Name

<!-- deleted by customization
### NAT rules	
	
-->
Resource Manager-based virtual machines can be configured with inbound NAT rules to allow incoming traffic from the Internet and be placed in a load balanced set. In both cases, you must specify a load balancer instance and other settings. For more information, see [Create a load balancer using Azure Resource Manager](/documentation/articles/load-balancer-arm-powershell).

<!-- deleted by customization
VMs created with the Resource Manager deployment model require a Resource Manager virtual network. If needed, create a new Resource Manager-based virtual network with at least one subnet for the new virtual machine. Here is an example for a new virtual network named **TestNet** with two subnets named **frontendSubnet** and **backendSubnet**.
-->
<!-- keep by customization: begin -->
Resource Manager-based virtual machines require a Resource Manager-based virtual network. If needed, create a new Resource Manager-based virtual network with at least one subnet for the new virtual machine. Here is an example for a new virtual network with two subnets named frontendSubnet and backendSubnet.
<!-- keep by customization: end -->

	$rgName="LOBServers"
	$locName="China North"
<!-- deleted by customization
	$frontendSubnet=New-AzureRmVirtualNetworkSubnetConfig -Name frontendSubnet -AddressPrefix 10.0.1.0/24
	$backendSubnet=New-AzureRmVirtualNetworkSubnetConfig -Name backendSubnet -AddressPrefix 10.0.2.0/24
	New-AzureRmVirtualNetwork -Name TestNet -ResourceGroupName $rgName -Location $locName -AddressPrefix 10.0.0.0/16 -Subnet $frontendSubnet,$backendSubnet
-->
<!-- keep by customization: begin -->
	$frontendSubnet=New-AzureVirtualNetworkSubnetConfig -Name frontendSubnet -AddressPrefix 10.0.1.0/24
	$backendSubnet=New-AzureVirtualNetworkSubnetConfig -Name backendSubnet -AddressPrefix 10.0.2.0/24
	New-AzurevirtualNetwork -Name TestNet -ResourceGroupName $rgName -Location $locName -AddressPrefix 10.0.0.0/16 -Subnet $frontendSubnet,$backendSubnet
<!-- keep by customization: end -->

Use these commands to list the existing virtual networks.

	$rgName="<resource group name>"
	<!-- deleted by customization Get-AzureRmVirtualNetwork --><!-- keep by customization: begin --> Get-AzureVirtualNetwork <!-- keep by customization: end --> -ResourceGroupName $rgName | Sort Name | Select Name

## Step 4: Build your command set

Open a fresh instance of the text editor of your choice or the PowerShell Integrated Scripting Environment (ISE) and copy the following lines to start your command set. Specify the name of the resource group, Azure location, and storage account for this new virtual machine. Replace everything within the quotes, including the < and > characters, with the correct names.

<!-- keep by customization: begin -->
	Switch-AzureMode AzureResourceManager
<!-- keep by customization: end -->
	$rgName="<resource group name>"
	$locName="<Azure location, such as China North>"
	$saName="<storage account name>"

You must specify the name of a Resource Manager-based virtual network and the index number of a subnet in the virtual network.  Use these commands to list the subnets for a virtual network.

	$rgName="<resource group name>"
	$vnetName="<virtual network name>"
	<!-- deleted by customization Get-AzureRmVirtualNetwork --><!-- keep by customization: begin --> Get-AzureVirtualNetwork <!-- keep by customization: end --> -Name $vnetName -ResourceGroupName $rgName | Select Subnets

The subnet index is the number of the subnet in the display of this command, numbering them consecutively from left to right and starting at 0.

For this example:

	PS C:\> <!-- deleted by customization Get-AzureRmVirtualNetwork --><!-- keep by customization: begin --> Get-AzureVirtualNetwork <!-- keep by customization: end --> -Name TestNet -ResourceGroupName LOBServers | Select Subnets

	Subnets
	-------
	{frontendSubnet, backendSubnet}

The subnet index for the frontendSubnet is 0 and the subnet index for the backendSubnet is 1.

Copy these lines to your command set and specify an existing virtual network name and the subnet index for the virtual machine.

	$vnetName="<name of an existing virtual network>"
	$subnetIndex=<index of the subnet on which to create the NIC for the virtual machine>
<!-- deleted by customization
	$vnet=Get-AzureRmVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
-->
<!-- keep by customization: begin -->
	$vnet=Get-AzurevirtualNetwork -Name $vnetName -ResourceGroupName $rgName
<!-- keep by customization: end -->

Next, you create a network interface card (NIC). Copy one of the following options to your command set and fill in the needed information.

### Option 1: Specify a NIC name and assign a public IP address

Copy the following lines to your command set and specify the name for the NIC.

	$nicName="<name of the NIC of the VM>"
	$pip = <!-- deleted by customization New-AzureRmPublicIpAddress --><!-- keep by customization: begin --> New-AzurePublicIpAddress <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -AllocationMethod Dynamic
	$nic = <!-- deleted by customization New-AzureRmNetworkInterface --><!-- keep by customization: begin --> New-AzureNetworkInterface <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -SubnetId $vnet.Subnets[$subnetIndex].Id -PublicIpAddressId $pip.Id

### Option 2: Specify a NIC name and a DNS domain name label

Copy the following lines to your command set and specify the name for the NIC and the globally unique domain name label. <!-- keep by customization: begin --> When you create virtual machines in the Service Management mode of Azure PowerShell, Azure completes these steps automatically. <!-- keep by customization: end -->

	$nicName="<name of the NIC of the VM>"
	$domName="<domain name label>"
	$pip = <!-- deleted by customization New-AzureRmPublicIpAddress --><!-- keep by customization: begin --> New-AzurePublicIpAddress <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -DomainNameLabel $domName -Location $locName -AllocationMethod Dynamic
	$nic = <!-- deleted by customization New-AzureRmNetworkInterface --><!-- keep by customization: begin --> New-AzureNetworkInterface <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -SubnetId $vnet.Subnets[$subnetIndex].Id -PublicIpAddressId $pip.Id

### Option 3: Specify a NIC name and assign a static, private IP address

Copy the following lines to your command set and specify the name for the NIC.

	$nicName="<name of the NIC of the VM>"
	$staticIP="<available static IP address on the subnet>"
	$pip = <!-- deleted by customization New-AzureRmPublicIpAddress --><!-- keep by customization: begin --> New-AzurePublicIpAddress <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -AllocationMethod Dynamic
	$nic = <!-- deleted by customization New-AzureRmNetworkInterface --><!-- keep by customization: begin --> New-AzureNetworkInterface <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -SubnetId $vnet.Subnets[$subnetIndex].Id -PublicIpAddressId $pip.Id -PrivateIpAddress $staticIP

### Option 4: Specify a NIC name and a load balancer instance for an inbound NAT rule.

To create a NIC and add it to a load balancer instance for an inbound NAT rule, you need:

- The name of a previously-created load balancer instance that has an inbound NAT rule for traffic being forwarded to the virtual machine.
- The index number of the back end address pool of the load balancer instance to assign to the NIC.
- The index number of the inbound NAT rule to assign to the NIC.

For information on how to create a load balancer instance with inbound NAT rules, see [Create a load balancer using Azure Resource Manager](/documentation/articles/load-balancer-arm-powershell).

Copy these lines to your command set and specify the needed names and index numbers.

	$nicName="<name of the NIC of the VM>"
	$lbName="<name of the load balancer instance>"
	$bePoolIndex=<index of the back end pool, starting at 0>
	$natRuleIndex=<index of the inbound NAT rule, starting at 0>
<!-- deleted by customization
	$lb=Get-AzureRmLoadBalancer -Name $lbName -ResourceGroupName $rgName
	$nic=New-AzureRmNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $locName -Subnet $vnet.Subnets[$subnetIndex].Id -LoadBalancerBackendAddressPool $lb.BackendAddressPools[$bePoolIndex] -LoadBalancerInboundNatRule $lb.InboundNatRules[$natRuleIndex]
-->
<!-- keep by customization: begin -->
	$lb=Get-AzureLoadBalancer -Name $lbName -ResourceGroupName $rgName 
	$nic=New-AzureNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $locName -Subnet $vnet.Subnets[$subnetIndex].Id -LoadBalancerBackendAddressPool $lb.BackendAddressPools[$bePoolIndex] -LoadBalancerInboundNatRule $lb.InboundNatRules[$natRuleIndex]
<!-- keep by customization: end -->

The $nicName string must be unique for the resource group. A best practice is to incorporate the virtual machine name in the string, such as "LOB07-NIC".

### Option 5: Specify a NIC name and a load balancer instance for a load-balanced set.

To create a NIC and add it to a load balancer instance for a load-balanced set, you need:

- The name of a previously-created load balancer instance that has a rule for the load-balanced traffic.
- The index number of the back end address pool of the load balancer instance to assign to the NIC.

For information on how to create a load balancer instance with rules for load-balanced traffic, see [Create a load balancer using Azure Resource Manager](/documentation/articles/load-balancer-arm-powershell).

Copy these lines to your command set and specify the needed names and index numbers.

	$nicName="<name of the NIC of the VM>"
	$lbName="<name of the load balancer instance>"
	$bePoolIndex=<index of the back end pool, starting at 0>
<!-- deleted by customization
	$lb=Get-AzureRmLoadBalancer -Name $lbName -ResourceGroupName $rgName
	$nic=New-AzureRmNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $locName -Subnet $vnet.Subnets[$subnetIndex].Id -LoadBalancerBackendAddressPool $lb.BackendAddressPools[$bePoolIndex]
-->
<!-- keep by customization: begin -->
	$lb=Get-AzureLoadBalancer -Name $lbName -ResourceGroupName $rgName 
	$nic=New-AzureNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $locName -Subnet $vnet.Subnets[$subnetIndex].Id -LoadBalancerBackendAddressPool $lb.BackendAddressPools[$bePoolIndex]
<!-- keep by customization: end -->

Next, create a local VM object and optionally add it to an availability set. Copy one of the two following options to your command set and fill in the name, size, and availability set name.

Option 1: Specify a virtual machine name and size.

	$vmName="<VM name>"
	$vmSize="<VM size string>"
<!-- deleted by customization
	$vm=New-AzureRmVMConfig -VMName $vmName -VMSize $vmSize
-->
<!-- keep by customization: begin -->
	$vm=New-AzureVMConfig -VMName $vmName -VMSize $vmSize
<!-- keep by customization: end -->

To determine the possible values of the VM size string for option 1, use these commands.

	$locName="<Azure location of your resource group>"
<!-- deleted by customization
	Get-AzureRmVMSize -Location $locName | Select Name
-->
<!-- keep by customization: begin -->
	Get-AzureVMSize -Location $locName | Select Name
<!-- keep by customization: end -->

Option 2: Specify a virtual machine name and size and add it to an availability set.

	$vmName="<VM name>"
	$vmSize="<VM size string>"
	$avName="<availability set name>"
<!-- deleted by customization
	$avSet=Get-AzureRmAvailabilitySet –Name $avName –ResourceGroupName $rgName
	$vm=New-AzureRmVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
-->
<!-- keep by customization: begin -->
	$avSet=Get-AzureAvailabilitySet –Name $avName –ResourceGroupName $rgName
	$vm=New-AzureVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
<!-- keep by customization: end -->

To determine the possible values of the VM size string for option 2, use these commands.

	$rgName="<resource group name>"
	$avName="<availability set name>"
	<!-- deleted by customization Get-AzureRmVMSize --><!-- keep by customization: begin --> Get-AzureVMSize <!-- keep by customization: end --> -ResourceGroupName $rgName -AvailabilitySetName $avName | Select Name

> [AZURE.NOTE] Currently with Resource Manager, you can only add a virtual machine to an availability set during its creation.

To add an additional data disk to the VM, copy these lines to your command set and specify the disk settings.

	$diskSize=<size of the disk in GB>
	$diskLabel="<the label on the disk>"
	$diskName="<name identifier for the disk in Azure storage, such as 21050529-DISK02>"
<!-- deleted by customization
	$storageAcc=Get-AzureRmStorageAccount -ResourceGroupName $rgName -Name $saName
-->
<!-- keep by customization: begin -->
	$storageAcc=Get-AzureStorageAccount -ResourceGroupName $rgName -Name $saName
<!-- keep by customization: end -->
	$vhdURI=$storageAcc.PrimaryEndpoints.Blob.ToString() + "vhds/" + $vmName + $diskName  + ".vhd"
	<!-- deleted by customization Add-AzureRmVMDataDisk --><!-- keep by customization: begin --> Add-AzureVMDataDisk <!-- keep by customization: end --> -VM $vm -Name $diskLabel -DiskSizeInGB $diskSize -VhdUri $vhdURI  -CreateOption empty

Next, you need to determine the publisher, offer, and SKU of the image for your virtual machine. Here is a table of commonly-used, Windows-based images.

|Publisher name | Offer name | SKU name
|:---------------------------------|:-------------------------------------------|:---------------------------------|
|MicrosoftWindowsServer | WindowsServer | 2008-R2-SP1 |
|MicrosoftWindowsServer | WindowsServer | 2012-Datacenter |
|MicrosoftWindowsServer | WindowsServer | 2012-R2-Datacenter |
|MicrosoftDynamicsNAV | DynamicsNAV | 2015 |
|MicrosoftSharePoint | MicrosoftSharePointServer | 2013 |
|MicrosoftSQLServer | SQL2014-WS2012R2 | Enterprise-Optimized-for-DW |
|MicrosoftSQLServer | SQL2014-WS2012R2 | Enterprise-Optimized-for-OLTP |
|MicrosoftWindowsServerEssentials | WindowsServerEssentials | WindowsServerEssentials |
|MicrosoftWindowsServerHPCPack | WindowsServerHPCPack | 2012R2 |

If the virtual machine image you need is not listed, use the instructions <!-- deleted by customization [here](/documentation/articles/resource-groups-vm-searching#powershell) --><!-- keep by customization: begin --> [here](/documentation/articles/resource-groups-vm-searching/#powershell) <!-- keep by customization: end --> to determine the publisher, offer, and SKU names.

Copy these commands to your command set and fill in the publisher, offer, and SKU names.

	$pubName="<Image publisher name>"
	$offerName="<Image offer name>"
	$skuName="<Image SKU name>"
	$cred=Get-Credential -Message "Type the name and password of the local administrator account."
	<!-- deleted by customization $vm=Set-AzureRmVMOperatingSystem --><!-- keep by customization: begin --> $vm=Set-AzureVMOperatingSystem <!-- keep by customization: end --> -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
	<!-- deleted by customization $vm=Set-AzureRmVMSourceImage --><!-- keep by customization: begin --> $vm=Set-AzureVMSourceImage <!-- keep by customization: end --> -VM $vm -PublisherName $pubName -Offer $offerName -Skus $skuName -Version "latest"
<!-- deleted by customization
	$vm=Add-AzureRmVMNetworkInterface -VM $vm -Id $nic.Id
-->
<!-- keep by customization: begin -->
	$vm=Add-AzureVMNetworkInterface -VM $vm -Id $nic.Id
<!-- keep by customization: end -->

Finally, copy these commands to your command set and fill in the name identifier for the operating system disk for the VM.

	$diskName="<name identifier for the disk in Azure storage, such as OSDisk>"
<!-- deleted by customization
	$storageAcc=Get-AzureRmStorageAccount -ResourceGroupName $rgName -Name $saName
-->
<!-- keep by customization: begin -->
	$storageAcc=Get-AzureStorageAccount -ResourceGroupName $rgName -Name $saName
<!-- keep by customization: end -->
	$osDiskUri=$storageAcc.PrimaryEndpoints.Blob.ToString() + "vhds/" + $diskName  + ".vhd"
	<!-- deleted by customization $vm=Set-AzureRmVMOSDisk --><!-- keep by customization: begin --> $vm=Set-AzureVMOSDisk <!-- keep by customization: end --> -VM $vm -Name $diskName -VhdUri $osDiskUri -CreateOption fromImage
<!-- deleted by customization
	New-AzureRmVM -ResourceGroupName $rgName -Location $locName -VM $vm
-->
<!-- keep by customization: begin -->
	New-AzureVM -ResourceGroupName $rgName -Location $locName -VM $vm
<!-- keep by customization: end -->

## Step 5: Run your command set

Review the Azure PowerShell command set you built in <!-- deleted by customization Step 4 in --> your text editor or the PowerShell ISE <!-- keep by customization: begin --> consisting of multiple blocks of commands from Step 4 <!-- keep by customization: end -->. <!-- deleted by customization Make sure --><!-- keep by customization: begin --> Ensure <!-- keep by customization: end --><!-- keep by customization: begin --> that <!-- keep by customization: end --> you have specified all the <!-- keep by customization: begin --> needed <!-- keep by customization: end --> variables and that they have the correct values. Also make sure that you have removed all the < and > characters.

If you have your commands in a text editor, copy the <!-- keep by customization: begin --> command <!-- keep by customization: end --> set to the clipboard and then right-click <!-- deleted by customization in --> your <!-- keep by customization: begin --> open <!-- keep by customization: end --> Azure PowerShell prompt. This will <!-- deleted by customization send --><!-- keep by customization: begin --> issue <!-- keep by customization: end --> the command set as a series of PowerShell commands and create your Azure virtual machine. Alternately, run the command set from the Azure PowerShell ISE.

<!-- deleted by customization
If you want to reuse this information to create additional VMs, you can save this command set as a PowerShell script file (*.ps1).
-->
<!-- keep by customization: begin -->
If you will be creating this virtual machine again or a similar one, you can save this command set as a PowerShell script file (*.ps1).
<!-- keep by customization: end -->

## Example

I need a PowerShell command set to create an additional virtual machine for a web-based line-of-business workload that:

- Is placed in the existing LOBServers resource group
- Uses the Windows Server 2012 R2 Datacenter image
- Has the name LOB07 and is in the existing WEB_AS availability set
- Has a NIC with a public IP address in the FrontEnd subnet (subnet index 0) of the existing AZDatacenter virtual network
- Has an additional data disk of 200 GB

<!-- deleted by customization
Here is the Azure PowerShell command set to create this virtual machine.
-->
<!-- keep by customization: begin -->
Here is the corresponding Azure PowerShell command set to create this virtual machine, based on the process described in Step 4.

	# Switch to the Resource Manager mode
	Switch-AzureMode AzureResourceManager
<!-- keep by customization: end -->

	# Set values for existing resource group and storage account names
	$rgName="LOBServers"
	$locName="China North"
	$saName="contosolobserverssa"

	# Set the existing virtual network and subnet index
	$vnetName="AZDatacenter"
	$subnetIndex=0
<!-- deleted by customization
	$vnet=Get-AzureRMVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
-->
<!-- keep by customization: begin -->
	$vnet=Get-AzurevirtualNetwork -Name $vnetName -ResourceGroupName $rgName
<!-- keep by customization: end -->

	# Create the NIC
	$nicName="LOB07-NIC"
	$domName="contoso-vm-lob07"
	<!-- deleted by customization $pip=New-AzureRmPublicIpAddress --><!-- keep by customization: begin --> $pip=New-AzurePublicIpAddress <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -DomainNameLabel $domName -Location $locName -AllocationMethod Dynamic
	<!-- deleted by customization $nic=New-AzureRmNetworkInterface --><!-- keep by customization: begin --> $nic=New-AzureNetworkInterface <!-- keep by customization: end --> -Name $nicName -ResourceGroupName $rgName -Location $locName -SubnetId $vnet.Subnets[$subnetIndex].Id -PublicIpAddressId $pip.Id

	# Specify the name, size, and existing availability set
	$vmName="LOB07"
	$vmSize="Standard_A3"
	$avName="WEB_AS"
<!-- deleted by customization
	$avSet=Get-AzureRmAvailabilitySet –Name $avName –ResourceGroupName $rgName
	$vm=New-AzureRmVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
-->
<!-- keep by customization: begin -->
	$avSet=Get-AzureAvailabilitySet –Name $avName –ResourceGroupName $rgName
	$vm=New-AzureVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
<!-- keep by customization: end -->

	# Add a 200 GB additional data disk
	$diskSize=200
	$diskLabel="APPStorage"
	$diskName="21050529-DISK02"
<!-- deleted by customization
	$storageAcc=Get-AzureRmStorageAccount -ResourceGroupName $rgName -Name $saName
-->
<!-- keep by customization: begin -->
	$storageAcc=Get-AzureStorageAccount -ResourceGroupName $rgName -Name $saName
<!-- keep by customization: end -->
	$vhdURI=$storageAcc.PrimaryEndpoints.Blob.ToString() + "vhds/" + $vmName + $diskName  + ".vhd"
	<!-- deleted by customization Add-AzureRmVMDataDisk --><!-- keep by customization: begin --> Add-AzureVMDataDisk <!-- keep by customization: end --> -VM $vm -Name $diskLabel -DiskSizeInGB $diskSize -VhdUri $vhdURI -CreateOption empty

	# Specify the image and local administrator account, and then add the NIC
	$pubName="MicrosoftWindowsServer"
	$offerName="WindowsServer"
	$skuName="2012-R2-Datacenter"
	$cred=Get-Credential -Message "Type the name and password of the local administrator account."
	<!-- deleted by customization $vm=Set-AzureRmVMOperatingSystem --><!-- keep by customization: begin --> $vm=Set-AzureVMOperatingSystem <!-- keep by customization: end --> -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
	<!-- deleted by customization $vm=Set-AzureRmVMSourceImage --><!-- keep by customization: begin --> $vm=Set-AzureVMSourceImage <!-- keep by customization: end --> -VM $vm -PublisherName $pubName -Offer $offerName -Skus $skuName -Version "latest"
<!-- deleted by customization
	$vm=Add-AzureRmVMNetworkInterface -VM $vm -Id $nic.Id
-->
<!-- keep by customization: begin -->
	$vm=Add-AzureVMNetworkInterface -VM $vm -Id $nic.Id
<!-- keep by customization: end -->

	# Specify the OS disk name and create the VM
	$diskName="OSDisk"
<!-- deleted by customization
	$storageAcc=Get-AzureRmStorageAccount -ResourceGroupName $rgName -Name $saName
-->
<!-- keep by customization: begin -->
	$storageAcc=Get-AzureStorageAccount -ResourceGroupName $rgName -Name $saName
<!-- keep by customization: end -->
	$osDiskUri=$storageAcc.PrimaryEndpoints.Blob.ToString() + "vhds/" + $vmName + $diskName  + ".vhd"
	<!-- deleted by customization $vm=Set-AzureRmVMOSDisk --><!-- keep by customization: begin --> $vm=Set-AzureVMOSDisk <!-- keep by customization: end --> -VM $vm -Name $diskName -VhdUri $osDiskUri -CreateOption fromImage
<!-- deleted by customization
	New-AzureRmVM -ResourceGroupName $rgName -Location $locName -VM $vm
-->
<!-- keep by customization: begin -->
	New-AzureVM -ResourceGroupName $rgName -Location $locName -VM $vm
<!-- keep by customization: end -->

## Additional Resources

[Azure Compute, Network and Storage Providers under Azure Resource Manager](/documentation/articles/virtual-machines-azurerm-versus-azuresm)

[Azure Resource Manager Overview](/documentation/articles/resource-group-overview)

[Deploy and Manage Azure Virtual Machines using Resource Manager Templates and PowerShell](/documentation/articles/virtual-machines-deploy-rmtemplates-powershell)

[Create a Windows virtual machine with a Resource Manager template and PowerShell](/documentation/articles/virtual-machines-create-windows-powershell-resource-manager-template-simple)

[How to install and configure Azure PowerShell](/documentation/articles/install-configure-powershell)
