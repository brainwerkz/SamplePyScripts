import MySQLdb

server = input("What is the server name to which you wish to connect?")
username = input("What is the username you wish to use?")
dbase_pwd = input("What is the password")
connection = MySQLdb.connect(
                host = server,
                user = username,
                passwd = dbase_pwd)  # create the connection

cursor = connection.cursor()     # get the cursor

cursor.execute("USE test") # select the database

cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

for (table_name,) in cursor:
    print(table_name)


connection.close()
