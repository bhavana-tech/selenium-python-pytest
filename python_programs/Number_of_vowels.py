string = "aeiouAEIOU"
new_string = string.lower()
words = new_string.split()

vowels = 'aeiou'
count_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
sum_of_vowels = 0

for word in words:
    for char in word:
        if char in vowels:
            count_vowels[char] += 1
            sum_of_vowels += 1
        else:
            count_vowels[char] = 0

for char, count_vowels in count_vowels.items():
    print(char, count_vowels)
    
print("sum_of_vowels is---->", sum_of_vowels)
