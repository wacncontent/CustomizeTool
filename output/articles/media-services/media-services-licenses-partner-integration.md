<properties 
	pageTitle="Using partners to deliver Widevine licenses to Azure Media Services" 
	description="This article describes how you can use Azure Media Services (AMS) to deliver a stream that is dynamically encrypted by AMS with both PlayReady and Widevine DRMs. The PlayReady license comes from Media Services PlayReady license server and Widevine license is delivered by castLabs license server." 
	services="media-services" 
	documentationCenter="" 
	authors="Juliako" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="10/07/2015"
	wacn.date=""/>

#Using partners to deliver Widevine licenses to Azure Media Services

##Overview

Windows Azure Media Services enables you to deliver MPEG-DASH protected with Widevine DRM, which is encrypted per the Common Encryption (CENC) specification.

Starting with the Media Services .NET SDK version 3.5.2, Media Services enables you to configure Widevine license template and get Widevine licenses. You can also use the following AMS partners to help you deliver Widevine licenses: [Axinom](http://www.axinom.com/press/ibc-axinom-drm-6/), [EZDRM](http://ezdrm.com/), [castLabs](http://castlabs.com/company/partners/azure/).

##castLabs

You can use [castLabs](http://castlabs.com/company/partners/azure/) to deliver Widevine licenses. For more information, see [Using castLabs to deliver DRM licenses to Azure Media Services](/documentation/articles/media-services-castlabs-integration)

##Axinom

You can use [Axinom](http://www.axinom.com/press/ibc-axinom-drm-6/) to deliver Widevine licenses. For more information, see [Using Axinom to deliver DRM licenses to Azure Media Services](/documentation/articles/media-services-axinom-integration)


##Media Services learning paths

[AZURE.INCLUDE [media-services-learning-paths-include](../includes/media-services-learning-paths-include.md)]

##Provide feedback

[AZURE.INCLUDE [media-services-user-voice-include](../includes/media-services-user-voice-include.md)]

##See also

[Using PlayReady and/or Widevine dynamic common encryption](/documentation/articles/media-services-protect-with-drm)

[Mingfei's blog](https://azure.microsoft.com/blog/azure-media-services-adds-google-widevine-packaging-for-delivering-multi-drm-stream/)

