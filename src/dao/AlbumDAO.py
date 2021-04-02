from src.models import db, Album


class AlbumDAO:
    @classmethod
    def create_album(cls, name, song_number,
                     duration, artist_id):
        created_album = Album(name=name, song_number=song_number,
                              duration=duration, artist_id=artist_id)
        db.session.add(created_album)
        db.session.commit()

        return created_album
