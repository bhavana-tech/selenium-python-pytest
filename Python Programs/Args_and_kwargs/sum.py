print("-------------------EXAMPLE 1 of SUM-----")

# def simple_sum(*args):
#     return sum(args)
#
# # Example usage
# result = simple_sum(1, 2, 3, 4, 5)
# print(f"Sum: {result}")

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
