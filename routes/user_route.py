from flask import Blueprint, jsonify
from init_controllers import user_controller

user = Blueprint("user", __name__)


@user.route('/users')
def get_users():
    users = user_controller.get_users()
    result = []

    for user in users:
        result.append(user.get_attrs())

    return jsonify(result)


@user.route('/users/<user_id>')
def get_user(user_id):
    user = user_controller.get_user(user_id)
    return jsonify(user.get_attrs())