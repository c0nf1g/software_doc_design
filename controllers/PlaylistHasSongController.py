class PlaylistHasSongController:
    def __init__(self, playlist_song_dao):
        self.playlist_song_dao = playlist_song_dao

    def add_song_to_playlist(self,
                             is_downloaded,
                             stop_time,
                             playlist,
                             song):
        return self.playlist_song_dao.create_association_playlist_song(
            is_downloaded,
            stop_time,
            playlist,
            song
        )

    def get_playlist_song_record(self, id):
        return self.playlist_song_dao.get_playlist_song_record(id)

    def get_playlist_song_records(self):
        return self.playlist_song_dao.get_playlist_song_records()

    def add_song_to_playlist_from_csv(self, filename):
        playlist_song_data = self.playlist_song_dao.read_playlist_song_from_csv(filename)
        playlist_song_header, playlist_song_values = playlist_song_data['PlaylistHasSong']

        for playlist_song_value in playlist_song_values:
            self.playlist_song_dao.create_playlist_song_from_csv(
                playlist_song_header,
                playlist_song_value
            )
