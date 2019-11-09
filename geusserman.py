cpuno = 167
prompt = "Guess"
while True:
    gamerman = input(prompt)
    if cpuno == int(gamerman):
        print("Succes!")
        break
    elif cpuno < int(gamerman):
        print("Too high!")
    else:
        print("Too low")
