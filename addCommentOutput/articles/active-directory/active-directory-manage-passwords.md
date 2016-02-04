<properties
	pageTitle="Manage passwords in Azure Active Directory | Windows Azure"
	description="How to manage passwords in Azure Active Directory."
	services="active-directory"
	documentationCenter=""
	authors="curtand"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="12/01/2015"
	wacn.date=""/>

# Manage passwords in Azure Active Directory

If you are an administrator, you can reset a userâs password in Azure Active Directory (Azure AD) in the Azure Management Portal. Click the name of your directory and on the Users page, click the name of the user and at the bottom of the portal click **Reset Password**.

This rest of this topic covers the full set of password management capabilities that Azure AD supports, including:

- **Self-service password** change allows end users or administrators to change their expired or non-expired passwords without calling an administrator or helpdesk for support.
- **Self-service password** reset allows end users or administrators to reset their passwords automatically without calling an administrator or helpdesk for support. Self-service password reset requires Azure AD Premium or Basic. For more information, see [Azure Active Directory editions](/documentation/articles/active-directory-editions).
- **Administrator-initiated password reset** allows an administrator to reset an end userâs or another administratorâs password from within the Azure Management Portal.
- **Password management activity reports** give administrators insights into password reset and registration activity occurring in their organization.
- **Password writeback** allows management of on-premises passwords from the cloud so all of the above scenarios can be performed by, or on the behalf of, federated or password synchronized users. Password writeback requires Azure AD Premium. <!-- deleted by customization For --><!-- keep by customization: begin --><!--For <!-- keep by customization: end --> more information, see [Getting started with Azure Active Directory <!-- deleted by customization Premium](/documentation/articles/active-directory-get-started-premium). --><!-- keep by customization: begin --> Premium](/documentation/articles/active-directory-get-started-premium).--><!-- keep by customization: end -->

> [AZURE.NOTE]
> Azure AD Premium is available for Chinese customers using the world wide instance of Azure AD. Azure AD Premium is not currently supported in the Windows Azure service operated by 21Vianet in China. For more information, contact us at the [Azure Active Directory Forum](http://feedback.azure.com/forums/169401-azure-active-directory).

Use the following links to jump to the documentation you are most interested in:

- [Overview: password management in Azure AD](/documentation/articles/active-directory-passwords-how-it-works)
- [Self-service password reset in Azure AD: how to enable, configure, and test self-service password reset](/documentation/articles/active-directory-passwords-getting-started#enable-users-to-reset-their-azure-ad-passwords)
- [Self-service password reset in Azure AD: how to customize password reset to meet your needs](/documentation/articles/active-directory-passwords-customize)
- [Self-service password reset in Azure AD: deployment and management best practices](/documentation/articles/active-directory-passwords-best-practices)
- [Password management reports in Azure AD: how to view password management activity in your tenant](/documentation/articles/active-directory-passwords-get-insights)
- [Password writeback: how to configure Azure AD to manage on-premises passwords](/documentation/articles/active-directory-passwords-getting-started#enable-users-to-reset-or-change-their-ad-passwords)
- [Troubleshooting Azure AD password management](/documentation/articles/active-directory-passwords-troubleshoot)
- [FAQ for Azure AD password management](/documentation/articles/active-directory-passwords-faq)

## What's next

- [Administering Azure AD](/documentation/articles/active-directory-administer)
- [Create or edit users in Azure AD](/documentation/articles/active-directory-create-users)
- [Manage groups in Azure AD](/documentation/articles/active-directory-manage-groups)
