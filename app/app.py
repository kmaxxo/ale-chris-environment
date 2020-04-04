import os
from flask import Flask, request, jsonify, make_response
from flask_socketio import SocketIO
from service import ToDoService
from modelsMongo import Schema
import json

app = Flask(__name__)
socketio = SocketIO(app)


@app.after_request
def add_headers(response):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return jsonify('{Hello World!}')


@app.route("/<name>")
def hello_name(name):

    todos = {}
    todos['saludo'] = name
    response = make_response( json.dumps(todos) )

    return response


@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.form))


if __name__ == "__main__":
    Schema()
    port = int(os.environ.get('PORT', 8888))
    socketio.run(app, debug=True, host='0.0.0.0', port=port)
