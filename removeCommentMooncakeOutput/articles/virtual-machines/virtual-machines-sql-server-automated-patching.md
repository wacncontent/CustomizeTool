<properties
	pageTitle="Automated SQL Server Patching in VMs | Azure"
	description="Explains the Automated Patching feature for SQL Server Virtual Machines running in Azure."
	services="virtual-machines"
	documentationCenter="na"
	authors="rothja"
	manager="jeffreyg"
	editor="monicar"
	tags="azure-resource-manager" />
<tags
	ms.service="virtual-machines"
	ms.date="02/03/2016"
	wacn.date=""/>

# Automated Patching for SQL Server in Azure Virtual Machines

Automated Patching establishes a maintenance window for an Azure Virtual Machine running SQL Server 2012 or 2014. Automated Updates can only be installed during this maintenance window. For SQL Server, this ensures that system updates and any associated restarts occur at the best possible time for the database. It depends on the SQL Server IaaS Agent.

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)]

## Configure Automated Patching with PowerShell

You can also use PowerShell to configure Automated Patching.

In the following example, PowerShell is used to configure Automated Patching on an existing SQL Server VM. The **New-AzureVMSqlServerAutoPatchingConfig** command configures a new maintenance window for automatic updates.

    $aps = New-AzureVMSqlServerAutoPatchingConfig -Enable -DayOfWeek "Thursday" -MaintenanceWindowStartingHour 11 -MaintenanceWindowDuration 120  -PatchCategory "Important"

    Get-AzureVM -ServiceName <vmservicename> -Name <vmname> | Set-AzureVMSqlServerExtension -AutoPatchingSettings $aps | Update-AzureVM

Based on this example, the following table describes the practical effect on the target Azure VM:

|Parameter|Effect|
|---|---|
|**DayOfWeek**|Patches installed every Thursday.|
|**MaintenanceWindowStartingHour**|Begin updates at 11:00am.|
|**MaintenanceWindowsDuration**|Patches must be installed within 120 minutes. Based on the start time, they must complete by 1:00pm.|
|**PatchCategory**|The only possible setting for this parameter is "Important".|

It could take several minutes to install and configure the SQL Server IaaS Agent.

To disable Automated Patching, run the same script without the -Enable parameter to the New-AzureVMSqlServerAutoPatchingConfig. As with installation, it can take several minutes to disable Automated Patching.

## Disabling and uninstalling the SQL Server IaaS Agent

If you want to disable the SQL Server IaaS Agent for Automated Backup and Patching, use the following command:

    Get-AzureVM -ServiceName <vmservicename> -Name <vmname> | Set-AzureVMSqlServerExtension -Disable | Update-AzureVM

To uninstall the SQL Server IaaS Agent, use the following syntax:

    Get-AzureVM -ServiceName <vmservicename> -Name <vmname> | Set-AzureVMSqlServerExtension -Uninstall | Update-AzureVM

You can also uninstall the extension using the **Remove-AzureVMSqlServerExtension** command:

    Get-AzureVM -ServiceName <vmservicename> -Name <vmname> | Remove-AzureVMSqlServerExtension | Update-AzureVM

## Compatibility

The following products are compatible with the SQL Server IaaS Agent features for Automated Patching:

- Windows Server 2012

- Windows Server 2012 R2

- SQL Server 2012

- SQL Server 2014

## Next steps

A related feature for SQL Server VMs in Azure is [Automated Backup for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-sql-server-automated-backup).

Review other [resources for running SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-sql-server-infrastructure-services).
