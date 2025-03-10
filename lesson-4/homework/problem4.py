import random
n = random.randint(1, 100)
h = False
print("Welcome to the Guessing Game! The computer chose a number between 1 and 100.")
i = 0
while h != True:
    while i <= 10:
        s = int(input("Guess: "))
        if s == n:
            print("Congratulations! You found it. It was", n)
            break
        elif s < n:
            print("You guessed lower than the actual value.")
        else:
            print("You guessed higher than the actual value.")
        i += 1
    else:
        will = input("You lost. Want to play again?")
    if s == n:
        break
    else: 
        if will.lower() in ['y', 'yes', 'ok']:
            h = False
            i = 0
        else :
            h = True