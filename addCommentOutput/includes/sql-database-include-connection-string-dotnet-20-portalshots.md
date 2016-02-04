<!--
<!-- deleted by customization includes/sql-database-include-connection-string-20-portalshots.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-20-portalshots.md <!-- keep by customization: end -->

Latest Freshness check:  2015-09-02 , GeneMi.

## Connection string
-->


### Obtain the connection string from the Azure Management Portal


Use the [Azure <!-- deleted by customization preview --><!-- keep by customization: begin --> classical <!-- keep by customization: end --> portal](http://manage.windowsazure.cn/) to obtain the connection string necessary for your client program to interact with Azure SQL Database:


1. Click **BROWSE** > **SQL databases**.

    <!-- deleted by customization ![Select SQL][1-select-sql] -->

2. Enter the name of your database into the filter text box near the upper-left of the **SQL databases** blade.

    <!-- deleted by customization ![Select Database][2-select-database]] -->

3. Click the row for your database.

4. After the blade appears for your database, for visual convenience you can click the standard minimize controls to collapse the blades  you used for browsing and database filtering.

5. On the blade for your database, click **Show database connection strings**.

6. If you intend to use the ADO.NET connection library, copy the string labeled **ADO.NET**.

	<!-- deleted by customization ![Copy the ADO.NET connection string for your database][3-get-connection-string] -->

7. Paste the connection string information into your client program code.  You will need to replace the {your_password_here} with your real password.



For more information, see: [Connection Strings and Configuration Files](http://msdn.microsoft.com/zh-cn/library/ms254494.aspx).

<!-- Image references. -->

[1-select-sql]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-select-sql.png


[2-select-database]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-select-database.PNG

[3-get-connection-string]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-dotnet.PNG


<!--
These three includes/ files are a sequenced set, but you can pick and choose:

<!-- deleted by customization includes/sql-database-include-connection-string-20-portalshots.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-20-portalshots.md <!-- keep by customization: end -->
<!-- deleted by customization includes/sql-database-include-connection-string-30-compare.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-30-compare.md <!-- keep by customization: end -->
<!-- deleted by customization includes/sql-database-include-connection-string-40-config.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-40-config.md <!-- keep by customization: end -->
-->
