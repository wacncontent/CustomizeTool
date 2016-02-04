<properties
	pageTitle="Hybrid Connections overview | Windows Azure"
	description="Learn about Hybrid Connections, including security, TCP ports, and supported configurations. MABS, WABS."
	services="biztalk-services"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor="cgronlun"/>

<tags
	ms.service="biztalk-services"
	ms.date="09/08/2015"
	wacn.date=""/>


<!-- deleted by customization
# Hybrid Connections overview
This article introduces Hybrid Connections, lists the supported configurations, and lists the required TCP ports.


## What is a hybrid connection

Hybrid Connections are a feature of Azure BizTalk Services. Hybrid Connections provide an easy and convenient way to connect the web sites feature in Azure Websites (formerly Websites) and the Mobile Apps feature in Azure Websites (formerly Mobile Services) to on-premises resources behind your firewall.

![Hybrid Connections][HCImage]
-->
<!-- keep by customization: begin -->

# Hybrid Connections Overview
This topic introduces Hybrid Connections, lists the supported configurations, and lists the required TCP Ports. Specifically:

- [What is a Hybrid Connection](#HCOverview)
- [Supported Configurations](#KnownIssues)
- [Security and Ports](#HCSecurity)

##<a name="HCOverview"></a>What is a Hybrid Connection

Hybrid Connections provides an easy and convenient way to connect Azure  Websites and Azure Mobile Services to on-premises resources. Hybrid Connections are a feature of Azure BizTalk Services:

![Hybrid Connections][HCImage]
<!-- keep by customization: end -->

Hybrid Connections benefits include:

<!-- deleted by customization
- web sites and Mobile Apps can access existing on-premises data and services securely.
- Multiple web sites or Mobile Apps can share a Hybrid Connection to access an on-premises resource.
- Minimal TCP ports are required to access your network.
-->
<!-- keep by customization: begin -->
-  Websites and Mobile Services can access existing on-premises data and services securely.
- Multiple  Websites or Mobile Services can share a Hybrid Connection to access an on-premises resource. 
- Minimal TCP Ports are required to access your network.
<!-- keep by customization: end -->
- Applications using Hybrid Connections access only the specific on-premises resource that is published through the Hybrid Connection.
- Can connect to any on-premises resource that uses a static TCP port, such as SQL Server, MySQL, HTTP Web APIs, and most custom Web Services.

	> <!-- deleted by customization [AZURE.NOTE] --><!-- keep by customization: begin --> [WACOM.NOTE] <!-- keep by customization: end --> TCP-based services that use dynamic ports (such as FTP Passive Mode or Extended Passive Mode) are currently not supported.

- Can be used with all frameworks supported by <!-- deleted by customization web sites --><!-- keep by customization: begin --> Azure  Websites <!-- keep by customization: end --> (.NET, PHP, Java, Python, Node.js) and <!-- keep by customization: begin --> Azure <!-- keep by customization: end --> Mobile <!-- deleted by customization Apps --><!-- keep by customization: begin --> Services <!-- keep by customization: end --> (Node.js, .NET).
- <!-- deleted by customization web sites --><!-- keep by customization: begin -->  Websites <!-- keep by customization: end --> and Mobile <!-- deleted by customization Apps --><!-- keep by customization: begin --> Services <!-- keep by customization: end --> can access on-premises resources in exactly the same way as if the <!-- deleted by customization Web --><!-- keep by customization: begin -->  Website <!-- keep by customization: end --> or Mobile <!-- deleted by customization App --><!-- keep by customization: begin --> Service <!-- keep by customization: end --> is located on your local network. For example, the same connection string used on-premises can also be used on Azure.


Hybrid Connections also provide <!-- deleted by customization enterprise administrators with --><!-- keep by customization: begin --> Enterprise Administrators <!-- keep by customization: end --> control and visibility into the corporate resources accessed by hybrid applications, including:

- Using Group Policy settings, <!-- deleted by customization administrators --><!-- keep by customization: begin --> Administrators <!-- keep by customization: end --> can allow Hybrid Connections on the network and also designate resources that can be accessed by hybrid applications.
- Event and <!-- deleted by customization audit --><!-- keep by customization: begin --> Audit <!-- keep by customization: end --> logs on the corporate network provide visibility into the resources accessed by Hybrid Connections.


<!-- deleted by customization
## Supported configurations
-->
<!-- keep by customization: begin -->
##<a name="KnownIssues"></a>Supported Configurations
<!-- keep by customization: end -->

Hybrid Connections support the following framework and application combinations:

- .NET framework access to SQL Server
- .NET framework access to HTTP/HTTPS services with WebClient
- PHP access to SQL Server, MySQL
- Java access to SQL Server, MySQL and Oracle
- Java access to HTTP/HTTPS services

When using Hybrid Connections to access on-premises SQL Server, consider the following:

- SQL Express Named Instances must be configured to use static ports. By default, SQL Express named instances use dynamic ports.
- SQL Express Default Instances <!-- deleted by customization use --><!-- keep by customization: begin --> uses <!-- keep by customization: end --> a static port, but TCP must be enabled. By default, TCP is not enabled.
- When using Clustering or Availability Groups, the <!-- deleted by customization `MultiSubnetFailover=true` --><!-- keep by customization: begin --> MultiSubnetFailover=true <!-- keep by customization: end --> mode is currently not supported.
- The <!-- deleted by customization `ApplicationIntent=ReadOnly` --><!-- keep by customization: begin --> ApplicationIntent=ReadOnly <!-- keep by customization: end --> is currently not supported.
- SQL Authentication may be required as the end-to-end authorization method supported by the Azure application and the on-premises SQL server.


<!-- deleted by customization
## Security and ports

Hybrid Connections use Shared Access Signature (SAS) authorization to secure the connections from the Azure applications and the on-premises Hybrid Connection Manager to the Hybrid Connection. Separate connection keys are created for the application and the on-premises Hybrid Connection Manager. These connection keys can be rolled over and revoked independently.

Hybrid Connections provide for seamless and secure distribution of the keys to the applications and the on-premises Hybrid Connection Manager.
-->
<!-- keep by customization: begin -->
##<a name="HCSecurity"></a>Security and Ports

Hybrid Connections uses Shared Access Signature (SAS) authorization to secure the connections from the Azure applications and the on-premises Hybrid Connection Manager to the Hybrid Connection. Separate connection keys are created for the application and the on-premises Hybrid Connection Manager. These connection keys can be rolled over and revoked independently.

Hybrid Connections provides for seamless and secure distribution of the keys to the applications and the on-premises Hybrid Connection Manager.
<!-- keep by customization: end -->

See[Create and Manage Hybrid Connections](/documentation/articles/integration-hybrid-connection-create-manage).

<!-- deleted by customization *Application --><!-- keep by customization: begin --> **Application <!-- keep by customization: end --> authorization is separate from the Hybrid <!-- deleted by customization Connection* --><!-- keep by customization: begin --> Connection** <!-- keep by customization: end -->. Any appropriate authorization method can be used. The authorization method depends on the end-to-end authorization methods supported across the Azure cloud and the on-premises components. For example, your Azure application accesses an on-premises SQL Server. In this scenario, SQL Authorization may be the authorization method that is supported end-to-end.

<!-- deleted by customization
#### TCP ports
Hybrid Connections require only outbound TCP or HTTP connectivity from your private network. You do not need to open any firewall ports or change your network perimeter configuration to allow any inbound connectivity into your network.
-->
<!-- keep by customization: begin -->
####TCP Ports
Hybrid Connections requires only outbound TCP or HTTP connectivity from your private network. You do not need to open any firewall ports or change your network perimeter configuration to allow any inbound connectivity into your network.
<!-- keep by customization: end -->

The following TCP ports are used by Hybrid Connections:

<!-- deleted by customization
Port | Why you need it
--- | ---
9350 - 9354 | These ports are used for data transmission. The Service Bus relay manager probes port 9350 to determine if TCP connectivity is available. If it is available, then it assumes that port 9352 is also available. Data traffic goes over port 9352. <br/><br/>Allow outbound connections to these ports.
5671 | When port 9352 is used for data traffic, port 5671 is used as the control channel. <br/><br/>Allow outbound connections to this port.
80, 443 | If ports 9352 and 5671 are not usable, *then* ports 80 and 443 are the fallback ports used for data transmission and the control channel.<br/><br/>Allow outbound connections to these ports. <br/><br/>**Note** It is not recommended to use these fallback ports in place of the other TCP ports. The HTTP/WebSocket is used as the protocol instead of native TCP for data channels. It could result in lower performance.



## Next steps

[Create and manage Hybrid Connections](/documentation/articles/integration-hybrid-connection-create-manage)<br/>
[Connect an Azure website to an on-premises resource](/documentation/articles/web-sites-hybrid-connection-get-started)<br/>
[Connect to on-premises SQL Server from an Azure web site](/documentation/articles/web-sites-hybrid-connection-connect-on-premises-sql-server)<br/>
 [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started)
-->
<!-- keep by customization: begin -->
<table border="1">
    <tr>
       <th><strong>Port</strong></th>
        <th>Why</th>
    </tr>
    <tr>
        <td>80</td>
        <td>HTTP port; Used for certificate validation.</td>
    </tr>
    <tr>
        <td>443</td>
        <td>HTTPS port</td>
    </tr>
	<tr>
        <td>5671</td>
        <td>Used to connect to Azure. If TCP port 5671 is unavailable, TCP port 443 is used.</td>
	</tr>
	<tr>
        <td>9352</td>
        <td>Used to push and pull data. If TCP port 9352 is unavailable, TCP port 443 is used.</td>
	</tr>
</table>


## Next

- [Create and Manage Hybrid Connections](/documentation/articles/integration-hybrid-connection-create-manage)
- [Connect an Azure  Website to an On-Premises Resource](http://go.microsoft.com/fwlink/p/?LinkId=397538)
- [Hybrid Connections Step-by-Step: Connect to on-premises SQL Server from an Azure  Website](/documentation/articles/web-sites-hybrid-connection-connect-on-premises-sql-server/)
- [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started)
<!-- keep by customization: end -->


## See Also

<!-- keep by customization: begin --> - <!-- keep by customization: end --> [REST API for Managing BizTalk Services on Windows Azure](http://msdn.microsoft.com/zh-cn/library/azure/dn232347.aspx)
<!-- deleted by customization
[BizTalk Services: Editions Chart](/documentation/articles/biztalk-editions-feature-chart)<br/>
[Create a BizTalk Service using Azure Management Portal](/documentation/articles/biztalk-provision-services)<br/>
[BizTalk Services: Dashboard, Monitor and Scale tabs](/documentation/articles/biztalk-dashboard-monitor-scale-tabs)<br/>
-->
<!-- keep by customization: begin -->
- [BizTalk Services: Editions Chart](http://go.microsoft.com/fwlink/p/?LinkID=302279)<br/>
- [Create a BizTalk Service using Azure Management Portal](http://go.microsoft.com/fwlink/p/?LinkID=302280)<br/>
- [BizTalk Services: Dashboard, Monitor and Scale tabs](http://go.microsoft.com/fwlink/p/?LinkID=302281)<br/>
<!-- keep by customization: end -->

[HCImage]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionImage.png
[HybridConnectionTab]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionTab.png
[HCOnPremSetup]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionOnPremSetup.png
[HCManageConnection]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionManageConn.png