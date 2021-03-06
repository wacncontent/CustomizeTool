<properties 
	pageTitle="Working with Azure Media Services Jobs" 
	description="This topics gives an overview of how to manage Managing Azure Media Services Jobs." 
	services="media-services" 
	documentationCenter="" 
	authors="juliako" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="02/03/2016"
	wacn.date=""/>

#Working with Azure Media Services Jobs

A **Job** contains metadata about the processing to be performed. Each **Job** contains one or more **Tasks** that specify an atomic processing task, its input Assets, output Assets, a media processor and its associated settings. For more information on encoder settings, see Encoder Guides and Encoder Schemas.

An encoding job is usually combined with other processing, for example, packaging, or encrypting the asset or assets generated by the encoder. Tasks within a Job can be chained together, where the output asset of one task is given as the input asset to the next task. In this way one job can contain all of the processing necessary for a media presentation.

This section provides links to common tasks that you would perform when working with Jobs\Tasks.

>[AZURE.NOTE]There is currently a limit of 30 tasks per job. If you need to chain more than 30 tasks, create more than one job to contain the tasks.


##Getting Media Processor

Get Media Processor with **.NET** or **REST API**.

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-get-media-processor">.NET</a>
<a href="/documentation/articles/media-services-rest-get-media-processor">REST API</a>
</div>
##Creating jobs

A job is an entity that contains metadata about a set of tasks (for example, encoding or indexing). Each task performs an atomic operation on the input asset(s). For example on how to create encoding jobs, see:

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-manage-content#encode">Portal</a>
<a href="/documentation/articles/media-services-dotnet-encode-asset">.NET</a>
<a href="/documentation/articles/media-services-rest-encode-asset">REST API</a>
</div>
##Indexing

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-manage-content">Portal</a>
<a href="/documentation/articles/media-services-index-content">.NET</a>
</div>
##Encoding

Encode with **Media Encoder Standard** using **Azure Management Portal**, **.NET**, or **REST API**.

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-manage-content#encode">Portal</a>
<a href="/documentation/articles/media-services-dotnet-encode-asset">.NET</a>
<a href="/documentation/articles/media-services-rest-encode-asset">REST API</a>
</div>
##Monitoring job progress

Monitor job progress using **Azure Management Portal**, **.NET** or **REST API**.

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-portal-check-job-progress">Portal</a>
<a href="/documentation/articles/media-services-check-job-progress">.NET</a>
<a href="/documentation/articles/media-services-rest-check-job-progress">REST API</a>
</div>
##Listing 

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-dotnet-manage-entities#list-jobs-and-assets">.NET</a>
<a href="/documentation/articles/media-services-rest-manage-entities#querying-entities">REST</a>
</div>
##Deleting jobs

<div class="technical-azure-selector">
<a href="/documentation/articles/media-services-dotnet-manage-entities#delete-a-job">.NET</a>
<a href="/documentation/articles/media-services-rest-manage-entities##deleting-entities">REST</a>
</div>
##Related links

[Quotas and Limitations](/documentation/articles/media-services-quotas-and-limitations) Ă˘ÂÂ Describes quotas used and limitations of the Media Services Encoder

