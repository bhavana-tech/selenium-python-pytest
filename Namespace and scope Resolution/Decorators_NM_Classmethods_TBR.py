country_rule = "Everyone should follow country rule"  #Global variable


def decorator1(func):
    def wrapper(self):
        print(country_rule)
        func(self)

    return wrapper


class State:
    state_rule = "Everyone should follow state rule"

    def __init__(self, city_rule):
        self.city_rule = city_rule

    @decorator1
    def rules(self):
        print("staterule", self.state_rule)  #access the class level
        print("cityrule", self.city_rule)  #access the instance level


city_object = State("Ok we follow rules")
city_object.rules()

