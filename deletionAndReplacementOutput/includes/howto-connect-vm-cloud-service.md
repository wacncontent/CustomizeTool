replacement:

deleted:

		Virtual machines created with the Service Management deployment model are always placed in a cloud service. The cloud service acts as a container and provides a unique public DNS name, a public IP address, and a set of endpoints to access the virtual machine over the Internet. The cloud service can be in a virtual network, but that's not a requirement.
		
		If a cloud service isn't in a virtual network, it's called a *standalone* cloud service. The virtual machines in a standalone cloud service can only communicate with other virtual machines by using the other virtual machines’ public DNS names, and that traffic travels over the Internet. If a cloud service is in a virtual network, the virtual machines in that cloud service can communicate with all other virtual machines in the virtual network without sending any traffic over the Internet.
		
		If you place your virtual machines in the same standalone cloud service, you can take still use load balancing and availability sets. For details, see [Load balancing virtual machines](/documentation/articles/load-balance-virtual-machines) and [Manage the availability of virtual machines](/documentation/articles/manage-availability-virtual-machines). However, you can't organize the virtual machines on subnets or connect a standalone cloud service to your on-premises network. Here's an example:
		
		![Virtual machines in a standalone cloud service](./media/howto-connect-vm-cloud-service/CloudServiceExample.png)
		
		If you place your virtual machines in a virtual network, you can decide how many cloud services you want to use for load balancing and availability sets. Additionally, you can organize the virtual machines on subnets in the same way as your on-premises network and connect the virtual network to your on-premises network. Here's an example:
		
		![Virtual machines in a virtual network](./media/howto-connect-vm-cloud-service/VirtualNetworkExample.png)
		
		Virtual networks are the recommended way to connect virtual machines in Azure. The best practice is to configure each tier of your application in a separate cloud service. However, you may need to combine some virtual machines from different application tiers into the same cloud service to remain within the maximum of 200 cloud services per subscription. To review this and other limits, see [Azure Subscription and Service Limits, Quotas, and Constraints](/documentation/articles/azure-subscription-service-limits).
		
		## Connect VMs in a virtual network
		
		To connect virtual machines in a virtual network:
		
		1.	Create the virtual network in the [Azure Management Portal](http://manage.windowsazure.cn). For more information, see [Virtual Network Configuration Tasks](/documentation/services/virtual-machines/).
		2.	Create the set of cloud services for your deployment to reflect your design for availability sets and load balancing. In the portal, click **New > Compute > Cloud Service > Custom Create** for each cloud service.
		3.	To create each new virtual machine, click **New > Compute > Virtual Machine > From Gallery**. Choose the correct cloud service and virtual network for the VM. If the cloud service is already joined to a virtual network, its name will already be selected for you.
		
		![Selecting a cloud service for a virtual machine](./media/howto-connect-vm-cloud-service/VMConfig1.png)
		
		## Connect VMs in a standalone cloud service
		
		To connect virtual machines in a standalone cloud service:
		
		1.	Create the cloud service in the [Azure Management Portal](http://manage.windowsazure.cn). Click **New > Compute > Cloud Service > Custom Create**. Or, you can create the cloud service for your deployment when you create your first virtual machine.
		2.	When you create the virtual machines, choose the name of cloud service created in the previous step.
		![Add a virtual machine to an existing cloud service](./media/howto-connect-vm-cloud-service/Connect-VM-to-CS.png)
		
		##Resources
		[Load balancing virtual machines](/documentation/articles/load-balance-virtual-machines)
		
		[Manage the availability of virtual machines](/documentation/articles/manage-availability-virtual-machines)
		
		[Virtual Network Configuration Tasks](/documentation/services/virtual-machines/)
		
		After you create a virtual machine, it's a good idea to add a data disk so your services and workloads have a location to store data. See one of the following:
		
		[How to Attach a Data Disk to a Linux Virtual Machine](/documentation/articles/virtual-machines-linux-how-to-attach-disk)
		
		[How to Attach a Data Disk to a Windows Virtual Machine](/documentation/articles/storage-windows-attach-disk)

replaced by:

		<properties authors="kathydav" editor="tysonn" manager="donaldg" /> 
		
		
		#How to Connect Virtual Machines in a Cloud Service
		
		
		
		When you create a virtual machine, a cloud service is automatically created to contain the machine. You can create multiple virtual machines under the same cloud service to enable the virtual machines to communicate with each other, to load-balance between virtual machines, and to maintain high availability of the machines. 
		
		For more information about load-balancing virtual machines, see [Load balancing virtual machines](../../articles/load-balance-virtual-machines/). For more information about managing the availability of your application, see [Manage the availability of virtual machines](../../articles/manage-availability-virtual-machines/). 
		
		
		First, you'll need to create a virtual machine with a new cloud service, and then you can connect additional virtual machines to the first virtual machine under the same cloud service. 
		
		
		
		1. Create a virtual machine using the steps in [How to create a custom virtual machine](../../articles/virtual-machines-create-custom/).
		
		
		2. After you create the first custom virtual machine, on the [Management Portal](http://manage.windowsazure.cn) command bar, click **New**.
		
		
			![Create a new virtual machine](./media/howto-connect-vm-cloud-service/Create.png)
		
		3. Click **Virtual Machine**, and then click **From Gallery**.
		
		
			![Create a custom virtual machine](./media/howto-connect-vm-cloud-service/CreateNew.png)
		
			The **Select the virtual machine operating system** dialog box appears. 
		
		
		4. From the **Choose an image** page, select an image, and then click the arrow to continue.
		
		
			The first **Virtual machine configuration** page appears.
		
		
		5. In **Virtual Machine Name**, type the name that you want to use for the virtual machine.
		
		6. In **Size**, select the size that you want to use for the virtual machine. The size that you select depends on the number of cores that are needed for your application.
		
		7. In **New User Name**, type a name for the administrative account that you want to use to manage the server.
		
		
		8. In **New Password**, type a strong password for the administrative account. In **Confirm Password**, retype the password.
		
		
		9. For a virtual machine running the Linux operating system, you can select to secure the machine with an SSH Key.
		
		
		10. In **Cloud Service**, select the cloud service that will contain the new virtual machine.
		
		11. In **Storage Account**, select a storage account to store the .vhd file, or leave the field set at the default to create the storage account automatically. Only one storage account is automatically created. All other virtual machines that you create with this setting are located in this storage account. You are limited to 20 storage accounts.
		
		
		12. To use an availability set, select the one was created when you created the first virtual machine.
		
		13. Review the default endpoint configuration, and modify if necessary. 
		
		14. Click the check mark to create the connected virtual machine.

reason: ()

