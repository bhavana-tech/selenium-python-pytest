

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
