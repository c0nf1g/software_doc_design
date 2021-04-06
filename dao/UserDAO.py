from src.models.User import db, User
from utils.heplers import read_csv_data


class UserDAO:
    @classmethod
    def create_user(cls, apple_id):
        created_user = User(apple_id=apple_id)
        db.session.add(created_user)
        db.session.commit()

        return created_user

    @classmethod
    def get_user(cls, user_id=None, apple_id=None):
        if user_id is not None:
            user = User.query.filter_by(id=user_id).first()
            return user
        elif apple_id is not None:
            user = User.query.filter_by(apple_id=apple_id).first()
            return user
        else:
            return None

    @classmethod
    def read_csv_user(cls, filename):
        return read_csv_data(filename, ['email'], ['sub_type', 'price'])
