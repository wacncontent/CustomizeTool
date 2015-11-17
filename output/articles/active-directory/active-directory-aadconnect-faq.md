<properties
	pageTitle="Azure AD Connect FAQ | Windows Azure"
	description="This page has frequently asked questions about Azure AD Connect."
	services="active-directory"
	documentationCenter=""
	authors="billmath"
	manager="stevenpo"
	editor="curtand"/>

<tags
	ms.service="active-directory"
	ms.date="10/13/2015"
	wacn.date=""/>

# Azure Active Directory Connect FAQ

## Express installation

## Custom installation

## Network
**Q: I have a firewall, network device, or something else that limits the maximum time connections can stay open on my network. How long should my client side timeout threshold be when using Azure AD Connect?**

All networking software, physical devices, or anything else that limits the maximum time connections can remain open should use a threshold of at least 5 minutes (300 seconds) for connectivity between the server where the Azure AD Connect client is installed and Azure Active Directory. This also applies to all previously released Microsoft Identity synchronization tools.


**Q: What do I do if I receive an email that asking me to renew my Office 365 certificate**

Use the guidance that is outlined in the article here to resolve to [here](/documentation/articles/active-directory-aadconnect-o365-certs) renew the certificate.

## Troubleshooting

**Q: How can I get help with Azure AD Connect?**

[Search the Microsoft Knowledge Base (KB)](https://www.microsoft.com/Search/result.aspx?q=azure%20active%20directory%20connect&form=mssupport)

- Search the Microsoft Knowledge Base (KB) for technical solutions to common break-fix issues about Support for Azure AD Connect.

[Windows Azure Active Directory Forums](https://social.msdn.microsoft.com/Forums/azure/zh-cn/home?forum=WindowsAzureAD)

- You can search and browse for technical questions and answers from the community or ask your own question by clicking [here](https://social.msdn.microsoft.com/Forums/azure/newthread?category=windowsazureplatform&forum=WindowsAzureAD&prof=required).


[Azure AD Connect customer support](https://manage.windowsazure.cn/?getsupport=true)

- Use this link to get support through the Azure Management Portal.

<!-- keep by customization: begin -->
**Q:What do I do if I receive an email that asking me to renew my Office 365 certificate**

Use the guidance that is outlined in the article here to resolve to [here](/documentation/articles/active-directory-aadconnect-o365-certs) renew the certificate.



<!-- keep by customization: end -->

