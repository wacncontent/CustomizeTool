<properties
	pageTitle="Azure AD Connect: FAQ | Windows Azure"
	description="This page has frequently asked questions about Azure AD Connect."
	services="active-directory"
	documentationCenter=""
	authors="billmath"
	manager="stevenpo"
	editor="curtand"/>

<tags
	ms.service="active-directory"
	ms.date="12/02/2015"
	wacn.date=""/>

# Azure AD Connect FAQ

## General installation
**Q: Will installation work if the Azure AD Global Admin has 2FA enabled?**

Installation will not work in this case. The Global Admin installing Azure AD Connect must not have MFA enabled. We are aware of this limitation and will support this in the future.

**Q: Is there a way to install Azure AD Connect unattended?**

It is only supported to install Azure AD Connect using the installation wizard. An unattended and silent installation is not supported.

**Q: I have a forest where one domain cannot be contacted. How do I install Azure AD Connect?**

We have heard this feedback and will support this in a future release.

## Network
**Q: I have a firewall, network device, or something else that limits the maximum time connections can stay open on my network. How long should my client side timeout threshold be when using Azure AD Connect?**

All networking software, physical devices, or anything else that limits the maximum time connections can remain open should use a threshold of at least 5 minutes (300 seconds) for connectivity between the server where the Azure AD Connect client is installed and Azure Active Directory. This also applies to all previously released Microsoft Identity synchronization tools.

**Q: What do I do if I receive an email that asking me to renew my Office 365 certificate**

Use the guidance that is outlined in the article here to resolve to [here](/documentation/articles/active-directory-aadconnect-o365-certs) renew the certificate.

**Q: Are SLDs (Single Label Domains) supported?**

No, Azure AD Connect does not support on-premises forests/domains using SLDs.

**Q: Are "dotted" NetBios named supported?**

No, Azure AD Connect does not support on-premises forests/domains where the NetBios name contains a period "." in the name.

## Environment

**Q: Is it supported to rename the server after Azure AD Connect has been installed?**

No. Changing the server name will cause the sync engine to not be able to connect to the SQL database and the service will not be able to start.

## Identity data

**Q: The UPN (userPrincipalName) attribute in Azure AD does not match the on-prem UPN - why?**

See these articles:

- [User names in Office 365, Azure, or Intune don't match the on-premises UPN or alternate login ID](https://support.microsoft.com/kb/2523192)
- [Changes aren't synced by the Azure Active Directory Sync tool after you change the UPN of a user account to use a different federated domain](https://support.microsoft.com/kb/2669550)

## Custom configuration

**Q: Where are the PowerShell cmdlets for Azure AD Connect documented?**

With the exception of the cmdlets documented on this site, other PowerShell cmdlets found in Azure AD Connect are not supported for customer use.

**Q: Can I use "Server export/server import" found in service manager to move configuration between servers?**

No. This option will not retrieve all configuration settings and should not be used. You should instead use the wizard to create the base configuration on the second server and use the sync rule editor to generate PowerShell scripts to move any custom rule between servers.

## Troubleshooting

**Q: How can I get help with Azure AD Connect?**

[Search the Microsoft Knowledge Base (KB)](https://www.microsoft.com/Search/result.aspx?q=azure%20active%20directory%20connect&form=mssupport)

- Search the Microsoft Knowledge Base (KB) for technical solutions to common break-fix issues about Support for Azure AD Connect.

[Windows Azure Active Directory Forums](https://social.msdn.microsoft.com/Forums/azure/zh-cn/home?forum=WindowsAzureAD)

- You can search and browse for technical questions and answers from the community or ask your own question by clicking [here](https://social.msdn.microsoft.com/Forums/azure/zh-cn/newthread?category=windowsazureplatform&forum=WindowsAzureAD&prof=required).).


[Azure AD Connect customer support](https://manage.windowsazure.cn/?getsupport=true)

- Use this link to get support through the Azure Management Portal.
