
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
