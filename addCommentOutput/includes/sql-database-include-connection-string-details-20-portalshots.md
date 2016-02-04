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

5. Make note of the **SQL database** name and the **Server name**.  The username will be yourusername@yourserver.

	<!-- deleted by customization ![Get Connection Details][3-get-connection-details] -->

7.  Paste the connection details into your client program code.  You will need to replace the {your_password_here} with your real password.


<!--
Could not find a good link for PHP

For more information, see:<br/>[Connection Strings and Configuration Files](https://msdn.microsoft.com/zh-cn/library/ms378428.aspx).
-->


<!-- Image references. -->

[1-select-sql]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-select-sql.png

[2-select-database]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-select-database.PNG

[3-get-connection-details]: ./media/sql-database-include-connection-string-20-portalshots/connection-string-details.PNG


<!--
These three includes/ files are a sequenced set, but you can pick and choose:

<!-- deleted by customization includes/sql-database-include-connection-string-20-portalshots.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-20-portalshots.md <!-- keep by customization: end -->
<!-- deleted by customization includes/sql-database-include-connection-string-30-compare.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-30-compare.md <!-- keep by customization: end -->
<!-- deleted by customization includes/sql-database-include-connection-string-40-config.md --><!-- keep by customization: begin --> ../includes/sql-database-include-connection-string-40-config.md <!-- keep by customization: end -->
-->
