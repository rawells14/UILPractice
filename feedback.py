import settings


def new_feedback(name, message):
    file = open(settings.PROJECT_PATH + 'feedback.txt', "a")
    file.write(
        name + '  wrote:  \n' + message + '\n' + '-------------------------------------------' + '\n\n' + '-------------------------------------------')
    file.close()