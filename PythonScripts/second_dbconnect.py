#!/usr/bin/python

import MySQLdb

server = input("What is the server name to which you wish to connect?")
user = input("What is the username you wish to use?")
dbase_pwd = input("What is the password")
# Open database connection
db = MySQLdb.connect(server, user, dbase_pwd,"phpmyadmin" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version: %s " % data)

# disconnect from server
db.close()
