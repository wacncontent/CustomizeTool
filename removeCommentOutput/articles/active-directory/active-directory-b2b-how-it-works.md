<properties
   pageTitle="Azure AD B2B collaboration preview: How it works | Windows Azure"
   description="Describes how Azure Active Directory B2B collaboration supports your cross-company relationships by enabling business partners to selectively access your corporate applications"
   services="active-directory"
   authors="viv-liu"
   manager="cliffdi"
   editor=""
   tags=""/>

<tags
	ms.service="active-directory"
	ms.date="10/27/2015"
	wacn.date=""/>

# Azure Active Directory (Azure AD) B2B collaboration preview: How it works
Azure AD B2B collaboration is based on an invite and redeem model. You provide the email addresses of the parties you want to work with, along with the applications you want them to use. Azure AD sends them an email invite with a link. The partner user follows the link and is prompted to sign in using their Azure AD account or sign up for a new Azure AD account.

1. Your admin invites partner users by uploading [a structured .csv file](/documentation/articles/active-directory-b2b-references-csv-file-format) using the Azure Management Portal.
2. The portal sends invite emails to these partner users.
3. The partner users click the link in the email, and are prompted to sign in using their work credentials (if they're already in Azure AD), or to sign up as an Azure AD B2B collaboration user.
4. Partner users are redirected to the application they were invited to, where they now have access.

## Directory operations
Partner users exist in your Azure AD as external users. This means your admin can provision licenses, assign group membership, and further grant access to corporate apps through the Azure Management Portal or using Azure PowerShell just like for users in your company.

While a paid Azure AD subscription (Basic or Premium) is not necessary to use Azure AD B2B, tenants who do have a paid Azure AD subscription (Basic or Premium) receive the following additional benefits:

 - Admins can assign groups to apps, providing for simpler management of invited user access.
 - Admin tenant branding is used to brand the invitation emails and redemption experience, providing more context to invited partner users.

## Related articles
 Browse our other articles on Azure B2B collaboration

 - [What is Azure AD B2B collaboration?](/documentation/articles/active-directory-b2b-what-is-azure-ad-b2b)
 - [Detailed walkthrough](/documentation/articles/active-directory-b2b-detailed-walkthrough)
 - [CSV file format reference](/documentation/articles/active-directory-b2b-references-csv-file-format)
 - [External user token format](/documentation/articles/active-directory-b2b-references-external-user-token-format)
 - [External user object attribute changes](/documentation/articles/active-directory-b2b-references-external-user-object-attribute-changes)
 - [Current preview limitations](/documentation/articles/active-directory-b2b-current-preview-limitations)
