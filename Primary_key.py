import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

new_corsour.execute("CREATE TABLE clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), code VARCHAR(255))")

# new_corsour.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")