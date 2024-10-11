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


def state_rule():
    print("Implemeting state rule--BEFORE UPDATING-->")
    global universal_rule
    universal_rule = "State rule"
    print("Implementing state rule--AFTER UDATING-->", universal_rule)
    print("\n\n")

if __name__ == "__main__":
    state_rule()
    country_rule()
#
# Execution Breakdown:
# The @decorator1 is applied to country_rule():
#
# When @decorator1 is applied, it triggers the execution of the decorator1() function with country_rule as an argument.
# Inside decorator1(), the message "Inside decorator, before wrapper func----> Google" is printed because the universal_rule at that point is still "Google".
# The wrapper() function is defined and immediately executed due to return wrapper(). This causes the following steps:
# The message "Inside wrapper func-----> Google" is printed.
# The country_rule() function is called.
# Inside country_rule(), it prints the messages before and after updating the universal_rule.
# After decorating country_rule():
#
# The state_rule() function is explicitly called.
# Inside state_rule(), it prints the messages before and after updating the universal_rule to "State rule".
# Finally, country_rule() is explicitly called:
#
# However, since country_rule() was already executed during the decoration process, when you explicitly call it again, nothing happens because the wrapper() function was already executed when the decorator was applied.
# Order of Execution:
# Step 1: The country_rule() function is executed during the decoration process when the @decorator1 is applied.
# Step 2: The state_rule() function is then called explicitly after the decoration.
# Conclusion:
# country_rule() is executed first, during the decoration process when @decorator1 is applied.
# state_rule() is executed second, when it is explicitly called in the code.

