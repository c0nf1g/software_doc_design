from models.Artist import db, Artist
from csv_module.generate_csv import read_from_csv


class ArtistDAO:
    def create_artist(self, artist_id, name, creation_date):
        created_artist = Artist(id=artist_id, name=name, creation_date=creation_date)
        db.session.add(created_artist)
        db.session.commit()
        return created_artist
    
    def get_artist(self, artist_id):
        artist = Artist.query.filter_by(id=artist_id).first()
        return artist

    def get_artists(self):
        artists = Artist.query.all()
        return artists

    def read_artist_from_csv(self, filename):
        return read_from_csv(filename, 'Artist')
    
    def create_artist_from_csv(self, artist_headers, artist_date):
        created_artist = Artist()
        created_artist.from_csv(artist_headers, artist_date)
        db.session.add(created_artist)
        db.session.commit()
