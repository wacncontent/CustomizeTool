<properties
   pageTitle="External user token format for Azure Active Directory B2B collaboration preview | Windows Azure"
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

# External user token format for Azure Active Directory (Azure AD) B2B collaboration preview
The claims for a standard Azure AD token are described in the [Supported Token and Claim Types](/documentation/articles/active-directory-token-and-claims) article on azure.microsoft.com.

The claims that are different for an authenticated B2B collaboration external user are as follows:<br/>
- **OID:** the object ID from the resource tenant<br/>
- **TID**: tenant ID from the resource tenant<br/>
- **Issuer**: this is the resource tenant<br/>
- **IDP**: this is the home tenant of the user<br/>
- **AltSecId**: this is the alternative security ID, which is opaque to you<br/>

## Related articles
Browse our other articles on Azure B2B collaboration:

- [What is Azure AD B2B collaboration?](/documentation/articles/active-directory-b2b-what-is-azure-ad-b2b)
- [How it works](/documentation/articles/active-directory-b2b-how-it-works)
- [Detailed walkthrough](/documentation/articles/active-directory-b2b-detailed-walkthrough)
- [CSV file format reference](/documentation/articles/active-directory-b2b-references-csv-file-format)
- [External user object attribute changes](/documentation/articles/active-directory-b2b-references-external-user-object-attribute-changes)
- [Current preview limitations](/documentation/articles/active-directory-b2b-current-preview-limitations)
