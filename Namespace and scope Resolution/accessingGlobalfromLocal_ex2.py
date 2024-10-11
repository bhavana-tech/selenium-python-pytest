 #LEGB rule
global_variable=10 #This is global namespace where global variables are stored.

def outer_func():
    enclosed_variable=20
    global global_variable #We are modifying the top most global variable from 10 to 100
    global_variable = 100
    print("enclosed_variable:",enclosed_variable)
    print(f"printing {global_variable} inside outer_func")


    def inner_func():
        global global_variable # We are modifying the top most global variable again from 100 to 1000
        local_variable=30
        global_variable=1000
        print("local_variable:",local_variable)
        print(f"printing {global_variable} inside inner_func")
    inner_func()
outer_func()

print(f"Printing the top most global variable {global_variable}")