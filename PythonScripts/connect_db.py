import MySQLdb

connection = MySQLdb.connect(
                host = 'localhost',
                user = 'john',
                passwd = '***')  # create the connection

cursor = connection.cursor()     # get the cursor

cursor.execute("USE test") # select the database

cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

for (table_name,) in cursor:
    print(table_name)


connection.close()
