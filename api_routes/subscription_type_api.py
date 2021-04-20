from flask import Blueprint, jsonify
from init_layers import subscription_type_service

subscription_type = Blueprint("subscription_type", __name__)


@subscription_type.route('/subscription_types')
def get_subscription_types():
    subscription_types = subscription_type_service.get_sub_types()
    result = []

    for subscription_type in subscription_types:
        result.append(subscription_type.get_attrs())

    return jsonify(result)


@subscription_type.route('/subscription_types/<subscription_type_id>')
def get_subscription_type(subscription_type_id):
    subscription_type = subscription_type_service.get_sub_type(subscription_type_id)
    return jsonify(subscription_type.get_attrs())