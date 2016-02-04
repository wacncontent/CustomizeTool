
<properties
	pageTitle="Troubleshooting dynamic membership for groups| Windows Azure"
	description="A topic that lists troubleshooting tips for dynamic membership for groups in Azure AD."
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


# Troubleshooting dynamic memberships to groups

| Symptom                                                                        | Action                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I configured a rule on a group but no memberships get updated in the group     | Verify <!-- deleted by customization that --> the <!-- deleted by customization **Enable --><!-- keep by customization: begin --> Enable <!-- keep by customization: end --> delegated group <!-- deleted by customization management** --><!-- keep by customization: begin --> management <!-- keep by customization: end --> setting is set to Yes in the Directory Configure tab. <!-- deleted by customization You --><!-- keep by customization: begin --> Note that you <!-- keep by customization: end --> will <!-- keep by customization: begin --> only <!-- keep by customization: end --> see this setting <!-- deleted by customization only --> if you are signed in <!-- deleted by customization as a user to whom --><!-- keep by customization: begin --> with an account that has <!-- keep by customization: end --> an Azure Active Directory Premium license <!-- deleted by customization is --> assigned <!-- keep by customization: begin --> to it <!-- keep by customization: end -->.  Verify the values for user attributes on the rule <!-- deleted by customization: --><!-- keep by customization: begin --> - <!-- keep by customization: end --> are there users that satisfy the rule?                                                                               |
<!-- deleted by customization
| I configured a rule, but now the existing members of the rule are removed      | This is expected behavior. Existing members of the group are removed when a rule is enabled or changed. The users returned from evaluation of the rule are added as members to the group.                                                                                                                                                                                                                                      |
| I donât see membership changes instantly when I add or change a rule, why not? | Dedicated membership evaluation is done periodically in an asynchronous background process. How long the process takes is determined by the number of users in your directory and the size of the group created as a result of the rule. Typically, directories with small numbers of users will see the group membership changes in less than a few minutes. Directories with a large number of users can take 30 minutes or longer to populate. |

These articles provide additional information on Azure Active Directory.
-->
<!-- keep by customization: begin -->
| I configured a rule, but now the existing members of the rule are removed      | This is expected - existing members of the group are removed when a rule is enabled or changed. The resulting set of users from evaluation of the rule is added as members to the group.                                                                                                                                                                                                                                      |
| I don't see membership changes instantly when I add or change a rule, why not? | Dedicated membership evaluation is done periodically in an asynchronous background process. The number of users in your tenant, and the size of the group created as a result of the rule play a factor in how long it takes. Typically tenants with small numbers of users will see the group membership changes in less than a few minutes. Tenants with a large number of users can take 30 minutes or longer to populate. |

Here are some topics that will provide some additional information on Azure Active Directory 
<!-- keep by customization: end -->

* [Managing access to resources with Azure Active Directory groups](/documentation/articles/active-directory-manage-groups)
* [What is Azure Active Directory?](/documentation/articles/active-directory-whatis)
* [Integrating your on-premises identities with Azure Active Directory](/documentation/articles/active-directory-aadconnect)
