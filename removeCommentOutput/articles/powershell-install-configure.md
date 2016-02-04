<properties
	pageTitle="How to install and configure Azure PowerShell"
	description="Learn how to install and configure Azure PowerShell."
	editor="tysonn"
	manager="stevenka"
	documentationCenter=""
	services=""
	authors="coreyp-at-msft"/>

<tags
	ms.service="multiple"
	ms.date="12/02/2015"
	wacn.date=""/>

# How to install and configure Azure PowerShell#

<div class="dev-center-tutorial-selector sublanding"><a href="/documentation/articles/install-and-configure-windows-powershell/" title="PowerShell" class="current">PowerShell</a><a href="/documentation/articles/xplat-cli-install/" title="Azure CLI">Azure  CLI</a></div>

##What is Azure PowerShell?#
Azure PowerShell is a module that provides cmdlets to manage Azure with Windows PowerShell. You can use the cmdlets to create, test, deploy, and manage solutions and services delivered through the Azure platform. In most cases, the cmdlets can be used for the same tasks as the Azure Management Portal, such as creating and configuring cloud services, virtual machines, virtual networks, and web sites.

The module and the source code are available for download on a publicly available repository:

- [PowerShell 1.0.1](https://github.com/Azure/azure-powershell/releases/download/v1.0.1-November2015/azure-powershell.1.0.1.msi)
- [Azure PowerShell 1.0.1 source code](https://github.com/Azure/azure-powershell/archive/v1.0.1-November2015.zip)

<a id="Install"></a>
## Step 1: Install
Download and install [PowerShell 1.0.1](https://github.com/Azure/azure-powershell/releases/download/v1.0.1-November2015/azure-powershell.1.0.1.msi)
<a id="Connect"></a>

## Step 2: Start
The module installs a customized console for Azure PowerShell. You can run the cmdlets from the standard Windows PowerShell console, or from the Azure PowerShell console.

## Step 3: Connect
The cmdlets need your subscription so they can manage your services. You can purchase an Azure subscription if you don't already have one. For instructions, see [How to buy Azure](https://azure.microsoft.com/zh-cn/pricing/overview/).

1. Type **Add-AzureAccount**

2. Type the email address and password associated with your account. Azure authenticates and saves the credential information, and then closes the window.

--OR--

Sign into your work or school account:

        $cred = Get-Credential
        Add-AzureAccount -Credential $cred

> [AZURE.NOTE] This non-interactive login method only works with a work or school account. A work or school account is a user that is managed by your work or school, and defined in the Azure Active Directory instance for your work or school. If you do not currently have a work or school account, and are using a Microsoft account to log in to your Azure subscription, you can easily create one using the following steps.

> 1. Login to the [Azure Management Portal](https://manage.windowsazure.cn), and click on **Active Directory**.

> 2. If no directory exists, select **Create your directory** and provide the requested information.

> 3. Select your directory and add a new user. This new user can sign in using a work or school account. During the creation of the user, you will be supplied with both an e-mail address for the user and a temporary password. Save this information, as it is used in step 5 below.

> 4. From the management portal, select **Settings** and then select **Administrators**. Select **Add**, and add the new user as a co-administrator. This allows the work or school account to manage your Azure subscription.

> 5. Finally, log out of the Azure Management Portal and then log back in using the work or school account. If this is the first time logging in with this account, you will be prompted to change the password.

> For more information on signing up for Windows Azure with a work or school account, see [Sign up for Windows Azure as an Organization](/documentation/articles/sign-up-organization).

### View account and subscription details

You can have multiple accounts and subscriptions available for use by Azure PowerShell. You can add multiple accounts by running **Add-AzureAccount** more than once.

To display the available Azure accounts, type **Get-AzureAccount**.

To display your Azure subscriptions, type **Get-AzureSubscription**.

## Step 4: Test<a id="Ex"></a>


After you've installed the module and configured your computer to connect to your subscription, you can create an Azure web site to make sure everything is working.

1. Start the Azure PowerShell console.

2. Choose a name for your web site. Pick a name that conforms to DNS naming conventions. Valid names can contain only letters 'a' through 'z', numbers '0' through '9', and a hyphen ('-').

	The web site name must be unique in Azure. We'll use "mySite" in this example, but be sure to choose a different name, such as your account name followed by a number.  

	After you pick a name, type a command similar to the following. Substitute your web site name for "mySite".

		New-AzureWebsite mySite

	The cmdlet creates the web site and returns an object that represents the new web site. The object properties include useful information about the web site.

3. To get information about the web site, type this command. It returns a bit of information about all web sites in the subscription, including the one that you just created.

		Get-AzureWebsite

4. To get more information about your web site, include the web site name in the command. Be sure to substitute the name of your web site for "mySite".

		Get-AzureWebsite -Name mySite

5. web sites are started after they are created. To stop the web site, type this command, including the name of your web site.

		Stop-AzureWebsite -Name mySite

6. To verify that the site's state is 'stopped', run the Get-AzureWebsite command again.

		Get-AzureWebsite

7. To complete this test, delete the web site. Type:  

		Remove-AzureWebsite -Name mySite

7. To complete the task, confirm that the web site is deleted.

		Get-AzureWebsite -Name mySite

##<a id="Help"></a>Getting help##

These resources provide help for specific cmdlets:


-   From within the console, you can use the built-in Help system. The **Get-Help** cmdlet provides access to this system. 



- Reference information about the cmdlets in the Azure PowerShell modules is also available in the Azure library. For information, see [Azure Cmdlet Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn708514.aspx).

For help from the community, try these popular forums:

- [Azure forum on MSDN]( https://social.msdn.microsoft.com:443/forums/azure/zh-cn/home?category=windowsazureplatform%2Cazuremarketplace%2Cwindowsazureplatformctp)
- [Stackoverflow](http://stackoverflow.com/questions/tagged/azure)
