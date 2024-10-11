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






print("-----------PIZZA with only size-----------")

# def pizza(size):
#     print(f"Ordered a pizza of size {size}")
#
# pizza("Large")

print("----------pizza with multiple toppings as positional arguments---------")


# def pizza(size, *toppings):
#     print(f"Ordered pizza of size {size} with toppings ")
#
#     for i in toppings:
#         print(f" - {i}")
#
#
# pizza("Large", "olive", "pepper", "corn")

print("----------pizza with multiple toppings as positional arguments and keyword arguments---------")
print("Here toppings are stored as list and details are stored as dictonaries")

def pizza(size, *toppings, **details):
    print(f"Ordered pizza of size {size} with toppings ")

    for i in toppings:
        print(f" - {i}")

    print("Below are the details")
    for key, value in details.items():
        print(f"{key}:{value}")
pizza("Large", "olive", "pepper", "corn", delivery=75,tips=20,SGST=90,CGSR=90)
