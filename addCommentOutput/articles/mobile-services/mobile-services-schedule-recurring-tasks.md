<properties
	pageTitle="Schedule backend tasks in a JavaScript backend mobile service | Windows Azure"
	description="Use the scheduler in Azure Mobile Services to define JavaScript backend jobs that run on a schedule."
	services="mobile-services"
	documentationCenter=""
	authors="ggailey777"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="12/07/2015"
	wacn.date=""/>

# Schedule recurring jobs in Mobile Services

<!-- deleted by customization
[AZURE.INCLUDE [mobile-service-note-mobile-apps](../includes/mobile-services-note-mobile-apps.md)]
&nbsp;


> [AZURE.SELECTOR]
- [.NET backend](/documentation/articles/mobile-services-dotnet-backend-schedule-recurring-tasks)
- [Javascript backend](/documentation/articles/mobile-services-schedule-recurring-tasks)

This topic shows you how to use the job scheduler functionality in the Azure Management Portal to define server script code that is executed based on a schedule that you define. In this case, the script periodically check with a remote service, in this case Twitter, and stores the results in a new table. Some other periodic tasks that can be scheduled include:
-->
<!-- keep by customization: begin -->
<div class="dev-center-tutorial-subselector">
	<a href="/documentation/articles/mobile-services-dotnet-backend-schedule-recurring-tasks/" title=".NET backend">.NET backend</a> | <a href="/documentation/articles/mobile-services-schedule-recurring-tasks/"  title="JavaScript backend" class="current">JavaScript backend</a>
</div>
 
This topic shows you how to use the job scheduler functionality in the Management Portal to define server script code that is executed based on a schedule that you define. In this case, the script periodically check with a remote service, in this case Twitter, and stores the results in a new table. Some other periodic tasks that can be scheduled include:
<!-- keep by customization: end -->

+ Archiving old or duplicate data records.
+ Requesting and storing external data, such as tweets, RSS entries, and location information.
+ Processing or resizing stored images.

This tutorial shows you how to use the job scheduler to create a scheduled job that requests tweet data from Twitter and stores the tweets in a new Updates table.

##<a name="get-oauth-credentials"></a>Register for access to Twitter v1.1 APIs and store credentials

[AZURE.INCLUDE [mobile-services-register-twitter-access](../includes/mobile-services-register-twitter-access.md)]

##<a name="create-table"></a>Create the new Updates table

Next, you need to create a new table in which to store tweets.

<!-- deleted by customization
2. In the [Azure Management Portal], click the **Data** tab for your mobile service, then click **+Create**.

3. In **Table name** type _Updates_, then click the check button.
-->
<!-- keep by customization: begin -->
1. In the Management Portal, click the **Data** tab for your mobile service, then click **+Create**.

2. In **Table name** type _Updates_, then click the check button.
<!-- keep by customization: end -->

##<a name="add-job"></a>Create a new scheduled job

Now, you can create the scheduled job that accesses Twitter and stores tweet data in the new Updates table.

<!-- deleted by customization 2 --><!-- keep by customization: begin --> 1 <!-- keep by customization: end -->. Click the **Scheduler** tab, then click **+Create**.

    >[AZURE.NOTE]When you run your mobile service in <em>Free</em> tier, you are only able to run one scheduled job at a time. In paid tiers, you can run up to ten scheduled jobs at a time.

<!-- deleted by customization 3 --><!-- keep by customization: begin --> 2 <!-- keep by customization: end -->. In the scheduler dialog, enter _getUpdates_ for the **Job Name**, set the schedule interval and units, then click the check button.
<!-- deleted by customization

   	This creates a new job named **getUpdates**.

4. Click the new job you just created, click the **Script** tab and replace the placeholder function **getUpdates** with the following code:
-->
<!-- keep by customization: begin -->
   
   	This creates a new job named **getUpdates**. 

3. Click the new job you just created, click the **Script** tab and replace the placeholder function **getUpdates** with the following code:
<!-- keep by customization: end -->

		var updatesTable = tables.getTable('Updates');
		var request = require('request');
		var twitterUrl = "https://api.twitter.com/1.1/search/tweets.json?q=%23mobileservices&result_type=recent";

		// Get the service configuration module.
		var config = require('mobileservice-config');
		// Get the stored Twitter consumer key and secret.
		var consumerKey = config.twitterConsumerKey,
		    consumerSecret = config.twitterConsumerSecret
		// Get the Twitter access token from app settings.
		var accessToken= config.appSettings.TWITTER_ACCESS_TOKEN,
		    accessTokenSecret = config.appSettings.TWITTER_ACCESS_TOKEN_SECRET;
		function getUpdates() {
		    // Check what is the last tweet we stored when the job last ran
		    // and ask Twitter to only give us more recent tweets
		    appendLastTweetId(
		        twitterUrl,
		        function twitterUrlReady(url){
		            // Create a new request with OAuth credentials.
		            request.get({
		                url: url,
		                oauth: {
		                    consumer_key: consumerKey,
		                    consumer_secret: consumerSecret,
		                    token: accessToken,
		                    token_secret: accessTokenSecret
		                }},
		                function (error, response, body) {
		                if (!error && response.statusCode == 200) {
		                    var results = JSON.parse(body).statuses;
		                    if(results){
		                        console.log('Fetched ' + results.length + ' new results from Twitter');
		                        results.forEach(function (tweet){
		                            if(!filterOutTweet(tweet)){
		                                var update = {
		                                    twitterId: tweet.id,
		                                    text: tweet.text,
		                                    author: tweet.user.screen_name,
		                                    date: tweet.created_at
		                                };
		                                updatesTable.insert(update);
		                            }
		                        });
		                    }
		                } else {
		                    console.error('Could not contact Twitter');
		                }
		            });
		        });
		 }
		// Find the largest (most recent) tweet ID we have already stored
		// (if we have stored any) and ask Twitter to only return more
		// recent ones
		function appendLastTweetId(url, callback){
		    updatesTable
		    .orderByDescending('twitterId')
		    .read({success: function readUpdates(updates){
		        if(updates.length){
		            callback(url + '&since_id=' + (updates[0].twitterId + 1));
		        } else {
		            callback(url);
		        }
		    }});
		}
		function filterOutTweet(tweet){
		    // Remove retweets and replies
		    return (tweet.text.indexOf('RT') === 0 || tweet.to_user_id);
		}


   	This script calls the Twitter query API using stored credentials to request recent tweets that contain the hashtag `#mobileservices`. Duplicate tweets and replies are removed from the results before they are stored in the table.

    >[AZURE.NOTE]This sample assumes that only a few rows are inserted into the table during each scheduled run. In cases where many rows are inserted in a loop you may run out of connections when running on the Free tier. In this case, you should perform inserts in batches. For more information, see [How to: Perform bulk inserts](/documentation/articles/mobile-services-how-to-use-server-scripts#bulk-inserts).

<!-- deleted by customization 6 --><!-- keep by customization: begin --> 4 <!-- keep by customization: end -->. Click **Run Once** to test the script.

   	This saves and executes the job while it remains disabled in the scheduler.

<!-- deleted by customization 7 --><!-- keep by customization: begin --> 5 <!-- keep by customization: end -->. Click the back button, click **Data**, click the **Updates** table, click **Browse**, and verify that Twitter data has been inserted into the table.

<!-- deleted by customization 8 --><!-- keep by customization: begin --> 6 <!-- keep by customization: end -->. Click the back button, click **Scheduler**, select **getUpdates**, then click **Enable**.

   	This enables the job to run on the specified schedule, in this case every hour.

Congratulations, you have successfully created a new scheduled job in your mobile service. This job will be executed as scheduled until you disable or modify it.

## <a name="nextsteps"> </a>See also

* [Mobile Services server script reference]
  <br/>Learn more about registering and using server scripts.

<!-- Anchors. -->
[Register for Twitter access and store credentials]: #get-oauth-credentials
[Create the new Updates table]: #create-table
[Create a new scheduled job]: #add-job
[Next steps]: #next-steps

<!-- Images. -->

<!-- URLs. -->
<!-- deleted by customization
[Mobile Services server script reference]: http://go.microsoft.com/fwlink/?LinkId=262293
[WindowsAzure.com]: http://azure.microsoft.com/
-->
<!-- keep by customization: begin -->
[Mobile Services server script reference]: /documentation/articles/mobile-services-how-to-use-server-scripts/
[windowsazure.cn]: http://www.windowsazure.cn/
<!-- keep by customization: end -->
[Azure Management Portal]: https://manage.windowsazure.cn/
[Register your apps for Twitter login with Mobile Services]: /documentation/articles/mobile-services-how-to-register-twitter-authentication
[Twitter Developers]: https://apps.twitter.com/
[App settings]: http://msdn.microsoft.com/zh-cn/library/azure/b6bb7d2d-35ae-47eb-a03f-6ee393e170f7
