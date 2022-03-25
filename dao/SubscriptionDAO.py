from models.Subscription import db, Subscription
from csv_module.generate_csv import read_from_csv


class SubscriptionDAO:
    def create_subscription(self, sub_id, active_until, last_payment,
                            is_active, user, subscription_type):
        created_subscription = Subscription(id=sub_id,
                                            active_until=active_until,
                                            last_payment=last_payment,
                                            is_active=is_active,
                                            user=user,
                                            subscription_type=subscription_type)
        db.session.add(created_subscription)
        db.session.commit()

        return created_subscription

    def get_subscription(self, sub_id):
        subscription = Subscription.query.filter_by(id=sub_id).first()
        return subscription

    def get_subscriptions(self):
        subscriptions = Subscription.query.all()
        return subscriptions

    def read_subscription_from_csv(self, filename):
        return read_from_csv(filename, 'Subscription')

    def create_subscription_from_csv(self, subscription_headers, subscription_data):
        created_subscription = Subscription()
        created_subscription.from_csv(subscription_headers, subscription_data)
        db.session.add(created_subscription)
        db.session.commit()
