# Terminalfour Web Services API Python Package

This repo contains a python package that I created to interact with the [Terminalfour Web Services API](https://docs.terminalfour.com/documentation/developer-resources/up-and-running-with-the-web-services-api/). The Web Services API is useful for working around issues that clients run into while using the user interface, and this package makes using it easier and more intuitive.

## Additional Notes
This is an early version of the python package, and the real version of this package is larger and is maintained in our support engineering Gitlab repo. This version includes the connect module, which is used to instantiate a terminalfour object and then connect to a terminalfour instance. It also includes a few additional modules that contain the first API calls that I created after the connect module was finished and a couple of scripts in the parent directory (including main.py) that use the functions from those modules to perform various tasks.

The main.py file can be utilized as a template and modified to perform the task you are trying to get done. For example, often times users will delete sections without deleting the content in them first. This creates 'orphaned' content items, and while you can select multiple items in the user interface and purge them, some of our larger clients end up with thousands of orphaned content items, and deleting them through the user interface would take too long. The current code that I've included makes use of our [purge endpoint](https://webapi.terminalfour.com/new/#/Content/purgeContent) and can be used to permanently delete thousands of orphaned content items at once.

The section_publish method (currently commented out) is another one of the first calls that I created for a client. That one enables you to publish an individual section or branch, and can be used in conjunction with the cron utility (or task manager if you are on Windows) to schedule a section / branch publish since you can only schedule a channel publish through our UI, and there are some clients that have certain pages that they want to prioritize.

These are just a couple of examples that demonstrate what this package can do, and there are many other ways in which this package can be used to help clients solve some of the problems they are facing and work around UI limitations. One of the main benefits of using a package like this is it becomes much easier and more intuitive for clients to interact with our API. For example, if you wanted to iterate over a list of media ids and return their name you can just do this:
	for id in ids:\
	```python 
		output_json = terminalfour.get_media(t4_url, t4.access_token, t4.jsession_id, id)  
		print(output_json['name'])
	```
however the code needed to do this would be much longer without the get_media function. A more useful example of this function can be found in the [media_report.py](https://github.com/bjohnson11719/Terminalfour-API-Client/blob/main/media_report.py) file, which is a script that I wrote to create a custom media file report for a client. Reusability and increased collaboration and knowledge-sharing are other key benefits to using a package like to interact with an API.