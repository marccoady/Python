
#!/usr/bin/env python3.7

# In python a string, is shortened to str and refers to anything inside quotes. The quotes can be double or single. The examples below are identical to python.

"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'

# If you want to include a direct quote in your sentence, then use single quotes for the string and double quotes for the direct quote. For example:

'The error message was "Incorrect DataType"'

# This allows you the flexibility to use single quotes to wrap the string and double quotes inside the string for a direct quote, without python getting confused.

# Strings, like all data types, can be assigned to a variable.

>>>first_name = "Monty"
>>>last_name = "Python"

# You can add strings together using variables. This concatenates them.

>>>print(first_name+last_name)
MontyPython

# In this method you can use the {} in your string to indicate where the variable should go. Then use .format(variable_name) after the quotation marks. If you have multiple variables, for each variable you use a {}. In the .format() separate each variable with a comma. For example .format(variable_1, variable_2).

first_name = "john"
surname = "Doe"

print("My first name is{}. My famly name is {}".format(first_name, surname))

# Since python version 3.6 it has been possible to use a format called f-strings to include variables in your strings. Some people find this format easier to read.

firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")