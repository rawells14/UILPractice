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
    badges =
    for i in q:

    if q is None:
        return False
    else:
        return True


def get_badges(uid):
    badges = []
    session = Session()
    q = session.query(Badge).filter(Badge.uid == uid).badgeids
    q_split = q.split(',')

    session.commit()
    session.close()


print(has_badge(1, 1))
