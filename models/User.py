from . import db
from models.Base import Base


class User(db.Model, Base):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    apple_id = db.Column('apple_id', db.String(45))
    subscription = db.relationship('Subscription', back_populates='user', uselist=False)
    playlists = db.relationship('Playlist', back_populates='user')

    def get_attrs(self):
        result = {
            'id': self.id,
            'apple_id': self.apple_id
        }
        return result
