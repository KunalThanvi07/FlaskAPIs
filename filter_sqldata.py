import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

new_sql= "SELECT * FROM students WHERE code = 'Frontend developer'"

new_corsour.execute(new_sql)
data= new_corsour.fetchall()
for x in data:
    print(x)