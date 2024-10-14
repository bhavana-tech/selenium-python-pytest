string3 = "India India lost ODI world cup in India"
string1 = string3.lower()
words = string1.split()

count_letter = {}

#Freqencies of char in words

for word in words:
    for char in word:
        if char in count_letter:
            count_letter[char] += 1
        else:
            count_letter[char] = 1

for char, frequency_letter in count_letter.items():
    print("count of", char, "is", frequency_letter)

#frequencies of word
count_word = {}
for word in words:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1
print("Lets count frequencies of word in words in",string1)

for word, frequency_word in count_word.items():
    print("Count of", word, "is-->", frequency_word)
