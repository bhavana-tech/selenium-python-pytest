print("Q1. Generate random numbers using lambda function")
import random
r = lambda: random.randint(100, 200)
generate_using_lambda = [r() for _ in range(5)]
print(generate_using_lambda)
-----------------------------------------------------------------
To print even numbers:

e=filter(lambda x:x%2==0,range(1,50))
print(list(e))

----------------------------------------------------------------------------
sorting of a tuple

tuple=[('a',3),('b',2),('c',1)]
tuple.sort(key=lambda x:x[1])
print(tuple)
-----------------------------------------------------------------------
sorting of a list

list=[23,2,5,2,5,8,1,1,2,232,32]
list.sort(key=lambda x:x)
print(list)

-------------------------------------------------------------------
addition of 3 numbers:

x = int(input("enter x: "))  
y = int(input("enter y: "))  
z = int(input("enter z: "))  
res = lambda x, y, z: x + y + z  
print(res(x, y, z))

----------------------------------------------------------------------
To square the numbers using map and lambda

numbers=[1,2,3,4,5]
res=map(lambda x:x**2, numbers)
print(list(res))
  ----- ---------------------------------------------------------------------
To generate only positive numbers

   numbers=[3,4,-2,3,-3]
  filter(lambda x:x>0 , numbers)
  print(numbers)
 ------ -----------------------------
