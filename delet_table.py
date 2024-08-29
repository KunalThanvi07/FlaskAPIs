import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

sql_command= "DROP TABLE IF EXISTS clients"

new_corsour.execute(sql_command)