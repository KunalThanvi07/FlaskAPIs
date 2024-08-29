import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

new_sql= "INSERT INTO students (name, code) VALUES (%s,%s)"

# for the single entry
# values= ("Mishra","Frontend Developer")

# new_corsour.execute(new_sql, values)

# for many entry
values = [
    ("Asha", "JAVA developer"),
    ("Durga", "JAVA developer"),
    ("Yash", "DevOps developer"),
    ("Priyanka", "Frontend developer")
]

new_corsour.executemany(new_sql, values)

new_db.commit()
print(new_corsour.rowcount, "new record inserted")