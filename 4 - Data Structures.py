
print("***** LISTS (ARRAY) *****")
squares = [1, 4, 9, 16, 25]
print(squares)

# ---------------- OUTPUT ----------------
# ***** LISTS (ARRAY) *****
# [1, 4, 9, 16, 25]


print("***** LISTS OPERATIONS *****")
animals = ['elephant', 'lion', 'tiger', "giraffe"]

# add 2 items to the list
animals += ["monkey", 'dog']
print(animals)

# add 1 items to the list using append
animals.append("dino")
print(animals)

# ---------------- OUTPUT ----------------
# ***** LISTS OPERATIONS *****
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog']
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog', 'dino']


print("***** LIST ITEMS *****")
# replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
animals[1:3] = ['cat']
print(animals)

# remove 2 items -- 'cat' and 'giraffe' from the list
animals[1:3] = []
print(animals)

# ---------------- OUTPUT ----------------
# ***** LIST ITEMS *****
# ['elephant', 'cat', 'giraffe', 'monkey', 'dog', 'dino']
# ['elephant', 'monkey', 'dog', 'dino']


print("***** TUPLES *****")
# Tuples are similar to lists but immutable. You cannot add, change or delete items from tuples
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
print(alphabet)

# ---------------- OUTPUT ----------------
# ***** TUPLES *****
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


print("***** DICTIONARIES *****")
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book['John']
print(phone_book)

# Read specific key value
print("Jill's Phone: %s" % (phone_book["Jill"]))

# check that phone_book contains "Jane" item
print("Jane" in phone_book)

# ---------------- OUTPUT ----------------
# ***** DICTIONARIES *****
# {'John': 123, 'Jane': 234, 'Jerard': 345}
# {'John': 123, 'Jane': 234, 'Jerard': 345, 'Jill': 345}
# {'Jane': 234, 'Jerard': 345, 'Jill': 345}
# Jill's Phone: 345
# True
