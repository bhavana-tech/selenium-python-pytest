def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
#
# @logger
# def add(x, y):
#     return x + y
#
# # Usage:
# add(10, 20)  # Output: Arguments: (10, 20), Keyword Arguments: {}
def test_logger():
    @logger
    def add(x, y):
        return x + y

    result = add(10, 20)
    assert result == 30
