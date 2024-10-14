print("Q1. Generate random numbers using lambda function")
import random
r = lambda: random.randint(100, 200)
generate_using_lambda = [r() for _ in range(5)]
print(generate_using_lambda)