import random
options = ['rock', 'paper', 'scissors']
comp_score = 0
human_score = 0
while max(comp_score, human_score) < 5:
    human_choice = input()
    comp_choice = random.choice(options)
    if human_choice not in options:
        print("Invalid choice.")
        while human_choice in options:
            print("Choose again.")
            human_choice = input()
    if human_choice == comp_choice:
        print("Tie!")
    elif (human_choice == "rock" and comp_choice == "scissors") or (human_choice == "scissors" and comp_choice == "paper") or (human_choice == "paper" and comp_choice == "rock"):
        human_score += 1
        print("You won :) Your score is", human_score, " The computer's score is", comp_score)
    else :
        comp_score += 1
        print("You lost :( Your score is", human_score, " The computer's score is", comp_score)
if human_score == 5:
    print("You won the game.")
else:
    print("You lost the game.")