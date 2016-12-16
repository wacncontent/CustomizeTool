<properties
    pageTitle="Create a virtual network using the Azure portal preview | Azure"
    description="Learn how to create a virtual network using the Azure portal preview | Resource Manager."
    services="virtual-network"
    documentationcenter=""
    author="jimdial"
    manager="carmonm"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="4ad679a4-a959-4e48-a317-d9f5655a442b"
    ms.service="virtual-network"
    ms.devlang="na"
    ms.topic="hero-article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="11/8/2016"
    wacn.date=""
    ms.author="jdial" />

# Create a virtual network using the Azure portal preview

[AZURE.INCLUDE [virtual-networks-create-vnet-intro](../../includes/virtual-networks-create-vnet-intro-include.md)]

Azure has two deployment models: Azure Resource Manager and classic. Azure recommends creating resources through the Resource Manager deployment model. To learn more about the differences between the two models, read the [Understand Azure deployment models](/documentation/articles/resource-manager-deployment-model/) article.
 
This article explains how to create a VNet through the Resource Manager deployment model using the Azure portal preview. You can also create a VNet through Resource Manager using other tools or create a VNet through the classic deployment model by selecting a different option from the following list:
> [AZURE.SELECTOR]
- [Portal](/documentation/articles/virtual-networks-create-vnet-arm-pportal/)
- [PowerShell](/documentation/articles/virtual-networks-create-vnet-arm-ps/)
- [CLI](/documentation/articles/virtual-networks-create-vnet-arm-cli/)
- [Template](/documentation/articles/virtual-networks-create-vnet-arm-template-click/)
- [Portal (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-pportal/)
- [PowerShell (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-netcfg-ps/)
- [CLI (Classic)](/documentation/articles/virtual-networks-create-vnet-classic-cli/)

[AZURE.INCLUDE [virtual-networks-create-vnet-scenario-include](../../includes/virtual-networks-create-vnet-scenario-include.md)]

## Create a virtual network

To create a virtual network using the Azure portal preview, complete the following steps:

1. From a browser, navigate to http://portal.azure.cn and, if necessary, sign in with your Azure account.
2. Click **New** > **Networking** > **Virtual network**, as shown in the following picture:

	![New Virtual Network](./media/virtual-network-create-vnet-arm-pportal/1.png)

3. In the **Virtual network** blade that appears, ensure that *Resource Manager* is selected and click **Create**, as shown in the following picture:

	![Virtual Network](./media/virtual-network-create-vnet-arm-pportal/2.png)
	
4. In the **Create virtual network** blade that appeared, enter *TestVNet* for **Name**, *192.168.0.0/16* for **Address space**, *FrontEnd* for **Subnet name** *192.168.1.0/24* for **Subnet address range**, *TestRG* for **Resource group**, select your **Subscription**, a **Location** and click the **Create** button, as shown in the following picture:

	![Create virtual network](./media/virtual-network-create-vnet-arm-pportal/3.png)

	Alternatively, you can select an existing resource group. To learn more about resource groups, read the [Resource Manager overview](/documentation/articles/resource-group-overview/#resource-groups) article. You can also select a different location. To learn more about Azure locations and regions, read the [Azure regions](https://azure.microsoft.com/regions) article.

5. The portal only enables you to create one subnet when creating a VNet. For this scenario, a second subnet must be created after the VNet is created. To create the second subnet, click **All resources**, then click **TestVNet** in the **All resources** blade, as shown in the following picture:

	![Created VNet](./media/virtual-network-create-vnet-arm-pportal/4.png)

6. In the **TestVNet** blade that appears, click **Subnet**, then click **+Subnet**, enter *BackEnd* for **Name**, *192.168.2.0/24* for **Address range** in the **Add subnet** blade, then click **OK**, as shown in the following picture:

	![Add subnet](./media/virtual-network-create-vnet-arm-pportal/5.png)

7. The two subnets are listed, as shown in the following picture:
	
	![List of subnets in VNet](./media/virtual-network-create-vnet-arm-pportal/6.png)

This article explained how to create a virtual network with two subnets for testing. Before creating a virtual network for production use, we recommend reading the [Virtual network overview](/documentation/articles/virtual-networks-overview/) and [Virtual network plan and design](/documentation/articles/virtual-network-vnet-plan-design-arm/) articles to fully understand virtual networks and all settings. 

## Next steps

Learn how to connect:

- A virtual machine (VM) to a virtual network by reading the [Create a Windows VM](/documentation/articles/virtual-machines-windows-hero-tutorial/) or [Create a Linux VM](/documentation/articles/virtual-machines-linux-quick-create-portal/) articles. Instead of creating a VNet and subnet in the steps of the articles, you can select an existing VNet and subnet to connect a VM to.
- The virtual network to other virtual networks by reading the [Connect VNets](/documentation/articles/vpn-gateway-howto-vnet-vnet-resource-manager-portal/) article.
- The virtual network to an on-premises network using a site-to-site virtual private network (VPN) or ExpressRoute circuit. Learn how by reading the [Connect a VNet to an on-premises network using a site-to-site VPN](/documentation/articles/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/) and [Link a VNet to an ExpressRoute circuit](/documentation/articles/expressroute-howto-linkvnet-portal-resource-manager/) articles.