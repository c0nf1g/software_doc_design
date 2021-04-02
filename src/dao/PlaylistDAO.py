from src.models import db, Playlist


class PlaylistDAO:
    @classmethod
    def create_playlist(cls, name, user_id):
        created_playlist = Playlist(name=name, user_id=user_id)
        db.session.add(created_playlist)
        db.session.commit()

        return created_playlist

