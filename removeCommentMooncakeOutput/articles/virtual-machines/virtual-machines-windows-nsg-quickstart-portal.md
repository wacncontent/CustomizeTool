<!-- Ibiza portal: tested -->

<properties
   pageTitle="Allow external access to a VM using the portal | Azure"
   description="Learn how to open a port / create an endpoint that allows access to your VM using the resource manager deployment model in the Azure Portal Preview"
   services="virtual-machines-windows"
   documentationCenter=""
   authors="iainfoulds"
   manager="timlt"
   editor=""/>

<tags
	ms.service="virtual-machines-windows"
	ms.date="05/24/2016"
	wacn.date=""/>

# Allow external access to your VM using the Azure Portal Preview
[AZURE.INCLUDE [virtual-machines-common-nsg-quickstart](../includes/virtual-machines-common-nsg-quickstart.md)]

## Quick commands
You can also [perform these steps using Azure PowerShell](/documentation/articles/virtual-machines-windows-nsg-quickstart-powershell/).

First, create your Network Security Group. Select a resource group in the portal, click 'Add', then search for and select 'Network Security Group':

![Add a Network Security Group](./media/virtual-machines-windows-nsg-quickstart-portal/add-nsg.png)

Enter a name for your Network Security Group and select a location:

![Create a Network Security Group](./media/virtual-machines-windows-nsg-quickstart-portal/create-nsg.png)

Select your new Network Security Group. You now create an inbound rule:

![Add an inbound rule](./media/virtual-machines-windows-nsg-quickstart-portal/add-inbound-rule.png)

Provide a name for your new rule. Note that port 80 is already entered by default. This is where you would change the source, protocol, and destination when adding additional rules to your Network Security Group:

![Create an inbound rule](./media/virtual-machines-windows-nsg-quickstart-portal/create-inbound-rule.png)

Your final step is to associate your Network Security Group with a subnet or a specific network interface. Let's associate the Network Security Group with a subnet:

![Associate a Network Security Group with a subnet](./media/virtual-machines-windows-nsg-quickstart-portal/associate-subnet.png)

Select your virtual network, and then select the appropriate subnet:

![Associating a Network Security Group with virtual networking](./media/virtual-machines-windows-nsg-quickstart-portal/select-vnet-subnet.png)

You have now created a Network Security Group, created an inbound rule that allows traffic on port 80, and associated it with a subnet. Any VMs you connect to that subnet will be reachable on port 80.


##<a name="more-information-on-network-security-groups"></a> More information on Network Security Groups
The quick commands here allow you to get up and running with traffic flowing to your VM. Network Security Groups provide a lot of great features and granularity for controlling access to your resources. You can read more about [creating a Network Security Group and ACL rules here](/documentation/articles/virtual-networks-create-nsg-arm-ps/).

Network Security Groups and ACL rules can also be defined as part of Azure Resource Manager templates. Read more about [creating Network Security Groups with templates](/documentation/articles/virtual-networks-create-nsg-arm-template/).

If you need to use port-forwarding to map a unique external port to an internal port on your VM, you need to use a load balancer and Network Address Translation (NAT) rules. For example, you may want to expose TCP port 8080 externally and have traffic directed to TCP port 80 on a VM.

## Next steps
In this example, you created a simple rule to allow HTTP traffic. You can find information on creating more detailed environments in the following articles:

- [Azure Resource Manager overview](/documentation/articles/resource-group-overview/)
- [What is a Network Security Group (NSG)?](/documentation/articles/virtual-networks-nsg/)
