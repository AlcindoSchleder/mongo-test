# mongo-test
A django app that use CRUD with mongoDB  and other operations

This application use advanced Django features like:
- Djongo library to create CRUD (**C**reate, **R**ead, **U**pdate and **D**elete). The library translates the sql commands generated from the django ORM to the mongoDB commands, maintaining the same programming structure as relational databases.
- Techniques on how to use http PUT, PATH and DELETE methods creating middleware for this task and configuring a CBV (**C**lass **B**ased **V**iew) to use all verbs in the same class.
- **Javascript** interacting directly with the django application with popup's for registering auxiliary tables, as well as django sends the javascript scripts to the frontend working in sync
- Manipulation of templates with **"regroup"** resources to generate a table in HTML with resources for grouping records.
- Use of post-save signals to generate film scores. This feature in relational databases, or even NoSQL like MongoDB, would be done directly in a trigger after insert, making the client application lighter, since the data processing will be done in the core of the database that is usually on a powerful server. But in this case, I wanted to implement this signaling functionality to demonstrate the power of the Django framework, even because, a direct implementation in the database would go unnoticed in the application code. The trigger results magically appear in the affected tables.

## Packages

* django==2.2.11 - Dependence of djongo
* django-static-fontawesome==5.12.1.4 - A collection web icons 
* djongo==1.3.1 - MongoDB engine for Django 2.2
* python-decouple==3.3 - To get environments variables

### Install

1. Install MongoDB on a server;
1. Clone this app;
   ```shell script
   git clone https://github.com/AlcindoSchleder/mongo-test.git
   cd mongo-test
   ```
1. Create a python virtual environment;
   ```shell script
   python3 -m venv venv
   ```
1. Enter on your python virtual machine;
   ```shell script
   on linux/mac:
   ./venv/bin/activate
   on windows:
   venv\Scripts\activate
   ```
1. Install all application dependencies;
   ```shell script
   pip install -r requirements.txt
   ```
1. Execute django migrate to create database, and tables to store all documents;
   ```shell script
   pyhton manage.py migrate 
   ```
1. Execute django server:
   ```shell script
   python manage.py runserver
   ```
1. Open your app on a browser on link showing to your installation. Note that if you are run django on remove server, you must to inform django the address and port to runserver comand:
   ```shell script
   python manage.py runserver 0.0.0.0:8000
   ```
   Now your django server listen connection to any server interface on port 8000.
   Don't forget add this to ALLOWED_HOSTS at settings.py.

This installation task would be much easier and faster using docker, but I have no patience with docker and my machine does not support so many features, and I have other more important applications for python development which is my focus.
So if someone in the community is interested in including the docker scripts I will be very happy to publish it.
