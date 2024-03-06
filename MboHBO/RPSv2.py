import random

# Define options and winning combinations
options = ["rock", "paper", "scissors"]
win_combos = {
    "rock": "Sscissors",
    "paper": "rock",
    "scissors": "paper"
}

# Initialize variables
user_wins = 0
computer_wins = 0
doorspelen = True

while doorspelen == True:
    # Get user input
    user_choice = input("Choose Rock, Paper, or Scissors (Q to quit): ").upper().strip()

    # Check for quit option
    if user_choice == "Q":
        print("Thanks for playing! You won", user_wins, "games.")
        break

    # Validate user input
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Generate computer choice
    computer_choice = random.choice(options)

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif win_combos[user_choice] == computer_choice:
        user_wins += 1
        print("You win! You chose", user_choice, "and computer chose", computer_choice)
    else:
        computer_wins += 1
        print("You lose! You chose", user_choice, "and computer chose", computer_choice)

    # Print current score
    print("Your wins:", user_wins, "Computer wins:", computer_wins)
