<properties
    pageTitle="Manage reserved IP addresses (Classic) using PowerShell | Azure"
    description="Understand reserved IP addresses (Classic) and how to manage them using PowerShell."
    services="virtual-network"
    documentationcenter="na"
    author="jimdial"
    manager="carmonm"
    editor="tysonn" />
<tags
    ms.assetid="34652a55-3ab8-4c2d-8fb2-43684033b191"
    ms.service="virtual-network"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="02/10/2016"
    wacn.date=""
    ms.author="jdial" />

# Reserved IP addresses (Classic)
> [AZURE.SELECTOR]
- [Azure portal preview](/documentation/articles/virtual-network-deploy-static-pip-arm-portal/)
- [PowerShell](/documentation/articles/virtual-network-deploy-static-pip-arm-ps/)
- [Azure CLI](/documentation/articles/virtual-network-deploy-static-pip-arm-cli/)
- [Template](/documentation/articles/virtual-network-deploy-static-pip-arm-template/)
- [PowerShell (Classic)](/documentation/articles/virtual-networks-reserved-public-ip/)

IP addresses in Azure fall into two categories: dynamic and reserved. Public IP addresses managed by Azure are dynamic by default. That means that the IP address used for a given cloud service (VIP) or to access a VM or role instance directly (ILPIP) can change from time to time, when resources are shutdown or deallocated.

To prevent IP addresses from changing, you can reserve an IP address. Reserved IPs can be used only as a VIP, ensuring that the IP address for the cloud service will be the same even as resources are shutdown or deallocated. Furthermore, you can convert existing dynamic IPs used as a VIP to a reserved IP address.

> [AZURE.IMPORTANT]
> Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/). This article covers using the classic deployment model. Azure recommends that most new deployments use the Resource Manager model. Learn how to reserve a static public IP address using the [Resource Manager deployment model](/documentation/articles/virtual-network-ip-addresses-overview-arm/).

To learn more about IP addresses in Azure, read the [IP addresses](/documentation/articles/virtual-network-ip-addresses-overview-classic/) article.

## When do I need a reserved IP?
* **You want to ensure that the IP is reserved in your subscription**. If you want to reserve an IP address that will not be released from your subscription under any circumstance, you should use a reserved public IP.  
* **You want your IP to stay with your cloud service even across stopped or deallocated state (VMs)**. If you want your service to be accessed by using an IP address that will not change even when VMs in the cloud service are stop or deallocated.
* **You want to ensure that outbound traffic from Azure uses a predictable IP address**. You may have your on-premises firewall configured to allow only traffic from specific IP addresses. By reserving an IP, you will know the source IP address and won't have to update your firewall rules due to an IP change.

## FAQ
1. Can I use a reserved IP for all Azure services?  
   * Reserved IPs can only be used for VMs and cloud service instance roles exposed through a VIP.
2. How many reserved IPs can I have?  
   * See the [Azure limits](/documentation/articles/azure-subscription-service-limits/#networking-limits) article.
3. Is there a charge for reserved IPs?
   * See [Reserved IP Address Pricing Details](/pricing/details/reserved-ip-addresses/) for pricing information.
4. How do I reserve an IP address?
   * You can use PowerShell, the [Azure Management REST API](https://msdn.microsoft.com/zh-cn/library/azure/dn722420.aspx), or the [Azure portal preview](https://portal.azure.cn) to reserve an IP address in a particular region. This reserved IP address is associated to your subscription.
5. Can I use this with affinity group based VNets?
   * Reserved IPs are only supported in regional VNets. It is not supported for VNets that are associated with affinity groups. For more information about associating a VNet with a region or an affinity group, see [About Regional VNets and Affinity Groups](/documentation/articles/virtual-networks-migrate-to-regional-vnet/).

## Manage reserved VIPs

Ensure you have installed and configured PowerShell by completing the steps in the [Install and configure PowerShell](/documentation/articles/powershell-install-configure/) article. 

Before you can use reserved IPs, you must add it to your subscription. To create a reserved IP from the pool of public IP addresses available in the *China North* location, run the following command:

    New-AzureReservedIP -ReservedIPName MyReservedIP -Location "China North"

Notice, however, that you cannot specify what IP is being reserved. To view what IP addresses are reserved in your subscription, run the following PowerShell command, and notice the values for *ReservedIPName* and *Address*:

    Get-AzureReservedIP

Expected output:

    ReservedIPName       : MyReservedIP
    Address              : 23.101.114.211
    Id                   : d73be9dd-db12-4b5e-98c8-bc62e7c42041
    Label                :
    Location             : China North
    State                : Created
    InUse                : False
    ServiceName          :
    DeploymentName       :
    OperationDescription : Get-AzureReservedIP
    OperationId          : 55e4f245-82e4-9c66-9bd8-273e815ce30a
    OperationStatus      : Succeeded

Once an IP is reserved, it remains associated to your subscription until you delete it. To delete the reserved IP shown above, run the following PowerShell command:

    Remove-AzureReservedIP -ReservedIPName "MyReservedIP"

## Reserve the IP address of an existing cloud service
You can reserve the IP address of an existing cloud service by adding the `-ServiceName` parameter. To reserve the IP address of a cloud service *TestService* in the *China North* location, run the following PowerShell command:

    New-AzureReservedIP -ReservedIPName MyReservedIP -Location "China North" -ServiceName TestService

## Associate a reserved IP to a new cloud service
The script below creates a new reserved IP, then associates it to a new cloud service named *TestService*.

    New-AzureReservedIP -ReservedIPName MyReservedIP -Location "China North"

    $image = Get-AzureVMImage|?{$_.ImageName -like "*RightImage-Windows-2012R2-x64*"}

    New-AzureVMConfig -Name TestVM -InstanceSize Small -ImageName $image.ImageName `
    | Add-AzureProvisioningConfig -Windows -AdminUsername adminuser -Password MyP@ssw0rd!! `
    | New-AzureVM -ServiceName TestService -ReservedIPName MyReservedIP -Location "China North"

> [AZURE.NOTE]
> When you create a reserved IP to use with a cloud service, you'll still need to refer to the VM by using *VIP:&lt;port number>* for inbound communication. Reserving an IP does not mean you can connect to the VM directly. The reserved IP is assigned to the cloud service that the VM has been deployed to. If you want to connect to a VM by IP directly, you have to configure an instance-level public IP. An instance-level public IP is a type of public IP (called a ILPIP) that is assigned directly to your VM. It cannot be reserved. See [Instance-level Public IP (ILPIP)](/documentation/articles/virtual-networks-instance-level-public-ip/) for more information.
> 

## Remove a reserved IP from a running deployment
To remove the reserved IP added to the new service created in the script above, run the following PowerShell command:

    Remove-AzureReservedIPAssociation -ReservedIPName MyReservedIP -ServiceName TestService

> [AZURE.NOTE]
> Removing a reserved IP from a running deployment does not remove the reservation from your subscription. It simply frees the IP to be used by another resource in your subscription.
> 

## Associate a reserved IP to a running deployment
The following commands create a new cloud service named *TestService2* with a new VM named *TestVM2*, and then associates the existing reserved IP named *MyReservedIP* to the cloud service:

    $image = Get-AzureVMImage|?{$_.ImageName -like "*RightImage-Windows-2012R2-x64*"}

    New-AzureVMConfig -Name TestVM2 -InstanceSize Small -ImageName $image.ImageName `
    | Add-AzureProvisioningConfig -Windows -AdminUsername adminuser -Password MyP@ssw0rd!! `
    | New-AzureVM -ServiceName TestService2 -Location "China North"

    Set-AzureReservedIPAssociation -ReservedIPName MyReservedIP -ServiceName TestService2

## Associate a reserved IP to a cloud service by using a service configuration file
You can also associate a reserved IP to a cloud service by using a service configuration (CSCFG) file. The sample xml below shows how to configure a cloud service to use a reserved VIP named *MyReservedIP*:

    <?xml version="1.0" encoding="utf-8"?>
    <ServiceConfiguration serviceName="ReservedIPSample" xmlns="http://schemas.microsoft.com/ServiceHosting/2008/10/ServiceConfiguration" osFamily="4" osVersion="*" schemaVersion="2014-01.2.3">
      <Role name="WebRole1">
        <Instances count="1" />
        <ConfigurationSettings>
          <Setting name="Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString" value="UseDevelopmentStorage=true" />
        </ConfigurationSettings>
      </Role>
      <NetworkConfiguration>
        <AddressAssignments>
          <ReservedIPs>
           <ReservedIP name="MyReservedIP"/>
          </ReservedIPs>
        </AddressAssignments>
      </NetworkConfiguration>
    </ServiceConfiguration>

## Next steps
* Understand how [IP addressing](/documentation/articles/virtual-network-ip-addresses-overview-classic/) works in the classic deployment model.
* Learn about [reserved private IP addresses](/documentation/articles/virtual-networks-reserved-private-ip/).
* Learn about [Instance Level Public IP (ILPIP) addresses](/documentation/articles/virtual-networks-instance-level-public-ip/).

