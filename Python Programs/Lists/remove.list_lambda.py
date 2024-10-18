In python, we can use lambda function to filter out specific items based on condition. Only the elements that satisfy that condition are filtered

Eg 1
list1=[1423,3242,3,5,6,4,5654,33,'g']
filtered_list=filter(lambda x:x<=10,list1)
print(filtered_list)
