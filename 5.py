
print("***** BOOLEAN OPERATORS *****")
name = "John"
age = 17
# checks that either name equals to "John" OR age equals to 17
print(name == "John" or age == 17)

# operator orders: NOT first, then AND, then OR last
print(name == "John" or not age > 16)
print(name == "John" and not age > 16)

# ---------------- OUTPUT ----------------
# ***** BOOLEAN OPERATORS *****
# True
# True
# False


print("***** IF STATEMENT *****")
if name == "John" or age == 17:
    print("name is %s" % name)
    print("%s is %d years old" % (name, age))

task = ["task1", "task2"]
if len(task) == 0:
    print("List Empty")
elif len(task) == 1:
    print("single record")
else:
    print("length %d" % len(task))

# ---------------- OUTPUT ----------------
# name is John
# John is 17 years old
# length 2
