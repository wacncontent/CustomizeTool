<properties
	pageTitle="Unable to connect to an Azure VM over SSH | Windows Azure"
	description="Troubleshoot Secure Shell (SSH) connections to an Azure virtual machine running Linux."
	services="virtual-machines"
	documentationCenter=""
	authors="dsk-2015"
	manager="timlt"
	editor=""
	tags="top-support-issue,azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/05/2015"
	wacn.date=""/>

# Troubleshoot Secure Shell (SSH) connections to a Linux-based Azure virtual machine

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-both-include.md)]



There could be various causes of SSH failures to a Linux-based Azure virtual machine. This article will help you find them out and correct the failures.

> [AZURE.NOTE] This article only applies to Azure virtual machines running Linux. For troubleshooting connections to Azure virtual machines running Windows, see [this article](/documentation/articles/virtual-machines-troubleshoot-remote-desktop-connections).

## Contact Azure Customer Support

If you need more help at any point in this article, you can contact the Azure experts on [the MSDN Azure and the Stack Overflow forums](http://azure.microsoft.com/support/forums/).

Alternatively, you can file an Azure support incident. Go to the [Azure Support site](http://azure.microsoft.com/support/options/) and click **Get support**. For information about using Azure Support, read the [Windows Azure Support FAQ](/support/faq/).


## Basic steps - classic deployment model

To resolve the more common SSH connection failures in virtual machines created using the classic deployment model, try these steps:

1. **Reset Remote Access** from the [Azure preview portal](https://manage.windowsazure.cn). Click **Browse all** > **Virtual machines (classic)** > your Windows virtual machine > **Reset Remote Access**.

	![Reset Remote Access](./media/virtual-machines-troubleshoot-ssh-connections/Portal-SSH-Reset-Windows.png)  

2. **Restart** the virtual machine. From the [Azure preview portal](https://manage.windowsazure.cn), click **Browse all** > **Virtual machines (classic)** > your Windows virtual machine > **Restart**. From the [Azure management portal](https://manage.windowsazure.cn), open the **Virtual machines** > **Instances** and click **Restart**.

3. [**Resize** the virtual machine](https://msdn.microsoft.com/zh-cn/library/dn168976.aspx).

4. Follow the instructions in [How to reset a password or SSH for Linux-based virtual machines](/documentation/articles/virtual-machines-linux-use-vmaccess-reset-password-or-ssh) on the virtual machine, to:

	- Reset the password or SSH key.
	- Create a new sudo user account.
	- Reset the SSH configuration.


## Basic steps - Resource Manager deployment model

To resolve the common SSH issues for virtual machines created using the Resource Manager deployment model, try the following steps.

1. **Reset the SSH connection** to your Linux VM on the command line, using either the Azure CLI or Azure PowerShell. Make sure the [Windows Azure Linux Agent](/documentation/articles/virtual-machines-linux-agent-user-guide) version 2.0.5 or later is installed.

	**Using Azure CLI**

	a. If you haven't already, [install the Azure CLI and connect to your Azure subscription](/documentation/articles/xplat-cli-install) using the `azure login` command.

	b. Switch to the Resource Manager mode.

	```
	azure config mode arm
	```

	c. Reset the SSH connection using either of the following methods.

	* Use the `vm reset-access` command as in the following example.

	```
	azure vm reset-access -g TestRgV2 -n TestVmV2 -r
	```

	This will install the `VMAccessForLinux` extension on your virtual machine.

	* Alternatively, create a file named PrivateConf.json with the following content:

	```
	{  
	"reset_ssh":"True"
	}
	```

	Then manually run the `VMAccessForLinux` extension to reset your SSH connection.

	```
	azure vm extension set "testRG" "testVM" VMAccessForLinux Microsoft.OSTCExtensions "1.2" --private-config-path PrivateConf.json
	```

	**Using Azure PowerShell**

	a. If you haven't already, [install Azure PowerShell and connect to your Azure subscription](/documentation/articles/powershell-install-configure) using the Azure AD method.

	b. Switch to the Resource Manager mode.

	```
	Switch-AzureMode -Name AzureResourceManager
	```

	c. Run the `VMAccessForLinux` extension to reset your SSH connection, as shown in the following example.

	```
	Set-AzureVMExtension -ResourceGroupName "testRG" -VMName "testVM" -Location "China North" -Name "VMAccessForLinux" -Publisher "Microsoft.OSTCExtensions" -ExtensionType "VMAccessForLinux" -TypeHandlerVersion "1.2" -SettingString "{}" -ProtectedSettingString '{"reset_ssh":true}'
	```

2. **Restart** your Linux VM from the portal. From the [Azure preview portal](https://manage.windowsazure.cn), click **Browse all** > **Virtual machines** > your Windows virtual machine > **Restart**.

	![Restart V2](./media/virtual-machines-troubleshoot-ssh-connections/Portal-SSH-Restart-V2-Windows.png)  

3. **Reset your password or the SSH key** for your Linux VM on the command line, using either the Azure CLI or Azure PowerShell. You can also create a new username and password with sudo authority as shown in the following example.

	**Using Azure CLI**

	Install and configure Azure CLI as mentioned above. Switch to Resource Manager mode and then run the extension using either of the following methods.

	* Run the `vm reset-access` command to set any of the SSH credentials.

	```
	azure vm reset-access TestRgV2 TestVmV2 -u NewUser -p NewPassword
	```

	See more information about this by typing `azure vm reset-access -h` on the command line.

	* Alternatively, create a file named PrivateConf.json with the following contents.
	```
	{
	"username":"NewUsername", "password":"NewPassword", "expiration":"2016-01-01", "ssh_key":"", "reset_ssh":false, "remove_user":""
	}
	```

	Then run the Linux extension using the above file.

	```
	$azure vm extension set "testRG" "testVM" VMAccessForLinux Microsoft.OSTCExtensions "1.2" --private-config-path PrivateConf.json
	```

	Note that you can follow steps similar to [How to reset a password or SSH for Linux-based virtual machines](/documentation/articles/virtual-machines-linux-use-vmaccess-reset-password-or-ssh) to try other variations. Remember to modify the Azure CLI instructions for the Resource Manager mode.

	**Using Azure PowerShell**

	Install and configure Azure PowerShell as mentioned above. Switch to Resource Manager mode and then run the extension as follows.

	```
	$RGName = 'testRG'
	$VmName = 'testVM'
	$Location = 'China North'

	$ExtensionName = 'VMAccessForLinux'
	$Publisher = 'Microsoft.OSTCExtensions'
	$Version = '1.2'

	$PublicConf = '{}'
	$PrivateConf = '{"username":"NewUsername", "password":"NewPassword", "ssh_key":"", "reset_ssh":false, "remove_user":""}'

	Set-AzureVMExtension -ResourceGroupName $RGName -VMName $VmName -Location $Location -Name $ExtensionName -Publisher $Publisher -ExtensionType $ExtensionName -TypeHandlerVersion $Version -SettingString $PublicConf -ProtectedSettingString $PrivateConf

	```

	Make sure to replace the values of $RGName, $VmName, $Location, and the SSH credentials with values specific to your installation.

## Detailed troubleshooting

If the SSH client still cannot reach the SSH service on the virtual machine, it can be due to many reasons. Here are the components involved.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot1.png)

The following sections will help you isolate the source of the failure and figure out solutions or workarounds.

### Steps before troubleshooting

First, check the status of virtual machine in the Azure Management Portal.

In the [Azure management portal](https://manage.windowsazure.cn), for virtual machines in classic deployment model:
-->
<!-- keep by customization: begin -->
If you can't connect to Linux-based Azure virtual machines, this article describes a methodical approach for isolating and correcting the problem. This applies to both Resource Manager and Classic deployment models.

## Step 1: Reset the SSH configuration, key, or password

Follow the instructions in [How to reset a password or SSH for Linux-based virtual machines](/documentation/articles/virtual-machines-linux-use-vmaccess-reset-password-or-ssh) on the virtual machine. With these instructions, you can:

- Reset the password or SSH key.
- Create a new sudo user account.
- Reset the SSH configuration.

If the SSH client still cannot reach the SSH service on the virtual machine, it can be due to many causes. Here is the set of components involved.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot1.png)

The following sections step through isolating and determining the various causes for this problem and providing solutions and workarounds.

## Step 2: Preliminary steps before detailed troubleshooting

First, check the status of virtual machine in the Azure management portal or the Azure preview portal.

In the Azure management portal:
<!-- keep by customization: end -->

1. Click **Virtual machines** > *VM name*.
<!-- deleted by customization
2. Click the VM's **Dashboard** to check its status.
-->
<!-- keep by customization: begin -->
2. Click **Dashboard** for the virtual machine to check its status.
<!-- keep by customization: end -->
3. Click **Monitor** to see recent activity for compute, storage, and network resources.
4. Click **Endpoints** to ensure that there is an endpoint for SSH traffic.

<!-- deleted by customization
In the [Azure preview portal](https://manage.windowsazure.cn):

1. For a virtual machine created in classic deployment model, click **Browse** > **Virtual machines (classic)** > *VM name*. For a virtual machine created using the Resource Manager, click **Browse** > **Virtual machines** > *VM name*. The status pane for the virtual machine should show **Running**. Scroll down to show recent activity for compute, storage, and network resources.
2. Click **Settings** to examine endpoints, IP addresses, and other settings. To identify endpoints in virtual machines created with the Resource Manager, check if a [Network Security Group](/documentation/articles/virtual-networks-nsg) is defined, the rules applied to it and if they are referenced in the subnet.

To verify network connectivity, check the configured endpoints and see if you can reach the VM through another protocol, such as HTTP or another service.
-->
<!-- keep by customization: begin -->
In the Azure preview portal:

1. Click **Browse** > **Virtual machines** > *VM name*. For a virtual machine created in Azure Resource Manager, click **Browse** > **Virtual machines (v2)** > *VM name*. The status pane for the virtual machine should show **Running**. Scroll down to show recent activity for compute, storage, and network resources.
2. Click **Settings** to examine endpoints, IP addresses, and other settings. 

To verify network connectivity, analyze the configured endpoints and determine if you can reach the virtual machine through another protocol, such as HTTP or another known service.

If needed, restart the virtual machine or [resize the virtual machine](/documentation/articles/virtual-machines-size-specs).
<!-- keep by customization: end -->

After these steps, try the SSH connection again.

<!-- deleted by customization

### Troubleshooting steps

The SSH client on your computer could fail to reach the SSH service on the Azure virtual machine due to these possible sources of issues or misconfigurations:
-->
<!-- keep by customization: begin -->
## Step 3: Detailed troubleshooting

The inability of your SSH client to reach the SSH service on the Azure virtual machine can be due to the following sources of issues or misconfigurations:
<!-- keep by customization: end -->

- SSH client computer
- Organization edge device
- Cloud service endpoint and access control list (ACL)
- Network Security Groups
- Linux-based Azure virtual machine

<!-- deleted by customization #### --><!-- keep by customization: begin --> ### <!-- keep by customization: end --> Source 1: SSH client computer

<!-- deleted by customization
To eliminate your computer as the source of the failure, check that it can make SSH connections to another on-premises, Linux-based computer.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot2.png)

If this fails, check for these on your computer:
-->
<!-- keep by customization: begin -->
To eliminate your computer as being the source of issues or misconfiguration, verify that your computer can make SSH connections to another on-premises, Linux-based computer.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot2.png)

If you cannot, check for these on your computer:
<!-- keep by customization: end -->

- A local firewall setting that is blocking inbound or outbound SSH traffic (TCP 22)
- Locally installed client proxy software that is preventing SSH connections
- Locally installed network monitoring software that is preventing SSH connections
- Other types of security software that either monitor traffic or allow/disallow specific types of traffic <!-- keep by customization: begin --> that is preventing SSH connections <!-- keep by customization: end -->

In all of these cases, <!-- keep by customization: begin --> try to <!-- keep by customization: end --> temporarily disable the software and <!-- deleted by customization try --><!-- keep by customization: begin --> attempt <!-- keep by customization: end --> an SSH connection to an on-premises computer to <!-- deleted by customization find out --><!-- keep by customization: begin --> determine <!-- keep by customization: end --> the cause. Then, work with your network administrator to correct the settings of the software to allow SSH connections.

If you are using certificate authentication, verify that you have these permissions to the .ssh folder in your home directory:

- Chmod 700 ~/.ssh
<!-- deleted by customization
- Chmod 644 ~/.ssh/\*.pub
- Chmod 600 ~/.ssh/id_rsa (or any other files that have your private keys stored in)
-->
<!-- keep by customization: begin -->
- Chmod 644 ~/.ssh/*.pub
- Chmod 600 ~/.ssh/id_rsa (or whatever other files you might have your private keys stored in)
<!-- keep by customization: end -->
- Chmod 644 ~/.ssh/known_hosts (contains hosts you’ve connected to via SSH)

<!-- deleted by customization #### --><!-- keep by customization: begin --> ### <!-- keep by customization: end --> Source 2: Organization edge device

To eliminate your organization edge device as <!-- keep by customization: begin --> being <!-- keep by customization: end --> the source of <!-- deleted by customization failure --><!-- keep by customization: begin --> issues or misconfiguration <!-- keep by customization: end -->, <!-- deleted by customization check --><!-- keep by customization: begin --> verify <!-- keep by customization: end --> that a computer directly connected to the Internet can make SSH connections to your Azure <!-- deleted by customization VM --><!-- keep by customization: begin --> virtual machine <!-- keep by customization: end -->. If you are accessing the <!-- deleted by customization VM --><!-- keep by customization: begin --> virtual machine <!-- keep by customization: end --> over a site-to-site VPN or ExpressRoute connection, skip to [Source 4: Network security groups](#nsg).

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot3.png)

If you do not have a computer that is directly connected to the Internet, you can easily create a new Azure virtual machine in its own resource group or cloud service and use it. For more information, see [Create a virtual machine running Linux in Azure](/documentation/articles/virtual-machines-linux-tutorial). Delete the resource group or virtual machine and cloud service when you are done with your testing.

If you can create an SSH connection with a computer directly attached to the Internet, check your organization edge device for:

- An internal firewall that is blocking SSH traffic with the Internet
- Your proxy server that is preventing SSH connections
- Intrusion detection or network monitoring software running on devices in your edge network that is preventing SSH connections

Work with your network administrator to correct the settings of your organization edge devices to allow SSH traffic with the Internet.

<!-- deleted by customization #### --><!-- keep by customization: begin --> ### <!-- keep by customization: end --> Source 3: Cloud service endpoint and ACL

<!-- deleted by customization
> [AZURE.NOTE] This source applies only for virtual machines created using classic deployment model. For virtual machines created using the Resource Manager, skip to [source 4: Network security groups](#nsg).

To eliminate the cloud service endpoint and ACL as the source of the failure, for VMs created using the [classic deployment model](/documentation/articles/resource-manager-deployment-model), check that another Azure VM in the same virtual network can make SSH connections to your VM.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot4.png)

If you do not have another VM in the same virtual network, you can easily create a new one. For more information, see [Create a virtual machine running Linux in Azure](/documentation/articles/virtual-machines-linux-tutorial). Delete the extra VM when you are done with your testing.

If you can create an SSH connection with a VM in the same virtual network, check:

- The endpoint configuration for SSH traffic on the target VM. The private TCP port of the endpoint should match the TCP port on which the SSH service on the VM is listening (default is 22). For VMs created in the Resource Manager deployment model using templates, verify the SSH TCP port number in the Azure preview portal with **Browse** > **Virtual machines (v2)** > *VM name* > **Settings** > **Endpoints**.
- The ACL for the SSH traffic endpoint on the target virtual machine. ACLs allow you to specify allowed or denied incoming traffic from the Internet, based on its source IP address. Misconfigured ACLs can prevent incoming SSH traffic to the endpoint. Check your ACLs to ensure that incoming traffic from public IP addresses of your proxy or other edge server are allowed. For more information, see [About network access control lists (ACLs)](/documentation/articles/virtual-networks-acl).

To eliminate the endpoint as a source of the problem, remove the current endpoint and create a new endpoint and specify the **SSH** name (TCP port 22 for the public and private port number). For more information, see [Set up endpoints on a virtual machine in Azure](/documentation/articles/virtual-machines-set-up-endpoints).

<a id="nsg"></a>
#### Source 4: Network security groups

Network security groups allow you to have more granular control of allowed inbound and outbound traffic. You can create rules that span subnets and cloud services in an Azure virtual network. Check your network security group rules to ensure that SSH traffic to and from the Internet is allowed.
-->
<!-- keep by customization: begin -->
To eliminate the cloud service endpoint and ACL as being the source of issues or misconfiguration for virtual machines created using the Service Management API, verify that another Azure virtual machine that is in the same virtual network can make SSH connections to your Azure virtual machine.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot4.png)

> [AZURE.NOTE] For virtual machines created in Azure Resource Manager, skip to [source 4: Network security groups](#nsg).

If you do not have another virtual machine in the same virtual network, you can easily create a new one. For more information, see [Create a virtual machine running Linux in Azure](/documentation/articles/virtual-machines-linux-tutorial). Delete the extra virtual machine when you are done with your testing.

If you can create an SSH connection with a virtual machine in the same virtual network, check:

- The endpoint configuration for SSH traffic on the target virtual machine. The private TCP port of the endpoint must match the TCP port on which the SSH service on the virtual machine is listening, which by default is 22. For virtual machines created in Azure Resource Manager using templates, verify the SSH TCP port number in the Azure preview portal with **Browse** > **Virtual machines (v2)** > *VM name* > **Settings** > **Endpoints**.
- The ACL for the SSH traffic endpoint on the target virtual machine. ACLs allow you to specify allowed or denied incoming traffic from the Internet, based on its source IP address. Misconfigured ACLs can prevent incoming SSH traffic to the endpoint. Examine your ACLs to ensure that incoming traffic from your public IP addresses of your proxy or other edge server are allowed. For more information, see [About network access control lists (ACLs)](/documentation/articles/networking/virtual-networks-acl).

To eliminate the endpoint as a source of the problem, remove the current endpoint and create a new endpoint, specifying the **SSH** name (TCP port 22 for the public and private port number). For more information, see [Set up endpoints on a virtual machine in Azure](/documentation/articles/virtual-machines-set-up-endpoints).

### <a id="nsg"></a>Source 4: Network security groups

Network security groups allow you to have more granular control of allowed inbound and outbound traffic. You can create rules that span subnets and cloud services in an Azure virtual network. Examine your network security group rules to ensure that SSH traffic to and from the Internet is allowed.
<!-- keep by customization: end -->
For more information, see [About network security groups](/documentation/articles/virtual-networks-nsg).

<!-- deleted by customization #### --><!-- keep by customization: begin --> ### <!-- keep by customization: end --> Source 5: Linux-based Azure virtual machine

The last source of possible problems is the Azure virtual machine itself.

![](./media/virtual-machines-troubleshoot-ssh-connections/ssh-tshoot5.png)

If you have not done so already, follow the instructions <!-- deleted by customization [to --><!-- keep by customization: begin --> in [How to <!-- keep by customization: end --> reset a password or SSH for Linux-based virtual machines](/documentation/articles/virtual-machines-linux-use-vmaccess-reset-password-or-ssh) on the virtual machine.

<!-- deleted by customization
Try connecting from your computer again. If it still fails, these are some of the possible problems:
-->
<!-- keep by customization: begin -->
Try the connection from your computer again. If you are not successful, here are some of the possible problems:
<!-- keep by customization: end -->

- The SSH service is not running on the target virtual machine.
- The SSH service is not listening on TCP port 22. To test this, install a telnet client on your local computer and run "telnet *cloudServiceName*.chinacloudapp.cn 22". This will <!-- deleted by customization find out if --><!-- keep by customization: begin --> determine whether <!-- keep by customization: end --> the virtual machine allows inbound and outbound communication to the SSH endpoint.
- The local firewall on the target virtual machine has rules that are preventing inbound or outbound SSH traffic.
- Intrusion detection or network monitoring software running on the Azure virtual machine is preventing SSH connections.


<!-- keep by customization: begin -->
## Step 4: Submit your issue to the Azure support forums

To get help from Azure experts around the world, you can submit your issue to either the MSDN Azure or CSDN forums. See [Windows Azure forums](http://www.windowsazure.cn/support/forums/) for more information.

## Step 5: File an Azure support incident

If you have done steps 1 through 4 in this article and submitted your issue to the Azure support forums, but still cannot create an SSH connection, one alternative to consider is whether you can re-create the virtual machine.

If you cannot re-create the virtual machine, it might be time for you to file an Azure support incident.

To file an incident, go to the [Azure Support site](/support/contact/), and then click **Get Support**.

For information about using Azure Support, see the [Windows Azure Support FAQ](/support/faq/).

<!-- keep by customization: end -->
## Additional resources

<!-- deleted by customization For virtual machines in classic deployment model, --> [How to reset a password or SSH for Linux-based virtual machines](/documentation/articles/virtual-machines-linux-use-vmaccess-reset-password-or-ssh)

[Troubleshoot Windows Remote Desktop connections to a Windows-based Azure virtual machine](/documentation/articles/virtual-machines-troubleshoot-remote-desktop-connections)

[Troubleshoot access to an application running on an Azure virtual machine](/documentation/articles/virtual-machines-troubleshoot-access-application)
