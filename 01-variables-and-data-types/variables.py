# Python Comments

# This is a single-line comment

# These are multi-lines comment
# but are just separated with 
# hash tags

# We can uncomment multiple comments using (Ctrt + /)


# Python Variables

# Python variables follows snake_casing or using underscore in each subsequent word.

# Example:
# first_name 
# last_name
# is_active

first_name = "Lau"
last_name = "Dev"

print(first_name)
print(last_name)



# Outputing Variables

# We use print() function to output something. 
# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

birthday = 1999
name = "Laurence"

# This will result to an error since we are concatenating string integer (using + opearting)
# print(" I am " + name + ". Born on " + birthday) 

# But we can also use comma (,) to output something with different datatypes

print("I am ", name, '. Born on', birthday)
