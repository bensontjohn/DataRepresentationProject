# DataRepresentationProject

Course: Higher Diploma in Data Analytics, GMIT, Ireland
Module: Data Representation
Lecturer: Andrew Beatty
Author: Benson Thomas John
Email: G00376535@gmit.ie

## Project

Create a Web application in Flask that has a RESTful API to perform CRUD opeartions on a database table.

This repository contains the following files:

1. README.md file - Brief description about this repository.
2. requirements.txt - Specifies the python packages with versions required. 
3. server.py - Flask server.
4. orderDAO.py - Defines the CRUD operation which connects to an API.
5. testOrderDAO.py - Ti test the DAO.
6. index.html - Web interface to perfom CRUD operations that uses AJAX calls. Saved in the staticpages folder.
7. dbconfig.py - Contains configuration for database connection.

## How to download this repository and run files

Run the following on command prompt or cmder.

 - git clone git@github.com:bensontjohn/DataRepresentationProject.git

 - pip install -r requirements.txt

 - python server.py

Open the local host URL in a web browser.

http://127.0.0.1:5000/customerOrder - Displays the database contents in json format.

http://127.0.0.1:5000/index.html - Displays the 'Customer Order Display system' page with all the customer orders. 
You can add new order, update exisiting order and delete orders as well.


