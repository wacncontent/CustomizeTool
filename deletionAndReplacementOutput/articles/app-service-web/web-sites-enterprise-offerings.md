deletion:

deleted:

		An alternative approach is to make use of your existing investment on premise. In the example scenario, an employee expense system, you may wish to maintain your data store within your own internal infrastructure. This could be for integration with internal systems (reporting, payroll, billing etc.) or to satisfy an IT governance requirement.  Web Apps provides two methods of enabling you to connect to your on premises infrastructure:
		
		- [Hybrid Connections](/documentation/articles/integration-hybrid-connection-overview) – Hybrid Connections are a feature of Windows Azure BizTalk Services and enable Web Apps to connect to on premises resources securely, for example SQL Server, MySQL, Web APIs and custom web services. 
		- [Virtual Network Integration](http://azure.microsoft.com/blog/2014/09/15/azure-websites-virtual-network-integration/) – Web Apps integrtaion with Azure Virtual Network allows you to connect your web app to an Azure Virtual Network which in turn can be connected to your on premises infrastructure through a site-to-site VPN.

reason: ()

deleted:

		In this migration the solution uses Azure SQL Database but that is not the only database that is supported on Azure. Companies can also make use of MySQL, MongoDB, Azure DocumentDB and many more via add-ons which can be purchased at the [Azure Store](/marketplace/partner-program/).

reason: ()

deleted:

		#### Connectivity to On Premises Resources ####
		Azure Websites offers two methods of connecting to on premises resources, such as databases, enabling reuse of existing high value infrastructure. The two methods are Web Apps Virtual Network Integration and Hybrid Connections:
		
		- Web Apps Virtual Network Integration supports integration between Web Apps and an Azure Virtual Network, allowing you access to resources running in your Virtual Network which, if connected to your on premises network with site-to-site VPN, allows connectivity direct to your on premises systems.
		- Hybrid Connections are a feature of Azure BizTalk Services and provide an easy way to connect to individual on-premises resources such as SQL Server, MySQL, HTTP Web APIs and most custom Web Services.

reason: ()

deleted:

		[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]
		
		[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

reason: ()

replacement:

deleted:

		Apps](/home/features/app-service/web/)

replaced by:

		Apps](/home/features/web-site/)

reason: ()

deleted:

		Windows Azure platform allows Role Based Authorization Controls enabling enterprise levels of control to resources within Web Apps. RBAC gives enterprises the power to implement their own access management policies for all of their assets in the Azure Environment, by assigning users to groups and in turn assigning the required permissions to those groups against the asset such as a web app. For more information on RBAC in Azure, see [http://aka.ms/azurerbac](/documentation/articles/role-based-access-control-configure). By utilizing Web Apps, you can be sure your web applications are deployed in a safe and secure environment and you have full control into which territory your assets are deployed. 
		
		Additionally, Web Apps is also able to make full use of your on premises investments by offering the ability to connect back to your internal resources, such as your data warehouse or SharePoint environment. As discussed in [High Level solution] you can make use of Hybrid Connections and Virtual Network Connectivity to establish connections to on premises infrastructure and services.
		
		### Global Scale ###
		
		Azure Websites is a global and scalable platform, enabling your web applications to grow and adapt to the needs of a growing business quickly and with minimal long term planning and cost. In typical on premises infrastructure scenarios, expansion and increase in demand both locally and geographically would require a large amount of management, planning and expenditure to provision and manage additional infrastructure. Web Apps offers the ability to scale your web applications with the ebb and flow of your requirements. For example using the expenses application as an example, for the majority of the month your users are light users of the application but as the deadline each month for expense submissions to be entered and usage increases on your application, Web Apps has the capability to automatically provision more infrastructure for your application and then once the usage has subsided again it can scale back to the baseline infrastructure you define.
		
		Web Apps is available globally in 17 datacenters worldwide, and growing. For the most updated list of regions and location, see [https://azure.microsoft.com/regions/](https://azure.microsoft.com/regions/). With Web Apps, your business can easily achieve global reach and scale. As your company grows into new regions, the reporting application dashboards that you use and host on Web Apps can easily be deployed into additional datacenters and serve local users far more quickly through the combination of Web Apps and Azure Traffic Manager, all with the added benefit of the scalable infrastructure underneath being able to contract and expand as the needs of the regional offices change.

replaced by:

		Windows Azure platform allows Role Based Authorization Controls enabling enterprise levels of control to resources within Web Apps. RBAC gives enterprises the power to implement their own access management policies for all of their assets in the Azure Environment, by assigning users to groups and in turn assigning the required permissions to those groups against the asset such as a web app. By utilizing Web Apps, you can be sure your web applications are deployed in a safe and secure environment and you have full control into which territory your assets are deployed.

reason: ()

