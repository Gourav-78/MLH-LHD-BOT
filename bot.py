import random

while True:
    possible_actions = ["rock", "paper", "scissors"]
    user_input = input(
        "Enter your choice : 0 for rock, 1 for paper and 2 for scissors : "
    )
    print("\n")
    user_action = possible_actions[int(user_input)]
    computer_action = random.choice(possible_actions)
    print("Your choice : ", user_action)
    print("Computer's choice : ", computer_action)
    print("\n")
    if user_action == computer_action:
        print("Both players selected same. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Want to play again Y/N : ")
    if play_again == "N":
        break
