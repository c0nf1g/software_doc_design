from src.models.PlaylistHasSong import db, PlaylistHasSong


class PlaylistHasSongDAO:
    @classmethod
    def create_association_playlist_song(cls, is_downloaded, stop_time):
        created_association = PlaylistHasSong(is_downloaded=is_downloaded,
                                              stop_time=stop_time)
        db.session.add(created_association)
        db.session.commit()

        return created_association
