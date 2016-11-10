<properties
   pageTitle="Manage Azure Traffic Manager profiles | Microsoft Azure"
   description="This article will help you create, disable, enable, delete, and view the history of a Azure Traffic Manager profile."
   services="traffic-manager"
   documentationCenter=""
   authors="joaoma"
   manager="carmonm"
   editor="tysonn" />
<tags
	ms.service="traffic-manager"
	ms.date="03/17/2016"
	wacn.date=""/>

# Manage an Azure Traffic Manager profile

You use a Traffic Manager profile to specify the cloud services or website endpoints that will be monitored by Traffic Manager, and what traffic routing  method you want to use to distribute connections to those endpoints.

## Create a Traffic Manager profile using Quick Create

You can quickly create a Traffic Manager profile by using Quick Create in the Azure  classic  Classic   portal  Management Portal . Quick Create allows you to create profiles with basic configuration settings. However, you cannot use Quick Create for settings such as the set of endpoints (cloud services and websites), the failover order for the failover traffic routing method, or monitoring settings. After creating your profile, you can configure these settings in the Azure  classic  Classic   portal  Management Portal . Traffic Manager supports up to 200 endpoints per profile. However, most usage scenarios require only a small number of endpoints.

### To create a new Traffic Manager profile

1. **Deploy your cloud services and websites to your production environment.** For more information about cloud services, see [Cloud  Services](https://msdn.microsoft.com/library/jj155995.aspx)  Services](https://msdn.microsoft.com/zh-CN/library/jj155995.aspx) . For information about cloud services, see [Best  practices](https://msdn.microsoft.com/library/azure/5229dd1c-5a91-4869-8522-bed8597d9cf5#bkmk_TrafficManagerBestPracticesProfile)  practices](https://msdn.microsoft.com/zh-cn/library/azure/5229dd1c-5a91-4869-8522-bed8597d9cf5#bkmk_TrafficManagerBestPracticesProfile) . For more information about websites, see [Websites](/home/features/web-site/).

2. **Log in to the Azure  classic  Classic   portal.**  Management Portal.**  To create a new Traffic Manager profile, click **New** on the lower left of the portal, click **Network Services > Traffic Manager**, and then click **Quick Create** to begin configuring your profile.
3. **Configure the DNS prefix.** Give your traffic manager profile a unique DNS prefix name. You can specify only the prefix for a Traffic Manager domain name.
4. **Select the subscription.** Select the appropriate Azure subscription. Each profile is associated with a single subscription. If you only have one subscription, this option does not appear.
5. **Select the traffic routing method.** Select the traffic routing method in **traffic routing Policy**. For more information about traffic routing methods, see [About Traffic Manager traffic routing methods](/documentation/articles/traffic-manager-routing-methods/).
6. **Click "Create" to create your new profile**. When the profile configuration is completed, you can locate your profile in the Traffic Manager pane in the Azure  classic  Classic   portal  Management Portal .
7. **Configure endpoints, monitoring, and additional settings in the Azure  classic  Classic   portal.**  Management Portal.**  Because you can only configure basic settings by using Quick Create, it is necessary to configure additional settings, such as the list of endpoints and the endpoint failover order, in order to complete your desired configuration.


## Disable, enable, or delete a profile

You can disable an existing Traffic Manager profile so that it will not refer user requests to its configured endpoints. When you disable a Traffic Manager profile, the profile itself and the information contained in the profile will remain intact and can be edited in the Traffic Manager interface. When you want to re-enable the profile, you can easily do so in the Azure  classic  Classic   portal  Management Portal  and referrals will resume. When you create a Traffic Manager profile in the Azure  classic  Classic   portal  Management Portal , it's automatically enabled. If you decide a profile will no longer be necessary, you can delete it.

### To disable a profile

1. Modify the DNS resource record on your Internet DNS server to use the appropriate record type and pointer to either another name or the IP address of a specific location on the Internet. In other words, change the DNS resource record on your Internet DNS server so that it no longer uses a CNAME resource record that points to the domain name of your Traffic Manager profile.
2. Traffic will stop being directed to the endpoints through the Traffic Manager profile settings.
3. Select the profile that you want to disable. To select the profile, on the Traffic Manager page, highlight the profile by clicking the column next to the profile name. Do not click the name of the profile or the arrow next to the name, as this will take you to the settings page for the profile.
4. After selecting the profile, click **Disable** at the bottom of the page.

### To enable a profile

1. Select the profile that you want to enable. To select the profile, on the Traffic Manager page, highlight the profile by clicking the column next to the profile name. Do not click the name of the profile or the arrow next to the name, as this will take you to the settings page for the profile.
2. After selecting the profile, click **Enable** at the bottom of the page.
3. Modify the DNS resource record on your Internet DNS server to use the CNAME record type, which maps your company domain name to the domain name of your Traffic Manager profile. For more information, see [Point a company Internet domain to a Traffic Manager domain](/documentation/articles/traffic-manager-point-internet-domain/).
4. Traffic will start being directed to the endpoints again.

### To delete a profile

1. Ensure that the DNS resource record on your Internet DNS server no longer uses a CNAME resource record that points to the domain name of your Traffic Manager profile.
2. Select the profile that you want to delete. To select the profile, on the Traffic Manager page, highlight the profile by clicking the column next to the profile. Do not click the name of the profile or the arrow next to the name, as this will take you to the settings page for the profile.
4. After selecting the profile, click **Delete** at the bottom of the page.

## View Traffic Manager profile change history


You can view the change history for your Traffic Manager profile in the Azure classic portal in Management Services.


You can view the change history for your Traffic Manager profile in the Azure Classic Management Portal in Management Services.


### To view your Traffic Manager change history


1. In the left pane of the Azure classic portal, click **Management Services**.


1. In the left pane of the Azure Classic Management Portal, click **Management Services**.

2. On the Management Services page, click **Operation Logs**.
3. On the Operation Logs page, you can filter to view the change history for your Traffic Manager profile. After selecting your filtering options, click the checkmark to view the results.
   - To view profile changes for all of your profiles, select your subscription and time range and then select **Traffic Manager** from the **Type** shortcut menu.
   - To filter by profile name, type the name of the profile in the **Service Name** field or select it from the shortcut menu.
   - To view details for each individual change, select the row with the change that you want to view, and then click **Details** at the bottom of the page. In the **Operation Details** window, you can view the XML representation of the API object that was created or updated as part of the operation and copy the XML code to the clipboard.


## Next steps

[Add an endpoint](/documentation/articles/traffic-manager-endpoints/)

[Configure failover routing method](/documentation/articles/traffic-manager-configure-failover-routing-method/)

[Configure round robin routing method](/documentation/articles/traffic-manager-configure-round-robin-routing-method/)

[Configure performance routing method](/documentation/articles/traffic-manager-configure-performance-routing-method/)

[Troubleshooting Traffic Manager degraded state](/documentation/articles/traffic-manager-troubleshooting-degraded/)