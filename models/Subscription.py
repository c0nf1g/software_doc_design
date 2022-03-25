from . import db
from models.Base import Base


class Subscription(db.Model, Base):
    __tablename__ = 'subscription'
    id = db.Column('id', db.Integer, primary_key=True)
    active_until = db.Column('active_until', db.Date)
    last_payment = db.Column('last_payment', db.Date)
    is_active = db.Column('is_active', db.Boolean, default=True)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False, unique=True)
    subscription_type_id = db.Column('subscription_type_id', db.Integer,
                                     db.ForeignKey('subscription_type.id'),
                                     nullable=False)

    subscription_type = db.relationship("SubscriptionType", back_populates="subscriptions")
    user = db.relationship("User", back_populates="subscription", uselist=False)

    def get_attrs(self):
        result = {
            'id': self.id,
            'active_until': self.active_until,
            'last_payment': self.last_payment,
            'is_active': self.is_active,
            'user_id': self.user_id,
            'subscription_type_id': self.subscription_type_id
        }
        return result
