import random

def getAnswer(answerNum):
    if answerNum=='1':
        return 'It is certain'
    elif answerNum==2:
        return 'It is decidely so '

    elif answerNum == 3:
        return 'Please try again '
    elif answerNum == 4:
        return 'It is wrong '
    elif answerNum == 5:
        return 'Next '
    elif answerNum == 6:
        return 'random '

r=random.randint(1,6)
answer=getAnswer(r)
print(answer)