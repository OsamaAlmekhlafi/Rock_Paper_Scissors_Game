# Done By : Osama Abdo Modhish

import random


def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input(
            "Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer wins!"
        else:
            return "You win!"

# Get the user's choice


def play_game():
    print("Welcome to Rock Paper Scissors!")
    while True:
        user_choice = get_user_choice()
        # Generate the computer's choice
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        # Determine the winner
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            print("The Game is Over...")
            print("------Thank You I hope You Had a Fun With My Game-------")
            break


# Call the Function to Start the game
play_game()
