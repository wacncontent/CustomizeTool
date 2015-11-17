replacement:

deleted:

		> [AZURE.WARNING] MongoDB<!-- keep by customization: begin --> <p>MongoDB <!-- keep by customization: end --> security features, such as authentication and IP address binding, are not enabled by default. Security features should be enabled before deploying MongoDB to a production environment.  See [Security<!-- keep by customization: begin --> <a href="http://www.mongodb.org/display/DOCS/Security+and+Authentication">Security <!-- keep by customization: end --> and Authentication](http://www.mongodb.org/display/DOCS/Security+and+Authentication)<!-- keep by customization: begin --> Authentication</a> <!-- keep by customization: end --> for more information.<!-- keep by customization: begin --> information.</p> <!-- keep by customization: end -->

replaced by:

		<div class="dev-callout">
		<b>Warning</b>
		<!-- keep by customization: begin --> <p>MongoDB

reason: ()

deleted:

		9. Add an endpoint with the following settings:
		
		 - **Name**: Mongo
		 - **Protocol**: TCP
		 - **Public Port**: 27017
		 - **Private Port**: 27017
		 
		 This will allow MongoDB to be accessed remotely.

replaced by:

		9. Add an endpoint with name "Mongo", protocol **TCP**, and both **Public** and **Private** ports set to "27017". This will allow MongoDB to be accessed remotely.
			
			![Endpoints][Image9]

reason: ()

