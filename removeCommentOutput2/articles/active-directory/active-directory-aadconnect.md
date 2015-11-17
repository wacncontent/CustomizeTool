<properties
	pageTitle="Integrating your on-premises identities with Azure Active Directory. | Windows Azure"
	description="This is the Azure AD Connect that describes what it is and why you would use it."
	services="active-directory"
	documentationCenter=""
	authors="andkjell"
	manager="stevenpo"
	editor="curtand"/>

<tags
	ms.service="active-directory"
	ms.date="10/13/2015"
	wacn.date=""/>

# Integrating your on-premises identities with Azure Active Directory
Azure AD Connect is the tool to integrate your on-premises identity system such as Windows Server Active Directory with Azure Active Directory and connect your users to Office 365, Azure and 1000’s of SaaS applications. This topic provides a comprehensive guide to prepare and deploy the necessary components for your end users to access cloud services with the same identity that they use today to access existing company apps.

![What is Azure AD Connect](./media/active-directory-aadconnect/arch.png)

## Why use Azure AD Connect
Integrating your on-premises directories with Azure AD makes your users more productive by providing a common identity for accessing both cloud and on-premises resources.  With this integration users and organizations can take advantage of the following:

- Users can use a single identity to access on-premises applications and cloud services such as Office 365.

- Single tool to provide an easy deployment experience for synchronization and sign-in.

- Provides the newest capabilities for your scenarios. Azure AD Connect replaces older versions of identity integration tools such as DirSync and Azure AD Sync. For more information, see [Directory integration tools comparison](/documentation/articles/active-directory-aadconnect-get-started-tools-comparison).


### How Azure AD Connect works

Azure Active Directory Connect is made up of three primary parts.  They are the synchronization services, the optional Active Directory Federation Services piece, and the monitoring piece which is done using [Azure AD Connect Health](/documentation/articles/active-directory-aadconnect-health).

<center>![Azure AD Connect Stack](./media/active-directory-aadconnect-how-it-works/AADConnectStack2.png)
</center>

- Synchronization - This part is made up of the components and functionality previously released as [Dirsync and Azure AD Sync](/documentation/articles/active-directory-aadconnect-get-started-tools-comparison).  This is the part that is responsible for creating users and groups.  It is also responsible for making sure that the information on users and groups in your on-premises environment, matches the cloud.
- AD FS - This is an optional part of Azure AD Connect and can be used to setup a hybrid environment using an on-premises AD FS infrastructure.  This part can be used by organizations to address complex deployments that include such things as domain join SSO, enforcement of AD login policy and smart card or 3rd party MFA.
- Health Monitoring - Azure AD Connect Health can provide robust monitoring of your AD FS servers and provide a central location in the Azure Management Portal to view this activity.  For additional information see [Azure Active Directory Connect Health](/documentation/articles/active-directory-aadconnect-health).

## Install Azure AD Connect

You can find the download for Azure AD Connect on [Microsoft Download Center](http://go.microsoft.com/fwlink/?LinkId=615771).


| Solution | Scenario |
| ----- | ----- |
| [Express settings](/documentation/articles/active-directory-aadconnect-get-started-express) | <li>Recommended and default option if you have a single forest AD.</li> <li>User sign in with the same password using password synchronization.</li>
| [Customized settings](/documentation/articles/active-directory-aadconnect-get-started-custom) | <li>Used when you have multiple forests. Supports many on-premises [topologies](/documentation/articles/active-directory-aadconnect-topologies).</li> <li>Customize your sign-in option , such as ADFS for federation or use a 3rd party identity provider.</li> <li>Customize synchronization features, such as filtering and writeback.</li>
| [Upgrade from DirSync](/documentation/articles/active-directory-aadconnect-dirsync-upgrade-get-started) | <li>If you have an existing DirSync server already running.</li>
| Upgrade from Azure AD Sync | <li>This is a seamless in-place upgrade.</li>


[After installation](/documentation/articles/active-directory-aadconnect-whats-next) you should verify it is working as expected and assign licenses to the users.

### Next steps to Install Azure AD Connect

| Topic |  |
| --------- | --------- |
| Hardware and prerequisites | [Azure AD Connect: Hardware and prerequisites](/documentation/articles/active-directory-aadconnect-prerequisites) |
| Download Azure AD Connect | [Download Azure AD Connect](http://go.microsoft.com/fwlink/?LinkId=615771) |
| Install using Express settings | [Express installation of Azure AD Connect](/documentation/articles/active-directory-aadconnect-get-started-express) |
| Install using Customized settings | [Custom installation of Azure AD Connect](/documentation/articles/active-directory-aadconnect-get-started-custom) |
| Upgrade from DirSync | [Upgrade from Azure AD sync tool (DirSync)](/documentation/articles/active-directory-aadconnect-dirsync-upgrade-get-started) |
| After installation | [Verify the installation and assign licenses ](/documentation/articles/active-directory-aadconnect-whats-next) |

### Learn more about Install Azure AD Connect

You also want to prepare for [operational](/documentation/articles/active-directory-aadconnectsync-operations) concerns. You might want to have a stand-by server so you easily can fall over in case of a [disaster](/documentation/articles/active-directory-aadconnectsync-operations#disaster-recovery). If you plan to make frequent configuration changes you should plan for a [staging mode](/documentation/articles/active-directory-aadconnectsync-operations#staging-mode) server.

| Topic |  |
| --------- | --------- |
| Supported topologies | [Topologies for Azure AD Connect](/documentation/articles/active-directory-aadconnect-topologies) |
| Design concepts | [Azure AD Connect design concepts](/documentation/articles/active-directory-aadconnect-design-concepts) |
| Accounts used for installation | [More about Azure AD Connect credentials and permissions](/documentation/articles/active-directory-aadconnect-accounts-permissions) |
| Operational planning | [Azure AD Connect sync: Operational tasks and considerations](/documentation/articles/active-directory-aadconnectsync-operations) |

## Configure features
Azure AD Connect comes with several features you can optionally turn on or are enabled by default. Some features might in some cases require additional configuration in certain scenarios and topologies.

[Filtering](/documentation/articles/active-directory-aadconnectsync-configure-filtering) is used when you want to limit which objects are synchronized to Azure AD. By default all users, contacts, groups, and Windows 10 computers are synchronized, but you can limit this based on domains, OUs, or attributes.

[Password synchronization](/documentation/articles/active-directory-aadconnectsync-implement-password-synchronization) will synchronize the password hash in Active Directory to Azure AD. This allows the user to use the same password on-premises and in the cloud but only manage it in one location. Since it will use your on-premises Active Directory it will also allow you to use your own password policy.

[Password writeback](/documentation/articles/active-directory-passwords-getting-started) will allow your users to change and reset their passwords in the cloud and have your on-premises password policy applied.

[Device writeback](/documentation/articles/active-directory-aadconnect-get-started-custom-device-writeback) will allow a device registered in Azure AD to be written back to on-premises Active Directory so it can be used for conditional access.

The [prevent accidental deletes](/documentation/articles/active-directory-aadconnectsync-feature-prevent-accidental-deletes) feature is turned on by default and will protect your cloud directory from a lot of deletes at the same time. By default it will allow 500 deletes per run and this can be changed depending on your organization’s size.

### Next steps to configure features

| Topic |  |
| --------- | --------- |
| Configure filtering | [Azure AD Connect sync: Configure filtering](/documentation/articles/active-directory-aadconnectsync-configure-filtering) |
| Password synchronization | [Azure AD Connect sync: Implement password synchronization](/documentation/articles/active-directory-aadconnectsync-implement-password-synchronization) |
| Password writeback | [Getting started with password management](/documentation/articles/active-directory-passwords-getting-started) |
| Device writeback | [Enabling device writeback in Azure AD Connect](/documentation/articles/active-directory-aadconnect-get-started-custom-device-writeback) |
| Prevent accidental deletes | [Azure AD Connect sync: Prevent accidental deletes](/documentation/articles/active-directory-aadconnectsync-feature-prevent-accidental-deletes) |

## Customize Azure AD Connect sync
Azure AD Connect sync comes with a default configuration which is intended to work for most customers and topologies. But there are always situations where the default configuration will not work and must be adjusted. It is supported to make changes as documented in this section and linked topics.

If you have not worked with a synchronization topology before you want to start to understand the basics and the terms used as described in the [technical concepts](/documentation/articles/active-directory-aadconnect-technical-concepts). Azure AD Connect is the evolution of MIIS2003, ILM2007, and FIM2010. Even if some things are identical, a lot has changed as well.

The configuration assumes there might be more than one forest in the configuration. In those topologies a user object might be represented as a contact in another forest. The user might also have a linked mailbox in another resource forest. The behavior of the default configuration is described in [users and contacts](/documentation/articles/active-directory-aadconnectsync-understanding-users-and-contacts).

The configuration model in sync is called [declarative provisioning](/documentation/articles/active-directory-aadconnectsync-understanding-declarative-provisioning-expressions). The advanced attribute flows are using [functions](/documentation/articles/active-directory-aadconnectsync-functions-reference) to express attribute transformations. You can see and examine the entire configuration using tools which comes with Azure AD Connect. If you need to make changes to the configuration, make sure you follow the [best practices](/documentation/articles/active-directory-aadconnectsync-best-practices-changing-default-configuration) so it will be easier to adopt new releases as these are made available.

### Next steps to customize Azure AD Connect sync

| Topic |  |
| --------- | --------- |
| Technical concepts | [Azure AD Connect sync: Technical Concepts](/documentation/articles/active-directory-aadconnect-technical-concepts) |
| Understanding users and contacts | [Azure AD Connect sync: Understanding Users and Contacts](/documentation/articles/active-directory-aadconnectsync-understanding-users-and-contacts) |
| Declarative provisioning | [Azure AD Connect Sync: Understanding Declarative Provisioning Expressions](/documentation/articles/active-directory-aadconnectsync-understanding-declarative-provisioning-expressions) |
| Declarative provisioning functions reference | [Azure AD Connect sync: Functions Reference](/documentation/articles/active-directory-aadconnectsync-functions-reference) |
| Best practices | [Best practices for changing the default configuration](/documentation/articles/active-directory-aadconnectsync-best-practices-changing-default-configuration) |

## More information and references

| Topic |  |
| --------- | --------- |
| Version history | [Version history](/documentation/articles/active-directory-aadconnect-version-history) |
| Compare DirSync, Azure ADSync, and Azure AD Connect | [Directory integration tools comparison](/documentation/articles/active-directory-aadconnect-get-started-tools-comparison) |
| Attributes synchronized | [Attributes synchronized](/documentation/articles/active-directory-aadconnectsync-attributes-synchronized) |
| Monitoring using Azure AD Connect Health | [Azure AD Connect Health](/documentation/articles/active-directory-aadconnect-health) |
| Frequently Asked Questions | [Azure AD Connect FAQ](/documentation/articles/active-directory-aadconnect-faq) |


**Additional Resources**


Ignite 2015 presentation on extending your on-premises directories to the cloud.



[Multi-forest Directory Sync with Single Sign-On Scenario](https://msdn.microsoft.com/zh-cn/library/azure/dn510976.aspx) - Integrate multiple directories with Azure AD.

[Azure AD Connect Health](/documentation/articles/active-directory-aadconnect-health) - Monitor the health of your on-premises AD FS infrastructure.

[Azure AD Connect FAQ](/documentation/articles/active-directory-aadconnect-faq) - Frequently asked questions around Azure AD Connect.






 




