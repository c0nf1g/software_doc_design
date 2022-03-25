from . import db
from models.Base import Base


class Playlist(db.Model, Base):
    __tablename__ = 'playlist'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship("User", back_populates="playlists")
    songs = db.relationship("PlaylistHasSong", back_populates="playlist")

    def get_attrs(self):
        result = {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }
        return result
