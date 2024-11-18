# Rock/ Paper/ Scissor Game
import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissor"]

while True:
    print("--------------------------------")
    user_input = input(
        "Choose one of the following options\nRock/ Paper/ Scissor or q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        print("Please choose a valid option")
        continue

    rand_num = random.randint(0, 2)

#  (Rock = 0, paper = 1, scissor = 2)
    computer_input = options[rand_num]
    print("Commputer choose: ", computer_input)

    if (user_input == "rock" and computer_input == "scissor"):
        print("YOU WON!")
        user_score += 1

    elif (user_input == "paper" and computer_input == "rock"):
        print("YOU WON!")
        user_score += 1

    elif (user_input == "scissor" and computer_input == "paper"):
        print("YOU WON!")
        user_score += 1

    elif (user_input == "scissor" and computer_input == "scissor"):
        print("Tie!")

    elif (user_input == "paper" and computer_input == "paper"):
        print("Tie")

    elif (user_input == "rock" and computer_input == "rock"):
        print("Tie")

    else:
        print("YOU LOOS!")
        computer_score += 1


print("--------------------------------")
print("Your total score is ", user_score)
print("Computer total score is", computer_score)
if user_score > computer_score:
    print("So You won this league")
elif user_score == computer_score:
    print("No one won this league")
else:
    print("Computer won this league")
print("--------------------------------")
