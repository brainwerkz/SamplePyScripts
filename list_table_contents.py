#!/usr/local/bin/python3

import MySQLdb

connection = MySQLdb.connect(
                host = 'localhost',
                user = 'john',
                passwd = '****')  # create the connection

cursor = connection.cursor()

#choose databse to query
#dbase = raw_input('Please enter the name of the database you would like to query:')

cursor.execute("USE phpmyadmin") # select the database

cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

# execute SQL query using execute() method.
cursor.execute("select * from pma__users")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print(data)
 
#for row in data:
# uname = row[1]
# email = row[2]
# print "Name ",uname,"<br>"
# print "Website ",email,"<hr>"
# disconnect from server
connection.close()



