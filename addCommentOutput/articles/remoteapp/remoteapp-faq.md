<properties 
	pageTitle="Azure RemoteApp FAQ | Windows Azure" 
	description="Learn answers to the most frequently asked questions about Azure RemoteApp." 
	services="remoteapp" 
	documentationCenter="" 
	authors="lizap" 
	manager="mbaldwin" 
	editor=""/>

<tags
	ms.service="remoteapp"
	ms.date="10/23/2015"
	wacn.date=""/>

# Azure RemoteApp FAQ
We've heard the following questions about Azure RemoteApp. Have others? Visit the [RemoteApp forums](https://social.msdn.microsoft.com/Forums/azure/home?forum=AzureRemoteApp) and let us know what you need to know <!-- deleted by customization, or drop a comment down below -->.

## What is Azure RemoteApp? ##


- **What is Azure RemoteApp?** RemoteApp is an Azure service helps you provide secure, remote access to applications from many different user devices. Read more  about [Azure RemoteApp](/documentation/articles/remoteapp-whatis).
<!-- deleted by customization
- **What are the deployment options?** There are two kinds of RemoteApp collections: cloud and hybrid. Which one you need depends on a number of factors, like whether you need domain join. We talk about all of those decisions [here](/documentation/articles/remoteapp-collections).

## Quick tips on using Azure RemoteApp ##
- **How long until I'm disconnected? How long can I be idle before you give me the boot?** 4 hours. If you or one of your users is idle for 4 hours, you'll be automatically signed out of Azure RemoteApp. Check out the other default settings in [Azure Subscription and Service Limits, Quotas, and Constraints](/documentation/articles/azure-subscription-service-limits).
- **Can I try this service for free?** Yes. There is a trial available for 30 days. After the trial ends, you can transition to a paid account (which you can use in production) or stop using the service. Start your trial by going to [manage.windowsazure.cn](http://manage.windowsazure.cn) - create a new instance of RemoteApp. With the trial, you can build 2 instances of RemoteApp with 10 users per instance. Remember that this trial only lives for 30 days.
## Azure RemoteApp subscription details ##

- **What are the service limits?** You can learn about the default settings and service limits of Azure RemoteApp in [Azure Subscription and Service Limits, Quotas, and Constraints](/documentation/articles/azure-subscription-service-limits). Let us know if you have more questions.
-->
<!-- keep by customization: begin -->
- **What are the two kinds of deployment options?** There are two kinds of RemoteApp deployments (or collections): cloud and hybrid. Figure out which [deployment option](/documentation/articles/remoteapp-whatis) works best for your organization.

## Supported configurations ##

- **What are the service limits?** You can learn about the default settings and serivce limits of Azure RemoteApp in [Azure Subscription and Service Limits, Quotas, and Constraints](/documentation/articles/azure-subscription-service-limits). Let us know if you have more questions.
<!-- keep by customization: end -->
- **How many users do I have to have?** There's a minimum of 20 users. Let me repeat that to be super clear - the MINIMUM is 20. You will be billed for 20. 
<!-- deleted by customization
- **How much does RemoteApp cost?** Check out [Azure RemoteApp Pricing Details ](../../../home/features/remoteapp/#price).
- **Does one type of collection cost more than another?** 
Yes, it can, depending on your collection requirements. A hybrid collection requires a connection from Azure RemoteApp to your on-premises network. If you use an existing VNET/Express Route, there is no additional cost. But if you use a new Azure VNET and either a gateway or Express Route, you will be charged for the [VPN gateway](../../../home/features/vpn-gateway/#price) or [Express Route](../../../home/features/expressroute/#price). This cost (detailed in the links) is on top of your monthly Azure RemoteApp cost.

## Collections - what's supported, which should you use, and others
-->
- **Are custom line-of-business (LOB) applications supported?** Yes. To use a custom application in Azure RemoteApp, create a [custom template image](/documentation/articles/remoteapp-create-custom-image), and then upload it to the RemoteApp collection.
- **Will my custom LOB application work in Azure RemoteApp?** The best way to figure that out is to test it. Review the [application compatibility requirements](http://www.microsoft.com/download/details.aspx?id=18704) and check out the [RD Compatibility Center](http://www.rdcompatibility.com/compatibility/default.aspx).
- **Which deployment method (cloud or hybrid) is best for my organization?** Hybrid collections provide the most complete experience if you want full integration with single sign-on (SSO) and secure on-premises network connectivity. Cloud collections provide an agile and easy way to isolate your deployment by using multiple authentication methods. Read more about the [deployment options](/documentation/articles/remoteapp-whatis).
<!-- keep by customization: begin -->
- **The hybrid collection requires a VNET. Can we use our existing VNET?** You can if the existing VNET is an Azure VNET. See "Step 1: Set up your virtual network" in the [hybrid collection instructions](/documentation/articles/remoteapp-create-hybrid-deployment) for more information.
- **Can I use a cloud or existing virtual machine as the template for my RemoteApp collection?** Yes! You can create an image based on an Azure VM, use one of the images included with your subscription, or create a custom image. Check out the [RemoteApp image options](/documentation/articles/remoteapp-imageoptions).
<!-- keep by customization: end -->
- **We have SQL or another database either on-premises or in Azure. Which deployment type should we use?** That depends on where your SQL or backend database is. If the database is in a private network, use the hybrid collection. If the database is exposed to the Internet and allows client connections to connect to it, you can use the cloud collection.
- **What about drive mapping, USB and serial port, clipboard sharing, and printer redirection?** All of those features are supported in Azure RemoteApp. Clipboard sharing and printer redirection is enabled by default. You can learn more about redirection [here](/documentation/articles/remoteapp-redirection). 


<!-- deleted by customization
## Template images
- **Can I use a cloud or existing virtual machine as the template for my RemoteApp collection?** Yes! You can create an image based on an Azure VM, use one of the images included with your subscription, or create a custom image. Check out the [RemoteApp image options](/documentation/articles/remoteapp-imageoptions).


## Network options
- **The hybrid collection requires a VNET. Can we use our existing VNET?** You can if the existing VNET is an Azure VNET. See "Step 1: Set up your virtual network" in the [hybrid collection instructions](/documentation/articles/remoteapp-create-hybrid-deployment) for more information.
- **Can I use a VNET with a cloud collection?** Indeed you can. Check out [Create a cloud collection](/documentation/articles/remoteapp-create-cloud-deployment), particularly Step 1, for more information.

## Authentication options



-->
- **How about authentication? Which methods are supported?** The cloud collection supports Microsoft accounts and Azure Active Directory accounts, which are Office 365 accounts as well. The hybrid collection supports only Azure Active Directory accounts that have been synced (using a tool like [Azure Active Directory Sync](http://blogs.technet.com/b/ad/archive/2014/09/16/azure-active-directory-sync-is-now-ga.aspx)) from a Windows Server Active Directory deployment; specifically, either synced with the Password Synchronization option or synced with Active Directory Federation Services (AD FS) federation configured. You can also configure [Multi-Factor Authentication (MFA)](/home/features/multi-factor-authentication/).

<!-- deleted by customization >[AZURE.NOTE]The --><!-- keep by customization: begin --> **Note:** The <!-- keep by customization: end --> Azure Active Directory users must be from the tenant that's associated with your subscription. (You can view and modify your subscription on the **Settings** tab in the portal. See [Change the Azure Active Directory tenant used by RemoteApp](/documentation/articles/remoteapp-changetenant) for more information.)

- **Why can't I give my Azure Active Directory account access?** The Azure Active Directory users must be from the directory that's associated with your subscription. You can view or modify that directory on the Settings tab in the portal. See [Change the Azure Active Directory tenant used by RemoteApp](/documentation/articles/remoteapp-changetenant) for more information.
<!-- deleted by customization

## Clients - what device can I use to access Azure RemoteApp?
You can find good client information, including steps for installing the different clients at [Accessing your apps in Azure RemoteApp](/documentation/articles/remoteapp-clients).

- **Which devices and operating systems do the client applications support?**
First, the computers and tablets: 
	- Windows 10 (client preview)
	- Windows 8.1 and Windows 8
	- Windows 7 Service Pack 1
	- Mac OS X
	- Windows RT
	- Android tablets
	- iPads
And the phones:
	- iPhone
	- Android Phone
	- Windows Phone
-->
<!-- keep by customization: begin -->
- **Which devices and operating systems do the client applications support?** Client applications are available for Windows 8.1, Windows 8, Windows 7 Service Pack 1, iOS, Mac OS X, Windows RT, Android devices, and Windows Phone. We also support the Windows 10 preview.
<!-- keep by customization: end -->
 
	[Download](https://www.remoteapp.windowsazure.cn/ClientDownload/AllClients.aspx) a RemoteApp client now.
- **Does Azure RemoteApp support Thin Clients?** Yes, the following Windows Embedded thin clients are supported:
<!-- deleted by customization
	- Windows Embedded Standard 7
	- Windows Embedded 8 Standard
	- Windows Embedded 8.1 Industry Pro
	- Windows 10 IoT Enterprise
-->
<!-- keep by customization: begin -->
	- Windows Embedded Standard 7 with Service Pack 1
	- Windows Embedded POSReady7 
	- Windows Embedded Thin PC 
	- Windows Embedded 8.1 Industry 
<!-- keep by customization: end -->

- **Which version of Windows Server is supported for the Remote Desktop Session Host (RDSH)?** Windows Server 2012 R2.

##Support and feedback

<!-- keep by customization: begin -->
- **Can I try this service for free?** Yes. There is a trial available for 30 days. After the trial ends, you can transition to a paid account (which you can use in production) or stop using the service. Start your trial by going to [manage.windowsazure.cn](http://manage.windowsazure.cn) - create a new instance of RemoteApp. With the trial, you can build 2 instances of RemoteApp with 10 users per instance. Remember that this trial only lives for 30 days.
<!-- keep by customization: end -->
- **What is the support plan for RemoteApp?** Support for billing and subscription management is provided at no cost. Technical support is available through the [Azure service plans](../../../support/plans/). You can also get free community support through our [Azure discussion forum](http://social.msdn.microsoft.com/Forums/zh-cn/home?forum=windowsazurezhchshome?forum=AzureRemoteApp). 
<!-- keep by customization: begin -->
- **How much does RemoteApp cost?** Check out [Azure RemoteApp Pricing Details ](../../../home/features/remoteapp/#price).
<!-- keep by customization: end -->
- **How do I submit feedback?** Visit the [feedback forum](http://feedback.azure.com/forums/247748-azure-remoteapp).
- **Who can I talk to learn more about Azure RemoteApp?** In addition to our [discussion forum](http://social.msdn.microsoft.com/Forums/zh-cn/home?forum=windowsazurezhchshome?forum=AzureRemoteApp), which is a great place to post questions, you can join the weekly [Ask the Experts webinar](https://azureinfo.microsoft.com/US-Azure-WBNR-FY15-11Nov-AzureRemoteAppAskTheExperts-Registration-Page.html), where we talk about all things RemoteApp.
- **What about RemoteApp documentation?** We're so glad you asked. In addition to the help content in the portal help drawer (just click the **?** on any page in the portal), the following articles are available to teach you all about RemoteApp:
	- **Get started:**
		- [What is RemoteApp?](/documentation/articles/remoteapp-whatis)
		- [What is in the RemoteApp template images?](/documentation/articles/remoteapp-images)
		- [How does licensing work?](/documentation/articles/remoteapp-licensing)
		- [How do RemoteApp and Office work together?](/documentation/articles/remoteapp-o365)
		- [How does redirection work in RemoteApp](/documentation/articles/remoteapp-redirection)?
	- **Deploy:**
		- [Create a custom template image](/documentation/articles/remoteapp-create-custom-image)
		- [Create a hybrid collection](/documentation/articles/remoteapp-create-hybrid-deployment)
		- [Create a cloud collection](/documentation/articles/remoteapp-create-cloud-deployment)
		- [Configure Azure Active Directory for RemoteApp](/documentation/articles/remoteapp-ad)
		- [Publish an app in RemoteApp](/documentation/articles/remoteapp-publish)
	- **Manage:**
		- [Add users](/documentation/articles/remoteapp-user)
		- [Best practices for configuring and using RemoteApp](/documentation/articles/remoteapp-bestpractices)	

	Videos! We also have a number of videos about RemoteApp. Some provide introduction ([Introduction to Azure <!-- deleted by customization RemoteApp](http://azure.microsoft.com/documentation/videos/cloud-cover-ep-150-azure-remote-app-with-thomas-willingham-and-nihar-namjoshi/)) --><!-- keep by customization: begin --> RemoteApp](http://www.windowsazure.cn/documentation/videos/cloud-cover-ep-150-azure-remote-app-with-thomas-willingham-and-nihar-namjoshi/)) <!-- keep by customization: end --> while others walk you through deployment ([Cloud deployment](https://www.youtube.com/watch?v=3NAv2iwZtGc&feature=youtu.be) and [Hybrid deployment](https://www.youtube.com/watch?v=GCIMxPUvg0c&feature=youtu.be)). Check them out!

<!-- deleted by customization
### Help us help you 
Did you know that in addition to rating this article and making comments down below, you can make changes to the article itself? Something missing? Something wrong? Did I write something that's just confusing? Scroll up and click **Edit on GitHub** to make changes - those will come to us for review, and then, once we sign off on them, you'll see your changes and improvements right here.

-->