from flask import Flask , jsonify
from flask_restful import Resource, Api

app= Flask(__name__)
api= Api(app)



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

class Help(Resource):
    def get(self):
        help={
            "API available" : ["Help", "info","emp_info"]
        }
        return jsonify(help)
    

class employee(Resource):
    def get(self):

        return jsonify(emp_info) 

class Variable(Resource):
   def get(self,ename):
      return jsonify(emp_info.get(ename))
   


api.add_resource(Help,"/")
api.add_resource(employee,"/employee")
api.add_resource(Variable,"/employee/<string:ename>")

app.run(debug=True,port=5000,host="localhost")