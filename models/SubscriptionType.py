from . import db
from models.Base import Base


class SubscriptionType(db.Model, Base):
    __tablename__ = 'subscription_type'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    price = db.Column('price', db.String(45))
    subscriptions = db.relationship('Subscription', back_populates='subscription_type')

    def get_attrs(self):
        result = {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
        return result
