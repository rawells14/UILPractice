import random
import time

from werkzeug.security import generate_password_hash, check_password_hash

from models import *
import settings











# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

data_base_address = settings.DB_ADDRESS
if settings.OS == 'W':
    engine = create_engine(data_base_address, echo=False)
else:
    engine = create_engine(data_base_address, echo=False, pool_size=20, max_overflow=0, pool_recycle=3600)
# add on to production

Session = sessionmaker(bind=engine)


def new_submission(uid, status):
    session = Session()
    t = time.time()
    sub = Submission(uid=uid, status=status, time_stamp=(int)(t))
    session.add(sub)
    session.commit()
    session.close()


def create_user(uname, full, pwd):
    session = Session()
    u = User(username=uname, fullname=full, password=generate_password_hash(pwd), score=0, totalattempted=0,
             totalcorrect=0, settings='')
    session.add(u)
    session.commit()
    session.close()


def get_all_users():
    session = Session()
    list = session.query(User).order_by(User.score.desc())
    session.close()
    return list


def users_by_accuracy():
    session = Session()
    list = session.query(User).order_by((User.totalcorrect * 100 / User.totalattempted).desc())
    session.close()
    return list


def compute_rank(user):
    users = get_all_users()
    rank = -1
    values = []
    value = 0
    for i in users:
        if i.username == user.username:
            value = i.score
        values.append(i.score)
    for i in range(len(values)):
        if values[i] == value:
            return i + 1
    return rank


def get_user_by_username(username):
    session = Session()
    u = session.query(User).filter(User.username == username).first()
    session.close()
    return u


def search_by_username(username):
    session = Session()
    users = session.query(User).filter(User.username.contains(username))
    session.close()
    return users


def get_user_by_uid(uid):
    session = Session()
    uid = int(uid)
    session.close()
    return session.query(User).filter(User.uid == uid).first()


def is_taken(username):
    username = username.lower()
    session = Session()
    q = session.query(User).filter(User.username == username).first()
    session.close()
    return not (q is None)


def is_valid(u, p):
    session = Session()
    user = session.query(User).filter(User.username == u.lower()).first()
    if (check_password_hash(user.password, p)):
        session.close()
        return True
    session.close()
    return False


def correct_and_total_num(username):
    u = get_user_by_username(username)
    data = []
    data.append(u.totalcorrect)
    data.append(u.totalattempted)
    return data


def incorrect(user, qid):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})
    session.query(User).filter(User.username == user.username).update({User.settings: 'Last: ' + qid})
    session.commit()
    session.close()
    new_submission(user.uid, 'i')
    from badge_system import award_badges

    award_badges(user.uid)


def correct(user, qid):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalcorrect: User.totalcorrect + 1})
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})
    session.query(User).filter(User.username == user.username).update({User.settings: 'Last: ' + qid + '|'})
    session.commit()
    session.close()
    new_submission(user.uid, 'c')
    from badge_system import award_badges

    award_badges(user.uid)


def get_random_question(subject):
    session = Session()
    matching_subject = session.query(Question).filter(Question.subject == subject)
    row_count = matching_subject.count()
    rnd = random.randint(0, row_count - 1)
    session.close()
    return matching_subject[rnd]


def get_question_by_qid(qid):
    session = Session()
    question = session.query(Question).filter(Question.qid == qid).first()
    session.close()
    return question


def add_question(questionheader, questiontext, answerchoices, correctanswer, explanation, subject):
    session = Session()
    question = Question(questionheader=questionheader, questiontext=questiontext, answerchoices=answerchoices,
                        correctanswer=correctanswer, explanation=explanation, subject=subject)
    session.add(question)
    session.commit()
    session.close()


def update_question(questionid, questionheader, questiontext, answerchoices, correctanswer, explanation, subject):
    session = Session()
    session.query(Question).filter(Question.qid == questionid).update({Question.questionheader: questionheader})
    session.query(Question).filter(Question.qid == questionid).update({Question.questiontext: questiontext})
    session.query(Question).filter(Question.qid == questionid).update({Question.answerchoices: answerchoices})
    session.query(Question).filter(Question.qid == questionid).update({Question.correctanswer: correctanswer})
    session.query(Question).filter(Question.qid == questionid).update({Question.explanation: explanation})
    session.query(Question).filter(Question.qid == questionid).update({Question.subject: subject})
    session.commit()
    session.close()


def get_last_question(user):
    str = user.settings
    if str is None or '':
        return
    settings = str.split('|')
    question_id = settings[0].replace('Last: ', '')
    if question_id == '':
        return
    return (int)(question_id)


def get_table_amts():
    session = Session()
    data = []
    data.append(session.query(User.uid).count())
    data.append(session.query(Question.qid).count())
    data.append(session.query(Question).filter(Question.subject == 'cs').count())
    data.append(session.query(Question).filter(Question.subject == 'math').count())
    data.append(session.query(Submission.uid).count())
    total_flags = 0
    for i in session.query(Flag):
        total_flags += i.flags
    session.close()
    data.append(total_flags)
    return data


def flag_question(qid):
    session = Session()
    if session.query(Flag).filter(Flag.qid == qid).count() == 0:
        session.add(Flag(qid=qid, flags=1))
    else:
        session.query(Flag).filter(Flag.qid == qid).update({Flag.flags: Flag.flags + 1})
    session.commit()
    session.close()


def get_top_flagged():
    session = Session()
    q = session.query(Flag).order_by(Flag.flags)
    flags = [[]]
    for flag in q:
        qid = flag.qid
        amt = flag.flags
        flags.append([qid, amt])
    flags.reverse()
    session.commit()
    session.close()
    return flags[:5]


def clear_flags():
    session = Session()
    session.query(Flag).delete()
    session.commit()
    session.close()


def is_moderator(u):
    username = u.username
    moderators = []
    f = open(settings.PROJECT_PATH + 'moderators.txt', mode='r')
    lines = f.readlines()
    for line in lines:
        moderators.append(line.split('\n')[0])
    for m in moderators:
        if m == username:
            return True
    return False


Base.metadata.create_all(engine)
