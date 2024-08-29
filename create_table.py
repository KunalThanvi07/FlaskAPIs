import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_cursor= new_db.cursor()

# new_cursor.execute("CREATE TABLE students (name VARCHAR(255), code VARCHAR(255))")

# print("table created sucessfully")

new_cursor.execute("SHOW TABLES")

for x in new_cursor:
    print(x)