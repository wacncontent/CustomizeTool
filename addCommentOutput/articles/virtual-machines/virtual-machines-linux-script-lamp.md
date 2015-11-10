<properties
	pageTitle="Use the CustomScript Extension on a Linux VM | Windows Azure"
	description="Learn how to use the CustomScript extension to deploy applications on Linux Virtual Machines in Azure created using the classic deployment model."
	editor="tysonn"
	manager="timlt"
	documentationCenter=""
	services="virtual-machines"
	authors="gbowerman"
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="02/23/2015"
	wacn.date=""/>

#Deploy a LAMP app using the Azure CustomScript Extension for Linux#

<!-- deleted by customization
[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-classic-include.md)] Resource Manager model.


The Windows Azure CustomScript Extension for Linux provides a way to customize your virtual machines (VMs) by running arbitrary code written in any scripting language supported by the VM (for example, Python, and Bash). This provides a very flexible way to automate application deployment to multiple machines.

You can deploy the CustomScript Extension using the Azure Management Portal, Windows PowerShell, or the Azure Command-Line Interface (Azure CLI).

In this article we'll use the Azure CLI to deploy a simple LAMP application to an Ubuntu VM created using the classic deployment model.
-->
<!-- keep by customization: begin -->
The Azure CustomScript extension for Linux provides a way to customize your virtual machines (VMs) by running arbitrary code written in any scripting language supported by the VM (e.g. Python, Bash etc.). This provides a very flexible way to automate application deployment to multiple machines.

You can deploy the CustomScript extension using the Azure Management Portal, PowerShell, or the Azure Command-Line Interface (Azure CLI).

In this example we'll walk through deploying a simple LAMP application to Ubuntu using the Azure CLI.
<!-- keep by customization: end -->

## Prerequisites

<!-- deleted by customization
For this example, first create two Azure VMs running Ubuntu 14.04 or later. The VMs are called *script-vm* and *lamp-vm*. Use unique names when you create the VMs. One is used to run the CLI commands and one is used to deploy the LAMP app.

You also need an Azure Storage account and a key to access it (you can get this from the Azure Management Portal).
-->
<!-- keep by customization: begin -->
For this walk-through, create two Azure VMs running Ubuntu 14.04. I'll call them *script-vm* and *lamp-vm* here. Use unique names when you try this. One will be for running the CLI commands and one is to deploy the LAMP app to.

You also need an Azure Storage account and  key to access it (you can get this from the Azure Management Portal).
<!-- keep by customization: end -->

If you need help creating Linux VMs on Azure refer to [Create a Virtual Machine Running Linux](/documentation/articles/virtual-machines-linux-tutorial).

<!-- deleted by customization
The install commands assume Ubuntu, but you can adapt the installation for any supported Linux distro.

The script-vm VM needs to have Azure CLI installed, with a working connection to Azure. For help with this refer to [Install and Configure the Azure Command-Line Interface](/documentation/articles/xplat-cli-install).

## Upload a script

We'll use the CustomScript Extension to run a script on a remote VM to install the LAMP stack and create a PHP page. In order to access the script from anywhere we'll upload it as an Azure blob.

### Script overview

The script example installs a LAMP stack to Ubuntu (including setting up a silent install of MySQL), writes a simple PHP file, and starts Apache.
-->
<!-- keep by customization: begin -->
Though the specific install commands will assume Ubuntu, you can adapt the general steps for any supported distro.

The *script-vm* VM needs to have Azure CLI installed, with a working connection to Azure. For help with this refer to [Install and Configure the Azure Command-Line Interface](/documentation/articles/xplat-cli).

## Uploading a script

In this example the CustomScript extension will execute a script on a remote VM to install the LAMP stack and create a PHP page. In order to access the script from anywhere we'll upload it as an Azure blob.

**The script**

This script installs a LAMP stack to Ubuntu (including setting up a silent install of MySQL), writes a simple PHP file and starts Apache:
<!-- keep by customization: end -->

	#!/bin/bash
	# set up a silent install of MySQL
	dbpass="mySQLPassw0rd"

	export DEBIAN_FRONTEND=noninteractive
	echo mysql-server-5.6 mysql-server/root_password password $dbpass | debconf-set-selections
	echo mysql-server-5.6 mysql-server/root_password_again password $dbpass | debconf-set-selections

	# install the LAMP stack
	apt-get -y install apache2 mysql-server php5 php5-mysql  

	# write some PHP
	echo \<center\>\<h1\>My Demo App\</h1\>\<br/\>\</center\> > /var/www/html/phpinfo.php
	echo \<\?php phpinfo\(\)\; \?\> >> /var/www/html/phpinfo.php

	# restart Apache
	apachectl restart

<!-- deleted by customization
### Upload script

Save the script as a text file, for example *lamp_install.sh*, and then upload it to Azure Storage. You can do this easily with Azure CLI. The following example uploads the file to a storage container named "scripts".  If the container doesn't exist you'll need to create it first.
-->
<!-- keep by customization: begin -->
**Upload**

Save the script as a text file, for example *lamp_install.sh*, and then upload it to Azure storage. You can do this easily with Azure CLI. The following example uploads the file to a storage container named "scripts". Note: If the container doesn't exist you'll need to create it first.
<!-- keep by customization: end -->

    azure storage blob upload -a <yourStorageAccountName> -k <yourStorageKey> --container scripts ./install_lamp.sh

Also create a JSON file <!-- deleted by customization that --><!-- keep by customization: begin --> which <!-- keep by customization: end --> describes how to download the script from Azure <!-- deleted by customization Storage --><!-- keep by customization: begin --> storage <!-- keep by customization: end -->. Save this as *public_config.json* (replacing "mystorage" with the name of your storage account):

<!-- deleted by customization
    {"fileUris":["https://mystorage.blob.core.chinacloudapi.cn/scripts/install_lamp.sh"], "commandToExecute":"sh install_lamp.sh" }


## Deploy the extension

Now you can use the next command to deploy the Linux CustomScript Extension to the remote VM using the Azure CLI.
-->
<!-- keep by customization: begin -->
    {fileUris":["https://mystorage.blob.core.chinacloudapi.cn/scripts/install_lamp.sh"], "commandToExecute":"sh install_lamp.sh" }


## Deploying the extension

Now we're ready to deploy the Linux CustomScript extension to the remote VM using the Azure CLI:
<!-- keep by customization: end -->

    azure vm extension set -c "./public_config.json" lamp-vm CustomScriptForLinux Microsoft.OSTCExtensions 1.*

<!-- deleted by customization
The previous command downloads and runs the *lamp_install.sh* script on the VM called *lamp-vm*.

Since the app includes a web server <!-- deleted by customization, --> remember to open an HTTP listening port on the remote VM with the next command.<!-- keep by customization: begin -->: <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
This will download and execute the *lamp_install.sh* script on the VM called *lamp-vm*.

Since the app includes a web server <!-- deleted by customization, --> remember to open an HTTP listening port on the remote VM <!-- keep by customization: begin -->: <!-- keep by customization: end -->
<!-- keep by customization: end -->

    azure vm endpoint create -n Apache -o tcp lamp-vm 80 80

## Monitoring and troubleshooting

You can check on <!-- deleted by customization how well --><!-- keep by customization: begin --> the progress of <!-- keep by customization: end --> the custom script <!-- deleted by customization runs --><!-- keep by customization: begin --> execution <!-- keep by customization: end --> by looking at the log file on the remote VM. SSH to *lamp-vm* and tail the log file <!-- deleted by customization with the next command. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

    cd /var/log/azure/Microsoft.OSTCExtensions.CustomScriptForLinux/1.3.0.0/
    tail -f extension.log

<!-- deleted by customization
After you run the CustomScript Extension, you can browse to the PHP page you created for information. The PHP page for the example in this article is *http://lamp-vm.chinacloudapp.cn/phpinfo.php*.

## Additional resources
-->
<!-- keep by customization: begin -->
Once the CustomScript extension has finished executing you can browse to the PHP page you created, which in this example would be: *http://lamp-vm.chinacloudapp.cn/phpinfo.php*.

## Additional Resources
<!-- keep by customization: end -->

You can use the same basic steps to deploy more complex apps. In this example the install script was saved as a public blob in Azure Storage. A more secure option would be to store the install script as a secure blob with a [Secure Access Signature](https://msdn.microsoft.com/zh-cn/library/azure/ee395415.aspx) (SAS).

<!-- deleted by customization
Additional resources for Azure CLI, Linux and the CustomScript Extension are listed next.
-->
<!-- keep by customization: begin -->
Here are some additional resources for Azure CLI, Linux and the CustomScript extension:
<!-- keep by customization: end -->

[Automate Linux VM Customization Tasks Using CustomScript Extension](http://azure.microsoft.com/blog/2014/08/20/automate-linux-vm-customization-tasks-using-customscript-extension/)

[Azure Linux Extensions (GitHub)](https://github.com/Azure/azure-linux-extensions)

[Linux and Open-Source Computing on Azure](/documentation/articles/virtual-machines-linux-opensource)
