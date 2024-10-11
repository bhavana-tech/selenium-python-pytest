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


for i in range(3):
    text = input("Enter string")
    result=palindrome(text)
    print(result)

#Here wrapper function can take only one argument 's' where teh scope is limited unilke *args, **kwargs.
#In case future we need to change the original palindrome function, we need to hange the decorator! Oh No!
#The above code is not flexible since it accepts only ONE ARGUMENT.
#*args, **kwargs can handle more arguments making the decortor more flexible.
