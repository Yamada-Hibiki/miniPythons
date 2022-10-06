import random

choices = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_choice = input("Please enter Rock, paper, scissors or Q to quit the game: ").lower()
    if user_choice == "q":
        break

    if user_choice not in choices:
        print("Please enter again: ")
        continue

    # 0 is rock, 1 is paper, 2 is scissors
    random_number = random.randint(0, 2)

    computer_choice = choices[random_number]
    print("Computer chose", computer_choice + ".")
    
    if user_choice == "rock" and computer_choice == "scissors":
        print("Congratulations! You won the game!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("Congratulations! You won the game!")
        user_wins += 1 
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Congratulations! You won the game!")
        user_wins += 1
    elif user_choice == computer_choice:
        print("Good. Let's play again.")
    else:
        print("You lost...")
        computer_wins += 1
    
print("You won", user_wins, "times!")
print("You lost", computer_wins, "times..")

print("Thanks for playing!")
    