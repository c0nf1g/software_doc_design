from flask import render_template, request
from init_layers import user_controller
from . import user


@user.route('/users_view', methods=['GET'])
def user_index():
    return render_template('user/user_index.html')


@user.route('/users_view/get', methods=['GET'])
def get_users():
    if request.args.get('id', None):
        user_id = int(request.args['id'])
        return user_controller.show_user(user_id=user_id)

    return user_controller.show_users()


@user.route('/users_view/post', methods=['POST'])
def create_user():
    apple_id = request.form.get('apple_id')
    return user_controller.create_user(apple_id=apple_id)


@user.route('/users_view/put', methods=['POST'])
def update_user():
    user_id = request.form.get('id')
    apple_id = request.form.get('apple_id')
    return user_controller.update_user(user_id=user_id, apple_id=apple_id)


@user.route('/user_view/delete', methods=['POST'])
def delete_user():
    user_id = request.form.get('id')
    return user_controller.delete_user(user_id=user_id)
