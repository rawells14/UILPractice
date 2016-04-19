import settings


def new_feedback(name, message):
    file = open(settings.PROJECT_PATH + 'feedback.txt', 'a')
    file.write(
        name + ' wrote:\n\n' + message + '\n----------------------------------------------------------------\n')
    file.close()


def clear_feedback():
    file = open(settings.PROJECT_PATH + 'feedback.txt', 'w')
    file.write('')
    file.close()

