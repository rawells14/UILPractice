from decimal import Decimal
from db_interaction import Session, get_all_users, users_by_accuracy, get_user_by_uid
from models import Badge


def add_badge(uid, bid):
    bid = (str)(bid)
    session = Session()
    if (has_badge(uid, bid)):
        session.close()
        return
    else:
        to_change = session.query(Badge).filter(Badge.uid == uid).first().badgeids + ',' + bid
        session.query(Badge).filter(Badge.uid == uid).update(
            {Badge.badgeids: to_change})

    session.commit()
    session.close()


def has_badge(uid, bid):
    badges = get_badges(uid)
    for b in badges:
        if b == bid or (int)(b) == (int)(bid):
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
        if b == '':
            badges.append((int)(0))
            continue
        badges.append((int)(b))
    session.commit()
    session.close()
    return badges


# Main Badge Award System
def award_badges(uid):
    badge_0(uid)
    print('BADGE 0 - ' + (str)(uid))


# Badge ID - 0
# Awards badge 0 if a user has answered greater than 10 questions correctly
def badge_0(uid):
    session = Session()
    u = get_user_by_uid(uid)
    total_correct = u.totalcorrect
    if total_correct >= 10:
        add_badge(uid, 0)
    session.commit()
    session.close()


def get_badge_names():
    names = []
    with open('BadgeNames.txt') as f:
        names.append(f.read().splitlines())
    return names[0]


print(get_badge_names())