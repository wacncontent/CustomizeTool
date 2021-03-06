<properties
	pageTitle="Azure AD and Applications: Assigning Groups to an Application | Windows Azure"
	description="How to implement group assignment for Azure applications."
	services="active-directory"
	documentationCenter=""
	authors="IHenkel"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="10/09/2015"
	wacn.date=""/>

# Azure AD and Applications: Assigning Groups to an Application
Before you can assign users and groups to an application, you must require user assignment.  To learn how to require user assignment please see the [Requiring User Assignment](/documentation/articles/active-directory-applications-guiding-developers-requiring-user-assignment) article.

This article assumes that you have already created groups in the active directory you are using for this application. The steps are included in the video below.

## Assigning Groups to an Application
1. Log in to the Azure Management Portal with an administrator account.
2. Click on the **All Items** item in the main menu.
3. Choose the directory you are using for the application.
4. Click on the **APPLICATIONS** tab.
5. Select the application from the list of applications associated with this directory.
6. Click the **USERS AND GROUPS** tab.
7. Filter the list of groups in your active directory by using the **Groups** dropdown list.
8. Select the group.
9. Click **ASSIGN**.
10. Click **yes** when prompted.

## Next Steps
[AZURE.INCLUDE [active-directory-applications-guiding-developers-for-lob-applications-toc.md](../includes/active-directory-applications-guiding-developers-for-lob-applications-toc.md)]
