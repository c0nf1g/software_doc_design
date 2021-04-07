from controllers import *
from dao import *

user_dao = UserDAO()
album_dao = AlbumDAO()
artist_dao = ArtistDAO()
playlist_dao = PlaylistDAO()
playlist_song_dao = PlaylistHasSongDAO()
song_dao = SongDAO()
subscription_dao = SubscriptionDAO()
subscription_type_dao = SubscriptionTypeDAO()

user_controller = UserController(user_dao)
album_controller = AlbumController(album_dao)
artist_controller = ArtistController(artist_dao)
playlist_controller = PlaylistController(playlist_dao)
playlist_song_controller = PlaylistHasSongController(playlist_song_dao)
song_controller = SongController(song_dao)
subscription_controller = SubscriptionController(subscription_dao)
subscription_type_controller = SubscriptionTypeController(subscription_type_dao)


def create_all_from_csv(path):
    user_controller.create_user_from_csv(path)
    artist_controller.create_artist_from_csv(path)
    subscription_type_controller.create_subscription_type_from_csv(path)
    subscription_controller.create_subscription_from_csv(path)
    album_controller.create_album_from_csv(path)
    playlist_controller.create_playlist_from_csv(path)
    song_controller.create_song_from_csv(path)
    playlist_song_controller.add_song_to_playlist_from_csv(path)
