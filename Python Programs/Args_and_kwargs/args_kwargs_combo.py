# def decorator_func(func):
#     def wrapper():
#         print("Drink amla juice first in the morning")
#         return func()
#
#     return wrapper
#
#
# @decorator_func
# def some_beverage():
#     print("drink coffee then")
#
#
# @decorator_func
# def breakfast():
#     print("Eat breakfast then")
#
# some_beverage()
# breakfast()

print("------------INCORPORATING ONLY *ARGS to the above program-------------------------")
#Modify the wrapper function to accept any number of positional arguments and any number of keyword argument.
#When we modify the wrapper funcion with *args and **kwargs, even the decorated functions like some_beverage()
#and breakfast() can accept arguemnts as well

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Drink amla juice first in the morning")
        return func(*args, **kwargs)

    return wrapper


@decorator_func
def some_beverage(beverage="default_beverage_NOT_REQUIRED"):
    print(f"drink {beverage} then")
    print("I have used *args only and  not used **kwargs")

@decorator_func
def some_breakfast(breakfast="default_breakfast_NOT REQUIRED"):
    print(f"Eat {breakfast} then")
    print("I have used *args only and not used **kwargs")
some_beverage("coffee")
some_beverage("tea")
some_beverage("masala tea")
some_beverage("black coffee")
some_beverage("ginger tea")


some_breakfast("upma")
some_breakfast("bisibelebath")
some_breakfast("pasta")
some_breakfast("idli")
some_breakfast("dosa")
some_breakfast("pongal")
some_breakfast("roti")


  
print("---------------------------------------------------------------------")
print("-------Incoporating *args and **kwargs to the above program")


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Drink amla juice first in the morning")
        return func(*args, **kwargs)

    return wrapper


@decorator_func
def some_beverage(beverage="default_beverage_NOT_REQUIRED", size="medium"):
    print(f"drink {beverage} then with {size}")
    print("I have used *args only and **kwargs")


@decorator_func
def some_breakfast(breakfast="default_breakfast_NOT REQUIRED", quantity="kg"):
    print(f"Eat {breakfast} then with {quantity}")
    print("I have used *args only and **kwargs")


some_beverage("coffee", "Medium")
some_beverage("tea", "Medium")
some_beverage("masala tea", "Medium")
some_beverage("black coffee", "Medium")
some_beverage("ginger tea", "Medium")

some_breakfast("upma","1kg")
some_breakfast("bisibelebath","1kg")
some_breakfast("pasta","1kg")
some_breakfast("idli","3")
some_breakfast("dosa","3")
some_breakfast("pongal","1")
some_breakfast("roti","2")
