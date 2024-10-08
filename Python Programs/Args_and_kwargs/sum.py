

print("----Example of usng sum using decorators----")

def decorator_sum(func):
    def wrapper(*args, **kwargs):
        # Call the original function to get two numbers
        x, y = func(*args, **kwargs)
        total = x + y
        print(f"The sum of {x} and {y} is {total}")
        return total
    return wrapper

@decorator_sum
def get_numbers():
    num_x = int(input("Enter x: "))
    num_y = int(input("Enter y: "))
    return num_x, num_y

# Use the decorated function
result = get_numbers()


print("----------Example 4------------)
      class ValueError(Exception):
    pass

def sum_numbers(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total

# Prompt the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input string into a list of strings
number_strings = user_input.strip().split()

# Convert the list of strings to a list of integers
try:
    numbers = [int(x) for x in number_strings]
except Exception as e:
    print(e,"Please enter valid integers separated by spaces.")
    exit(1)

# Calculate the sum using the sum_numbers function
result = sum_numbers(numbers)

print(f"The sum of the entered numbers is: {result}")
