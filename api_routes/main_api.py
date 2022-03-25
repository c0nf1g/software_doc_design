from flask import Blueprint

main = Blueprint("main", __name__)


@main.route('/')
def index():
    return "This is LAB2 api"
