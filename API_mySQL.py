from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
import mysql.connector

# Establishing connection with the MySQL database
new_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="newPython"
)

new_cursor = new_db.cursor()

app = Flask(__name__)
api = Api(app)

# Defining the Help resource
class Help(Resource):
    def get(self):
        help_data = {
            "API available": ['/help', "/HVAC_info"]
        }
        return make_response(jsonify(help_data), 200)

# Defining the HVAC_data resource
class HVAC_data(Resource):
    def get(self):
        new_cursor.execute("SELECT * FROM students")
        data = new_cursor.fetchall()
        
        # Converting the list of tuples into a list of dictionaries
        response_data = [
            {"name": row[0], "job_title": row[1], "id": row[2]}
            for row in data
        ]
        
        return make_response(jsonify(response_data), 200)

# Adding routes for the APIs
api.add_resource(Help, "/api/v1/help")
api.add_resource(HVAC_data, "/api/v1/hvac")

# Running the Flask application
app.run(debug=True, port=5000, host="localhost")
