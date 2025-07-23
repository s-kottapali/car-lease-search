#created a client and server file, server being made from flask backend which is a web framework for python
#created a python virtual environment using python -m venv venv, this is so the version of flask being used doesn't affect future projects and dependencies
#once the virtual environment is created I useed venv\Scripts\activate to activate the virtual environment
#I then used pip install flask to install flask
#Once flask was installed i used pip freeze > requirements.txt to create a file that showed the dependencies i used for this project

#I now created an app.py file
#In the file I imported Flask to build the web server and handle requests and jsonify which converts python lists/dictionaries into JSON responses for the browser or front end

#JSON stands for JavaScript Object Notation, its a lightweight data format used to send and recieve data between a backend like Flask and a front end like react, or between two systems.

#An API = Application Programming Interface, is is a way for one piece of siftware to talk to another, it defines how you can ask for data, send data, or control something remotely.
#REST API stands for representational State Transfer, A REST API is a web-based API that follows specific rules to organize and share data using the internet 
#HTTP methods like GET, POST, PUT, DELETE
#URLs(routes) to access specific pieces of data
#JSON to send data back and forth
