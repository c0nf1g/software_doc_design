from models.User import db, User
from csv_module.generate_csv import read_from_csv


class UserDAO:
    def create_user(self, apple_id, user_id=None):
        if user_id is None:
            created_user = User(apple_id=apple_id)
        else:
            created_user = User(id=user_id, apple_id=apple_id)
        db.session.add(created_user)
        db.session.commit()
        return created_user

    def get_user(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    def get_users(self):
        users = User.query.all()
        return users

    def update_user(self, user_id, apple_id):
        user = self.get_user(user_id=user_id)
        user.apple_id = apple_id
        db.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id=user_id)
        db.session.delete(user)
        db.session.commit()
        return user

    def read_user_from_csv(self, filename):
        return read_from_csv(filename, 'User')

    def create_user_from_csv(self, user_headers, user_data):
        created_user = User()
        created_user.from_csv(user_headers, user_data)
        db.session.add(created_user)
        db.session.commit()
