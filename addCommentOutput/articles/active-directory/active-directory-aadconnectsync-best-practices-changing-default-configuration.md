<properties
	pageTitle="Azure AD Connect sync: Best practices for changing the default configuration | Windows Azure"
	description="Provides best practices for changing the default configuration of Azure AD Connect sync."
	services="active-directory"
	documentationCenter=""
	authors="andkjell"
	manager="stevenpo"
	editor=""/>

<tags
	ms.service="active-directory"
	ms.date="11/11/2015"
	wacn.date=""/>


# Azure AD Connect <!-- deleted by customization sync --><!-- keep by customization: begin --> Sync <!-- keep by customization: end -->: Best practices for changing the default configuration

The purpose of this topic is to describe supported and unsupported changes to Azure AD Connect sync.

The configuration created by Azure AD Connect works <!-- deleted by customization âas isâ --><!-- keep by customization: begin --> “as is” <!-- keep by customization: end --> for the majority of environments that synchronize on-premises Active Directory with Azure AD. However, in some cases, it is necessary to apply some changes to a configuration to satisfy a particular need or requirement.

## Changes to the service account
Azure AD Connect sync is running under a service account created by the installation wizard. This service account holds the encryption keys to the database used by sync. It is created with a 127 characters long password and the password is set to not expire.

- It is **unsupported** to change or reset the password of the service account. Doing so will destroy the encryption keys and the service will not be able to access the database and <!-- deleted by customization will not --> be able to start.

## Changes to the scheduler
Azure AD Connect sync is set to synchronize identity data every 3 hours. During installation a scheduled task is created running under a service account with permissions to operate the sync server.

- It is **unsupported** to make changes to the scheduled task. The password for the service account is not known. See [changes to the service account](#changes-to-the-service-account)
- It is **unsupported** to synchronize more frequently than the default 3 hours.

## Changes to Synchronization Rules

<!-- deleted by customization
The installation wizard provides a configuration which is supposed to work for the most common scenarios. In case you need to make changes to the configuration, then you must follow these rules to still have a supported configuration.

- The only supported change to an out-of-box sync rule is to disable it. Any other change might be lost in an upgrade.
- If you need to make any other change to an out-of-box rule, then make a copy of it and disable the original rule. The Sync Rule Editor will prompt you and help you with this.
-->
<!-- keep by customization: begin -->
While it is supported to apply changes to your Azure AD Connect sync configuration, you should apply them with care because Azure AD Connect sync is supposed to be as close as possible an appliance.

The following is a list of expected behaviors:

- After upgrading Azure AD Connect to a newer version, most settings will be reset back to default.
- Changes to “out-of-box” synchronization rules are lost after an upgrade has been applied.
- Deleted “out-of-box” synchronization rules are recreated during an upgrade to a newer version.
- Custom synchronization rules you have created remain unmodified when an upgrade to a newer version has been applied.



When you need to change the default configuration, do the following:

- When you need to modify an attribute flow of an “out-of-box” synchronization rule, do not change it. Instead, create a new synchronization rule with a higher precedence (lower numeric value) that contains your required attribute flow.
<!-- keep by customization: end -->
- Export your custom synchronization rules using the Synchronization Rules Editor. This provides you with a PowerShell script you can use to easily recreate them in the case of a disaster recovery scenario.
<!-- deleted by customization

>[AZURE.WARNING] The out-of-box sync rules have a thumbprint. If you make a change to these rules, the thumbprint will no longer match and you might have problems in the future when you try to apply a new release of Azure AD Connect. Only make changes the way it is described in this article.

### Delete an unwanted Sync Rule
Do not delete an out-of-box sync rule; it will be recreated during next upgrade.

In some cases the installation wizard has produced a configuration which will not work for your topology. For example if you have an account-resource forest topology but you have extended the schema in the account forest with the Exchange schema then rules for Exchange will be created for the account forest as well as the resource forest. In this case we need to disable the Sync Rule for Exchange.

![Disabled sync rule](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/exchangedisabledrule.png)

In the picture above the installation wizard has found an old Exchange 2003 schema in the account forest. This was added before the resource forest was introduced in Fabrikam's environment. To ensure no attributes from the old Exchange implementation are synchronized the sync rule should be disabled as shown.

### Change out-of-box rules
If you need to make changes to an out-of-box rule then you should make a copy of the out-of-box rule and disable the original rule. Then make the changes to the cloned rule. The Sync Rule Editor will help you with this. When you open an out-of-box rule you will be presented with this dialog box:

![Warning out of box rule](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/warningoutofboxrule.png)

Select **Yes** to create a copy of the rule. The cloned rule is then opened.

![Cloned rule](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/clonedrule.png)

On this cloned rule, make any necessary changes to scope, join, and transformations.

### Do not flow an attribute
There are two ways to not flow an attribute. The first is available in the installation wizard and allows you to [remove selected attributes](/documentation/articles/active-directory-aadconnect-get-started-custom#azure-ad-app-and-attribute-filtering). This option works if you have never synchronized the attribute before. However if you have started to synchronize this attribute and later remove it with this feature, then the sync engine will stop managing the attribute and the existing values will be left in Azure AD.

If you want to remove the value of an attribute and make sure it will not flow in the future, you will need create a custom rule instead.

At Fabrikam we have realized that some of the attributes we synchronize to the cloud should not be there. We want to make sure these attributes are removed from Azure AD.

![Extension Attributes](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/badextensionattribute.png)

- Create a new inbound Synchronization Rule and populate the description
![Descriptions](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/syncruledescription.png)
- Create attribute flows of type **Expression** and with the source **AuthoritativeNull**. The literal **AuthoritativeNull** indicates that the value should be empty in the MV even if a lower precedence sync rule tries to populate the value.
![Extension Attributes](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/syncruletransformations.png)
- Save the Sync Rule. Start **Synchronization Service**, find the Connector, select **Run**, and **Full Synchronization**. This will recalculate all attribute flows.
- Verify that the intended changes are about to be exported by searching the connector space.
![Staged delete](./media/active-directory-aadconnectsync-best-practices-changing-default-configuration/deletetobeexported.png)

## Next steps
Learn more about the [Azure AD Connect sync](/documentation/articles/active-directory-aadconnectsync-whatis) configuration.

Learn more about [Integrating your on-premises identities with Azure Active Directory](/documentation/articles/active-directory-aadconnect).
-->
<!-- keep by customization: begin -->
- If you need to change the scope or the join setting in an “out-of-box” synchronization rule, document this and reapply the change after upgrading to a newer version of Azure AD Sync.



**Other important notes:**

- If you have attribute based filtering and password synchronization configured, make sure that only objects that are synchronized to Azure AD are in the scope of password synchronization. 





## Additional Resources

* [Azure AD Connect Sync: Customizing Synchronization options](/documentation/articles/active-directory-aadconnectsync-whatis)
* [Integrating your on-premises identities with Azure Active Directory](/documentation/articles/active-directory-aadconnect)
 
<!--Image references-->
<!-- keep by customization: end -->
