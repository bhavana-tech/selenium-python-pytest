print(
    "1. There are 2 arrays A and B. You need to merge these arrays into 1, remove duplicates and the nsort in ascending order")

array_A = list(input("Enter list of array A"))
array_B = list(input("Enter list of array B"))
array_C = array_A + array_B
print("After merging ", array_C)
removing_duplicates = set(array_C)
print("Removing Duplicates", removing_duplicates)
after_sorting = sorted(removing_duplicates)
print("after_sorting-----", after_sorting)

print(
    "2. There are 2 lists 1 and 2. You need to merge these lists into 1, remove duplicates and the nsort in ascending order")

# list1 = [2, 3, 4, 4]
# list2 = [5, 7, 6]
# list3 = list1 + list2
# print("After merging ", list3)
# removing_duplicates = set(list3)
# print("Removing Duplicates", removing_duplicates)
# newly_sorted = sorted(removing_duplicates)
# print("Sorted-->", newly_sorted)
# #or
# print(sorted(set(list2 + list1)))
