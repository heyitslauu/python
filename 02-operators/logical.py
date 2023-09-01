'''
Logical operators are used to combine conditional statements:

The logical operators are:
and -> Returns True if BOTH statements are True
or -> Returns True if at least one of the statements are True
not -> Reverses the result of the initial statements (Initial value ofTrue will became False)
'''


grade = 80

print(grade > 70 and grade < 79) #Returs False since 80 is greater than 79
print(grade > 70 or grade < 79) #Return True since one of the statements is True
print(not(grade > 70 and grade < 79)) #Returns True since it reversed the initial value: False