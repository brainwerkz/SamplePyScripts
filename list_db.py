#!/usr/bin/python3

import MySQLdb

connection = MySQLdb.connect(
                host = 'localhost',
                user = 'john',
                passwd = 'JEllen69!')  # create the connection

cursor = connection.cursor()     # get the cursor


#cursor.execute("USE information_schema") # select the database

cursor.execute("SHOW DATABASES")    # execute 'SHOW TABLES' (but data is not returned)

for (database_name,) in cursor:
        print(database_name)



# Close the connection
connection.close()
