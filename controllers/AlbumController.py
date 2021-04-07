class AlbumController:
    def __init__(self, album_dao):
        self.album_dao = album_dao
        
    def create_album(self, 
                     name,
                     song_number,
                     duration,
                     artist):
        return self.album_dao.create_album(
            name,
            song_number,
            duration,
            artist
        )
    
    def get_album(self, album_id):
        return self.album_dao.get_album(album_id)

    def get_albums(self):
        return self.album_dao.get_albums()

    def create_album_from_csv(self, filename):
        album_data = self.album_dao.read_album_from_csv(filename)
        album_header, album_values = album_data['Album']

        for album_value in album_values:
            self.album_dao.create_album_from_csv(
                album_header,
                album_value
            )
