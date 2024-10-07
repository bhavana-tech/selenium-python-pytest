print("-------------------EXAMPLE 1 of SUM-----")

 def simple_sum(*args):
  return sum(args)

result = simple_sum(1, 2, 3, 4, 5)
print(f"Sum: {result}")

print("-------------------EXAMPLE 2 of SUM-----")


def sum1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


total = sum1(1, 2, 4, 5, 7)
total2 = sum1(100,200)
total3=sum1(1000,2000)
print(total)
print(total2)
print(total3)

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
