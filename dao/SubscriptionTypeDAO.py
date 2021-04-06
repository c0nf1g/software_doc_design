from src.models.SubscriptionType import db, SubscriptionType
from utils.heplers import read_csv_data


class SubscriptionTypeDAO:
    @classmethod
    def create_subscription_type(cls, name, price):
        created_subscription_type = SubscriptionType(name=name, price=price)
        db.session.add(created_subscription_type)
        db.session.commit()

        return created_subscription_type

    @classmethod
    def get_subscription_type(cls, sub_id=None, name=None):
        if sub_id is not None:
            subscription = SubscriptionType.query.filter_by(id=sub_id).first()
            return subscription
        elif name is not None:
            subscription = SubscriptionType.query.filter_by(name=name).first()
            return subscription
        else:
            return None

    @classmethod
    def read_csv_sub_type(cls, filename):
        return read_csv_data(filename, ['sub_type', 'price'], ['artist', 'creation_date'])
