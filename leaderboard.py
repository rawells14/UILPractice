from decimal import Decimal
from db_interaction import Session, get_all_users, users_by_accuracy


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
    users = users_by_accuracy()
    usernames = []
    accuracies = []

    tot = 0
    for user in users:
        if (user.totalattempted > 10):
            usernames.append(user.username)
            accuracies.append((int)(100 * (user.totalcorrect / user.totalattempted)))
            tot += 1
        if (tot >= 10):
            break
    data = [usernames, accuracies]
    return data


print(get_top_ten_accuracy())
