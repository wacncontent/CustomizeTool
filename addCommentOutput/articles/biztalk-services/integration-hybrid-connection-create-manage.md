<properties 
	pageTitle="Create and Manage Hybrid Connections | Windows Azure" 
	description="Learn how to create a hybrid connection, manage the connection, and install the Hybrid Connection Manager. MABS, WABS" 
	services="biztalk-services" 
	documentationCenter="" 
	authors="MandiOhlinger" 
	manager="dwrede" 
	editor="cgronlun"/>

<tags
	ms.service="biztalk-services"
	ms.date="09/24/2015"
	wacn.date=""/>

<!-- deleted by customization

# Create and Manage Hybrid Connections


## Overview of the Steps
1. Create a Hybrid Connection by entering the host name or IP address of the on-premises resource in your private network.
2. Link your Azure web sites or Azure Mobile Apps to the Hybrid Connection.
3. Install the Hybrid Connection Manager on your on-premises resource and connect to the specific Hybrid Connection. The Azure Management Portal provides a single-click experience to install and connect.
4. Manage Hybrid Connections and their connection keys.

This topic lists these steps. 


## <a name="CreateHybridConnection"></a>Create a Hybrid Connection

A Hybrid Connection can be created in the Azure Management Portal using web sites **or** using BizTalk Services. 

**To create Hybrid Connections using web sites**, see [Connect Azure web sites to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started).
-->
<!-- keep by customization: begin -->
#Create and Manage Hybrid Connections

This topic lists the steps to create and manage Azure Hybrid Connections. 

To connect to an on-premises resource, the steps include:

1. [Create a Hybrid Connection](#CreateHybridConnection) by specifying the host name or IP address of the on-premises resource in your private network.

2.	[Link your Azure website or Azure mobile service](#LinkWebSite) to the Hybrid Connection.

3. [Install the Hybrid Connection Manager](#InstallHCM) on your on-premises resource and connect to the specific Hybrid Connection. The Azure Management Portal provides a single-click experience to install and connect.

4. [Manage Hybrid Connections](#ManageHybridConnection) and their connection keys.


##<a name="CreateHybridConnection"></a>Create a Hybrid Connection

A Hybrid Connection can be created in the Azure Management Portal using Websites **or** using BizTalk Services. 

**To create Hybrid Connections using Websites**, see [Connect an Azure Website to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started/).
<!-- keep by customization: end -->

**To create Hybrid Connections in BizTalk Services**:

1. Sign in to the [Azure Management <!-- deleted by customization Portal](https://manage.windowsazure.cn/) --><!-- keep by customization: begin --> Portal](http://manage.windowsazure.cn/) <!-- keep by customization: end -->.
2. In the left navigation pane, select **BizTalk Services** and then select your BizTalk Service. 
<!-- deleted by customization

	If you don't have an existing BizTalk Service, you can [Create a BizTalk Service](/documentation/articles/biztalk-provision-services).
-->
<!-- keep by customization: begin -->
<br/>If you don't have an existing BizTalk Service, you can [Create a BizTalk Service](/documentation/articles/biztalk-service-state-chart/).
<!-- keep by customization: end -->
3. Select the Hybrid Connections tab:  
<!-- deleted by customization
![Hybrid Connections Tab][HybridConnectionTab]
-->
<!-- keep by customization: begin -->
<br/>
![Hybrid Connections Tab][HybridConnectionTab]
<!-- keep by customization: end -->

4. Select **Create a Hybrid Connection** or select the **ADD** button in the task bar. Enter the following:

<!-- deleted by customization
	Property | Description
--- | ---
Name | The<!-- keep by customization: begin --> <td>The <!-- keep by customization: end --> Hybrid Connection name must be unique and cannot be the same name as the BizTalk Service. You can enter any name but be specific with its purpose. Examples <!-- deleted by customization include:<br/><br/>Payroll*SQLServer*<br/>SupplyList*SharepointServer*<br/>Customers*OracleServer* --><!-- keep by customization: begin --> include:<br/><br/> <!-- keep by customization: end -->
Host Name | Enter the fully qualified host name, only the host name, or the IPv4 address of the on-premises resource. Examples include:<br/><br/>mySQLServer<br/>*mySQLServer*.*Domain*.corp.*yourCompany*.com<br/>*myHTTPSharePointServer*<br/>*myHTTPSharePointServer*.*yourCompany*.com<br/>10.100.10.10
Port | Enter<!-- keep by customization: begin --> <td>Enter <!-- keep by customization: end --> the port number of the on-premises resource. For example, if you're using web sites, enter port 80 or port 443. If you're using SQL Server, enter port 1433.<!-- keep by customization: begin --> 1433.</td> <!-- keep by customization: end -->

5. Select the check mark to complete the setup. 

#### Additional

- Multiple Hybrid Connections can be created. See the [BizTalk Services: Editions Chart](/documentation/articles/biztalk-editions-feature-chart) for the number of connections allowed.
-->
<!-- keep by customization: begin -->
	<table border="1">
    <tr>
       <td><strong>Name</strong></td>
<!-- keep by customization: begin --> <td>The <!-- keep by customization: end --> Hybrid Connection name must be unique and cannot be the same name as the BizTalk Service. You can enter any name but be specific with its purpose. Examples <!-- deleted by customization include:<br/><br/>Payroll*SQLServer*<br/>SupplyList*SharepointServer*<br/>Customers*OracleServer* --><!-- keep by customization: begin --> include:<br/><br/> <!-- keep by customization: end -->
		Payroll<em>SQLServer</em><br/>
		SupplyList<em>SharepointServer</em><br/>
		Customers<em>OracleServer</em>
        </td>
    </tr>
    <tr>
        <td><strong>Host Name</strong></td>
        <td>Enter the fully qualified host name, only the host name, or the IPv4 address of the on-premises resource. Examples include:
        <br/><br/>
<em>mySQLServer</em>
<br/>
<em>mySQLServer</em>.<em>Domain</em>.corp.<em>yourCompany</em>.com
<br/>
<em>myHTTPSharePointServer</em>
<br/>
<em>myHTTPSharePointServer</em>.<em>yourCompany</em>.com
<br/>
10.100.10.10
       </td>
    </tr>
	<tr>
        <td><strong>Port</strong></td>
<!-- keep by customization: begin --> <td>Enter <!-- keep by customization: end --> the port number of the on-premises resource. For example, if you're using a website, enter port 80 or port 443. If you're using SQL Server, enter port <!-- keep by customization: begin --> 1433.</td> <!-- keep by customization: end -->
	</tr>
	</table>


5. Select the check mark. 

####Additional

- Multiple Hybrid Connections can be created. See the [BizTalk Services: Editions Chart](/documentation/articles/biztalk-editions-feature-chart/) for the number of connections allowed.
<!-- keep by customization: end -->
- Each Hybrid Connection is created with a pair of connection strings: Application keys that SEND and On-premises keys that LISTEN. Each pair has a Primary and a Secondary key. 


<!-- deleted by customization
## <a name="LinkWebSite"></a>Link your Azure web sites or Azure Mobile Apps

To link the Azure web sites to an existing Hybrid Connection, select **use an existing Hybrid Connection** in the Hybrid Connections blade. See [Connect  Azure web sites to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started).

To link the Azure Mobile Apps to an existing Hybrid Connection, select **add hybrid connection** when changing or creating a Mobile Service. See [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started).


## <a name="InstallHCM"></a>Install the Hybrid Connection Manager on-premises

After a Hybrid Connection is created, install the Hybrid Connection Manager on the on-premises resource. It can be downloaded from your Azure web sites or from your BizTalk Service. BizTalk Services steps:

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
-->
<!-- keep by customization: begin -->
##<a name="LinkWebSite"></a>Link your Azure website or Azure mobile service

To link the Azure Website to an existing Hybrid Connection, select **use an existing Hybrid Connection** in the Hybrid Connections blade. See [Connect an Azure Website to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started/).

To link the Azure Mobile Service to an existing Hybrid Connection, select **add hybrid connection** when changing or creating a Mobile Service. See [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started).


##<a name="InstallHCM"></a>Install the Hybrid Connection Manager on-premises

After a Hybrid Connection is created, install the Hybrid Connection Manager on the on-premises resource. It can be downloaded from your Azure Website or from your BizTalk Service. BizTalk Services steps:

1. Sign in to the [Azure Management Portal](http://manage.windowsazure.cn).
<!-- keep by customization: end -->
2. In the left navigation pane, select **BizTalk Services** and then select your BizTalk Service. 
3. Select the **Hybrid Connections** tab:  
<!-- deleted by customization
![Hybrid Connections Tab][HybridConnectionTab]
-->
<!-- keep by customization: begin -->
<br/>
![Hybrid Connections Tab][HybridConnectionTab]
<!-- keep by customization: end -->
4. In the task bar, select **On-Premises Setup**:  
<!-- deleted by customization
![On-Premises Setup][HCOnPremSetup]
-->
<!-- keep by customization: begin -->
<br/>
![On-Premises Setup][HCOnPremSetup]
<!-- keep by customization: end -->
5. Select **Install and Configure** to run or download the Hybrid Connection Manager on the on-premises system. 
6. Select the check mark to start the installation. 

<!--
You can also download the Hybrid Connection Manager MSI file and copy the file to your on-premises resource. Specific steps:

1. Copy the on-premises primary Connection String. See [Manage Hybrid Connections](#ManageHybridConnection) in this topic for the specific steps.
2. Download the Hybrid Connection Manager MSI file. 
3. On the on-premises resource, install the Hybrid Connection Manager from the MSI file. 
4. Using Windows PowerShell, type: 
> Add-HybridConnection -ConnectionString â*Your On-Premises Connection String that you copied*â 
--> 

#### Additional
- Hybrid Connections support on-premises resources installed on the following operating systems:

	- Windows Server 2008 R2
	- Windows Server 2012
	- Windows Server 2012 R2


- After you install the Hybrid Connection Manager, the following occurs: 

	- The Hybrid Connection hosted on Azure is automatically configured to use the Primary Application Connection String. 
	- The On-Premises resource is automatically configured to use the Primary On-Premises Connection String.

- The Hybrid Connection Manager must use a valid on-premises connection string for authorization. The Azure <!-- deleted by customization web sites --><!-- keep by customization: begin --> Website <!-- keep by customization: end --> orMobile <!-- deleted by customization Apps --><!-- keep by customization: begin --> Service <!-- keep by customization: end --> must use a valid application connection string for authorization.
<!-- deleted by customization
- You can scale Hybrid Connections by installing another instance of the Hybrid Connection Manager on another server. Configure the on-premises listener to use the same address as the first on-premises listener. In this situation, the traffic is randomly distributed (round robin) between the active on-premises listeners. 


## <a name="ManageHybridConnection"></a>Manage Hybrid Connections
-->
<!-- keep by customization: begin -->


##<a name="ManageHybridConnection"></a>Manage Hybrid Connections
<!-- keep by customization: end -->
To manage your Hybrid Connections, you can:

- Use the Azure Management Portal and go to your BizTalk Service. 
- Use [REST APIs](http://msdn.microsoft.com/zh-cn/library/azure/dn232347.aspx).

<!-- deleted by customization
#### Copy/regenerate the Hybrid Connection Strings

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
-->
<!-- keep by customization: begin -->
####Copy/regenerate the Hybrid Connection Strings

1. Sign in to the [Azure Management Portal](http://manage.windowsazure.cn).
<!-- keep by customization: end -->
2. In the left navigation pane, select **BizTalk Services** and then select your BizTalk Service. 
3. Select the **Hybrid Connections** tab:  
<!-- deleted by customization
![Hybrid Connections Tab][HybridConnectionTab]
-->
<!-- keep by customization: begin -->
<br/>
![Hybrid Connections Tab][HybridConnectionTab]
<!-- keep by customization: end -->
4. Select the Hybrid Connection. In the task bar, select **Manage Connection**:  
<!-- deleted by customization
![Manage Options][HCManageConnection]
-->
<!-- keep by customization: begin -->
<br/>
![Manage Options][HCManageConnection]
<br/>
<!-- keep by customization: end -->
	**Manage Connection** lists the Application and On-Premises connection strings. You can copy the Connection Strings or regenerate the Access Key used in the connection string. 
<!-- keep by customization: begin -->
<br/>
<br/>
<!-- keep by customization: end -->
	**If you select Regenerate**, the Shared Access Key used within the Connection String is changed. Do the following:
	- In the Azure <!-- deleted by customization Management --><!-- keep by customization: begin --> mangement <!-- keep by customization: end --> Portal, select **Sync Keys** in the Azure application.
	- Re-run the **On-Premises Setup**. When you re-run the On-Premises Setup, the on-premises resource is automatically configured to use the updated Primary connection string.


<!-- deleted by customization #### Use --><!-- keep by customization: begin --> ####Use <!-- keep by customization: end --> Group Policy to control the on-premises resources used by a Hybrid Connection

<!-- deleted by customization
1. Download the [Hybrid Connection Manager Administrative Templates](http://www.microsoft.com/download/details.aspx?id=42963).
-->
<!-- keep by customization: begin -->
1. Download the Hybrid Connection Manager Administrative Templates.
<!-- keep by customization: end -->
2. Extract the files.
3. On the computer that modifies group policy, do the following:  
<!-- deleted by customization

	- Copy the .ADMX files to the *%WINROOT%\PolicyDefinitions* folder.
-->
<!-- keep by customization: begin -->
- Copy the .ADMX files to the *%WINROOT%\PolicyDefinitions* folder.
<!-- keep by customization: end -->
	- Copy the .ADML files to the *%WINROOT%\PolicyDefinitions\en-us* folder.

Once copied, you can use Group Policy Editor to change the policy.




## Next

<!-- deleted by customization
[Connect Azure web sites to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started)  
[Connect to on-premises SQL Server from Azure web sites](/documentation/articles/web-sites-hybrid-connection-connect-on-premises-sql-server)  
 [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started)
 [Hybrid Connections Overview](/documentation/articles/integration-hybrid-connection-overview)
-->
<!-- keep by customization: begin -->
- [Connect an Azure Website to an On-Premises Resource](/documentation/articles/web-sites-hybrid-connection-get-started/)
- [Hybrid Connections Step-by-Step: Connect to on-premises SQL Server from an Azure website](/documentation/articles/web-sites-hybrid-connection-connect-on-premises-sql-server/)
- [Azure Mobile Services and Hybrid Connections](/documentation/articles/mobile-services-dotnet-backend-hybrid-connections-get-started)
- [Hybrid Connections Overview](/documentation/articles/integration-hybrid-connection-overview)
<!-- keep by customization: end -->


## See Also

<!-- keep by customization: begin --> - <!-- keep by customization: end --> [REST API for Managing BizTalk Services on Windows Azure](http://msdn.microsoft.com/zh-cn/library/azure/dn232347.aspx)
<!-- deleted by customization
[BizTalk Services: Editions Chart](/documentation/articles/biztalk-editions-feature-chart)  
[Create a BizTalk Service using Azure Management Portal](/documentation/articles/biztalk-provision-services)  
[BizTalk Services: Dashboard, Monitor and Scale tabs](/documentation/articles/biztalk-dashboard-monitor-scale-tabs)


[HybridConnectionTab]: ./media/integration-hybrid-connection-create-manage/WABS_HybridConnectionTab.png
[HCOnPremSetup]: ./media/integration-hybrid-connection-create-manage/WABS_HybridConnectionOnPremSetup.png
[HCManageConnection]: ./media/integration-hybrid-connection-create-manage/WABS_HybridConnectionManageConn.png 

-->
<!-- keep by customization: begin -->
- [BizTalk Services: Editions Chart](/documentation/articles/biztalk-editions-feature-chart/)<br/>
- [Create a BizTalk Service using Azure Management Portal](/documentation/articles/biztalk-provision-services/)<br/>
- [BizTalk Services: Dashboard, Monitor and Scale tabs](/documentation/articles/biztalk-dashboard-monitor-scale-tabs/)<br/>


[HybridConnectionTab]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionTab.png
[HCOnPremSetup]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionOnPremSetup.png
[HCManageConnection]: ./media/integration-hybrid-connection-overview/WABS_HybridConnectionManageConn.png
<!-- keep by customization: end -->