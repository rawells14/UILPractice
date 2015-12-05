def new_feedback(name, message):
    file = open('feedback.txt', "a")
    file.write(name + '  wrote:  ' + message + '\n'+'***********************************'+'\n\n')
    file.close()