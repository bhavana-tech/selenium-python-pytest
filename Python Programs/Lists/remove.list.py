#We can remove multiple elements from the list using for loop,comprehenive methods and lambda method

#Normal single removal of items in the list can be done by using "del" or "remove"

1. Removal of items using "del"
original_list1=['a','b','c','d',23,34]
del original_list1[0]
print(original_list1)
-----------------------------------------------------------------------------------------
2. REmoval of items using "remove"
original_list1=['a','b','v','e',23]
original_list1.remove[23]
print(original_list1)
------------------------------------------------------------------------------------------
3. To remove multipe items or duplicates in the list using for loop:
print("Removing items from the list using loop")
original_list1=['a','b','c','d',23,34]
elements_to_removed1=['a','b','c']

for x in elements_to_removed1:
    if x in original_list1:
        original_list1.remove(x)
print(original_list1)
----------------------------------------------------------------------------------------
4. To remove duplicates in the list by using comprehensive method

original_list = [1, 2, 3, 4, 5, 6, 7]
elements_to_remove = {3, 5, 7}  # Use a set for faster membership checking

filtered_list = [x for x in original_list if x not in elements_to_remove]
print(filtered_list)  # Output: [1, 2, 4, 6]


-----------------------------------------------------------------------------------------
5. To remove itesm in list using lambda method

list1=[2,4,5,87,8324,3]

filter_list=filter(lambda x:x >1000, list1)

print(filter_list) ---leads to <filter object at 0x7c8c3b2a1ab0>, so convert the filtered list to list

print(list(filter_list))----- prints [8324], to remove [], add *

print(*list(filter_list))

#Suppose there is a string in list, in lambda method we should add another condition that >= condition applies ony to integer and not to string.

original_list=[3,42,455,56,23,'test']
filtered_list=filter(lambda x: isinstance(x,int) and x >= 10,original_list)
print(list(filtered_list))
---------------------------------------------------------------------------------------------------

Remove Duplicates: Use sets to remove duplicates from a list

