# Variables

print("***** DEFINITION AND TYPES *****")
var_string = "Hello!"
var_number = 9
var_float = 9.0

print(var_string)
print(var_number)
print(var_float)

print(type(var_number))
print(type(var_float))

# ---------------- OUTPUT ----------------
# Hello!
# 9
# 9.0
# <class 'int'>
# <class 'float'>


print("***** CONVERSION *****")
print(var_float)
print(int(var_float))          # Convert to int
print(str(var_float))          # Convert to string

# ---------------- OUTPUT ----------------
# ***** CONVERSION *****
# 9.0
# 9
# 9.0


print("***** ARITHMETIC OPERATORS *****")
result = var_float / 3            # Division Operator (/)
remainder = var_float - result    # Subtraction Operator (-)
multiplication = var_float * 5    # Multiplication Operator (*)
power = var_float ** 2            # Power Operator (**)
modulo = var_float % 4            # modulo Operator (%)

print("result = " + str(result))
print("remainder = " + str(remainder))
print("multiplication = " + str(multiplication))
print("power = " + str(power))
print("modulo = " + str(modulo))

# ---------------- OUTPUT ----------------
# ***** ARITHMETIC OPERATORS *****
# result = 3.0
# remainder = 6.0
# multiplication = 45.0
# power = 81.0
# modulo = 1.0


print("***** ASSIGNMENTS *****")
var_float -= 2
print("Assignment -= 2 equals " + str(var_float))

var_float += 5
print("Assignment += 5 equals " + str(var_float))

# ---------------- OUTPUT ----------------
# ***** ASSIGNMENTS *****
# Assignment -= 2 equals 7.0
# Assignment += 5 equals 12.0


print("***** BOOLEAN OPERATORS *****")
one = 1
two = 2
three = 3

is_equal = two == three
not_equal = two != three

print(is_equal)
print(not_equal)

# ---------------- OUTPUT ----------------
# ***** BOOLEAN OPERATORS *****
# False
# True


print("***** COMPARAISON OPERATORS *****")
print(one < two < three)

is_greater = three > two
print(is_greater)

# ---------------- OUTPUT ----------------
# ***** COMPARAISON OPERATORS *****
# True
# True
