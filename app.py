from flask import Flask
from extensions import db

# routes

from routes.main_route import main
from routes.user_route import user
from routes.csv_route import csv
from routes.song_route import song
from routes.subscription_type_route import subscription_type
from routes.subscription_route import subscription
from routes.artist_route import artist
from routes.album_route import album
from routes.playlist_route import playlist
from routes.playlist_song_route import playlist_song


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@127.0.0.1:3306/apple_music"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_routes(app)

    return app


def register_routes(app):
    app.register_blueprint(main)
    app.register_blueprint(csv)
    app.register_blueprint(user)
    app.register_blueprint(song)
    app.register_blueprint(subscription_type)
    app.register_blueprint(subscription)
    app.register_blueprint(artist)
    app.register_blueprint(album)
    app.register_blueprint(playlist)
    app.register_blueprint(playlist_song)


if __name__ == '__main__':
    app = create_app()
    app.run()
