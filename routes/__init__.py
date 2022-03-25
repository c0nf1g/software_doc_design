from flask import Blueprint

main = Blueprint("main", __name__)
user = Blueprint("user", __name__)
song = Blueprint("song", __name__)

from . import main_route, user_route, song_route
