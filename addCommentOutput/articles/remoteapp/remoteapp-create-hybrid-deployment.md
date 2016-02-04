<properties 
	pageTitle="How to create a hybrid collection for Azure RemoteApp | Windows Azure" 
	description="Learn how to create a deployment of RemoteApp that connects to your internal network." 
	services="remoteapp" 
	documentationCenter="" 
	authors="lizap" 
	manager="mbaldwin" 
	editor=""/>

<tags
	ms.service="remoteapp"
	ms.date="11/04/2015"
	wacn.date=""/>

# How to create a hybrid collection for Azure RemoteApp

There are two kinds of <!-- deleted by customization Azure --> RemoteApp collections:

<!-- deleted by customization
- Cloud: resides completely in Azure. You can choose to save all data in the cloud (so a cloud-only collection) or to connect your collection to a VNET and save data there.   
- Hybrid: includes a virtual network for on-premises access - this requires the use of Azure AD and an on-premises Active Directory environment.

Don't know which you need? Check out [Which kind of collection do you need for Azure RemoteApp](/documentation/articles/remoteapp-collections).
-->
<!-- keep by customization: begin -->
- Cloud: resides completely in Azure and is created using the **Quick create** option in the Azure management portal.  
- Hybrid: includes a virtual network for on-premises access and is created using the **Create with VNET** option in the management portal.
<!-- keep by customization: end -->

This tutorial walks you through the process of creating a hybrid collection. There are eight steps: 

1.	Decide what [image](/documentation/articles/remoteapp-imageoptions) to use for your collection. You can create a custom image or use one of the Microsoft images included with your subscription.
2. Set up your virtual network. <!-- deleted by customization Check out the [VNET planning](/documentation/articles/remoteapp-planvpn) and [sizing](/documentation/articles/remoteapp-vnetsizing) information. -->
2.	Create a <!-- keep by customization: begin --> RemoteApp <!-- keep by customization: end --> collection.
<!-- deleted by customization
2.	Join your collection to your local domain.
-->
<!-- keep by customization: begin -->
2.	Link your collection to your virtual network.
<!-- keep by customization: end -->
3.	Add a template image to your collection.
4.	Configure directory synchronization. <!-- deleted by customization Azure --> RemoteApp requires that you integrate with Azure Active Directory by either 1) configuring Azure Active Directory Sync with the Password Sync option, or 2) configuring Azure Active Directory Sync without the Password Sync option but using a domain that is federated to AD FS. Check out the [configuration info for Active Directory with RemoteApp](/documentation/articles/remoteapp-ad).
5.	Publish RemoteApp apps.
6.	Configure user access.

**Before you begin**

You need to do the following before creating the collection:

<!-- deleted by customization
- [Sign up](/home/features/remoteapp/) for Azure RemoteApp. 
- Create a user account in Active Directory to use as the Azure RemoteApp service account. Restrict the permissions for this account so that it can only join machines to the domain.
-->
<!-- keep by customization: begin -->
- [Sign up](http://www.windowsazure.cn/services/remoteapp/) for RemoteApp. 
- Create a user account in Active Directory to use as the  RemoteApp service account. Restrict the permissions for this account so that it can only join machines to the domain.
<!-- keep by customization: end -->
- Gather information about your on-premises network: IP address information and VPN device details.
- Install the [Azure PowerShell](/documentation/articles/powershell-install-configure) module.
- Gather information about the users that you want to grant access to. You will need the Azure Active Directory user principal name (for example, name@contoso.com) for each user. <!-- deleted by customization Make sure that the UPN matches between Azure AD and Active Directory. -->
- Choose your template image. <!-- deleted by customization An Azure --><!-- keep by customization: begin --> A <!-- keep by customization: end --> RemoteApp template image contains the apps and programs that you want to publish for your users. See <!-- deleted by customization [Azure RemoteApp --><!-- keep by customization: begin --> [RemoteApp <!-- keep by customization: end --> image options](/documentation/articles/remoteapp-imageoptions) for more information.
<!-- deleted by customization
- Want to use the Office 365 ProPlus image? Check out info [here](/documentation/articles/remoteapp-officesubscription).
-->
- [Configure Active Directory for RemoteApp](/documentation/articles/remoteapp-ad).



## Step 1: Set up your virtual network
You can deploy a hybrid <!-- keep by customization: begin --> RemoteApp <!-- keep by customization: end --> collection that uses an existing Azure virtual network, or you can create a new virtual network. A virtual network lets your users access data on your local network through RemoteApp remote resources. Using an Azure virtual network gives your collection direct network access to other Azure services and virtual machines deployed to that virtual network.
<!-- deleted by customization

Make sure you review the [VNET planning](/documentation/articles/remoteapp-planvnet) and [VNET size](/documentation/articles/remoteapp-vnetsizing) information before you create your VNET.
-->

### Create an Azure VNET and join it to your Active Directory deployment

Start by creating a [virtual <!-- deleted by customization network](/documentation/articles/virtual-networks-create-vnet) --><!-- keep by customization: begin --> network](/documentation/articles/networking/virtual-networks-create-vnet) <!-- keep by customization: end -->. This is done on the **Network** tab in the Azure Management portal. You need to connect your virtual network to the Active Directory deployment that is synchronized to your Azure Active Directory tenant.

See [About Virtual Network Settings in the Management <!-- deleted by customization Portal](/documentation/articles/virtual-networks-settings) --><!-- keep by customization: begin --> Portal](/documentation/articles/networking/virtual-networks-settings) <!-- keep by customization: end --> for more information.

### Make sure your virtual network is ready for <!-- deleted by customization Azure --> RemoteApp
Before you create your <!-- keep by customization: begin --> RemoteApp <!-- keep by customization: end --> collection, let's make sure that your new virtual network is ready. You can validate this by doing the following:

1. Create an Azure virtual machine inside the subnet of the virtual network you just created for RemoteApp.
2. Use Remote Desktop to connect to the virtual machine. (Click **Connect**.)
3. Join it to the same Active Directory deployment that you want to use for RemoteApp.

Did that work? Your virtual network and subnet are ready for <!-- deleted by customization Azure --> RemoteApp!

You can find more information about creating Azure virtual machines and connecting to them with Remote Desktop [here](https://msdn.microsoft.com/zh-cn/library/azure/jj156003.aspx).

## Step 2: Create <!-- deleted by customization an Azure --><!-- keep by customization: begin --> a <!-- keep by customization: end --> RemoteApp collection ##



1. In the [Azure Management Portal](http://manage.windowsazure.cn), go to the <!-- deleted by customization Azure --> RemoteApp page.
2. Click **New > Create with VNET**.
3. Enter a name for your collection.
4. Choose the plan that you want to use - standard or basic.
<!-- deleted by customization
5. Choose your VNET from the drop down list and then your subnet.
6. Choose to join it to your domain.
-->
5. Click **Create RemoteApp collection**.

After your <!-- deleted by customization Azure --> RemoteApp collection has been created, double-click the name of the collection. That will bring up the **Quick Start** page - this is where you finish configuring the collection.

<!-- deleted by customization
Did something go wrong? Check out the [hybrid collection troubleshooting information](/documentation/articles/remoteapp-hybridtrouble).

## Step 3: Link your collection to the local domain ##

 
1. On the **Quick Start** page, click **join a local domain**.
2. Add the Azure RemoteApp service account to your local Active Directory domain. You will need the domain name, organizational unit, service account user name and password.
-->
<!-- keep by customization: begin -->
## Step 3: Link your collection to the virtual network ##

 
1. On the **Quick Start** page, click **link a virtual network**.
2. Choose the virtual network you want to use from the drop-down list.
3. Choose the region you want to use, and make sure the correct subscription shows up in the field. 
5. Back on the **Quick Start** page, click **join local domain**. Add the  RemoteApp service account to your local Active Directory domain. You will need the domain name, organizational unit, service account user name and password.
<!-- keep by customization: end -->

	This is the information you gathered if you followed the steps in [Configure Active Directory for Azure RemoteApp](/documentation/articles/remoteapp-ad).


## Step 4: Link to <!-- deleted by customization an Azure --><!-- keep by customization: begin --> a <!-- keep by customization: end --> RemoteApp image ##

<!-- deleted by customization An Azure --><!-- keep by customization: begin --> A <!-- keep by customization: end --> RemoteApp template image contains the programs that you want to share with users. You can either create a new [template image](/documentation/articles/remoteapp-imageoptions) or link to an existing image (one already imported or uploaded to Azure RemoteApp). You can also link to one of the <!-- deleted by customization Azure --> RemoteApp [template images](/documentation/articles/remoteapp-images) that contain Office 365 or Office 2013 (for trial use) programs.

If you are uploading the new image, you need to enter the name and choose the location for the image. On the next page of the wizard, you'll see a set of PowerShell cmdlets - copy and run these cmdlets from an elevated Windows PowerShell prompt to upload the specified image.

If you are linking to an existing template image, simply specify the image name, location, and associated Azure subscription.



## Step 5: Configure Active Directory directory synchronization ##

<!-- deleted by customization Azure --> RemoteApp requires that you integrate with Azure Active Directory by either 1) configuring Azure Active Directory Sync with the Password Sync option, or 2) configuring Azure Active Directory Sync without the Password Sync option but using a domain that is federated to AD FS. <!-- keep by customization: begin --> See [Directory synchronization roadmap](http://msdn.microsoft.com//library/azure/hh967642.aspx) for planning information and detailed steps. <!-- keep by customization: end -->

<!-- deleted by customization
Check out [AD Connect](http://blogs.technet.com/b/ad/archive/2014/08/04/connecting-ad-and-azure-ad-only-4-clicks-with-azure-ad-connect.aspx) - this article helps you set up directory integration in 4 steps.

See [Directory synchronization roadmap](http://msdn.microsoft.com//library/azure/hh967642.aspx) for planning information and detailed steps.

## Step 6: Publish apps ##

An Azure RemoteApp app is the app or program that you provide to your users. It is located in the template image you uploaded for the collection. When a user accesses an app, it appears to run in their local environment, but it is really running in Azure. 

Before your users can access apps, you need to publish them to the end-user feed - a list of available apps that your users access through the Remote Desktop client.
 
You can publish multiple apps to your  collection. From the  publishing page, click **Publish** to add an app. You can either publish from the **Start** menu of the template image or by specifying the path on the template image for the app. If you choose to add from the **Start** menu, choose the program to add. If you choose to provide the path to the app, provide a name for the app and the path to where it is installed on the template image.
-->
<!-- keep by customization: begin -->
## Step 6: Publish RemoteApp apps ##

A RemoteApp app is the app or program that you provide to your users. It is located in the template image you uploaded for the collection. When a user accesses an app, it appears to run in their local environment, but it is really running in Azure. 

Before your users can access RemoteApp apps, you need to publish them to the end-user feed - a list of available apps that your users access through the Remote Desktop client.
 
You can publish multiple apps to your RemoteApp collection. From the RemoteApp publishing page, click **Publish** to add an app. You can either publish from the Start menu of the template image or by specifying the path on the template image for the app. If you choose to add from the Start menu, choose the program to app. If you choose to provide the path to the app, provide a name for the app and the path to where it is installed on the template image.
<!-- keep by customization: end -->

## Step 7: Configure user access ##

Now that you have created your <!-- keep by customization: begin --> RemoteApp <!-- keep by customization: end --> collection, you need to add the users that you want to be able to use your remote resources. The users that you provide access to need to exist in the Active Directory tenant associated with the subscription you used to create this <!-- deleted by customization Azure --> RemoteApp collection.

1.	From the Quick Start page, click **Configure user access**. 
2.	Enter the work account (from Active Directory) or Microsoft account that you want to grant access for.

	**Notes:** 

	Make sure that you use the “user@domain.com” format.

	If you are using Office 365 ProPlus in your collection, you must use the Active Directory identities for your users. This helps validate licensing. 


3.	Once the users are validated, click **Save**.


## Next steps ##
That's it - you have successfully created and deployed your <!-- deleted by customization Azure --> RemoteApp hybrid collection. The next step is to have your users download and install the Remote Desktop client. You can find the URL for the client on the <!-- deleted by customization Azure --> RemoteApp Quick Start page. Then, have users log into the client and access the apps you published.


 
<!-- deleted by customization
### Help us help you 
Did you know that in addition to rating this article and making comments down below, you can make changes to the article itself? Something missing? Something wrong? Did I write something that's just confusing? Scroll up and click **Edit on GitHub** to make changes - those will come to us for review, and then, once we sign off on them, you'll see your changes and improvements right here.
-->