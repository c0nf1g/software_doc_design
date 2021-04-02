from src.models import db, User


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
