from services import *
from dao import *
from controllers import *

user_dao = UserDAO()
album_dao = AlbumDAO()
artist_dao = ArtistDAO()
playlist_dao = PlaylistDAO()
playlist_song_dao = PlaylistHasSongDAO()
song_dao = SongDAO()
subscription_dao = SubscriptionDAO()
subscription_type_dao = SubscriptionTypeDAO()

user_service = UserService(user_dao)
album_service = AlbumService(album_dao)
artist_service = ArtistService(artist_dao)
playlist_service = PlaylistService(playlist_dao)
playlist_song_service = PlaylistHasSongService(playlist_song_dao)
song_service = SongService(song_dao)
subscription_service = SubscriptionService(subscription_dao)
subscription_type_service = SubscriptionTypeService(subscription_type_dao)

user_controller = UserController(user_service)
song_controller = SongController(song_service)

def create_all_from_csv(path):
    user_service.create_user_from_csv(path)
    artist_service.create_artist_from_csv(path)
    subscription_type_service.create_subscription_type_from_csv(path)
    subscription_service.create_subscription_from_csv(path)
    album_service.create_album_from_csv(path)
    playlist_service.create_playlist_from_csv(path)
    song_service.create_song_from_csv(path)
    playlist_song_service.add_song_to_playlist_from_csv(path)
