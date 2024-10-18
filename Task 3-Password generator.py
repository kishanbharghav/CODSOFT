#Simple password generator in python
import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    # Defining character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensuring password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Filling the rest of the password with a mix of all character sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffling the password list to randomize character order
    random.shuffle(password)

    # Joining the list to form the final password string
    return ''.join(password)

# Main loop for generating passwords
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        generated_password = generate_password(length)
        if generated_password:
            print("Generated Password:", generated_password)
        
        # Asking the user if they want to generate another password
        choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the password generator. Goodbye!")
            break
    except ValueError:
        print("Please enter a valid number.")
