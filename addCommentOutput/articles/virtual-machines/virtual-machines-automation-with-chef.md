<properties
   pageTitle="Azure virtual machine deployment with Chef | Windows Azure"
   description="Learn how to use Chef to do automated virtual machine deployment and configuration on Windows Azure"
   services="virtual-machines"
   documentationCenter=""
   authors="diegoviso"
   manager="timlt"
   tags="azure-service-management,azure-resource-manager"
   editor=""/>

<tags ms.service="virtual-machines" ms.workload="infrastructure-services"
ms.tgt_pltfrm="vm-multiple"
ms.devlang="na"
ms.topic="article"
ms.date="05/19/2015"
ms.author="diviso"/>

<!-- deleted by customization
# Automating Azure virtual machine deployment with Chef
-->
<!-- keep by customization: begin -->
# Automating Azure Virtual Machine Deployment with Chef
<!-- keep by customization: end -->

Chef is a great tool for delivering automation and desired state configurations.

With our latest cloud-api release, Chef provides seamless integration with Azure, giving you the ability to provision and deploy configuration states through a single command.

In this article, I’ll show you how to <!-- deleted by customization set up --><!-- keep by customization: begin --> setup <!-- keep by customization: end --> your Chef environment to provision Azure <!-- deleted by customization virtual machines --><!-- keep by customization: begin --> Virtual Machines <!-- keep by customization: end --> and walk you through creating a policy or “CookBook” and then deploying this cookbook to an Azure <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end -->.

Let’s begin!

<!-- deleted by customization
## Chef basics

Before you begin, I suggest you review the basic concepts of Chef. There is great material <a href="http://www.chef.io/chef" target="_blank">here</a> and I recommend you have a quick read before you attempt this walkthrough. I will however recap the basics before we get started.

The following diagram depicts the high-level Chef architecture.

![][2]

Chef has three main architectural components: Chef Server, Chef Client (node), and Chef Workstation.

The Chef Server is our management point and there are two options for the Chef Server: a hosted solution or an on-premises solution. We will be using a hosted solution.

The Chef Client (node) is the agent that sits on the servers you are managing.

The Chef Workstation is our admin workstation where we create our policies and execute our management commands. We run the **knife** command from the Chef Workstation to manage our infrastructure.
-->
<!-- keep by customization: begin -->
## Chef Basics

Before you begin, I suggest you familiar yourself with the basic concepts of Chef. There is great material <a href="http://www.chef.io/chef" target="_blank">here</a> and I recommend you have a quick read before you attempt this walk through. I will however recap the basics before we get started.

The below diagram depicts the high level Chef architecture.

![][2]

Chef has three main architectural components. The **Chef Server, Chef Client (Node)** and the **Chef Workstation.**

The **Chef Server** is our management point and there are two options for the Chef Server: a hosted solution or an on-premises solution. We will be using a hosted solution.

The **Chef Client (node)** is the agent that sits on the servers you are managing.

The **Chef Workstation** is our admin workstation where we create our policies and execute our management commands. We run the **“knife”** command from the Chef Workstation to manage our infrastructure.
<!-- keep by customization: end -->

There is also the concept of “Cookbooks” and “Recipes”. These are effectively the policies we define and apply to our servers.

## Preparing the workstation

First, lets prep the workstation. I’m using a standard Windows workstation. We need to create a directory to store our config files and cookbooks.

<!-- deleted by customization
First create a directory called C:\chef.

Then create a second directory called c:\chef\cookbooks.
-->
<!-- keep by customization: begin -->
First create a directory called **C:\chef**. 

Then create a second directory **c:\chef\cookbooks**
<!-- keep by customization: end -->

We now need to download our Azure settings file so Chef can communicate with our Azure subscription.

<!-- deleted by customization
Download your publish settings from [here](https://manage.windowsazure.cn/publishsettings/).

Save the publish settings file in C:\chef.
-->
<!-- keep by customization: begin -->
Download your publish settings from here: <a href="https://manage.windowsazure.cn/publishsettings/" target="_blank">https://manage.windowsazure.cn/publishsettings/</a>

Save the publish settings file in **C:\chef**
<!-- keep by customization: end -->

##Creating a managed Chef account

<!-- deleted by customization
Sign up for a hosted Chef account [here](https://manage.chef.io/signup).
-->
<!-- keep by customization: begin -->
Sign up for a hosted Chef account: <a href="https://manage.chef.io/signup" target="_blank">https://manage.chef.io/signup</a>
<!-- keep by customization: end -->

During the signup process, you will be asked to create a new organization.

![][3]

Once your organization is created, download the starter kit.

![][4]

<!-- deleted by customization > [AZURE.NOTE] --><!-- keep by customization: begin --> **Note:** <!-- keep by customization: end --> If you receive a prompt warning you that your keys will be reset, it’s ok to proceed as we have no existing infrastructure configured as yet.

This starter kit zip file contains your organization config files and keys.

##Configuring the Chef workstation

<!-- deleted by customization
Extract the content of the chef-starter.zip to C:\chef.

Copy all files under chef-starter\chef-repo\.chef to your c:\chef directory.

Your directory should now look something like the following example.

![][5]

You should now have four files including the Azure publishing file in the root of c:\chef.

The PEM files contain your organization and admin private keys for communication while the knife.rb file contains your knife configuration. We will need to edit the knife.rb file.

Open the file in your editor of choice and modify the “cookbook_path” by removing the /../ from the path so it appears as shown next.
-->
<!-- keep by customization: begin -->
Extract the content of the chef-starter.zip to **C:\chef**

Copy all files under **chef-starter\chef-repo\.chef** to your **c:\chef**

Your directory should now look something like this:

![][5]

You should now have 4 files including the Azure publishing file in the root of c:\chef

The PEM files contain your organization and admin private keys for communication while the **knife.rb** file contains your knife configuration. We will need to edit the **knife.rb** file.

Open the file in your editor of choice and modify the “cookbook_path” by removing the /../ from the path so it appears as below:
<!-- keep by customization: end -->

	cookbook_path  ["#{current_dir}/cookbooks"]

Also add the following line reflecting the name of your Azure publish settings file.

	knife[:azure_publish_settings_file] = "yourfilename.publishsettings"

<!-- deleted by customization
Your knife.rb file should now look similar to the following example.

![][6]

These lines will ensure that Knife references the cookbooks directory under c:\chef\cookbooks, and also uses our Azure Publish Settings file during Azure operations.
-->
<!-- keep by customization: begin -->
Your knife.rb file should now look similar to this:

![][6]

These lines will ensure Knife references in our cookbooks directory under c:\chef\cookbooks and also uses our Azure Publish Settings file during Azure operations.
<!-- keep by customization: end -->

## Installing the Chef Development Kit

<!-- deleted by customization
Next [download and install](http://downloads.getchef.com/chef-dk/windows) the ChefDK (Chef Development Kit) to set up your Chef Workstation.

![][7]

Install in the default location of c:\opscode. This install will take around 10 minutes.
-->
<!-- keep by customization: begin -->
Next Download and install the ChefDK (Chef Development Kit) to setup your Chef Workstation.

<a href="http://downloads.getchef.com/chef-dk/windows" target="_blank">http://downloads.getchef.com/chef-dk/windows</a>

![][7]

This is straight forward. Let it install in its default location of c:\opscode. This install will take around 10 minutes.
<!-- keep by customization: end -->

Confirm your PATH variable contains entries for C:\opscode\chefdk\bin;C:\opscode\chefdk\embedded\bin;c:\users\yourusername\.chefdk\gem\ruby\2.0.0\bin

If they are not there, make sure you add these paths!

<!-- deleted by customization *NOTE --><!-- keep by customization: begin --> **NOTE <!-- keep by customization: end --> THE ORDER OF THE PATH IS <!-- deleted by customization IMPORTANT!* --><!-- keep by customization: begin --> IMPORTANT!** <!-- keep by customization: end --> If your opscode paths are not in the correct order you will have issues.

Reboot your workstation before you continue.

Next, we will install the Knife Azure extension. This provides Knife with the “Azure Plugin”.

<!-- deleted by customization
Run the following command.
-->
<!-- keep by customization: begin -->
Run the following command:
<!-- keep by customization: end -->

	chef gem install knife-azure ––pre

<!-- deleted by customization
> [AZURE.NOTE] The –pre argument ensures you are receiving the latest RC version of the Knife Azure Plugin which provides access to the latest set of APIs.
-->
<!-- keep by customization: begin -->
**Note:** The –pre argument ensures you are receiving the latest RC version of the knife azure plugin which provides access to the latest set of API’s.
<!-- keep by customization: end -->

It’s likely that a number of dependencies will also be installed at the same time.

![][8]


<!-- deleted by customization
To ensure everything is configured correctly, run the following command.
-->
<!-- keep by customization: begin -->
To ensure everything is configured correctly, run:
<!-- keep by customization: end -->

	knife azure image list

If everything is configured correctly, you will see a list of available Azure images scroll through.

<!-- deleted by customization
Congratulations. The workstation is set up!
-->
<!-- keep by customization: begin -->
Congratulations. The workstation has been setup!
<!-- keep by customization: end -->

##Creating a Cookbook

A Cookbook is used by Chef to define a set of commands that you wish to execute on your managed client. Creating a Cookbook is <!-- deleted by customization straightforward --><!-- keep by customization: begin --> straight forward <!-- keep by customization: end --> and we use the <!-- deleted by customization **chef --><!-- keep by customization: begin --> command chef <!-- keep by customization: end --> generate <!-- deleted by customization cookbook** command --><!-- keep by customization: begin --> cookbook <!-- keep by customization: end --> to generate our Cookbook template. I will be calling my Cookbook <!-- deleted by customization web server --><!-- keep by customization: begin --> webserver <!-- keep by customization: end --> as I would like a policy that automatically deploys IIS.

Under your C:\Chef directory run the following command <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

	chef generate cookbook webserver

This will generate a set of files under the directory <!-- deleted by customization C:\Chef\cookbooks\webserver. --><!-- keep by customization: begin --> **C:\Chef\cookbooks\webserver.** <!-- keep by customization: end --> We now need to define the set of commands we would like our Chef <!-- deleted by customization client --><!-- keep by customization: begin --> Client <!-- keep by customization: end --> to execute on our managed <!-- deleted by customization virtual machine --><!-- keep by customization: begin --> VM <!-- keep by customization: end -->.

The commands are stored in the file <!-- deleted by customization default.rb. --><!-- keep by customization: begin --> **default.rb.** <!-- keep by customization: end --> In this file, I’ll be defining a set of commands that installs IIS, starts IIS and copies a template file to the wwwroot folder.

<!-- deleted by customization
Modify the C:\chef\cookbooks\webserver\recipes\default.rb file and add the following lines.
-->
<!-- keep by customization: begin -->
Modify the **C:\chef\cookbooks\webserver\recipes\default.rb** and add the following lines:
<!-- keep by customization: end -->

	powershell_script 'Install IIS' do
 		action :run
 		code 'add-windowsfeature Web-Server'
	end

	service 'w3svc' do
 		action [ :enable, :start ]
	end

	template 'c:\inetpub\wwwroot\Default.htm' do
 		source 'Default.htm.erb'
 		rights :read, 'Everyone'
	end

Save the file once you are done.

## Creating a template

As we mentioned previously, we need to generate a template file which will be used as our default.html page.

<!-- deleted by customization
Run the following command to generate the template.
-->
<!-- keep by customization: begin -->
Execute the following command to generate the template:
<!-- keep by customization: end -->

	chef generate template webserver Default.htm

<!-- deleted by customization
Now navigate to the C:\chef\cookbooks\webserver\templates\default\Default.htm.erb file. Edit the file by adding some simple “Hello World” HTML code, and then save the file.

-->
<!-- keep by customization: begin -->
Now navigate to the file **C:\chef\cookbooks\webserver\templates\default\Default.htm.erb** and edit the file.

Add some simple “Hello World” html code and save the file.
<!-- keep by customization: end -->

## Upload the Cookbook to the Chef Server

In this step, we are taking a copy of the Cookbook that we have created on our local machine and uploading it to the Chef Hosted Server. Once uploaded, the Cookbook will appear under the <!-- deleted by customization **Policy** --><!-- keep by customization: begin --> policy <!-- keep by customization: end --> tab.

	knife cookbook upload webserver

![][9]

<!-- deleted by customization
## Deploy a virtual machine with Knife Azure

We will now deploy an Azure virtual machine and apply the “Webserver” Cookbook which will install our IIS web service and default web page.
-->
<!-- keep by customization: begin -->
## Deploying a Virtual Machine with Knife Azure

We will now deploy an Azure Virtual Machine and apply the “Webserver” Cookbook which will install our IIS Web Service and default web page.
<!-- keep by customization: end -->

In order to do this, use the **knife azure server create** command.

<!-- deleted by customization
Am example of the command appears next.

	knife azure server create --azure-dns-name 'diegotest01' --azure-vm-name 'testserver01' --azure-vm-size 'Small' --azure-storage-account 'portalvhdsxxxx' --bootstrap-protocol 'cloud-api' --azure-source-image 'a699494373c04fc0bc8f2bb1389d6106__Windows-Server-2012-Datacenter-201411.01-en.us-127GB.vhd' --azure-service-location 'Southeast Asia' --winrm-user azureuser --winrm-password 'myPassword123' --tcp-endpoints 80,3389 --r 'recipe[webserver]'
-->
<!-- keep by customization: begin -->
Here is an example of the command:

	knife azure server create --azure-dns-name 'diegotest01' --azure-vm-name 'testserver01' --azure-vm-size 'Small' --azure-storage-account 'portalvhdsxxxx' --bootstrap-protocol 'cloud-api' --azure-source-image 'a699494373c04fc0bc8f2bb1389d6106__Windows-Server-2012-Datacenter-201411.01-en.us-127GB.vhd' --azure-service-location 'China North' --winrm-user azureuser --winrm-password 'myPassword123' --tcp-endpoints 80,3389 --r 'recipe[webserver]'
<!-- keep by customization: end -->

The parameters are self-explanatory. Substitute your particular variables and run.

<!-- deleted by customization > [AZURE.NOTE] --><!-- keep by customization: begin --> **Note:** <!-- keep by customization: end --> Through the the command line <!-- deleted by customization, --> I’m also automating my endpoint network filter rules by using the –tcp-endpoints parameter. I’ve opened up ports 80 and 3389 to provide access to my web page and RDP session.

Once you run the command, <!-- deleted by customization go --><!-- keep by customization: begin --> pop over <!-- keep by customization: end --> to the Azure Management Portal and you will see your machine begin to provision.

![][13]

<!-- deleted by customization
The command prompt appears next.

![][10]

Once the deployment is complete, we should be able to connect to the web service over port 80 as we had opened the port when we provisioned the virtual machine with the Knife Azure command. As this virtual machine is the only virtual machine in my cloud service, I’ll connect it with the cloud service url.

![][11]

As you can see, I got creative with my HTML code.
-->
<!-- keep by customization: begin -->
Back at the command prompt:

![][10]

Once the deployment is complete, we should be able to connect to the web service over port 80 as we had opened the port when we provisioned the VM with the knife azure command. As this VM is the only VM in my cloud service, I’ll connect it with the cloud service url.

![][11]

As you can see, I got creative with my html code :)
<!-- keep by customization: end -->

Don’t forget we can also connect through an RDP session from the Azure Management Portal via port 3389.

<!-- deleted by customization
I hope this has been helpful! Go  and start your infrastructure as code journey with Azure today!
-->
<!-- keep by customization: begin -->
I hope this has been helpful! Go  and start your Infrastructure as Code journey with Azure today!

<!-- keep by customization: end -->


<!--Image references-->
[2]: ./media/virtual-machines-automation-with-chef/2.png
[3]: ./media/virtual-machines-automation-with-chef/3.png
[4]: ./media/virtual-machines-automation-with-chef/4.png
[5]: ./media/virtual-machines-automation-with-chef/5.png
[6]: ./media/virtual-machines-automation-with-chef/6.png
[7]: ./media/virtual-machines-automation-with-chef/7.png
[8]: ./media/virtual-machines-automation-with-chef/8.png
[9]: ./media/virtual-machines-automation-with-chef/9.png
[10]: ./media/virtual-machines-automation-with-chef/10.png
[11]: ./media/virtual-machines-automation-with-chef/11.png
[13]: ./media/virtual-machines-automation-with-chef/13.png


<!--Link references-->
