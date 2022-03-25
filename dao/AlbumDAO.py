from models.Album import db, Album
from csv_module.generate_csv import read_from_csv


class AlbumDAO:
    def create_album(self, album_id, name, song_number,
                     duration, artist_id):
        created_album = Album(id=album_id, 
                              name=name, 
                              song_number=song_number,
                              duration=duration, 
                              artist_id=artist_id)
        db.session.add(created_album)
        db.session.commit()

        return created_album
    
    def get_album(self, album_id):
        album = Album.query.filter_by(id=album_id).first()
        return album

    def get_albums(self):
        albums = Album.query.all()
        return albums
    
    def read_album_from_csv(self, filename):
        return read_from_csv(filename, 'Album')
    
    def create_album_from_csv(self, album_headers, album_data):
        created_album = Album()
        created_album.from_csv(album_headers, album_data)
        db.session.add(created_album)
        db.session.commit()
