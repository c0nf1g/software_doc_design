from src.models import db, SubscriptionType


class SubscriptionTypeDAO:
    @classmethod
    def create_subscription_type(cls, name, price):
        created_subscription_type = SubscriptionType(name=name, price=price)
        db.session.add(created_subscription_type)
        db.session.commit()

        return created_subscription_type

    @classmethod
    def get_subscription_type(cls, sub_id=None, name=None, price=None):
        if sub_id is not None:
            subscription = SubscriptionType.query.filter_by(id=sub_id).first()
            return subscription
        elif name is not None:
            subscription = SubscriptionType.query.filter_by(name=name).first()
            return subscription
        elif price is not None:
            subscription = SubscriptionType.query.filter_by(price=price).first()
            return subscription
        else:
            return None
