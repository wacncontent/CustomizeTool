<properties
	pageTitle="Finding unsanctioned cloud applications with Cloud App Discovery | Windows Azure"
	description="Provides information about finding and managing applications with Cloud App Discovery, what are the benefits and how it works."
	services="active-directory"
	keywords="cloud app discovery, managing applications"
	documentationCenter=""
	authors="markusvi"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="11/20/2015"
	wacn.date=""/>

<!-- deleted by customization
# Finding unsanctioned cloud applications with Cloud App Discovery

## Overview
In modern enterprises, IT departments are often not aware of all the cloud applications that members of their organization use to do their work. It is easy to see why administrators would have concerns about unauthorized access to corporate data, possible data leakage and other security risks. This lack of awareness can make creating a plan for dealing with these security risks seem daunting.

Cloud App Discovery is a feature of Azure Active Directory (AD) Premium that enables you to discover cloud applications being used by the people in your organization.
-->
<!-- keep by customization: begin -->
# How can I discover unsanctioned cloud apps that are used within my organization

In modern enterprises, IT departments are often not aware of all the cloud applications that are used by the users to do their work.
 As a consequence of this, administrators often have concerns in conjunction with unauthorized access to corporate data, possible data leakage and other security risks inherent in the applications.
 Because they donât know how many or which apps are used, even getting started building a plan to deal with these risks seems to be daunting.

You can address these concerns by using Cloud App Discovery.
 Cloud App Discovery is a Premium feature of Azure Active Directory that enables you to discover cloud applications that are uses by the employees in your organization. 

<!-- keep by customization: end -->

**With Cloud App Discovery, you can:**

<!-- deleted by customization
- Find the cloud applications being used and measure that usage by number of users, volume of traffic or number of web requests to the application.
- Identify the users that are using an application.
- Export data for offline analysis.
- Bring these applications under IT control and enable single sign on for user management.

## How it works
1. Application usage agents are installed on user's computers.
2. The application usage information captured by the agents is sent over a secure, encrypted channel to the cloud app discovery service.
3. The Cloud App Discovery service evaluates the data and generates reports.

![Cloud App Discovery diagram](./media/active-directory-cloudappdiscovery/cad01.png)

To get started with Cloud App Discovery, see [Getting Started With Cloud App Discovery](http://social.technet.microsoft.com/wiki/contents/articles/30962.getting-started-with-cloud-app-discovery.aspx)

## Related articles
- [Cloud App Discovery Security and Privacy Considerations](/documentation/articles/active-directory-cloudappdiscovery-security-and-privacy-considerations)  
- [Cloud App Discovery Group Policy Deployment Guide](http://social.technet.microsoft.com/wiki/contents/articles/30965.cloud-app-discovery-group-policy-deployment-guide.aspx)
- [Cloud App Discovery System Center Deployment Guide](http://social.technet.microsoft.com/wiki/contents/articles/30968.cloud-app-discovery-system-center-deployment-guide.aspx)
- [Cloud App Discovery Registry Settings for Proxy Servers with Custom Ports](/documentation/articles/active-directory-cloudappdiscovery-registry-settings-for-proxy-services)
- [Cloud App Discovery Agent Changelog ](http://social.technet.microsoft.com/wiki/contents/articles/24616.cloud-app-discovery-agent-changelog.aspx)
- [Cloud App Discovery Frequently Asked Questions](http://social.technet.microsoft.com/wiki/contents/articles/24037.cloud-app-discovery-frequently-asked-questions.aspx)
-->
<!-- keep by customization: begin -->
* Discover applications in use and measure usage by number of users, volume of traffic or number of web requests to the application. 
* Identify the users that are using an application.
* Export data for addition offline analysis. 
* Prioritize applications to bring under IT control and integrate applications easily to enable Single Sign-on and user management. 

With cloud app discovery, the data retrieval part is accomplished by agents that run on computers in your environments.
The app usage information that is captured by the agents is send over a secure, encrypted channel to the cloud app discovery service.
The cloud app discovery service evaluates the data and generates reports you can use to analyze your environment.


<center>![How Cloud App Discovery Works](./media/active-directory-cloudappdiscovery/cad01.png)</center>

##Next Steps


* To learn more about How Cloud app discovery works, see [Getting Started With Cloud App Discovery](http://social.technet.microsoft.com/wiki/contents/articles/30962.getting-started-with-cloud-app-discovery.aspx) 
* For security and privacy considerations, see [Cloud App Discovery Security and Privacy Considerations](/documentation/articles/active-directory-cloudappdiscovery-security-and-privacy-considerations) 
* For information about deploying the Cloud App Discovery agent in an enterprise environment with: 
 * Active Directory Group Policy Management, see  [Cloud App Discovery Group Policy Deployment Guide](http://social.technet.microsoft.com/wiki/contents/articles/30965.cloud-app-discovery-group-policy-deployment-guide.aspx) 
 * Microsoft System Center Configuration Manager, see [Cloud App Discovery System Center Deployment Guide](http://social.technet.microsoft.com/wiki/contents/articles/30968.cloud-app-discovery-system-center-deployment-guide.aspx) 
 * Proxy servers with custom ports, see [Cloud App Discovery Registry Settings for Proxy Servers with Custom Ports](/documentation/articles/active-directory-cloudappdiscovery-registry-settings-for-proxy-services) 





**Additional Resources**


* [Cloud App Discovery - Agent Changelog ](http://social.technet.microsoft.com/wiki/contents/articles/24616.cloud-app-discovery-agent-changelog.aspx)
* [Cloud App Discovery - Frequently Asked Questions](http://social.technet.microsoft.com/wiki/contents/articles/24037.cloud-app-discovery-frequently-asked-questions.aspx)


<!-- keep by customization: end -->
