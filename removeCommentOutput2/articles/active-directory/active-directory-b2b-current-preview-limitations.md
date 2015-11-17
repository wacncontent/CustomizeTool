<properties
   pageTitle="Current preview limitations for Azure Active Directory B2B collaboration | Windows Azure"
   description="Azure Active Directory B2B supports your cross-company relationships by enabling business partners to selectively access your corporate applications"
   services="active-directory"
   authors="viv-liu"
   manager="cliffdi"
   editor=""
   tags=""/>

<tags
	ms.service="active-directory"
	ms.date="10/27/2015"
	wacn.date=""/>

# Current preview limitations for Azure Active Directory (Azure AD) B2B collaboration

- Multi-factor authentication (MFA) not supported on external users. For example, if Contoso has MFA, but Partner Org does not, then Partner Org users can't be granted MFA through B2B collaboration.
- Invites are possible only via CSV; individual invites and API access are not supported.
- Only Azure AD Global Administrators can upload .csv files.
- Invitations to consumer email addresses (such as hotmail.com, Gmail.com, or comcast.net) are currently not supported.
- External user access to on-premises applications not tested.
- External users are not automatically cleaned up when the actual user is deleted from their directory.
- Invitations to DLs are not supported.
- Maximum of 2,000 records can be uploaded via CSV.

## Related articles
Browse our other articles on Azure B2B collaboration:

- [What is Azure AD B2B collaboration?](/documentation/articles/active-directory-b2b-what-is-azure-ad-b2b)
- [How it works](/documentation/articles/active-directory-b2b-how-it-works)
- [Detailed walkthrough](/documentation/articles/active-directory-b2b-detailed-walkthrough)
- [CSV file format reference](/documentation/articles/active-directory-b2b-references-csv-file-format)
- [External user token format](/documentation/articles/active-directory-b2b-references-external-user-token-format)
- [External user object attribute changes](/documentation/articles/active-directory-b2b-references-external-user-object-attribute-changes)
