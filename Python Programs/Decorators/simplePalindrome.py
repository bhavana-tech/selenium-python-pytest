What Are Decorators in Python?
Decorators are a powerful feature in Python that allow you to modify or enhance the behavior of functions or methods without changing their actual code. Think of decorators as wrappers that add extra functionality to your existing functions.

Simple Definition
A decorator is a function that takes another function as input, adds some functionality to it, and returns the new function. This allows you to "decorate" or "wrap" your original function with additional features.

Why Use Decorators?
Reusability: You can apply the same decorator to multiple functions.
Separation of Concerns: Keep your core logic separate from auxiliary features like logging, timing, or access control.
Clean Code: Makes your code cleaner and more readable by abstracting repetitive tasks.


def palindrome(s):
    try:

        if s == s[::-1]:
            return f'"{s}" is palindrome'
        else:
            return f'"{s}" is not palindrome'
    except Exception as e:
        return f"An error occured{str(e)}"

    finally:
        print("palindrome check completed")
#f is a format string
for i in range(5):
    text=str(input("Enter the string"))

    result =palindrome(text)
    print(result)
