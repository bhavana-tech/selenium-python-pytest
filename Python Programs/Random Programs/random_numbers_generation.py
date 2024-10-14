# print("Q1. Printing random integers from 100-200")
# import random
#
# start = 100
# end = 200
# for i in range(10):
#     r = random.randint(start, end)
#     print(int(r))

# print("Q2. Printing random integers for a selected given range")
#
# import random #random is a module
#
# range_start = int(input("Enter the starting range to print random numbers\n"))
# range_end = int(input("Enter the ending range to print random numbers\n"))
# numbers = int(input("How many integers you want to print?\n"))
#
# for i in range(numbers):
#     r = random.randint(range_start, range_end)
#     print(r)

# print("Q3. Generate random numbers using list comprehensions")
#
# import random
#
# r1 = [random.randint(100, 200) for _ in range(2)]
# print(r1)

print("Q4. Using lambda function, generate random numbers")
# import random
#
# r = lambda: random.randint(100, 200)
# generate_using_lambda = [r() for _ in range(5)]
# print(generate_using_lambda)

print("Q5. Verify whether random numbers u generated falls within the range")
# import random
# number = random.randint(100, 200)
# print(number)
# assert 200 >= number >= 100, f"Number {number} out of range"

print("Q6. Generate random float numbers")
# import random
#
# random_float = [random.random() for _ in range(100, 200)]
# print(random_float)

print("Q7. Suppose there is a list given and u want to print random number from that list")
# import random
#
# item = ['apple', 'banana', 'cat', 'dog', 'elephant']
# random_from_choice = [random.choice(item) for _ in range(3)]
# print(random_from_choice)



