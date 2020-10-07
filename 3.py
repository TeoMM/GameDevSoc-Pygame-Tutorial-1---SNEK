
print("***** CONCATENATION *****")
hello = "Hello"
world = 'World'
hello_world = hello + " " + world

print(hello_world)

# ---------------- OUTPUT ----------------
# Hello World


print("***** STRING-BY-NUMBER MULTIPLICATION *****")
hello = "hello"
ten_of_hellos = hello * 10
print(ten_of_hellos)

# ---------------- OUTPUT ----------------
# hellohellohellohellohellohellohellohellohellohello


print("***** INDEXING *****")
python = "This is a python string!"

# string indexing starts with 0
print(python[2])

# use -1 to get the last letter
print(python[-1])

# ---------------- OUTPUT ----------------
# i
# !


print("***** SLICING *****")
python_developer = "Python Developer"

# string[start:end]
print(python_developer[:6])
print(python_developer[7:])
print(python_developer[4:10])
print(python_developer[:])

# ---------------- OUTPUT ----------------
# Python
# Developer
# on Dev
# Python Developer


print("***** IN OPERATOR *****")
ice_cream = "Ice Cream"

# check if string contains cream
print("ream" in ice_cream)

# ---------------- OUTPUT ----------------
# True


print("***** LENGTH *****")
print(len(ice_cream))

# ---------------- OUTPUT ----------------
# 9

print("***** ESCAPING *****")


print("\"Sweet\"" + ice_cream)
print('\"Sweet\"' + ice_cream)
print("Sweet\n" + ice_cream)        # new line

# ---------------- OUTPUT ----------------
# "Sweet"ice cream
# "Sweet"ice cream
# Sweet
# ice cream


print("***** LOWER / UPPER *****")
print(ice_cream.lower())
print(ice_cream.upper())

# ---------------- OUTPUT ----------------
# ice cream
# ICE CREAM


print("***** FORMATTING *****")
name = "Peter"
integer = 5
decimal = 9.0
print("Hello, PyCharm! My name is %s!\nMy favourite numbers: Integer(%d) and Decimal(%d)" %
      (name, integer, decimal))

# ---------------- OUTPUT ----------------
# Hello, PyCharm! My name is Peter!
# My favourite numbers: Integer(5) and Decimal(9)
