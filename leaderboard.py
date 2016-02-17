from decimal import Decimal
from db_interaction import Session, get_all_users


def get_top_ten_score():
    users = get_all_users().all()
    usernames = []
    scores = []
    for i in range(10):
        usernames.append(users[i].username)
        scores.append(int(Decimal((users[i].score))))
    data = [usernames, scores]
    return data

def get_top_ten_accuracy():
    return