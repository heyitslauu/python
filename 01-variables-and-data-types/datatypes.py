# Unlike other languages, Python do not need to be declared with any particular type, 
# and can even change type after they have been set.

# Data types and Type Casting

# There are different datatypes such as:
# int, float, list, bool, range, set

age = str(24);
price = float(10);

print(age) # Will return '24' since it is converted into string
print(type(age)) # Will return class of 'str'

print(price) # Will return 10.0  since it is converted to floating point
print(type(price))  # Will return class of 'float'

# Another type casting example:

birth_year = input("Hi, what's your birth year? ");

# age = 2023 - birth_year

# print(age) 
#This will produce an error since birth_year is a string, so we need to convert it

age = 2023 - int(birth_year)

print(age)