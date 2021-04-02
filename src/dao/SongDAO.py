from src.models import db, Song


class SongDAO:
    @classmethod
    def create_song(cls, name, duration,
                    artist_id, album_id):
        created_song = Song(name=name, duration=duration,
                            artist_id=artist_id, album_id=album_id)
        db.session.add(created_song)
        db.session.commit()

        return created_song
