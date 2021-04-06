from src.models.Subscription import db, Subscription
from utils.heplers import read_csv_data


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
    
    @classmethod
    def read_csv_subscription(cls, filename):
        return read_csv_data(filename, 
                             ['active_until', 'last_payment', 'is_active', 'user', 'sub_type'],
                             ['album', 'song_number', 'duration', 'artist'])
