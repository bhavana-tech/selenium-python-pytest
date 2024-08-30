# def decortor_cakemaking(func):
#     def wrapper(*size, **flavour):
#         print("Add maida and baking soda to make cake")
#         return func(*size, **flavour)
#     return wrapper
#
#
# @decortor_cakemaking
# def egglesscake(size, flavour):
#     print(f"Do not add egg to {flavour} flavour of size {size}")
#
#
# @decortor_cakemaking
# def eggcake(size, flavour):
#     print(f"You can add egg to {size} of {flavour} flavour")
#
# eggcake("medium size","chocolate")
# egglesscake("large","vanilla")
#
#
from _ctypes_test import func

print("ONE MORE COMPLEX EXAMPLE WITHOUT *ARGS and **KWARGS")

# def decorator_eggless_cake(func):
#     def wrapper():
#         ingredients_eggless = [
#             'Baking powder', 'Butter', 'Sugar', 'Vanilla flovour', 'Salt']
#
#         print(*ingredients_eggless)
#
#         return func()
#
#     return wrapper
#
# def decorator_egg_cake(func):
#     def wrapper():
#         ingredients_eggcake = ['Egg', 'Baking powder', 'Butter', 'Sugar', 'Vanilla flovour', 'Salt']
#         print(*ingredients_eggcake)
#
#         return func()
#
#     return wrapper
#
# def decorator_choice(func):
#     def wrapper():
#         print("Which cake do you want?")
#         #choice()
#         option = input("Enter 1 for Eggless cake and 2 for Egg cake")
#
#         if option == '1':
#             return decorator_eggless_cake(func)()
#         elif option == '2':
#             return decorator_egg_cake(func)()
#         else:
#             print(option, "Not a valid option")
#             return func()
#
#     return wrapper
#
#
# @decorator_choice
# def choice():
#     print("Making choice")
#
#
# @decorator_eggless_cake
# def eggless_cake():
#     print("Inside eggless function--non decorator")
#
#
# #eggless_cake()
#
#
# @decorator_egg_cake
# def egg_cake():
#     print("Inside egg_cake function--non decorator")
#
#
# choice()
# eggless_cake()
# egg_cake()

print("ONE MORE EXAMPLE WITH *ARGS and **KWARGS")


def decorator_egg_less_cake(func):
    def wrapper(*args):
        ingredients_egg_less_cake = ["Baking soda", "vanilla", "maida"]
        print(ingredients_egg_less_cake, "are the ingredients of Egg less cake")

        return func(*args)

    return wrapper


def decorator_egg_cake(func):
    def wrapper(*args, **kwargs):
        ingredients_egg_cake = ["Egg", "Baking soda", "vanilla", "maida"]

        print(ingredients_egg_cake, "are the ingredients of Egg cake")

        return func(*args, **kwargs)

    return wrapper


@decorator_egg_less_cake
def egg_less_cake(soda="defaultsoda"):
    print(f"Making egg less cake with {soda}")


@decorator_egg_cake
def egg_cake(numofeggs="1", pork="defaultpork"):
    print(f"Making cake with egg of quantity {numofeggs} and {pork}")


def choice():
  for i in range(3):

    print("Enter 1 for egg_cake and 2 for egg_less_cake")

    option = int(input("Enter the choice"))
    if option == 1:
      egg_cake("2", "yes")
    elif option == 2:
      egg_less_cake("soda")
    else:
        print("Invalid choice")


choice()


