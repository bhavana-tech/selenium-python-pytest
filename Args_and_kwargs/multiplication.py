print("Multiplication using *args ONLY")
# def multiplication(*numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     print(result)
#
#
# multiplication(2, 3, 4, 5)
# multiplication(2, 3, 4)
# multiplication(2, 3, 4, 34, 5)
# multiplication(2, 3, 4, 5, 0)

print("multiplication using decorators only")


def decorator_multiplication(func):
    print("multiplication using decorators inside wrapper")

    def wrapper(x, y):
        for i in range(4):
            num_x = int(input("Enter x"))
            num_y = int(input("Enter y"))
            result = num_x * num_y
            print(result)

        return func()

    return wrapper


@decorator_multiplication
def multiplication():
    print("This is decorated func")


multiplication(3, 5)
