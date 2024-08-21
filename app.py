from flask import Flask
from flask_restful import Resource, Api

app= Flask(__name__)
api= Api(app)

class Help(Resource):
    def get(self):
        help = {
            "Available REST APIs are ": ["/ping","/employee_info"] 
        }
        return help
    
class Ping(Resource):
    def get(self):
        status= {
            "status":"alive"
        }
        return status
    
class employee(Resource):
    def get(self):
       emp_info = {
    "emp1": {
        "name" : "abc",
        "salary": "10L"
    },
    "emp2" :  {
        "name" :"xyz",
        "salary":"14L"
    }
}
       return emp_info
    

api.add_resource(Help,"/")
api.add_resource(Ping,"/Ping")
api.add_resource(employee,"/employee")

app.run(port=5000,host="localhost")