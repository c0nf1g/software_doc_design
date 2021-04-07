from . import db
from models.Base import Base


class Album(db.Model, Base):
    __tablename__ = 'album'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    song_number = db.Column('song_number', db.Integer)
    duration = db.Column('duration', db.Time)
    artist_id = db.Column('artist_id', db.Integer,
                          db.ForeignKey('artist.id'),
                          nullable=False)
    songs = db.relationship('Song', back_populates="album")
    artist = db.relationship('Artist', back_populates="albums")

    def get_attrs(self):
        result = {
            'id': self.id,
            'name': self.name,
            'song_number': self.song_number,
            'duration': self.duration.strftime('%H:%M:%S'),
            'artist_id': self.artist_id
        }
        return result
