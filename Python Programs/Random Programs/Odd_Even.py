list1 = [12,3,4,342,24,434]
for i in list1:
    try:
        if (i%2 == 0):
            print("Number is even")
        else:
            print("Number is odd")


---------------------------------------------------
another method:

list=[2,4,2,43,3]
list1=(x for x in list if i/2!=0)
print(list1)
