<properties
	pageTitle="Request increased DocumentDB account limits | Windows Azure"
	description="Learn how to request an adjustment to DocumentDB limits such as the number of allowed collections, stored procedures and query clauses."
	services="documentdb"
	authors="AndrewHoh"
	manager="jhubbard"
	editor="monicar"
	documentationCenter=""/>

<tags
	ms.service="documentdb"
	ms.date="10/22/2015"
	wacn.date=""/>

# Request increased DocumentDB account limits

<!-- deleted by customization [Windows --><!-- keep by customization: begin --> [Microsoft <!-- keep by customization: end --> Azure <!-- deleted by customization DocumentDB](/home/features/documentdb/) --><!-- keep by customization: begin --> DocumentDB](http://azure.microsoft.com/services/documentdb/) <!-- keep by customization: end --> has a set of default limits and quota enforcements.  Several quotas can be adjusted by contacting Azure support.  This article shows how to request an account limit increase.

After reading this article, you'll be able to answer the following questions:  

-	Which DocumentDB account quotas can be adjusted by contacting Azure support?
-	How can I request a DocumentDB account quota adjustment?

##<a id="AdjustableQuotas"></a> Adjustable DocumentDB account quotas

The following table describes the DocumentDB quotas that can be adjusted by contacting Azure support:   

|Entity |Quota (Standard Offer)|
|-------|--------|
|Database Accounts     |5
|Number of stored procedures, triggers and UDFs per collection       |25 each
|Maximum collections per database account    |100
|Maximum document storage per database (100 collections)    |1 TB
|Maximum number of UDFs per query     <!-- deleted by customization |2 --><!-- keep by customization: begin --> |1 <!-- keep by customization: end -->
|Maximum number of JOINs per query    <!-- deleted by customization |5 --><!-- keep by customization: begin --> |2 <!-- keep by customization: end -->
|Maximum number of AND clauses per query      <!-- deleted by customization |20 --><!-- keep by customization: begin --> |5 <!-- keep by customization: end -->
|Maximum number of OR clauses per query       <!-- deleted by customization |10 --><!-- keep by customization: begin --> |5 <!-- keep by customization: end -->
|Maximum number of values per IN expression       |100
<!-- deleted by customization
|Maximum number of points in a polygon argument in a ST_WITHIN query	|16
-->
|Maximum number of collection creates per minute    |5
|Maximum number of scale operations per minute    |5

##<a id="RequestQuotaIncrease"></a> Request a quota adjustment
The following steps show how to request a quota adjustment.

1. In the [Azure Preview <!-- deleted by customization portal](https://manage.windowsazure.cn) --><!-- keep by customization: begin --> portal](https://portal.azure.com) <!-- keep by customization: end -->, click **Browse**, and then click **Help + support**.

<!-- deleted by customization
	![Screenshot of launching help and support](./media/documentdb-increase-limits/helpsupport.png)
-->
<!-- keep by customization: begin -->
	![Screenshot of launching help and support](media/documentdb-increase-limits/helpsupport.png)
<!-- keep by customization: end -->

2. In the **Help + support** blade, click **Get Support**.

<!-- deleted by customization
	![Screenshot of creating a support ticket](./media/documentdb-increase-limits/getsupport.png)

3. In the **New support request** blade, click **Basics**. Next, set **Issue type** to **Quota**, **Subscription** to your subscription that hosts your DocumentDB account, **Service** to **DocumentDB**, and **Support plan** to **Quota SUPPORT - Included**. Finally, click **Next**.

	![Screenshot of support ticket request type](./media/documentdb-increase-limits/supportrequest1.png)

4. In the **Problem** blade, choose a severity. Set **Problem type** to **DocumentDB** and include information about your quota increase in **Details**. Click **Next**.

	![Screenshot of support ticket subscription picker](./media/documentdb-increase-limits/supportrequest2.png)

5. Finally, fill in your contact information in the **Contact information** blade.

	![Screenshot of support ticket resource picker](./media/documentdb-increase-limits/supportrequest3.png)

Once the support ticket has been created, you should receive the support request number via email.  You can also view the support request by clicking **Manage support requests** in the **Help + support** blade.

![Screenshot of support requests blade](./media/documentdb-increase-limits/supportrequest4.png)

-->
<!-- keep by customization: begin -->
	![Screenshot of creating a support ticket](media/documentdb-increase-limits/getsupport.png) 

3. In the **New support request** blade, click **Request Type**, and then in the **Request type** blade, click **Quotas**.

	![Screenshot of support ticket request type](media/documentdb-increase-limits/supportrequest1.png) 

4. In the **Subscription** blade, choose the subscription that hosts your DocumentDB account.

	![Screenshot of support ticket subscription picker](media/documentdb-increase-limits/supportrequest2.png)

5. In the **Resources** blade, choose **DocumentDB Accounts**.

	![Screenshot of support ticket resource picker](media/documentdb-increase-limits/supportrequest3.png)

6. In the **Support plan** blade, choose **Quotas Free Support**.

	![Screenshot of support ticket support plan picker](media/documentdb-increase-limits/supportrequest4.png)

7. In the **Problem** blade, choose the problem category **Quota or Core Increase Requests DocumentDB**.

	![Screenshot of support ticket problem category picker](media/documentdb-increase-limits/supportrequest5.png)

8. In the **Description** blade, enter a description of the request.  Be sure to include the specific quota adjustments you are requesting as well as the account(s) to which the adjustments should be made.

	![Screenshot of support ticket description textbox](media/documentdb-increase-limits/supportrequest6.png)

9. Click **Create**.

	![Screenshot of support ticket create button](media/documentdb-increase-limits/supportrequest7.png)

Once the support ticket has been created, you should receive the support request number via email.  You can also view the support request by clicking **Support requests** in the **Help + Support** blade.

![Screenshot of support requests blade](media/documentdb-increase-limits/supportrequest8.png)
  
<!-- keep by customization: end -->

##<a name="NextSteps"></a> Next steps
- To learn more about DocumentDB, click [here](http://azure.com/docdb).