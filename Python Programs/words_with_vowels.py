string = "Land is green and sky is blue"
words = string.lower().split()

vowels = "aeiou"
count_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

words_with_vowels = []

for word in words:
    has_vowels = False #Initialise to false for each word

    for char in word:
        if char in vowels:
            has_vowels = True
            count_vowels[char] += 1
        # else:
        #     has_vowels = False

    if has_vowels:
        words_with_vowels.append(word)
print(words_with_vowels)
