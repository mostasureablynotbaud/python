import random
cpuno = random.randint(1,1000)
prompt =("Guess")
while True:
    gamerman = input(prompt)
    if cpuno == int(gamerman):
        print("CORRECT")
        break
    elif cpuno > int(gamerman):
        print('UNDERSHOT')
    else:
        print('OVERSHOT')
