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

When we call any function in python, we can call that functon by passign any argument. There are 2 types of argument--positional arguments and keyword arguments. 
Positional arguments are those arguments that needs to be passed in specific order, here the position of each argument matters, the first srgument u pass goes to the first parameter, the second argument u pass goes to 
the second paramter.

 eg def some_func(name, age):
      print(f"{name} is {age} years")

    some_func("Bhavana",33)
Here name and age are 2 parameters,teh first argument "Bhavana" is assigned to first parameter "name" and second argument "33" is assigned to second parameter "age".

But in keyword arguments, position doesn't matter. We can assign which parameter each argument should be assigned to. 

eg some_func(name,age):
     print(f"{name} is {age} years")

   some_func(name="Bhavana",age=33)

positional arguments should come before keyword arguments. If we interchange, python will raise syntax error. 

We use these positional arguments and keyword arguments with decorators. 
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before func runs")
        return func
        print("After func runs")
    return wrapper()

@decorator    
def some_func(name, message="hi"):
    print(f"{message}, {name}")
    
some_func("Sritaata") ---#positional argument only

some_func(name="usha", message="Hello") ---#Keyword argument only

some_func("Bhavana",message="Hiiii") --#both positional and keyword argument

some_func(message="guru!",name="Rakesh")  ---#Keyword argument only

  
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
