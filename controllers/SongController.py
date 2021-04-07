class SongController:
    def __init__(self, song_dao):
        self.song_dao = song_dao
        
    def create_song(self,
                    name,
                    duration,
                    artist,
                    album):
        return self.song_dao.create_song(
            name,
            duration,
            artist,
            album
        )
    
    def get_song(self, song_id):
        return self.song_dao.get_song(song_id)

    def get_songs(self):
        return self.song_dao.get_songs()

    def create_song_from_csv(self, filename):
        song_data = self.song_dao.read_song_from_csv(filename)
        song_header, song_values = song_data['Song']

        for song_value in song_values:
            self.song_dao.create_song_from_csv(
                song_header,
                song_value
            )
