print("Code for TUPPle is -UPPend, Extend, [Insert!Replacing], Pop")
tuple=[(3,5,6),(3,2,4),('a','b','c')]
tuple2=[('d','e','f')]
tuple+=tuple2
tuple.append(tuple2)
print(tuple)

tuple3=[(1,2),(3,4)]
tuple4=[(5,6),(7,8)]
tuple3+=tuple4
tuple3.extend(tuple3)
print(tuple4)

tuple[1]='avrevrevr'
print(tuple)

tuple5=[1,2,4,5,6,7,8]
tuple5.pop(1)
print(tuple5)

tuple6=[2,3,4,5,3]
tuple6.pop(-1)
print(tuple6)