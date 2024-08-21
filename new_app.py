from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

app= Flask(__name__)
api= Api(app)

class Help(Resource):
    def get(self):
        help = {
            "API available": ['/help',"/Emp_info"]
        }
        return make_response(jsonify(help),404)  #404 is not found 
    

api.add_resource(Help,"/help")

app.run(debug=True,port=5000,host="localhost")

