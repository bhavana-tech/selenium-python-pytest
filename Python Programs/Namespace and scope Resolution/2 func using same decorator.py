universal_rule = "Google"

#decorators
def decorator1(func):
    print("Inside decorator, before wrapper func---->", universal_rule)
    def wrapper():
        print("Inside wrapper func----->", universal_rule)
        print("\n\n")
        func()
    return wrapper()

@decorator1
def country_rule():
    print("Implemeting county rule--BEFORE UPDATING-->")
    global universal_rule
    universal_rule="Contry rule"
    print("Implementing country rule--AFTER UDATING-->", universal_rule)
    print("\n\n")

@decorator1
def state_rule():
    print("Implemeting state rule--BEFORE UPDATING-->")
    global universal_rule
    universal_rule = "State rule"
    print("Implementing state rule--AFTER UDATING-->", universal_rule)
    print("\n\n")

state_rule()
country_rule()


# Question: Which is execued first? country_rule() or state_rule().
# Answer: Since both functions are decorated with same decorator, teh decorator is applied immediately during the
# function defination, not when the functio nsi called.
# Here’s the sequence of execution:
#
# When the @decorator1 is applied to country_rule():
#
# The decorator decorator1() is called with country_rule as its argument.
# Inside decorator1(), the message "Inside decorator, before wrapper func" is printed.
# The wrapper() function is defined and called immediately because of return wrapper().
# Inside wrapper(), the message "Inside wrapper func" is printed.
# Then, the original country_rule() function is executed, changing the universal_rule and printing the messages.
# The same happens for state_rule():
#
# The decorator decorator1() is called with state_rule as its argument.
# Inside decorator1(), the message "Inside decorator, before wrapper func" is printed.
# The wrapper() function is defined and called immediately because of return wrapper().
# Inside wrapper(), the message "Inside wrapper func" is printed.
# Then, the original state_rule() function is executed, changing the universal_rule and printing the messages.
# Order of Execution:
# country_rule() is decorated first, so its decorator executes first.
# state_rule() is decorated next, so its decorator executes afterward.