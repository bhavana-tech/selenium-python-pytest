def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


text = "radar"
if palindrome(text):
    print("It is palindrome")
else:

    print("Not palindrome")
