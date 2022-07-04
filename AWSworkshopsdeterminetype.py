my_variable = "A String"
print(type(my_variable))

# Here is an example of a TypeError below.

#my_number = 50
#some_string = "The number is "
#print(some_string + my_number)

# Here is how we can fix the TypeError by telling python to convert my_number to a string

my_number = 50
some_string = "The number is "
print(some_string + str(my_number))


