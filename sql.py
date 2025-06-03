import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmed@516"
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS ah07")
print("Database created successfully!")
cursor.close()
mydb.close()

import mysql.connector

# Connect with database specified
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmed@516",
    database="my_database"  # Replace with your actual database name
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

cursor.close()
mydb.close()


import mysql.connector
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="project")
con=connect_db()
cur=cun.cursor()
cur.execute("create database project")
con.commit()
cur.close()
con.close()