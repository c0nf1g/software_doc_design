from src.dao.UserDAO import UserDAO
from src.dao.SubscriptionDAO import SubscriptionDAO
from src.dao.SubscriptionTypeDAO import SubscriptionTypeDAO
import datetime


def query_db():
    user = UserDAO.get_user(apple_id="orest@gmail.com")
    sub_type = SubscriptionTypeDAO.get_subscription_type(name="standard")
    SubscriptionDAO.create_subscription(
        active_until=datetime.date(2020, 1, 4),
        last_payment=datetime.date(2021, 3, 4),
        is_active=True,
        user=user,
        subscription_type=sub_type
    )

