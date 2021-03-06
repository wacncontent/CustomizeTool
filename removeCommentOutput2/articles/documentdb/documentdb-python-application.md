<properties
    pageTitle="Python Flask web site Development with DocumentDB | Windows Azure"
    description="Review a database tutorial on using DocumentDB to store and access data from a Python Flask web site hosted on Azure. Find application development solutions." 
	keywords="Application development, database tutorial, python flask, python web site, python web development, documentdb, azure, Microsoft azure"
    services="documentdb"
    documentationCenter="python"
    authors="ryancrawcour"
    manager="jhubbard"
    editor="cgronlun"/>

<tags
	ms.service="documentdb"
	ms.date="12/18/2015"
	wacn.date=""/>

# Python Flask Web Application Development with DocumentDB

> [AZURE.SELECTOR]
- [.NET](documentdb-dotnet-application.md)
- [Node.js](documentdb-nodejs-application.md)
- [Java](documentdb-java-application.md)
- [Python](documentdb-python-application.md)

To highlight how customers can efficiently leverage Azure DocumentDB to
store and query JSON documents, this document provides an end-to-end Python web application 
tutorial showing how to build a voting web site using Azure DocumentDB.

This tutorial shows you how to use the DocumentDB service provided by
Azure to store and access data from a Python web application hosted on
Azure and presumes that you have some prior experience using Python and
Azure websites.

This database tutorial covers:

1. Creating and provisioning a DocumentDB account.
2. Creating a Python MVC application.
3. Connecting to and using Azure DocumentDB from your web application.
4. Deploying the web site to Azure Websites.

By following this tutorial, you will build a simple voting
application that allows you to vote for a poll.

![Screen shot of the todo list web application created by this database tutorial](./media/documentdb-python-application/image1.png)


## Database tutorial prerequisites

Before following the instructions in this article, you should ensure
that you have the following installed:

- [Visual Studio 2013](http://www.visualstudio.com/) or higher, or Visual Studio Express, which is the free version.
- Python Tools for Visual Studio from [here][].
- Azure SDK for Visual Studio 2013, version 2.4 or higher available from
[here][1].
- Python 2.7 from [here][2].
- Microsoft Visual C++ Compiler for Python 2.7 from [here][3].

## Step 1: Create a DocumentDB database account

Let's start by creating a DocumentDB account. If you already have an account, you can skip to [Step 2: Create a new Python Flask web application](#Step-2:-Create-a-new-Python-Flask-Web-Application).

[AZURE.INCLUDE [documentdb-create-dbaccount](../../includes/documentdb-create-dbaccount.md)]

[AZURE.INCLUDE [documentdb-keys](../../includes/documentdb-keys.md)]

<br/>
We will now walk through how to create a new Python Flask web application from the ground up.

## Step 2: Create a new Python Flask web application 

1. Open Visual Studio, click **File** -\> **New Project** -\> **Python** -\>, **Flask Web
Project**, and then create a new project with the name **tutorial**.

	For those new to Python Flask, it is a web application development framework that helps us build web applications in Python faster. [Click here to access Flask tutorials][].

	![Screen shot of the New Project window in Visual Studio with Python highlighted on the left, Python Flask Web Project selected in the middle, and the name tutorial in the Name box](./media/documentdb-python-application/image9.png)

2. It will ask you whether you want to
install external packages. Click **Install into a virtual environment**. Be sure to use Python 2.7 as the base environment because PyDocumentDB does not currently support Python 3.x.  This will set up the required Python virtual environment for your project.

	![Screen shot of the database tutorial - Python Tools for Visual Studio window](./media/documentdb-python-application/image10.png)


## Step 3: Modify the Python Flask web application 

### Add Python Flask packages to your project

After your project is set up, you need to add certain Flask packages that
you will need for your project, including pydocumentdb, the Python package for DocumentDB.

1. Open the file named **requirements.txt** and replace the contents with the following:

    	flask==0.9
    	flask-mail==0.7.6
    	sqlalchemy==0.7.9
    	flask-sqlalchemy==0.16
    	sqlalchemy-migrate==0.7.2
    	flask-whooshalchemy==0.55a
    	flask-wtf==0.8.4
    	pytz==2013b
    	flask-babel==0.8
    	flup
    	pydocumentdb>=1.0.0

2. Right-click **env** and click **install from requirements.txt**.

	![Screen shot showing env (Python 2.7) selected with Install from requirements.txt highlighted in the list](./media/documentdb-python-application/image11.png)

> [AZURE.NOTE] In rare cases, you might see a failure in the output window. If
this happens, check if the error is related to cleanup. Sometimes the
cleanup fails, but the installation will still be successful (scroll up
in the output window to verify this).
<a name="verify-the-virtual-environment"></a> If this occurs, it's OK to continue.


### Verify the virtual environment

Let's make sure that everything is installed correctly.

- Start the website by pressing **F5** This launches the Flask development server
and starts your web browser. You should see the following page.

	![The empty Python Flask web development project displayed in a browser](./media/documentdb-python-application/image12.png)

### Create database, collection, and document definitions

Now let's create your voting application.

- Add a Python file by right-clicking the folder named **tutorial** in the Solution Explorer.  Name the file **forms.py**.  

```python
from flask.ext.wtf import Form
from wtforms import RadioField

class VoteForm(Form):
	deploy_preference  = RadioField('Deployment Preference', choices=[
        ('Web Site', 'Web Site'),
        ('Cloud Service', 'Cloud Service'),
        ('Virtual Machine', 'Virtual Machine')], default='Web Site')
```

### Add the required imports to views.py

- Add the following import statements at the top in **views.py**. These import DocumentDB's PythonSDK and the Flask packages.

```python
from forms import VoteForm
import config
import pydocumentdb.document_client as document_client
```


### Create database, collection, and document

- Add the following code to **views.py**. This takes care of creating the
database used by the form. Do not delete any of the existing code in
**views.py**. Simply append this to the end.

```python
@app.route('/create')
def create():
	"""Renders the contact page."""
        client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
	
        # Attempt to delete the database.  This allows this to be used to recreate as well as create
        try:
        db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
        client.DeleteDatabase(db['_self'])
        except:
        pass
	
       	# Create database
        db = client.CreateDatabase({ 'id': config.DOCUMENTDB_DATABASE })
        
        # Create collection
        collection = client.CreateCollection(db['_self'],{ 'id': config.DOCUMENTDB_COLLECTION }, { 'offerType': 'S1' })
        
        # Create document
        document = client.CreateDocument(collection['_self'],
        { 'id': config.DOCUMENTDB_DOCUMENT,
          'Web Site': 0,
          'Cloud Service': 0,
          'Virtual Machine': 0,
          'name': config.DOCUMENTDB_DOCUMENT 
        })
	
        return render_template(
        	'create.html',
        	title='Create Page',
        	year=datetime.now().year,
        	message='You just created a new database, collection, and document.  Your old votes have been deleted')
```

> [AZURE.TIP] The **CreateCollection** method takes an optional **RequestOptions** as the third parameter. This can be used to specify the Offer Type for the collection. If no offerType value is supplied, then the collection will be created using the default Offer Type. For more information on DocumentDB Offer Types, see [Performance levels in DocumentDB](documentdb-performance-levels.md).
>
### Read database, collection, document, and submit form

- Add the following code to **views.py**. This takes care of setting up
the form, reading the database, collection, and document. Do not delete
any of the existing code in **views.py**. Simply append this to the end.

```python
@app.route('/vote', methods=['GET', 'POST'])
def vote():
	form = VoteForm()
        replaced_document ={}
        if form.validate_on_submit(): # is user submitted vote  
        client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY})
	
        # Read databases and take the first since the id should not be duplicated.
        db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE))
	
        # Read collections and take the first since the id should not be duplicated.
        coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config.DOCUMENTDB_COLLECTION))
	
        # Read documents and take the first since the id should not be duplicated.
        doc = next((doc for doc in client.ReadDocuments(coll['_self']) if doc['id'] == config.DOCUMENTDB_DOCUMENT))
	
        # Take the data from the deploy_preference and increment your database
        doc[form.deploy_preference.data] = doc[form.deploy_preference.data] + 1
        replaced_document = client.ReplaceDocument(doc['_self'], doc)
	
        # Create a model to pass to results.html
        class VoteObject:
        	choices = dict()
                total_votes = 0
		
	vote_object = VoteObject()
        vote_object.choices = {
        	"Web Site" : doc['Web Site'],
                "Cloud Service" : doc['Cloud Service'],
                "Virtual Machine" : doc['Virtual Machine']
	}
        
        vote_object.total_votes = sum(vote_object.choices.values())
	
        return render_template(
        	'results.html',
                year=datetime.now().year,
                vote_object = vote_object)
		
	else :
        return render_template(
        	'vote.html',
                title = 'Vote',
                year=datetime.now().year,
                form = form)
```


### Create the HTML files

Under the templates folder, add the following html files: create.html, results.html, vote.html.

1. Add the following code to **create.html**. It takes care of displaying
a message stating that we created a new database, collection, and document.

```html
{% extends "layout.html" %}
{% block content %}
<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<p><a href="{{ url_for('vote') }}" class="btn btn-primary btn-large">Vote &raquo;</a></p>
{% endblock %}
```

2. Add the following code to **results.html**. It takes care of displaying
the results of the poll.

```html
{% extends "layout.html" %}
{% block content %}
<h2>Results of the vote</h2>
	<br />
	
{% for choice in vote_object.choices %}
<div class="row">
	<div class="col-sm-5">{{choice}}</div>
        <div class="col-sm-5">
        	<div class="progress">
        		<div class="progress-bar" role="progressbar" aria-valuenow="{{vote_object.choices[choice]}}" aria-valuemin="0" aria-valuemax="{{vote_object.total_votes}}" style="width: {{(vote_object.choices[choice]/vote_object.total_votes)*100}}%;">
                    		{{vote_object.choices[choice]}}
			</div>
		</div>
        </div>
</div>
{% endfor %}

<br />
<a class="btn btn-primary" href="{{ url_for('vote') }}">Vote again?</a>
{% endblock %}
```

3. Add the following code to **vote.html**. It takes care of displaying the
poll and accepting the votes. On registering the votes, the control is
passed over to views.py where we will recognize the vote cast and
append the document accordingly.

```html
{% extends "layout.html" %}
{% block content %}
<h2>What is your favorite way to host an application on Azure?</h2>
<form action="" method="post" name="vote">
	{{form.hidden_tag()}}
        {{form.deploy_preference}}
        <button class="btn btn-primary" type="submit">Vote</button>
</form>
{% endblock %}
```

4. Replace the contents of **index.html** with the following. This
serves as the landing page for your application.

```html
{% extends "layout.html" %}
{% block content %}
<h2>Python + DocumentDB Voting Application.</h2>
<h3>This is a sample DocumentDB voting application using PyDocumentDB</h3>
<p><a href="{{ url_for('create') }}" class="btn btn-primary btn-large">Create/Clear the Voting Database &raquo;</a></p>
<p><a href="{{ url_for('vote') }}" class="btn btn-primary btn-large">Vote &raquo;</a></p>
{% endblock %}
```

### Add a configuration file and change the \_\_init\_\_.py

1. Right-click the project name tutorial and add a file, **config.py**.
This config file is required by forms in Flask. You can use it to provide a
secret key as well. This key is not needed for this tutorial though.

2. Add the following code to config.py. Alter the values of **DOCUMENTDB\_HOST** and **DOCUMENTDB\_KEY**.

```python
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DOCUMENTDB_HOST = 'https://YOUR_DOCUMENTDB_NAME.documents.azure.com:443/'
DOCUMENTDB_KEY = 'YOUR_SECRET_KEY_ENDING_IN_=='

DOCUMENTDB_DATABASE = 'voting database'
DOCUMENTDB_COLLECTION = 'voting collection'
DOCUMENTDB_DOCUMENT = 'voting document'
```

3. Similarly replace the contents of **\_\_init\_\_.py** with the following.

```python
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
import tutorial.views
```

4. After following the above mentioned steps, this is how Solution
Explorer should look.

	![Screen shot of the Visual Studio Solution Explorer window](./media/documentdb-python-application/image15.png)


## Step 4: Run your web application locally

1. Press F5 or click the **Run** button in Visual Studio, and you should see the
following on your screen.

	![Screen shot of the Python + DocumentDB Voting Application displayed in a web browser](./media/documentdb-python-application/image16.png)

2. Click **Create/Clear the Voting Database** to generate the database.

	![Screen shot of the Create Page of the web application – development details](./media/documentdb-python-application/image17.png)

3. Then, click **Vote** and select your option.

	![Screen shot of the web application with a voting question posed](./media/documentdb-python-application/image18.png)

4. For every vote you cast, it increments the appropriate counter.

	![Screen shot of the Results of the vote page shown](./media/documentdb-python-application/image19.png)


## Step 5: Deploy the web application to Azure Websites

Now that you have the complete application working correctly against
DocumentDB, we're going to deploy this to Azure Websites.

1. Right-click the project in Solution Explorer (make sure you're not still running it
locally) and select **Publish**.  Then, select **Microsoft Azure Websites**.

 	![Screen shot of the tutorial selected in Solution Explorer, with the Publish option highlighted](./media/documentdb-python-application/image20.png)

2. Configure your Azure website by providing your credentials and click **Publish**.

	![Screen shot of the Publish Web window](./media/documentdb-python-application/image21.png)

3. In a few seconds, Visual Studio will finish publishing your web
application and launch a browser where you can see your handy work
running in Azure!

## Next steps

Congratulations! You have just completed your first Python web application using
Azure DocumentDB and published it to Azure Websites.

We update and improve this topic frequently based on your feedback.  Once you've completed the tutorial, please using the voting buttons at the top and bottom of this page, and be sure to include your feedback on what improvements you want to see made. If you'd like us to contact you directly, feel free to include your email address in your comments.

To add additional functionality to your web application, review the APIs available in the [DocumentDB Python SDK](https://pypi.python.org/pypi/pydocumentdb).

For more information, see the [Python Developer Center](/develop/python/).


  [Click here to access Flask tutorials]: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
  [Visual Studio Express]: http://www.visualstudio.com/products/visual-studio-express-vs.aspx
  [here]: http://aka.ms/ptvs
  [1]: http://go.microsoft.com/fwlink/?linkid=254281&clcid=0x409
  [2]: https://www.python.org/downloads/windows/
  [3]: http://aka.ms/vcpython27
  [Microsoft Web Platform Installer]: http://www.microsoft.com/web/downloads/platform.aspx
  [Azure portal]: http://portal.azure.com
