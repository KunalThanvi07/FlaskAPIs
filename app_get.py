from flask import Flask
from flask_restful import Resource, Api

app_get= Flask(__name__)
api = Api(app_get) 

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

class employee(Resource):
    def get(self):
        return emp_info
    

api.add_resource(employee,"/info")

app_get.run(port=5000,host="localhost")