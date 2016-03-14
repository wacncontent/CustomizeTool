<!-- to be customized -->

<properties
   pageTitle="Navigate and select VM images | Windows Azure"
   description="Learn how to determine the publisher, offer, and SKU for images when creating an Azure virtual machine with the Resource Manager deployment model."
   services="virtual-machines"
   documentationCenter=""
   authors="squillace"
   manager="timlt"
   editor=""
   tags="azure-resource-manager"
   />

<tags
	ms.service="virtual-machines"
	ms.date="12/08/2015"
	wacn.date=""/>

# Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI

## Table of commonly used images


| PublisherName | äş§ĺ | Name |
|:---------------------------------|:-------------------------------------------|:---------------------------------|:--------------------|
| OpenLogic | CentOS | f1179221e23b4dbb89e39d70e5bc9e72__OpenLogic-CentOS-70-20150904 |
| OpenLogic | CentOS | f1179221e23b4dbb89e39d70e5bc9e72__OpenLogic-CentOS-71-20150731 |
| Microsoft SharePoint Group | MicrosoftSharePointServer | 9619bdbee1584b6f80d684565a6eeb74__SharePoint-2013-Trial-3-26-2014 |
| Microsoft SQL Server Group | SQL2014-WS2012R2 | 74bb2f0b8dcc47fbb2914b60ed940c35__SQL-Server-2014-RTM-12.0.2361.0-DataWarehousing-CHS-Win2012R2-cy14su05 |
| Microsoft SQL Server Group | SQL2014-WS2012R2 | 74bb2f0b8dcc47fbb2914b60ed940c35__SQL-Server-2014-RTM-12.0.2361.0-Web-CHS-Win2012R2-cy14su05 |
| Canonical | UbuntuServer | b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_5-LTS-amd64-server-20150204-en-us-30GB |
| Canonical | UbuntuServer | b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_3-LTS-amd64-server-20151019-en-us-30GB |
| Microsoft | WindowsServer | 55bc2b193643443bb879a78bda516fc8__Windows-Server-2012-Datacenter-20151021-zh.cn-127GB.vhd |
| Microsoft | WindowsServer | 55bc2b193643443bb879a78bda516fc8__Windows-Server-2012-R2-20151021-zh.cn-127GB.vhd |
| Microsoft | WindowsServer | 55bc2b193643443bb879a78bda516fc8__Win2K8R2SP1-Datacenter-20151021-zh.cn-127GB.vhd |
| Microsoft | WindowsServer | 55bc2b193643443bb879a78bda516fc8__Windows-Server-Technical-Preview-20151118-en.us-127GB.vhd |
| Microsoft Windows Server Essentials Group | WindowsServerEssentials | 0c5c79005aae478e8883bf950a861ce0__Windows-Server-2012-Essentials-20141204-zhcn |
| Microsoft Windows Server HPC Pack team | WindowsServerHPCPack | 86f94d8ddf9d4aad9b064efb793ff4c2__HPC-Pack-2012R2-Update1-4.3.4660.0-WS2012R2-CHN |



## Azure CLI

The easiest and quickest way to locate an image is to call the `azure vm image list` command and pass the publisher name, and OS. For example, the following list is only a short example -- many lists are quite long -- if you know that "Canonical" is a publisher for the "Ubuntu". You can use the following bash command to search

	azure vm image list | cat | grep -E "data:\s*Name|data:\s*-+|data:\s*[^\s]*Ubuntu.*\s*Canonical"

And, you will get the following output.

	data:    Name                                                                                                      Category  OS       Publisher
	data:    --------------------------------------------------------------------------------------------------------  --------  -------  -----------------------------------------
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_3-LTS-amd64-server-20140130-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_4-LTS-amd64-server-20140529-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_4-LTS-amd64-server-20140606-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_4-LTS-amd64-server-20140619-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_4-LTS-amd64-server-20140702-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_5-LTS-amd64-server-20140829.2-en-us-30GB                   Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_5-LTS-amd64-server-20140925.1-en-us-30GB                   Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-12_04_5-LTS-amd64-server-20150204-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140226.1-beta1-en-us-30GB               Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140416.1-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140528-en-us-30GB                       Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04-LTS-amd64-server-20140606.1-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_1-LTS-amd64-server-20140909-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_1-LTS-amd64-server-20140927-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_1-LTS-amd64-server-20141125-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_1-LTS-amd64-server-20150123-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_2-LTS-amd64-server-20150706-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_04_3-LTS-amd64-server-20151019-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-14_10-amd64-server-20140826-beta1-en-us-30GB                     Public    Linux    Canonical
	data:    b549f4301d0b4295b8e76ceb65df47d4__Ubuntu-15_04-amd64-server-20150707-en-us-30GB                           Public    Linux    Canonical

More information about how to use these images, see [Create a multi-VM deployment with the Azure CLI](/documentation/articles/virtual-machines-create-multi-vm-deployment-xplat-cli)

## PowerShell

When creating a new virtual machine, in some cases you need to specify an image name. And, these image name can be achieved by `Get-AzureVMImage`. However, the list is quite long, so you need to use the following PowerShell script to filter the result of `Get-AzureVMImage`.

This sample will get image with name containing **Ubuntu**, OS equal to **Linux**, Publisher equal to **Canonical**, and Label containing **14.04.3**

	$images = Get-AzureVMImage
	foreach ($image in $images){
		if (($image.ImageName -like '*Ubuntu*') -and `
			($image.OS -eq 'Linux') -and `
			($image.PublisherName -eq 'Canonical') -and `
			($image.Label -like '*14.04.3*')){
			$image
		}
	}

More information about how to use these images, see [Create a SQL Server Virtual Machine in Azure (PowerShell)](/documentation/articles/virtual-machines-sql-server-create-vm-with-powershell)

<!--Image references-->
[5]: ./media/markdown-template-for-new-articles/octocats.png
[6]: ./media/markdown-template-for-new-articles/pretty49.png
[7]: ./media/markdown-template-for-new-articles/channel-9.png
[8]: ./media/markdown-template-for-new-articles/copytemplate.png

<!--Reference style links - using these makes the source content way more readable than using inline links-->
[gog]: http://google.com/
[yah]: http://search.yahoo.com/  
[msn]: http://search.msn.com/
