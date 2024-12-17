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

---------------------------------------------------------------------------------
universal_rule="asia"

def deco_func(func):
    def wrapper():
        
        enclosed_variable="india"
        global universal_rule
        universal_rule="india"
        print("universal_rule in decoraotr",universal_rule)
        
        return func()
    return wrapper
    
@deco_func    
def outer_func():
    global universal_rule
    universal_rule="karnataka"
    print("universal_rule in outer",universal_rule)
    
@deco_func    
def inner_func():
    global universal_rule
    universal_rule="mysore"
    print("universal_rule in inner",universal_rule)
    
inner_func()
outer_func()

    
