[CONST]
# Below is the const string that will be substituted
cloudapp.net = 	chinacloudapp.cn
windows.net = 	chinacloudapi.cn
database.windows.net = 	database.chinacloudapi.cn
manage.windowsazure.com = 	manage.windowsazure.cn
https://portal.azure.com/ = 	https://manage.windowsazure.cn
windowsazure.com/en-us/ = 	windowsazure.cn/
windowsazure.com = 	windowsazure.cn
azurewebsites.net = 	chinacloudsites.cn
http://msdn.microsoft.com/en-us/library/azure/ = http://msdn.microsoft.com/zh-cn/library/azure/
http://msdn.microsoft.com/library/azure/ = 	http://msdn.microsoft.com/zh-cn/library/azure/
azurehdinsight.net = azurehdinsight.cn
trafficmanager.net = trafficmanager.cn
/en-us/documentation/articles/ = 	/documentation/articles/
onmicrosoft.com = 	partner.onmschina.cn
azure-mobile.net = 	azure-mobile.net
http://portal.microsoftonline.com = 	https://portal.partner.microsoftonline.cn
azure.net = 	???
http://en.wikipedia.org = 	http://zh.wikipedia.org
Microsoft Azure = 	Windows Azure
http://azure.microsoft.com/services/active-directory/ = 	/home/features/identity/
/documentation/services/active-directory = /documentation/services/identity
http://azure.microsoft.com/zh-cn/services/app-service/web/ = /home/features/web-site/
/documentation/articles/app-service/ = /documentation/articles/
https://passwordreset.microsoftonline.com = 	???
http://myapps.microsoft.com = 	???
# £×est US , etc..	China East, China North
http://azure.microsoft.com/en-us/downloads/ = 	/downloads/
wacn.date{equal}"" = wacn.date{equal}"09/15/2015"
¨C = -
../../includes/ = ../includes/

[REGEX]
# [link text](xxx-xxx-xxx.md) = 	[link text](/documentation/articles/xxx-xxx-xxx)
(\[.*?\]\()(\.\.\/)?([^\/]*?)(\.md)(\)) = \1/documentation/articles/\3\5

# [link text](/zh-cn/documentation/articles/xxx-xxx-xxx)	[link text](/documentation/articles/xxx-xxx-xxx)
(\[.*?\]\()(\/zh-cn)(\/documentation\/articles\/.*?\)) = \1\3

#[link text](xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\()(\.\.\/)?([^\/]*?)(\.md)#([^\/]*?)(\)) = \1/documentation/articles/\3#\5\6

#[link text](/documentation/articles/xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\()/documentation/articles/([^\/]*?)(\.md)#([^\/]*?)(\)) = \1/documentation/articles/\2#\4\5

#![image text](media/xxx-xxx-xxx/xxx-xxx.xxx) = ![image text](./media/xxx-xxx-xxx/xxx-xxx.xxx)
(!\[.*?\]\()media/([^\(|^\)]+\)) = \1./media/\2

https?://azure.microsoft.com(/zh-cn)?/documentation/articles/ = /documentation/articles/

# ## 1\. = ## 1.
([\#]+)([\s]*)([0-9]+)\\\. = \1\2\3.

# **XXX\_XXX** = **XXX_XXX**
(\*+[^\*]*)\\_([^\*]*\*+) = \1_\2