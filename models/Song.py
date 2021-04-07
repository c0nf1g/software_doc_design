from datetime import datetime

from . import db
from models.Base import Base


class Song(db.Model, Base):
    __tablename__ = 'song'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    duration = db.Column('duration', db.Time)
    artist_id = db.Column('artist_id', db.Integer,
                          db.ForeignKey('artist.id'),
                          nullable=False)
    album_id = db.Column('album_id', db.Integer,
                         db.ForeignKey('album.id'),
                         nullable=False)
    playlists = db.relationship("PlaylistHasSong", back_populates="song")
    album = db.relationship("Album", back_populates="songs")
    artist = db.relationship("Artist", back_populates="songs")

    def get_attrs(self):
        result = {
            'id': self.id,
            'artist_id': self.artist_id,
            'album_id': self.album_id,
            'duration': self.duration.strftime('%H:%M:%S')
        }
        return result
