class SubscriptionService:
    def __init__(self, subscription_dao):
        self.subscription_dao = subscription_dao
        
    def create_subscription(self, 
                            active_until,
                            last_payment,
                            is_active,
                            subscription,
                            subscription_type):
        return self.subscription_dao.create_subscription(
            active_until,
            last_payment,
            is_active,
            subscription,
            subscription_type)

    def get_subscription(self, sub_id):
        return self.subscription_dao.get_subscription(sub_id)

    def get_subscriptions(self):
        return self.subscription_dao.get_subscriptions()

    def create_subscription_from_csv(self, filename):
        subscription_data = self.subscription_dao.read_subscription_from_csv(filename)
        subscription_header, subscription_values = subscription_data['Subscription']

        for subscription_value in subscription_values:
            self.subscription_dao.create_subscription_from_csv(
                subscription_header,
                subscription_value
            )
