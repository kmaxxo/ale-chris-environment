import requests
from flask import jsonify

apiEntrypoint = 'http://ace-server:8888'

class ToDoService:
    def create(self, params):
        response = requests.post(apiEntrypoint+"/todo", data = params).json()
        return response

    def list(self):
        #response = self.model.list_items()
        #return response
        response = requests.get(apiEntrypoint+"/todo").json()
        return response