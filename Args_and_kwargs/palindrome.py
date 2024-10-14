def decorator_palindrome(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        if text == text[::-1]:
            print(f"{text} is palindrome")
        else:
            print(f"{text} is not palindrome")
        return text

    return wrapper


@decorator_palindrome
def palindrome(text,extra=""):
    return text
#Here palinrome unctio ncan take 2 arguments- 'text' and 'extra'. However only one argument 'text'
# is needed because 'extra' parameter has default value.

for i in range(3):
    text = input("Enter string")
    result = palindrome(text)
    print(result)

#Compare with palindrome_decorators.py example in decorators folder. the ian advantage of using *args, **kwargs
# is - to the wrapper function, we can pass any kind of arguemnts that might be passed to the original palindrome
# function. If we wan to modify the palindrom functon to accept addition lrguments, decorator would still work!

#Here wrapper function can take only one argument 's' where teh scope is limited unilke *args, **kwargs.
#In case future we need to change the original palindrome function, we need to hange the decorator! Oh No!
#The above code is not flexible since it accepts only ONE ARGUMENT.
#*args, **kwargs can handle more arguments making the decortor more flexible.

# WHEN DO YOU USE *args, **kwargs?
# ANs: We use *args, **kwargs when we need more flexible decorators and the functions accepts these wrapper funcions
# with many arguments.

#What if we dont use *args, **kwargs? and just use specific(single) arguemnt?
#Ans - If we want the decorator applicable to single function with known signature.