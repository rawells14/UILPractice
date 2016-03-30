from decimal import Decimal
from db_interaction import Session, get_all_users, users_by_accuracy
from models import Badge


def add_badge(uid, bid):
    bid = (str)(bid)
    session = Session()
    if (has_badge(uid, bid)):
        session.close()
        return
    else:
        session.query(Badge).filter(Badge.uid == uid).update(
            {Badge.badgeids: (Badge.badgeids + ',' + bid)})
    session.commit()
    session.close()


def has_badge(uid, bid):
    badges = get_badges(uid)
    for b in badges:
        if (b == bid):
            return True
    return False


def get_badges(uid):
    badges = []
    session = Session()
    q = session.query(Badge).filter(Badge.uid == uid)
    amt = q.count()
    if amt < 1:
        b = Badge(uid=uid, badgeids='')
        session.add(b)
        session.commit()
    q = q.first().badgeids
    q_split = q.split(',')
    for b in q_split:
        badges.append(b)
    session.commit()
    session.close()
    return badges


add_badge(1, 3)
print(get_badges(1))
