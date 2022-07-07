# Overview

I created a database using python and the build-in library SQLITE

The software i created possesses a database which contains 3 tables

I wrote this sofware in order to demonstrated how to use python and SQLite to manupulate and create database files.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](https://youtu.be/9QNlb9yYNEU)

# Relational Database

SQLite is a software library that provides a relational database management system. The lite in SQLite means lightweight in terms of setup, database administration, and required resources.
SQLite has the following noticeable features: self-contained, serverless, zero-configuration, transactional.}

## Table 1: Student Info table
The table contains 5 columns namely : student Id , fname, lname, and phone and email. 
The id is auto incremented.

## Table 2: emergency_contact Table
The table contains 4 columns namely: Id, parent or Tutor name, email and phone number.
The id is also autoincremented. 

## Table 3: student_gpa table
The table contains 3 columns namely: id, emergency_id 

# Development Environment

Visual Studio Code
SQLite3
Pyrhon3


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](https://docs.python.org/3.8/library/sqlite3.html)
* [Web Site Name](https://www.sqlitetutorial.net/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Retrieve student whose gpa is greater than 3.0
* apdate student information
* Delete gradute student data.