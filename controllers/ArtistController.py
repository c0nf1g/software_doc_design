class ArtistController:
    def __init__(self, artist_dao):
        self.artist_dao = artist_dao

    def create_artist(self, name, creation_date):
        return self.artist_dao.create_artist(name, creation_date)

    def get_artist(self, artist_id):
        return self.artist_dao.get_artist(artist_id)
    
    def create_artist_from_csv(self, filename):
        artist_data = self.artist_dao.read_artist_from_csv(filename)
        artist_header, artist_values = artist_data['Artist']

        for artist_value in artist_values:
            self.artist_dao.create_artist_from_csv(
                artist_header,
                artist_value
            )
