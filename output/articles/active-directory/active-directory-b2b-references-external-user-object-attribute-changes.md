<properties
   pageTitle="External user object attribute changes for Azure Active Directory B2B collaboration preview | Windows Azure"
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

# External user object attribute changes for Azure Active Directory (Azure AD) B2B collaboration preview
Each user in an Azure AD directory is represented by a user object. The user object in Azure AD undergoes attribute changes in various stages of the B2B collaboration invite-redeem flow. The user object representing the partner user in the directory has attributes that change at redeem time, when the partner user clicks the link in the invite email. Specifically:

- The **SignInName** and **AltSecId** attributes are populated
- The **DisplayName** attribute changes from the User Principal Name (user_fabrikam.com#EXT#@contoso.com) to the sign-in name (user@fabrikam.com)

Tracking these attributes in Azure AD can help you troubleshoot whether or not a partner user has redeemed their B2B collaboration invitation.

## Related articles
Browse our other articles on Azure B2B collaboration:

- [What is Azure AD B2B collaboration?](/documentation/articles/active-directory-b2b-what-is-azure-ad-b2b)
- [How it works](/documentation/articles/active-directory-b2b-how-it-works)
- [Detailed walkthrough](/documentation/articles/active-directory-b2b-detailed-walkthrough)
- [CSV file format reference](/documentation/articles/active-directory-b2b-references-csv-file-format)
- [External user token format](/documentation/articles/active-directory-b2b-references-external-user-token-format)
- [Current preview limitations](/documentation/articles/active-directory-b2b-current-preview-limitations)
