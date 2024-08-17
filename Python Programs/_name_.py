# Imagine you have two toy boxes: Toy Box A and Toy Box B. When you're playing with your toys, you usually play with Toy Box A. But sometimes, you let your friend play with Toy Box B.
#
# Now, there's a special sticker on each toy box:
#
# When you're playing with Toy Box A, the sticker says "Main Toy Box".
# When your friend is playing with Toy Box B, the sticker on Toy Box B says "Friend's Toy Box".
# In Python, the __name__ variable is like that sticker. When you('re running your own'
# ' program (playing with Toy Box A), the __name__ variable will be "__main__", which means '
# '"Main Toy Box". But when someone else is using your program '
# '(like your friend playing with Toy Box B), __name__ will have a different name, like "Toy Box B".)

#FILE -->my_toys.py
def play_with_toys():
    print("I'm playing with my toys!")

if __name__ == "__main__":
    print("This is my main toy box!")
    play_with_toys()
#
# But,
# if your friend (another program) wants to use the toys in your toy box,
# they can import your toys (your file) and use them, like this:

# friend_toys.py
#import my_toys

#print("Friend is playing with your toys!")

# When you run friend_toys.py, it will not print "This is my main toy box!"
# because my_toys.py is being used by another file. It will only print:
# Friend is playing with your toys!
