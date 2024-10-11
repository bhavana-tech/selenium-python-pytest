global_variable="Implement global rule"

def decorator_countryrule(func):
    def wrapper():
        print("Decorator Country rule-- ")
        func()
    return wrapper

@decorator_countryrule
def state_rule():
    print("State rule implement")
    print(global_variable)

@decorator_countryrule
def city_rule():
    print("Implement city rule")
    print(global_variable)

city_rule()
state_rule()
