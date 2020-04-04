import requests
from flask import jsonify

class ToDoService:
    def create(self, params):
        response = requests.post("http://ace-server:8888/todo", data = params).json()
        return response

    def list(self):
        #response = self.model.list_items()
        #return response
        response = requests.get("http://ace-server:8888/todo").json()
        return response