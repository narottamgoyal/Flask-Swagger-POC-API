from flask import Flask, Blueprint
from endpoints.CustomApp import ns as custom_namespace
from endpoints.TodoApp import ns as todo_namespace
from endpoints.restapi import api

app = Flask(__name__)
blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
api.add_namespace(custom_namespace)
api.add_namespace(todo_namespace)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
