import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  
)

print("Connected successfully")

new_cursor= new_db.cursor()

# new_cursor.execute("CREATE DATABASE newPython")
new_cursor.execute("SHOW DATABASES")

for n in new_cursor:
    print(n)


