
print("***** FOR LOOP *****")
for i in range(5):
    print(i)

primes = [2, 3, 5, 7]
for i in range(len(primes)):
    print("index %d " % primes[i])

# ---------------- OUTPUT ----------------
# ***** For loop *****
# 0
# 1
# 2
# 3
# 4
# index 2
# index 3
# index 5
# index 7


print("***** FOR LOOP USING STRING *****")
hello_world = "Hello, World!"

# print each character
for ch in hello_world:
    print(ch)

# count how many character using for loop
length = 0
for ch in hello_world:
    length += 1
print("number of characters %d " % length)

# ---------------- OUTPUT ----------------
# ***** FOR LOOP USING STRING *****
# H
# e
# l
# l
# o
# ,
#
# W
# o
# r
# l
# d
# !
# number of characters 13


print("***** WHILE LOOP *****")
square = 1

# print 1 to 10
while square <= 10:
    print(square)
    square += 1

# print square 1 to 100 with power ** (1, 4, 16...)
number = 1
while square <= 99:
    square = number ** 2
    print("square %d" % square)
    number += 1


# ---------------- OUTPUT ----------------
# ***** WHILE LOOP *****
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# square 1
# square 4
# square 9
# square 16
# square 25
# square 36
# square 49
# square 64
# square 81
# square 100


print("***** BREAK *****")
count = 0

# logically this cannot be False
while True:
    print(count)
    count += 1
    if count >= 5:
        # exit loop
        break

zoo = ["lion", 'tiger', 'elephant']

# logically this cannot be False
while True:
    # pop: return last item in the list
    animal = zoo.pop()
    print(animal)
    if animal == "lion":
        break

# ---------------- OUTPUT ----------------
# ***** BREAK *****
# 0
# 1
# 2
# 3
# 4
# elephant
# tiger
# lion


print("***** CONTINUE *****")
for i in range(5):
    if i == 3:
        # skip the rest of the code and move to the next loop
        continue
    print(i)

# print only odd numbers
for x in range(10):
    if (x % 2) == 0:
        # skip print(x) for this loop
        continue
    print("event number %d" % x)

# ---------------- OUTPUT ----------------
# ***** CONTINUE *****
# 0
# 1
# 2
# 4
# event number 1
# event number 3
# event number 5
# event number 7
# event number 9
