from src.models.Artist import db, Artist


class ArtistDAO:
    @classmethod
    def create_artist(cls, name, creation_date):
        created_artist = Artist(name=name, creation_date=creation_date)
        db.session.add(created_artist)
        db.session.commit()

        return created_artist
