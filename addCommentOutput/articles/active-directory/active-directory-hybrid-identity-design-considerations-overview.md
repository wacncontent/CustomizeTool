<properties
	pageTitle="Azure Active Directory hybrid identity design considerations - overview | Windows Azure"
	description="Overview and content map of Hybrid Identity design considerations guide"
	documentationCenter=""
	services="active-directory"
	authors="yuridio"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/07/2015"
	wacn.date=""/>

# Azure Active Directory Hybrid Identity Design Considerations

Consumer-based devices are proliferating the corporate world, and cloud-based software-as-a-service (SaaS) applications are easy to adopt. As a result, maintaining control of users' application access across internal datacenters and cloud platforms is challenging.  Microsoft's identity solutions span on-premises and cloud-based capabilities, creating a single user identity for authentication and authorization to all resources, regardless of location. We call this Hybrid Identity. There are different design and configuration options for hybrid identity using Microsoft solutions, and in some case it might be difficult to determine which combination will best meet the needs of your organization. This Hybrid Identity Design Considerations Guide will help you to understand how to design a hybrid identity solution that best fits the business and technology needs for your organization.  This guide will detail a series of steps and tasks that you can follow to help you design a hybrid identity solution that meets your organization's unique requirements. Throughout the steps and tasks, the guide will present the relevant technologies and feature options available to organizations to meet functional and service quality (such as availability, scalability, performance, manageability, and security) level requirements. 
Specifically, the hybrid identity design considerations guide goals are to answer the following questions: 

- What questions do I need to ask and answer to drive a hybrid identity-specific design for a technology or problem domain that best meets my requirements?
- What sequence of activities should I complete to design a hybrid identity solution for the technology or problem domain? 
- What hybrid identity technology and configuration options are available to help me meet my requirements? What are the trade-offs between those options so that I can select the best option for my business?


## Who is this guide intended for?
 CIO, CITO, Chief Identity Architects, Enterprise Architects and IT Architects responsible for designing a hybrid identity solution for medium or large organizations.

## How can this guide help you? 
You can use this guide to understand how to design a hybrid identity solution that is able to integrate a cloud based identity management system with your current on-premises identity solution. The following graphic shows an example a hybrid identity solution that enables IT Admins to manage to integrate their current Windows Server Active Directory solution located on-premises with Windows Azure Active Directory to enable users to use Single Sign-On (SSO) across applications located in the cloud and on-premises.

![](./media/hybrid-id-design-considerations/hybridID-example.png)


The above illustration is an example of a hybrid identity solution that is leveraging cloud services to integrate with on-premises capabilities in order to provide a single experience to the end user authentication process and to facilitate IT managing those resources. Although this can be a very common scenario, every organization's hybrid identity design is likely to be different than the example illustrated in Figure 1 due to different requirements. 
This guide provides a series of steps and tasks that you can follow to design a hybrid identity solution that meets your organization's unique requirements. Throughout the following steps and tasks, the guide presents the relevant technologies and feature options available to you to meet functional and service quality level requirements for your organization.

**Assumptions**: You have some experience with Windows Server, Active Directory Domain Services and Azure Active Directory. In this document, we assume you are looking for how these solutions can meet your business needs on their own or in an integrated solution.

## Design considerations overview
This document provides a set of steps and tasks that you can follow to design a hybrid identity solution that best meets your requirements. The steps are presented in an ordered sequence. Design considerations you learn in later steps may require you to change decisions you made in earlier steps, however, due to conflicting design choices. Every attempt is made to alert you to potential design conflicts throughout the document. 

You will arrive at the design that best meets your requirements only after iterating through the steps as many times as necessary to incorporate all of the considerations within the document. 

| Hybrid Identity Phase                                             | Topic List                                                                                                                                                                                       |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Determine identity requirements                                   | [Determine business needs](/documentation/articles/active-directory-hybrid-identity-design-considerations-business-needs)<br> [Determine directory synchronization requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-directory-sync-requirements)<br> [Determine multi-factor authentication requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-multifactor-auth-requirements)<br> [Define a hybrid identity adoption strategy](/documentation/articles/active-directory-hybrid-identity-design-considerations-identity-adoption-strategy)                       |
| Plan for enhancing data security through strong identity solution | [Determine data protection requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-dataprotection-requirements) <br> [Determine content management requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-contentmgt-requirements)<br> [Determine access control requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-accesscontrol-requirements)<br> [Determine incident response requirements](/documentation/articles/active-directory-hybrid-identity-design-considerations-incident-response-requirements) <br> [Define data protection strategy](/documentation/articles/active-directory-hybrid-identity-design-considerations-data-protection-strategy)  |
| Plan for hybrid identity lifecycle                                | [Determine hybrid identity management tasks](/documentation/articles/active-directory-hybrid-identity-design-considerations-hybridId-management-tasks) <br> [Synchronization Management](/documentation/articles/active-directory-hybrid-identity-design-considerations-hybridId-management-tasks)<br> [Determine hybrid identity management adoption strategy](/documentation/articles/active-directory-hybrid-identity-design-considerations-lifecycle-adoption-strategy) |     


##Download this guide
You can download a pdf version of the Hybrid Identity Design Considerations guide from the [Technet gallery](https://gallery.technet.microsoft.com/Azure-Hybrid-Identity-b06c8288). 

                                                             