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
azurehdinsight.net = 	http://msdn.microsoft.com/zh-cn/library/azure/	azurehdinsight.cn
trafficmanager.net = 	http://msdn.microsoft.com/zh-cn/library/azure/	trafficmanager.cn
/en-us/documentation/articles/ = 	/documentation/articles/
onmicrosoft.com = 	partner.onmschina.cn
azure-mobile.net = 	azure-mobile.net
http://portal.microsoftonline.com = 	https://portal.partner.microsoftonline.cn
azure.net = 	???
http://en.wikipedia.org = 	http://zh.wikipedia.org
SQL Database = 	SQL Êý¾Ý¿â
Microsoft Azure = 	Windows Azure
http://azure.microsoft.com/services/active-directory/ = 	/home/features/identity/
https://passwordreset.microsoftonline.com = 	???
http://myapps.microsoft.com = 	???
# £×est US , etc..	China East, China North
http://azure.microsoft.com/en-us/downloads/ = 	/downloads/

[REGEX]
# [link text](xxx-xxx-xxx.md) = 	[link text](/documentation/articles/xxx-xxx-xxx)
(\[.*?\]\()(\.\.\/)?([^\/]*?)(\.md)(\)) = \1/documentation/articles/\3\5

# [link text](/zh-cn/documentation/articles/xxx-xxx-xxx)	[link text](/documentation/articles/xxx-xxx-xxx)
(\[.*?\]\()(\/zh-cn)(\/documentation\/articles\/.*?\)) = \1\3

#[link text](xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\()(\.\.\/)?([^\/]*?)(\.md)#([^\/]*?)(\)) = \1/documentation/articles/\3#\5\6

#[link text](/documentation/articles/xxx-xxx-xxx.md#xxx-xxx) = 	[link text](/documentation/articles/xxx-xxx-xxx#xxx-xxx)
(\[.*?\]\()/documentation/articles/([^\/]*?)(\.md)#([^\/]*?)(\)) = \1/documentation/articles/\2#\4\5