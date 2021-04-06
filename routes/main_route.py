from flask import Blueprint
from src.domain.test import query_db

main = Blueprint("main", __name__)


@main.route('/')
def index():
    query_db()
    return "hello world"
