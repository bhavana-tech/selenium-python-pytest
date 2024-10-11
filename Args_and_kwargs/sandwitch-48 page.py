def sandwich_making(size,count,*toppings, **details):
    #These toppings are stored as tuples and these are positiona larguments
    #Details are kwargs and are stored as dictnaries
    print(f"\nPreparing sandwich of {size} size of count {count} with below toppings")

    for i in toppings:
        print(f"{i}")

    for key,value in details.items():
        print(f"{key}:{value}")

sandwich_making("Big",4, "capsicum","corn","cheese",delivery=75, tips=50, CGST=30, SGST=40)
sandwich_making("Medium",1,"pepper","salt",delivery=75)
sandwich_making("Large",3,"sause",roaming_charge=45)
sandwich_making("Small",2)
