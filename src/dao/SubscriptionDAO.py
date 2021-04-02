from src.models import db, Subscription


class SubscriptionDAO:
    @classmethod
    def create_subscription(cls, active_until, last_payment,
                            is_active, user, subscription_type):
        created_subscription = Subscription(active_until=active_until,
                                            last_payment=last_payment,
                                            is_active=is_active,
                                            user=user,
                                            subscription_type=subscription_type)
        db.session.add(created_subscription)
        db.session.commit()

        return created_subscription
