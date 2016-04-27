from db_interaction import *


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
            continue
        badges.append((int)(b))
    session.commit()
    session.close()
    return badges


# Main Badge Award System
def award_badges(uid):
    badge_0(uid)
    badge_1(uid)
    badge_2(uid)
    badge_3(uid)
    badge_4(uid)


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


# Badge ID - 1
# Awards the badge if the user has answered 25 questions correctly
def badge_1(uid):
    session = Session()
    session = Session()
    u = get_user_by_uid(uid)
    total_correct = u.totalcorrect
    if total_correct >= 25:
        add_badge(uid, 1)
    session.commit()
    session.close()


# Badge ID - 2
# Awards the badge if the user has answered 50 questions correctly
def badge_2(uid):
    session = Session()
    session = Session()
    u = get_user_by_uid(uid)
    total_correct = u.totalcorrect
    if total_correct >= 50:
        add_badge(uid, 2)
    session.commit()
    session.close()


# Badge ID - 3
# Awards the badge if the user has answered 100 questions correctly
def badge_3(uid):
    session = Session()
    session = Session()
    u = get_user_by_uid(uid)
    total_correct = u.totalcorrect
    if total_correct >= 100:
        add_badge(uid, 3)
    session.commit()
    session.close()


# Badge ID - 4
# Awards the badge if the user has answered 250 questions correctly
def badge_4(uid):
    session = Session()
    session = Session()
    u = get_user_by_uid(uid)
    total_correct = u.totalcorrect
    if total_correct >= 250:
        add_badge(uid, 4)
    session.commit()
    session.close()


def get_badge_names():
    names = []
    f = open(settings.PROJECT_PATH + 'BadgeNames.txt', mode='r')
    lines = f.readlines()
    for line in lines:
        names.append(line.split('\n')[0])
    f.close()
    return names
