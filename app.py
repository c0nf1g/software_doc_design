from flask import Flask
from extensions import db
from api_routes import api
from routes import main, user, song
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@127.0.0.1:3306/apple_music"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Bootstrap(app)

    register_routes(app)

    return app


def register_routes(app):
    app.register_blueprint(api)
    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(song)


if __name__ == '__main__':
    app = create_app()
    app.run()
