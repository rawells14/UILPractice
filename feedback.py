import os


def new_feedback(name, message):
    print(os.path.dirname('feedback.txt'))
    file = open('feedback.txt', "a")
    file.write(name + '  wrote:  ' + message + '\n'+'***********************************'+'\n\n')
    file.close()

new_feedback('Hello', 'Dank memes')