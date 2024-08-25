def decorator_palindrome(func):
    def wrapper(s):
        if s == s[::-1]:
            return f'"{s}" is palindrome'

        else:
            return f'"{s}" is not palindrome'
    return wrapper

@decorator_palindrome
def palindrome(s):
    return s

text="radar"
result=palindrome(text)
print(result)