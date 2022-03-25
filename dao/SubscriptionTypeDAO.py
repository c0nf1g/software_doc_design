from models.SubscriptionType import db, SubscriptionType
from csv_module.generate_csv import read_from_csv


class SubscriptionTypeDAO:
    def create_subscription_type(self, sub_type_id, name, price):
        created_subscription_type = SubscriptionType(id=sub_type_id, name=name, price=price)
        db.session.add(created_subscription_type)
        db.session.commit()

        return created_subscription_type

    def get_subscription_type(self, sub_type_id):
        sub_type = SubscriptionType.query.filter_by(id=sub_type_id).first()
        return sub_type

    def get_subscription_types(self):
        sub_types = SubscriptionType.query.all()
        return sub_types

    def read_subscription_type_from_csv(self, filename):
        return read_from_csv(filename, 'SubscriptionType')

    def create_subscription_type_from_csv(self, subscription_type_headers, subscription_type_data):
        created_subscription_type = SubscriptionType()
        created_subscription_type.from_csv(subscription_type_headers, subscription_type_data)
        db.session.add(created_subscription_type)
        db.session.commit()
