from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

import mysql.connector

new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"  ,
    database= "newPython"
)

new_corsour= new_db.cursor()

app= Flask(__name__)
api= Api(app)

class Help(Resource):
    def get(self):
        help =  help = {
            "API available": ['/help',"/HVAC_info"]
        }
        return make_response(jsonify(help),200)  #404 is not found 
    
class HVAC_data(Resource):
    def get(self):
        new_corsour.execute("SELECT * FROM students")
        data= new_corsour.fetchall()
        for x in data:
           print(x)
        return make_response(jsonify(x),200)




api.add_resource(Help,"/api/v1/help")
api.add_resource(HVAC_data,"/api/v1/hvac")

app.run(debug=True,port=5000,host="localhost")