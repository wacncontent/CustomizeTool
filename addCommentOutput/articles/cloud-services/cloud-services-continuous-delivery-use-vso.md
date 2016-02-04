<properties
	pageTitle="Continuous delivery with Visual Studio Team Services in Azure | Windows Azure"
	description="Learn how to configure your Visual Studio Team Services team projects to automatically build and deploy to the web site feature in Azure Websites or cloud services."
	services="cloud-services"
	documentationCenter=".net"
	authors="TomArcher"
	manager="douge"
	editor=""/>

<tags
	ms.service="cloud-services"
	ms.date="12/18/2015"
	wacn.date=""/>

<!-- deleted by customization
# Continuous delivery to Azure using Visual Studio Team Services

You can configure your Visual Studio Team Services team projects to automatically build and deploy to Azure web sites or cloud services.  (For information on how to set up a continuous build and deploy system using an *on-premises* Team Foundation Server, see [Continuous Delivery for Cloud Services in Azure](/documentation/articles/cloud-services-dotnet-continuous-delivery).)
-->
<!-- keep by customization: begin -->

# Continuous delivery to Azure using Visual Studio Online

You can configure your Visual Studio Online team projects to automatically build and deploy to Azure website or cloud services.  (For information on how to set up a continuous build and deploy system using an *on-premises* Team Foundation Server, see [Continuous Delivery for Cloud Services in Azure](/documentation/articles/cloud-services-dotnet-continuous-delivery).)
<!-- keep by customization: end -->

This tutorial assumes you have Visual Studio 2013 and the Azure SDK installed. If you don't already have Visual Studio 2013, download it by choosing the **Get started for free** link at [www.visualstudio.com](http://www.visualstudio.com). Install the Azure SDK from [here](/downloads/).

> [AZURE.NOTE] You need an Visual Studio <!-- deleted by customization Team Services --><!-- keep by customization: begin --> online <!-- keep by customization: end --> account to complete this tutorial:
> You can [open a Visual Studio <!-- deleted by customization Team Services --><!-- keep by customization: begin --> Online <!-- keep by customization: end --> account for free](https://www.visualstudio.com/get-started/setup/sign-up-for-visual-studio-online).

To set up a cloud service to automatically build and deploy to Azure by using Visual Studio <!-- deleted by customization Team Services --><!-- keep by customization: begin --> Online <!-- keep by customization: end -->, follow these steps <!-- deleted by customization. --><!-- keep by customization: begin -->: <!-- keep by customization: end -->

## Step 1: Create a team project

Follow the instructions [here](https://www.visualstudio.com/get-started/setup/connect-to-visual-studio-online) to create your team project and link it to Visual Studio. This walkthrough assumes you are using Team Foundation Version Control (TFVC) as your source control solution. If you want to use Git for version control, see [the Git version of this walkthrough](/documentation/articles/cloud-services-continuous-delivery-use-vso-git/).

## <!-- deleted by customization Step --><!-- keep by customization: begin --> <a name="step2"> </a>Step <!-- keep by customization: end --> 2: Check in a project to source control

1. In Visual Studio, open the solution you want to deploy, or create a new one.
You can deploy a <!-- deleted by customization web site --><!-- keep by customization: begin -->  Website <!-- keep by customization: end --> or a cloud service (Azure Application) by following the steps in this walkthrough.
If you want to create a new solution, create a new Azure Cloud Service project,
or a new ASP.NET MVC project. Make sure that the project targets .NET Framework 4 or 4.5, and if you are creating a cloud service project, add an ASP.NET MVC web role and a worker role, and choose Internet application for the web role. When prompted, choose **Internet Application**.
<!-- deleted by customization
If you want to create a web site, choose the ASP.NET web site project template, and then choose MVC. See [Create an ASP.NET web site in Azure Websites](/documentation/articles/web-sites-dotnet-get-started).

	> [AZURE.NOTE] Visual Studio Team Services only support CI deployments of Visual Studio web sites at this time. Web Site projects are out of scope.

1. Open the context menu for the solution, and choose **Add Solution to Source Control**.

	![][5]

1. Accept or change the defaults and choose the **OK** button. Once the process completes, source control icons appear in **Solution Explorer**.

	![][6]

1. Open the shortcut menu for the solution, and choose **Check In**.

	![][7]

1. In the **Pending Changes** area of **Team Explorer**, type a comment for the check-in and choose the **Check In** button.

	![][8]
-->
<!-- keep by customization: begin -->
If you want to create a  Website, choose the ASP.NET Web Site project template, and then choose MVC. See [Get started with Azure and ASP.NET](/documentation/articles/web-sites-dotnet-get-started).

	> [AZURE.NOTE] Visual Studio Online only support CI deployments of Visual Studio Web Sites at this time. Web Site projects are out of scope.

2. Open the context menu for the solution, and choose **Add Solution to Source Control**.

	![][5]

3. Accept or change the defaults and choose the **OK** button. Once the process completes, source control icons appear in **Solution Explorer**.

	![][6]

4. Open the shortcut menu for the solution, and choose **Check In**.

	![][7]

5. In the **Pending Changes** area of **Team Explorer**, type a comment for the check-in and choose the **Check In** button.

	![][8]
<!-- keep by customization: end -->

	Note the options to include or exclude specific changes when you check in. If desired changes are excluded, choose the **Include All** link.

	![][9]

## Step 3: Connect the project to Azure

<!-- deleted by customization
1. Now that you have a VSTS team project with some source code in it, you are ready to connect your team project to Azure.  In the [Azure Management Portal](http://manage.windowsazure.cn), select your cloud service or web site, or create a new one by choosing the **+** icon at the bottom left and choosing **Cloud Service** or **Web Apps** and then **Quick Create**. Choose the **Set up publishing with Visual Studio Team Services** link.

	![][10]

1. In the wizard, type the name of your Visual Studio Team Services account in the textbox and click the **Authorize Now** link. You might be asked to sign in.<!-- keep by customization: begin --> in.<br/> <!-- keep by customization: end -->

	![][11]

1. In the **Connection Request** pop-up dialog, choose the **Accept** button to authorize Azure to configure your team project in VSTS.

	![][12]

1. When authorization succeeds, you see a dropdown containing a list of your Visual Studio Team Services team projects. Choose  the name of team project that you created in the previous steps, and then choose the wizard's checkmark button.

	![][13]

1. After your project is linked, you will see some instructions for checking in changes to your Visual Studio Team Services team project.  On your next check-in, Visual Studio Team Services will build and deploy your project to Azure.  Try this now by clicking the **Check In from Visual Studio** link, and then the **Launch Visual Studio** link (or the equivalent **Visual Studio** button at the bottom of the portal screen).

	![][14]
-->
<!-- keep by customization: begin -->
1. Now that you have a VSO team project with some source code in it, you are ready to connect your team project to Azure.  In the [Azure Management Portal](http://manage.windowsazure.cn), select your cloud service or  Website, or create a new one by selecting the + icon at the bottom left and choosing **Cloud Service** or ** Website** and then **Quick Create**. Choose the **Set up publishing with Visual Studio Online** link.<br/>
![][10]

2. In the wizard, type the name of your Visual Studio Online account in the textbox and click the **Authorize Now** link. You might be asked to sign <!-- keep by customization: begin --> in.<br/> <!-- keep by customization: end -->
![][11]

3. In the **Connection Request** pop-up dialog, choose the **Accept** button to authorize Azure to configure your team project in VSO.
![][12]

4. When authorization succeeds, you see a dropdown containing a list of your Visual Studio Online team projects. Choose  the name of team project that you created in the previous steps, and then choose the wizard's checkmark button.

	![][13]

5. After your project is linked, you will see some instructions for checking in changes to your Visual Studio Online team project.  On your next check-in, Visual Studio Online will build and deploy your project to Azure.  Try this now by clicking the **Check In from Visual Studio** link, and then the **Launch Visual Studio** link (or the equivalent **Visual Studio** button at the bottom of the portal screen).

	![][14]
<!-- keep by customization: end -->

## Step 4: Trigger a rebuild and redeploy your project

1. In Visual Studio's **Team Explorer**, choose the **Source Control Explorer** link.

	![][15]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 2 <!-- keep by customization: end -->. Navigate to your solution file and open it.

	![][16]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 3 <!-- keep by customization: end -->. In **Solution Explorer**, open up a file and change it. For example, change the file `_Layout.cshtml` under the Views\\Shared folder in an MVC web role.

	![][17]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 4 <!-- keep by customization: end -->. Edit the logo for the site and choose **Ctrl+S** to save the file.

	![][18]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 5 <!-- keep by customization: end -->. In **Team Explorer**, choose the **Pending Changes** link.
<!-- deleted by customization

	![][19]

1. Enter a comment and then choose the **Check In** button.

	![][20]

1. Choose the **Home** button to return to the **Team Explorer** home page.

	![][21]

1. Choose the **Builds** link to view the builds in progress.

	![][22]
-->
<!-- keep by customization: begin -->
![][19]

6. Enter a comment and then choose the **Check In** button.

	![][20]

7. Choose the **Home** button to return to the **Team Explorer** home page.

	![][21]

8. Choose the **Builds** link to view the builds in progress.

	![][22]
<!-- keep by customization: end -->

	**Team Explorer** shows that a build has been triggered for your check-in.

	![][23]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 9 <!-- keep by customization: end -->. Double-click the name of the build in progress to view a detailed log as the build progresses.

	![][24]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 10 <!-- keep by customization: end -->. While the build is in-progress, take a look at the build definition that was created when you linked TFS to Azure by using the wizard.  Open the shortcut menu for the build definition and choose **Edit Build Definition**.

	![][25]

	In the **Trigger** tab, you will see that the build definition is set to build on every check-in by default.

	![][26]

	In the **Process** tab, you can see the deployment environment is set to the name of your cloud service or web site. If you are working with web sites, the properties you see will be different from those shown here.

	![][27]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 11 <!-- keep by customization: end -->. Specify values for the properties if you want different values than the defaults. The properties for Azure publishing are in the **Deployment** section.

	The following table shows the available properties in the **Deployment** section:

	|Property|Default Value|
	|---|---|
	|Allow Untrusted Certificates|If false, SSL certificates must be signed by a root authority.|
	|Allow Upgrade|Allows the deployment to update an existing deployment instead of creating a new one. Preserves the IP address.|
	|Do Not Delete|If true, do not overwrite an existing unrelated deployment (upgrade is allowed).|
	|Path to Deployment Settings|The path to your .pubxml file for a web site, relative to the root folder of the repo. Ignored for cloud services.|
	|Sharepoint Deployment Environment|The same as the service name.|
	|Azure Deployment Environment|The web site or cloud service name.|

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 12 <!-- keep by customization: end -->. If you are using multiple service configurations (.cscfg files), you can specify the desired service configuration in the **Build, Advanced, MSBuild arguments** setting. For example, to use ServiceConfiguration.Test.cscfg, set MSBuild arguments line option `/p:TargetProfile=Test`.
<!-- deleted by customization

	![][38]
-->
<!-- keep by customization: begin -->
![][38]
<!-- keep by customization: end -->

	By this time, your build should be completed successfully.

	![][28]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 13 <!-- keep by customization: end -->. If you double-click the build name, Visual Studio shows a **Build Summary**, including any test results from associated unit test projects.

	![][29]

<!-- deleted by customization
1. In the [Azure Management Portal](http://manage.windowsazure.cn), you can view the associated deployment on the **Deployments** tab when the staging environment is selected.

	![][30]

1.	Browse to your site's URL. For a web site, just click the **Browse** button on the command bar. For a cloud service, choose the URL in the **Quick Glance** section of the **Dashboard** page that shows the Staging environment for a cloud service. Deployments from continuous integration for cloud services are published to the Staging environment by default. You can change this by setting the **Alternate Cloud Service Environment** property to **Production**. This screenshot shows where the site URL is on the cloud service's dashboard page <!-- deleted by customization. --><!-- keep by customization: begin -->: <br/> <!-- keep by customization: end -->

	![][31]
-->
<!-- keep by customization: begin -->
14. In the [Azure Management Portal](http://manage.windowsazure.cn), you can view the associated deployment on the Deployments tab when the staging environment is selected.<br/>
![][30]

15.	Browse to your site's URL. For a  Website, just click the Browse button on the command bar. For a cloud service, choose the URL in the **Quick Glance** section of the **Dashboard** page that shows the Staging environment for a cloud service. Deployments from continuous integration for cloud services are published to the Staging environment by default. You can change this by setting the Alternate Cloud Service Environment property to Production. This screenshot shows where the site URL is on the cloud service's dashboard page <!-- deleted by customization. --><!-- keep by customization: begin -->: <br/> <!-- keep by customization: end -->
![][31]
<!-- keep by customization: end -->

	A new browser tab will open to reveal your running site.

	![][32]

	<!-- deleted by customization For --><!-- keep by customization: begin --> 16.	For <!-- keep by customization: end --> cloud services, if you make other changes to your project, you trigger more builds, and you will accumulate multiple deployments. The latest one marked as <!-- deleted by customization Active. --><!-- keep by customization: begin --> Active.<br/> <!-- keep by customization: end -->
<!-- deleted by customization

	![][33]
-->
<!-- keep by customization: begin -->
![][33]
<!-- keep by customization: end -->

## Step 5: Redeploy an earlier build

This step applies to cloud services and is optional. In the Azure <!-- deleted by customization Management Portal --><!-- keep by customization: begin --> management portal <!-- keep by customization: end -->, choose an earlier deployment and then choose the **Redeploy** button to rewind your site to an earlier check-in.  Note that this will trigger a new build in TFS and create a new entry in your deployment history.
<!-- deleted by customization

![][34]
-->
<!-- keep by customization: begin -->
![][34]
<!-- keep by customization: end -->

## Step 6: Change the Production deployment

This step applies only to cloud services, not <!-- deleted by customization web sites --><!-- keep by customization: begin -->  Websites <!-- keep by customization: end -->. When you are ready, you can promote the Staging environment to the production environment by choosing the <!-- deleted by customization **Swap** --><!-- keep by customization: begin --> Swap <!-- keep by customization: end --> button in the <!-- deleted by customization Azure Management Portal --><!-- keep by customization: begin --> management portal <!-- keep by customization: end -->. The newly deployed Staging environment is promoted to Production, and the previous Production environment, if any, becomes a Staging environment. The Active deployment may be different for the Production and Staging environments, but the deployment history of recent builds is the same regardless of <!-- deleted by customization environment. --><!-- keep by customization: begin --> environment.<br/> <!-- keep by customization: end -->
<!-- deleted by customization

![][35]
-->
<!-- keep by customization: begin -->
![][35]
<!-- keep by customization: end -->

## Step 7: Run unit tests

This step applies only to web sites, not cloud services. To put a quality gate on your deployment, you can run unit tests and if they fail, you can stop the deployment.

1.  In Visual Studio, add a unit test project.

	![][39]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 2 <!-- keep by customization: end -->.  Add project references to the project you want to test.

	![][40]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 3 <!-- keep by customization: end -->.  Add some unit tests. To get started, try a dummy test that will always pass.

		```
		using System;
		using Microsoft.VisualStudio.TestTools.UnitTesting;

		namespace UnitTestProject1
		{
		    [TestClass]
		    public class UnitTest1
		    {
		        [TestMethod]
		        [ExpectedException(typeof(NotImplementedException))]
		        public void TestMethod1()
		        {
		            throw new NotImplementedException();
		        }
		    }
		}
		```

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 4 <!-- keep by customization: end -->.  Edit the build definition, choose the **Process** tab, and expand the **Test** node.

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 5 <!-- keep by customization: end -->.  Set the **Fail build on test failure** to True. This means that the deployment won't occur unless the tests pass.

	![][41]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 6 <!-- keep by customization: end -->.  Queue a new build.

	![][42]

	![][43]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 7 <!-- keep by customization: end -->. While the build is proceeding, check on its progress.

	![][44]

	![][45]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 8 <!-- keep by customization: end -->. When the build is done, check the test results.

	![][46]

	![][47]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 9 <!-- keep by customization: end -->.  Try creating a test that will fail. Add a new test by copying the first one, rename it, and comment out the line of code that states NotImplementedException is an expected exception.

		```
		[TestMethod]
		//[ExpectedException(typeof(NotImplementedException))]
		public void TestMethod2()
		{
		    throw new NotImplementedException();
		}
		```

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 10 <!-- keep by customization: end -->. Check in the change to queue a new build.

	![][48]

<!-- deleted by customization 1 --><!-- keep by customization: begin --> 11 <!-- keep by customization: end -->. View the test results to see details about the failure.

	![][49]

	![][50]

<!-- deleted by customization
## Next steps
For more about unit testing in Visual Studio Team Services, see [Run unit tests in your build](https://msdn.microsoft.com/library/ms253138.aspx). If you're using Git, see [Share your code in Git](http://www.visualstudio.com/get-started/share-your-code-in-git-vs.aspx) and [Continuous deployment using GIT in Azure Websites](/documentation/articles/web-sites-publish-source-control).  For more information about Visual Studio Team Services, see [Visual Studio Team Services](https://www.visualstudio.com/).
-->
<!-- keep by customization: begin -->
For more about unit testing in Visual Studio Online, see [Run unit tests in your build](https://msdn.microsoft.com/library/ms253138.aspx).

For more information, see [Visual Studio Online](https://www.visualstudio.com/). If you're using Git, see [Share your code in Git](http://www.visualstudio.com/get-started/share-your-code-in-git-vs.aspx) and [Continuous deployment using GIT in Azure Websites](/documentation/articles/web-sites-publish-source-control).
<!-- keep by customization: end -->

[0]: ./media/cloud-services-continuous-delivery-use-vso/tfs0.PNG
[1]: ./media/cloud-services-continuous-delivery-use-vso/tfs1.png
[2]: ./media/cloud-services-continuous-delivery-use-vso/tfs2.png

[5]: ./media/cloud-services-continuous-delivery-use-vso/tfs5.png
[6]: ./media/cloud-services-continuous-delivery-use-vso/tfs6.png
[7]: ./media/cloud-services-continuous-delivery-use-vso/tfs7.png
[8]: ./media/cloud-services-continuous-delivery-use-vso/tfs8.png
[9]: ./media/cloud-services-continuous-delivery-use-vso/tfs9.png
[10]: ./media/cloud-services-continuous-delivery-use-vso/tfs10.png
[11]: ./media/cloud-services-continuous-delivery-use-vso/tfs11.png
[12]: ./media/cloud-services-continuous-delivery-use-vso/tfs12.png
[13]: ./media/cloud-services-continuous-delivery-use-vso/tfs13.png
[14]: ./media/cloud-services-continuous-delivery-use-vso/tfs14.png
[15]: ./media/cloud-services-continuous-delivery-use-vso/tfs15.png
[16]: ./media/cloud-services-continuous-delivery-use-vso/tfs16.png
[17]: ./media/cloud-services-continuous-delivery-use-vso/tfs17.png
[18]: ./media/cloud-services-continuous-delivery-use-vso/tfs18.png
[19]: ./media/cloud-services-continuous-delivery-use-vso/tfs19.png
[20]: ./media/cloud-services-continuous-delivery-use-vso/tfs20.png
[21]: ./media/cloud-services-continuous-delivery-use-vso/tfs21.png
[22]: ./media/cloud-services-continuous-delivery-use-vso/tfs22.png
[23]: ./media/cloud-services-continuous-delivery-use-vso/tfs23.png
[24]: ./media/cloud-services-continuous-delivery-use-vso/tfs24.png
[25]: ./media/cloud-services-continuous-delivery-use-vso/tfs25.png
[26]: ./media/cloud-services-continuous-delivery-use-vso/tfs26.png
[27]: ./media/cloud-services-continuous-delivery-use-vso/tfs27.png
[28]: ./media/cloud-services-continuous-delivery-use-vso/tfs28.png
[29]: ./media/cloud-services-continuous-delivery-use-vso/tfs29.png
[30]: ./media/cloud-services-continuous-delivery-use-vso/tfs30.png
[31]: ./media/cloud-services-continuous-delivery-use-vso/tfs31.png
[32]: ./media/cloud-services-continuous-delivery-use-vso/tfs32.png
[33]: ./media/cloud-services-continuous-delivery-use-vso/tfs33.png
[34]: ./media/cloud-services-continuous-delivery-use-vso/tfs34.png
[35]: ./media/cloud-services-continuous-delivery-use-vso/tfs35.png
[36]: ./media/cloud-services-continuous-delivery-use-vso/tfs36.PNG
[37]: ./media/cloud-services-continuous-delivery-use-vso/tfs37.PNG
[38]: ./media/cloud-services-continuous-delivery-use-vso/AdvancedMSBuildSettings.PNG
[39]: ./media/cloud-services-continuous-delivery-use-vso/AddUnitTestProject.PNG
[40]: ./media/cloud-services-continuous-delivery-use-vso/AddProjectReferences.PNG
[41]: ./media/cloud-services-continuous-delivery-use-vso/EditBuildDefinitionForTest.PNG
[42]: ./media/cloud-services-continuous-delivery-use-vso/QueueNewBuild.PNG
[43]: ./media/cloud-services-continuous-delivery-use-vso/QueueBuildDialog.PNG
[44]: ./media/cloud-services-continuous-delivery-use-vso/BuildInTeamExplorer.PNG
[45]: ./media/cloud-services-continuous-delivery-use-vso/BuildRequestInfo.PNG
[46]: ./media/cloud-services-continuous-delivery-use-vso/BuildSucceeded.PNG
[47]: ./media/cloud-services-continuous-delivery-use-vso/TestResultsPassed.PNG
[48]: ./media/cloud-services-continuous-delivery-use-vso/CheckInChangeToMakeTestsFail.PNG
[49]: ./media/cloud-services-continuous-delivery-use-vso/TestsFailed.PNG
[50]: ./media/cloud-services-continuous-delivery-use-vso/TestsResultsFailed.PNG