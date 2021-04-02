from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    apple_id = db.Column('apple_id', db.String(45))
    subscription = db.relationship('Subscription', back_populates='user', uselist=False)
    playlists = db.relationship('Playlist', back_populates='user')


class SubscriptionType(db.Model):
    __tablename__ = 'subscription_type'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    price = db.Column('price', db.String(45))
    subscriptions = db.relationship('Subscription', back_populates='subscription_type')


class Subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column('id', db.Integer, primary_key=True)
    active_until = db.Column('active_until', db.Date)
    last_payment = db.Column('last_payment', db.Date)
    is_active = db.Column('is_active', db.Boolean)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False, unique=True)
    subscription_type_id = db.Column('subscription_type_id', db.Integer,
                                     db.ForeignKey('subscription_type.id'),
                                     nullable=False)

    subscription_type = db.relationship("SubscriptionType", back_populates="subscriptions")
    user = db.relationship("User", back_populates="subscription", uselist=False)


class Playlist(db.Model):
    __tablename__ = 'playlist'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship("User", back_populates="playlists")
    songs = db.relationship("PlaylistHasSong", back_populates="playlist")


class PlaylistHasSong(db.Model):
    __tablename__ = 'playlist_has_song'
    id = db.Column('id', db.Integer, primary_key=True)
    playlist_id = db.Column('playlist_id', db.Integer,
                            db.ForeignKey('playlist.id'),
                            primary_key=True)
    song_id = db.Column('song_id', db.Integer,
                        db.ForeignKey('song.id'),
                        primary_key=True)
    is_downloaded = db.Column('is_downloaded', db.Boolean)
    stop_time = db.Column('stop_time', db.Time)

    song = db.relationship("Song", back_populates="playlists")
    playlist = db.relationship("Playlist", back_populates="songs")


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    duration = db.Column('duration', db.Time)
    artist_id = db.Column('artist_id', db.Integer,
                          db.ForeignKey('artist.id'),
                          nullable=False)
    album_id = db.Column('album_id', db.Integer,
                         db.ForeignKey('album.id'),
                         nullable=False)
    playlists = db.relationship("PlaylistHasSong", back_populates="song")
    album = db.relationship("Album", back_populates="songs")
    artist = db.relationship("Artist", back_populates="songs")


class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    song_number = db.Column('song_number', db.Integer)
    duration = db.Column('duration', db.Time)
    artist_id = db.Column('artist_id', db.Integer,
                          db.ForeignKey('artist.id'),
                          nullable=False)
    songs = db.relationship('Song', back_populates="album")
    artist = db.relationship('Artist', back_populates="albums")


class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    creation_date = db.Column('creation_date', db.Date)
    albums = db.relationship('Album', back_populates='artist')
    songs = db.relationship('Song', back_populates="artist")
