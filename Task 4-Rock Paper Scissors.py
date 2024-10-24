import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors: ").lower()
    if user_input in choices:
        return user_input
    else:
        print("Invalid choice, try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(f"Result: {result}")

if __name__ == "__main__":
    play_game()
