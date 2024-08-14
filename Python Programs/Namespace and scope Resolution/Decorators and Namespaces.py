world_rule = "Everyone must sleep at night."  # Global rule

# Decorator that checks the global rule
def check_world_rule(func):
    def wrapper():
        print("Checking world rule:", world_rule)  # Access the global rule
        func()
    return wrapper

@check_world_rule  # Decorator applied
def house_rule():
    print("House rule: Everyone must sleep by 10 PM.")  # Local rule

house_rule()
