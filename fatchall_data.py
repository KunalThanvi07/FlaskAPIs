import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

new_corsour.execute("SELECT * FROM students")

# all record will be printed here

all_data= new_corsour.fetchall()
for x in all_data:
    print(x)

# only first record will get printed here

#data= new_corsour.fetchone()
#print(data)
