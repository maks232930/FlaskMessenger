from flask import Blueprint

app_route = Blueprint('route', __name__)


@app_route.route('/')
def index():
    return '<h1>Hello World</h1>'

