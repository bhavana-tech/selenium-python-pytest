universal_rule = "Everyone should follow" #global variable

def outer_func():

    universal_rule = "Changing universal rule in outer func"
    print(universal_rule)
    def inner_func():
        print("inner func")
        universal_rule = "Changing universal rule in inner func"
        print(universal_rule)
    inner_func()
outer_func()

#Here we have not used global keyword to updaet the global variable. Since the outer_func
#and inner_func has universal_rule assigned, it treats it as local variable