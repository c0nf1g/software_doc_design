from flask import Blueprint, jsonify
from init_layers import subscription_service

subscription = Blueprint("subscription", __name__)


@subscription.route('/subscriptions')
def get_subscriptions():
    subscriptions = subscription_service.get_subscriptions()
    result = []

    for subscription in subscriptions:
        result.append(subscription.get_attrs())

    return jsonify(result)


@subscription.route('/subscriptions/<subscription_id>')
def get_subscription(subscription_id):
    subscription = subscription_service.get_subscription(subscription_id)
    return jsonify(subscription.get_attrs())