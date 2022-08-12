from flask import Blueprint

hello_world_blueprint = Blueprint('hello_world_blueprint', __name__)

# Provide a route for the blueprint
@hello_world_blueprint.route('/')
def hello_world():
    return 'Hello World!'