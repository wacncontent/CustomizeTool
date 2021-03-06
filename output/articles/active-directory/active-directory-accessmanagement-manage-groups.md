<properties

	pageTitle="Managing security groups in Azure Active Directory | Windows Azure"
	description="How to create and manage security groups to manage Azure resource access using Azure Active Directory."
	services="active-directory"
	documentationCenter=""
	authors="curtand"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="11/17/2015"
	wacn.date=""/>


#Managing security groups in Azure Active Directory

Within Azure Active Directory (Azure AD), one of the major features is the ability to manage access to resources. These resources can be part of the directory, as in the case of permissions to manage objects through roles in the directory, or resources that are external to the directory, such as SaaS applications, Azure services, and SharePoint sites or on premise resources. A group can be assigned to a resource by the resource owner, and by doing so, granting the members of that group access to the resource. Membership of the group can then be managed by the owner of the group. Effectively, the resource owner delegates the permission to assign users to their resource to the owner of the group.


##How do I create and manage a security group

**To create a group in the Azure Management Portal**

1. In the Azure Management Portal, click **Active Directory**, and then click the name of your organization's directory.
2. Click the **Groups** tab.
3. On the Groups page, click **Add Group**.
4. In the **Add Group** window, specify the name and the description of a group.
5. This task can be completed using either the Office 365 account portal, the Windows Intune account portal or the Azure Management Portal, depending on which services your organization has subscribed to. For more information about using portals to manage your Azure Active Directory, see [Administering your Azure AD directory](/documentation/articles/active-directory-administer).

## How do I assign or remove users in a security group

**To add a member to a group in the Azure Management Portal**

1. In the Azure Management Portal, click **Active Directory**, and then click the name of your organization's directory.
2. Click the **Groups** tab.
3. On the **Groups** page, click on the name of the group that you want to add members to. By default, this displays the **Members** tab of the selected group.
4. On that group's page, click **Add Members**.
5. On the **Add Members** page, click on the name of the user or a group that you want to add as a member of this group and make sure this name is added to the Selected pane.


**To remove a member from a group in the Azure Management Portal**

1. In the Azure Management Portal, click **Active Directory**, and then click on the name of your organization's directory.
2. Click the **Groups** tab.
3. On the Groups page, click on the name of the group that you want to remove members from.
4. On that group's page, click the **Members** tab.
5. On that group's page, click on the name of the member that you want to remove from this group and then click **Remove**.
6. Verify that you want to remove this member from the group by clicking **Yes** as the answer to the action confirmation question.


## How do I use a rule to dynamically manage members of a security group

**To enable dynamic membership for a particular group, perform the following steps:**

1. In the Azure Management Portal, under the **Groups** tab, select the group you want to edit, and then in this group's **Configure** tab, set the **Enable Dynamic Memberships** switch to **Yes**.
2. You can now set up a simple single rule for the group that will control how dynamic membership for this group functions. Make sure the **Add users where** radio button is checked and then select a user property from the pull-down menu (for example, department, jobTitle, etc.),
3. Next, select a condition (Not Equals, Equals, Not Starts With, Starts With, Not Contains, Contains, Not Match, Match), and finally specify a value for the selected user property.

For example, if a group is assigned to a SaaS application (for more information see Assign access for a group to a SaaS application in Azure AD) and you enable dynamic memberships for this group by setting a rule whereby Add users where is set to the jobTitle that Equals(-eq)Sales Rep, all users within your Azure AD directory whose job titles are set to Sales Rep, will have access to this SaaS application.

## Additional information

These articles provide additional information on Azure Active Directory.

* [Managing access to resources with Azure Active Directory groups](/documentation/articles/active-directory-manage-groups)

* [What is Azure Active Directory?](/documentation/articles/active-directory-whatis)

* [Integrating your on-premises identities with Azure Active Directory](/documentation/articles/active-directory-aadconnect)
