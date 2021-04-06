from . import db
from models.Base import Base


class PlaylistHasSong(db.Model, Base):
    __tablename__ = 'playlist_has_song'
    id = db.Column('id', db.Integer, primary_key=True)
    playlist_id = db.Column('playlist_id', db.Integer,
                            db.ForeignKey('playlist.id'),
                            primary_key=True)
    song_id = db.Column('song_id', db.Integer,
                        db.ForeignKey('song.id'),
                        primary_key=True)
    is_downloaded = db.Column('is_downloaded', db.Boolean, default=True)
    stop_time = db.Column('stop_time', db.Time)

    song = db.relationship("Song", back_populates="playlists")
    playlist = db.relationship("Playlist", back_populates="songs")

    def get_attrs(self):
        result = {
            'id': self.id,
            'playlist_id': self.playlist_id,
            'song_id': self.song_id,
            'is_downloaded': self.is_downloaded,
            'stop_time': self.stop_time
        }
        return result
