class NotAStringError(Exception):
    pass

class EmptyStringError(Exception):
    pass
def decorator_palindrome(func):
    def wrapper(s):
        try:
            if not isinstance(s, str):
                raise NotAStringError
            if s == "":
                raise EmptyStringError

            if s == s[::-1]:
                print(f"{s} is palindrome")
            else:
                print(f"{s} is not palindrome")

        except NotAStringError as e:
            print(e)



        except EmptyStringError as e:
            print(e)

        finally:
            print("Palindrome test compelted")
    return wrapper
@decorator_palindrome
def palindrome(s):
    print("It is palindrome")

for i in range(5):
    text = str(input("Enter the string"))

    result = palindrome(text)
    print(result)

