class PlaylistService:
    def __init__(self, playlist_dao):
        self.playlist_dao = playlist_dao

    def create_playlist(self, name, playlist):
        return self.playlist_dao.create_playlist(name, playlist)
        
    def get_playlist(self, playlist_id):
        return self.playlist_dao.get_playlist(playlist_id)

    def get_playlists(self):
        return self.playlist_dao.get_playlists()

    def create_playlist_from_csv(self, filename):
        playlist_data = self.playlist_dao.read_playlist_from_csv(filename)
        playlist_header, playlist_values = playlist_data['Playlist']

        for playlist_value in playlist_values:
            self.playlist_dao.create_playlist_from_csv(
                playlist_header,
                playlist_value
            )