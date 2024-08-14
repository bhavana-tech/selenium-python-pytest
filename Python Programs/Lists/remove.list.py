#We can remove multiple elements from the list using for loop and comprehenive methods

print("Removing items from the list using loop")
original_list1=['a','b','c','d',23,34]
elements_to_removed1=['a','b','c']

for item in elements_to_removed1:
    if item in original_list1:
        original_list1.remove(item)
print(original_list1)

print("--------------------------------------------------------------------")

original_list = [1, 2, 3, 4, 5, 6, 7]
elements_to_remove = {3, 5, 7}  # Use a set for faster membership checking

filtered_list = [x for x in original_list if x not in elements_to_remove]
print(filtered_list)  # Output: [1, 2, 4, 6]


print("---------------------------------------------------------------------")

original_list1 = [1, 2, 3, 4, 5, 6, 7]
elements_to_remove1 = [3, 5, 7]

filtered_list1 = [x for x in original_list1 if x not in elements_to_remove1]
print(filtered_list1)  # Output: [1, 2, 4, 6]