team = {'India': 1, 'Australia': 2, 'England': 2}
team.pop('India') #pop always eliminates the Key and not value
team.popitem()
print(team)

print("Question 1: How will you access the data stored in dictonaries")
dict={'apple':1,'banana':3}
item=dict['apple']
print(item)


print("Question 2 How can u store webdriver options in dictionary")
dict={'headless':True,'disble-gpu':True}
item=dict['apple']
print(item)

print("Question 3: When do you use dictonary  and list in selenium tests ")
#   A dictionary stores key-value pairs and is used to store unique keys and their values. A list is used when order of the
#elements matters or when you perform operatisn like indexing and iterating. Lists are used for storing multipel test cases and
#storing results. Dict are used for configurations.

print("Question 4: How can u handle nested dictionaries in pytest fixtures")
@pytest.fixtures
def some_method():
    return{
        "dict1": {'a': 1, 'b': 2},
        "dict2": {'fw': 12, 'gr': True}
    }

print("5. What methods are used to manipulate dictionares in pyhon")
# .get(), .keys(), .values(), .update(), .pop(), .items(), popitem()
like
dict={'a':1,'b':2,'c':3}
dict.get('a') Output is 1

dict.keys() Output is a,b,c, ie it will return all the keys

dict.values() output is 

dict.update({'b':4})
print(dict) output is a:1, b:4, c:3

dict.pop('a') # This will pop the key
dict.popitem() # This will pop the last item





