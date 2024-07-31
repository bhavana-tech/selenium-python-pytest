list1 = [24, 433, 5, 6634, 2, 232, 5, 43, 7, 42]

odd = (x for x in list1 if x % 2 != 0)
print(list(odd))

even = (x for x in list1 if x %2 ==0)
print(list(even))