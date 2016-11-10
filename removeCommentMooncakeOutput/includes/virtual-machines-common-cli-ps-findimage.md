

## Azure CLI

> [AZURE.NOTE] This article describes how to navigate and select virtual machine images, using a recent installation of either the Azure CLI or Azure PowerShell. As a prerequisite, you would need to change to the Resource Manager mode. With the Azure CLI, enter that mode by typing `azure config mode arm`. 

The easiest and quickest way to locate an image to use either with `azure vm quick-create` or to create a resource group template file is to call the `azure vm image list` command and pass the location, the publisher name (it's not case-sensitive!), and an offer -- if you know the offer. For example, the following list is only a short example -- many lists are quite long -- if you know that "Canonical" is a publisher for the "UbuntuServer" offer.

    azure vm image list chinanorth canonical ubuntuserver
	info:    Executing command vm image list
	+ Getting virtual machine image skus (Publisher:"canonical" Offer:"ubuntuserver" Location:"chinanorth")
	data:    Publisher  Offer         Sku          OS     Version          Location    Urn
	data:    ---------  ------------  -----------  -----  ---------------  ----------  --------------------------------------------------
	data:    canonical  ubuntuserver  12.04.5-LTS  Linux  12.04.201601140  chinanorth  canonical:ubuntuserver:12.04.5-LTS:12.04.201601140
	data:    canonical  ubuntuserver  12.04.5-LTS  Linux  12.04.201602010  chinanorth  canonical:ubuntuserver:12.04.5-LTS:12.04.201602010
	data:    canonical  ubuntuserver  14.04.2-LTS  Linux  14.04.201507060  chinanorth  canonical:ubuntuserver:14.04.2-LTS:14.04.201507060
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201510190  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201510190
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201601190  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201601190
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201602010  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201602010
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201602171  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201602171
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201602220  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201602220
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201603140  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201603140
	data:    canonical  ubuntuserver  14.04.3-LTS  Linux  14.04.201604060  chinanorth  canonical:ubuntuserver:14.04.3-LTS:14.04.201604060
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201601230  chinanorth  canonical:ubuntuserver:15.10:15.10.201601230
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201602040  chinanorth  canonical:ubuntuserver:15.10:15.10.201602040
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201602171  chinanorth  canonical:ubuntuserver:15.10:15.10.201602171
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201602220  chinanorth  canonical:ubuntuserver:15.10:15.10.201602220
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201602260  chinanorth  canonical:ubuntuserver:15.10:15.10.201602260
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201603150  chinanorth  canonical:ubuntuserver:15.10:15.10.201603150
	data:    canonical  ubuntuserver  15.10        Linux  15.10.201604050  chinanorth  canonical:ubuntuserver:15.10:15.10.201604050

The **Urn** column will be the form you pass to `azure vm quick-create`.

Often, however, you don't yet know what is available. In this case, you can navigate images by discovering publishers first by using `azure vm image list-publishers` and responding to the location prompt with a data center location you expect to use for your resource group. For example, the following lists all image publishers in the China North location (pass the location argument by lowercasing and removing spaces from the standard locations)

    azure vm image list-publishers
    info:    Executing command vm image list-publishers
    Location: chinanorth
	+ Getting virtual machine and/or extension image publishers (Location: "chinanorth")
	data:    Publisher                                        Location
	data:    -----------------------------------------------  ----------
	data:    Canonical                                        chinanorth
	data:    Microsoft.Azure.Diagnostics                      chinanorth
	data:    Microsoft.Azure.Extensions                       chinanorth
	data:    Microsoft.Azure.RecoveryServices                 chinanorth
	data:    Microsoft.Azure.Security                         chinanorth
	data:    Microsoft.AzureCAT.AzureEnhancedMonitoring       chinanorth
	data:    Microsoft.AzureCAT.Test.AzureEnhancedMonitoring  chinanorth
	data:    Microsoft.Compute                                chinanorth
	data:    Microsoft.HpcPack                                chinanorth
	data:    Microsoft.OSTCExtensions                         chinanorth
	data:    Microsoft.OSTCExtensions1                        chinanorth
	data:    Microsoft.Powershell                             chinanorth
	data:    Microsoft.SqlServer.Management                   chinanorth
	data:    Microsoft.VisualStudio.Azure.RemoteDebug         chinanorth
	data:    MicrosoftWindowsServerHPCPack                    chinanorth
	data:    MSOpenTech.Extensions                            chinanorth
	data:    OpenLogic                                        chinanorth
	data:    SUSE                                             chinanorth
	data:    TrendMicro.DeepSecurity                          chinanorth


These lists can be quite long, so the example list above is just a snippet. Let's say that I noticed that Canonical is, indeed, an image publisher in the China North location. You can now find their offers by calling `azure vm image list-offers` and pass the location and the publisher at the prompts, like the following example:

    azure vm image list-offers
    info:    Executing command vm image list-offers
    Location: chinanorth
    Publisher: canonical
    + Getting virtual machine image offers (Publisher: "canonical" Location:"chinanorth")
    data:    Publisher  Offer         Location
    data:    ---------  ------------  --------
    data:    canonical  UbuntuServer  chinanorth  
    info:    vm image list-offers command OK

Now we know that in the China North region, Canonical publishes the **UbuntuServer** offer on Azure. But what SKUs? To get those, you call `azure vm image list-skus` and respond to the prompt with the location, publisher, and offer that you have discovered.

    azure vm image list-skus
    info:    Executing command vm image list-skus
    Location: chinanorth
    Publisher: canonical
    Offer: ubuntuserver
    + Getting virtual machine image skus (Publisher:"canonical" Offer:"ubuntuserver" Location:"chinanorth")
	data:    Publisher  Offer         sku          Location
	data:    ---------  ------------  -----------  ----------
	data:    canonical  ubuntuserver  12.04.5-LTS  chinanorth
	data:    canonical  ubuntuserver  14.04.2-LTS  chinanorth
	data:    canonical  ubuntuserver  14.04.3-LTS  chinanorth
	data:    canonical  ubuntuserver  14.10        chinanorth
	data:    canonical  ubuntuserver  15.04        chinanorth
	data:    canonical  ubuntuserver  15.10        chinanorth
	info:    vm image list-skus command OK

With this information, you can now find exactly the image you want by calling the original call at the top.

    azure vm image list chinanorth canonical ubuntuserver 14.04.2-LTS
    info:    Executing command vm image list
    + Getting virtual machine images (Publisher:"canonical" Offer:"ubuntuserver" Sku: "14.04.2-LTS" Location:"chinanorth")
	data:    Publisher  Offer         Sku          OS         Version          Location    Urn
	data:    ---------  ------------  -----------  ---------  ---------------  ----------  --------------------------------------------------
	data:    canonical  ubuntuserver  14.04.2-LTS  undefined  14.04.201507060  chinanorth  canonical:ubuntuserver:14.04.2-LTS:14.04.201507060
	info:    vm image list command OK

Now you can choose precisely the image you want to use. To create a virtual machine quickly by using the URN information, which you just found, or to use a template with that URN information, see [Using the Azure CLI for Mac, Linux, and Windows with Azure Resource Manager](/documentation/articles/xplat-cli-azure-resource-manager/).

## PowerShell

With PowerShell, type `Switch-AzureMode AzureResourceManager`. See [Using Azure CLI with Resource Manager](/documentation/articles/xplat-cli-azure-resource-manager/) and [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager/) for more complete update and configuration details.

> [AZURE.NOTE] With Azure PowerShell modules above 1.0, the `Switch-AzureMode` cmdlet was removed. With that version and more recent, please replace the commands below with the `Azure` portion replaced with `AzureRm`. If you are using Azure PowerShell modules below 1.0, you will use the below commands but you must first `Switch-AzureMode AzureResourceManager`. 


When creating a new virtual machine with Azure Resource Manager, in some cases you need to specify an image with the combination of the following image properties:

- Publisher
- Offer
- SKU

For example, these values are needed for the **Set-AzureVMSourceImage** PowerShell cmdlet or with a resource group template file in which you must specify the type of virtual machine to be created.

If you need to determine these values, you can navigate the images to determine these values:

1. List the image publishers.
2. For a given publisher, list their offers.
3. For a given offer, list their SKUs.

To do this in PowerShell, first switch to the Resource Manager mode of Azure PowerShell.

	Switch-AzureMode AzureResourceManager

For the first step above, list the publishers with these commands.

	$locName="<Azure location, such as China North>"
	Get-AzureVMImagePublisher -Location $locName | Select PublisherName

Fill in your chosen publisher name and run these commands.

	$pubName="<publisher>"
	Get-AzureVMImageOffer -Location $locName -Publisher $pubName | Select Offer

Fill in your chosen offer name and run these commands.

	$offerName="<offer>"
	Get-AzureVMImageSku -Location $locName -Publisher $pubName -Offer $offerName | Select Skus

From the display of the **Get-AzureVMImageSku** command, you have all the information you need to specify the image for a new virtual machine.

Here is an example.

	PS C:\> $locName="China North"
	PS C:\> Get-AzureVMImagePublisher -Location $locName | Select PublisherName

	PublisherName
	-------------
	a10networks
	aiscaler-cache-control-ddos-and-url-rewriting-
	alertlogic
	AlertLogic.Extension
	Barracuda.Azure.ConnectivityAgent
	barracudanetworks
	basho
	boxless
	bssw
	Canonical
	...

For the "MicrosoftWindowsServer" publisher:

	PS C:\> $pubName="MicrosoftWindowsServer"
	PS C:\> Get-AzureVMImageOffer -Location $locName -Publisher $pubName | Select Offer

	Offer
	-----
	WindowsServer

For the "WindowsServer" offer:

	PS C:\> $offerName="WindowsServer"
	PS C:\> Get-AzureVMImageSku -Location $locName -Publisher $pubName -Offer $offerName | Select Skus

	Skus
	----
	2008-R2-SP1
	2012-Datacenter
	2012-R2-Datacenter
	Windows-Server-Technical-Preview

From this list, copy the chosen SKU name, and you have all the information for the **Set-AzureVMSourceImage** PowerShell cmdlet or for a resource group template file that requires you to specify the publisher, offer, and SKU for an image.



<!--Image references-->
[5]: ./media/markdown-template-for-new-articles/octocats.png
[6]: ./media/markdown-template-for-new-articles/pretty49.png
[7]: ./media/markdown-template-for-new-articles/channel-9.png
[8]: ./media/markdown-template-for-new-articles/copytemplate.png

<!--Reference style links - using these makes the source content way more readable than using inline links-->
[gog]: http://google.com/
[yah]: http://search.yahoo.com/  
[msn]: http://search.msn.com/