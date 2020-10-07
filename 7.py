print("***** FUNCTION DEFINITION *****")

# define a function name hello_world


def hello_world():
    print("Hello, World!")


# call the function 5 times
for i in range(5):
    hello_world()

# ---------------- OUTPUT ----------------
# ***** FUNCTION DEFINITION *****
# Hello, World!
# Hello, World!
# Hello, World!
# Hello, World!
# Hello, World!


print("***** FUNCTION WITH PARAMETERS AND ARG *****")

# x is a parameter


def foo(x):
    print("x = %d" % x)


# pass 5 to the function parameter. Here 5 is an arg.
foo(5)

# ---------------- OUTPUT ----------------
# ***** FUNCTION WITH PARAMETERS AND ARG *****
# x = 5


print("***** FUNCTION WITH RETURN *****")

# function that return sum or 2 numbers


def sum_two_numbers(a, b):
    return a + b


c = sum_two_numbers(3, 12)
print("c = %d" % c)

# ---------------- OUTPUT ----------------
# ***** FUNCTION WITH RETURN *****
# c = 15


print("***** FUNCTION WITH DEFAULT PARAMETER *****")


def multiply_by(a, b=2):
    return a * b


print(multiply_by(3, 47))

# single arg can be passed
print(multiply_by(3))

# ---------------- OUTPUT ----------------
# ***** FUNCTION WITH DEFAULT PARAMETER *****
# 141
# 6
