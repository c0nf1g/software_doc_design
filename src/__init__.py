from flask import Flask
from src.routes.main_route import main
from src.routes.user_route import user
from src.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@127.0.0.1:3306/apple_music"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_routes(app)

    return app


def register_routes(app):
    app.register_blueprint(main)
    app.register_blueprint(user)
