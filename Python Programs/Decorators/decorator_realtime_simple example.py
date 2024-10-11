global_variable ="This is universal rule"

def decorator(func):
    print("Inside decorator ,outside wrapper")
    def wrapper():
        print("Inside wrapper")
        print("DRINK AMLA FIRST")
        return func
    return wrapper()

@decorator
def next_food():
    print("DRINK COFFEE NEXT")

@decorator
def other_next_food():
    print("tindi")

next_food()
print("----------------")
other_next_food()