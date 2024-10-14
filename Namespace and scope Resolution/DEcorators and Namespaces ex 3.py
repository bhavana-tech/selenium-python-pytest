base_url = "Universal rule"  #Global Variable


def country_rule(func):
    def wrapper():
        func()
        print("Implementing country rule")
        print(f"Inside country rule---> This rule is there! {base_url}")

    return wrapper


@country_rule
def state_rule():
    print("implementing state rule")
    print(f"Inside state rule---> this rule is there! {base_url}")


@country_rule
def city_rule():
    global base_url
    print("implementing city rule")
    base_url = "www.city.com"
    print(f"Inside city rule---> this rule is there! {base_url}")

city_rule()
state_rule()

# Now write state_rule() at first and then city_rule last and see the result.
Step-by-Step Explanation
Initial Global Variable (base_url):

Initially, base_url is set to "Universal rule" globally. This is the value it has everywhere in the code before any functions are called.
City Rule Function (city_rule()):

When city_rule() runs, you declare global base_url. This allows the function to modify the global base_url variable.
Inside city_rule(), you change base_url to "www.city.com".
After this, the global value of base_url is no longer "Universal rule"; it has been changed to "www.city.com" for the entire program.
State Rule Function (state_rule()):

When state_rule() is called, it prints the value of base_url.
Since city_rule() already changed base_url to "www.city.com", state_rule() will display this new value, not "Universal rule".
Why "Universal rule" Doesn't Appear:

The global variable base_url was changed by city_rule() before state_rule() could print it. So, "Universal rule" was overwritten and never displayed.
Visualization:
Before any function call: base_url = "Universal rule"
After city_rule() runs: base_url = "www.city.com" (Global value is changed)
When state_rule() runs: It sees base_url as "www.city.com" because it was modified earlier.

