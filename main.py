import random

print("Welcome to Rock Paper Scissors! Type 'stop' to end the game.")

# Error proof user input
valid_choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choice is yours - rock, paper, or scissors: ").lower()

    # Check if the user wants to stop the game
    if user_choice == "stop":
        print("Thanks for playing! Goodbye!")
        break

    # Validate input
    if user_choice not in valid_choices:
        print("Invalid input. Please try again.")
        continue

    print(f"You have selected {user_choice.capitalize()}")

    # Bot selection
    bot_select = random.choice(valid_choices)
    print(f"Bot has selected {bot_select.capitalize()}")

    # Game logic
    if user_choice == bot_select:
        print("It's a tie!")
    elif (user_choice == "rock" and bot_select == "scissors") or \
         (user_choice == "paper" and bot_select == "rock") or \
         (user_choice == "scissors" and bot_select == "paper"):
        print("You win!")
    else:
        print("You lose!")