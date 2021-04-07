class SubscriptionTypeController:
    def __init__(self, subscription_type_dao):
        self.subscription_type_dao = subscription_type_dao
        
    def create_sub_type(self, name, price):
        return self.subscription_type_dao.create_subscription_type(name, price)
    
    def get_sub_type(self, sub_type_id):
        return self.subscription_type_dao.get_subscription_type(sub_type_id)

    def get_sub_types(self):
        return self.subscription_type_dao.get_subscription_types()

    def create_subscription_type_from_csv(self, filename):
        subscription_type_data = self.subscription_type_dao.read_subscription_type_from_csv(filename)
        subscription_type_header, subscription_type_values = subscription_type_data['SubscriptionType']

        for subscription_type_value in subscription_type_values:
            self.subscription_type_dao.create_subscription_type_from_csv(
                subscription_type_header,
                subscription_type_value
            )
