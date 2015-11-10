
   * Click **Sign In**, and then enter the credentials for your Azure account.

     This method is quicker and easier, but if you use this method you won't be able to see Azure SQL Database or Mobile Services in the **Server Explorer** window.

   * Click **Manage subscriptions** in order to install a management certificate that enables access to your account.

     In the **Manage Azure Subscriptions** dialog box, click the **Certificates** tab, and then click **Import**. Follow the directions to download and import a subscription file (also called a *.publishsettings* file) for your Azure account.

<!-- deleted by customization
     > [AZURE.NOTE] Download<!-- keep by customization: begin --> <p>Download <!-- keep by customization: end --> the subscription file to a folder outside your source code directories (for example, in the Downloads folder), and then delete it once the import has completed. A malicious user who gains access to the subscription file can edit, create, and delete your Azure services.<!-- keep by customization: begin --> services.</p></div> <!-- keep by customization: end -->
-->
<!-- keep by customization: begin -->
     <div class="dev-callout"><strong>Security Note:</strong>
     <!-- keep by customization: begin --> <p>Download <!-- keep by customization: end --> the subscription file to a folder outside your source code directories (for example, in the Downloads folder), and then delete it once the import has completed. A malicious user who gains access to the subscription file can edit, create, and delete your Azure <!-- keep by customization: begin --> services.</p></div> <!-- keep by customization: end -->
<!-- keep by customization: end -->

   For more information, see [How to Connect to Azure from Visual Studio](https://msdn.microsoft.com/zh-cn/library/azure/hh531793.aspx).
