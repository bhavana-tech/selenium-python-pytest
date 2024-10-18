#We can remove multiple elements from the list using for loop and comprehenive methods

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

