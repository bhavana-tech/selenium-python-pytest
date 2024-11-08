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

#To sorted in reverse order:


array_A = list(input("Enter list of array A"))
array_B = list(input("Enter list of array B"))
array_C = array_A + array_B
print("After merging ", array_C)
descend_sorting=sorted(array_C,reverse=True)
print(descend_sorting)
