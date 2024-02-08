import random

actions = ['rock', 'paper', 'scissors']

while True:
    user_choice = input('Enter your choice (rock, paper or scissors): ')

    program_choice = random.choice(actions)

    print("Your choice", user_choice, "and Computer choice", program_choice)

    if user_choice == program_choice:
        print("Both players selected same . It's a tie!")
    elif user_choice == "rock":
        if program_choice == "scissors":
            print("You win! because Rock smashes scissors.")
        else:
            print("You lose,Paper covers rock!")
    elif user_choice == "paper":
        if program_choice == "rock":
            print("You win! because Paper covers rock.")
        else:
            print("You lose,Scissors cuts paper!")
    elif user_choice == "scissors":
        if program_choice == "paper":
            print("You win! because Scissors cuts paper.")
        else:
            print("You lose,Rock smashes scissors!")
            
    play_again = input('Play again? (y/n) : ')
    if (play_again.lower() == 'n'):
        break
