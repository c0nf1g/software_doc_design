from . import db
from models.Base import Base


class Artist(db.Model, Base):
    __tablename__ = 'artist'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    creation_date = db.Column('creation_date', db.Date)
    albums = db.relationship('Album', back_populates='artist')
    songs = db.relationship('Song', back_populates="artist")

    def get_attrs(self):
        result = {
            'id': self.id,
            'name': self.name,
            'creation_date': self.creation_date
        }
        return result
