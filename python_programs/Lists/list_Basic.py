print("Code for list is --Append, Extend, [Insert!Replacing], Remove, Delete")

list1=[1,2,3,4,5,6,7,8,'abc','def']
print("Original list                                                  ",list1)

#This is appending ie addign as a single element at the end
list1.append(['append1','append2'])
print("AFTER APPENDING ie adding multiple elements as a single element",list1)

#This is extending ie adding as individual elements at the end
list1.extend([11,12])
list1.extend('aeiou')
print("AFTER EXTENDING ie adding as individual elements at the end    ",list1)

#This is inserting NO..NO..REPLACING
list1[0]='Replacing_at_0th_position'
print("AFTER REPLACING at 0th position ie list1[0]=                   ",list1)
print("Replacing last position is list1[-1]                           ",list1)

#Replacing multiple elements
list2=[1,2,3,4,5,6,7,8,9]
list2[0:5]=[11,12,13,14,15]
print(list2)

#Removing specific element
list1.remove('Replacing_at_0th_position')
print("After removing specific element                                ",list1)

#Deleting at specific position
del list1[0]
print("After deleting at 0th position list1[0]                        ",list1)
print("updated list now                                               ",list1)

list3=[1,33,3,4,3,'d',7,75,44]
del list3[0:3]
print("Deleting firt 4 elements                                        ",list3)
del list3[-1]
print("Deleting last item")
print("Deleting first 4 elements                                        ",list3)
