print("--------------------Ordering pizza without positional argument ie *args")
# def order_pizza(size, count):
#     print("ordering pizza")
#     print("size", size)
#     print("count", count)


#order_pizza("Medium", 1)

print("--------------------Ordering pizza with positional argument *args")
# def ordering_pizza(size, count, *toppings):
#     print("Ordering pizza")
#     print("size",size)
#     print("Count",count)
#     if toppings:
#         print("Below are the toppings")
#         for topping in toppings:
#             print(f"{topping}")
##
# pizza = ordering_pizza("Medium", 1, "olive", "cheese", "corn")
# print(pizza)


print("Ordering pizza with positional argument and keyword arguments")


def order_pizza(size, count, *toppings, **customization):
    print("Ordering pizza")
    print("size",size)
    print("count",count)
    if toppings:
        print("Below are the toppings")
        for topping in toppings:
            print(f"{topping}")
    if customization:
        print("Below are the customization")
        for key, value in customization.items():
            print(f"{key}:{value}")


order_pizza("Medium", 1, "olive", "cheese", "sause", "capsicum", "customization_1", "Custom_2")
