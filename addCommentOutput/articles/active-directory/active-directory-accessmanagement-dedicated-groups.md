<properties
	pageTitle="Dedicated groups in Azure Active Directory | Windows Azure"
	description="Overview of how dedicated groups work in Azure Active Directory and how they are created."
	services="active-directory"
	documentationCenter=""
	authors="curtand"
	manager="stevenpo"
	editor=""
	/>

<tags
	ms.service="active-directory"
	ms.date="11/17/2015"
	wacn.date=""/>

# Dedicated groups in Azure Active Directory

In Azure Active Directory, dedicated groups are created automatically and group membership for the dedicated groups is also automatic. You cannot add or remove members to and from dedicated groups through the Azure Management <!-- deleted by customization Portal --><!-- keep by customization: begin --> portal <!-- keep by customization: end -->, Windows PowerShell cmdlets, or programmatically. To enable dedicated groups, In the Azure Management Portal, on the Configure tab, set the <!-- deleted by customization **Enable --><!-- keep by customization: begin --> Enable <!-- keep by customization: end --> Dedicated Groups switch to <!-- deleted by customization Yes** --><!-- keep by customization: begin --> Yes <!-- keep by customization: end -->.

<!-- deleted by customization
Once the Enable Dedicated Groups switch is set to **Yes**, you can further enable the directory to automatically create the All Users dedicated group by setting the **Enable “All Users” Group** switch to **Yes**. You can then also edit the name of this dedicated group by typing it in the **Display Name for “All Users” Group** field.
-->
<!-- keep by customization: begin -->
In the current public preview release, once the Enable Dedicated Groups switch is set to Yes, you can further enable the directory to automatically create the All Users dedicated group by setting the Enable “All Users” Group switch to Yes. You can then also edit the name of this dedicated group by typing it in the Display Name for “All Users” Group field.
<!-- keep by customization: end -->

The All Users dedicated group can be useful if you want to assign the same permissions to all the users in your directory. For example, you can grant all users in your directory access to a SaaS application by assigning access for the All Users dedicated group to this application.

<!-- deleted by customization
These articles provide additional information on Azure Active Directory.
-->
<!-- keep by customization: begin -->
Here are some topics that will provide some additional information on Azure Active Directory 
<!-- keep by customization: end -->

* [Managing access to resources with Azure Active Directory groups](/documentation/articles/active-directory-manage-groups)
* [What is Azure Active Directory?](/documentation/articles/active-directory-whatis)
* [Integrating your on-premises identities with Azure Active Directory](/documentation/articles/active-directory-aadconnect)
