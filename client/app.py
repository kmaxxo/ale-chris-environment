import os
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from service import ToDoService

import json

app = Flask(__name__)
socketio = SocketIO(app)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/<name>")
def hello_name(name):
    return render_template('index.html', name=name)


@app.route("/todo", methods=['GET', 'POST'])
def list_todo():

    # POST: Sign user in
    if request.method == 'POST':
        # Get Form Fields
        sendTodo = {}
        sendTodo['title'] = request.form.get('item')

        result = ToDoService().create(sendTodo)

        return render_template('feedback/thanks.html', name_item=result)

    result = ToDoService().list()

    return render_template('form.html', result=result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8888))
    socketio.run(app, debug=True, host='0.0.0.0', port=port)
