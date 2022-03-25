from flask import jsonify
from init_layers import user_service
from . import api


@api.route('/users')
def get_users():
    users = user_service.get_users()
    result = []

    for user in users:
        result.append(user.get_attrs())

    return jsonify(result)


@api.route('/users/<user_id>')
def get_user(user_id):
    user = user_service.get_user(user_id)
    return jsonify(user.get_attrs())
