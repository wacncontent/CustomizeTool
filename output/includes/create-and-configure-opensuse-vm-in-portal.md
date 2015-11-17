<!-- deleted by customization
<properties writer="kathydav" editor="tysonn" manager="timlt" />

1. Sign in to the [Azure Management Portal](http://manage.windowsazure.cn). Check out the [Trial](/pricing/1rmb-trial/) offer if you don't have a subscription yet.

2. On the command bar at the bottom of the window, click **New**.

3. Under **Compute**, click **Virtual Machine**, and then click **From Gallery**.

	![Create a New Virtual Machine][Image1]

4. Under the **SUSE** group, select an OpenSUSE virtual machine image, and then click arrow to continue.

5. On the first **Virtual machine configuration** page:

	- Type a **Virtual Machine Name**, such as "testlinuxvm".
	- Verify the **Tier** and pick a **Size**. The tier determines the sizes you can choose from. The size affects the cost of using it, as well as configuration options such as how many data disks you can attach. For details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-size-specs).
	- Type a **New User Name**, or accept the default, **azureuser**. This name is added to the Sudoers list file.
	- Decide which type of **Authentication** to use. For general password guidelines, see [Strong passwords](http://msdn.microsoft.com/zh-cn/library/ms161962.aspx).

6. On the next **Virtual machine configuration** page:

	- Use the default **Create a new cloud service**.
	- In the **DNS Name** box, type a valid DNS name to use as part of the address, such as "testlinuxvm".
-->
<!-- keep by customization: begin -->
<properties writer="kathydav" editor="tysonn" manager="jeffreyg" /> 

**Important**: If you want your virtual machine to use a virtual network, make sure you specify the virtual network when you create the virtual machine. A virtual machine can be configured to join a virtual network only when you create the virtual machine. For more information about virtual networks, see [Azure Virtual Network Overview](https://msdn.microsoft.com/zh-cn/library/azure/jj156007.aspx).


1. Login to the [Azure Management Portal][AzurePreviewPortal] using your Azure account.

2. In the Management Portal, at the bottom left of the web page, click **+New**, click **Virtual Machine**, and then click **From Gallery**.

	![Create a New Virtual Machine][Image1]

3. Select an OpenSUSE virtual machine image from **Platform Images**, and then click the next arrow at the bottom right of the page.


4. On the **Virtual machine configuration** page, provide the following information:

	- Provide a **Virtual Machine Name**, such as "testlinuxvm".
	- Specify a **New User Name**, such as "newuser", which will be added to the Sudoers list file.
	- In the **New Password** box, type a [strong password](http://msdn.microsoft.com/zh-cn/library/ms161962.aspx).
	- In the **Confirm Password** box, retype the password.
	- Select the appropriate **Size** from the drop down list.

	Click the next arrow to continue.

5. On the **Virtual machine mode** page, provide the following information:
	- Select **Standalone Virtual Machine**.
	- In the **DNS Name** box, type a valid DNS address.  For example, "testlinuxvm".
<!-- keep by customization: end -->
	- In the **Region/Affinity Group/Virtual Network** box, select a region where this virtual image will be hosted.
<!-- deleted by customization
	- Under **Endpoints**, keep the SSH endpoint. You can add others now, or add, change, or delete them after the virtual machine is created.

	>[AZURE.NOTE] If you want a virtual machine to use a virtual network, you **must** specify the virtual network when you create the virtual machine. You can't add a virtual machine to a virtual network after you create the virtual machine. For more information, see [Virtual Network Overview](/documentation/articles/virtual-networks-overview).

7.	On the last **Virtual machine configuration** page, keep the default settings and then click the check mark to finish.

The portal lists the new virtual machine under **Virtual Machines**. While the status is reported as **(Provisioning)**, the virtual machine is being set up. When the status is reported as **Running**, you can move on to the next step.
-->
<!-- keep by customization: begin -->

   Click the next arrow to continue.
	
6. On the **Virtual machine options** page, select **(none)** in the **Availability Set** box. Click the check mark to continue.
	
7. Wait while Azure prepares your virtual machine.

##Configure Endpoints
Once the virtual machine is created you must configure endpoints in order to remotely connect.

1. In the Management Portal, click **Virtual Machines**, then click the name of your new virtual machine, then click **Endpoints**.

2. Click **Edit Endpoint** at the bottom of the page, and edit the SSH endpoint so that its **Public Port** is 22.
<!-- keep by customization: end -->

##Connect to the Virtual Machine
<!-- deleted by customization

You'll use SSH or PuTTY to connect to the virtual machine, depending on the operating system on the computer you'll connect from:

- From a computer running Linux, use SSH. At the command prompt, type:

	`$ ssh newuser@testlinuxvm.chinacloudapp.cn -o ServerAliveInterval=180`

	Type the user's password.

- From a computer running Windows, use PuTTY. If you don't have it installed, download it from the [PuTTY Download Page][PuTTYDownload].

	Save **putty.exe** to a directory on your computer. Open a command prompt, navigate to that folder, and run **putty.exe**.

	Type the host name, such as "testlinuxvm.chinacloudapp.cn", and type "22" for the **Port**.

	![PuTTY Screen][Image6]  
-->
<!-- keep by customization: begin -->
When the virtual machine has been provisioned and the endpoints configured you can connect to it using SSH or PuTTY.

###Connecting Using SSH
If you are using a linux computer, connect to the VM using SSH.  At the command prompt, run:

	$ ssh newuser@testlinuxvm.chinacloudapp.cn -o ServerAliveInterval=180

Enter the user's password.

###Connecting using PuTTY
If you are using a Windows computer, connect to the VM using PuTTY. PuTTY can be downloaded from the [PuTTY Download Page][PuTTYDownLoad]. 

1. Download and save **putty.exe** to a directory on your computer. Open a command prompt, navigate to that folder, and execute **putty.exe**.

2. Enter "testlinuxvm.chinacloudapp.cn" for the **Host Name** and "22" for the **Port**.
![PuTTY Screen][Image6]  
<!-- keep by customization: end -->

##Update the Virtual Machine (optional)
<!-- deleted by customization

1. After you're connected to the virtual machine, you can optionally install system updates and patches. To run the update, type:
-->
<!-- keep by customization: begin -->
1. Once you've connected to the virtual machine, you can optionally install system updates and patches. Run:
<!-- keep by customization: end -->

	`$ sudo zypper update`

<!-- deleted by customization
2. Select **Software**, then **Online Update** to list available updates. Select **Accept** to start the installation and apply all new available patches (except the optional ones).

3. After installation is done, select **Finish**.  Your system is now up to date.
-->
<!-- keep by customization: begin -->
2. Select **Software** then **Online Update**.  A list of updates is displayed.  Select **Accept** to start the installation and apply all new patches (except the optional ones) that are currently available for your system. 

3. After installation is complete, select **Finish**.  Your system is now up to date.
<!-- keep by customization: end -->

[PuTTYDownload]: http://www.puttyssh.org/download.html
<!-- keep by customization: begin -->
[AzurePreviewPortal]: http://manage.windowsazure.cn
<!-- keep by customization: end -->

[Image1]: ./media/create-and-configure-opensuse-vm-in-portal/CreateVM.png

[Image6]: ./media/create-and-configure-opensuse-vm-in-portal/putty.png
