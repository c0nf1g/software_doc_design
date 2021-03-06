class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, apple_id):
        return self.user_dao.create_user(apple_id=apple_id)

    def get_user(self, user_id):
        return self.user_dao.get_user(user_id)

    def get_users(self):
        return self.user_dao.get_users()

    def update_user(self, user_id, apple_id):
        return self.user_dao.update_user(user_id=user_id, apple_id=apple_id)

    def delete_user(self, user_id):
        return self.user_dao.delete_user(user_id=user_id)

    def create_user_from_csv(self, filename):
        user_data = self.user_dao.read_user_from_csv(filename)
        user_header, user_values = user_data['User']

        for user_value in user_values:
            self.user_dao.create_user_from_csv(
                user_header,
                user_value
            )
