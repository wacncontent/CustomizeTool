<properties
   pageTitle="Run any Windows app on any device with Azure RemoteApp | Windows Azure"
   description="Learn how to share any Windows app with your users by using Azure RemoteApp."
   services="remoteapp"
   documentationCenter=""
   authors="lizap"
   manager="mbaldwin"
   editor=""/>

<tags
	ms.service="remoteapp"
	ms.date="11/05/2015"
	wacn.date=""/>

# Run any Windows app on any device with Azure RemoteApp

<!-- deleted by customization You can --><!-- keep by customization: begin --> This tutorial will show you how to <!-- keep by customization: end --> run a Windows application anywhere on any device, right now, seriously <!-- deleted by customization - just by using Azure RemoteApp -->. Whether it's <!-- keep by customization: begin --> Internet Explorer 6, <!-- keep by customization: end --> a custom application written 10 years ago, or an Office app, your users no longer have to be tied to a specific operating system (like Windows XP) for those few applications.

<!-- deleted by customization With --><!-- keep by customization: begin --> By using <!-- keep by customization: end --> Azure RemoteApp, your users can also use their own Android or Apple devices and get the same experience they got on Windows (or on Windows Phones). This is accomplished by hosting your Windows application in a collection of Windows virtual machines on Azure <!-- deleted by customization - --><!-- keep by customization: begin --> where <!-- keep by customization: end --> your users can access them from anywhere they have an internet connection.

<!-- deleted by customization
Read on for an example of exactly how to do this.

In this article, we're going to share Access with all of our users. However, you can use ANY app. As long as you can install your app on a Windows Server 2012 R2 computer, you can share it using the steps below. You can review the [app requirements](/documentation/articles/remoteapp-appreqs) to make sure your app will work.
-->
<!-- keep by customization: begin -->
For this tutorial, we're going to share Access with all of our users. However, you can use ANY app. As long as you can install your app on a Windows Server 2012 R2 computer, you can share it using the steps below. You can review the [app requirements](/documentation/articles/remoteapp-appreqs) to make sure your app will work.
<!-- keep by customization: end -->

Please note that because Access is a database, and we want that database to be useful, we will be doing a few extra steps to let users access the Access data share. If your app isn't a database, or you don't need your users to be able to access a file share, you can skip those steps in this tutorial

[AZURE.INCLUDE [free-trial-note](../includes/free-trial-note.md)]


## Create a collection in RemoteApp

Start by creating a collection. The collection serves as a container for your apps and users. Each collection is based on an image - you can create your own or use one provided with your subscription. For this tutorial, we're using the Office 2013 trial image - it contains the app that we want to share.

1. In the Azure <!-- deleted by customization Management Portal --><!-- keep by customization: begin --> management portal <!-- keep by customization: end -->, scroll down in the left hand <!-- deleted by customization nav tree --><!-- keep by customization: begin --> navigation <!-- keep by customization: end --> until you see <!-- keep by customization: begin --> Azure <!-- keep by customization: end --> RemoteApp. Open that page.
2. Click **Create a RemoteApp collection**.
3. Click **Quick create** and enter a name for your collection.
4. Select the region you want to use to create your collection. For the best experience, select the region that is closest geographically to the location where your users will access the app. For example, in this tutorial, the users will be located in Redmond, Washington. The closest Azure region is **China North**.
5. Select the billing plan you want to use. The basic billing plan puts 16 users on a large Azure VM, while the standard billing plan has 10 users on a large Azure VM. As a general example, the basic plan works great for data entry-type workflow. For a productivity app, like Office, you'd want the standard plan.
6. Finally, select the  Office 2013 Professional image. This image contains Office 2013 apps. <!-- deleted by customization Just a reminder - this image is only good for trial collections and POCs. You' can't use this image in a production collection. -->
7. Now, click **Create RemoteApp collection**.

![Create a cloud collection in RemoteApp](./media/remoteapp-anyapp/ra-anyappcreatecollection.png)

This starts creating your collection, but it can take up to an hour.

Now you're ready to add your users.

## Share the app with users

Once your collection has been created successfully, itâs time to publish Access to users and add the users who should have access to it.

If you have navigated away from the Azure RemoteApp node while the collection was being created, start by making your way back to it from the Azure home page.

<!-- keep by customization: begin -->
1. Click **RemoteApp** in the left hand navigation.
<!-- keep by customization: end -->
2. Click the collection you created earlier to access additional options and configure the collection.
![A new RemoteApp cloud collection](./media/remoteapp-anyapp/ra-anyappcollection.png)
3. On the **Publishing** tab, click **Publish** at the bottom of the screen, and then click **Publish Start menu programs**.
![Publish a RemoteApp program](./media/remoteapp-anyapp/ra-anyapppublish.png)
4. Select the apps you want to publish from the list. For our purpose, we chose Access. Click **Complete**. Wait for the apps to finish publishing.
![Publishing Access in RemoteApp](./media/remoteapp-anyapp/ra-anyapppublishaccess.png)


1. Once the app has finished publishing, head over to the **User Access** tab to add all the users that need access to your apps. Enter user names (email address) for your users and then click **Save**.
<!-- deleted by customization

![Add users to RemoteApp](./media/remoteapp-anyapp/ra-anyappaddusers.png)


1. Now, itâs time to tell your users about these new apps and how to access them. To do this, send your users an email pointing them to the Remote Desktop client download URL.
![The client download URL for RemoteApp](./media/remoteapp-anyapp/ra-anyappurl.png)
-->
<!-- keep by customization: begin -->
![Add users to RemoteApp](./media/remoteapp-anyapp/ra-anyappaddusers.png)


1. Now, itâs time to tell your users about these new apps  how to access them. To do this, send your users an email pointing them to the Remote Desktop client download URL.
![The client download URL for RemoteApp](./media/remoteapp-anyapp/ra-anyappurl.png)
<!-- keep by customization: end -->

## Configure access to Access

Some apps need extra configuration after you deploy them through RemoteApp. In particular, for Access, we're going to create a file share on Azure that any user can access. (If you don't want to do that, you can create a [hybrid collection](/documentation/articles/remoteapp-create-hybrid-deployment) [instead of our cloud collection] that lets your users access files and information on your local network.) Then, we'll need to tell our users to map a local drive on their computer to the Azure file system.

The first part you as the admin do. Then, we have some steps for your users.

1. Start by publishing the command line interface (cmd.exe). In the **Publishing** tab, select **cmd**, and then click **Publish > Publish program using path**.
2. Enter the name of the app and the path. For our purpose, use "File Explorer" as the name and "%SYSTEMDRIVE%\windows\explorer.exe" as the path.
![Publish the cmd.exe file.](./media/remoteapp-anyapp/ra-publishcmd.png)
3. Now you need to create an Azure [storage account](/documentation/articles/storage-create-storage-account). We named ours "accessstorage," so pick a name that's meaningful to you <!-- deleted by customization. (To misquote Highlander, there --><!-- keep by customization: begin --> (there <!-- keep by customization: end --> can be only one <!-- deleted by customization "accessstorage.") --><!-- keep by customization: begin --> "accessstorage"). <!-- keep by customization: end -->
![Our Azure storage account](./media/remoteapp-anyapp/ra-anyappazurestorage.png)
4. Now go back to your dashboard so you can get the path to your storage (endpoint location). You'll use this in a bit, so make sure you copy it somewhere.
<!-- deleted by customization
![The storage account path](./media/remoteapp-anyapp/ra-anyappstoragelocation.png)
-->
<!-- keep by customization: begin -->

![The storage account path](./media/remoteapp-anyapp/ra-anyappstoragelocation.png)
<!-- keep by customization: end -->
5. Next, once the storage account has been created, you need the primary access key. Click **Manage access keys**, and then copy the primary access key.
6. Now, set the context of the storage account <!-- deleted by customization and --><!-- keep by customization: begin -->, <!-- keep by customization: end --> create a new file share for Access. Run the following cmdlets in an elevated Windows PowerShell window:

        $ctx=New-AzureStorageContext <account name> <account key>
    	$s = New-AzureStorageShare <share name> -Context $ctx

	So for our share, these are the cmdlets we run:

	    $ctx=New-AzureStorageContext accessstorage <key>
    	$s = New-AzureStorageShare <share name> -Context $ctx


Now, it's the user's turn. First, have your users install a [RemoteApp client](/documentation/articles/remoteapp-clients). Next, the users need to map a drive from their account to that Azure file share you created and add their Access files. This is how they do that:

1. In the RemoteApp client, access the published apps. Start the cmd.exe program.
2. Run the following command to map a drive from your computer to the file share:

		net use z: \\<accountname>.file.core.chinacloudapi.cn\<share name> /u:<user name> <account key>

	If you set the **/persistent** parameter to yes, the mapped drive will persist across sessions.
1. Now, launch the File Explorer app from RemoteApp. Copy any Access files you want to use in the shared app to the file share.
![Putting Access files in an Azure share](./media/remoteapp-anyapp/ra-anyappuseraccess.png)
1. Finally, open Access, and then open the database that you just shared. You should see your data in Access running from the cloud.
![A real Access database running from the cloud](./media/remoteapp-anyapp/ra-anyapprunningaccess.png)

Now you can use Access on any of your devices - just make sure you install a RemoteApp client.

<!--Every topic should have next steps and links to the next logical set of content to keep the customer engaged-->
## Next steps

Now that you've mastered creating a collection, try creating a [collection that uses Office 365](/documentation/articles/remoteapp-tutorial-o365anywhere). Or you can create a [hybrid collection ](/documentation/articles/remoteapp-create-hybrid-deployment)that can access your local network.

<!--Image references-->