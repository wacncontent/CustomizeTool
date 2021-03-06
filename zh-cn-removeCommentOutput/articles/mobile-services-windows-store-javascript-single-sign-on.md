﻿<properties 
	pageTitle="使用 Live Connect 对应用程序进行身份验证 (JavaScript)" 
	description="了解如何在 Azure 移动服务中从 Windows 应用商店应用程序使用 Live Connect 单一登录。" 
	services="mobile-services" 
	documentationCenter="windows" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="08/08/2015" 
	wacn.date="10/22/2015"/>

# 使用 Microsoft 帐户以客户端托管身份验证方式对 Windows 应用商店应用进行身份验证

[AZURE.INCLUDE [mobile-services-selector-single-signon](../includes/mobile-services-selector-single-signon.md)]

##概述
本主题说明如何通过 Windows 应用商店应用程序对 Azure 移动服务中的用户进行身份验证。在本教程中，你将使用 Live Connect 向快速入门项目添加身份验证功能。成功通过 Live Connect 进行身份验证后，将使用名称欢迎已登录的用户并显示用户 ID 值。

>[AZURE.NOTE]本教程将演示使用客户端托管身份验证和 Live SDK 的好处。这使你可以更轻松地使用移动服务对已登录的用户进行身份验证。你还可以请求额外的范围，使你的应用程序也能访问 OneDrive 等资源。服务托管的身份验证提供更通用的体验，并支持多种身份验证提供者。有关服务托管身份验证的详细信息，请参阅[向应用程序添加身份验证](/documentation/articles/mobile-services-windows-store-javascript-get-started-users)。

本教程需要的内容如下：

+ [Live SDK for Windows]
+ Microsoft Visual Studio 2012 Express for Windows 8 RC 或更高版本
+ 你还必须先完成教程[将移动服务添加到现有应用程序]。

##注册应用程序以使用 Microsoft 帐户进行身份验证

若要对用户进行身份验证，必须在 Microsoft 帐户开发人员中心注册你的应用程序。然后，必须将此注册连接到你的移动服务。请完成以下主题中的步骤，以创建 Microsoft 帐户注册并将注册连接到你的移动服务。

+ [注册应用程序以使用 Microsoft 帐户登录](/documentation/articles/mobile-services-how-to-register-microsoft-authentication)

##<a name="permissions"></a>将权限限制给已经过身份验证的用户

接下来，必须限制对资源的访问，在本例中，请确保 *TodoItems* 表只能由登录用户访问。

[AZURE.INCLUDE [mobile-services-restrict-permissions-windows](../includes/mobile-services-restrict-permissions-windows.md)]

##<a name="add-authentication"></a>向应用程序添加身份验证

最后，请添加 Live SDK 并用它来对应用程序中的用户进行身份验证。

1. 在“解决方案资源管理器”中，右键单击该解决方案，然后选择“管理 NuGet 程序包”。

2. 在左窗格中，选择“联机”类别，搜索“LiveSDK”，单击“Live SDK”包对应的“安装”，然后接受许可协议。

  	这会将 Live SDK 添加到解决方案。

3. 打开 default.html 项目文件，并在 `<script>` 元素中添加以下 `<head>` 元素。

        <script src="/js/wl.js"></script>

4. 在 **app.OnActivated** 方法重载中，将对 **refreshTodoItems** 方法的调用替换为以下代码：
	
        // Set the mobileClient variable to client variable generated by the tooling.
        var mobileClient = <yourClient>;

        var session = null;
        var login = function () {
            return new WinJS.Promise(function (complete) {                    
                WL.login({ scope: "wl.basic"}).then(function (result) {
                    session = result.session;

                    WinJS.Promise.join([
                        WL.api({ path: "me", method: "GET" }),
                        mobileClient.login(result.session.authentication_token)
                    ]).done(function (results) {
                        // Build the welcome message from the Microsoft account info.
                        var profile = results[0];
                        var title = "Welcome " + profile.first_name + "!";
                        var message = "You are now logged in as: "
                            + mobileClient.currentUser.userId;
                        var dialog = new Windows.UI.Popups.MessageDialog(message, title);
                        dialog.showAsync().then(function () {
                            // Reload items from the mobile service.
                            refreshTodoItems();
                        }).done(complete);
                        
                    }, function (error) {

                    });                       
                }, function (error) {                        
                    session = null;
                    var dialog = new Windows.UI.Popups.MessageDialog("You must log in.", "Login Required");
                    dialog.showAsync().done(complete);                        
                });
            });
        }

        var authenticate = function () {
            // Block until sign-in is successful.
            login().then(function () {
                if (session === null) {
                    // Authentication failed, try again.
                    authenticate();
                }
            });
        }

		// Initialize the Live client.
        WL.init({
            redirect_uri: mobileClient.applicationUrl
        });           
            
		// Start the sign-in process.
        authenticate();

    此代码初始化 Live Connect 客户端，向 Microsoft 帐户发送一个新的登录请求，将返回的身份验证令牌发送到移动服务，然后显示有关已登录用户的信息。

	>[AZURE.NOTE]理想情况下，你应该不会在每次你的应用运行时都请求实时连接身份验证令牌或移动服务授权令牌。不只是这效率低下，你可以运行到使用情况的相关问题应该很多客户尝试在同一时间开始你的应用程序。更好的方法是缓存令牌，并首先尝试使用缓存的移动服务令牌，然后再调用 **LoginWithMicrosoftAccountAsync**。有关如何缓存此令牌的示例，请参阅[身份验证入门](/documentation/articles/mobile-services-windows-store-javascript-get-started-users/#tokens)
	
5. 将上述代码第一行中的值 `<yourClient>` 替换为将项目连接到移动服务时添加的 .js 文件中定义的变量。
		
6. 按 F5 键运行应用程序，然后使用你的 Microsoft 帐户登录。

   	当你成功登录时，应用应该运行而不会出现错误，你应该能够查询移动服务，并对数据进行更新。

## <a name="next-steps"></a>后续步骤

在下一教程[使用脚本为用户授权]中，你将使用移动服务基于已进行身份验证的用户提供的用户 ID 值来筛选移动服务返回的数据。有关如何使用其他标识提供者进行身份验证的信息，请参阅[身份验证入门]。

<!-- Anchors. -->
[Register your app for authentication and configure Mobile Services]: #register
[Restrict table permissions to authenticated users]: #permissions
[Add authentication to the app]: #add-authentication
[Next Steps]: #next-steps

<!-- Images. -->

<!-- URLs. -->
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253
[将移动服务添加到现有应用程序]: /documentation/articles/mobile-services-windows-store-javascript-get-started-data
[身份验证入门]: /documentation/articles/mobile-services-windows-store-javascript-get-started-users
[使用脚本为用户授权]: /documentation/articles/mobile-services-windows-store-javascript-authorize-users-in-scripts

[Azure Management Portal]: https://manage.windowsazure.cn/

<!---HONumber=74-->