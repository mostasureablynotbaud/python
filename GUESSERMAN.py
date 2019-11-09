import random
Prompt = ('TAKE THOU SHOT')
QUIT = -1
QUIT_TXT = 'q'
QUIT_MSG = 'Fare thee well then'
CON_QUTI_MSG = 'Is thou certain of thine action?(Y/n)?'

def con_quit():
    spam = input(CON_QUIT_MSG)
    if spam == 'n':
        return False
    else:
        return True

def do_shot_round():
    """Choose a random number, ask the user to guess"""
    cpuNO = random.randint(0,9999)
    SHOTS = 0

    while True:
        Guesserman = input(Prompt)
        if Guesserman == QUIT_TXT:
                if con_quit():
                    return QUIT
                else:
                    continue
                SHOTS = SHOTS+1
        if cpuNO == int(Guesserman):
            print('CORRECT')
            return SHOTS
        elif cpuNO > int(Guesserman):
            print('UNDERSHOT')
        else:
            print('OVERSHOT')


total_rounds = 0
total_SHOTS = 0


while True:
    total_rounds = total_rounds+1
    print('ROUND'+str(total_rounds))
    print('START')
    thisround = do_shot_round()

    
    if thisround == QUIT:
          total_rounds = total_rounds - 1
          statsmsg = 'THOU COMPLETED NO ROUNDS.'+\
                         'I AWAIT THOU RETURN'

    else:
        statsmsg = 'YOU SURVIVED' + str(total_rounds) +\
        'ROUNDS, AVRAGING' +\
        str(avg)
    break


total_SHOTS = total_SHOTS+thisround
avg = str(total_SHOTS/float(total_rounds))
print('THOU SHOT'+str(thisround)+'THIS ROUND')
print('YOUR FIRING AVRAGE ='+ str(avg))
print("")

print(statsmsg)
