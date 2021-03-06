<properties 
	pageTitle="Media Encoder Standard formats and codecs" 
	description="This topic gives an overview of Azure Media Encoder Standard formats and codecs." 
	services="media-services" 
	documentationCenter="" 
	authors="juliako,anilmur" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="10/15/2015"
	wacn.date=""/>

#Media Encoder Standard Formats and Codecs


This document contains a list of the most common import and export file formats that you can use with Media Encoder Standard.


##Input Container/File Formats

File formats (file extensions)|Supported
---|---|---|---
FLV (with H.264 and AAC codecs) (.flv)			|Yes 
MXF	(.mxf)					|Yes 
GXF	(.gxf)					|Yes 
MPEG2-PS, MPEG2-TS, 3GP (.ts, .ps, .3gp, .3gpp, .mpg)	|Yes 
Windows Media Video (WMV)/ASF (.wmv, .asf) |Yes 
AVI (Uncompressed 8bit/10bit) (.avi)|Yes 
MP4 (.mp4, .m4a, .m4v)/ISMV (.isma, .ismv)|Yes 
[Microsoft Digital Video Recording(DVR-MS)](https://msdn.microsoft.com/zh-cn/library/windows/desktop/dd692984) (.dvr-ms) |Yes 
Matroska/WebM (.mkv)		|Yes 
WAVE/WAV (.wav)	|Yes 
QuickTime (.mov) |Yes
 
###Audio formats in input containers 

Media Encoder Standard supports carrying the following audio formats in input containers:

- MXF, GXF and QuickTime files which have audio tracks with interleaved stereo or 5.1 samples

or

- MXF, GXF and QuickTime files where the audio is carried as separate PCM tracks but the channel mapping (to stereo or 5.1) can be deduced from the file metadata

Note that support for explicit/user-supplied channel mapping will be provided in the near future.


##Input Video Codecs

Input Video Codecs|Supported
---|---|---|---
AVC 8-bit/10-bit, up to 4:2:2, including AVCIntra	|8 bit 4:2:0 and 4:2:2 
Avid DNxHD (in MXF)									|Yes 
DVCPro/DVCProHD (in MXF)							|Yes 
Digital video (DV) (in AVI files)                   |Yes
JPEG 2000											|Yes 
MPEG-2 (up to 422 Profile and High Level; including variants such as XDCAM, XDCAM HD, XDCAM IMX, CableLabs速 and D10)|Up to 422 Profile 
MPEG-1												|Yes 
VC-1/WMV9											|Yes 
Canopus HQ/HQX										|No 
MPEG-4 Part 2										|Yes 
[Theora](https://zh.wikipedia.org/wiki/Theora)		|Yes 
YUV420 uncompressed, or mezzanine					|Yes
Apple ProRes 422									|Yes
Apple ProRes 422 LT	|Yes
Apple ProRes 422 HQ |Yes
Apple ProRes Proxy|Yes
Apple ProRes 4444 |Yes
Apple ProRes 4444 XQ |Yes



##Input Audio Codecs

Input Audio Codecs|Supported
---|---|---|---
AAC (AAC-LC, AAC-HE, and AAC-HEv2; up to 5.1)|Yes 
MPEG Layer 2|Yes 
MP3 (MPEG-1 Audio Layer 3)|Yes 
Windows Media Audio|Yes 
WAV/PCM|Yes 
[FLAC](https://zh.wikipedia.org/wiki/FLAC)</a>|Yes 
<!-- deleted by customization
[Opus](https://zh.wikipedia.org/wiki/Opus_codec |Yes 
-->
<!-- keep by customization: begin -->
[Opus](https://en.wikipedia.org/wiki/Opus_codec) |Yes 
<!-- keep by customization: end -->
[Vorbis](https://en.wikipedia.org/wiki/Vorbis)</a>|Yes 
AMR (adaptive multi-rate)|Yes
AES (SMPTE 331M and 302M, AES3-2003)		|No 
Dolby速 E									|No 
Dolby速 Digital (AC3)						|No 
Dolby速 Digital Plus (E-AC3)					|No 


##Output Formats and codecs

The following table lists the codecs and file formats that are supported for export.


File Format|Video Codec|Audio Codec
---|---|---
MP4 <br/><br/>(including multi-bitrate MP4 containers) |H.264 (High, Main, and Baseline Profiles)|AAC-LC, HE-AAC v1, HE-AAC v2 
MPEG2-TS |H.264 (High, Main, and Baseline Profiles)|AAC-LC, HE-AAC v1, HE-AAC v2 


<!-- deleted by customization

##Media Services learning paths

[AZURE.INCLUDE [media-services-learning-paths-include](../includes/media-services-learning-paths-include.md)]

##Provide feedback

[AZURE.INCLUDE [media-services-user-voice-include](../includes/media-services-user-voice-include.md)]

-->
##See also

[Encoding On-Demand Content with Azure Media Services](/documentation/articles/media-services-encode-asset)

[How to encode with Media Encoder Standard](/documentation/articles/media-services-dotnet-encode-with-media-encoder-standard)
