<properties 
	pageTitle="Azure Government Developers Guide" 
	description="This provides a comparision of features and guidance on developing applications for Azure Government" 
	services="" 
	documentationCenter="" 
	authors="Joharve2" 
	manager="Chrisnie" 
	editor=""/>

<tags
	ms.service="multiple"
	ms.date="10/29/2015"
	wacn.date=""/>


#  Windows Azure Government Developer Guide 

Windows Azure Government is a physically and network isolated instance of Windows Azure.  This developers guide will provide details on the differences that application developers and administrators would need to interact and work with these seperate regions of Azure.

<!--Table of contents for topic, the words in brackets must match the heading wording exactly-->


## In this topic


+ [Overview](#Overview)
+ [Guidance for Developers](#Guidance)
+ [Features currently available in Windows Azure Government](#Features)
+ [Endpoint Mapping](#Endpoint)
+ [Next Steps](#next)


## <a name="Overview"></a>Overview

Windows Azure Government is a separate instance of the Windows Azure service addressing the security and compliance needs of U.S. federal agencies, state and local governments and their solutions providers. Azure Government offers physical and network isolation from non-U.S. government deployments and provides screened U.S. personnel. 

Microsoft provides a number of tools to create and deploy cloud applications to Microsoft's global Windows Azure service ("Global Service") and Windows Azure Government services.

When creating and deploying applications to the Azure Government Services, as opposed to the Global Service, developers need to know the key differences of the two services.  Specifically around setting up and configuring their programming environment, configuring endpoints, writing applications, and deploying them as services to Azure Government.

The information in this document summarizes those differences and supplements the information available on the [Azure Government](http://www.windowsazure.cn/gov "Azure Government") site and the [Windows Azure Technical Library](http://msdn.microsoft.com/cloud-app-development-msdn "MSDN") on MSDN. Official information may also be available in many other locations such as the [Windows Azure Trust Center](/support/trust-center/ "Windows Azure Trust Center"), [Azure Documentation Center](http://azure.microsoft.com/documentation/) and in [Azure Blogs](http://azure.microsoft.com/blog/ "Azure Blogs"). 

This content is intended for partners and developers who are deploying to Windows Azure Government.



## <a name="Guidance"></a>Guidance for Developers
Because most of the technical content that is available currently assumes that applications are being developed for the Global Service rather than for Windows Azure Government, it's important for you to ensure that developers are aware of key differences for applications developed to be hosted in Azure Government.

- First, there are services and feature differences, this means that certain features that are in specific regions of the Global Service may not be available in Azure Government.

- Second, for features that are offered in Azure Government, there are configuration differences from the Global Service.  Therefore, you should review your sample code, configurations and steps to ensure that you are building and executing within the Azure Government Cloud Services environment.


## <a name="Features"></a> Features currently available in Windows Azure Government
Azure Government currently has the following services available in both US GOV IOWA and US GOV VIRGINIA regions:

- Virtual Machines
- Cloud Services
- Storage
- Active Directory
- Scheduler
- Virtual Networking
- SQL Database
- Azure Files
- Media Services
- Traffic Manager
- Service Bus
- StorSimple
- Redis Cache
- Azure Backup
- Automation
- ExpressRoute
- etc.

Other services are available, and more services will be added on a continuous basis.  For the most current list of services, please see the [regions page](http://azure.microsoft.com/regions/#services) which will highlight each available region and their services.  

Currently, US GOV Iowa and US GOV Virginia are the data centers supporting Azure Government.  Please refer to the regions page above for current data centers and services available.

## <a name="Endpoint"></a>Endpoint Mapping

Use the following table to guide you when mapping public Windows Azure and SQL Database endpoints to Azure Government specific endpoints.


Service Type|Azure Public|Azure Government
---|---|---
Management Portal|manage.windowsazure.cn|manage.windowsazure.us
General|*.chinacloudapi.cn|*.usgovcloudapi.net
Core|*.core.chinacloudapi.cn|*.core.usgovcloudapi.net
Compute|*.chinacloudapp.cn|*.usgovchinacloudapp.cn
Blob Storage|*.blob.core.chinacloudapi.cn|	*.blob.core.usgovcloudapi.net
Queue Storage|*.queue.core.chinacloudapi.cn|*.queue.core.usgovcloudapi.net
Table Storage|*.table.core.chinacloudapi.cn|*.table.core.usgovcloudapi.net
Service Management|management.core.chinacloudapi.cn|management.core.usgovcloudapi.net
SQL Database|*.database.chinacloudapi.cn|*.database.usgovcloudapi.net
ARM Load balanced Endpoint|https://management.chinacloudapi.cn|https://management.usgovcloudapi.net  

* For ARM authentication via Azure AD, please reference [Authenticating Azure Resource Manager Requests](https://msdn.microsoft.com/zh-cn/library/azure/dn790557.aspx)

## <a name="next"></a>Next steps

If you are interested in learning more and about Azure Government please leverage some of the links below.

- **[Sign up for a trial](https://azuregov.microsoft.com/trial/azuregovtrial)**

- **[Acquiring and accessing Azure Government](http://azure.com/gov)**

- **[Azure Government Overview](/azure-government-overview)**

- **[Azure Government Blog](http://blogs.msdn.com/b/azuregov/)**

- **[Azure Compliance](/support/trust-center/compliance/)**

<!--Anchors-->



<!-- Images. -->

[1]: ./media/azure-government-developer-guide/publisherguide.png


<!--Link references-->
[Link 1 to another azure.microsoft.com documentation topic]: virtual-machines-windows-tutorial.md
[Link 2 to another azure.microsoft.com documentation topic]: web-sites-custom-domain-name.md
[Link 3 to another azure.microsoft.com documentation topic]: storage-whatis-account.md
