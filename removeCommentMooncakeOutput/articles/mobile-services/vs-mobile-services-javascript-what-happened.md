<properties 
	pageTitle="What happens when you add Mobile Services to a Javascript app by using Visual Studio Connected Services" 
	description="Describes what happened to your Azure Mobile Services project in Visual Studio" 
	services="mobile-services" 
	documentationCenter="" 
	authors="TomArcher" 
	manager="douge" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="09/23/2015" 
	wacn.date=""/>

# What happens to my Javascript project when I add Azure Mobile Services using Connected Visual Studio Services?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-mobile-services-javascript-getting-started)
> - [What Happened](/documentation/articles/vs-mobile-services-javascript-what-happened)

###What happened to my project?

#####NuGet package added

The **WindowsAzure.MobileServices.WinJS** NuGet package was installed, including the Azure Mobile Service library in the `js\MobileServices.js` file.
  
#####Connection string values for Mobile Services 

In the `services\mobileServices\settings` folder, a new JavaScript (.js) file with a **MobileServiceClient** was generated that contains the selected mobile service's application URL and application key.  


#####References added to default.html

References to `MobileServices.js` and the settings file were added to `default.html`.  


#####Connected services files added

In the services folder, Connected Services configuration files were added.



 