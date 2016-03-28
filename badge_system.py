from decimal import Decimal
from db_interaction import Session, get_all_users, users_by_accuracy
from models import Badge


def add_badge(uid, bid):
    session = Session()
    if (not (has_badge(uid, bid))):
        print('s')
    session.commit()
    session.close()


def has_badge(uid, bid):
    session = Session()
    q = session.query(Badge).filter(Badge.uid == uid and Badge.bid == bid).first()
    session.commit()
    session.close()
    if q is None:
        return False
    else:
        return True


print(has_badge(1, 1))
