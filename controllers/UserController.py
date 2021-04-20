from flask import render_template


class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def show_user(self, user_id):
        user = [self.user_service.get_user(user_id=user_id)]
        return render_template('user/user_list.html', users=user)

    def show_users(self):
        users = self.user_service.get_users()
        return render_template('user/user_list.html', users=users)

    def create_user(self, apple_id):
        user = self.user_service.create_user(apple_id=apple_id)
        return self.show_user(user.id)

    def update_user(self, user_id, apple_id):
        user = self.user_service.update_user(user_id=user_id, apple_id=apple_id)
        return self.show_user(user.id)

    def delete_user(self, user_id):
        user = self.user_service.delete_user(user_id=user_id)
        return self.show_user(user.id)

