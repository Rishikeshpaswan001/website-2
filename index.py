from math import sqrt

# Function to calculate the result
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error: " + str(e)

# Function to calculate square root
def square_root(num):
    try:
        return str(sqrt(num))
    except Exception as e:
        return "Error: " + str(e)

# Command-line interface
if __name__ == "__main__":
    while True:
        user_input = input("Enter a calculation (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break
        elif user_input.startswith('√'):
            try:
                number = float(user_input[1:].strip())
                print("Square root:", square_root(number))
            except ValueError:
                print("Error: Please enter a valid number.")
        else:
            print("Result:", calculate(user_input))
