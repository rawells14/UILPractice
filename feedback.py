import settings


def new_feedback(fullname, username, message):
    file = open(settings.PROJECT_PATH + 'feedback.txt', 'a')
    file.write(
        fullname + '(' + username + ')' + '\n' + message + '\n----\n')
    file.close()


def clear_feedback():
    file = open(settings.PROJECT_PATH + 'feedback.txt', 'w')
    file.write('')
    file.close()


# returns feedback in the format: [[fullname(username), message....], [fullname(username), message....]]
def get_feedback():
    feedback = []
    f = open(settings.PROJECT_PATH + 'feedback.txt', mode='r')
    lines = f.readlines()
    current_feedback = []
    for line in lines:
        if line.split('\n')[0] == '----':
            feedback.append(current_feedback)
            current_feedback = []
        elif len(current_feedback) == 0 or len(current_feedback) == 1:
            current_feedback.append(line.split('\n')[0])
        else:
            current_feedback[1] = current_feedback[1] + line.split('\n')[0]
    return feedback


