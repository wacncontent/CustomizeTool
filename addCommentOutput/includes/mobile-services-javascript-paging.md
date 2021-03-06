

1. In Visual Studio, open the project that you modified when you completed the tutorial **Get started with data**.

2. Press the **F5** key to run the app, then type text in **Insert a TodoItem** and click **Save**.

3. Repeat the previous step at least three times, so that you have more than three items stored in the TodoItem table. 

<!-- deleted by customization 2 --><!-- keep by customization: begin --> 4 <!-- keep by customization: end -->. In the default.js file, replace the **RefreshTodoItems** method with the following code:

        var refreshTodoItems = function () {
            // Define a filtered query that returns the top 3 items.
            todoTable.where({ complete: false })
                .take(3)
                .read()
                .done(function (results) {
                    todoItems = new WinJS.Binding.List(results);
                    listItems.winControl.itemDataSource = todoItems.dataSource;
                });
        };

  	This query, when executed during data binding, returns the top three items that are not marked as completed.

<!-- deleted by customization 3 --><!-- keep by customization: begin --> 5 <!-- keep by customization: end -->. Press the **F5** key to run the app.

  	Notice that only the first three results from the TodoItem table are displayed. 

<!-- deleted by customization 4 --><!-- keep by customization: begin --> 6 <!-- keep by customization: end -->. (Optional) View the URI of the request sent to the mobile service by using message inspection software, such as browser developer tools or [Fiddler].

   	Notice that the **take(3)** method was translated into the query option **$top=3** in the query URI.

<!-- deleted by customization 5 --><!-- keep by customization: begin --> 7 <!-- keep by customization: end -->. Update the **RefreshTodoItems** method once more with the following code:
            
        var refreshTodoItems = function () {
            // Define a filtered query that skips the first 3 items and 
            // then returns the next 3 items.
            todoTable.where({ complete: false })
                .skip(3)
                .take(3)
                .read()
                .done(function (results) {
                    todoItems = new WinJS.Binding.List(results);
                    listItems.winControl.itemDataSource = todoItems.dataSource;
                });
        };

   	This query skips the first three results and returns the next three after that. This is effectively the second "page" of data, where the page size is three items.

    > [AZURE.NOTE] This tutorial uses a simplified scenario by passing hard-coded paging values to the **Take** and **Skip** methods. In a real-world app, you can use queries similar to the above with a pager control or comparable UI to let users navigate to previous and next pages.  You can also call the  **includeTotalCount** method to get the total count of items available on the server, along with the paged data.

<!-- deleted by customization 6 --><!-- keep by customization: begin --> 8 <!-- keep by customization: end -->. (Optional) Again view the URI of the request sent to the mobile service.

   	Notice that the **skip(3)** method was translated into the query option **$skip=3** in the query URI.

<!-- URLs -->
[Fiddler]: http://go.microsoft.com/fwlink/?LinkID=262412