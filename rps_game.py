import random

def get_user_choice():
    """
    Prompts the user to enter their choice of 'rock', 'paper', or 'scissors'.
    Keeps asking until a valid choice is entered.

    Returns:
        str: The user's choice in lowercase.
    """
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose from 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    """
    Randomly selects a choice for the computer from 'rock', 'paper', or 'scissors'.

    Returns:
        str: The computer's choice.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a Rock-Paper-Scissors round.

    Parameters:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.

    Returns:
        str: A message indicating if the user wins, computer wins, or it's a tie.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    The game continues until the user chooses not to play again.
    """
    print("Welcome to Rock-Paper-Scissors!")
    play_again = 'yes'
    
    while play_again == 'yes':
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Show choices
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Determine and display winner
        print(determine_winner(user_choice, computer_choice))

        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
