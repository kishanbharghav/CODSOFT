# Function to perform advanced arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    elif operation == '%':
        return num1 % num2
    elif operation == '**':
        return num1 ** num2
    else:
        return "Invalid operation!"

# Main loop for multiple calculations
def main():
    while True:
        try:
            # Prompting the user for inputs
            number1 = float(input("\nEnter the first number: "))
            number2 = float(input("Enter the second number: "))
            print("Available operations: +, -, *, /, %, ** (exponentiation)")
            operation = input("Choose an operation: ")

            # Performing the calculation and displaying the result
            result = calculate(number1, number2, operation)
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        
        # Asking user if they want to perform another calculation
        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Running the main calculator loop
main()
