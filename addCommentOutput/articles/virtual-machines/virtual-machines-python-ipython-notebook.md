<properties
	pageTitle="Create an Jupyter/IPython Notebook | Windows Azure"
	description="Learn how to deploy the Jupyter/IPython Notebook on a Linux virtual machine created with the resource manager deployment model in Azure."
	services="virtual-machines"
	documentationCenter="python"
	authors="huguesv"
	manager="wpickett"
	editor=""
	tags=“azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="05/20/2015"
	wacn.date=""/>

<!-- deleted by customization
# Jupyter Notebook on Azure

The [Jupyter project](http://jupyter.org), formerly the [IPython project](http://ipython.org), provides a collection of tools for scientific computing using powerful interactive shells that combine code execution with the creation of a live computational document. These notebook files can contain arbitrary text, mathematical formulas, input code, results, graphics, videos and any other kind of media that a modern web browser is capable of displaying. Whether you're absolutely new to Python and want to learn it in a fun, interactive environment or do some serious parallel/technical computing, the Jupyter Notebook is a great choice.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-spectral.png)
Using SciPy and Matplotlib packages to analyze the structure of a sound recording.


## Jupyter Two Ways: Azure Notebooks or Custom Deployment
Azure provides a service that you can use to [quickly start using Jupyter
](http://blogs.technet.com/b/machinelearning/archive/2015/07/24/introducing-jupyter-notebooks-in-azure-ml-studio.aspx).  By using the Azure Notebook Service, you can easily gain access to Jupyter's web-accessible interface to
-->
<!-- keep by customization: begin -->

# IPython Notebook on Azure

The [IPython project](http://ipython.org) provides a collection of tools for scientific computing that include powerful interactive shells, high-performance and easy to use parallel libraries and a web-based environment called the IPython Notebook. The Notebook provides a working environment for interactive computing that combines code execution with the creation of a live computational document. These notebook files can contain arbitrary text, mathematical formulas, input code, results, graphics, videos and any other kind of media that a modern web browser is capable of displaying.

Whether you're absolutely new to Python and want to learn it in a fun, interactive environment or do some serious parallel/technical computing, the IPython Notebook is a great choice. As an illustration of its capabilities, the
following screenshot shows the IPython Notebook being used, in combination with the SciPy and Matplotlib packages, to analyze the structure of a sound recording.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-spectral.png)

This article will show you how to deploy the IPython Notebook on Microsoft
Azure, using Linux or Windows virtual machines (VMs).  By using the IPython
Notebook on Azure, you can easily provide a web-accessible interface to
<!-- keep by customization: end -->
scalable computational resources with all the power of Python and its many
<!-- deleted by customization
libraries.  Since the installation is handled by the service, users can access these
resources without the need for administration and configuration by the user.

If the notebook service does not work for your scenario please continue to read this article which will will show you how to deploy the Jupyter Notebook on Windows Azure, using Linux virtual machines (VMs).

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-rm-include.md)] classic deployment model.
-->
<!-- keep by customization: begin -->
libraries.  Since all installation is done in the cloud, users can access these
resources without the need for any local configuration beyond a modern web
browser.
<!-- keep by customization: end -->

[AZURE.INCLUDE [create-account-and-vms-note](../includes/create-account-and-vms-note.md)]

## Create and configure a VM on Azure

The first step is to create a virtual machine (VM)  running on Azure.
This VM is a complete operating system in the cloud and will be used to
run the <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> Notebook. Azure is capable of running both Linux and Windows
virtual machines, and we will cover the setup of <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> on both types of virtual machines.

<!-- deleted by customization
### Create a Linux VM and open a port for Jupyter

Follow the instructions given [here][portal-vm-linux] to create a virtual machine of the  *Ubuntu* distribution. This tutorial uses  Ubuntu Server 14.04 LTS. We'll assume the  user name *azureuser*.

After the virtual machine deploys we need to open up a security rule on the network security group.  From the portal, go to **Network Security Groups** and open the tab for the Security Group corresponding to your VM. You need to add an Inbound Security rule with the following settings:
**TCP** for the protocol, **\*** for the source (public) port and **9999** for the destination (private) port.

![Screenshot](./media/virtual-machines-python-ipython-notebook/azure-add-endpoint.png)

While in your Network Security Group, click on **Network Interfaces** and note the **Public IP Address** as it will be needed to connect to your VM in the next step.
-->
<!-- keep by customization: begin -->
### Linux VM

Follow the instructions given [here][portal-vm-linux] to create a virtual machine of the *OpenSUSE* or *Ubuntu* distribution. This tutorial uses OpenSUSE 13.2 and Ubuntu Server 14.04 LTS. We'll assume the default user name *azureuser*.

### Windows VM

Follow the instructions given [here][portal-vm-windows] to create a virtual machine of the *Windows Server 2012 R2 Datacenter* distribution. In this tutorial, we'll assume that the user name is *azureuser*.

## Create an endpoint for the IPython Notebook

This step applies to both the Linux and Windows VM. Later on we will configure
IPython to run its notebook server on port 9999. To make this port publicly
available, we must create an endpoint in the Azure Management Portal. This
endpoint opens up a port in the Azure firewall and maps the public port (HTTPS,
443) to the private port on the VM (9999).

To create an endpoint, go to the VM dashboard, click **Endpoints**, then click **Add
Endpoint** and create a new endpoint (called `ipython_nb` in this example). Pick
**TCP** for the protocol, **443** for the public port and **9999** for the private port.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-azure-linux-005.png)

After this step, the **Endpoints** Dashboard tab will look like the next screenshot.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-azure-linux-006.png)
<!-- keep by customization: end -->

## Install required software on the VM

<!-- deleted by customization
To run the Jupyter Notebook on our VM, we must first install Jupyter and
its dependencies. Connect to your linux vm using ssh and the username/password pair you chose when you created the vm. In this tutorial we will use PuTTY and connect from Windows.

### Installing Jupyter on Ubuntu
Install Anaconda, a popular data science python distribution, using one of the links provided from [Continuum Analytics](https://www.continuum.io/downloads).  As of the writing of this document, the below links are the most up to date versions.

#### Anaconda Installs for Linux
<table>
  <th>Python 3.4</th>
  <th>Python 2.7</th>
  <tr>
    <td>
		<a href='https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.3.0-Linux-x86_64.sh'>64 bit</href>
	</td>
    <td>
		<a href='https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Linux-x86_64.sh'>64 bit</href>
	</td>
  </tr>
  <tr>
    <td>
		<a href='https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.3.0-Linux-x86.sh'>32 bit</href>
	</td>
    <td>
		<a href='https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Linux-x86.sh'>32 bit</href>
	</td>  
  </tr>
</table>


#### Installing Anaconda3 2.3.0 64-bit on Ubuntu
As an example, this is how you can install Anaconda on Ubuntu

	# install anaconda
	cd ~
	mkdir -p anaconda
	cd anaconda/
	curl -O https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.3.0-Linux-x86_64.sh
	sudo bash Anaconda3-2.3.0-Linux-x86_64.sh -b -f -p /anaconda3

	# clean up home directory
	cd ..
	rm -rf anaconda/

	# Update Jupyter to the latest install and generate its config file
	sudo /anaconda3/bin/conda install -f jupyter -y
	/anaconda3/bin/jupyter-notebook --generate-config


![Screenshot](./media/virtual-machines-python-ipython-notebook/anaconda-install.png)


### Configuring Jupyter and using SSL
After installing we need to take a moment to setup the configuration files for Jupyter. If you experience troubles with configuring Jupyter it may be helpful to look at the [Jupyter Documentation for Running a Notebook Server](http://jupyter-notebook.readthedocs.org/en/latest/public_server.html).
-->
<!-- keep by customization: begin -->
To run the IPython Notebook on our VM, we must first install IPython and
its dependencies. 

### Linux (OpenSUSE)

To install IPython and its dependencies, SSH into the Linux VM, complete
the following steps.

Install [NumPy][NumPy], [Matplotlib][Matplotlib], [Tornado][Tornado] and other IPython's dependencies with the following commands.

    sudo zypper install python-matplotlib
    sudo zypper install python-tornado
    sudo zypper install python-jinja2
    sudo zypper install ipython

### Linux (Ubuntu)

To install IPython and its dependencies, SSH into the Linux VM and carry out
the following steps.

First, retrieve new lists of packages with the following command.

    sudo apt-get update

Install [NumPy][NumPy], [Matplotlib][Matplotlib], [Tornado][Tornado] and other IPython's dependencies with the following commands.

    sudo apt-get install python-matplotlib
    sudo apt-get install python-tornado
    sudo apt-get install ipython
    sudo apt-get install ipython-notebook

### Windows

To install IPython and its dependencies on the Windows VM, use Remote Desktop to connect to the VM. Then carry out the following steps,
using the Windows PowerShell to run all command-line actions.

**Note**: To download anything using Internet Explorer, you'll need to change some security settings.  From **Server Manager**, click **Local Server**, then on **IE Enhanced Security Configuration**, turn it off for administrators.  You can enable it again after you install IPython.

1.  Download and install the latest 32-bit version of [Python 2.7][].  You will need to add `C:\Python27` and `C:\Python27\Scripts` to your `PATH` environment variable.

1.  Install [Tornado][Tornado] and [PyZMQ][PyZMQ] and other IPython's dependencies with the following commands.

        easy_install tornado
        easy_install pyzmq
        easy_install jinja2
        easy_install six
        easy_install python-dateutil
        easy_install pyparsing

1.  Download and install [NumPy][NumPy] using the `.exe` binary installer available on their website.  As of this writing, the latest version is numpy-1.9.1-win32-superpack-python2.7.exe.

1.  Install [Matplotlib][Matplotlib] with the following command.

        pip install matplotlib==1.4.2

1.  Download and install [OpenSSL][].

	* You'll find the required Visual C++ 2008 Redistributable on the same download page.

	* You will  need to add `C:\OpenSSL-Win32\bin` to your `PATH` environment variable.

	> [AZURE.NOTE] When installing OpenSSL, use version 1.0.1g or later as these include a fix for the Heartbleed security vulnerability.

1.  Install IPython using the following command.

        pip install ipython==2.4

1.  Open a port in Windows Firewall.  On Windows Server 2012, the firewall will block incoming connections by default.  To open port 9999, follow these steps:

    - Start **Windows Firewall with Advanced Security** from the Start screen.

    - Click **Inbound Rules** in the left panel.

	- Click **New Rule** in the Actions panel.

	- In the New Inbound Rule Wizard, select **Port**.

	- In the next screen, select **TCP** and enter **9999** in **Specific local ports**.

	- Accept defaults, give the rule a name and then click **Finish**.

### Configure the IPython Notebook

Next, we configure the IPython Notebook. The first step is to create a custom
IPython configuration profile to encapsulate the configuration information with the following command.

    ipython profile create nbserver
<!-- keep by customization: end -->

Next we `cd` to the profile directory to create our SSL certificate and edit
the profiles configuration file.

On Linux use the following command.

<!-- deleted by customization
    cd ~/.jupyter
-->
<!-- keep by customization: begin -->
    cd ~/.ipython/profile_nbserver/

On Windows use the following command.

    cd \users\azureuser\.ipython\profile_nbserver
<!-- keep by customization: end -->

Use the following command to create the SSL certificate(Linux and Windows).

    openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem

Note that since we are creating a self-signed SSL certificate, when connecting
to the notebook your browser will give you a security warning.  For long-term
production use, you will want to use a properly signed certificate associated
with your organization.  Since certificate management is beyond the scope of
this demo, we will stick to a self-signed certificate for now.

In addition to using a certificate, you must also provide a password to protect
your notebook from unauthorized use.  For security reasons <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> uses
encrypted passwords in its configuration file, so you'll need to encrypt your
password first.  IPython provides a utility to do so; at a command prompt run the following command.

<!-- deleted by customization
    /anaconda3/bin/python -c "import IPython;print(IPython.lib.passwd())"

This will prompt you for a password and confirmation, and will then print the password. Note this for the following step.
-->
<!-- keep by customization: begin -->
    python -c "import IPython;print IPython.lib.passwd()"

This will prompt you for a password and confirmation, and will then print the 
password as follows.
<!-- keep by customization: end -->

    Enter password:
    Verify password:
    sha1:b86e933199ad:a02e9592e59723da722.. (elided the rest for security)

Next, we will edit the profile's configuration file, which is the
<!-- deleted by customization `jupyter_notebook_config.py` --><!-- keep by customization: begin --> `ipython_notebook_config.py` <!-- keep by customization: end --> file in the <!-- keep by customization: begin --> profile <!-- keep by customization: end --> directory you are in.  Note that this file may not exist -- just create it <!-- deleted by customization if that is the case -->.  This
file has a number of fields and by default all are commented out.  You can open
this file with any text editor of your liking, and you should ensure that it
has at least the following content. <!-- deleted by customization Be sure to replace the password with the sha1 from the previous step. -->

    c = get_config()

<!-- keep by customization: begin -->
    # This starts plotting support always with matplotlib
    c.IPKernelApp.pylab = 'inline'

<!-- keep by customization: end -->
    # You must give the path to the certificate file.
<!-- deleted by customization
    c.NotebookApp.certfile = u'/home/azureuser/.jupyter/mycert.pem'
-->
<!-- keep by customization: begin -->

    # If using a Linux VM:
    c.NotebookApp.certfile = u'/home/azureuser/.ipython/profile_nbserver/mycert.pem'

    # And if using a Windows VM:
    c.NotebookApp.certfile = r'C:\Users\azureuser\.ipython\profile_nbserver\mycert.pem'
<!-- keep by customization: end -->

    # Create your own password as indicated above
    c.NotebookApp.password = u'sha1:b86e933199ad:a02e9592e5 etc... '

    # Network and browser details. We use a fixed port (9999) so it matches
    # our Azure setup, where we've allowed <!-- deleted by customization :wqtraffic --><!-- keep by customization: begin --> traffic <!-- keep by customization: end --> on that port
    c.NotebookApp.ip = '*'
    c.NotebookApp.port = 9999
    c.NotebookApp.open_browser = False

<!-- deleted by customization
### Run the Jupyter Notebook

At this point we are ready to start the Jupyter Notebook. To do this,
-->
<!-- keep by customization: begin -->
### Run the IPython Notebook

At this point we are ready to start the IPython Notebook. To do this,
<!-- keep by customization: end -->
navigate to the directory you want to store notebooks in and start
the <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> Notebook server with the following command.

<!-- deleted by customization
    /anaconda3/bin/jupyter-notebook

You should now be able to access your Jupyter Notebook at the address
`https://[PUBLIC-IP-ADDRESS]:9999`.

When you first access your notebook, the login page asks for your password. And
once you log in, you will see the "Jupyter Notebook Dashboard", which is the
ontrol center for all notebook operations.  From this page you can create
-->
<!-- keep by customization: begin -->
    ipython notebook --profile=nbserver

You should now be able to access your IPython Notebook at the address
`https://[Your Chosen Name Here].chinacloudapp.cn`.

When you first access your notebook, the login page asks for your password. 

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-001.png)

And once you log in, you will see the "IPython Notebook Dashboard", which is
the control center for all notebook operations.  From this page you can create
<!-- keep by customization: end -->
new notebooks and open existing ones.

<!-- deleted by customization
![Screenshot](./media/virtual-machines-python-ipython-notebook/jupyter-tree-view.png)

### Using the Jupyter Notebook

If you click the **New** button, you will see the following opening page.

![Screenshot](./media/virtual-machines-python-ipython-notebook/jupyter-untitled-notebook.png)
-->
<!-- keep by customization: begin -->
![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-002.png)

If you click the **New Notebook** button, you will see the following opening page.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-003.png)
<!-- keep by customization: end -->

The area marked with an `In []:` prompt is the input area, and here you can
type any valid Python code and it will execute when you hit `Shift-Enter` or
click on the "Play" icon (the right-pointing triangle in the toolbar).
<!-- keep by customization: begin -->

Since we have configured the notebook to start with NumPy and Matplotlib support
automatically, you can even produce figures as shown in the next screenshot.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-004.png)
<!-- keep by customization: end -->

## A powerful paradigm: live computational documents with rich media

The notebook itself should feel very natural to anyone who has used Python and
a word processor, because it is in some ways a mix of both: you can execute
blocks of Python code, but you can also keep notes and other text by changing
the style of a cell from "Code" to "Markdown" using the drop-down menu in the
toolbar.

<!-- deleted by customization
Jupyter is much more than a word processor as it allows the
-->
<!-- keep by customization: begin -->
![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-005.png)


But this is much more than a word processor, as the IPython notebook allows the
<!-- keep by customization: end -->
mixing of computation and rich media (text, graphics, video and virtually
<!-- deleted by customization
anything a modern web browser can display). You can mix, text, code, videos and more!

![Screenshot](./media/virtual-machines-python-ipython-notebook/jupyter-editing-experience.png)
-->
<!-- keep by customization: begin -->
anything a modern web browser can display). For example, you can mix
explanatory videos with computation for educational purposes.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-006.png)

or, as shown in the next screenshot, embed external websites that remain live and usable, inside of a notebook
file.

![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-007.png)
<!-- keep by customization: end -->

And with the power of Python's many excellent libraries for scientific and
technical computing, in the following screenshot, a simple calculation can be performed with the same ease
as a complex network analysis, all in one environment.

<!-- keep by customization: begin -->
![Screenshot](./media/virtual-machines-python-ipython-notebook/ipy-notebook-008.png)

<!-- keep by customization: end -->
This paradigm of mixing the power of the modern web with live computation
offers many possibilities, and is ideally suited for the cloud; the Notebook
can be used:

* As a computational scratchpad to record exploratory work on a problem.

* To share results with colleagues, either in 'live' computational form or in
  hardcopy formats (HTML, PDF).

* To distribute and present live teaching materials that involve computation,
  so students can immediately experiment with the real code, modify it and
  re-execute it interactively.

* To provide "executable papers" that present the results of research in a way
  that can be immediately reproduced, validated and extended by others.

* As a platform for collaborative computing: multiple users can log in to the
  same notebook server to share a live computational session.


If you go to the IPython source code [repository][], you will find an entire
directory with notebook examples which you can download and then experiment with on your own Azure <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> VM.  Simply download the `.ipynb` files from the site and upload them onto the dashboard of your notebook Azure VM (or download them directly into the VM).

## Conclusion

The <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> Notebook provides a powerful interface for accessing interactively
the power of the Python ecosystem on Azure.  It covers a wide range of
usage cases including simple exploration and learning Python, data analysis and
visualization, simulation and parallel computing. The resulting Notebook
documents contain a complete record of the computations that are performed and
<!-- deleted by customization
can be shared with other Jupyter users.  The Jupyter Notebook can be used as a
-->
<!-- keep by customization: begin -->
can be shared with other IPython users.  The IPython Notebook can be used as a
<!-- keep by customization: end -->
local application, but it is ideally suited for cloud deployments on Azure

The core features of <!-- deleted by customization Jupyter --><!-- keep by customization: begin --> IPython <!-- keep by customization: end --> are also available inside Visual Studio via the
[Python Tools for Visual Studio][](/documentation/articles/PTVS). PTVS is a free and open-source plug-in
from Microsoft that turns Visual Studio into an advanced Python development
environment that includes an advanced editor with IntelliSense, debugging,
profiling and parallel computing integration.

<!-- deleted by customization
## Next steps

For more information, see the [Python Developer Center](/develop/python/).

[portal-vm-linux]: /documentation/articles/virtual-machines-linux-tutorial-portal-rm/
-->
<!-- keep by customization: begin -->



[Tornado]:      http://www.tornadoweb.org/          "Tornado"
[PyZMQ]:        https://github.com/zeromq/pyzmq     "PyZMQ"
[NumPy]:        http://www.numpy.org/               "NumPy"
[Matplotlib]:   http://matplotlib.sourceforge.net/  "Matplotlib"

[portal-vm-windows]: /documentation/articles/virtual-machines-windows-tutorial
[portal-vm-linux]: /documentation/articles/virtual-machines-linux-tutorial
<!-- keep by customization: end -->
[repository]: https://github.com/ipython/ipython
<!-- deleted by customization
[Python Tools for Visual Studio]: http://aka.ms/ptvs
-->
<!-- keep by customization: begin -->
[python Tools for visual studio]: http://aka.ms/ptvs
[Python 2.7]: http://www.python.org/download
[OpenSSL]: http://slproweb.com/products/Win32OpenSSL.html
<!-- keep by customization: end -->
